"""MCP server exposing the library to agents (Claude Desktop, Claude Code, any MCP client).

    pip install -r requirements-agent.txt
    python agent/library.py build
    python agent/server.py            # stdio transport

Every result carries the source's licence, reuse_level and permitted_use. Agents must cite
the url, and must not redistribute text from full-text-restricted sources.
"""
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
Always cite a result's url. Respect reuse_level: full-text-restricted text is a private reference
copy (no redistribution or commercial use); summary-only and catalog-only sources have no stored text."""

server = Server("og-tech-sources", instructions=INSTRUCTIONS)
_db = None
_embedder = False


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
    return library.search(query, kind, sector, discipline, region, reuse_level, min(limit, 50), database, _embedder or None)


@server.tool()
def get_source(source_id: str) -> dict | None:
    """Full catalog record for one source, with the list of its collected documents."""
    return library.get_source(source_id, db())


@server.tool()
def get_document(path: str) -> dict | None:
    """Front matter and full text of one collected document, by the path a search result gave."""
    return library.get_document(path, db())


@server.tool()
def list_by_tag(code: str | None = None, region: str | None = None, reuse_level: str | None = None,
                source_type: str | None = None) -> list[dict]:
    """List catalog sources by sector or discipline code, region, reuse level or source type."""
    return library.list_by_tag(code, region, reuse_level, source_type, db())


@server.tool()
def library_stats() -> dict:
    """Counts of sources, documents, chunks and vectors in the index."""
    return library.stats(db())


if __name__ == "__main__":
    server.run()
