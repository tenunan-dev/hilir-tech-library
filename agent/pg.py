"""Read-only Postgres access for the MCP server and the web UI: guarded SQL, hybrid search and graph walks.

    import pg
    pg.counts()                                                 # table sizes for the dashboard
    pg.hybrid_search("CO2 storage Malay Basin", k=10)           # fused keyword + vector ranking, qvec optional
    pg.graph_neighbors("technology:ccs-cryogenic", 2)           # walk the knowledge graph from one node
    pg.run_sql("SELECT * FROM v_gap ORDER BY name LIMIT 20")    # one agent-written SELECT/WITH, guarded

The DSN comes from $DATABASE_URL and must be the read-only role's DSN (og_mcp_read, see db/readonly.sql and
`python tools/load_postgres.py --grant-readonly`), never the owner DSN. psycopg is imported lazily inside the
connect helper, so importing this module works even without psycopg installed. Behind Neon's transaction-mode
pooler no session state survives, so every call runs in its own transaction: conn.read_only makes psycopg
begin it READ ONLY, and the transaction starts with SET LOCAL statement_timeout and SET LOCAL search_path —
transaction-scoped, the only SET form that pooling cannot lose.

Every value is bound with %s parameters, with one deliberate exception: the statement handed to run_sql is
itself outside SQL text, and _check() confines it to a single comment-free SELECT/WITH while the read-only
role and the READ ONLY transaction reject anything that is not a read.
"""
import json
import os
import re
import urllib.parse

DSN_ENV = "DATABASE_URL"

_conn = None

_NOT_A_READ = "one SELECT/WITH statement only, no semicolon, no comments"
_BANNED = re.compile(r"\b(into|insert|update|delete|drop|alter|create|grant|revoke|copy|truncate|vacuum|"
                     r"analyze|reindex|call|do|merge)\b", re.I)
NODE_ID = re.compile(r"^[a-z_]+:[A-Za-z0-9._/#:-]{1,150}$")
NODE_KIND = re.compile(r"^[a-z_]{1,30}$")


class NotConfigured(RuntimeError):
    """No DSN in the environment."""


class BadSql(ValueError):
    """_check rejected the statement; str(e) is a user-safe message."""


class DatabaseError(RuntimeError):
    """A psycopg error, wrapped with a clean message."""


def configured() -> bool:
    """True when a DSN is in the environment."""
    return bool(os.environ.get(DSN_ENV))


def dsn() -> str | None:
    return os.environ.get(DSN_ENV) or None


def _connect():
    """autocommit so nothing runs outside our explicit transactions; read_only so every transaction() begins READ ONLY."""
    import psycopg
    conn = psycopg.connect(dsn())
    conn.autocommit = True
    conn.read_only = True
    return conn


def _close():
    global _conn
    if _conn is None:
        return
    try:
        _conn.close()
    except Exception:
        pass
    _conn = None


def _execute(work):
    """Run work(cursor) inside one transaction; on a dropped connection reconnect once and retry once."""
    global _conn
    if not configured():
        raise NotConfigured(f"no {DSN_ENV} in the environment")
    import psycopg
    for attempt in (0, 1):
        try:
            if _conn is None:
                _conn = _connect()
            with _conn.transaction():
                cur = _conn.cursor()
                cur.execute("SET LOCAL statement_timeout = '15s'")
                cur.execute("SET LOCAL search_path = og, public")
                return work(cur)
        except psycopg.OperationalError as e:
            if attempt:
                raise DatabaseError(str(e)) from e
            _close()
        except psycopg.Error as e:
            raise DatabaseError(str(e)) from e


def _cell(value):
    """One result cell: None, or str(value) capped at 2000 characters."""
    if value is None:
        return None
    text = str(value)
    return text if len(text) <= 2000 else text[:2000] + "…"


def _rows(cur):
    """Remaining rows as dicts keyed by the cursor's column names."""
    cols = [c.name for c in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def _check(sql: str) -> None:
    """Confine run_sql to one comment-free SELECT/WITH; the read-only role and READ ONLY transaction back it up."""
    text = sql.strip()
    if not text or ";" in text or "--" in text or "/*" in text:
        raise BadSql(_NOT_A_READ)
    if text.split(None, 1)[0].lower() not in ("select", "with"):
        raise BadSql(_NOT_A_READ)
    if _BANNED.search(text):
        raise BadSql(_NOT_A_READ)


def run_sql(sql: str, max_rows: int = 200) -> dict:
    """One guarded read-only statement; at most max_rows rows (1..500), cells capped at 2000 characters."""
    _check(sql)
    limit = max(1, min(500, int(max_rows)))

    def work(cur):
        cur.execute(sql)
        columns = [c.name for c in cur.description]
        rows = cur.fetchmany(limit + 1)
        truncated = len(rows) > limit
        cells = [[_cell(v) for v in row] for row in rows[:limit]]
        if sum(len(cell) for row in cells for cell in row if cell is not None) > 400_000:
            raise DatabaseError("result too large; add LIMIT")
        return {"columns": columns, "rows": cells, "rowcount": len(cells), "truncated": truncated}

    return _execute(work)


def _vec_text(qvec) -> str:
    """pgvector text form "[0.1,0.2]", 6 significant digits — same as vec_text in tools/load_postgres.py."""
    return "[" + ",".join(f"{float(x):.6g}" for x in qvec) + "]"


def hybrid_search(q: str, k: int = 10, qvec=None, sector: str | None = None) -> list[dict]:
    """hybrid_search(q, qvec, k, sector) over passages, cards, vendors, equipment and sources;
    qvec (384 floats) optional, None means keyword only; sector (taxonomy code) optional."""
    k = max(1, min(50, int(k)))
    vec = _vec_text(qvec) if qvec is not None else None

    def work(cur):
        cur.execute("SELECT kind, ref, title, score FROM hybrid_search(%s, %s::vector, %s, %s)", (q, vec, k, sector))
        return _rows(cur)

    return _execute(work)


def graph_neighbors(node: str, depth: int = 1, rels: list[str] | None = None) -> list[dict]:
    """graph_neighbors(start_id, max_depth, rels): both directions; rels None or empty follows every relation."""
    depth = max(1, min(3, int(depth)))

    def work(cur):
        cur.execute("SELECT node_id, kind, label, depth, via FROM graph_neighbors(%s, %s, %s)",
                    (node, depth, list(rels) if rels else None))
        return _rows(cur)

    return _execute(work)


def node_row(node_id: str) -> dict | None:
    """One node by exact id, for the graph UI's details drawer. The id is validated, then bound."""
    if not NODE_ID.match(node_id or ""):
        raise BadSql("node id looks wrong; expected kind:key like technology:ccs-cryogenic")

    def work(cur):
        cur.execute("SELECT id, kind, label, props FROM node WHERE id = %s", (node_id,))
        rows = _rows(cur)
        return rows[0] if rows else None

    return _execute(work)


def top_node(kind: str) -> dict | None:
    """Highest-degree node of one kind: the atlas's suggested entry point into the network view."""
    if not NODE_KIND.match(kind or ""):
        raise BadSql("node kind looks wrong; expected a word like technology or vendor")

    def work(cur):
        cur.execute("SELECT n.id, n.label, count(e.src) AS degree FROM node n LEFT JOIN edge e ON e.src = n.id WHERE n.kind = %s GROUP BY n.id, n.label ORDER BY degree DESC, n.label LIMIT 1", (kind,))
        rows = _rows(cur)
        return rows[0] if rows else None

    return _execute(work)


def graph_overview() -> dict:
    """Node kinds, relations and kind-pair edge counts: the atlas and the network view's legend."""

    def work(cur):
        cur.execute("SELECT kind, count(*) AS n FROM node GROUP BY kind ORDER BY n DESC")
        kinds = _rows(cur)
        cur.execute("SELECT rel, count(*) AS n FROM edge GROUP BY rel ORDER BY n DESC")
        rels = _rows(cur)
        cur.execute("SELECT a.kind AS src_kind, b.kind AS dst_kind, e.rel, count(*) AS n FROM edge e JOIN node a ON a.id = e.src JOIN node b ON b.id = e.dst GROUP BY 1, 2, 3 ORDER BY n DESC")
        return {"kinds": kinds, "rels": rels, "pairs": _rows(cur)}

    return _execute(work)


def node_search(q: str, limit: int = 12) -> list[dict]:
    """Autocomplete over node labels and ids for the graph UI.

    The user's text is wildcard-escaped and bound as one parameter; the % wildcards around it are
    part of the static SQL ('%' || parameter || '%'), never assembled around input in Python.
    """
    limit = max(1, min(30, int(limit)))
    text = q.strip().replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")

    def work(cur):
        cur.execute("SELECT id, kind, label FROM node WHERE label LIKE '%' || %s || '%' ESCAPE '\\' OR id LIKE '%' || %s || '%' ESCAPE '\\' ORDER BY kind, label LIMIT %s", (text, text, limit))
        return _rows(cur)

    return _execute(work)


def neighborhood(node_id: str, depth: int = 1, rels: list[str] | None = None, limit: int = 150) -> dict | None:
    """Center node, its walk and every edge between the returned nodes: one payload for the network view."""
    if not NODE_ID.match(node_id or ""):
        raise BadSql("node id looks wrong; expected kind:key like technology:ccs-cryogenic")
    depth = max(1, min(3, int(depth)))
    limit = max(10, min(300, int(limit)))

    def work(cur):
        cur.execute("SELECT id, kind, label, props FROM node WHERE id = %s", (node_id,))
        center = _rows(cur)
        if not center:
            return None
        cur.execute("SELECT node_id, kind, label, depth, via FROM graph_neighbors(%s, %s, %s) LIMIT %s",
                    (node_id, depth, list(rels) if rels else None, limit))
        neighbors = _rows(cur)
        ids = [n["node_id"] for n in neighbors]
        ids.insert(0, node_id)
        cur.execute("SELECT id, kind, label, props FROM node WHERE id = ANY(%s)", (ids,))
        info = {r["id"]: r for r in _rows(cur)}
        for n in neighbors:
            row = info.get(n["node_id"]) or {}
            n["props"] = row.get("props") or {}
        cur.execute("SELECT src, dst, rel, weight FROM edge WHERE src = ANY(%s) AND dst = ANY(%s)", (ids, ids))
        return {"center": center[0], "neighbors": neighbors, "edges": _rows(cur),
                "truncated": len(neighbors) >= limit}

    return _execute(work)


_COUNTS_SQL = (
    "SELECT 'source' AS t, count(*) AS n FROM source"
    " UNION ALL SELECT 'document', count(*) FROM document"
    " UNION ALL SELECT 'chunk', count(*) FROM chunk"
    " UNION ALL SELECT 'technology', count(*) FROM technology"
    " UNION ALL SELECT 'vendor', count(*) FROM vendor"
    " UNION ALL SELECT 'equipment', count(*) FROM equipment"
    " UNION ALL SELECT 'register_entry', count(*) FROM register_entry"
    " UNION ALL SELECT 'node', count(*) FROM node"
    " UNION ALL SELECT 'edge', count(*) FROM edge"
)


def counts() -> dict:
    """Row counts of the main tables; static SQL because none of it comes from the caller."""

    def work(cur):
        cur.execute(_COUNTS_SQL)
        return {row["t"]: row["n"] for row in _rows(cur)}

    return _execute(work)


# ---------------------------------------------------------------- catalog reads for the web UI
# Decision #34 Phase 1: the web pages read Neon first (single source of truth) and fall back to
# the SQLite index in web.py. These helpers return rows shaped like their library.py /
# vendors.py / equipment.py counterparts so a handler renders identically from either source.

def _jsonb(value):
    """psycopg loads jsonb as Python objects already; explicit casts can still arrive as text."""
    return value if not isinstance(value, str) else json.loads(value)


def library_stats() -> dict:
    """library.stats() equivalent from live counts; no embedding_model key (Neon does not store it)."""

    def work(cur):
        cur.execute("SELECT count(*) FROM source")
        out = {"sources": cur.fetchone()[0]}
        cur.execute("SELECT count(*) FROM document")
        out["documents"] = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM chunk")
        out["chunks"] = cur.fetchone()[0]
        cur.execute("""SELECT (SELECT count(*) FROM chunk WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM technology WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM vendor WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM equipment WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM source WHERE embedding IS NOT NULL)""")
        out["vectors"] = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM technology")
        out["technologies"] = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM vendor")
        out["vendors"] = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM equipment")
        out["equipment"] = cur.fetchone()[0]
        return out

    return _execute(work)


def tech_cards() -> list[dict]:
    """Every card as the full card jsonb — pure functions over them live in technologies.py."""

    def work(cur):
        cur.execute("SELECT card FROM technology ORDER BY id")
        return [_jsonb(r[0]) for r in cur.fetchall()]

    return _execute(work)


def tech_card(tech_id: str) -> dict | None:
    """One card jsonb by id."""

    def work(cur):
        cur.execute("SELECT card FROM technology WHERE id = %s", (tech_id,))
        rows = cur.fetchall()
        return _jsonb(rows[0][0]) if rows else None

    return _execute(work)


def card_names() -> dict:
    """{technology id: name} for pages that render linked card names."""

    def work(cur):
        cur.execute("SELECT id, name FROM technology")
        return dict(cur.fetchall())

    return _execute(work)


def vendor_rows(role: str | None = None, sector: str | None = None, query: str | None = None) -> list[dict]:
    """Vendor rows shaped like vendors.summary, filtered exactly like library.list_vendors
    (role, sector via the cards' sectors, text over name/aliases/description/products/country)."""

    def work(cur):
        cur.execute("SELECT id, name, aliases, country, roles, description, products, url, technologies FROM vendor ORDER BY name")
        rows = cur.fetchall()
        cur.execute("SELECT id, sector FROM technology")
        sector_of = dict(cur.fetchall())
        out = []
        for vid, name, aliases, country, roles, description, products, url, technologies in rows:
            sectors = {sector_of[t] for t in (technologies or []) if t in sector_of}
            if role and role not in (roles or []):
                continue
            if sector and sector not in sectors:
                continue
            hay = " ".join([name, " ".join(aliases or []), description or "",
                            " ".join(products or []), country or ""]).lower()
            if query and query.lower() not in hay:
                continue
            out.append({"id": vid, "name": name, "country": country, "roles": roles or [],
                        "aliases": aliases or [], "products": products or [], "url": url,
                        "technologies": technologies or []})
        return out

    return _execute(work)


def vendor_row(vendor_id: str) -> dict | None:
    """One og.vendor row (columns only; og.vendor holds no sources/notes fields)."""

    def work(cur):
        cur.execute("SELECT id, name, aliases, country, roles, description, products, url, technologies FROM vendor WHERE id = %s", (vendor_id,))
        rows = cur.fetchall()
        if not rows:
            return None
        vid, name, aliases, country, roles, description, products, url, technologies = rows[0]
        return {"id": vid, "name": name, "aliases": aliases or [], "country": country, "roles": roles or [],
                "description": description, "products": products or [], "url": url, "technologies": technologies or []}

    return _execute(work)


def vendor_names() -> dict:
    """{vendor id: name} for pages that render linked vendor names."""

    def work(cur):
        cur.execute("SELECT id, name FROM vendor")
        return dict(cur.fetchall())

    return _execute(work)


def coverage_queue() -> tuple[list, list]:
    """(queue, notes) of supplier names on cards that no vendor record answers to — the same
    classifier as web._coverage_queue / tools/build.py, fed from og.technology and og.vendor."""

    def work(cur):
        cur.execute("SELECT id, sector, s->>'name' FROM technology, LATERAL jsonb_array_elements(card->'suppliers') s")
        suppliers = cur.fetchall()
        cur.execute("SELECT name, aliases FROM vendor")
        vendors = cur.fetchall()
        cards = [{"id": cid, "sector": sector, "suppliers": [{"name": name}]} for cid, sector, name in suppliers]
        records = [{"name": name, "aliases": aliases or []} for name, aliases in vendors]
        return _coverage_queue_from(cards, records)

    return _execute(work)


def _coverage_queue_from(cards, records):
    """Imported late so pg.py stays importable without the catalog loader modules."""
    import vendors as vendor_records

    return vendor_records.coverage_queue(cards, records)


def source_rows(code: str | None = None, region: str | None = None, reuse_level: str | None = None) -> list[dict]:
    """Catalog source rows shaped like library.list_by_tag output, filtered and sorted the same
    (Asia Pacific and Southeast Asia first, then quality tier, then name)."""

    def work(cur):
        cur.execute("""SELECT id, name, url, source_type, reuse_level, quality_tier,
                              record->'sectors', record->'disciplines', record->'regions'
                       FROM source ORDER BY id""")
        out = []
        for sid, name, url, stype, reuse, tier, sectors, disciplines, regions in cur.fetchall():
            sectors, disciplines, regions = _jsonb(sectors) or [], _jsonb(disciplines) or [], _jsonb(regions) or []
            if code and code not in sectors + disciplines:
                continue
            if (region and region not in regions) or (reuse_level and reuse_level != reuse):
                continue
            out.append({"id": sid, "name": name, "url": url, "source_type": stype, "regions": regions,
                        "reuse_level": reuse, "quality_tier": tier})
        out.sort(key=lambda r: (not ({"sea", "apac"} & set(r["regions"])), r["quality_tier"], r["name"].lower()))
        return out

    return _execute(work)


def source_row(source_id: str) -> dict | None:
    """Full catalog record for one source plus its collected documents (restricted ones dropped,
    as the hosted server's exclude_restricted behaviour does)."""

    def work(cur):
        cur.execute("SELECT record FROM source WHERE id = %s", (source_id,))
        rows = cur.fetchall()
        if not rows:
            return None
        rec = _jsonb(rows[0][0])
        cur.execute("SELECT id, title, url, reuse_level FROM document WHERE source_id = %s ORDER BY id", (source_id,))
        docs = [{"path": did, "title": title, "url": url} for did, title, url, d_reuse in cur.fetchall()
                if (d_reuse or rec.get("reuse_level")) != "full-text-restricted"]
        rec["documents"] = docs
        return rec

    return _execute(work)


def document_row(path: str) -> dict | None:
    """library.get_document equivalent from og.document: front matter and full text. Text of
    full-text-restricted documents is never returned — the stored body is ignored for them
    (the same licence gate the hosted server applies on its SQLite path)."""

    def work(cur):
        cur.execute("""SELECT d.id, d.meta, d.body, d.reuse_level, s.reuse_level
                       FROM document d LEFT JOIN source s ON s.id = d.source_id
                       WHERE d.id = %s""", (path.split("#")[0],))
        rows = cur.fetchall()
        if not rows:
            return None
        did, meta, body, d_reuse, s_reuse = rows[0]
        if (d_reuse or s_reuse) == "full-text-restricted":
            return {"path": did, "error": "Private reference copy; not served by this server. Cite the source url instead."}
        return {"path": did, "meta": _jsonb(meta) or {}, "text": body or ""}

    return _execute(work)


def gap_rows(sector: str | None = None, field: str | None = None) -> list[dict]:
    """list_gaps-shaped rows from v_gap (card gaps plus register entries with no card)."""

    def work(cur):
        sql = """SELECT technology_id, name, sector, field, item, reason_code, reason, "where", action, blocked_by
                 FROM v_gap"""
        conds, params = [], []
        if sector:
            conds.append("sector = %s")
            params.append(sector)
        if field:
            conds.append("field = %s")
            params.append(field)
        if conds:
            sql += " WHERE " + " AND ".join(conds)
        cur.execute(sql, params)
        return [{"card": tid, "technology": name, "sector": sector_, "field": f, "item": item,
                 "reason_code": rc, "reason": reason, "action": action, "blocked_by": blocked_by,
                 "where": _jsonb(where) or []}
                for tid, name, sector_, f, item, rc, reason, where, action, blocked_by in cur.fetchall()]

    return _execute(work)


def register_rows(code: str | None = None, maturity: str | None = None, query: str | None = None) -> list[dict]:
    """Register entries from og.register_entry, filtered like library.list_register (code,
    maturity, text over name/area/examples). Order is by id (code, then name), not the YAML's
    declaration order — content is identical."""

    def work(cur):
        cur.execute("SELECT sector, area, name, maturity, examples, card_id FROM register_entry ORDER BY id")
        q = (query or "").lower()
        return [{"code": code_, "area": area, "name": name, "maturity": maturity_, "examples": examples,
                 "card": card_id}
                for code_, area, name, maturity_, examples, card_id in cur.fetchall()
                if (not code or code_ == code) and (not maturity or maturity_ == maturity)
                and (not q or q in f"{name} {area} {examples}".lower())]

    return _execute(work)


def equipment_rows(equipment_type: str | None = None, query: str | None = None) -> list[dict]:
    """Equipment rows shaped like equipment.summary, filtered like library.list_equipment
    (text over name/aliases/description/spec metrics/vendors; og.equipment holds no aliases)."""

    def work(cur):
        cur.execute("SELECT id, name, equipment_type, sector, sector_codes, description, specifications, vendors, technologies FROM equipment ORDER BY name")
        out = []
        for eid, name, etype, sector, sector_codes, description, specifications, vendors, technologies in cur.fetchall():
            specifications = _jsonb(specifications) or []
            if equipment_type and equipment_type != etype:
                continue
            hay = " ".join([name, description or "",
                            " ".join(s["metric"] for s in specifications),
                            " ".join(vendors or [])]).lower()
            if query and query.lower() not in hay:
                continue
            out.append({"id": eid, "name": name, "equipment_type": etype, "sector": sector,
                        "sector_codes": sector_codes or [], "aliases": [],
                        "spec_metrics": [s["metric"] for s in specifications],
                        "vendors": vendors or [], "technologies": technologies or []})
        return out

    return _execute(work)


def equipment_row(equipment_id: str) -> dict | None:
    """One og.equipment row with every field the equipment page's detail panel renders
    (specifications, vendor_models, gaps, vendors, technologies, sources, description)."""

    def work(cur):
        cur.execute("""SELECT id, name, equipment_type, sector, sector_codes, description, specifications,
                              vendor_models, vendors, technologies, gaps, sources
                       FROM equipment WHERE id = %s""", (equipment_id,))
        rows = cur.fetchall()
        if not rows:
            return None
        (eid, name, etype, sector, sector_codes, description, specifications, vendor_models,
         vendors, technologies, gaps, sources) = rows[0]
        return {"id": eid, "name": name, "equipment_type": etype, "sector": sector,
                "sector_codes": sector_codes or [], "description": description,
                "specifications": _jsonb(specifications) or [], "vendor_models": _jsonb(vendor_models) or [],
                "vendors": vendors or [], "technologies": technologies or [],
                "gaps": _jsonb(gaps) or [], "sources": _jsonb(sources) or []}

    return _execute(work)


def search_vector_count() -> int:
    """Rows with an embedding, across every embedded kind — the /search page's honest
    semantic badge (the SQLite path counts the same rows in its vectors table)."""

    def work(cur):
        cur.execute("""SELECT (SELECT count(*) FROM chunk WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM technology WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM vendor WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM equipment WHERE embedding IS NOT NULL)
                            + (SELECT count(*) FROM source WHERE embedding IS NOT NULL)""")
        return cur.fetchone()[0]

    return _execute(work)


def drift_stamp() -> dict:
    """The data version (R4): row counts, the vector total and the freshest review/verify dates,
    so frontend/backend/data agreement is visible at a glance via /api/version."""
    out = {"counts": {k: counts().get(k) for k in
                      ("source", "document", "chunk", "technology", "vendor", "equipment", "register_entry")}}

    def work(cur):
        cur.execute("SELECT max(last_reviewed) FROM technology")
        out["last_reviewed"] = cur.fetchone()[0]
        cur.execute("SELECT max(last_verified) FROM source")
        out["last_verified"] = cur.fetchone()[0]
        return None

    _execute(work)
    out["vectors"] = search_vector_count()
    return out


def search_library(q: str, kind: str = "all", sector: str | None = None, limit: int = 10, qvec=None) -> list[dict]:
    """library.search equivalent from Neon: hybrid_search ranking, then one enrichment query per
    kind so rows carry the fields the web page and REST render (licence, snippet, roles, ...)."""
    kinds = ("source", "chunk", "technology", "vendor", "equipment") if kind == "all" else (kind,)
    hits = hybrid_search(q, min(max(1, int(limit)), 50), qvec, sector)
    by_kind = {}
    for h in hits:
        if h["kind"] in kinds:
            by_kind.setdefault(h["kind"], []).append(h["ref"])
    out = []

    def work(cur):
        if "technology" in by_kind:
            import technologies  # noqa: F401  (late import; pure functions over the card jsonb)
            cur.execute("SELECT id, name, maturity, category, card FROM technology WHERE id = ANY(%s)", (by_kind["technology"],))
            by_id = {r[0]: r for r in cur.fetchall()}
            for h in hits:
                if h["kind"] == "technology" and h["ref"] in by_id:
                    _, name, maturity, category, card = by_id[h["ref"]]
                    row = {"kind": "technology", "ref": h["ref"], "title": name, "score": round(h["score"], 4),
                           "licence": "Library's own summary of cited sources; cite the sources listed in the card",
                           "reuse_level": "full-text-open", "permitted_use": "any",
                           "hint": "Call get_technology for the block diagram, figures and sources."}
                    row.update(technologies.summary(_jsonb(card)))
                    row["title"] = name
                    out.append(row)
        if "vendor" in by_kind:
            cur.execute("SELECT id, country, roles, products, technologies FROM vendor WHERE id = ANY(%s)", (by_kind["vendor"],))
            by_id = {r[0]: r for r in cur.fetchall()}
            for h in hits:
                if h["kind"] == "vendor" and h["ref"] in by_id:
                    _, country, roles, products, technologies = by_id[h["ref"]]
                    out.append({"kind": "vendor", "ref": h["ref"], "title": h["title"], "score": round(h["score"], 4),
                                "licence": "Library's own curated vendor record; cite the sources listed in the record",
                                "reuse_level": "full-text-open", "permitted_use": "any",
                                "country": country, "roles": roles or [], "products": products or [],
                                "technologies": technologies or [],
                                "hint": "Call get_vendor for the full record and the sources behind it."})
        if "equipment" in by_kind:
            cur.execute("SELECT id, equipment_type, vendors FROM equipment WHERE id = ANY(%s)", (by_kind["equipment"],))
            by_id = {r[0]: r for r in cur.fetchall()}
            for h in hits:
                if h["kind"] == "equipment" and h["ref"] in by_id:
                    _, etype, vendors_ = by_id[h["ref"]]
                    out.append({"kind": "equipment", "ref": h["ref"], "title": h["title"], "score": round(h["score"], 4),
                                "licence": "Library's own curated equipment record; cite the sources listed in the record",
                                "reuse_level": "full-text-open", "permitted_use": "any",
                                "equipment_type": etype, "vendors": vendors_ or [], "spec_metrics": [],
                                "hint": "Call get_equipment for the specification ranges, vendor model lines and sources."})
        if "source" in by_kind:
            cur.execute("SELECT id, url, licence, reuse_level, permitted_use, record->'sectors', record->'regions', record->'disciplines' FROM source WHERE id = ANY(%s)", (by_kind["source"],))
            by_id = {r[0]: r for r in cur.fetchall()}
            for h in hits:
                if h["kind"] == "source" and h["ref"] in by_id:
                    _, url, licence, reuse, permitted, sectors, regions, disciplines = by_id[h["ref"]]
                    out.append({"kind": "source", "ref": h["ref"], "title": h["title"], "score": round(h["score"], 4),
                                "licence": licence, "reuse_level": reuse, "permitted_use": permitted or "unstated",
                                "url": url, "regions": _jsonb(regions) or [], "sectors": _jsonb(sectors) or [],
                                "disciplines": _jsonb(disciplines) or []})
        if "chunk" in by_kind:
            cur.execute("""SELECT c.id, d.url, d.licence, d.reuse_level, d.summary, c.body, d.source_id
                           FROM chunk c JOIN document d ON d.id = c.document_id
                           WHERE c.id = ANY(%s)""", (by_kind["chunk"],))
            by_id = {r[0]: r for r in cur.fetchall()}
            for h in hits:
                if h["kind"] == "chunk" and h["ref"] in by_id:
                    _, url, licence, reuse, summary, body, source_id = by_id[h["ref"]]
                    row = {"kind": "chunk", "ref": h["ref"], "title": h["title"], "score": round(h["score"], 4),
                           "licence": licence, "reuse_level": reuse, "permitted_use": "unstated",
                           "path": h["ref"].split("#")[0], "url": url, "snippet": (body or "")[:400]}
                    if summary:
                        row["summary"] = summary
                    out.append(row)
        # keep the hybrid_search ranking order across kinds
        order = {h["ref"]: i for i, h in enumerate(hits)}
        out.sort(key=lambda r: order.get(r["ref"], 10**9))
        return out

    return _execute(work)


def tables_doc() -> dict:
    """Static schema description for the db_catalog MCP tool and the web /database page."""
    return {
        "tables": [
            {"name": "source",
             "columns": ["id", "name", "url", "source_type", "publisher_org", "country", "access", "licence",
                         "reuse_level", "permitted_use", "automated_access", "quality_tier", "verification",
                         "last_verified", "update_frequency", "notes", "record jsonb", "embedding", "tsv"],
             "holds": "one row per catalog record"},
            {"name": "source_tag",
             "columns": ["source_id", "kind", "code"],
             "holds": "taxonomy tags; kind is sector, discipline or region"},
            {"name": "document",
             "columns": ["id", "source_id", "title", "url", "licence", "reuse_level", "retrieved_at", "sha256",
                         "sectors[]", "text_included", "summary", "body", "meta jsonb"],
             "holds": "corpus documents; restricted ones have text_included=false and no passages; "
                      "body holds the full text of open-licence documents only"},
            {"name": "chunk",
             "columns": ["id", "document_id", "ord", "title", "body", "embedding vector(384)", "tsv"],
             "holds": "passages of open-licence documents"},
            {"name": "technology",
             "columns": ["id", "name", "sector", "category", "maturity", "principle", "trl_low", "trl_high",
                         "last_reviewed", "card jsonb", "embedding", "tsv"],
             "holds": "technology cards"},
            {"name": "technology_alias",
             "columns": ["technology_id", "alias"],
             "holds": "card children: aliases"},
            {"name": "technology_source",
             "columns": ["technology_id", "url", "source_id", "note"],
             "holds": "card children: citations with source_id"},
            {"name": "technology_figure",
             "columns": ["id", "technology_id", "kind", "metric", "low", "high", "unit", "year", "basis", "source_url"],
             "holds": "card children: performance and cost figures with unit/year/basis/source_url"},
            {"name": "technology_supplier",
             "columns": ["technology_id", "supplier", "product", "source_id"],
             "holds": "card children: suppliers"},
            {"name": "technology_gap",
             "columns": ["technology_id", "field", "item", "reason_code", "reason", "action", "blocked_by", "where"],
             "holds": "card children: gaps with reason_code/reason/action/where"},
            {"name": "vendor",
             "columns": ["id", "name", "aliases[]", "country", "roles[]", "description", "products[]", "url", "technologies[]",
                         "embedding", "tsv"],
             "holds": "curated vendor directory records; technologies[] holds the card ids they supply"},
            {"name": "equipment",
             "columns": ["id", "name", "equipment_type", "sector", "sector_codes[]", "description",
                         "specifications jsonb", "vendor_models jsonb", "vendors[]", "technologies[]",
                         "gaps jsonb", "sources jsonb", "embedding", "tsv"],
             "holds": "curated equipment catalog records (one per equipment class, boilers first); "
                      "specifications hold metric/range/basis/source and vendor_models the model lines"},
            {"name": "register_entry",
             "columns": ["id", "sector", "area", "name", "maturity", "examples", "card_id"],
             "holds": "the ~300-technology register"},
            {"name": "node",
             "columns": ["id", "kind", "label", "props", "embedding"],
             "holds": "knowledge graph nodes with ids \"<kind>:<key>\" (source:netl, document:corpus/..., "
                      "technology:ccs-cryogenic, register:CCS/..., org:honeywell-uop, vendor:wartsila, "
                      "equipment:boiler-hrsg, sector:CCS, "
                      "discipline:PRC, region:sea, country:MY, gap:<card>:<n>)"},
            {"name": "edge",
             "columns": ["src", "dst", "rel", "weight", "props"],
             "holds": "knowledge graph edges; relations published_by, in_sector, covers_discipline, in_region, "
                      "in_country, from_source, cites, cites_document, supplied_by, realised_by, example_supplier, "
                      "alternative_to, mentions, has_gap, look_in, supplies, supplies_equipment, uses_equipment, "
                      "alias_of, similar_to"},
        ],
        "views": [
            {"name": "v_gap",
             "holds": "everything missing from the cards, with reason_code, where to look and action"},
            {"name": "v_technology_co_citation",
             "holds": "pairs of cards citing the same sources"},
        ],
        "functions": [
            {"name": "graph_neighbors", "signature": "start_id text, max_depth int, rels text[]",
             "does": "recursive walk of the graph, both directions"},
            {"name": "hybrid_search", "signature": "q text, qvec vector(384), k int, sector text",
             "does": "reciprocal-rank fusion of full-text and vector search over passages, cards, vendors, "
                     "equipment and catalog sources; qvec/sector optional"},
            {"name": "refresh_similarity", "signature": "k int, min_sim float",
             "does": "rebuilds similar_to edges (write path, loader only)"},
        ],
    }


def readonly_dsn(owner_dsn: str, user: str = "og_mcp_read", password: str = "") -> str:
    """The owner DSN with the credentials swapped for the read-only role; host, port, db and query unchanged."""
    parts = urllib.parse.urlsplit(owner_dsn)
    netloc = parts.netloc.rpartition("@")[2]
    creds = urllib.parse.quote(user, safe="") + (":" + urllib.parse.quote(password, safe="") if password else "")
    return urllib.parse.urlunsplit((parts.scheme, creds + "@" + netloc, parts.path, parts.query, parts.fragment))


def _unpooled_dsn(dsn: str) -> str:
    """Neon's <host>-pooler hosts give transaction mode; the same DSN without -pooler gives session mode."""
    parts = urllib.parse.urlsplit(dsn)
    host = parts.hostname or ""
    if "-pooler" not in host:
        return dsn
    userinfo, at, _ = parts.netloc.rpartition("@")
    direct = host.replace("-pooler", "", 1)
    if ":" in direct:
        direct = f"[{direct}]"
    if parts.port:
        direct += f":{parts.port}"
    netloc = userinfo + "@" + direct if at else direct
    return urllib.parse.urlunsplit((parts.scheme, netloc, parts.path, parts.query, parts.fragment))
