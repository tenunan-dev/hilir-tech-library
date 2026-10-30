"""Search index over the catalog, the corpus and the vendor directory, shared by the MCP server and the CLI.

The index is a SQLite file (build/library.db, not committed) with:
  sources      one row per catalog record
  docs         one row per corpus document, with its front matter
  search       FTS5 table over catalog records, corpus chunks, technology cards and vendor records
  vectors      optional embeddings per search row (see agent/embed.py)
  technologies one row per technology card
  vendors      one row per vendor directory record

Rebuild it with `python agent/library.py build` after the catalog, corpus or vendors change.
"""
import json
import pathlib
import re
import sqlite3
import sys

import yaml

import technologies
import vendors

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
# Technology cards are curated syntheses, so they rank a little above single sources.
TECHNOLOGY_BOOST = 1.3
TECHNOLOGY_LICENCE = "Library's own summary of cited sources; cite the sources listed in the card"
VENDOR_LICENCE = "Library's own curated vendor record; cite the sources listed in the record"


def vendor_text(v, card_names):
    """The text a vendor record is indexed and embedded by (SQLite and Postgres stay identical)."""
    return "\n".join([v["name"], " ".join(v.get("aliases", [])), v.get("country", ""),
                      " ".join(v.get("roles", [])), " ".join(v.get("products", [])), v.get("description", ""),
                      " ".join(card_names.get(t, "") for t in v.get("technologies", []))])


def vendor_sectors(v, sector_of):
    return sorted({sector_of[t] for t in v.get("technologies", []) if t in sector_of})


# Words that mark a document as belonging to a sector. Documents inherit their source's sectors,
# which is too broad for multi-topic sources such as arXiv or OSTI, so build() narrows them.
SECTOR_TERMS = {
    "UPS": ("reservoir", "wellbore", "drilling", "upstream", "offshore", "subsea", "oilfield", "history matching"),
    "MID": ("pipeline", "midstream", "storage terminal", "linepack", "flow assurance", "shipping"),
    "GAS": ("natural gas", "lng", "liquefaction", "regasification", "gas processing", "gas network", "gas market"),
    "REF": ("refinery", "refining", "hydrocracking", "crude", "fcc", "hydrotreating"),
    "PCH": ("petrochemical", "olefin", "polymer", "methanol", "aromatics", "steam cracking"),
    "PWR": ("power", "grid", "gas turbine", "turbine", "photovoltaic", "pv", "wind", "electricity"),
    "H2": ("hydrogen", "electrolyzer", "electrolyser", "electrolysis", "ammonia", "aviation fuel", "biofuel"),
    "CCS": ("carbon capture", "co2 capture", "co2 storage", "ccs", "ccus", "sequestration", "direct air capture",
            "carbonation", "post-combustion", "co2 utili"),
}


def doc_sectors(title, body, inherited):
    text = f"{title} {body}".lower()
    found = [code for code, terms in SECTOR_TERMS.items()
             if any(re.search(rf"\b{re.escape(t)}", text) for t in terms)]
    narrowed = [c for c in found if c in inherited] if inherited else found
    if narrowed:
        return narrowed
    # No sector words: a narrow source's tags still apply, a broad source's (3+ sectors) do not.
    return list(inherited) if len(inherited) <= 2 else found


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
        CREATE TABLE technologies (id TEXT PRIMARY KEY, card TEXT NOT NULL);
        CREATE TABLE vendors (id TEXT PRIMARY KEY, vendor TEXT NOT NULL, sectors TEXT NOT NULL);
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
        meta["sectors"] = doc_sectors(meta.get("title", ""), body, meta.get("sectors", []))
        rel = str(path.relative_to(corpus.parent))
        db.execute("INSERT INTO docs VALUES (?, ?, ?, ?, ?)",
                   (rel, meta.get("source_id"), meta.get("title"), meta.get("url"), json.dumps(meta, ensure_ascii=False)))
        tags = tag_text({**meta, "regions": by_id.get(meta.get("source_id"), {}).get("regions", [])}, labels)
        # The library's own summary leads the first chunk so searches reach it and snippets start with it.
        indexed = f"{meta['summary']}\n\n{body}" if meta.get("summary") else body
        for i, text in enumerate(chunk(indexed)):
            db.execute("INSERT INTO search VALUES ('chunk', ?, ?, ?, ?, ?)",
                       (f"{rel}#{i}", meta.get("source_id"), meta.get("title"), text, tags))
            n_chunks += 1
        n_docs += 1
    cards = technologies.load_cards(corpus.parent / "catalog" / "technologies")
    for card in cards:
        db.execute("INSERT INTO technologies VALUES (?, ?)", (card["id"], json.dumps(card, ensure_ascii=False)))
        text = "\n".join([card["category"], card["principle"], " ".join(card.get("aliases", [])),
                          " ".join(card.get("applications", [])), " ".join(card["key_equipment"]),
                          " ".join(s["name"] + " " + s.get("product", "") for s in card["suppliers"]), card["maturity"],
                          # What a card offers, so "options ... block diagram equipment cost" queries reach it.
                          "technology option block flow diagram process steps equipment",
                          " ".join(f["metric"] for f in card.get("costs", []) + card.get("performance", []))])
        db.execute("INSERT INTO search VALUES ('technology', ?, ?, ?, ?, ?)",
                   (card["id"], card["id"], card["name"], text, tag_text({"sectors": [card["sector"]]}, labels)))
    sector_of = {c["id"]: c["sector"] for c in cards}
    card_names = {c["id"]: c["name"] for c in cards}
    vendor_recs = vendors.load_vendors(corpus.parent / "catalog" / "vendors")
    for v in vendor_recs:
        sectors = vendor_sectors(v, sector_of)
        db.execute("INSERT INTO vendors VALUES (?, ?, ?)",
                   (v["id"], json.dumps(v, ensure_ascii=False), json.dumps(sectors)))
        db.execute("INSERT INTO search VALUES ('vendor', ?, ?, ?, ?, ?)",
                   (v["id"], v["id"], v["name"], vendor_text(v, card_names), tag_text({"sectors": sectors}, labels)))
    db.execute("INSERT INTO info VALUES ('root', ?)", (str(corpus.parent),))
    db.commit()
    return {"sources": len(records), "documents": n_docs, "chunks": n_chunks, "technologies": len(cards),
            "vendors": len(vendor_recs)}


def _matches(rec, sector, discipline, region, reuse_level):
    return ((not sector or sector in rec["sectors"]) and (not discipline or discipline in rec["disciplines"])
            and (not region or region in rec["regions"]) and (not reuse_level or rec["reuse_level"] == reuse_level))


def _doc_meta(db, path):
    row = db.execute("SELECT meta FROM docs WHERE path = ?", (path,)).fetchone()
    return json.loads(row["meta"]) if row else {}


def doc_restricted(db, path, rec):
    meta = _doc_meta(db, path)
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
        if meta.get("summary"):
            out["summary"] = meta["summary"]
        if doc_restricted(db, path, rec):
            out["use_note"] = "Private reference copy. Do not redistribute or use commercially; cite the url."
    return out


def search(query, kind="all", sector=None, discipline=None, region=None, reuse_level=None, limit=10,
           db=None, embedder=None, exclude_restricted=False, query_vector=None):
    """Keyword search (BM25), fused with vector search when vectors and an embedder are available.

    exclude_restricted drops passages from full-text-restricted sources (catalog records stay),
    for servers that other people can reach.
    """
    db = db or connect()
    records = {r["id"]: json.loads(r["record"]) for r in db.execute("SELECT * FROM sources")}
    kinds = ("source", "chunk", "technology", "vendor") if kind == "all" else (kind,)
    # Keep word characters only, then quote each token: any of the query's words may match, and
    # BM25 ranks rows that match more of them higher. The token filter is what keeps the MATCH
    # value inert, so it must stay on this path into the parameterised query below.
    terms = re.findall(r"\w+", query.lower())
    q = " OR ".join(f'"{t}"' for t in terms)
    if not q:
        return []
    # BM25 weights per column (kind, ref, source_id, title, text, tags): a match in the name or
    # text counts more than one in the taxonomy labels every record of a sector shares.
    sql = ("SELECT rowid, kind, ref, source_id, title, text, tags, "
           "bm25(search, 0, 0, 0, 3.0, 1.0, 0.4) AS rank FROM search "
           "WHERE search MATCH ? ORDER BY rank LIMIT 500")
    rows = db.execute(sql, (q,)).fetchall()
    # Rows matching more of the query's words come first; BM25 orders rows within each group.
    terms = set(re.findall(r"\w+", query.lower()))
    rows.sort(key=lambda r: (-sum(t in f"{r['title']} {r['text']} {r['tags']}".lower() for t in terms), r["rank"]))
    ranked = {}
    for pos, row in enumerate(rows):
        ranked[row["rowid"]] = [row, 1.0 / (60 + pos)]
    qvec = None
    if db.execute("SELECT count(*) FROM vectors").fetchone()[0]:
        import numpy as np
        if query_vector is not None and len(query_vector) == 384:
            # pre-embedded query (edge Workers AI service, decision #32): normalise defensively
            qvec = np.asarray(query_vector, dtype=np.float32)
            n = np.linalg.norm(qvec)
            if n:
                qvec = qvec / n
        elif embedder is not None:
            qvec = np.asarray(embedder([query])[0], dtype=np.float32)
    if qvec is not None:
        import numpy as np
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
        if row["kind"] == "technology":
            card = json.loads(db.execute("SELECT card FROM technologies WHERE id = ?", (row["ref"],)).fetchone()[0])
            if "technology" in kinds and (not sector or card["sector"] == sector) and not discipline \
                    and reuse_level in (None, "full-text-open"):
                results.append((score * TECHNOLOGY_BOOST, row, card))
            continue
        if row["kind"] == "vendor":
            found = db.execute("SELECT vendor, sectors FROM vendors WHERE id = ?", (row["ref"],)).fetchone()
            if not found:
                continue
            vrec, vsectors = json.loads(found[0]), json.loads(found[1])
            if "vendor" in kinds and (not sector or sector in vsectors) and not discipline \
                    and reuse_level in (None, "full-text-open"):
                results.append((score, row, vrec))
            continue
        rec = records.get(row["source_id"])
        if not rec or row["kind"] not in kinds or not _matches(rec, None, discipline, region, reuse_level):
            continue
        if sector and sector not in (_doc_meta(db, row["ref"].split("#")[0]).get("sectors", []) if row["kind"] == "chunk"
                                     else rec["sectors"]):
            continue
        if exclude_restricted and row["kind"] == "chunk" and doc_restricted(db, row["ref"].split("#")[0], rec):
            continue
        boost = max([REGION_BOOST.get(g, 1.0) for g in rec["regions"]] + [1.0])
        results.append((score * boost, row, rec))
    results.sort(key=lambda t: -t[0])
    return [_technology_result(row, score, rec) if row["kind"] == "technology" else
            _vendor_result(row, score, rec) if row["kind"] == "vendor" else
            _result(db, row, score, records)
            for score, row, rec in results[:limit]]


def _technology_result(row, score, card):
    out = {"kind": "technology", "ref": card["id"], "title": card["name"], "score": round(score, 4),
           "licence": TECHNOLOGY_LICENCE, "reuse_level": "full-text-open", "permitted_use": "any"}
    out.update(technologies.summary(card))
    out["hint"] = "Call get_technology for the block diagram, figures and sources."
    return out


def get_technology(tech_id, db=None):
    """Full technology card plus its block flow diagram as Mermaid text."""
    db = db or connect()
    row = db.execute("SELECT card FROM technologies WHERE id = ?", (tech_id,)).fetchone()
    if not row:
        return None
    card = json.loads(row[0])
    card["block_diagram_mermaid"] = technologies.mermaid(card)
    card["licence"] = TECHNOLOGY_LICENCE
    return card


def list_register(code=None, maturity=None, query=None):
    """Technology register entries (indicative, unverified), optionally filtered."""
    q = (query or "").lower()
    return [e for e in technologies.load_register()
            if (not code or e["code"] == code) and (not maturity or e["maturity"] == maturity)
            and (not q or q in f"{e['name']} {e['area']} {e['examples']}".lower())]


def list_gaps(sector=None, field=None, reason_code=None, include_no_card=False, db=None):
    """Missing inputs recorded on cards (why missing, where to get them, next action); optionally register entries with no card."""
    db = db or connect()
    cards = [json.loads(r[0]) for r in db.execute("SELECT card FROM technologies")]
    rows = technologies.gaps(cards, technologies.load_register(cards=cards) if include_no_card else [])
    return [r for r in rows if (not sector or r["sector"] == sector) and (not field or r["field"] == field)
            and (not reason_code or r["reason_code"] == reason_code)]


def compare_technologies(sector=None, maturity=None, application=None, db=None):
    db = db or connect()
    cards = [json.loads(r[0]) for r in db.execute("SELECT card FROM technologies")]
    return technologies.compare(cards, sector, maturity, application)


def _vendor_result(row, score, vrec):
    out = {"kind": "vendor", "ref": vrec["id"], "title": vrec["name"], "score": round(score, 4),
           "licence": VENDOR_LICENCE, "reuse_level": "full-text-open", "permitted_use": "any",
           "country": vrec.get("country"), "roles": vrec.get("roles", []), "products": vrec.get("products", []),
           "technologies": vrec.get("technologies", [])}
    out["hint"] = "Call get_vendor for the full record and the sources behind it."
    return out


def get_vendor(vendor_id, db=None):
    """Full vendor directory record."""
    db = db or connect()
    row = db.execute("SELECT vendor FROM vendors WHERE id = ?", (vendor_id,)).fetchone()
    return json.loads(row[0]) if row else None


def list_vendors(role=None, sector=None, query=None, db=None):
    """Vendor directory records, optionally filtered by role, sector code or text."""
    db = db or connect()
    q = (query or "").lower()
    out = []
    for blob, sectors in db.execute("SELECT vendor, sectors FROM vendors"):
        v = json.loads(blob)
        if role and role not in v.get("roles", []):
            continue
        if sector and sector not in json.loads(sectors):
            continue
        hay = " ".join([v["name"], " ".join(v.get("aliases", [])), v.get("description", ""),
                        " ".join(v.get("products", [])), v.get("country", "")]).lower()
        if q and q not in hay:
            continue
        out.append(vendors.summary(v))
    out.sort(key=lambda s: s["name"].lower())
    return out


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
            "technologies": db.execute("SELECT count(*) FROM technologies").fetchone()[0],
            "vendors": db.execute("SELECT count(*) FROM vendors").fetchone()[0],
            "embedding_model": (db.execute("SELECT value FROM info WHERE key = 'model'").fetchone() or [None])[0]}


if __name__ == "__main__":
    if sys.argv[1:2] == ["build"]:
        print(json.dumps(build()))
    elif sys.argv[1:2] == ["search"]:
        query = " ".join(re.findall(r"\w+", " ".join(sys.argv[2:]).lower()))  # word characters only
        for hit in search(query):
            print(f"{hit['score']:.4f}  {hit['kind']:6}  {hit.get('source_id', hit['ref']):24}  {hit['title']}")
    else:
        print("usage: python agent/library.py build | search <query>")
