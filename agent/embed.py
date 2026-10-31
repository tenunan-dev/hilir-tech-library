"""Add embeddings to the search index so search() can fuse keyword and vector results.

    pip install -r requirements-agent.txt fastembed
    python agent/library.py build && python agent/embed.py                  # full re-embed
    python agent/library.py build && python agent/embed.py --incremental    # only new/changed rows

--incremental keeps vectors cached by (kind, ref) and the embedding input's hash in
build/embed-cache.db, so after a rebuild only rows whose text changed get re-embedded —
a one-supplier publish re-embeds one row instead of the whole index (decision #34, R6).
--kind and --ref narrow a run to one kind or specific refs (by-id); unfiltered runs still
reuse the cache for every unchanged row. A different --model wipes the cache.

fastembed runs a small ONNX model on the CPU; it downloads the model once on first use.
The default is English; pass --model for a multilingual one, e.g.
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 for Bahasa, Thai, Vietnamese or Chinese text.
"""
import argparse
import hashlib
import pathlib
import sqlite3
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import library  # noqa: E402

DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"
CACHE = pathlib.Path(__file__).resolve().parent.parent / "build" / "embed-cache.db"


def _cache(path):
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE IF NOT EXISTS cache (kind TEXT NOT NULL, ref TEXT NOT NULL, hash TEXT NOT NULL, vec BLOB NOT NULL, PRIMARY KEY (kind, ref))")
    db.execute("CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT)")
    db.commit()
    return db


def _hash(title, text) -> str:
    return hashlib.sha256(f"{title or ''}\n{text or ''}".encode("utf-8")).hexdigest()


def _normalize(vec):
    import numpy as np
    vec = np.asarray(vec, dtype=np.float32)
    return (vec / np.linalg.norm(vec)).tobytes()


def _model(name):
    from fastembed import TextEmbedding
    return TextEmbedding(model_name=name)


def embed_index(db, model_name=DEFAULT_MODEL, model=None, batch=64, cache_path=None):
    """Embed every search row into `vectors`; with cache_path the vectors also go into the
    (kind, ref)-keyed cache so the next --incremental run reuses everything (the CLI passes it)."""
    import numpy as np
    model = model or _model(model_name)
    rows = db.execute("SELECT rowid, title, text FROM search").fetchall()
    db.execute("DELETE FROM vectors")
    cache = _cache(cache_path) if cache_path else None
    if cache is not None:
        stored = cache.execute("SELECT value FROM meta WHERE key = 'model'").fetchone()
        if stored and stored[0] != model_name:
            cache.execute("DELETE FROM cache")
        cache.execute("INSERT OR REPLACE INTO meta VALUES ('model', ?)", (model_name,))
    for start in range(0, len(rows), batch):
        part = rows[start:start + batch]
        vecs = model.passage_embed([f"{r['title']}\n{r['text']}" for r in part])
        for row, vec in zip(part, vecs):
            blob = _normalize(vec)
            db.execute("INSERT INTO vectors VALUES (?, ?)", (row["rowid"], blob))
            if cache is not None:
                kind, ref = db.execute("SELECT kind, ref FROM search WHERE rowid = ?", (row["rowid"],)).fetchone()
                cache.execute("INSERT OR REPLACE INTO cache VALUES (?, ?, ?, ?)",
                              (kind, ref, _hash(row["title"], row["text"]), blob))
    db.execute("INSERT OR REPLACE INTO info VALUES ('model', ?)", (model_name,))
    db.commit()
    if cache is not None:
        cache.commit()
    return len(rows)


def embed_incremental(db, model_name=DEFAULT_MODEL, model=None, batch=64, cache_path=None,
                      kind=None, ref=None):
    """Embed only rows whose (kind, ref) is missing from the cache or whose embedding input
    (title + text) changed; every other row's vector is reused from the cache. kind narrows the
    embedding work to one kind, ref (comma-separated) to specific refs — rows outside the filter
    still get their cached vector, so the vectors table ends up fully populated either way.
    Returns {embedded, reused, missing, total}."""
    model = model or _model(model_name)
    cache = _cache(cache_path or CACHE)
    stored = cache.execute("SELECT value FROM meta WHERE key = 'model'").fetchone()
    wiped = bool(stored) and stored[0] != model_name
    if wiped:
        cache.execute("DELETE FROM cache")  # a different model invalidates every cached vector
    cache.execute("INSERT OR REPLACE INTO meta VALUES ('model', ?)", (model_name,))

    all_rows = db.execute("SELECT rowid, kind, ref, title, text FROM search").fetchall()
    wanted = {r.strip() for r in ref.split(",")} if ref else None
    rows = [r for r in all_rows if (not kind or r["kind"] == kind) and (not wanted or r["ref"] in wanted)]
    cached = {(k, r): (h, vec) for k, r, h, vec in cache.execute("SELECT kind, ref, hash, vec FROM cache")}
    if not wiped and any((r["kind"], r["ref"]) not in cached for r in rows):
        # First run against an index embedded before the cache existed (or after a filtered
        # run): adopt the vectors table's rows into the cache instead of re-embedding. Safe
        # because adoption only finds vectors when the rowids still belong to the same build
        # (a rebuild clears the vectors table), so the vectors match the current text.
        with_vec = dict(db.execute("SELECT rowid, vec FROM vectors").fetchall())
        for row in all_rows:
            if (row["kind"], row["ref"]) not in cached and row["rowid"] in with_vec:
                cache.execute("INSERT OR REPLACE INTO cache VALUES (?, ?, ?, ?)",
                              (row["kind"], row["ref"], _hash(row["title"], row["text"]), with_vec[row["rowid"]]))
        cached = {(k, r): (h, vec) for k, r, h, vec in cache.execute("SELECT kind, ref, hash, vec FROM cache")}

    todo = []  # rows the cache cannot answer: new, or with changed text
    for row in rows:
        hit = cached.get((row["kind"], row["ref"]))
        if not hit or hit[0] != _hash(row["title"], row["text"]):
            todo.append(row)
    vecs = {}
    for start in range(0, len(todo), batch):
        part = todo[start:start + batch]
        for row, vec in zip(part, model.passage_embed([f"{r['title']}\n{r['text']}" for r in part])):
            vecs[(row["kind"], row["ref"])] = _normalize(vec)

    db.execute("DELETE FROM vectors")
    embedded = reused = missing = 0
    for row in all_rows:
        key = (row["kind"], row["ref"])
        blob = vecs.get(key)
        if blob is not None:
            cache.execute("INSERT OR REPLACE INTO cache VALUES (?, ?, ?, ?)",
                          (key[0], key[1], _hash(row["title"], row["text"]), blob))
            embedded += 1
        else:
            hit = cached.get(key)
            if hit:
                blob = hit[1]
                reused += 1
            else:
                missing += 1
        if blob is not None:
            db.execute("INSERT INTO vectors VALUES (?, ?)", (row["rowid"], blob))
    for (k, r) in list(cached):  # rows removed from the index leave the cache
        if (k, r) not in {(x["kind"], x["ref"]) for x in all_rows}:
            cache.execute("DELETE FROM cache WHERE kind = ? AND ref = ?", (k, r))
    db.commit()
    cache.commit()
    return {"embedded": embedded, "reused": reused, "missing": missing, "total": len(all_rows)}


def load_embedder(db):
    """Return a query embedder matching the index's model, or None when vectors are unavailable."""
    row = db.execute("SELECT value FROM info WHERE key = 'model'").fetchone()
    if not row:
        return None
    try:
        model = _model(row[0])
    except ImportError:
        return None

    def embed(texts):
        import numpy as np
        return [np.asarray(v, dtype=np.float32) / np.linalg.norm(v) for v in model.query_embed(texts)]
    return embed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--incremental", action="store_true",
                        help="embed only new/changed rows (cache in build/embed-cache.db)")
    parser.add_argument("--kind", help="with --incremental: narrow the embedding work to one kind")
    parser.add_argument("--ref", help="with --incremental: narrow to these refs, comma-separated (by-id)")
    args = parser.parse_args()
    db = library.connect()
    if args.incremental:
        result = embed_incremental(db, args.model, kind=args.kind, ref=args.ref)
        print(f"embedded {result['embedded']}, reused {result['reused']}, missing {result['missing']} "
              f"of {result['total']} rows ({args.model})")
    else:
        print(f"{embed_index(db, args.model, cache_path=CACHE)} rows embedded with {args.model}")
