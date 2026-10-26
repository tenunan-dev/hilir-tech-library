"""MCP server exposing the library to agents (Claude Desktop, Claude Code, any MCP client).

    pip install -r requirements-agent.txt
    python agent/library.py build
    python agent/server.py                      # stdio, for agents on this machine
    LIBRARY_API_KEY=... python agent/server.py --http --port 8000
                                                # streamable HTTP at /mcp, for hosted agents
                                                # (Copilot Studio, claude.ai connectors, others),
                                                # plus a REST API under /api (see agent/api.py)
An HTML web interface (cards, catalog, gaps, database console) is served under / — see agent/web.py; set DATABASE_URL (a read-only DSN) to enable the Postgres-backed tools.

HTTP mode requires an API key (header x-api-key, or Authorization: Bearer <key>) and by
default does not serve text from full-text-restricted sources, because people other than the
owner may reach it. --include-restricted turns that off for a server only the owner can use.
LIBRARY_ALLOWED_HOSTS (comma-separated) enables Host header checks behind a known hostname.

Every result carries the source's licence, reuse_level and permitted_use. Agents must cite
the url, and must not redistribute text from full-text-restricted sources.
"""
import argparse
import hmac
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import api  # noqa: E402
import embed  # noqa: E402
import library  # noqa: E402
import pg  # noqa: E402
import web  # noqa: E402

try:
    from mcp.server.mcpserver import MCPServer as Server
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as Server

INSTRUCTIONS = """Library of public sources on oil, gas, petrochemical and energy technologies,
weighted toward Asia Pacific and Southeast Asia. Sector codes: UPS, MID, GAS, REF, PCH, PWR, H2, CCS.
Discipline codes: PRC, ROT, INS, MAT, HSE, DIG. Regions include sea, apac, global.
For "what are the options for X" questions, start with compare_technologies and get_technology
(curated cards with block diagrams, equipment, costs with basis, and sources), then search for more.
For who-supplies-it questions, use list_vendors and get_vendor (curated vendor records citing their pages).
Always cite a result's url. Respect reuse_level: full-text-restricted text is a private reference
copy (no redistribution or commercial use); summary-only and catalog-only sources have no stored text."""

server = Server("og-tech-sources", instructions=INSTRUCTIONS)
_db = None
_embedder = False
EXCLUDE_RESTRICTED = False


def db():
    global _db, _embedder
    if _db is None:
        if not library.DB_PATH.exists():
            library.build()
        _db = library.connect()
        _embedder = embed.load_embedder(_db)
    return _db


@server.tool()
def search(query: str, kind: str = "all", sector: str | None = None, discipline: str | None = None,
           region: str | None = None, reuse_level: str | None = None, limit: int = 10) -> list[dict]:
    """Search catalog sources, collected documents, technology cards and vendor records.

    kind: "all", "source" (catalog records), "chunk" (passages from collected documents),
    "technology" (cards) or "vendor" (vendor directory records).
    sector / discipline: a taxonomy code such as H2 or ROT. region: e.g. sea, apac, global.
    """
    database = db()
    return library.search(query, kind, sector, discipline, region, reuse_level, min(limit, 50), database,
                          _embedder or None, EXCLUDE_RESTRICTED)


@server.tool()
def get_source(source_id: str) -> dict | None:
    """Full catalog record for one source, with the list of its collected documents."""
    return library.get_source(source_id, db(), EXCLUDE_RESTRICTED)


@server.tool()
def get_document(path: str) -> dict | None:
    """Front matter and full text of one collected document, by the path a search result gave."""
    return library.get_document(path, db(), EXCLUDE_RESTRICTED)


@server.tool()
def list_by_tag(code: str | None = None, region: str | None = None, reuse_level: str | None = None,
                source_type: str | None = None) -> list[dict]:
    """List catalog sources by sector or discipline code, region, reuse level or source type."""
    return library.list_by_tag(code, region, reuse_level, source_type, db())


@server.tool()
def get_technology(technology_id: str) -> dict | None:
    """One technology card: principle, process steps with equipment, block flow diagram (Mermaid),
    key equipment, performance and cost figures with their basis and source, suppliers, reference plants."""
    return library.get_technology(technology_id, db())


@server.tool()
def compare_technologies(sector: str | None = None, maturity: str | None = None,
                         application: str | None = None) -> list[dict]:
    """Comparison table of technology options, commercial first. sector: e.g. CCS.
    maturity: commercial, demonstration, pilot or lab. application: e.g. cement, power, hydrogen."""
    return library.compare_technologies(sector, maturity, application, db())


@server.tool()
def list_vendors(role: str | None = None, sector: str | None = None, query: str | None = None) -> list[dict]:
    """The vendor directory: curated records for suppliers, OEMs, licensors and packagers, each citing
    the pages it was written from. role: oem, licensor, packager, epc, developer, operator, rental,
    service, supplier or integrator. sector: a taxonomy code such as PWR or CCS. query: text."""
    return library.list_vendors(role, sector, query, db())


@server.tool()
def get_vendor(vendor_id: str) -> dict | None:
    """One vendor record: country, roles, products, the technology cards it supplies, and the sources behind it."""
    return library.get_vendor(vendor_id, db())


@server.tool()
def list_technology_register(code: str | None = None, maturity: str | None = None, query: str | None = None) -> list[dict]:
    """The full register of about 300 technologies across all sectors (code: UPS, MID, GAS, REF, PCH, PWR, H2,
    CCS, or a discipline code for cross-cutting equipment). Maturity and examples are indicative and unverified;
    entries with a "card" id have a verified technology card (use get_technology)."""
    return library.list_register(code, maturity, query)


@server.tool()
def list_gaps(sector: str | None = None, field: str | None = None, reason_code: str | None = None,
              include_no_card: bool = False) -> list[dict]:
    """Inputs the technology cards still lack, each with why it is missing (reason_code: not_in_sources_read,
    source_unreachable, source_not_collected, paid_source, status_unchecked, conflicting_sources,
    general_knowledge_only), where to get it, the next action and any blocker. field: trl, performance, costs,
    reference_plants, suppliers, status, process, other. include_no_card adds register technologies with no card.
    Use it to tell users what the library cannot answer yet, or to pick the next collection task."""
    return library.list_gaps(sector, field, reason_code, include_no_card, db())


@server.tool()
def library_stats() -> dict:
    """Counts of sources, documents, chunks and vectors in the index."""
    return library.stats(db())


@server.tool()
def sql_query(sql: str, max_rows: int = 100) -> dict:
    """Run ONE read-only SQL statement against the library's Postgres layer (schema og: catalog
    sources, documents and passages with vectors, technology cards, the register, the knowledge
    graph). Read db_catalog first for the table reference. One SELECT or WITH statement only —
    no semicolon, no comments. Read-only role, 15 s statement timeout, at most 500 rows."""
    try:
        return pg.run_sql(sql, max_rows)
    except pg.NotConfigured:
        return {"error": "database not configured: set DATABASE_URL (read-only DSN) and reload"}
    except (pg.BadSql, pg.DatabaseError) as e:
        return {"error": str(e)}


@server.tool()
def db_catalog() -> dict:
    """Reference for the Postgres layer — tables and their columns, views, and the
    graph_neighbors / hybrid_search functions. Read this before writing sql_query statements."""
    try:
        return pg.tables_doc()
    except pg.NotConfigured:
        return {"error": "database not configured: set DATABASE_URL (read-only DSN) and reload"}


@server.tool()
def graph_neighbors(node: str, depth: int = 1, rels: list[str] | None = None) -> list[dict] | dict:
    """Walk the knowledge graph from one node (ids like technology:ccs-cryogenic, source:netl,
    org:honeywell-uop, sector:CCS). depth 1-3; rels limits relations (cites, supplied_by,
    similar_to, mentions, ...; None follows all)."""
    try:
        return pg.graph_neighbors(node, depth, rels)
    except pg.NotConfigured:
        return {"error": "database not configured: set DATABASE_URL (read-only DSN) and reload"}
    except (pg.BadSql, pg.DatabaseError) as e:
        return {"error": str(e)}


class RequireApiKey:
    """ASGI middleware: reject requests without the API key (x-api-key or Authorization: Bearer)."""

    def __init__(self, app, key):
        self.app, self.key = app, key.encode()

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and scope["path"] not in api.PUBLIC_PATHS and not web.is_web_path(scope["path"]):
            headers = dict(scope["headers"])
            given = headers.get(b"x-api-key") or headers.get(b"authorization", b"").removeprefix(b"Bearer ").strip()
            if not hmac.compare_digest(given, self.key):
                await send({"type": "http.response.start", "status": 401,
                            "headers": [(b"content-type", b"application/json")]})
                await send({"type": "http.response.body", "body": b'{"error": "missing or wrong API key"}'})
                return
        await self.app(scope, receive, send)


def http_app(key):
    hosts = [h.strip() for h in os.environ.get("LIBRARY_ALLOWED_HOSTS", "").split(",") if h.strip()]
    try:
        from mcp.server.transport_security import TransportSecuritySettings
        security = TransportSecuritySettings(enable_dns_rebinding_protection=bool(hosts), allowed_hosts=hosts)
        app = server.streamable_http_app(stateless_http=True, json_response=True, transport_security=security, host="0.0.0.0")
    except TypeError:  # mcp 1.x takes these as server settings
        server.settings.stateless_http = True
        server.settings.json_response = True
        app = server.streamable_http_app()
    app.router.routes.extend(api.routes(sys.modules[__name__]))  # REST API for agents without MCP
    app.router.routes.extend(web.routes(sys.modules[__name__], key))
    return RequireApiKey(app, key)


def main(argv=None):
    global EXCLUDE_RESTRICTED
    ap = argparse.ArgumentParser()
    ap.add_argument("--http", action="store_true", help="serve streamable HTTP at /mcp instead of stdio")
    ap.add_argument("--host", default="0.0.0.0")
    ap.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8000)))
    ap.add_argument("--include-restricted", action="store_true",
                    help="HTTP mode: also serve full-text-restricted text (only if no one but the owner can reach it)")
    args = ap.parse_args(argv)
    if not args.http:
        server.run()
        return 0
    key = os.environ.get("LIBRARY_API_KEY", "")
    if len(key) < 24:
        print("Set LIBRARY_API_KEY (at least 24 characters) before serving over HTTP.", file=sys.stderr)
        return 2
    EXCLUDE_RESTRICTED = not args.include_restricted
    db()
    import uvicorn
    uvicorn.run(http_app(key), host=args.host, port=args.port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
