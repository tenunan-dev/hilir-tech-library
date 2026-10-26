"""Server-rendered HTML interface for the library: browse technology cards, the catalog, the register,
gaps and, when DATABASE_URL is set, the Postgres layer.

    LIBRARY_API_KEY=... python agent/server.py --http --port 8000
    # /                home: library stats, search, sector links
    # /search /technologies /register /sources /documents /gaps
    # /database        row counts, schema reference, SQL console, semantic search, graph
    #                  (the last three only when the environment carries a read-only DATABASE_URL)

People sign in once at /login with the library API key; the session cookie is Secure because the server
sits behind TLS at techlib.hilir.app. Agents can call the same pages with the x-api-key header instead.
Mounted by server.http_app() next to /mcp and /api at the same origin; deploy/cloudflare/src/index.ts
mirrors PREFIXES to keep these paths off the edge API-key check.

Every data value reaches the HTML through esc(); text from full-text-restricted documents is still
filtered by the tools module before it gets here.
"""
import html
import hmac
import json
import re
import urllib.parse
from hashlib import sha256

from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.routing import Route

import pg

COOKIE = "oglib_session"
# keep in sync with the worker: deploy/cloudflare/src/index.ts (UI_PREFIXES)
PREFIXES = ("/login", "/logout", "/search", "/technologies", "/register", "/sources", "/documents", "/gaps", "/database")
SECTOR_SELECT = ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS", "PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
MATURITIES = ["commercial", "demonstration", "pilot", "lab"]
REUSE_LEVELS = ["full-text-open", "full-text-restricted", "summary-only", "catalog-only"]
GAP_FIELDS = ["trl", "performance", "costs", "reference_plants", "suppliers", "status", "process", "other", "card"]
SECTOR_COLORS = {"UPS": "#8a6d3b", "MID": "#5e8f5e", "GAS": "#b0703a", "REF": "#7d6ba8", "PCH": "#4f8fa8",
                 "PWR": "#c8963e", "H2": "#3e8fc8", "CCS": "#5aa08a"}
COLOR_FALLBACK = "#5a6b7b"
MATURITY_COLORS = {"commercial": "#2e7d32", "demonstration": "#1565c0", "pilot": "#ef6c00", "lab": "#616161"}
NAV = (("Technologies", "/technologies"), ("Register", "/register"), ("Sources", "/sources"),
       ("Gaps", "/gaps"), ("Database", "/database"))
HOME_SECTORS = (("UPS", "upstream"), ("MID", "midstream"), ("GAS", "gas processing & LNG"), ("REF", "refining"),
                ("PCH", "petrochemicals"), ("PWR", "power"), ("H2", "hydrogen"), ("CCS", "carbon capture"))
RELS = ["published_by", "in_sector", "covers_discipline", "in_region", "in_country", "from_source", "cites",
        "cites_document", "supplied_by", "realised_by", "example_supplier", "alternative_to", "mentions",
        "has_gap", "look_in", "similar_to"]
GRAPH_NODE_DEFAULT = "technology:ccs-cryogenic"
SQL_EXAMPLES = (
    ("UPS gaps", "SELECT * FROM v_gap WHERE sector = 'UPS' ORDER BY name LIMIT 50"),
    ("cards citing the same sources",
     "SELECT * FROM v_technology_co_citation WHERE a = 'ccs-cryogenic' OR b = 'ccs-cryogenic' LIMIT 20"),
    ("graph neighbourhood",
     "SELECT node_id, kind, label, depth FROM graph_neighbors('technology:ups-co2-eor', 2, ARRAY['cites','supplied_by','mentions'])"),
    ("hybrid search", "SELECT kind, ref, title, score FROM hybrid_search('CO2 storage Malay Basin', NULL, 10)"),
)
MERMAID_SCRIPT = ('<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";'
                  'mermaid.initialize({startOnLoad:true,securityLevel:"strict"});</script>')

CSS = """
* { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
       background: #f6f7f9; color: #1c2733; line-height: 1.5; }
a { color: #1a4f8b; }
h1 { font-size: 1.35rem; margin: 0 0 .5rem; }
h2 { font-size: 1.05rem; margin: .1rem 0 .5rem; }
header { position: sticky; top: 0; z-index: 5; background: #0e2033; color: #fff;
         box-shadow: 0 1px 4px rgba(14,32,51,.35); }
header .bar { max-width: 74rem; margin: 0 auto; padding: .55rem 1rem; display: flex;
              flex-wrap: wrap; gap: .5rem .9rem; align-items: center; }
header a { color: #fff; text-decoration: none; }
header .brand { font-weight: 700; }
header nav { display: flex; flex-wrap: wrap; gap: .15rem; }
header nav a { padding: .18rem .5rem; border-radius: 6px; color: #c8d6e5; font-size: .92rem; }
header nav a.active { background: #27425f; color: #fff; font-weight: 600; }
header form { display: flex; gap: .35rem; flex: 1 1 11rem; }
header input[type=search] { flex: 1; min-width: 7rem; background: #1b3450; border: 1px solid #2f4d6e;
                            color: #fff; border-radius: 6px; padding: .3rem .55rem; }
header input::placeholder { color: #8fa6bd; }
.container { max-width: 74rem; margin: 0 auto; padding: 1rem; }
.card { background: #fff; border: 1px solid #d9dee3; border-radius: 8px; padding: 1rem; margin: 0 0 1rem; }
.card.error { background: #fdf0ee; border-color: #e6b8b0; }
.narrow { max-width: 26rem; margin: 2.5rem auto; }
.stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(7.5rem, 1fr)); gap: .75rem; }
.stat { border: 1px solid #d9dee3; border-radius: 8px; padding: .6rem .4rem; text-align: center;
        font-size: .78rem; color: #5a6b7b; }
.stat b { display: block; font-size: 1.35rem; color: #1c2733; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr)); gap: .75rem; }
.grid a { display: flex; align-items: center; gap: .5rem; background: #fff; border: 1px solid #d9dee3;
          border-radius: 8px; padding: .6rem .8rem; color: #1c2733; text-decoration: none; }
.grid a:hover { border-color: #9fb2c4; }
.dot { width: .7rem; height: .7rem; border-radius: 50%; display: inline-block; flex: none; }
.big { text-align: center; padding: 1.75rem 1rem; }
.big form { display: flex; gap: .5rem; margin: 0 auto; max-width: 36rem; }
.big input { flex: 1; padding: .55rem .8rem; border: 1px solid #d9dee3; border-radius: 8px; font-size: 1rem; }
.scroll { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: .9rem; }
th, td { border: 1px solid #d9dee3; padding: .35rem .55rem; text-align: left; vertical-align: top; }
th { background: #eef1f4; }
tbody tr:nth-child(even) { background: #f7f9fa; }
td.wrap { white-space: pre-wrap; }
pre, code { font-family: ui-monospace, "SF Mono", Menlo, Consolas, monospace; }
code { background: #eef1f4; border-radius: 4px; padding: .05rem .3rem; font-size: .88em; }
pre { background: #eef1f4; border-radius: 8px; padding: .75rem; overflow-x: auto; font-size: .82rem; }
pre code { background: none; padding: 0; }
pre.doc { font-size: .8rem; white-space: pre-wrap; }
.badge { display: inline-block; background: #5a6b7b; color: #fff; border-radius: 999px;
         padding: .02rem .5rem; font-size: .72rem; vertical-align: middle; white-space: nowrap; }
.pill { display: inline-block; border: 1px solid #c9d2da; background: #f1f4f6; color: #40506a;
        border-radius: 999px; padding: 0 .5rem; font-size: .72rem; vertical-align: middle; white-space: nowrap; }
.muted { color: #5a6b7b; }
.small { font-size: .8rem; }
.snippet { font-size: .85rem; color: #3d4f60; margin: .15rem 0 .1rem; }
.gap { margin: .7rem 0; padding-top: .6rem; border-top: 1px solid #eef1f4; }
ul { margin: .3rem 0; padding-left: 1.2rem; }
.hits li { margin: .4rem 0; }
form.filters { display: flex; flex-wrap: wrap; gap: .5rem; align-items: center; margin-bottom: .8rem; }
input, select, textarea, button { font: inherit; }
input, select, textarea { background: #fff; color: #1c2733; border: 1px solid #d9dee3;
                          border-radius: 6px; padding: .3rem .5rem; }
textarea { width: 100%; font-family: ui-monospace, Menlo, monospace; font-size: .85rem; }
button { background: #0e2033; color: #fff; border: 1px solid #0e2033; border-radius: 6px;
         padding: .3rem .8rem; cursor: pointer; }
button:hover { background: #1c3350; }
button.ghost { background: transparent; border-color: #3d5a78; color: #c8d6e5; }
button.example { background: #eef1f4; color: #1c2733; border-color: #d9dee3; font-size: .8rem; }
label.check { display: inline-flex; gap: .25rem; align-items: center; font-size: .8rem; margin-right: .6rem; }
details { margin: .25rem 0; }
summary { cursor: pointer; color: #1a4f8b; font-size: .85rem; }
footer { max-width: 74rem; margin: 0 auto; padding: .75rem 1rem 2rem; color: #5a6b7b;
         font-size: .85rem; text-align: center; }
footer a { color: #1a4f8b; }
"""


def is_web_path(path: str) -> bool:
    """True for "/" and any path starting with a PREFIX at a segment boundary (/technologiesx is not a web path)."""
    if path == "/":
        return True
    return any(path == p or path.startswith(p + "/") for p in PREFIXES)


def session_token(key: str) -> str:
    return hmac.new(key.encode(), b"og-tech-library web session v1", sha256).hexdigest()


def _authed(request: Request, key: str) -> bool:
    given = request.headers.get("x-api-key") or request.headers.get("authorization", "").removeprefix("Bearer ").strip()
    if given and hmac.compare_digest(given.encode(), key.encode()):
        return True
    token = request.cookies.get(COOKIE, "")
    return bool(token) and hmac.compare_digest(token.encode(), session_token(key).encode())


def esc(value) -> str:
    return html.escape(str(value)) if value is not None else ""


def _trunc(value, n: int) -> str:
    text = "" if value is None else str(value)
    return text if len(text) <= n else text[:n] + "…"


def _int(value, default, low, high):
    try:
        return max(low, min(high, int(value)))
    except (TypeError, ValueError):
        return default


def _safe_next(value) -> str:
    return value if isinstance(value, str) and value.startswith("/") and not value.startswith("//") else "/"


def _badge(text, color=COLOR_FALLBACK) -> str:
    return f'<span class="badge" style="background:{esc(color)}">{esc(text)}</span>' if text else ""


def _sector_badge(code) -> str:
    return _badge(code, SECTOR_COLORS.get(code, COLOR_FALLBACK))


def _maturity_badge(maturity) -> str:
    return _badge(maturity, MATURITY_COLORS.get(maturity, COLOR_FALLBACK))


def _pill(text) -> str:
    return f'<span class="pill">{esc(text)}</span>' if text else ""


def _section(title, inner) -> str:
    head = f"<h2>{esc(title)}</h2>" if title else ""
    return f'<section class="card">{head}{inner}</section>'


def _error_box(message) -> str:
    return f'<section class="card error"><p>{esc(message)}</p></section>'


def _select(name, options, selected="") -> str:
    rendered = "".join(
        f'<option value="{esc(value)}"{" selected" if value == (selected or "") else ""}>{esc(label)}</option>'
        for value, label in options)
    return f'<select name="{name}">{rendered}</select>'


def _bullets(items) -> str:
    return "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"


def _meta_table(pairs) -> str:
    """pairs are (label, html) values, already escaped by the caller; empty values are skipped."""
    rows = "".join(f"<tr><th>{esc(label)}</th><td>{value}</td></tr>"
                   for label, value in pairs if value not in (None, "", []))
    return f'<div class="scroll"><table>{rows}</table></div>'


def _meta_value(value) -> str:
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value)
    return _trunc(value, 200)


def _figure_value(fig) -> str:
    low, high, unit = fig.get("low"), fig.get("high"), fig.get("unit") or ""
    if low is not None and high is not None and low != high:
        return f"{low}–{high} {unit}".strip()
    value = low if low is not None else high
    return f"{value} {unit}".strip() if value is not None else "—"


def _source_link(source, width=60) -> str:
    url = (source or {}).get("url")
    if not url:
        return "—"
    return f'<a href="{esc(url)}">{esc(_trunc((source or {}).get("note") or url, width))}</a>'


def _db_panel() -> str:
    steps = (
        "Create a Neon project (neon.tech).",
        "<code>pip install -r requirements-postgres.txt</code>",
        "<code>export DATABASE_URL=&lt;owner DSN&gt;</code>",
        "<code>python tools/load_postgres.py</code>",
        "<code>OG_READONLY_PASSWORD=... python tools/load_postgres.py --grant-readonly</code>",
        "Set the printed read-only DSN as this server's <code>DATABASE_URL</code> "
        "(Cloudflare: <code>wrangler secret put DATABASE_URL</code>) and redeploy.",
    )
    links = " · ".join(f'<a href="{href}">{label}</a>' for href, label in (
        ("/database/sql", "SQL console"), ("/database/search", "Semantic search"), ("/database/graph", "Graph")))
    return ('<section class="card"><h2>Postgres layer not configured</h2>'
            '<p>The database pages read the Postgres layer (schema <code>og</code>: catalog sources, documents '
            'and passages with vectors, technology cards, the register and the knowledge graph) over a '
            'read-only connection. To set it up:</p>'
            f'<ol>{"".join(f"<li>{s}</li>" for s in steps)}</ol>'
            '<p class="muted">See docs/POSTGRES.md. The DSN must be the read-only role\'s, never the owner DSN.</p>'
            f'<p class="muted">{links}</p></section>')


def _page(title, body, *, q="", active="") -> HTMLResponse:
    links = []
    for label, href in NAV:
        mark = ' class="active"' if href == active else ""
        links.append(f'<a href="{href}"{mark}>{label}</a>')
    nav = "".join(links)
    return HTMLResponse(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — O&amp;G technology library</title>
<style>{CSS}</style>
</head>
<body>
<header><div class="bar">
<a class="brand" href="/">O&amp;G technology library</a>
<nav>{nav}</nav>
<form action="/search" method="get"><input type="search" name="q" value="{esc(q)}" placeholder="Search the library" aria-label="Search"><button type="submit">Search</button></form>
<form action="/logout" method="post"><button type="submit" class="ghost">Sign out</button></form>
</div></header>
<main class="container">
{body}
</main>
<footer>Every result carries its licence — cite the url. full-text-restricted text is never served.
 · <a href="/api/openapi.json">REST API</a> · <a href="/mcp">MCP</a></footer>
</body>
</html>""")


def _not_found(message="Nothing is served at this address.") -> HTMLResponse:
    resp = _page("Not found", f'<section class="card"><h1>Not found</h1><p class="muted">{esc(message)}</p></section>')
    resp.status_code = 404
    return resp


def _bad_request(message) -> HTMLResponse:
    resp = _page("Bad request", f'<section class="card"><h1>Bad request</h1><p class="muted">{esc(message)}</p></section>')
    resp.status_code = 400
    return resp


SECTOR_OPTIONS = [("", "any sector")] + [(c, c) for c in SECTOR_SELECT]
MATURITY_OPTIONS = [("", "any maturity")] + [(m, m) for m in MATURITIES]
KIND_OPTIONS = [("all", "all"), ("source", "source"), ("chunk", "chunk"), ("technology", "technology")]
REUSE_OPTIONS = [("", "any reuse level")] + [(r, r) for r in REUSE_LEVELS]
FIELD_OPTIONS = [("", "any field")] + [(f, f) for f in GAP_FIELDS]


def routes(tools, key: str) -> list:
    """tools: the server module, whose MCP tool functions apply the hosted server's licence filtering;
    tools.db() and tools._embedder back the database pages."""

    async def home(request: Request):
        stats = tools.library_stats()
        cards = "".join(f'<div class="stat"><b>{esc(v)}</b>{esc(k)}</div>' for k, v in stats.items() if v is not None)
        sectors = "".join(
            f'<a href="/technologies?sector={code}"><span class="dot" '
            f'style="background:{SECTOR_COLORS.get(code, COLOR_FALLBACK)}"></span>{esc(label)}</a>'
            for code, label in HOME_SECTORS)
        more = " · ".join(f'<a href="{href}">{label}</a>' for href, label in (
            ("/register", "Register"), ("/sources", "Sources"), ("/gaps", "Gaps"), ("/database", "Database")))
        body = (
            f'<section class="card"><div class="stats">{cards}</div></section>'
            '<section class="card big"><form action="/search" method="get">'
            '<input type="search" name="q" placeholder="Search sources, passages and technology cards" autofocus>'
            '<button type="submit">Search</button></form></section>'
            f'<section class="card"><h2>Browse by sector</h2><div class="grid">{sectors}</div></section>'
            f'<section class="card"><h2>More</h2><p>{more}</p></section>')
        return _page("Oil, gas and energy technologies", body)

    async def login(request: Request):
        if request.method == "POST":
            form = await request.form()
            next_url = _safe_next(form.get("next"))
            if hmac.compare_digest(str(form.get("key") or "").encode(), key.encode()):
                resp = RedirectResponse(next_url, status_code=303)
                resp.set_cookie(COOKIE, session_token(key), max_age=2592000, httponly=True, secure=True,
                                samesite="lax", path="/")
                return resp
            error = '<p><b>Wrong key.</b></p>'
        else:
            next_url = _safe_next(request.query_params.get("next"))
            error = ""
        form = (f'<form method="post" action="/login"><input type="hidden" name="next" value="{esc(next_url)}">'
                '<p><label>API key <input type="password" name="key" autofocus required></label></p>'
                '<p><button type="submit">Sign in</button></p></form>')
        body = (f'<section class="card narrow"><h1>Sign in</h1>'
                f'<p class="muted">The same key agents send in the x-api-key header.</p>{error}{form}</section>')
        resp = _page("Sign in", body)
        if error:
            resp.status_code = 401
        return resp

    async def logout(request: Request):
        resp = RedirectResponse("/", status_code=303)
        resp.delete_cookie(COOKIE, path="/")
        return resp

    async def search(request: Request):
        qp = request.query_params
        query, kind, sector = str(qp.get("q") or ""), str(qp.get("kind") or ""), str(qp.get("sector") or "")
        body = ['<section class="card"><form class="filters" method="get" action="/search">'
                f'<input type="search" name="q" value="{esc(query)}" placeholder="Search sources, passages and cards" size="34"> '
                + _select("kind", KIND_OPTIONS, kind or "all") + " " + _select("sector", SECTOR_OPTIONS, sector)
                + ' <button type="submit">Search</button></form></section>']
        if query.strip():
            results = tools.search(query, kind or "all", sector or None, None, None, None, 30)
            sections = []
            for title, want in (("Technologies", "technology"), ("Sources", "source"), ("Passages", "chunk")):
                hits = [r for r in results if r.get("kind") == want]
                if hits:
                    render = _tech_row if want == "technology" else _source_row if want == "source" else _chunk_row
                    sections.append(_section(title, '<ul class="hits">' + "".join(render(r) for r in hits) + "</ul>"))
            body += sections or [_section("", '<p class="muted">No results. Try fewer or different words.</p>')]
        return _page("Search", "".join(body), q=query)

    async def technologies(request: Request):
        qp = request.query_params
        sector, maturity, query = str(qp.get("sector") or ""), str(qp.get("maturity") or ""), str(qp.get("q") or "")
        items = tools.compare_technologies(sector or None, maturity or None, None)
        if query:
            needle = query.lower()
            items = [i for i in items if needle in f"{i.get('name', '')} {i.get('category', '')}".lower()]
        head = "<th>Name</th>" + ("<th>Sector</th>" if sector else "") + "<th>Category</th><th>Maturity</th><th>TRL</th><th>Largest reference</th>"
        rows = "".join(
            "<tr><td>" + f'<a href="/technologies/{esc(i.get("id"))}">{esc(i.get("name"))}</a></td>'
            + (f"<td>{_sector_badge(sector)}</td>" if sector else "")
            + f"<td>{esc(i.get('category'))}</td><td>{_maturity_badge(i.get('maturity'))}</td>"
            f"<td>{esc(i.get('trl') or '')}</td><td class=\"muted\">{esc(_trunc(i.get('largest_reference'), 80))}</td></tr>"
            for i in items)
        body = ('<section class="card"><form class="filters" method="get" action="/technologies">'
                + _select("sector", SECTOR_OPTIONS, sector) + _select("maturity", MATURITY_OPTIONS, maturity)
                + f' <input type="search" name="q" value="{esc(query)}" placeholder="name or category" size="18">'
                + ' <button type="submit">Filter</button></form>'
                + f'<p class="muted">{len(items)} cards</p>'
                + f'<div class="scroll"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div></section>')
        return _page("Technologies", body, active="/technologies")

    async def technology(request: Request):
        card = tools.get_technology(request.path_params["technology_id"])
        if not card:
            return _not_found("No technology card with that id.")
        body = [_card_head(card)]
        if card.get("principle"):
            body.append(_section("Principle", f"<p>{esc(card['principle'])}</p>"))
        diagram = card.get("block_diagram_mermaid")
        if diagram:
            body.append(_section("Block diagram", f'<pre class="mermaid">{esc(diagram)}</pre>'))
        if card.get("applications"):
            body.append(_section("Applications", _bullets(card["applications"])))
        if card.get("process_steps"):
            body.append(_section("Process steps", "<ul>" + "".join(_step_li(s) for s in card["process_steps"]) + "</ul>"))
        if card.get("key_equipment"):
            body.append(_section("Key equipment", _bullets(card["key_equipment"])))
        if card.get("performance"):
            body.append(_section("Performance", _figures_table(card["performance"])))
        if card.get("costs"):
            body.append(_section("Costs", _figures_table(card["costs"])))
        if card.get("suppliers"):
            body.append(_section("Suppliers", "<ul>" + "".join(_supplier_li(s) for s in card["suppliers"]) + "</ul>"))
        if card.get("reference_plants"):
            body.append(_section("Reference plants", _plants_table(card["reference_plants"])))
        if card.get("advantages"):
            body.append(_section("Advantages", _bullets(card["advantages"])))
        if card.get("limitations"):
            body.append(_section("Limitations", _bullets(card["limitations"])))
        if card.get("gaps"):
            body.append(_section("Gaps", "".join(_gap_block(g) for g in card["gaps"])))
        if card.get("sources"):
            body.append(_section("Sources", _sources_table(card["sources"])))
        if diagram:
            body.append(MERMAID_SCRIPT)
        return _page(str(card.get("name") or card.get("id")), "".join(body), active="/technologies")

    async def register(request: Request):
        qp = request.query_params
        code, maturity, query = str(qp.get("code") or ""), str(qp.get("maturity") or ""), str(qp.get("q") or "")
        entries = tools.list_technology_register(code or None, maturity or None, query or None)
        rows = "".join(
            "<tr><td>" + (f'<a href="/technologies/{esc(e.get("card"))}">{esc(e.get("name"))}</a> {_pill("card")}'
                          if e.get("card") else esc(e.get("name")))
            + f"</td><td>{_sector_badge(e.get('code'))}</td><td>{esc(e.get('area'))}</td>"
            f"<td>{_maturity_badge(e.get('maturity'))}</td><td>{esc(e.get('examples'))}</td></tr>"
            for e in entries)
        body = ('<section class="card"><form class="filters" method="get" action="/register">'
                + _select("code", SECTOR_OPTIONS, code) + _select("maturity", MATURITY_OPTIONS, maturity)
                + f' <input type="search" name="q" value="{esc(query)}" placeholder="name, area or examples" size="18">'
                + ' <button type="submit">Filter</button></form>'
                + f'<p class="muted">{len(entries)} register entries</p>'
                + '<div class="scroll"><table><thead><tr><th>Name</th><th>Sector</th><th>Area</th><th>Maturity</th>'
                + f'<th>Examples</th></tr></thead><tbody>{rows}</tbody></table></div></section>')
        return _page("Technology register", body, active="/register")

    async def sources(request: Request):
        qp = request.query_params
        code, region, reuse = str(qp.get("code") or ""), str(qp.get("region") or ""), str(qp.get("reuse_level") or "")
        items = tools.list_by_tag(code or None, region or None, reuse or None, None)
        rows = "".join(
            f'<tr><td><a href="/sources/{esc(i.get("id"))}">{esc(i.get("name"))}</a></td>'
            f"<td>{esc(i.get('source_type'))}</td><td>{esc(', '.join(i.get('regions') or []))}</td>"
            f"<td>{_badge(i.get('reuse_level'))}</td><td>{esc(i.get('quality_tier'))}</td></tr>" for i in items)
        body = ('<section class="card"><form class="filters" method="get" action="/sources">'
                + _select("code", SECTOR_OPTIONS, code) + _select("reuse_level", REUSE_OPTIONS, reuse)
                + f' <input type="text" name="region" value="{esc(region)}" placeholder="region, e.g. sea" size="12">'
                + ' <button type="submit">Filter</button></form>'
                + f'<p class="muted">{len(items)} sources</p>'
                + '<div class="scroll"><table><thead><tr><th>Name</th><th>Type</th><th>Regions</th><th>Reuse level</th>'
                + f'<th>Tier</th></tr></thead><tbody>{rows}</tbody></table></div></section>')
        return _page("Sources", body, active="/sources")

    async def source(request: Request):
        rec = tools.get_source(request.path_params["source_id"])
        if not rec:
            return _not_found("No catalog source with that id.")
        url = rec.get("url") or ""
        name_value = f'<a href="{esc(url)}">{esc(rec.get("name"))}</a>' if url else esc(rec.get("name"))

        def joined(name):
            return ", ".join(str(v) for v in rec.get(name) or [])

        meta = _meta_table([
            ("Name", name_value), ("Type", esc(rec.get("source_type"))), ("Publisher", esc(rec.get("publisher_org"))),
            ("Country", esc(rec.get("country"))), ("Sectors", esc(joined("sectors"))),
            ("Disciplines", esc(joined("disciplines"))), ("Regions", esc(joined("regions"))),
            ("Access", esc(rec.get("access"))), ("Licence", esc(rec.get("licence"))),
            ("Reuse level", _badge(rec.get("reuse_level"))), ("Permitted use", esc(rec.get("permitted_use"))),
            ("Automated access", esc(rec.get("automated_access"))), ("Quality tier", esc(rec.get("quality_tier"))),
            ("Verification", esc(rec.get("verification"))), ("Last verified", esc(rec.get("last_verified"))),
            ("Update frequency", esc(rec.get("update_frequency"))), ("Notes", esc(rec.get("notes"))),
        ])
        docs = rec.get("documents") or []
        if docs:
            items = "".join(
                f'<li><a href="/documents?path={urllib.parse.quote(str(d.get("path") or ""), safe="")}">'
                f'{esc(d.get("title") or d.get("path"))}</a>'
                + (f' <a class="muted small" href="{esc(d.get("url"))}">{esc(_trunc(d.get("url"), 60))}</a>'
                   if d.get("url") else "") + "</li>" for d in docs)
            documents = f'<ul>{items}</ul>'
        else:
            documents = '<p class="muted">None collected yet.</p>'
        body = f'<section class="card">{meta}</section>' + _section("Collected documents", documents)
        return _page(str(rec.get("name") or rec.get("id")), body, active="/sources")

    async def documents(request: Request):
        path = request.query_params.get("path")
        if not path:
            return _bad_request("This address needs a ?path= parameter, as given by a search result.")
        doc = tools.get_document(path)
        if not doc:
            return _not_found("No collected document at that path.")
        meta = doc.get("meta") or {}
        title = str(meta.get("title") or doc.get("path") or path)
        badges = " ".join(filter(None, (_badge(meta.get("licence")), _badge(meta.get("reuse_level")))))
        rows = "".join(f"<tr><th>{esc(k)}</th><td>{esc(_meta_value(v))}</td></tr>" for k, v in meta.items())
        body = [f'<section class="card"><h1>{esc(title)} {badges}</h1>'
                f'<div class="scroll"><table>{rows}</table></div></section>']
        if doc.get("error"):
            body.append(_section("", f'<p class="muted">{esc(doc["error"])}</p>'))
        if doc.get("text"):
            body.append('<section class="card"><pre class="doc">' + esc(doc["text"])
                        + '</pre><p class="muted">Open-licence copy; cite the url.</p></section>')
        return _page(title, "".join(body))

    async def gaps(request: Request):
        qp = request.query_params
        sector, field = str(qp.get("sector") or ""), str(qp.get("field") or "")
        rows = tools.list_gaps(sector or None, field or None, None, False)
        groups = {}
        for gap in rows:
            groups.setdefault((gap.get("card"), gap.get("technology")), []).append(gap)
        blocks = "".join(
            f'<section class="card"><h2>' + (f'<a href="/technologies/{esc(card_id)}">{esc(name)}</a>' if card_id
                                             else esc(name))
            + f"</h2>{''.join(_gap_block(g) for g in items)}</section>"
            for (card_id, name), items in groups.items())
        body = ('<section class="card"><form class="filters" method="get" action="/gaps">'
                + _select("sector", SECTOR_OPTIONS, sector) + _select("field", FIELD_OPTIONS, field)
                + ' <button type="submit">Filter</button></form>'
                + f'<p class="muted">{len(rows)} gaps</p></section>')
        body += blocks or _section("", '<p class="muted">No open gaps for that filter.</p>')
        return _page("Gaps", body, active="/gaps")

    async def database(request: Request):
        if not pg.configured():
            return _page("Database", _db_panel(), active="/database")
        body = []
        try:
            counts = pg.counts()
        except pg.NotConfigured:
            return _page("Database", _db_panel(), active="/database")
        except pg.DatabaseError as e:
            body.append(_error_box(str(e)))
        else:
            stats = "".join(f'<div class="stat"><b>{esc(v)}</b>{esc(k)}</div>' for k, v in counts.items())
            body.append(f'<section class="card"><div class="stats">{stats}</div></section>')
        doc = pg.tables_doc()
        tables = "".join(
            f'<li><b>{esc(t.get("name"))}</b> <span class="muted">{esc(t.get("holds", ""))}</span><br>'
            f'<span class="muted small">{esc(", ".join(t.get("columns") or []))}</span></li>'
            for t in doc.get("tables") or [])
        views = "".join(f'<li><b>{esc(v.get("name"))}</b> <span class="muted">{esc(v.get("holds", ""))}</span></li>'
                        for v in doc.get("views") or [])
        functions = "".join(f'<li><b>{esc(f.get("name"))}({esc(f.get("signature", ""))})</b> '
                            f'<span class="muted">{esc(f.get("does", ""))}</span></li>'
                            for f in doc.get("functions") or [])
        examples = "".join(f'<li><a href="/database/sql?sql={urllib.parse.quote(sql, safe="")}">{esc(label)}</a></li>'
                           for label, sql in SQL_EXAMPLES)
        body += [_section("Tables", f'<ul>{tables}</ul>'), _section("Views", f"<ul>{views}</ul>"),
                 _section("Functions", f"<ul>{functions}</ul>"), _section("Example queries", f"<ul>{examples}</ul>")]
        return _page("Database", "".join(body), active="/database")

    async def database_sql(request: Request):
        if request.method == "POST":
            form = await request.form()
            sql, max_rows = str(form.get("sql") or ""), _int(form.get("max_rows"), 100, 1, 500)
        else:
            qp = request.query_params
            # a GET with ?sql= both prefills the textarea and runs the query
            sql, max_rows = str(qp.get("sql") or ""), _int(qp.get("max_rows"), 100, 1, 500)
            if not sql.strip():
                empty = _sql_console("", max_rows) if pg.configured() else _db_panel()
                return _page("SQL console", empty, active="/database")
        result = error = None
        try:
            result = pg.run_sql(sql, max_rows)
        except pg.NotConfigured:
            return _page("SQL console", _db_panel(), active="/database")
        except (pg.BadSql, pg.DatabaseError) as e:
            error = str(e)
        body = [_sql_console(sql, max_rows)]
        if error is not None:
            body.append(_error_box(error))
        elif result is not None:
            body.append(_sql_result(result))
        return _page("SQL console", "".join(body), active="/database")

    async def database_search(request: Request):
        if not pg.configured():
            return _page("Semantic search", _db_panel(), active="/database")
        qp = request.query_params
        query, k = str(qp.get("q") or ""), _int(qp.get("k"), 10, 1, 50)
        body = ['<section class="card"><form class="filters" method="get" action="/database/search">'
                f'<input type="search" name="q" value="{esc(query)}" placeholder="search passages and cards" size="30"> '
                f'<label>k <input type="number" name="k" value="{k}" min="1" max="50" style="width:4.5rem"></label>'
                ' <button type="submit">Search</button></form></section>']
        if query.strip():
            tools.db()
            embedder = getattr(tools, "_embedder", None)
            qvec = list(embedder([query])[0]) if embedder else None
            try:
                results = pg.hybrid_search(query, k, qvec)
            except pg.NotConfigured:
                return _page("Semantic search", _db_panel(), active="/database")
            except pg.DatabaseError as e:
                results, rows = None, ""
                body.append(_error_box(str(e)))
            else:
                rows = "".join(_hybrid_row(r) for r in results)
                mode = _badge("semantic") if qvec is not None else (
                    _badge("keyword only") + ' <span class="muted small">vectors appear once embeddings are loaded</span>')
                empty = '<p class="muted">No matches.</p>' if not results else ""
                body.append(_section("", f"<p>{mode}</p>"
                                     + '<div class="scroll"><table><thead><tr><th>Kind</th><th>Ref</th><th>Title</th>'
                                     + f'<th>Score</th></tr></thead><tbody>{rows}</tbody></table></div>{empty}'))
        return _page("Semantic search", "".join(body), active="/database")

    async def database_graph(request: Request):
        if not pg.configured():
            return _page("Graph", _db_panel(), active="/database")
        qp = request.query_params
        node = str(qp.get("node") or "")
        depth = _int(qp.get("depth"), 1, 1, 2)
        chosen = [r for r in RELS if r in qp.getlist("rels")]
        boxes = "".join(f'<label class="check"><input type="checkbox" name="rels" value="{esc(r)}"'
                        f'{" checked" if r in chosen else ""}>{esc(r)}</label>' for r in RELS)
        body = ['<section class="card"><form method="get" action="/database/graph">'
                f'<p><label>Start node <input type="text" name="node" value="{esc(node or GRAPH_NODE_DEFAULT)}" size="34"></label> '
                f'<label>Depth <select name="depth"><option value="1"{" selected" if depth == 1 else ""}>1</option>'
                f'<option value="2"{" selected" if depth == 2 else ""}>2</option></select></label> '
                '<button type="submit">Walk</button></p>'
                f'<p>{boxes}</p><p class="muted small">Leave every relation unchecked to follow all of them.</p></form></section>']
        if node.strip():
            try:
                rows = pg.graph_neighbors(node, depth, chosen or None)
            except pg.NotConfigured:
                return _page("Graph", _db_panel(), active="/database")
            except pg.DatabaseError as e:
                rows = None
                body.append(_error_box(str(e)))
            if rows is not None:
                if rows:
                    trs = "".join(
                        f"<tr><td>{esc(r.get('node_id'))}</td><td>{esc(r.get('kind'))}</td><td>{esc(r.get('label'))}</td>"
                        f"<td>{esc(r.get('depth'))}</td><td>{esc(', '.join(str(v) for v in r.get('via') or []))}</td></tr>"
                        for r in rows)
                    body.append(_section("Neighbors", '<div class="scroll"><table><thead><tr><th>Node</th><th>Kind</th>'
                                         '<th>Label</th><th>Depth</th><th>Via</th></tr></thead>'
                                         f'<tbody>{trs}</tbody></table></div>'))
                    diagram, shown, total = _graph_mermaid(node, rows)
                    cut = f'<p class="muted">showing {shown} of {total} nodes</p>' if shown < total else ""
                    body.append(_section("Diagram", f'<pre class="mermaid">{esc(diagram)}</pre>{cut}{MERMAID_SCRIPT}'))
                else:
                    body.append(_section("", '<p class="muted">No neighbors found for that node.</p>'))
        return _page("Graph", "".join(body), active="/database")

    def gated(handler):
        async def with_gate(request: Request):
            if not _authed(request, key):
                return RedirectResponse("/login?next=" + urllib.parse.quote(request.url.path), status_code=303)
            return await handler(request)
        return with_gate

    return [
        Route("/", gated(home)),
        Route("/login", login, methods=["GET", "POST"]),
        Route("/logout", logout, methods=["GET", "POST"]),
        Route("/search", gated(search)),
        Route("/technologies", gated(technologies)),
        Route("/technologies/{technology_id}", gated(technology)),
        Route("/register", gated(register)),
        Route("/sources", gated(sources)),
        Route("/sources/{source_id}", gated(source)),
        Route("/documents", gated(documents)),
        Route("/gaps", gated(gaps)),
        Route("/database", gated(database)),
        Route("/database/sql", gated(database_sql), methods=["GET", "POST"]),
        Route("/database/search", gated(database_search)),
        Route("/database/graph", gated(database_graph)),
    ]


def _tech_row(hit) -> str:
    ref = hit.get("ref") or hit.get("id") or ""
    out = [f'<li><a href="/technologies/{esc(ref)}">{esc(hit.get("name") or hit.get("title") or ref)}</a> ',
           _maturity_badge(hit.get("maturity"))]
    if hit.get("category"):
        out.append(f' <span class="muted">{esc(hit["category"])}</span>')
    if hit.get("hint"):
        out.append(f'<br><span class="muted small">{esc(hit["hint"])}</span>')
    out.append("</li>")
    return "".join(out)


def _source_row(hit) -> str:
    ref = hit.get("ref") or hit.get("source_id") or ""
    out = [f'<li><a href="/sources/{esc(ref)}">{esc(hit.get("name") or hit.get("title") or ref)}</a> ',
           _badge(hit.get("licence")), " ", _badge(hit.get("reuse_level"))]
    if hit.get("url"):
        out.append(f' <a class="muted small" href="{esc(hit["url"])}">{esc(_trunc(hit["url"], 60))}</a>')
    out.append("</li>")
    return "".join(out)


def _chunk_row(hit) -> str:
    ref = str(hit.get("ref") or "")
    out = [f"<li><b>{esc(hit.get('title'))}</b> ", _badge(hit.get("licence")), " ", _badge(hit.get("reuse_level")), "</li>"]
    if hit.get("snippet"):
        out.append(f'<p class="snippet">{esc(_trunc(hit["snippet"], 400))}</p>')
    links = f'<a href="/documents?path={urllib.parse.quote(ref.split("#")[0], safe="")}">document</a>'
    if hit.get("source_id"):
        links += f' · <a href="/sources/{esc(hit["source_id"])}">source</a>'
    out.append(f'<p class="small">{links}</p></li>')
    return "".join(out)


def _card_head(card) -> str:
    trl = card.get("trl") or {}
    low, high = trl.get("low"), trl.get("high")
    if low is None or high is None:
        trl_text = ""
    elif low == high:
        trl_text = f"TRL {low}"
    else:
        trl_text = f"TRL {low}–{high}"
    metas = [t for t in (trl_text, f"last reviewed {card.get('last_reviewed')}" if card.get("last_reviewed") else "") if t]
    out = [f'<section class="card"><h1>{esc(card.get("name"))} {_sector_badge(card.get("sector"))} '
           f'{_maturity_badge(card.get("maturity"))}</h1>']
    if metas:
        out.append(f'<p class="muted">{esc(" · ".join(metas))}</p>')
    if card.get("aliases"):
        out.append(f'<p class="muted small">Also: {esc(", ".join(str(a) for a in card["aliases"]))}</p>')
    if card.get("licence"):
        out.append(f'<p class="muted small">Licence: {esc(card["licence"])}</p>')
    out.append("</section>")
    return "".join(out)


def _step_li(step) -> str:
    if isinstance(step, str):
        return f"<li>{esc(step)}</li>"
    if isinstance(step, dict):
        parts = []
        for value in step.values():
            if isinstance(value, dict):
                parts += [str(v) for v in value.values()]
            elif isinstance(value, list):
                parts += [str(v) for v in value]
            else:
                parts.append(str(value))
        return f"<li>{esc(' — '.join(parts))}</li>"
    return ""


def _supplier_li(supplier) -> str:
    out = [esc(supplier.get("name"))]
    if supplier.get("product"):
        out.append(f' <span class="muted">({esc(supplier["product"])})</span>')
    if supplier.get("url"):
        out.append(f' <a href="{esc(supplier["url"])}">{esc(_trunc(supplier["url"], 60))}</a>')
    return "<li>" + "".join(out) + "</li>"


def _figures_table(figures) -> str:
    rows = "".join(
        f"<tr><td>{esc(f.get('metric'))}</td><td>{esc(_figure_value(f))}</td>"
        f"<td>{esc(f.get('year') if f.get('year') is not None else '—')}</td>"
        f"<td>{esc(f.get('basis') or '—')}</td><td>{_source_link(f.get('source'))}</td></tr>"
        for f in figures)
    return ('<div class="scroll"><table><thead><tr><th>Metric</th><th>Value</th><th>Year</th><th>Basis</th>'
            f'<th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>')


def _plants_table(plants) -> str:
    rows = "".join(
        f"<tr><td>{esc(p.get('name'))}</td><td>{esc(p.get('country') or '—')}</td>"
        f"<td>{esc(p.get('capacity') or '—')}</td><td>{esc(p.get('status') or '—')}</td>"
        f"<td>{esc(p.get('year') if p.get('year') is not None else '—')}</td>"
        f"<td>{_source_link(p.get('source'))}</td></tr>" for p in plants)
    return ('<div class="scroll"><table><thead><tr><th>Name</th><th>Country</th><th>Capacity</th><th>Status</th>'
            f'<th>Year</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table></div>')


def _sources_table(sources) -> str:
    rows = []
    for s in sources:
        url = s.get("url") or ""
        url_cell = f'<a href="{esc(url)}">{esc(_trunc(url, 70))}</a>' if url else "—"
        sid = s.get("source_id")
        sid_cell = f'<a href="/sources/{esc(sid)}">{esc(sid)}</a>' if sid else "—"
        rows.append(f"<tr><td>{url_cell}</td><td>{sid_cell}</td><td>{esc(s.get('note') or '—')}</td></tr>")
    return ('<div class="scroll"><table><thead><tr><th>URL</th><th>Catalog id</th><th>Note</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>')


def _gap_block(gap) -> str:
    head = f"{_badge(gap.get('field'))} <b>{esc(gap.get('item'))}</b> {_pill(gap.get('reason_code'))}"
    reason = str(gap.get("reason") or "")
    if gap.get("blocked_by"):
        reason = f"{reason} Blocked by: {gap['blocked_by']}." if reason else f"Blocked by: {gap['blocked_by']}."
    parts = [f"<p>{head}</p>"]
    if reason:
        parts.append(f'<p class="muted">{esc(reason)}</p>')
    if gap.get("action"):
        parts.append(f"<p>Next: {esc(gap['action'])}</p>")
    hints = [w.get("hint") for w in gap.get("where") or [] if isinstance(w, dict) and w.get("hint")]
    if hints:
        parts.append("<details><summary>where to look</summary><ul>"
                     + "".join(f"<li>{esc(h)}</li>" for h in hints) + "</ul></details>")
    return '<div class="gap">' + "".join(parts) + "</div>"


def _sql_console(sql, max_rows) -> str:
    buttons = "".join(
        f'<button type="button" class="example" onclick="{esc(_fill_js(query))}">{esc(label)}</button> '
        for label, query in SQL_EXAMPLES)
    return ('<section class="card"><h2>SQL console</h2>'
            '<p class="muted small">One read-only SELECT or WITH statement against schema og; at most 500 rows.</p>'
            '<form method="post" action="/database/sql">'
            f'<textarea id="sql" name="sql" rows="8" placeholder="one SELECT statement — no semicolon, no comments">{esc(sql)}</textarea>'
            f'<p><label>max rows <input type="number" name="max_rows" value="{int(max_rows)}" min="1" max="500" '
            'style="width:5rem"></label> <button type="submit">Run</button></p></form>'
            f'<p class="small">Examples: {buttons}</p></section>')


def _fill_js(query) -> str:
    # esc() escapes the double quotes; the HTML parser decodes them back into the JS the browser runs.
    return 'document.getElementById("sql").value = ' + json.dumps(query)


def _sql_result(result) -> str:
    columns = result.get("columns") or []
    rows = result.get("rows") or []
    head = "".join(f"<th>{esc(c)}</th>" for c in columns)
    body = "".join("<tr>" + "".join(f'<td class="wrap">{esc(v) if v is not None else "—"}</td>' for v in row) + "</tr>"
                   for row in rows)
    note = f'{result.get("rowcount", len(rows))} rows'
    if result.get("truncated"):
        note += " " + _badge("truncated")
    return (f'<section class="card"><p class="muted">{note}</p>'
            f'<div class="scroll"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div></section>')


def _hybrid_row(hit) -> str:
    ref, kind = str(hit.get("ref") or ""), hit.get("kind") or ""
    if kind == "technology":
        ref_cell = f'<a href="/technologies/{esc(ref)}">{esc(ref)}</a>'
    elif kind == "chunk":
        ref_cell = f'<a href="/documents?path={urllib.parse.quote(ref.split("#")[0], safe="")}">{esc(ref)}</a>'
    else:
        ref_cell = esc(ref)
    return (f"<tr><td>{esc(kind)}</td><td>{ref_cell}</td>"
            f"<td>{esc(hit.get('title'))}</td><td>{esc(hit.get('score'))}</td></tr>")


def _graph_mermaid(start, rows):
    """graph LR of the neighbourhood: the start node plus each row's node, capped at 40 nodes."""
    sanitized, node_lines, edge_lines = {}, [], []
    drawn = set()

    def mid(value):
        value = str(value)
        if value not in sanitized:
            cleaned = re.sub(r"[^A-Za-z0-9_]", "", value)
            # a mermaid id must not be empty or start with a digit
            sanitized[value] = "n" + cleaned if not cleaned or cleaned[0].isdigit() else cleaned
        return sanitized[value]

    def label(value):
        text = str(value or "").replace('"', "").replace("(", "").replace(")", "")
        return _trunc(text, 40)

    def add_node(value, text):
        key = mid(value)
        if key not in drawn:
            drawn.add(key)
            node_lines.append(f'    {key}["{esc(label(text))}"]')

    add_node(start, start)
    for row in rows[:39]:  # the start node plus 39 rows is the 40-node cap
        node_id = row.get("node_id")
        if not node_id:
            continue
        add_node(node_id, row.get("label"))
        via = [str(v) for v in row.get("via") or []]
        rel = esc(via[-1]) if via else ""
        edge = f'{mid(start)} -->|"{rel}"| {mid(node_id)}' if rel else f"{mid(start)} --> {mid(node_id)}"
        edge_lines.append("    " + edge)
    diagram = "graph LR\n" + "\n".join(node_lines + edge_lines)
    return diagram, len(drawn), 1 + len(rows)
