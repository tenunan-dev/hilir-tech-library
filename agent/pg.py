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
