"""MCP server exposing the library to agents (Claude Desktop, Claude Code, any MCP client).

    pip install -r requirements-agent.txt
    python agent/library.py build
    python agent/server.py                      # stdio, for agents on this machine
    python agent/server.py --http --port 8000   # streamable HTTP at /mcp, for hosted agents
                                                # (Copilot Studio, claude.ai connectors, others),
                                                # plus a REST API under /api (see agent/api.py)
An HTML web interface (cards, catalog, gaps, database console) is served under / — see agent/web.py; set DATABASE_URL (a read-only DSN) to enable the Postgres-backed tools.

HTTP mode requires a hilir Access bearer token (Authorization: Bearer <access
token>, forwarded by the edge, verified here against the issuer's JWKS) and by
default does not serve text from full-text-restricted sources, because people
other than the owner may reach it. --include-restricted turns that off for a
server only the owner can use.
LIBRARY_ALLOWED_HOSTS (comma-separated) enables Host header checks behind a known hostname.

Every result carries the source's licence, reuse_level and permitted_use. Agents must cite
the url, and must not redistribute text from full-text-restricted sources.
"""
import argparse
import os
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import api  # noqa: E402
import auth as hilir_auth  # noqa: E402 — hilir Access token verification
import embed  # noqa: E402
import library  # noqa: E402
import pg  # noqa: E402
import technologies  # noqa: E402
import userstore  # noqa: E402
import web  # noqa: E402

# The PUBLIC origin of this API (RFC 9728 metadata must name it, not the Caddy
# tunnel upstream that appears in the proxied Host header).
MCP_PUBLIC_ORIGIN = os.environ.get("LIBRARY_MCP_ORIGIN", "https://techlib-api.hilir.app")

try:
    from mcp.server.mcpserver import MCPServer as Server
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as Server

INSTRUCTIONS = """A curated library of public sources, technology cards, vendors, projects and figures for oil,
gas, petrochemical, power, hydrogen, CCUS, data-centre, water and industrial-decarbonisation work,
weighted toward Asia Pacific and Southeast Asia. Everything here is evidence-linked: a card, vendor,
project or figure is only recorded because a page was read, and each carries the page it came from.

TERMINOLOGY: a "card" is a technology card (one technology, with principle, process steps, suppliers,
figures, reference plants, gaps). "Sector codes" are UPS, MID, GAS, REF, PCH, PWR, H2, CCS, IDC, WWT.
"Discipline codes" are PRC, ROT, ELE, CIV, INS, MAT, HSE, DIG. Call taxonomy() when you need the exact
code list with names and subtopics rather than guessing.

ROUTING — pick the tool by the question being asked:
- "What are the options for X?" -> compare_technologies, then get_technology on the interesting ids.
- "How much does X cost / how efficient is X?" -> find_figures (returns every recorded figure with
  its basis, dollar year and source url). Use get_technology when you want the whole card.
- "Who supplies X / what does vendor Y make?" -> list_vendors, then get_vendor.
- "What equipment classes exist and what are their limits?" -> list_equipment, then get_equipment.
- "Which plants or projects use X, or what is built in country Z?" -> list_projects (filter by
  status, sector or country), get_project.
- "What does this acronym mean?" -> get_glossary_term (or list_glossary to browse).
- "Which standard applies?" -> list_standards / get_standard (designation, title, scope, url).
- "Find me sources or text about X" -> search (kind: all/source/chunk/technology/vendor/equipment/
  project), then get_source or get_document for the full record or text.
- "What does the library not know yet?" -> list_gaps (per-card missing inputs with reason and next
  action), and list_technology_register for the indicative register including entries with no card.
- "How are these things connected?" -> graph_neighbors (technology, vendor, project, source nodes).
- "Give me counts / is the data current?" -> library_stats.
- Anything the tools above do not express -> sql_query against the read-only Postgres layer; call
  db_catalog first for tables, views and columns.

RULES THAT MATTER:
1. Cite the url (source_url, url, or the source note) for every factual claim you take from here.
2. Respect reuse_level: full-text-restricted means a private reference copy — quote briefly and never
   redistribute; summary-only and catalog-only sources have no stored text.
3. A figure without its basis is not usable. Prefer figures whose basis names the scope (installed vs
   overnight vs LCOE, per kW vs per kWh, dollar year). If a card records no figure, say so and point
   at the gap rather than estimating.
4. Cards record gaps deliberately; when a gap exists, tell the user what is missing instead of filling
   it yourself.
5. Maturity and register entries are indicative unless a card exists (cards are the verified layer)."""

server = Server("hilir-tech-library", instructions=INSTRUCTIONS)
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


def _with_neon(pg_call, fallback):
    """Decision #34: Neon is the live data layer — a publish shows up in the tools without a
    deploy. The baked SQLite index is the automatic fallback (no database configured, or the
    database unreachable)."""
    if pg.configured():
        try:
            return pg_call()
        except (pg.NotConfigured, pg.DatabaseError):
            pass
    return fallback()


@server.tool()
def search(query: str, kind: str = "all", sector: str | None = None, discipline: str | None = None,
           region: str | None = None, reuse_level: str | None = None, limit: int = 10) -> list[dict]:
    """Search catalog sources, collected documents, technology cards, vendor and equipment records.

    kind: "all", "source" (catalog records), "chunk" (passages from collected documents),
    "technology" (cards), "vendor" (vendor directory records), "equipment" (equipment classes)
    or "project" (named projects and operating plants).
    sector / discipline: a taxonomy code such as H2 or ROT. region: e.g. sea, apac, global.
    """
    # Decision #34: with a database configured, search runs on Neon (single source of truth —
    # a publish shows up here without a deploy); the SQLite index is the fallback. All filters
    # are honoured on both paths, and passages of full-text-restricted documents never surface
    # from either.
    if pg.configured():
        try:
            import embed as embed_module
            embedder = embed_module.load_embedder(db())
            qvec = list(embedder([query])[0]) if embedder else _query_vector(query)
            return pg.search_library(query, kind, sector, min(limit, 50), qvec, discipline, region, reuse_level)
        except (pg.NotConfigured, pg.DatabaseError):
            pass
    database = db()
    # Local fastembed first (_embedder); the hosted container has none, so it asks the
    # edge /__embed service for the query vector instead (decision #32).
    qvec = None
    if not _embedder:
        try:
            import embed_client
            qvec = embed_client.query_vector(query)
        except Exception:
            qvec = None
    return library.search(query, kind, sector, discipline, region, reuse_level, min(limit, 50), database,
                          _embedder or None, EXCLUDE_RESTRICTED, query_vector=qvec)


def _query_vector(query: str):
    """Query embedding without the SQLite index's model row (the split containers keep no
    embeddings): local fastembed with the default model, else the edge /__embed service."""
    try:
        import embed as embed_module
        model = embed_module._model(embed_module.DEFAULT_MODEL)

        def embed(texts):
            import numpy as np
            return [np.asarray(v, dtype=np.float32) / np.linalg.norm(v) for v in model.query_embed(texts)]
        return list(embed([query])[0])
    except Exception:
        try:
            import embed_client
            return embed_client.query_vector(query)
        except Exception:
            return None


@server.tool()
def get_source(source_id: str) -> dict | None:
    """Full catalog record for one source, with the list of its collected documents."""
    return _with_neon(lambda: pg.source_row(source_id),
                      lambda: library.get_source(source_id, db(), EXCLUDE_RESTRICTED))


@server.tool()
def get_document(path: str) -> dict | None:
    """Front matter and full text of one collected document, by the path a search result gave."""
    return _with_neon(lambda: pg.document_row(path),
                      lambda: library.get_document(path, db(), EXCLUDE_RESTRICTED))


@server.tool()
def list_by_tag(code: str | None = None, region: str | None = None, reuse_level: str | None = None,
                source_type: str | None = None) -> list[dict]:
    """List catalog sources by sector or discipline code, region, reuse level or source type."""
    return _with_neon(lambda: pg.source_rows(code, region, reuse_level, source_type),
                      lambda: library.list_by_tag(code, region, reuse_level, source_type, db()))


@server.tool()
def get_technology(technology_id: str) -> dict | None:
    """One technology card: principle, process steps with equipment, block flow diagram (Mermaid),
    key equipment, performance and cost figures with their basis and source, suppliers, reference plants."""
    def neon():
        card = pg.tech_card(technology_id)
        if card is not None:
            card["block_diagram_mermaid"] = technologies.mermaid(card)
            card["licence"] = library.TECHNOLOGY_LICENCE
        return card
    return _with_neon(neon, lambda: library.get_technology(technology_id, db()))


@server.tool()
def compare_technologies(sector: str | None = None, maturity: str | None = None,
                         application: str | None = None) -> list[dict]:
    """Comparison table of technology options, commercial first. sector: e.g. CCS.
    maturity: commercial, demonstration, pilot or lab. application: e.g. cement, power, hydrogen."""
    return _with_neon(lambda: technologies.compare(pg.tech_cards(), sector, maturity, application),
                      lambda: library.compare_technologies(sector, maturity, application, db()))


@server.tool()
def find_figures(kind: str = "both", sector: str | None = None, technology_id: str | None = None,
                 query: str | None = None, unit: str | None = None, limit: int = 50) -> list[dict]:
    """Every cost or performance figure recorded on the cards, one row per figure.

    Use this for numbers questions ("installed cost per kW of a heavy-duty gas turbine", "round-trip
    efficiency of liquid air storage", "energy per tonne of captured CO2"). Each row carries the
    metric, low/high, unit, dollar or publication year, the basis (scope: installed vs overnight,
    per kW vs per kWh, feed conditions) and the source url — quote the basis with the number.
    kind: "cost", "performance" or "both". sector: a taxonomy code. technology_id: one card.
    query: substring over metric, basis and card name. unit: substring of the unit, e.g. "USD/kW",
    "GJ/t", "kWh/t", "%". limit: rows returned (max 200). Empty results mean the cards record no
    figure for that question — check list_gaps rather than estimating."""
    if kind not in ("cost", "performance", "both"):
        raise ValueError('kind must be "cost", "performance" or "both"')
    return _with_neon(lambda: pg.figure_rows(kind, sector, technology_id, query, unit, limit),
                      lambda: library.find_figures(kind, sector, technology_id, query, unit, limit, db()))


@server.tool()
def list_vendors(role: str | None = None, sector: str | None = None, query: str | None = None) -> list[dict]:
    """The vendor directory: curated records for suppliers, OEMs, licensors and packagers, each citing
    the pages it was written from. role: oem, licensor, packager, epc, developer, operator, rental,
    service, supplier or integrator. sector: a taxonomy code such as PWR or CCS. query: text."""
    return _with_neon(lambda: pg.vendor_rows(role, sector, query),
                      lambda: library.list_vendors(role, sector, query, db()))


@server.tool()
def get_vendor(vendor_id: str) -> dict | None:
    """One vendor record: country, roles, products, the technology cards it supplies, and the sources behind it."""
    return _with_neon(lambda: pg.vendor_row(vendor_id),
                      lambda: library.get_vendor(vendor_id, db()))


@server.tool()
def list_equipment(equipment_type: str | None = None, query: str | None = None) -> list[dict]:
    """The equipment catalog: one curated record per equipment class (starting with boilers), each with
    specification ranges, the vendors that supply it and the pages behind every figure.
    equipment_type: e.g. boiler. query: text."""
    return _with_neon(lambda: pg.equipment_rows(equipment_type, query),
                      lambda: library.list_equipment(equipment_type, query, db()))


@server.tool()
def get_equipment(equipment_id: str) -> dict | None:
    """One equipment record: specification ranges with basis and sources, vendor model lines, and the gaps."""
    return _with_neon(lambda: pg.equipment_row(equipment_id),
                      lambda: library.get_equipment(equipment_id, db()))


@server.tool()
def list_projects(status: str | None = None, sector: str | None = None, country: str | None = None,
                  query: str | None = None) -> list[dict]:
    """Named projects and operating plants: one curated record each with status, location, capacities,
    owners and the technology cards it deploys.
    status: proposed, FID, under-construction, commissioning, operating, suspended or decommissioned.
    sector: a taxonomy code such as H2, CCS or IDC. country: full name or two-letter code, e.g.
    "US" (matches "United States"), "Canada", "NL". query: text."""
    return _with_neon(lambda: pg.project_rows(status, sector, country, query),
                      lambda: library.list_projects(status, sector, country, query, db=db()))


@server.tool()
def get_project(project_id: str) -> dict | None:
    """One project record: capacities with sources, milestones, owners, contractors, offtakers and gaps."""
    return _with_neon(lambda: pg.project_row(project_id),
                      lambda: library.get_project(project_id, db()))


@server.tool()
def list_technology_register(code: str | None = None, maturity: str | None = None, query: str | None = None) -> list[dict]:
    """The full register of about 300 technologies across all sectors (code: UPS, MID, GAS, REF, PCH, PWR, H2,
    CCS, or a discipline code for cross-cutting equipment). Maturity and examples are indicative and unverified;
    entries with a "card" id have a verified technology card (use get_technology)."""
    return _with_neon(lambda: pg.register_rows(code, maturity, query),
                      lambda: library.list_register(code, maturity, query))


@server.tool()
def list_gaps(sector: str | None = None, field: str | None = None, reason_code: str | None = None,
              include_no_card: bool = False) -> list[dict]:
    """Inputs the technology cards still lack, each with why it is missing (reason_code: not_in_sources_read,
    source_unreachable, source_not_collected, paid_source, status_unchecked, conflicting_sources,
    general_knowledge_only), where to get it, the next action and any blocker. field: trl, performance, costs,
    reference_plants, suppliers, status, process, other. include_no_card adds register technologies with no card.
    Use it to tell users what the library cannot answer yet, or to pick the next collection task."""
    return _with_neon(lambda: pg.gap_rows(sector, field, reason_code, include_no_card),
                      lambda: library.list_gaps(sector, field, reason_code, include_no_card, db()))


@server.tool()
def taxonomy() -> dict:
    """The library's two tag axes with names and subtopics, plus region codes.

    Call this before filtering anything by sector, discipline or region so you use real codes
    (sectors: UPS, MID, GAS, REF, PCH, PWR, H2, CCS, IDC, WWT; disciplines: PRC, ROT, ELE, CIV,
    INS, MAT, HSE, DIG). Cheaper and more reliable than guessing a code and getting zero results."""
    return library.taxonomy()


@server.tool()
def list_glossary(query: str | None = None) -> list[dict]:
    """The library's glossary: terms and abbreviations with their expansion and a short note.

    Use it to resolve acronyms an agent or user may not know (PUE, WUE, TRL, SRU, MERCON, SMR,
    DLE, HRSG...). query filters term, expansion and note by substring."""
    return library.list_glossary(query)


@server.tool()
def get_glossary_term(term: str) -> dict | None:
    """One glossary entry by term or expansion; falls back to a substring match, returns null if absent."""
    return library.get_glossary_term(term)


@server.tool()
def list_standards(org: str | None = None, query: str | None = None) -> list[dict]:
    """Standards, codes and specifications referenced across the library, with designation, title,
    scope and url. org filters the issuing body (e.g. API, ISO, NORSOK, ASME, IEC, DNV). query
    matches designation, title and scope. Use get_standard for one entry."""
    return library.list_standards(org, query)


@server.tool()
def get_standard(ref: str) -> dict | None:
    """One standard by id or designation (e.g. "API RP 535", "ISO 21809-2", "NORSOK M-501")."""
    return library.get_standard(ref)


@server.tool()
def library_stats() -> dict:
    """Counts of sources, documents, chunks and vectors in the library."""
    # Neon first (decision #34): the container's baked index is the offline fallback and holds
    # no embeddings, so without this the MCP number disagreed with REST /api/stats.
    if pg.configured():
        try:
            return pg.library_stats()
        except (pg.NotConfigured, pg.DatabaseError):
            pass
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


class RequireHilirToken:
    """ASGI middleware: reject requests without a hilir Access bearer token.

    The edge verifies the browser session and forwards
    ``Authorization: Bearer <access token>``; this gate confirms the token
    locally (signature, issuer, audience — agent/auth.py). web=True exempts
    the UI paths (web.py's own gates do the same verification per page and add
    role resolution); a backend-only container (LIBRARY_WEB=off) exempts
    nothing. There is no other credential (step 3): no library key, no
    per-user keys."""

    def __init__(self, app, web=True):
        self.app, self.web = app, web

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http" and scope["path"] not in api.PUBLIC_PATHS \
                and not (self.web and web.is_web_path(scope["path"])):
            headers = dict(scope["headers"])
            raw = headers.get(b"authorization", b"").removeprefix(b"Bearer ").strip()
            token = raw.decode("utf-8", "replace")
            # verify() accepts BOTH credentials: a JWT (local JWKS check) and
            # a person's opaque key (RFC 7662 introspection at Access).
            if hilir_auth is None or hilir_auth.verify(token) is None:
                # RFC 9728 §5.1 + RFC 6750 §3.1: the 401 names the protected-
                # resource metadata (so MCP clients can discover Access) and
                # adds error="invalid_token" only when a bearer was presented.
                # The public MCP origin is pinned by config, not the Host header
                # (the tunnel Host is the Caddy upstream name).
                presented = bool(raw)
                challenge = ", ".join([
                    'Bearer resource_metadata="%s/.well-known/oauth-protected-resource"'
                    % MCP_PUBLIC_ORIGIN.rstrip("/"),
                    *(['error="invalid_token"'] if presented else []),
                ])
                await send({"type": "http.response.start", "status": 401,
                            "headers": [(b"content-type", b"application/json"),
                                        (b"www-authenticate", challenge.encode())]})
                await send({"type": "http.response.body", "body": b'{"error": "missing or invalid token"}'})
                return
        await self.app(scope, receive, send)


def http_app(with_web=True):
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
    if with_web:
        app.router.routes.extend(web.routes(sys.modules[__name__]))
    return RequireHilirToken(app, with_web)


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
    EXCLUDE_RESTRICTED = not args.include_restricted
    web_on = os.environ.get("LIBRARY_WEB", "on").lower() not in ("off", "0", "false", "no")
    if web_on:
        # Loud at boot: a missing account store leaves every verified identity
        # without a role row, so no page opens (fail-closed, by design).
        if not userstore.configured():
            print(
                "WARNING: the account store is not configured — USER_STORE_URL is empty. "
                "Verified hilir Access identities have no role row and every gated page "
                "will refuse them until the edge supplies a store DSN.",
                file=sys.stderr,
            )
    db()
    import uvicorn
    uvicorn.run(http_app(with_web=web_on), host=args.host, port=args.port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
