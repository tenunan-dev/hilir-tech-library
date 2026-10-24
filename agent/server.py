"""MCP server exposing the library to agents (Claude Desktop, Claude Code, any MCP client).

    pip install -r requirements-agent.txt
    python agent/library.py build
    python agent/server.py                      # stdio, for agents on this machine
    LIBRARY_API_KEY=... python agent/server.py --http --port 8000
                                                # streamable HTTP at /mcp, for hosted agents
                                                # (Copilot Studio, claude.ai connectors, others)

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
import embed  # noqa: E402
import library  # noqa: E402

try:
    from mcp.server.mcpserver import MCPServer as Server
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as Server

INSTRUCTIONS = """Library of public sources on oil, gas, petrochemical and energy technologies,
weighted toward Asia Pacific and Southeast Asia. Sector codes: UPS, MID, GAS, REF, PCH, PWR, H2, CCS.
Discipline codes: PRC, ROT, INS, MAT, HSE, DIG. Regions include sea, apac, global.
For "what are the options for X" questions, start with compare_technologies and get_technology
(curated cards with block diagrams, equipment, costs with basis, and sources), then search for more.
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
    """Search catalog sources and collected documents.

    kind: "all", "source" (catalog records) or "chunk" (passages from collected documents).
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
def library_stats() -> dict:
    """Counts of sources, documents, chunks and vectors in the index."""
    return library.stats(db())


class RequireApiKey:
    """ASGI middleware: reject requests without the API key (x-api-key or Authorization: Bearer)."""

    def __init__(self, app, key):
        self.app, self.key = app, key.encode()

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
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
