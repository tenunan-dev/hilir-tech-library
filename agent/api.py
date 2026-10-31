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
        path = request.query_params.get("path")
        if not path:
            return JSONResponse({"error": "query parameter path is required"}, status_code=400)
        return _found(tools.get_document(path))

    async def technologies(request: Request):
        q = request.query_params
        return JSONResponse(tools.compare_technologies(q.get("sector"), q.get("maturity"), q.get("application")))

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

    async def register(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_technology_register(q.get("code"), q.get("maturity"), q.get("q")))

    async def gaps(request: Request):
        q = request.query_params
        return JSONResponse(tools.list_gaps(q.get("sector"), q.get("field"), q.get("reason_code"),
                                            q.get("include_no_card", "").lower() in ("1", "true", "yes")))

    async def stats(request: Request):
        # Decision #34: the live counts come from Neon when it is configured (the baked SQLite
        # index in a container is the fallback, and it can be stale); no embedding_model key.
        if pg.configured():
            try:
                return JSONResponse(pg.library_stats())
            except (pg.NotConfigured, pg.DatabaseError):
                pass
        return JSONResponse(tools.library_stats())

    async def openapi(request: Request):
        return JSONResponse(openapi_spec(os.environ.get("LIBRARY_PUBLIC_URL", str(request.base_url).rstrip("/"))))

    return [
        Route("/api/search", search), Route("/api/sources", list_sources), Route("/api/sources/{source_id}", source),
        Route("/api/documents", document), Route("/api/technologies", technologies),
        Route("/api/technologies/{technology_id}", technology), Route("/api/vendors", vendors),
        Route("/api/vendors/{vendor_id}", vendor), Route("/api/register", register),
        Route("/api/equipment", equipment_list), Route("/api/equipment/{equipment_id}", equipment),
        Route("/api/gaps", gaps), Route("/api/stats", stats), Route("/api/openapi.json", openapi),
    ]


def _param(name, description, required=False, schema=None, where="query"):
    return {"name": name, "in": where, "required": required or where == "path", "description": description,
            "schema": schema or {"type": "string"}}


SECTOR = _param("sector", "Sector code: UPS, MID, GAS, REF, PCH, PWR, H2 or CCS")
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
        "components": {"securitySchemes": {"ApiKey": {"type": "apiKey", "in": "header", "name": "x-api-key"}}},
        "security": [{"ApiKey": []}],
        "paths": {
            "/api/search": get("search", "Search catalog sources, document passages, technology cards, vendor records and equipment records", [
                _param("q", "Search text", required=True),
                _param("kind", "all, source, chunk, technology, vendor or equipment"), SECTOR,
                _param("discipline", "Discipline code: PRC, ROT, INS, MAT, HSE or DIG"),
                _param("region", "Region code, e.g. sea, apac, global"),
                _param("reuse_level", "full-text-open, full-text-restricted, summary-only or catalog-only"),
                _param("limit", "Results to return, 1-50 (default 10)", schema={"type": "integer"})]),
            "/api/sources": get("listSources", "List catalog sources by code, region, reuse level or type, Asia Pacific first", [
                _param("code", "Sector or discipline code"), _param("region", "Region code"),
                _param("reuse_level", "Reuse level"), _param("source_type", "e.g. licensor, journal, agency-data")]),
            "/api/sources/{source_id}": get("getSource", "One catalog record with its collected documents",
                                            [_param("source_id", "Catalog id", where="path")], JSON_OR_404),
            "/api/documents": get("getDocument", "Front matter and text of one document, by the path a search result gave",
                                  [_param("path", "Document path, e.g. corpus/netl/....md", required=True)], JSON_OR_404),
            "/api/technologies": get("compareTechnologies", "Comparison table of technology options, commercial first", [
                SECTOR, _param("maturity", "commercial, demonstration, pilot or lab"),
                _param("application", "e.g. cement, power, hydrogen")]),
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
            "/api/register": get("listTechnologyRegister", "Register of about 300 technologies across all sectors", [
                _param("code", "Sector or discipline code"), _param("maturity", "Maturity filter"), _param("q", "Text filter")]),
            "/api/gaps": get("listGaps", "Inputs the technology cards still lack, with where to get them", [
                SECTOR, _param("field", "trl, performance, costs, reference_plants, suppliers, status, process, other"),
                _param("reason_code", "Why it is missing"),
                _param("include_no_card", "true to add register technologies without a card", schema={"type": "boolean"})]),
            "/api/stats": get("libraryStats", "Counts of sources, documents, chunks and technology cards", []),
        },
    }
