"""REST API over the same functions as the MCP tools, for agents that do not speak MCP
(ChatGPT custom GPT Actions, LangChain or n8n HTTP tools, scripts).

Mounted by server.http_app() next to /mcp, behind the same API key. GET only, JSON out.
/api/openapi.json is served without a key so tools can import the schema; it holds no data.
"""
import os

import pg
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

PUBLIC_PATHS = {"/api/openapi.json"}


def _int(value, default, low, high):
    try:
        return max(low, min(high, int(value)))
    except (TypeError, ValueError):
        return default


def _found(value):
    # An error-shaped payload {"path", "error"} is a licence refusal (restricted text), not a
    # success: answer 403 instead of 200-with-error-body. None stays a plain 404.
    if value is not None and isinstance(value, dict) and set(value) == {"path", "error"}:
        return JSONResponse(value, status_code=403)
    return JSONResponse(value) if value is not None else JSONResponse({"error": "not found"}, status_code=404)


def routes(tools):
    """tools: the server module, whose MCP tool functions apply the hosted server's licence filtering."""

    async def search(request: Request):
        q = request.query_params
        if not q.get("q"):
            return JSONResponse({"error": "query parameter q is required"}, status_code=400)
        return JSONResponse(tools.search(q["q"], q.get("kind", "all"), q.get("sector"), q.get("discipline"),
                                         q.get("region"), q.get("reuse_level"), _int(q.get("limit"), 10, 1, 50)))

    async def list_sources(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_by_tag(q.get("code"), q.get("region"), q.get("reuse_level"), q.get("source_type")))

    async def source(request: Request):
        return _found(tools.get_source(request.path_params["source_id"]))

    async def document(request: Request):
        q = request.query_params
        path = q.get("path")
        if not path:
            # List mode: the documents index (path/title/source/reuse_level/text_included),
            # optionally narrowed to one source or sector.
            return JSONResponse(tools.list_documents(q.get("source_id"), q.get("sector"),
                                                     _int(q.get("limit"), 50, 1, 500)))
        return _found(tools.get_document(path, _int(q.get("offset"), 0, 0, 10**9),
                                         _int(q.get("limit"), 20000, 1, 100_000)))

    async def technologies(request: Request):
        q = request.query_params
        ids = [t.strip() for t in (q.get("technology_ids") or "").split(",") if t.strip()] or None
        return JSONResponse(tools.compare_technologies(q.get("sector"), q.get("maturity"),
                                                       q.get("application"), ids))

    async def technology(request: Request):
        return _found(tools.get_technology(request.path_params["technology_id"]))

    async def vendors(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_vendors(q.get("role"), q.get("sector"), q.get("q")))

    async def vendor(request: Request):
        return _found(tools.get_vendor(request.path_params["vendor_id"]))

    async def equipment_list(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_equipment(q.get("equipment_type"), q.get("q")))

    async def equipment(request: Request):
        return _found(tools.get_equipment(request.path_params["equipment_id"]))

    async def project_list(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_projects(q.get("status"), q.get("sector"), q.get("country"), q.get("q")))

    async def project(request: Request):
        return _found(tools.get_project(request.path_params["project_id"]))

    async def product_list(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_products(q.get("product_type"), q.get("manufacturer"), q.get("q")))

    async def product(request: Request):
        return _found(tools.get_product(request.path_params["product_id"]))

    async def drawing_list(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_drawings(q.get("diagram_type"), q.get("sector"), q.get("q")))

    async def drawing(request: Request):
        return _found(tools.get_drawing(request.path_params["drawing_id"]))

    async def register(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_technology_register(q.get("code"), q.get("maturity"), q.get("q")))

    async def register_entry(request: Request):
        return _found(tools.get_register_entry(request.path_params["entry_id"]))

    async def gaps(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_gaps(q.get("sector"), q.get("field"), q.get("reason_code"),
                                            q.get("include_no_card", "").lower() in ("1", "true", "yes")))

    async def figures(request: Request):
        q = request.query_params
        return JSONResponse(tools.find_figures(q.get("kind", "both"), q.get("sector"), q.get("technology_id"),
                                               q.get("q"), q.get("unit"), _int(q.get("limit"), 50, 1, 200)))

    async def taxonomy(_request: Request):
        return JSONResponse(tools.taxonomy())

    async def glossary(request: Request):
        return JSONResponse(tools.list_glossary(request.query_params.get("q")))

    async def glossary_term(request: Request):
        return _found(tools.get_glossary_term(request.path_params["term"]))

    async def standards(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_standards(q.get("org"), q.get("q")))

    async def standard(request: Request):
        return _found(tools.get_standard(request.path_params["ref"]))

    async def stats(request: Request):
        # Decision #34: the live counts come from Neon when it is configured (the baked SQLite
        # index in a container is the fallback, and it can be stale); no embedding_model key.
        if pg.configured():
            try:
                return JSONResponse(pg.library_stats())
            except (pg.NotConfigured, pg.DatabaseError):
                pass
        return JSONResponse(tools.library_stats())

    async def version(request: Request):
        """Drift stamp (decision #34 R4): Neon counts, vector total and the freshest review /
        verify dates when the database is configured; the baked SQLite index otherwise."""
        if pg.configured():
            try:
                return JSONResponse({"service": "HILIR Technology Library", "layer": "neon", **pg.drift_stamp()})
            except (pg.NotConfigured, pg.DatabaseError):
                pass
        stats = tools.library_stats()
        counts = {k: stats.get(v) for k, v in (("source", "sources"), ("document", "documents"),
                                               ("technology", "technologies"), ("vendor", "vendors"),
                                               ("equipment", "equipment"))}
        return JSONResponse({"service": "HILIR Technology Library", "layer": "sqlite-fallback", "counts": counts})

    async def openapi(request: Request):
        return JSONResponse(openapi_spec(os.environ.get("LIBRARY_PUBLIC_URL", str(request.base_url).rstrip("/"))))

    return [
        Route("/api/search", search), Route("/api/sources", list_sources), Route("/api/sources/{source_id}", source),
        Route("/api/documents", document), Route("/api/technologies", technologies),
        Route("/api/technologies/{technology_id}", technology), Route("/api/vendors", vendors),
        Route("/api/vendors/{vendor_id}", vendor), Route("/api/register", register),
        Route("/api/register/{entry_id:path}", register_entry),
        Route("/api/equipment", equipment_list), Route("/api/equipment/{equipment_id}", equipment),
        Route("/api/projects", project_list), Route("/api/projects/{project_id}", project),
        Route("/api/products", product_list), Route("/api/products/{product_id}", product),
        Route("/api/drawings", drawing_list), Route("/api/drawings/{drawing_id}", drawing),
        Route("/api/gaps", gaps), Route("/api/stats", stats), Route("/api/version", version),
        Route("/api/figures", figures), Route("/api/taxonomy", taxonomy),
        Route("/api/glossary", glossary), Route("/api/glossary/{term}", glossary_term),
        Route("/api/standards", standards), Route("/api/standards/{ref}", standard),
        Route("/api/openapi.json", openapi),
    ]


def _param(name, description, required=False, schema=None, where="query"):
    return {"name": name, "in": where, "required": required or where == "path", "description": description,
            "schema": schema or {"type": "string"}}


SECTOR = _param("sector", "Sector code: UPS, MID, GAS, REF, PCH, PWR, H2, CCS, IDC or WWT")
JSON_OK = {"200": {"description": "JSON result"}, "401": {"description": "Missing or wrong API key"}}
JSON_OR_404 = {**JSON_OK, "404": {"description": "Not found"}}


def openapi_spec(server_url):
    def get(op_id, summary, params, responses=JSON_OK):
        return {"get": {"operationId": op_id, "summary": summary, "parameters": params, "responses": responses}}

    return {
        "openapi": "3.1.0",
        "info": {"title": "HILIR Technology Library", "version": "1.0",
                 "description": "Curated sources, documents and technology cards on oil, gas, petrochemical, "
                                "hydrogen, CCUS and power technologies, weighted to Asia Pacific and Southeast Asia. "
                                "Every result carries url, licence and reuse_level: always cite the url and respect "
                                "the licence."},
        "servers": [{"url": server_url}],
        "components": {"securitySchemes": {"HilirBearer": {"type": "http", "scheme": "bearer",
                                                           "description": "A hilir Access access token (aud = this app's resource)"}}},
        "security": [{"HilirBearer": []}],
        "paths": {
            "/api/search": get("search", "Search catalog sources, document passages, technology cards, vendor records, equipment records and projects", [
                _param("q", "Search text", required=True),
                _param("kind", "all, source, chunk, technology, vendor, equipment or project"), SECTOR,
                _param("discipline", "Discipline code: PRC, ROT, ELE, CIV, INS, MAT, HSE or DIG (keeps only sources and passages)"),
                _param("region", "Region code, e.g. sea, apac, global (keeps only sources and passages)"),
                _param("reuse_level", "full-text-open, full-text-restricted, summary-only or catalog-only"),
                _param("limit", "Results to return, 1-50 (default 10)", schema={"type": "integer"})]),
            "/api/sources": get("listSources", "List catalog sources by code, region, reuse level or type, Asia Pacific first", [
                _param("code", "Sector or discipline code"), _param("region", "Region code"),
                _param("reuse_level", "Reuse level"), _param("source_type", "e.g. licensor, journal, agency-data")]),
            "/api/sources/{source_id}": get("getSource", "One catalog record with its collected documents",
                                            [_param("source_id", "Catalog id", where="path")], JSON_OR_404),
            "/api/documents": get("getDocument", "One document by path (front matter and text, paged in characters; "
                                  "403 for restricted text), or the documents index when no path is given", [
                _param("path", "Document path, e.g. corpus/netl/....md"),
                _param("source_id", "List mode: one catalog source id"),
                _param("sector", "List mode: a sector code"),
                _param("offset", "Character offset into the text (default 0)", schema={"type": "integer"}),
                _param("limit", "Characters to return, 1-100000 (default 20000)", schema={"type": "integer"})], JSON_OR_404),
            "/api/technologies": get("compareTechnologies", "Comparison table of technology options, commercial first; "
                                     "technology_ids compares named cards side by side in order", [
                SECTOR, _param("maturity", "commercial, demonstration, pilot or lab"),
                _param("application", "e.g. cement, power, hydrogen"),
                _param("technology_ids", "Comma-separated card ids to compare in order, e.g. "
                        "ccs-amine-post-combustion,ccs-polymeric-membrane (overrides the filters)")]),
            "/api/technologies/{technology_id}": get(
                "getTechnology", "One technology card: process steps, equipment, block diagram (Mermaid), costs with basis, suppliers, sources",
                [_param("technology_id", "Card id, e.g. ccs-amine-post-combustion", where="path")], JSON_OR_404),
            "/api/vendors": get("listVendors", "The vendor directory: curated supplier records with the cards they supply", [
                _param("role", "oem, licensor, packager, epc, developer, operator, rental, service, supplier or integrator"),
                SECTOR, _param("q", "Text filter")]),
            "/api/vendors/{vendor_id}": get(
                "getVendor", "One vendor record: country, roles, products, technologies supplied, sources behind it",
                [_param("vendor_id", "Vendor id, e.g. wartsila", where="path")], JSON_OR_404),
            "/api/equipment": get("listEquipment", "The equipment catalog: one curated record per equipment class with "
                                  "specification ranges and supplying vendors", [
                _param("equipment_type", "e.g. boiler"), _param("q", "Text filter")]),
            "/api/equipment/{equipment_id}": get(
                "getEquipment", "One equipment record: specification ranges with basis and sources, vendor model "
                "lines, technologies and gaps",
                [_param("equipment_id", "Equipment id, e.g. boiler-hrsg", where="path")], JSON_OR_404),
            "/api/projects": get("listProjects", "Named projects and operating plants: status, location, "
                                 "capacities, owners and the technology cards they deploy", [
                _param("status", "proposed, FID, under-construction, commissioning, operating, suspended or decommissioned"),
                SECTOR, _param("country", "Country filter: full name or two-letter code, e.g. US, Canada, NL"),
                _param("q", "Text filter")]),
            "/api/projects/{project_id}": get(
                "getProject", "One project record: capacities with sources, milestones, owners, contractors, "
                "offtakers, technologies and gaps",
                [_param("project_id", "Project id, e.g. hornsea-2-offshore-wind-farm-uk-north-sea-orsted", where="path")], JSON_OR_404),
            "/api/products": get("listProducts", "Vendor product catalog: product lines with printed specifications", [
                _param("product_type", "e.g. boiler, burner, valve-train"), _param("manufacturer", "Vendor id"),
                _param("q", "Text filter")]),
            "/api/products/{product_id}": get("getProduct", "One product line with printed specifications and source url",
                                              [_param("product_id", "Product id", where="path")], JSON_OR_404),
            "/api/drawings": get("listDrawings", "Citable PFDs, P&IDs, schematics and flowsheets", [
                _param("diagram_type", "PFD, P&ID, schematic, flowsheet or block-diagram"), SECTOR,
                _param("q", "Text filter")]),
            "/api/drawings/{drawing_id}": get("getDrawing", "One process drawing: scope, publisher, url and coverage",
                                              [_param("drawing_id", "Drawing id", where="path")], JSON_OR_404),
            "/api/register": get("listTechnologyRegister", "The full technology register (400+ entries across all sectors)", [
                _param("code", "Sector or discipline code"), _param("maturity", "Maturity filter"), _param("q", "Text filter")]),
            "/api/register/{entry_id}": get("getRegisterEntry", "One register entry by its id, which register rows carry",
                                            [_param("entry_id", "Register entry id (code/slug-of-name)", where="path")], JSON_OR_404),
            "/api/gaps": get("listGaps", "Inputs the technology cards still lack, with where to get them", [
                SECTOR, _param("field", "trl, performance, costs, reference_plants, suppliers, status, process, other"),
                _param("reason_code", "Why it is missing"),
                _param("include_no_card", "true to add register technologies without a card", schema={"type": "boolean"})]),
            "/api/figures": get("findFigures", "Every cost or performance figure recorded on the cards, one row "
                                "per figure, each with its basis, year and source url", [
                _param("kind", "cost, performance or both (default both)"), SECTOR,
                _param("technology_id", "Restrict to one card id, e.g. pwr-gas-engines"),
                _param("q", "Substring over metric, basis and card name"),
                _param("unit", "Substring of the unit, e.g. USD/kW, GJ/t, kWh/t, %"),
                _param("limit", "Rows to return, 1-200 (default 50)", schema={"type": "integer"})]),
            "/api/taxonomy": get("taxonomy", "Sector and discipline codes with names and subtopics, plus region codes", []),
            "/api/glossary": get("listGlossary", "Terms and abbreviations with their expansion and a short note", [
                _param("q", "Text filter over term, expansion and note")]),
            "/api/glossary/{term}": get("getGlossaryTerm", "One glossary entry by term or expansion",
                                        [_param("term", "e.g. CCGT", where="path")], JSON_OR_404),
            "/api/standards": get("listStandards", "Standards and codes referenced by the library, with scope and url", [
                _param("org", "Issuing body: API, ISO, IEC, ASME, ASCE, CEN, NFPA or UL"),
                _param("q", "Text filter over designation, title and scope")]),
            "/api/standards/{ref}": get("getStandard", "One standard by id or designation",
                                        [_param("ref", "e.g. IEC 60079 or api-rp-535", where="path")], JSON_OR_404),
            "/api/stats": get("libraryStats", "Counts of sources, documents, chunks, vectors, technology cards, vendors, equipment classes and projects", []),
            "/api/version": get("libraryVersion", "Drift stamp: row counts, vectors and the freshest review/verify dates", []),
        },
    }
