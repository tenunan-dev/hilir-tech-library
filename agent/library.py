"""Search index over the catalog and the corpus, shared by the MCP server and the CLI.

The index is a SQLite file (build/library.db, not committed) with:
  sources   one row per catalog record
  docs      one row per corpus document, with its front matter
  search    FTS5 table over catalog records and corpus chunks
  vectors   optional embeddings per search row (see agent/embed.py)

Rebuild it with `python agent/library.py build` after the catalog or corpus changes.
"""
import json
import pathlib
import re
import sqlite3
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
DB_PATH = ROOT / "build" / "library.db"
CHUNK_CHARS = 1200
# Asia Pacific and Southeast Asia sources rank slightly higher, per the library's regional focus.
REGION_BOOST = {"sea": 1.25, "apac": 1.15}
COUNTRIES = {
    "AE": "United Arab Emirates", "AU": "Australia", "BE": "Belgium", "BG": "Bulgaria", "BN": "Brunei",
    "CH": "Switzerland", "CN": "China", "DE": "Germany", "DK": "Denmark", "FI": "Finland", "FR": "France",
    "GB": "United Kingdom UK", "ID": "Indonesia", "IN": "India", "IT": "Italy", "JP": "Japan", "KR": "Korea",
    "MM": "Myanmar", "MY": "Malaysia", "NL": "Netherlands", "NO": "Norway", "PH": "Philippines", "QA": "Qatar",
    "SA": "Saudi Arabia", "SE": "Sweden", "SG": "Singapore", "TH": "Thailand", "US": "United States USA",
    "VN": "Vietnam", "INT": "International",
}
# BM25 weights per column (kind, ref, source_id, title, text, tags): a match in the name or text
# counts more than one in the taxonomy labels every record of a sector shares.
BM25 = "bm25(search, 0, 0, 0, 3.0, 1.0, 0.4)"


def taxonomy_labels():
    tax = yaml.safe_load((ROOT / "taxonomy.yaml").read_text(encoding="utf-8"))
    labels = {code: info["name"] for code, info in {**tax["sectors"], **tax["disciplines"]}.items()}
    labels.update(tax["regions"])
    return labels


def connect(path=None):
    # Read-mostly and shared by the MCP server's worker threads.
    db = sqlite3.connect(path or DB_PATH, check_same_thread=False)
    db.row_factory = sqlite3.Row
    return db


def load_records():
    path = ROOT / "catalog" / "catalog.jsonl"
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def read_document(path):
    """Split a corpus Markdown file into (front matter dict, body)."""
    text = pathlib.Path(path).read_text(encoding="utf-8")
    meta, body = {}, text
    if text.startswith("---\n"):
        head, _, body = text[4:].partition("\n---\n")
        for line in head.splitlines():
            key, _, value = line.partition(": ")
            try:
                meta[key] = json.loads(value)
            except json.JSONDecodeError:
                meta[key] = value
    return meta, body.strip()


def chunk(body, size=CHUNK_CHARS):
    """Group paragraphs into chunks of roughly `size` characters."""
    chunks, current = [], ""
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if not para:
            continue
        if current and len(current) + len(para) > size:
            chunks.append(current)
            current = ""
        current = f"{current}\n\n{para}" if current else para
    return chunks + ([current] if current else [])


def source_text(rec):
    return "\n".join(p for p in (rec["publisher_org"], rec.get("notes", ""), rec["source_type"]) if p)


def tag_text(meta, labels):
    """Codes plus their names, country and region names, so "LNG Malaysia" reaches GAS records in MY."""
    codes = meta.get("sectors", []) + meta.get("disciplines", []) + meta.get("regions", [])
    return " ".join(codes + [labels.get(c, "") for c in codes] + [COUNTRIES.get(meta.get("country"), "")])


def build(db_path=None, corpus=None):
    corpus = pathlib.Path(corpus or CORPUS)
    db_path = pathlib.Path(db_path or DB_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()
    db = connect(db_path)
    db.executescript("""
        CREATE TABLE sources (id TEXT PRIMARY KEY, record TEXT NOT NULL);
        CREATE TABLE docs (path TEXT PRIMARY KEY, source_id TEXT, title TEXT, url TEXT, meta TEXT);
        CREATE VIRTUAL TABLE search USING fts5(kind UNINDEXED, ref UNINDEXED, source_id UNINDEXED,
                                               title, text, tags, tokenize='porter unicode61');
        CREATE TABLE vectors (rowid INTEGER PRIMARY KEY, vec BLOB NOT NULL);
        CREATE TABLE info (key TEXT PRIMARY KEY, value TEXT);
    """)
    records = load_records()
    labels = taxonomy_labels()
    by_id = {r["id"]: r for r in records}
    for rec in records:
        db.execute("INSERT INTO sources VALUES (?, ?)", (rec["id"], json.dumps(rec, ensure_ascii=False)))
        db.execute("INSERT INTO search VALUES ('source', ?, ?, ?, ?, ?)",
                   (rec["id"], rec["id"], rec["name"], source_text(rec), tag_text(rec, labels)))
    n_docs = n_chunks = 0
    for path in sorted(corpus.glob("*/*.md")):
        if path.parent.name.startswith("_"):
            continue
        meta, body = read_document(path)
        rel = str(path.relative_to(corpus.parent))
        db.execute("INSERT INTO docs VALUES (?, ?, ?, ?, ?)",
                   (rel, meta.get("source_id"), meta.get("title"), meta.get("url"), json.dumps(meta, ensure_ascii=False)))
        tags = tag_text({**meta, "regions": by_id.get(meta.get("source_id"), {}).get("regions", [])}, labels)
        for i, text in enumerate(chunk(body)):
            db.execute("INSERT INTO search VALUES ('chunk', ?, ?, ?, ?, ?)",
                       (f"{rel}#{i}", meta.get("source_id"), meta.get("title"), text, tags))
            n_chunks += 1
        n_docs += 1
    db.execute("INSERT INTO info VALUES ('root', ?)", (str(corpus.parent),))
    db.commit()
    return {"sources": len(records), "documents": n_docs, "chunks": n_chunks}


def fts_query(text):
    """Any of the query's words; BM25 already ranks rows that match more of them higher."""
    return " OR ".join(f'"{t}"' for t in re.findall(r"\w+", text.lower()))


def _matches(rec, sector, discipline, region, reuse_level):
    return ((not sector or sector in rec["sectors"]) and (not discipline or discipline in rec["disciplines"])
            and (not region or region in rec["regions"]) and (not reuse_level or rec["reuse_level"] == reuse_level))


def doc_restricted(db, path, rec):
    row = db.execute("SELECT meta FROM docs WHERE path = ?", (path,)).fetchone()
    meta = json.loads(row["meta"]) if row else {}
    return meta.get("reuse_level", rec["reuse_level"]) == "full-text-restricted"


def _result(db, row, score, records):
    rec = records[row["source_id"]]
    out = {"kind": row["kind"], "ref": row["ref"], "source_id": rec["id"], "title": row["title"], "score": round(score, 4),
           "licence": rec["licence"], "reuse_level": rec["reuse_level"], "permitted_use": rec.get("permitted_use", "unstated")}
    if row["kind"] == "source":
        out.update(url=rec["url"], regions=rec["regions"], sectors=rec["sectors"], disciplines=rec["disciplines"])
    else:
        path = row["ref"].split("#")[0]
        doc = db.execute("SELECT url, meta FROM docs WHERE path = ?", (path,)).fetchone()
        meta = json.loads(doc["meta"]) if doc else {}
        out.update({k: meta[k] for k in ("licence", "reuse_level", "permitted_use") if k in meta})
        out.update(path=path, url=doc["url"] if doc else None, snippet=row["text"][:400])
        if doc_restricted(db, path, rec):
            out["use_note"] = "Private reference copy. Do not redistribute or use commercially; cite the url."
    return out


def search(query, kind="all", sector=None, discipline=None, region=None, reuse_level=None, limit=10,
           db=None, embedder=None, exclude_restricted=False):
    """Keyword search (BM25), fused with vector search when vectors and an embedder are available.

    exclude_restricted drops passages from full-text-restricted sources (catalog records stay),
    for servers that other people can reach.
    """
    db = db or connect()
    records = {r["id"]: json.loads(r["record"]) for r in db.execute("SELECT * FROM sources")}
    kinds = ("source", "chunk") if kind == "all" else (kind,)
    q = fts_query(query)
    if not q:
        return []
    rows = db.execute(f"SELECT rowid, kind, ref, source_id, title, text, tags, {BM25} AS rank FROM search "
                      "WHERE search MATCH ? ORDER BY rank LIMIT 500", (q,)).fetchall()
    # Rows matching more of the query's words come first; BM25 orders rows within each group.
    terms = set(re.findall(r"\w+", query.lower()))
    rows.sort(key=lambda r: (-sum(t in f"{r['title']} {r['text']} {r['tags']}".lower() for t in terms), r["rank"]))
    ranked = {}
    for pos, row in enumerate(rows):
        ranked[row["rowid"]] = [row, 1.0 / (60 + pos)]
    if embedder is not None and db.execute("SELECT count(*) FROM vectors").fetchone()[0]:
        import numpy as np
        qvec = np.asarray(embedder([query])[0], dtype=np.float32)
        ids, vecs = zip(*((r[0], np.frombuffer(r[1], dtype=np.float32)) for r in db.execute("SELECT rowid, vec FROM vectors")))
        sims = np.stack(vecs) @ qvec
        for pos, idx in enumerate(np.argsort(-sims)[:200]):
            rowid = ids[idx]
            if rowid not in ranked:
                row = db.execute("SELECT rowid, kind, ref, source_id, title, text FROM search WHERE rowid = ?", (rowid,)).fetchone()
                ranked[rowid] = [row, 0.0]
            ranked[rowid][1] += 1.0 / (60 + pos)
    results = []
    for row, score in ranked.values():
        rec = records.get(row["source_id"])
        if not rec or row["kind"] not in kinds or not _matches(rec, sector, discipline, region, reuse_level):
            continue
        if exclude_restricted and row["kind"] == "chunk" and doc_restricted(db, row["ref"].split("#")[0], rec):
            continue
        boost = max([REGION_BOOST.get(g, 1.0) for g in rec["regions"]] + [1.0])
        results.append((score * boost, row, rec))
    results.sort(key=lambda t: -t[0])
    return [_result(db, row, score, records) for score, row, _ in results[:limit]]


def get_source(source_id, db=None, exclude_restricted=False):
    db = db or connect()
    row = db.execute("SELECT record FROM sources WHERE id = ?", (source_id,)).fetchone()
    if not row:
        return None
    rec = json.loads(row["record"])
    docs = [dict(d) for d in db.execute("SELECT path, title, url FROM docs WHERE source_id = ? ORDER BY path", (source_id,))]
    rec["documents"] = [d for d in docs if not (exclude_restricted and doc_restricted(db, d["path"], rec))]
    return rec


def get_document(path, db=None, exclude_restricted=False):
    db = db or connect()
    row = db.execute("SELECT d.path, s.record FROM docs d JOIN sources s ON s.id = d.source_id WHERE d.path = ?",
                     (path.split("#")[0],)).fetchone()
    if not row:
        return None
    if exclude_restricted and doc_restricted(db, row["path"], json.loads(row["record"])):
        return {"path": row["path"], "error": "Private reference copy; not served by this server. Cite the source url instead."}
    root = db.execute("SELECT value FROM info WHERE key = 'root'").fetchone()
    meta, body = read_document(pathlib.Path(root[0] if root else ROOT) / row["path"])
    return {"path": row["path"], "meta": meta, "text": body}


def list_by_tag(code=None, region=None, reuse_level=None, source_type=None, db=None):
    db = db or connect()
    out = []
    for r in db.execute("SELECT record FROM sources ORDER BY id"):
        rec = json.loads(r["record"])
        if code and code not in rec["sectors"] + rec["disciplines"]:
            continue
        if not _matches(rec, None, None, region, reuse_level) or (source_type and rec["source_type"] != source_type):
            continue
        out.append({k: rec[k] for k in ("id", "name", "url", "source_type", "regions", "reuse_level", "quality_tier")})
    out.sort(key=lambda r: (not ({"sea", "apac"} & set(r["regions"])), r["quality_tier"], r["name"].lower()))
    return out


def stats(db=None):
    db = db or connect()
    return {"sources": db.execute("SELECT count(*) FROM sources").fetchone()[0],
            "documents": db.execute("SELECT count(*) FROM docs").fetchone()[0],
            "chunks": db.execute("SELECT count(*) FROM search WHERE kind = 'chunk'").fetchone()[0],
            "vectors": db.execute("SELECT count(*) FROM vectors").fetchone()[0],
            "embedding_model": (db.execute("SELECT value FROM info WHERE key = 'model'").fetchone() or [None])[0]}


if __name__ == "__main__":
    if sys.argv[1:2] == ["build"]:
        print(json.dumps(build()))
    elif sys.argv[1:2] == ["search"]:
        for hit in search(" ".join(sys.argv[2:])):
            print(f"{hit['score']:.4f}  {hit['kind']:6}  {hit['source_id']:24}  {hit['title']}")
    else:
        print("usage: python agent/library.py build | search <query>")
