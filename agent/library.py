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
import equipment
import projects
import bm25

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
EQUIPMENT_LICENCE = "Library's own curated equipment record; cite the sources listed in the record"
PROJECT_LICENCE = "Library's own curated project record; cite the sources listed in the record"
# Candidates each kind contributes to the rank fusion. og.hybrid_search uses the same 50
# (its CTE keeps `r <= 50`), so a passage pool of 15,000 rows cannot crowd out the records.
FUSION_POOL = 50
# Subscript digits, so "CO₂" tokenises like "CO2" instead of losing the 2.
_SUBSCRIPTS = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
_concept_cache = None


def search_concepts(path=None):
    """concept -> tuple of interchangeable terms, from catalog/search-concepts.yaml.

    The same file seeds og.search_concept on the Postgres path (tools/load_postgres.py), so both
    rankings expand a query identically. A missing or empty file means no expansion — each query
    word is its own concept — which is the safe fallback, not an error.
    """
    global _concept_cache
    if path is None and _concept_cache is not None:
        return _concept_cache
    file = pathlib.Path(path) if path else ROOT / "catalog" / "search-concepts.yaml"
    data = yaml.safe_load(file.read_text(encoding="utf-8")) if file.exists() else {}
    table = {}
    for concept, members in ((data or {}).get("concepts") or {}).items():
        words = tuple(w for term in members or [] for w in re.findall(r"\w+", str(term).lower()))
        if words:
            table[str(concept).lower()] = words
    if path is None:
        _concept_cache = table
    return table


def concept_groups(query, concepts=None):
    """The query's tokens grouped by concept, each group expanded to every term of its concept.

    ["carbon", "capture", "amine"] -> [("carbon", "co2"), ("capture",), ("amine",)]. A word in
    no group is its own concept.
    """
    table = search_concepts() if concepts is None else concepts
    lookup = {term: concept for concept, members in table.items() for term in members}
    groups, seen = [], set()
    for token in re.findall(r"\w+", query.translate(_SUBSCRIPTS).lower()):
        concept = lookup.get(token, token)
        if concept in seen:
            continue
        seen.add(concept)
        groups.append(table.get(concept, (token,)))
    return groups


def _concept_coverage(groups, row):
    """How many of the query's concepts this row covers (substring match, as the index does)."""
    haystack = f"{row['title']} {row['text']} {row['tags']}".lower()
    return sum(1 for group in groups if any(term in haystack for term in group))


def term_df(db, term):
    """How many index rows carry `term` — 0 when the index does not hold it at all."""
    row = db.execute("SELECT df FROM term_df WHERE term = ?", (term,)).fetchone()
    return row[0] if row else 0


def rare_groups(groups, db):
    """The query's rare concepts — the qualifiers a user typed (a product or process code).

    "Rare" is measured, not listed: a concept is rare when the least common of its terms appears
    in at least one and no more than 1% of the index (floor 8 records). On the production corpus
    that separates product codes (0.03–0.8% of records) from ordinary domain words (3–27%).
    og.hybrid_search applies the same cut-off against og.search_term. A term the index does not
    hold at all is not rare — it matches nothing, so promoting it would only add noise.
    """
    n = db.execute("SELECT count(*) FROM search").fetchone()[0]
    cutoff = max(8, n // 100)
    return [group for group in groups if 0 < min(term_df(db, t) for t in group) <= cutoff]



def equipment_text(rec, card_names, vendor_names):
    """The text an equipment record is indexed and embedded by (SQLite and Postgres stay identical)."""
    specs = "\n".join(f"{s['metric']}: {s.get('basis', '')}".rstrip(" :") for s in rec.get("specifications", []))
    models = "\n".join(f"{vendor_names.get(m['vendor'], m['vendor'])} {m.get('line', '')}: {m.get('range', '')}"
                       for m in rec.get("vendor_models", []))
    return "\n".join([rec["name"], " ".join(rec.get("aliases", [])), rec.get("equipment_type", ""),
                      rec.get("description", ""), specs, models,
                      " ".join(card_names.get(t, "") for t in rec.get("technologies", []))])


def equipment_of_vendors(equipment_recs, vendor_names):
    """Map vendor id -> the equipment-class names of the records that list it, so vendors that
    supply a class surface in search even when their own page never says the word ("boiler")."""
    out = {}
    for rec in equipment_recs:
        for vid in rec.get("vendors", []):
            out.setdefault(vid, []).append(rec["name"])
    return out


def project_text(rec, card_names, vendor_names):
    """The text a project record is indexed and embedded by (SQLite and Postgres stay identical)."""
    caps = "\n".join(f"{c['metric']}: {c.get('basis', '')}".rstrip(" :") for c in rec.get("capacities", []))
    parties = "\n".join(f"{p.get('role', '')}: {vendor_names.get(p.get('vendor_id', ''), '') or p['name']}".strip(" :")
                        for group in ("owners", "contractors", "offtakers") for p in rec.get(group, []))
    return "\n".join([rec["name"], " ".join(rec.get("aliases", [])), rec.get("location", ""),
                      rec.get("description", ""), rec.get("status", ""), caps, parties,
                      " ".join(card_names.get(t, "") for t in rec.get("technologies", [])),
                      "project plant facility reference case"])


def vendor_text(v, card_names, equipment_names=None):
    """The text a vendor record is indexed and embedded by (SQLite and Postgres stay identical)."""
    return "\n".join([v["name"], " ".join(v.get("aliases", [])), v.get("country", ""),
                      " ".join(v.get("roles", [])), " ".join(v.get("products", [])), v.get("description", ""),
                      " ".join(card_names.get(t, "") for t in v.get("technologies", [])),
                      "supplies equipment classes: " + " ".join(equipment_names or [])])


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
        CREATE TABLE equipment (id TEXT PRIMARY KEY, record TEXT NOT NULL, sectors TEXT NOT NULL);
        CREATE TABLE projects (id TEXT PRIMARY KEY, record TEXT NOT NULL, sectors TEXT NOT NULL);
        CREATE TABLE term_df (term TEXT PRIMARY KEY, df INTEGER NOT NULL);
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
        db.execute("INSERT INTO search VALUES ('technology', ?, ?, ?, ?, ?)",
                   (card["id"], card["id"], card["name"], technologies.search_text(card),
                    tag_text({"sectors": [card["sector"]]}, labels)))
    sector_of = {c["id"]: c["sector"] for c in cards}
    card_names = {c["id"]: c["name"] for c in cards}
    equipment_recs = equipment.load_equipment(corpus.parent / "catalog" / "equipment")
    vendor_recs = vendors.load_vendors(corpus.parent / "catalog" / "vendors")
    eq_names_by_vendor = equipment_of_vendors(equipment_recs, {v["id"]: v["name"] for v in vendor_recs})
    for v in vendor_recs:
        sectors = vendor_sectors(v, sector_of)
        db.execute("INSERT INTO vendors VALUES (?, ?, ?)",
                   (v["id"], json.dumps(v, ensure_ascii=False), json.dumps(sectors)))
        db.execute("INSERT INTO search VALUES ('vendor', ?, ?, ?, ?, ?)",
                   (v["id"], v["id"], v["name"], vendor_text(v, card_names, eq_names_by_vendor.get(v["id"])),
                    tag_text({"sectors": sectors}, labels)))
    for rec in equipment_recs:
        sector_tags = rec.get("sector_codes") or ([rec["sector"]] if rec.get("sector") else [])
        sectors = sorted(set(sector_tags))
        db.execute("INSERT INTO equipment VALUES (?, ?, ?)",
                   (rec["id"], json.dumps(rec, ensure_ascii=False), json.dumps(sectors)))
        db.execute("INSERT INTO search VALUES ('equipment', ?, ?, ?, ?, ?)",
                   (rec["id"], rec["id"], rec["name"], equipment_text(rec, card_names, {v["id"]: v["name"] for v in vendor_recs}),
                    tag_text({"sectors": sectors}, labels)))
    project_recs = projects.load_projects(corpus.parent / "catalog" / "projects")
    vnames = {v["id"]: v["name"] for v in vendor_recs}
    for rec in project_recs:
        sector_tags = rec.get("sector_codes") or ([rec["sector"]] if rec.get("sector") else [])
        sectors = sorted(set(sector_tags))
        db.execute("INSERT INTO projects VALUES (?, ?, ?)",
                   (rec["id"], json.dumps(rec, ensure_ascii=False), json.dumps(sectors)))
        db.execute("INSERT INTO search VALUES ('project', ?, ?, ?, ?, ?)",
                   (rec["id"], rec["id"], rec["name"], project_text(rec, card_names, vnames),
                    tag_text({"sectors": sectors}, labels)))
    db.execute("INSERT INTO info VALUES ('root', ?)", (str(corpus.parent),))
    # Per-term document frequency, the same signal og.search_term carries on the Postgres path:
    # a product code is in a handful of records, an ordinary word in thousands, and the rare-concept
    # pool uses that ratio to let a query naming a code rank the record that carries it.
    counts = {}
    for title, text, tags in db.execute("SELECT title, text, tags FROM search"):
        for tok in {t for t in re.findall(r"\w+", f"{title} {text} {tags}".lower())}:
            counts[tok] = counts.get(tok, 0) + 1
    db.executemany("INSERT INTO term_df VALUES (?, ?)", counts.items())
    db.commit()
    return {"sources": len(records), "documents": n_docs, "chunks": n_chunks, "technologies": len(cards),
            "vendors": len(vendor_recs), "equipment": len(equipment_recs), "projects": len(project_recs)}


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
    """Keyword search (BM25) fused with vector search, ranked the same way og.hybrid_search is.

    Three rules shape it, each from a measured failure (2026-11-23):

    * The query is expanded through catalog/search-concepts.yaml, so "carbon" also searches
      "co2" — the catalogue writes the molecule, people type the element. "carbon capture amine"
      could not find the card named "Amine solvent post-combustion capture" without it.
    * Rows are ordered by how many query CONCEPTS they cover, then by BM25. Counting raw words
      let a document whose title happens to hold every word outrank every card, and let cards
      that merely said "carbon" often beat the card that is the answer.
    * A concept that is rare in the index (a product or process code: "KS-1", "MDEA") forms a
      third pool of its own, so the record carrying it leads even when a common word in the same
      query has a better vector neighbourhood. See rare_groups().

    exclude_restricted drops passages from full-text-restricted sources (catalog records stay),
    for servers that other people can reach.
    """
    db = db or connect()
    records = {r["id"]: json.loads(r["record"]) for r in db.execute("SELECT * FROM sources")}
    kinds = ("source", "chunk", "technology", "vendor", "equipment", "project") if kind == "all" else (kind,)
    # Keep word characters only, then quote each token: any of the query's words (or a word its
    # concept group adds) may match. The token filter is what keeps the MATCH value inert, so it
    # must stay on this path into the parameterised query below.
    concepts = concept_groups(query)
    terms = [t for group in concepts for t in group]
    q = " OR ".join(f'"{t}"' for t in terms)
    if not q:
        return []
    # BM25 weights per column (kind, ref, source_id, title, text, tags): a match in the name or
    # text counts more than one in the taxonomy labels every record of a sector shares.
    # The MATCH query itself lives in ./bm25.py (its own validated module); q is
    # inert here — word-character tokens only, quoted per token (filter above).
    rows = bm25.match_rows(db, q)
    rows.sort(key=lambda r: (-_concept_coverage(concepts, r), r["rank"]))
    # Reciprocal rank fusion, per kind: a passage pool of 15,000 rows must not push every card,
    # vendor and equipment class out of the candidate set. og.hybrid_search partitions the same
    # way (50 per kind); a single global pool buried all 400 cards under the corpus (2026-11-23).
    ranked = {}
    kw_pos = {}
    for row in rows:
        kw_pos[row["kind"]] = kw_pos.get(row["kind"], 0) + 1
        if kw_pos[row["kind"]] > FUSION_POOL:
            continue
        ranked[row["rowid"]] = [row, 1.0 / (60 + kw_pos[row["kind"]])]
    # A third pool for the query's rare concepts — the code the user typed. Fusion sums pools, so
    # this is what keeps a common word's vector neighbourhood from outvoting the one record that
    # names the code ("KS-1 solvent" put the amine card keyword-1st but 4th overall, 2026-11-23).
    rare = rare_groups(concepts, db)
    if rare:
        rare_pos = {}
        for row in sorted((r for r in rows if _concept_coverage(rare, r)), key=lambda r: r["rank"]):
            rare_pos[row["kind"]] = rare_pos.get(row["kind"], 0) + 1
            if rare_pos[row["kind"]] > FUSION_POOL:
                continue
            if row["rowid"] not in ranked:
                ranked[row["rowid"]] = [row, 0.0]
            ranked[row["rowid"]][1] += 1.0 / (60 + rare_pos[row["kind"]])
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
        vec_rows = db.execute("SELECT v.rowid, s.kind, v.vec FROM vectors v JOIN search s ON s.rowid = v.rowid").fetchall()
        ids = [r[0] for r in vec_rows]
        vec_kind = {r[0]: r[1] for r in vec_rows}
        sims = np.stack([np.frombuffer(r[2], dtype=np.float32) for r in vec_rows]) @ qvec
        vec_pos = {}
        for idx in np.argsort(-sims):
            rowid = ids[idx]
            kind_ = vec_kind[rowid]
            if vec_pos.get(kind_, 0) >= FUSION_POOL:
                continue
            vec_pos[kind_] = vec_pos.get(kind_, 0) + 1
            if rowid not in ranked:
                row = db.execute("SELECT rowid, kind, ref, source_id, title, text FROM search WHERE rowid = ?", (rowid,)).fetchone()
                ranked[rowid] = [row, 0.0]
            ranked[rowid][1] += 1.0 / (60 + vec_pos[kind_])
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
        if row["kind"] == "equipment":
            found = db.execute("SELECT record, sectors FROM equipment WHERE id = ?", (row["ref"],)).fetchone()
            if not found:
                continue
            erec, esectors = json.loads(found[0]), json.loads(found[1])
            if "equipment" in kinds and (not sector or sector in esectors) and not discipline \
                    and reuse_level in (None, "full-text-open"):
                results.append((score, row, erec))
            continue
        if row["kind"] == "project":
            found = db.execute("SELECT record, sectors FROM projects WHERE id = ?", (row["ref"],)).fetchone()
            if not found:
                continue
            prec, psectors = json.loads(found[0]), json.loads(found[1])
            if "project" in kinds and (not sector or sector in psectors) and not discipline \
                    and reuse_level in (None, "full-text-open"):
                results.append((score, row, prec))
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
            _equipment_result(row, score, rec) if row["kind"] == "equipment" else
            _project_result(row, score, rec) if row["kind"] == "project" else
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


def get_register_entry(entry_id):
    """One register entry by its id — "<code>/<slug-of-name>", the same id the Neon rows carry
    (graph.register_id minus the "register:" prefix). Returns None for an unknown id."""
    from graph import slug
    needle = (entry_id or "").strip().removeprefix("register:")
    if not needle:
        return None
    for e in technologies.load_register():
        if f"{e['code']}/{slug(e['name'])[:80]}" == needle:
            return e
    return None


def list_documents(source_id=None, sector=None, limit=50, db=None, exclude_restricted=False):
    """Document index rows (path, title, source, reuse level), optionally per source or sector.
    Mirrors pg.document_rows: restricted documents are listed with their metadata even when the
    text is withheld (text_included=false) — the index is the discovery surface, not the text."""
    db = db or connect()
    out = []
    for path, title, url, sid, blob in db.execute(
            "SELECT d.path, d.title, d.url, s.id, s.record FROM docs d JOIN sources s ON s.id = d.source_id ORDER BY d.path"):
        rec = json.loads(blob)
        if source_id and sid != source_id:
            continue
        if sector and sector not in rec.get("sectors", []):
            continue
        if len(out) >= max(1, min(int(limit), 500)):
            break
        restricted = exclude_restricted and doc_restricted(db, path, rec)
        out.append({"path": path, "title": title, "source_id": sid, "source_name": rec.get("name"),
                    "source_url": rec.get("url"), "reuse_level": rec.get("reuse_level"),
                    "text_included": not restricted, "sectors": rec.get("sectors", [])})
    return out


def list_gaps(sector=None, field=None, reason_code=None, include_no_card=False, db=None):
    """Missing inputs recorded on cards (why missing, where to get them, next action); optionally register entries with no card."""
    db = db or connect()
    cards = [json.loads(r[0]) for r in db.execute("SELECT card FROM technologies")]
    rows = technologies.gaps(cards, technologies.load_register(cards=cards) if include_no_card else [])
    return [r for r in rows if (not sector or r["sector"] == sector) and (not field or r["field"] == field)
            and (not reason_code or r["reason_code"] == reason_code)]


def compare_technologies(sector=None, maturity=None, application=None, db=None, technology_ids=None):
    db = db or connect()
    cards = [json.loads(r[0]) for r in db.execute("SELECT card FROM technologies")]
    return technologies.compare(cards, sector, maturity, application, technology_ids)


GLOSSARY_PATH = ROOT / "catalog" / "glossary.jsonl"
STANDARDS_PATH = ROOT / "catalog" / "standards.jsonl"


def _read_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def taxonomy():
    """The two tag axes with their subtopics, so a caller can pick valid filter codes.

    Every source and card carries at least one sector and one discipline; the register uses the
    same codes. Returned as lists of {code, name, subtopics} to keep the shape stable on the wire.
    """
    tax = yaml.safe_load((ROOT / "taxonomy.yaml").read_text(encoding="utf-8"))
    return {
        "sectors": [{"code": code, **info} for code, info in tax["sectors"].items()],
        "disciplines": [{"code": code, **info} for code, info in tax["disciplines"].items()],
        "regions": [{"code": code, "name": name} for code, name in (tax.get("regions") or {}).items()],
        "note": "Filter sectors/disciplines/regions use these codes. A card has one sector; a discipline "
                "code may be either axis when filtering sources.",
    }


def find_figures(kind="both", sector=None, technology_id=None, query=None, unit=None, limit=50, db=None):
    """Every performance or cost figure recorded on the cards, one row per figure.

    kind: "cost", "performance" or "both". sector / technology_id narrow to one card or sector.
    query matches the metric, basis or card name (case-insensitive substring). unit matches the
    unit string the same way (e.g. "USD/kW", "GJ/t"). Each row keeps its basis and source, which
    is what makes a figure usable — a bare number without them is not evidence.
    """
    db = db or connect()
    kinds = ("performance", "cost") if kind == "both" else (kind,)
    q = (query or "").lower()
    u = (unit or "").lower()
    out = []
    for row in db.execute("SELECT card FROM technologies"):
        card = json.loads(row[0])
        if sector and card.get("sector") != sector:
            continue
        if technology_id and card.get("id") != technology_id:
            continue
        for one in kinds:
            for fig in card.get("costs" if one == "cost" else "performance") or []:
                if u and u not in (fig.get("unit") or "").lower():
                    continue
                hay = f'{card["name"]} {fig.get("metric", "")} {fig.get("basis", "")}'.lower()
                if q and q not in hay:
                    continue
                src = fig.get("source") or {}
                out.append({"kind": one, "technology": card["name"], "technology_id": card["id"],
                            "sector": card.get("sector"), "metric": fig.get("metric"),
                            "low": fig.get("low"), "high": fig.get("high"), "unit": fig.get("unit"),
                            "year": fig.get("year"), "basis": fig.get("basis"),
                            "source_url": src.get("url"), "source_note": src.get("note"),
                            "licence": TECHNOLOGY_LICENCE})
    out.sort(key=lambda r: (r["technology"].lower(), r["kind"], r["metric"] or ""))
    return out[:limit]


def list_glossary(query=None):
    """Terms and expansions used across the library, optionally filtered by text."""
    q = (query or "").lower()
    return [t for t in _read_jsonl(GLOSSARY_PATH)
            if not q or q in f'{t["term"]} {t.get("expansion", "")} {t.get("note", "")}'.lower()]


def get_glossary_term(term):
    """One glossary entry by term or expansion (exact first, then substring)."""
    needle = (term or "").strip().lower()
    if not needle:
        return None
    entries = _read_jsonl(GLOSSARY_PATH)
    for t in entries:
        if needle == t["term"].lower() or needle == (t.get("expansion") or "").lower():
            return t
    for t in entries:
        if needle in f'{t["term"]} {t.get("expansion", "")}'.lower():
            return t
    return None


def list_standards(org=None, query=None):
    """Standards and codes referenced by the library (27 entries): designation, title, scope, url."""
    q = (query or "").lower()
    return [s for s in _read_jsonl(STANDARDS_PATH)
            if (not org or s.get("org") == org)
            and (not q or q in f'{s["designation"]} {s["title"]} {s.get("scope", "")}'.lower())]


def get_standard(ref):
    """One standard by id or designation, exact then substring."""
    needle = (ref or "").strip().lower()
    if not needle:
        return None
    entries = _read_jsonl(STANDARDS_PATH)
    for s in entries:
        if needle in (s.get("id", "").lower(), s["designation"].lower()):
            return s
    for s in entries:
        if needle in f'{s["designation"]} {s["title"]}'.lower():
            return s
    return None


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


def get_equipment(equipment_id, db=None):
    """Full equipment catalog record: specifications, vendors, sources and gaps."""
    db = db or connect()
    row = db.execute("SELECT record FROM equipment WHERE id = ?", (equipment_id,)).fetchone()
    return json.loads(row[0]) if row else None


def list_equipment(equipment_type=None, query=None, db=None):
    """Equipment catalog records, optionally filtered by equipment type or text."""
    db = db or connect()
    q = (query or "").lower()
    out = []
    for blob in db.execute("SELECT record FROM equipment"):
        rec = json.loads(blob[0])
        if equipment_type and equipment_type != rec.get("equipment_type"):
            continue
        hay = " ".join([rec["name"], " ".join(rec.get("aliases", [])), rec.get("description", ""),
                        " ".join(s["metric"] for s in rec.get("specifications", [])),
                        " ".join(rec.get("vendors", []))]).lower()
        if q and q not in hay:
            continue
        out.append(equipment.summary(rec))
    out.sort(key=lambda s: s["name"].lower())
    return out


def _equipment_result(row, score, erec):
    out = {"kind": "equipment", "ref": erec["id"], "title": erec["name"], "score": round(score, 4),
           "licence": EQUIPMENT_LICENCE, "reuse_level": "full-text-open", "permitted_use": "any",
           "equipment_type": erec.get("equipment_type"), "sector": erec.get("sector"),
           "vendors": erec.get("vendors", []),
           "spec_metrics": [s["metric"] for s in erec.get("specifications", [])]}
    out["hint"] = "Call get_equipment for the specification ranges, vendor model lines and sources."
    return out


def _project_result(row, score, prec):
    out = {"kind": "project", "ref": prec["id"], "title": prec["name"], "score": round(score, 4),
           "licence": PROJECT_LICENCE, "reuse_level": "full-text-open", "permitted_use": "any",
           "status": prec.get("status"), "country": prec.get("country"), "sector": prec.get("sector"),
           "project_type": prec.get("project_type"),
           "technologies": prec.get("technologies", []),
           "owners": [p.get("vendor_id") or p["name"] for p in prec.get("owners", [])]}
    out["hint"] = "Call get_project for the capacities, milestones, contractors and sources."
    return out


def get_project(project_id, db=None):
    """Full project record: capacities, milestones, owners, contractors, sources and gaps."""
    db = db or connect()
    row = db.execute("SELECT record FROM projects WHERE id = ?", (project_id,)).fetchone()
    return json.loads(row[0]) if row else None


def list_projects(status=None, sector=None, country=None, query=None, db=None):
    """Project catalog records, optionally filtered by status, sector code, country or text."""
    db = db or connect()
    q = (query or "").lower()
    out = []
    for blob in db.execute("SELECT record, sectors FROM projects"):
        rec = json.loads(blob[0])
        if status and status != rec.get("status"):
            continue
        if sector and sector not in json.loads(blob[1]):
            continue
        if not projects.country_matches(rec.get("country"), country):
            continue
        hay = " ".join([rec["name"], " ".join(rec.get("aliases", [])), rec.get("location", ""),
                        rec.get("description", ""), rec.get("country", "")]).lower()
        if q and q not in hay:
            continue
        out.append(projects.summary(rec))
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


def get_document(path, db=None, exclude_restricted=False, offset=0, limit=None):
    db = db or connect()
    row = db.execute("SELECT d.path, s.record FROM docs d JOIN sources s ON s.id = d.source_id WHERE d.path = ?",
                     (path.split("#")[0],)).fetchone()
    if not row:
        return None
    if exclude_restricted and doc_restricted(db, row["path"], json.loads(row["record"])):
        return {"path": row["path"], "error": "Private reference copy; not served by this server. Cite the source url instead."}
    # The baked root is absolute and machine-specific, so a checkout that was moved after the
    # build still holds the old one. Prefer it while it resolves, then fall back to this checkout.
    root = db.execute("SELECT value FROM info WHERE key = 'root'").fetchone()
    bases = [pathlib.Path(root[0]) if root else ROOT, ROOT]
    doc_path = next((b / row["path"] for b in bases if (b / row["path"]).exists()), bases[0] / row["path"])
    meta, body = read_document(doc_path)
    # Page through the text in characters (default limit 20,000, hard cap 100,000): the corpus
    # holds documents over 2M characters, so an uncapped call is unusable for an agent.
    if limit is None:
        limit = 20000
    limit = max(0, min(int(limit), 100_000))
    offset = max(0, int(offset))
    return {"path": row["path"], "meta": meta, "text": body[offset:offset + limit],
            "total_chars": len(body), "offset": offset, "limit": limit}


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
            "equipment": db.execute("SELECT count(*) FROM equipment").fetchone()[0],
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
