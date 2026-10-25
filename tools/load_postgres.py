"""Load the library into Postgres (pgvector) with a knowledge graph, for Neon or any Postgres 15+.

    pip install -r requirements-postgres.txt
    export DATABASE_URL='postgresql://user:password@host/dbname?sslmode=require'   # never commit this
    python tools/load_postgres.py                    # open-licence text only, embeddings from build/library.db if present
    python tools/load_postgres.py --embeddings fastembed    # compute embeddings here (needs fastembed)
    python tools/load_postgres.py --include-restricted      # only for a database nobody else can read
    python tools/load_postgres.py --dump-graph build/graph  # write nodes.jsonl and edges.jsonl, no database needed

The load replaces the contents of every table in schema `og` inside one transaction, so a failed load
leaves the previous data. See docs/POSTGRES.md.
"""
import argparse
import json
import os
import pathlib
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "agent"))
import graph  # noqa: E402
import library  # noqa: E402
import technologies  # noqa: E402

SCHEMA = ROOT / "db" / "schema.sql"
TABLES = ["edge", "node", "register_entry", "technology_gap", "technology_supplier", "technology_figure",
          "technology_source", "technology_alias", "technology", "chunk", "document", "source_tag", "source"]
DIM = 384


def vec_text(vec):
    """pgvector text form, so no client-side adapter is needed."""
    return "[" + ",".join(f"{float(x):.6g}" for x in vec) + "]"


def sqlite_vectors(db_path):
    """{(kind, ref): vector} from the SQLite index built by agent/embed.py, or {} if it has none."""
    import numpy as np
    if not pathlib.Path(db_path).exists():
        return {}
    db = sqlite3.connect(db_path)
    try:
        rows = db.execute("SELECT s.kind, s.ref, v.vec FROM search s JOIN vectors v ON v.rowid = s.rowid").fetchall()
    except sqlite3.Error:
        return {}
    out = {}
    for kind, ref, blob in rows:
        vec = np.frombuffer(blob, dtype=np.float32)
        if len(vec) == DIM:
            out[(kind, ref)] = vec
    return out


def fastembed_vectors(items):
    """items: [(kind, ref, text)] -> {(kind, ref): vector}."""
    import numpy as np
    from fastembed import TextEmbedding
    model = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")
    out = {}
    for start in range(0, len(items), 64):
        part = items[start:start + 64]
        for (kind, ref, _), vec in zip(part, model.passage_embed([t for _, _, t in part])):
            vec = np.asarray(vec, dtype=np.float32)
            out[(kind, ref)] = vec / np.linalg.norm(vec)
    return out


def collect(include_restricted=False):
    """Everything to load, as plain Python values."""
    labels = library.taxonomy_labels()
    records = library.load_records()
    by_id = {r["id"]: r for r in records}
    cards = technologies.load_cards()
    entries = technologies.load_register(None, cards)
    docs, chunks = [], []
    for path in sorted(library.CORPUS.glob("*/*.md")):
        if path.parent.name.startswith("_"):
            continue
        meta, body = library.read_document(path)
        meta["sectors"] = library.doc_sectors(meta.get("title", ""), body, meta.get("sectors", []))
        rel = str(path.relative_to(library.ROOT))
        text_ok = include_restricted or meta.get("reuse_level") == "full-text-open"
        docs.append({"id": rel, "source_id": meta.get("source_id") if meta.get("source_id") in by_id else None,
                     "title": meta.get("title"), "url": meta.get("url"), "licence": meta.get("licence"),
                     "reuse_level": meta.get("reuse_level"), "retrieved_at": meta.get("retrieved_at"),
                     "sha256": meta.get("sha256"), "sectors": meta["sectors"], "text_included": text_ok,
                     "summary": meta.get("summary"), "meta": meta})
        if text_ok:
            for i, text in enumerate(library.chunk(body)):
                chunks.append({"id": f"{rel}#{i}", "document_id": rel, "ord": i, "title": meta.get("title"), "body": text})
    return {"labels": labels, "records": records, "cards": cards, "entries": entries, "docs": docs, "chunks": chunks}


def card_search_text(card):
    """Same text the SQLite index embeds for a card."""
    return "\n".join([card["category"], card["principle"], " ".join(card.get("aliases", [])),
                      " ".join(card.get("applications", [])), " ".join(card["key_equipment"]),
                      " ".join(s["name"] + " " + s.get("product", "") for s in card["suppliers"]), card["maturity"]])


def load(conn, data, nodes, edges, vectors):
    """Replace all rows. `conn` is an open psycopg connection; the caller commits."""
    cur = conn.cursor()
    cur.execute(SCHEMA.read_text(encoding="utf-8"))
    cur.execute("SET search_path = og, public")
    cur.execute("TRUNCATE " + ", ".join(TABLES) + " RESTART IDENTITY CASCADE")
    for r in data["records"]:
        cur.execute("""INSERT INTO source (id, name, url, source_type, publisher_org, country, access, licence, reuse_level,
                       permitted_use, automated_access, quality_tier, verification, last_verified, update_frequency, notes, record)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (r["id"], r["name"], r["url"], r["source_type"], r["publisher_org"], r.get("country"), r["access"], r["licence"],
                     r["reuse_level"], r.get("permitted_use"), r.get("automated_access"), r.get("quality_tier"), r["verification"],
                     r.get("last_verified"), r.get("update_frequency"), r.get("notes"), json.dumps(r)))
        for kind, key in (("sector", "sectors"), ("discipline", "disciplines"), ("region", "regions")):
            for code in r.get(key, []):
                cur.execute("INSERT INTO source_tag VALUES (%s,%s,%s)", (r["id"], kind, code))
    for d in data["docs"]:
        cur.execute("""INSERT INTO document (id, source_id, title, url, licence, reuse_level, retrieved_at, sha256, sectors,
                       text_included, summary, meta) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (d["id"], d["source_id"], d["title"], d["url"], d["licence"], d["reuse_level"], d["retrieved_at"], d["sha256"],
                     d["sectors"], d["text_included"], d["summary"], json.dumps(d["meta"])))
    cur.executemany("INSERT INTO chunk (id, document_id, ord, title, body, embedding) VALUES (%s,%s,%s,%s,%s,%s::vector)",
                    [(c["id"], c["document_id"], c["ord"], c["title"], c["body"],
                      vec_text(vectors[("chunk", c["id"])]) if ("chunk", c["id"]) in vectors else None) for c in data["chunks"]])
    source_ids = {r["id"] for r in data["records"]}
    for card in data["cards"]:
        trl = card.get("trl") or {}
        v = vectors.get(("technology", card["id"]))
        cur.execute("""INSERT INTO technology (id, name, sector, category, maturity, principle, trl_low, trl_high, last_reviewed, card, embedding)
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s::vector)""",
                    (card["id"], card["name"], card["sector"], card["category"], card["maturity"], card["principle"], trl.get("low"),
                     trl.get("high"), card["last_reviewed"], json.dumps(card), vec_text(v) if v is not None else None))
        for alias in set(card.get("aliases", [])):
            cur.execute("INSERT INTO technology_alias VALUES (%s,%s)", (card["id"], alias))
        for s in card["sources"]:
            cur.execute("INSERT INTO technology_source VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING",
                        (card["id"], s["url"], s.get("source_id") if s.get("source_id") in source_ids else None, s.get("note")))
        for kind, key in (("performance", "performance"), ("cost", "costs")):
            for f in card.get(key, []):
                cur.execute("""INSERT INTO technology_figure (technology_id, kind, metric, low, high, unit, year, basis, source_url)
                               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                            (card["id"], kind, f["metric"], f.get("low"), f.get("high"), f["unit"], f.get("year"), f["basis"], f["source"]["url"]))
        for s in card["suppliers"]:
            cur.execute("INSERT INTO technology_supplier VALUES (%s,%s,%s,%s) ON CONFLICT DO NOTHING",
                        (card["id"], s["name"], s.get("product"), s.get("source_id") if s.get("source_id") in source_ids else None))
        for g in card.get("gaps", []):
            cur.execute("""INSERT INTO technology_gap (technology_id, field, item, reason_code, reason, action, blocked_by, "where")
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (card["id"], g["field"], g["item"], g["reason_code"], g["reason"], g["action"], g.get("blocked_by"),
                         json.dumps(g.get("where", []))))
    for e in data["entries"]:
        cur.execute("INSERT INTO register_entry VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (graph.register_id(e).removeprefix("register:"), e["code"], e["area"], e["name"], e["maturity"], e["examples"], e["card"]))
    for n in nodes:
        kind, _, key = n["id"].partition(":")
        v = vectors.get((kind, key)) if kind in ("technology", "source") else None
        cur.execute("INSERT INTO node (id, kind, label, props, embedding) VALUES (%s,%s,%s,%s,%s::vector)",
                    (n["id"], n["kind"], n["label"], json.dumps(n["props"]), vec_text(v) if v is not None else None))
    for e in edges:
        cur.execute("INSERT INTO edge VALUES (%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING",
                    (e["src"], e["dst"], e["rel"], e["weight"], json.dumps(e["props"])))
    if any(("technology", c["id"]) in vectors for c in data["cards"]):
        cur.execute("SELECT refresh_similarity()")
    cur.execute("ANALYZE")
    return {"sources": len(data["records"]), "documents": len(data["docs"]), "chunks": len(data["chunks"]),
            "technologies": len(data["cards"]), "register": len(data["entries"]), "nodes": len(nodes), "edges": len(edges),
            "vectors": len(vectors)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dsn", default=os.environ.get("DATABASE_URL"), help="connection string (default: $DATABASE_URL)")
    ap.add_argument("--embeddings", choices=["auto", "sqlite", "fastembed", "none"], default="auto")
    ap.add_argument("--include-restricted", action="store_true",
                    help="also load text of full-text-restricted documents (only for a database no one else can read)")
    ap.add_argument("--dump-graph", metavar="DIR", help="write nodes.jsonl and edges.jsonl and exit")
    args = ap.parse_args(argv)

    nodes, edges = graph.build_graph()
    if args.dump_graph:
        out = pathlib.Path(args.dump_graph)
        out.mkdir(parents=True, exist_ok=True)
        (out / "nodes.jsonl").write_text("".join(json.dumps(n, ensure_ascii=False) + "\n" for n in nodes), encoding="utf-8")
        (out / "edges.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in edges), encoding="utf-8")
        print(json.dumps(graph.stats(nodes, edges)))
        return 0
    if not args.dsn:
        print("Set DATABASE_URL or pass --dsn.", file=sys.stderr)
        return 2
    import psycopg

    data = collect(args.include_restricted)
    vectors = {}
    if args.embeddings in ("auto", "sqlite"):
        vectors = sqlite_vectors(library.DB_PATH)
    if args.embeddings == "fastembed" or (args.embeddings == "auto" and not vectors):
        try:
            items = ([("technology", c["id"], card_search_text(c)) for c in data["cards"]]
                     + [("chunk", c["id"], f"{c['title']}\n{c['body']}") for c in data["chunks"]])
            vectors = fastembed_vectors(items)
        except ImportError:
            if args.embeddings == "fastembed":
                raise
            print("No embeddings: build them with `python agent/embed.py` or install fastembed. Loading without vectors.", file=sys.stderr)
    with psycopg.connect(args.dsn) as conn:
        result = load(conn, data, nodes, edges, vectors)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
