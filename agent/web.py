"""Server-rendered HTML interface for the library: browse technology cards, vendors, the catalog, the register,
gaps and, when DATABASE_URL is set, the Postgres layer — including its knowledge graph as an interactive
network and an atlas view of the whole database.

    LIBRARY_API_KEY=... python agent/server.py --http --port 8000
    # /                home: library stats, search, sector links
    # /search /technologies /vendors /register /sources /documents /gaps
    # /database        row counts, schema reference, SQL console, semantic search, graph, atlas
    #                  (the last four only when the environment carries a read-only DATABASE_URL)

People sign in once at /login — with the library API key (the owner, as before) or with a named
email + password account from the LIBRARY_USERS secret (agent/users.py creates entries); both
issue the same session cookie, which for accounts carries the signed identity. The session cookie
is Secure because the server sits behind TLS at techlib.hilir.app. Agents can call the same pages
with the x-api-key header instead.
Mounted by server.http_app() next to /mcp and /api at the same origin; deploy/cloudflare/src/index.ts
mirrors PREFIXES to keep these paths off the edge API-key check.

Every data value reaches the HTML through esc(); text from full-text-restricted documents is still
filtered by the tools module before it gets here.
"""
import html
import hmac
import json
import re
import time
import urllib.parse
from hashlib import sha256

from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, RedirectResponse
from starlette.routing import Route

import pg
import users as user_accounts
import userstore
import vendors as vendor_records

COOKIE = "oglib_session"
# keep in sync with the worker: deploy/cloudflare/src/index.ts (UI_PREFIXES)
PREFIXES = ("/login", "/logout", "/search", "/technologies", "/vendors", "/register", "/sources", "/documents", "/gaps", "/database", "/admin", "/account")
SECTOR_SELECT = ["UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS", "PRC", "ROT", "INS", "MAT", "HSE", "DIG"]
MATURITIES = ["commercial", "demonstration", "pilot", "lab"]
REUSE_LEVELS = ["full-text-open", "full-text-restricted", "summary-only", "catalog-only"]
GAP_FIELDS = ["trl", "performance", "costs", "reference_plants", "suppliers", "status", "process", "other", "card"]
SECTOR_COLORS = {"UPS": "#8a6d3b", "MID": "#5e8f5e", "GAS": "#b0703a", "REF": "#7d6ba8", "PCH": "#4f8fa8",
                 "PWR": "#c8963e", "H2": "#3e8fc8", "CCS": "#5aa08a"}
COLOR_FALLBACK = "#5a6b7b"
MATURITY_COLORS = {"commercial": "#2e7d32", "demonstration": "#1565c0", "pilot": "#ef6c00", "lab": "#616161"}
NAV = (("Technologies", "/technologies"), ("Vendors", "/vendors"), ("Register", "/register"), ("Sources", "/sources"),
       ("Gaps", "/gaps"), ("Database", "/database"))
# Second-level tabs shown on every /database page (keep in step with the routes below).
DATABASE_TABS = (("Overview", "/database"), ("SQL console", "/database/sql"), ("Semantic search", "/database/search"),
                 ("Network", "/database/graph"), ("Atlas", "/database/map"))
HOME_SECTORS = (("UPS", "upstream"), ("MID", "midstream"), ("GAS", "gas processing & LNG"), ("REF", "refining"),
                ("PCH", "petrochemicals"), ("PWR", "power"), ("H2", "hydrogen"), ("CCS", "carbon capture"))
RELS = ["published_by", "in_sector", "covers_discipline", "in_region", "in_country", "from_source", "cites",
        "cites_document", "supplied_by", "realised_by", "example_supplier", "alternative_to", "mentions",
        "has_gap", "look_in", "supplies", "alias_of", "similar_to"]
GRAPH_NODE_DEFAULT = "technology:ccs-cryogenic"
# Knowledge-graph node kinds and their colours in the network and atlas views.
KIND_COLORS = {"technology": "#4f9ad6", "source": "#d6a44f", "org": "#a8875e", "vendor": "#d6739b",
               "register": "#9a86c8", "document": "#5aa08a", "gap": "#cf6a66", "sector": "#2f6bab",
               "discipline": "#7d8a97", "region": "#6da86d", "country": "#c8963e"}
REL_COLORS = {"supplied_by": "#c2803d", "supplies": "#c2803d", "similar_to": "#8f6cc8", "alternative_to": "#8f6cc8",
              "cites": "#5e8f5e", "cites_document": "#5e8f5e", "mentions": "#5e8f5e", "in_sector": "#4a7fb5",
              "published_by": "#7d8a97", "has_gap": "#cf6a66", "look_in": "#cf6a66", "example_supplier": "#c2803d",
              "realised_by": "#8f6cc8", "alias_of": "#d6739b", "in_region": "#6da86d", "in_country": "#c8963e",
              "covers_discipline": "#7d8a97", "from_source": "#5aa08a"}
REL_COLOR_CYCLE = ["#5e8f5e", "#4a7fb5", "#c2803d", "#8f6cc8", "#cf6a66", "#5aa08a", "#c8963e", "#d6739b"]
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
/* second-level tabs on the database pages */
.subnav { max-width: 74rem; margin: 0 auto; padding: .45rem 1rem 0; display: flex; flex-wrap: wrap; gap: .25rem; }
.subnav a { color: #40506a; text-decoration: none; font-size: .88rem; padding: .32rem .75rem;
            border-radius: 6px 6px 0 0; border: 1px solid transparent; border-bottom: none; }
.subnav a:hover { color: #1c2733; }
.subnav a.active { background: #fff; border-color: #d9dee3; color: #1c2733; font-weight: 600; }
/* canvas graph views (network explorer, atlas) */
.canvasbox { position: relative; background: #0b1622; border: 1px solid #22344a; border-radius: 8px; overflow: hidden; }
.canvasbox canvas { display: block; width: 100%; height: 100%; cursor: grab; }
.canvasbox canvas.dragging { cursor: grabbing; }
.netwrap { height: 34rem; margin: 0 0 1rem; }
.mapwrap { height: 30rem; }
.netbar { display: flex; flex-wrap: wrap; gap: .4rem .6rem; align-items: center; margin: 0 0 .6rem; }
.netbar input[type=text] { flex: 1 1 14rem; }
.chip { display: inline-block; border: 1px solid #c9d2da; background: #f1f4f6; color: #40506a;
        border-radius: 999px; padding: 0 .55rem; font-size: .74rem; cursor: pointer; user-select: none; }
.chip.on { background: #0e2033; border-color: #0e2033; color: #fff; }
.legend { position: absolute; left: .6rem; bottom: .5rem; right: 1rem; display: flex; flex-wrap: wrap;
          gap: .15rem .8rem; font-size: .72rem; color: #9fb2c4; z-index: 2; pointer-events: none; }
.drawer { position: absolute; top: .6rem; right: .6rem; width: 19rem; max-width: 82%; max-height: 92%;
          overflow-y: auto; background: rgba(14,32,51,.94); color: #dbe6f2; border: 1px solid #2f4d6e;
          border-radius: 8px; padding: .7rem .8rem; font-size: .82rem; display: none; }
.drawer.open { display: block; }
.drawer h3 { margin: 0 0 .3rem; font-size: .95rem; color: #fff; }
.drawer .kbadges { margin: 0 0 .5rem; }
.drawer dl { margin: .3rem 0; }
.drawer dt { font-weight: 600; color: #9fb2c4; font-size: .74rem; margin-top: .35rem; }
.drawer dd { margin: 0; overflow-wrap: anywhere; }
.drawer a { color: #8ec3ef; }
.drawer button { margin: .5rem .4rem 0 0; padding: .2rem .55rem; font-size: .78rem; }
.drawer .close { position: absolute; top: .3rem; right: .5rem; background: none; border: none;
                 color: #9fb2c4; font-size: 1rem; padding: 0 .2rem; }
.tip { position: absolute; pointer-events: none; background: rgba(14,32,51,.95); color: #fff;
       border: 1px solid #2f4d6e; border-radius: 6px; padding: .15rem .45rem; font-size: .76rem;
       display: none; max-width: 22rem; z-index: 3; }
.mapstats { display: grid; grid-template-columns: repeat(auto-fit, minmax(6.5rem, 1fr)); gap: .5rem;
            margin: 0 0 .6rem; }
.mapstats a { display: block; background: #10203180; border: 1px solid #22344a; border-radius: 8px;
              padding: .4rem .2rem; text-align: center; color: #9fb2c4; font-size: .72rem;
              text-decoration: none; }
.mapstats a b { display: block; color: #fff; font-size: 1.1rem; }
"""

# Interactive force-directed network for /database/graph. Self-contained vanilla JS on one canvas:
# spring-embedder with per-kind clustering, pan/zoom, click for details, double-click to expand.
# Uses the NET config object injected just before this script by the database_graph handler.
GRAPH_JS = """
(() => {
  const cv = document.getElementById("net");
  if (!cv || typeof NET === "undefined") return;
  const ctx = cv.getContext("2d");
  const tip = document.getElementById("nettip");
  const drawer = document.getElementById("drawer");
  const dpr = window.devicePixelRatio || 1;
  const nodes = new Map();
  const edges = [];
  let center = null, alpha = 0, sel = null, hover = null, userMoved = false, frame = 0;
  const view = { x: 0, y: 0, k: 1 };
  const kindColor = (k) => NET.kindColors[k] || "#9fb2c4";
  const relColor = (r) => NET.relColors[r] || "#7d8a97";
  const esc = (s) => String(s == null ? "" : s).replace(/[&<>"']/g,
    (c) => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"}[c]));

  const W = () => cv.width / dpr, H = () => cv.height / dpr;
  function resize() { cv.width = Math.max(300, cv.clientWidth) * dpr; cv.height = Math.max(220, cv.clientHeight) * dpr; }
  window.addEventListener("resize", () => { resize(); fit(); });
  resize();

  function addNode(n, cx, cy) {
    const nid = n.id || n.node_id;
    let v = nodes.get(nid);
    if (v) { v.kind = n.kind; v.label = n.label || nid; v.props = n.props || {}; return v; }
    const a = Math.random() * 6.2832, r = 40 + Math.random() * 140;
    v = { id: nid, kind: n.kind, label: n.label || nid, props: n.props || {},
          x: (cx || 0) + Math.cos(a) * r, y: (cy || 0) + Math.sin(a) * r, vx: 0, vy: 0, deg: 0 };
    nodes.set(nid, v);
    return v;
  }
  function addEdges(list) {
    for (const e of list) {
      const a = nodes.get(e.src), b = nodes.get(e.dst);
      if (!a || !b) continue;
      if (edges.some((x) => x.a === a && x.b === b && x.rel === e.rel)) continue;
      edges.push({ a, b, rel: e.rel });
    }
    for (const v of nodes.values()) v.deg = 0;
    for (const e of edges) { e.a.deg++; e.b.deg++; }
  }
  function s2w(px, py) { return { x: (px - W() / 2) / view.k + view.x, y: (py - H() / 2) / view.k + view.y }; }

  const checked = () => [...document.querySelectorAll("#netcontrols input[name=rels]:checked")].map((x) => x.value);
  const depthVal = () => parseInt(document.getElementById("netdepth").value, 10) || 1;

  async function load(id, opts) {
    if (!id) return;
    const o = opts || {};
    const p = new URLSearchParams();
    p.set("id", id);
    p.set("depth", String(o.depth || depthVal()));
    const rels = o.rels || checked();
    if (rels.length) p.set("rels", rels.join(","));
    try {
      const r = await fetch("/database/graph/neighborhood.json?" + p.toString());
      const j = await r.json();
      if (!r.ok || j.error) throw new Error(j.error || ("HTTP " + r.status));
      if (o.keep) {
        j.neighbors.forEach((n) => addNode(n));
        addNode(j.center);
        addEdges(j.edges);
        alpha = Math.max(alpha, 0.7);
      } else {
        nodes.clear(); edges.length = 0; sel = null; hover = null; hideDrawer();
        userMoved = false;
        center = addNode(j.center);
        j.neighbors.forEach((n) => addNode(n));
        addEdges(j.edges);
        alpha = 1;
        fit();
      }
    } catch (err) { flash(String(err.message || err)); }
  }

  function fit() {
    if (!nodes.size) return;
    let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    for (const v of nodes.values()) {
      x0 = Math.min(x0, v.x); y0 = Math.min(y0, v.y); x1 = Math.max(x1, v.x); y1 = Math.max(y1, v.y);
    }
    const pad = 70;
    view.x = (x0 + x1) / 2; view.y = (y0 + y1) / 2;
    view.k = Math.min(2.5, Math.max(0.05, Math.min((W() - pad) / Math.max(80, x1 - x0 + pad), (H() - pad) / Math.max(80, y1 - y0 + pad))));
  }

  function tick() {
    const list = [...nodes.values()];
    const n = list.length;
    if (alpha > 0.004 && n > 1) {
      const rep = 1400;
      for (let i = 0; i < n; i++) {
        const a = list[i];
        for (let j = i + 1; j < n; j++) {
          const b = list[j];
          let dx = a.x - b.x, dy = a.y - b.y, d2 = dx * dx + dy * dy;
          if (d2 < 0.01) { dx = Math.random() - 0.5; dy = Math.random() - 0.5; d2 = 0.25; }
          const d = Math.sqrt(d2), f = rep / d2;
          const fx = (dx / d) * f, fy = (dy / d) * f;
          a.vx += fx; a.vy += fy; b.vx -= fx; b.vy -= fy;
        }
      }
      for (const e of edges) {
        const dx = e.b.x - e.a.x, dy = e.b.y - e.a.y;
        const d = Math.sqrt(dx * dx + dy * dy) || 1;
        const f = (d - 70) * 0.03, fx = (dx / d) * f, fy = (dy / d) * f;
        e.a.vx += fx; e.a.vy += fy; e.b.vx -= fx; e.b.vy -= fy;
      }
      const cent = {};
      for (const v of list) {
        const c = cent[v.kind] || (cent[v.kind] = { x: 0, y: 0, c: 0 });
        c.x += v.x; c.y += v.y; c.c++;
      }
      for (const k in cent) { cent[k].x /= cent[k].c; cent[k].y /= cent[k].c; }
      for (const v of list) {
        v.vx += (cent[v.kind].x - v.x) * 0.012 - v.x * 0.006;
        v.vy += (cent[v.kind].y - v.y) * 0.012 - v.y * 0.006;
        v.vx *= 0.8; v.vy *= 0.8;
        v.x += Math.max(-30, Math.min(30, v.vx));
        v.y += Math.max(-30, Math.min(30, v.vy));
      }
      alpha *= 0.988;
    }
    if (!userMoved && alpha > 0.05 && ++frame % 24 === 0) fit();
    draw();
    requestAnimationFrame(tick);
  }

  function draw() {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.fillStyle = "#0b1622";
    ctx.fillRect(0, 0, W(), H());
    ctx.translate(W() / 2, H() / 2);
    ctx.scale(view.k, view.k);
    ctx.translate(-view.x, -view.y);
    ctx.lineWidth = 1 / view.k;
    ctx.font = (11 / view.k) + "px system-ui, sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "top";
    const named = view.k > 0.75;
    for (const e of edges) {
      ctx.strokeStyle = relColor(e.rel);
      ctx.globalAlpha = 0.5;
      ctx.beginPath(); ctx.moveTo(e.a.x, e.a.y); ctx.lineTo(e.b.x, e.b.y); ctx.stroke();
    }
    ctx.globalAlpha = 1;
    for (const v of nodes.values()) {
      const r = 3 + Math.sqrt(v.deg) * 1.7;
      ctx.fillStyle = kindColor(v.kind);
      ctx.beginPath(); ctx.arc(v.x, v.y, r, 0, 6.2832); ctx.fill();
      if (v === center || v === sel) {
        ctx.strokeStyle = v === center ? "#ffffff" : "#ffd166";
        ctx.lineWidth = 1.6 / view.k;
        ctx.beginPath(); ctx.arc(v.x, v.y, r + 3.5 / view.k, 0, 6.2832); ctx.stroke();
        ctx.lineWidth = 1 / view.k;
      }
      if (named || v.deg >= 6 || v === sel || v === hover) {
        ctx.fillStyle = "#dbe6f2";
        const t = v.label.length > 34 ? v.label.slice(0, 33) + "\\u2026" : v.label;
        ctx.fillText(t, v.x, v.y + r + 2 / view.k);
      }
    }
  }

  function pick(x, y) {
    let best = null, bd = 1e9;
    for (const v of nodes.values()) {
      const r = 3 + Math.sqrt(v.deg) * 1.7 + 4 / view.k;
      const d = (v.x - x) * (v.x - x) + (v.y - y) * (v.y - y);
      if (d < r * r && d < bd) { best = v; bd = d; }
    }
    return best;
  }

  function nodeLink(n) {
    const i = n.id.indexOf(":");
    const kind = n.id.slice(0, i), key = n.id.slice(i + 1);
    if (kind === "technology") return "/technologies/" + encodeURIComponent(key);
    if (kind === "source") return "/sources/" + encodeURIComponent(key);
    if (kind === "document") return "/documents?path=" + encodeURIComponent(key);
    if (kind === "gap") return "/technologies/" + encodeURIComponent(key.split(":")[0]);
    if (kind === "sector") return "/technologies?sector=" + encodeURIComponent(key);
    return "";
  }

  function showDrawer(n) {
    sel = n;
    const props = n.props || {};
    const rows = Object.keys(props).filter((k) => props[k] !== "" && props[k] != null)
      .map((k) => "<dt>" + esc(k) + "</dt><dd>" +
        esc(Array.isArray(props[k]) ? props[k].join(", ") : props[k]) + "</dd>").join("");
    const link = nodeLink(n);
    drawer.innerHTML =
      '<button class="close" id="dclose" aria-label="Close">\\u2715</button>' +
      "<h3>" + esc(n.label) + "</h3>" +
      '<p class="kbadges"><span class="badge" style="background:' + kindColor(n.kind) + '">' + esc(n.kind) + "</span></p>" +
      "<dl><dt>id</dt><dd>" + esc(n.id) + "</dd></dl>" +
      (rows ? "<dl>" + rows + "</dl>" : "") +
      (link ? '<p><a href="' + link + '">Open in the library \\u2192</a></p>' : "") +
      '<p><button id="dexpand">Expand</button><button id="dcenter">Set as centre</button>' +
      '<button class="example" id="dfit">Fit</button></p>';
    drawer.classList.add("open");
    document.getElementById("dclose").onclick = hideDrawer;
    document.getElementById("dexpand").onclick = () => load(n.id, { depth: 1, keep: true });
    document.getElementById("dcenter").onclick = () => load(n.id, { depth: depthVal() });
    document.getElementById("dfit").onclick = fit;
  }
  function hideDrawer() { drawer.classList.remove("open"); sel = null; }
  function flash(msg) {
    tip.style.display = "block"; tip.style.left = "12px"; tip.style.top = "12px"; tip.textContent = msg;
    setTimeout(() => { tip.style.display = "none"; }, 4500);
  }

  function pos(e) { const r = cv.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; }
  let pan = null;
  cv.addEventListener("mousedown", (e) => { pan = { s: pos(e), vx: view.x, vy: view.y, moved: false }; cv.classList.add("dragging"); });
  window.addEventListener("mousemove", (e) => {
    if (pan) {
      const p = pos(e), dx = p.x - pan.s.x, dy = p.y - pan.s.y;
      if (Math.abs(dx) + Math.abs(dy) > 3) { pan.moved = true; userMoved = true; }
      view.x = pan.vx - dx / view.k;
      view.y = pan.vy - dy / view.k;
      return;
    }
    if (e.target !== cv) { hover = null; tip.style.display = "none"; return; }
    const p = pos(e), w = s2w(p.x, p.y);
    hover = pick(w.x, w.y);
    if (hover) {
      tip.style.display = "block"; tip.style.left = (p.x + 12) + "px"; tip.style.top = (p.y + 12) + "px";
      tip.textContent = hover.label + " (" + hover.kind + ")";
      cv.style.cursor = "pointer";
    } else { tip.style.display = "none"; cv.style.cursor = ""; }
  });
  window.addEventListener("mouseup", (e) => {
    if (!pan) return;
    const clicked = !pan.moved;
    pan = null;
    cv.classList.remove("dragging");
    if (clicked && e.target === cv) {
      const p = pos(e), w = s2w(p.x, p.y);
      const hit = pick(w.x, w.y);
      if (hit) showDrawer(hit); else hideDrawer();
    }
  });
  cv.addEventListener("dblclick", (e) => {
    const p = pos(e), w = s2w(p.x, p.y);
    const hit = pick(w.x, w.y);
    if (hit) load(hit.id, { depth: 1, keep: true });
  });
  cv.addEventListener("wheel", (e) => {
    e.preventDefault();
    userMoved = true;
    const p = pos(e), w = s2w(p.x, p.y);
    view.k = Math.min(8, Math.max(0.05, view.k * Math.exp(-e.deltaY * 0.0012)));
    view.x = w.x - (p.x - W() / 2) / view.k;
    view.y = w.y - (p.y - H() / 2) / view.k;
  }, { passive: false });

  const form = document.getElementById("netcontrols");
  const nodebox = document.getElementById("nodebox");
  const datalist = document.getElementById("nodelist");
  let deb = 0;
  nodebox.addEventListener("input", () => {
    clearTimeout(deb);
    const q = nodebox.value.trim();
    if (q.length < 2) { datalist.innerHTML = ""; return; }
    deb = setTimeout(async () => {
      try {
        const r = await fetch("/database/graph/nodes.json?q=" + encodeURIComponent(q));
        const j = await r.json();
        if (Array.isArray(j)) {
          datalist.innerHTML = j.map((n) =>
            '<option value="' + esc(n.id) + '">' + esc(n.label) + "</option>").join("");
        }
      } catch (err) { /* suggestions are optional */ }
    }, 250);
  });
  form.addEventListener("submit", (e) => { e.preventDefault(); load(nodebox.value.trim()); });
  document.getElementById("netdepth").addEventListener("change", () => { if (center) load(center.id); });
  form.querySelectorAll("input[name=rels]").forEach((x) =>
    x.addEventListener("change", () => { if (center) load(center.id); }));
  document.getElementById("netfit").addEventListener("click", fit);

  if (NET.node) load(NET.node, { depth: NET.depth, rels: NET.rels });
  tick();
})();
"""

# The atlas for /database/map: the whole knowledge graph as a constellation. One bubble per node
# kind sized by its live count, one drifting dot per real node (capped), and ribbons for the
# kind-pairs that actually have edges. Uses the ATLAS config object injected before this script.
ATLAS_JS = """
(() => {
  const cv = document.getElementById("atlas");
  if (!cv || typeof ATLAS === "undefined") return;
  const ctx = cv.getContext("2d");
  const tip = document.getElementById("atlastip");
  const dpr = window.devicePixelRatio || 1;
  const kinds = ATLAS.kinds || [];
  const color = (k) => ATLAS.kindColors[k] || "#9fb2c4";
  const relColor = (r) => ATLAS.relColors[r] || "#7d8a97";
  let t = 0;
  let lastW = 0, lastH = 0;

  function resize() { cv.width = Math.max(300, cv.clientWidth) * dpr; cv.height = Math.max(240, cv.clientHeight) * dpr; }
  window.addEventListener("resize", () => { resize(); layout(); });
  resize();

  const K = Math.max(1, kinds.length);
  function layout() {
    lastW = cv.width; lastH = cv.height;
    const w = cv.width / dpr, h = cv.height / dpr;
    const R = Math.min(w, h) * 0.33, maxn = kinds.length ? kinds[0].n : 1, maxr = Math.min(w, h) * 0.14;
    kinds.forEach((k, i) => {
      const a = -Math.PI / 2 + (i * 2 * Math.PI) / K;
      k.bx = w / 2 + Math.cos(a) * R;
      k.by = h / 2 + Math.sin(a) * R;
      k.r = Math.max(16, maxr * Math.sqrt(k.n / maxn));
    });
  }
  layout();

  const byKind = kinds.map(() => []);
  kinds.forEach((k, ki) => {
    const m = Math.min(k.n, 140);
    for (let i = 0; i < m; i++) {
      const a = Math.random() * 6.2832, rr = Math.sqrt(Math.random()) * 0.92;
      byKind[ki].push({ dx: Math.cos(a) * rr, dy: Math.sin(a) * rr, ph: Math.random() * 6.2832, sp: 0.4 + Math.random() * 0.8 });
    }
  });
  const ribbons = (ATLAS.pairs || []).filter((p) => p.n >= 3).slice(0, 36)
    .map((p) => ({ ...p, a: kinds.find((k) => k.kind === p.src_kind), b: kinds.find((k) => k.kind === p.dst_kind) }))
    .filter((p) => p.a && p.b);

  function ctrl(rb) {
    const w = cv.width / dpr, h = cv.height / dpr;
    const mx = (rb.a.bx + rb.b.bx) / 2, my = (rb.a.by + rb.b.by) / 2;
    return { x: (w / 2 + mx) / 2, y: (h / 2 + my) / 2 };
  }

  function draw() {
    if (cv.width !== lastW || cv.height !== lastH) layout();
    const w = cv.width / dpr, h = cv.height / dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.fillStyle = "#0b1622";
    ctx.fillRect(0, 0, w, h);
    for (const rb of ribbons) {
      const c = ctrl(rb);
      ctx.strokeStyle = relColor(rb.rel);
      ctx.globalAlpha = 0.3;
      ctx.lineWidth = Math.min(9, 0.7 + Math.log10(1 + rb.n) * 1.8);
      ctx.beginPath();
      ctx.moveTo(rb.a.bx, rb.a.by);
      ctx.quadraticCurveTo(c.x, c.y, rb.b.bx, rb.b.by);
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
    kinds.forEach((k, ki) => {
      ctx.fillStyle = color(k.kind) + "26";
      ctx.beginPath(); ctx.arc(k.bx, k.by, k.r, 0, 6.2832); ctx.fill();
      ctx.strokeStyle = color(k.kind);
      ctx.lineWidth = 1;
      ctx.stroke();
      ctx.fillStyle = color(k.kind);
      for (const d of byKind[ki]) {
        ctx.globalAlpha = 0.7;
        ctx.beginPath();
        ctx.arc(k.bx + d.dx * k.r + Math.sin(t * d.sp + d.ph) * 3,
                k.by + d.dy * k.r + Math.cos(t * d.sp * 0.8 + d.ph) * 3, 1.5, 0, 6.2832);
        ctx.fill();
      }
      ctx.globalAlpha = 1;
      ctx.fillStyle = "#dbe6f2";
      ctx.font = "12px system-ui, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(k.kind + " \\u00b7 " + k.n, k.bx, Math.min(h - 16, k.by + k.r + 8));
    });
  }

  function pick(p) {
    for (const k of kinds) {
      const dx = p.x - k.bx, dy = p.y - k.by;
      if (dx * dx + dy * dy <= k.r * k.r) return { type: "kind", k };
    }
    for (const rb of ribbons) {
      const c = ctrl(rb);
      for (let i = 0; i <= 24; i++) {
        const u = i / 24, iu = 1 - u;
        const x = iu * iu * rb.a.bx + 2 * iu * u * c.x + u * u * rb.b.bx;
        const y = iu * iu * rb.a.by + 2 * iu * u * c.y + u * u * rb.b.by;
        const dx = p.x - x, dy = p.y - y;
        if (dx * dx + dy * dy < 49) return { type: "rel", rb };
      }
    }
    return null;
  }
  function pos(e) { const r = cv.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; }
  cv.addEventListener("mousemove", (e) => {
    const p = pos(e), hit = pick(p);
    if (hit) {
      tip.style.display = "block"; tip.style.left = (p.x + 12) + "px"; tip.style.top = (p.y + 12) + "px";
      tip.textContent = hit.type === "kind"
        ? hit.k.kind + " \\u2014 " + hit.k.n + " nodes \\u00b7 click to open the network here"
        : hit.rb.rel + " \\u2014 " + hit.rb.n + " edges (" + hit.rb.src_kind + " \\u2192 " + hit.rb.dst_kind + ")";
      cv.style.cursor = "pointer";
    } else { tip.style.display = "none"; cv.style.cursor = ""; }
  });
  cv.addEventListener("click", async (e) => {
    const hit = pick(pos(e));
    if (!hit || hit.type !== "kind") return;
    try {
      const r = await fetch("/database/graph/center.json?kind=" + encodeURIComponent(hit.k.kind));
      const j = await r.json();
      if (j.id) window.location.href = "/database/graph?node=" + encodeURIComponent(j.id) + "&depth=2";
    } catch (err) { /* navigation is best-effort */ }
  });
  (function frame() { t += 0.016; draw(); requestAnimationFrame(frame); })();
})();
"""


def is_web_path(path: str) -> bool:
    """True for "/" and any path starting with a PREFIX at a segment boundary (/technologiesx is not a web path)."""
    if path == "/":
        return True
    return any(path == p or path.startswith(p + "/") for p in PREFIXES)


def session_token(key: str) -> str:
    return hmac.new(key.encode(), b"hilir-tech-library web session v1", sha256).hexdigest()


def _client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else ""


def _account(request: Request, key: str) -> dict | None:
    """The authenticated identity: {'kind': 'key', 'role': 'admin'} for the library key
    (header or cookie — the key is the owner's credential), the owning account row for a
    per-user API key (hlt_… header, role inherited from the account), or the account row
    for a v2 session. A v2 session is only valid while its account still exists, so
    deleting an account in the admin page revokes access within the account-cache window."""
    given = request.headers.get("x-api-key") or request.headers.get("authorization", "").removeprefix("Bearer ").strip()
    if given:
        if hmac.compare_digest(given.encode(), key.encode()):
            return {"kind": "key", "email": None, "name": "library key", "role": "admin"}
        if given.startswith(userstore.KEY_PREFIX):
            return userstore.account_for_key(given)
        return None
    token = request.cookies.get(COOKIE, "")
    if token.startswith("v2|"):
        email = user_accounts.session_email(token, key)
        if not email:
            return None
        row = userstore.all_accounts().get(email)
        if not row:
            return None
        return {"kind": "account", "email": email, "name": row.get("name") or email,
                "role": row.get("role") or "user"}
    if token and hmac.compare_digest(token.encode(), session_token(key).encode()):
        return {"kind": "key", "email": None, "name": "library key", "role": "admin"}
    return None


def _authed(request: Request, key: str) -> bool:
    return _account(request, key) is not None


def _is_admin(request: Request, key: str) -> bool:
    account = _account(request, key)
    return bool(account) and account["role"] == "admin"


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


def _page(title, body, *, q="", active="", subnav=None, subactive="", admin_nav=False) -> HTMLResponse:
    links = []
    nav_items = NAV + (("Admin", "/admin"), ("Account", "/account")) if admin_nav else NAV + (("Account", "/account"),)
    for label, href in nav_items:
        mark = ' class="active"' if href == active else ""
        links.append(f'<a href="{href}"{mark}>{label}</a>')
    nav = "".join(links)
    tabs = ""
    if subnav:
        tabs = '<nav class="subnav">' + "".join(
            f'<a href="{href}"{" class=\"active\"" if href == subactive else ""}>{esc(label)}</a>'
            for label, href in subnav) + "</nav>"
    return HTMLResponse(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} — HILIR Technology Library</title>
<style>{CSS}</style>
</head>
<body>
<header><div class="bar">
<a class="brand" href="/">HILIR Technology Library</a>
<nav>{nav}</nav>
<form action="/search" method="get"><input type="search" name="q" value="{esc(q)}" placeholder="Search the library" aria-label="Search"><button type="submit">Search</button></form>
<form action="/logout" method="post"><button type="submit" class="ghost">Sign out</button></form>
</div></header>
{tabs}
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
KIND_OPTIONS = [("all", "all"), ("source", "source"), ("chunk", "chunk"), ("technology", "technology"),
                ("vendor", "vendor")]
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
            ("/vendors", "Vendors"), ("/register", "Register"), ("/sources", "Sources"), ("/gaps", "Gaps"),
            ("/database", "Database"), ("/database/map", "Atlas")))
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
            userstore.set_dsn_from_header(request.headers.get(userstore.HEADER_DSN))
            form = await request.form()
            next_url = _safe_next(form.get("next"))
            email = str(form.get("email") or "").strip()
            if email:
                # secret entries and admin-page accounts share one namespace; verify against
                # whichever holds the email (scrypt verification is constant-time on the hash)
                row = userstore.all_accounts().get(email.lower())
                user = row if row and user_accounts.verify_password(str(form.get("password") or ""), row["hash"]) else None
                if user:
                    userstore.record("login_ok", user["email"], "", _client_ip(request))
                    resp = RedirectResponse(next_url, status_code=303)
                    resp.set_cookie(COOKIE, user_accounts.session_token(user["email"], key),
                                    max_age=user_accounts.SESSION_TTL, httponly=True, secure=True,
                                    samesite="lax", path="/")
                    return resp
                time.sleep(0.5)  # damp online guessing; constant-ish failure time
                userstore.record("login_fail", email, "wrong email or password", _client_ip(request))
                error = '<p><b>Wrong email or password.</b></p>'
            else:
                if hmac.compare_digest(str(form.get("key") or "").encode(), key.encode()):
                    userstore.record("login_ok", "key", "", _client_ip(request))
                    resp = RedirectResponse(next_url, status_code=303)
                    resp.set_cookie(COOKIE, session_token(key), max_age=2592000, httponly=True,
                                    secure=True, samesite="lax", path="/")
                    return resp
                time.sleep(0.5)
                userstore.record("login_fail", "key", "wrong key", _client_ip(request))
                error = '<p><b>Wrong key.</b></p>'
        else:
            next_url = _safe_next(request.query_params.get("next"))
            error = ""
        account_form = (f'<form method="post" action="/login"><input type="hidden" name="next" value="{esc(next_url)}">'
                        '<p><label>Email <input type="email" name="email" autofocus required autocomplete="username"></label></p>'
                        '<p><label>Password <input type="password" name="password" required autocomplete="current-password"></label></p>'
                        '<p><button type="submit">Sign in</button></p></form>')
        key_form = (f'<form method="post" action="/login"><input type="hidden" name="next" value="{esc(next_url)}">'
                    '<p><label>API key <input type="password" name="key" required></label></p>'
                    '<p><button type="submit">Sign in</button></p></form>')
        # The page is public: no account-state disclosure, secret names or internal docs.
        # Both forms always render; with no accounts configured, an email attempt fails
        # exactly like a wrong password (generic 401 after the damping delay).
        body = (f'<section class="card narrow"><h1>Sign in</h1>{error}{account_form}</section>'
                f'<section class="card narrow"><h2>Or with the library key</h2>{key_form}</section>')
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
            for title, want in (("Technologies", "technology"), ("Vendors", "vendor"), ("Sources", "source"),
                                ("Passages", "chunk")):
                hits = [r for r in results if r.get("kind") == want]
                if hits:
                    render = _tech_row if want == "technology" else _vendor_row if want == "vendor" else \
                        _source_row if want == "source" else _chunk_row
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

    async def vendors_page(request: Request):
        qp = request.query_params
        sector, role, query = str(qp.get("sector") or ""), str(qp.get("role") or ""), str(qp.get("q") or "")
        items = tools.list_vendors(role or None, sector or None, query or None)
        vid = str(qp.get("id") or "")
        if vid:
            items = [v for v in items if v.get("id") == vid]
        # linked technology names come from the built index, so the hosted server agrees with this page
        card_names = {t.get("id"): t.get("name") for t in tools.compare_technologies()}
        body_rows = []
        for v in items:
            name = f'<a href="{esc(v["url"])}">{esc(v["name"])}</a>' if v.get("url") else esc(v["name"])
            techs = "; ".join(f'<a href="/technologies/{esc(t)}">{esc(card_names.get(t, t))}</a>'
                              for t in v.get("technologies", []))
            body_rows.append(f'<tr><td>{name}</td><td>{esc(v.get("country") or "—")}</td>'
                             f'<td>{esc(", ".join(v.get("roles", [])))}</td>'
                             f'<td>{esc("; ".join(v.get("products", []))) or "—"}</td>'
                             f'<td>{techs or "—"}</td>'
                             f'<td class="muted small"><a href="/database/graph?node=vendor:{esc(v["id"])}&amp;depth=1">graph</a></td></tr>')
        body = ('<section class="card"><form class="filters" method="get" action="/vendors">'
                + _select("sector", SECTOR_OPTIONS, sector)
                + _select("role", [("", "any role")] + [(r, r) for r in
                            ("oem", "licensor", "packager", "epc", "developer", "operator", "rental", "service",
                             "supplier", "integrator")], role)
                + f' <input type="search" name="q" value="{esc(query)}" placeholder="name, product, description" size="20">'
                + ' <button type="submit">Filter</button></form>'
                + f'<p class="muted">{len(items)} vendor records. Curated one-per-vendor directory citing its pages; '
                'the graph column opens the record in the network view.</p>'
                + '<div class="scroll"><table><thead><tr><th>Vendor</th><th>Country</th><th>Roles</th><th>Products</th>'
                + f'<th>Supplies</th><th></th></tr></thead><tbody>{"".join(body_rows)}</tbody></table></div></section>')
        queue = _coverage_queue()
        if queue:
            blocks = "".join(f"<li><b>{esc(code)}</b> ({len(names)}): {esc('; '.join(names))}</li>"
                             for code, names in queue)
            body += (_section("Coverage queue: supplier names on cards not yet in the directory",
                              f'<ul class="small">{blocks}</ul><p class="muted small">Adding a record for one of '
                              'them is the next batch of the directory (see catalog/index/vendors.md).</p>'))
        return _page("Vendors", body, active="/vendors")

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
            return _page("Database", _db_panel(), active="/database", subnav=DATABASE_TABS, subactive="/database")
        body = []
        try:
            counts = pg.counts()
        except pg.NotConfigured:
            return _page("Database", _db_panel(), active="/database", subnav=DATABASE_TABS, subactive="/database")
        except pg.DatabaseError as e:
            body.append(_error_box(str(e)))
        else:
            stats = "".join(f'<div class="stat"><b>{esc(v)}</b>{esc(k)}</div>' for k, v in counts.items())
            body.append(f'<section class="card"><div class="stats">{stats}</div></section>')
        views = "".join(
            f'<a href="{href}"><span class="dot" style="background:{color}"></span><span><b>{esc(label)}</b>'
            f'<br><span class="muted small">{esc(desc)}</span></span></a>'
            for label, href, color, desc in (
                ("Tables and schema", "/database", "#5a6b7b", "row counts, columns, example queries (this page)"),
                ("SQL console", "/database/sql", "#4a7fb5", "run one read-only SELECT against schema og"),
                ("Semantic search", "/database/search", "#5e8f5e", "hybrid keyword + vector ranking over passages, cards and vendors"),
                ("Network", "/database/graph", "#c2803d", "walk the knowledge graph from any node, interactively"),
                ("Atlas", "/database/map", "#8f6cc8", "the whole graph as a constellation of node kinds")))
        body.append(f'<section class="card"><h2>Database views</h2><div class="grid">{views}</div></section>')
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
        return _page("Database", "".join(body), active="/database", subnav=DATABASE_TABS, subactive="/database")

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
                return _page("SQL console", empty, active="/database", subnav=DATABASE_TABS, subactive="/database/sql")
        result = error = None
        try:
            result = pg.run_sql(sql, max_rows)
        except pg.NotConfigured:
            return _page("SQL console", _db_panel(), active="/database", subnav=DATABASE_TABS, subactive="/database/sql")
        except (pg.BadSql, pg.DatabaseError) as e:
            error = str(e)
        body = [_sql_console(sql, max_rows)]
        if error is not None:
            body.append(_error_box(error))
        elif result is not None:
            body.append(_sql_result(result))
        return _page("SQL console", "".join(body), active="/database", subnav=DATABASE_TABS, subactive="/database/sql")

    async def database_search(request: Request):
        if not pg.configured():
            return _page("Semantic search", _db_panel(), active="/database", subnav=DATABASE_TABS, subactive="/database/search")
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
                return _page("Semantic search", _db_panel(), active="/database", subnav=DATABASE_TABS, subactive="/database/search")
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
        return _page("Semantic search", "".join(body), active="/database", subnav=DATABASE_TABS, subactive="/database/search")

    async def database_graph(request: Request):
        if not pg.configured():
            return _page("Graph", _db_panel(), active="/database", subnav=DATABASE_TABS, subactive="/database/graph")
        qp = request.query_params
        node = str(qp.get("node") or GRAPH_NODE_DEFAULT)
        depth = _int(qp.get("depth"), 2, 1, 3)
        chosen = [r for r in RELS if r in qp.getlist("rels")]
        try:
            overview = pg.graph_overview()
        except pg.DatabaseError as e:
            return _page("Graph", _error_box(str(e)), active="/database", subnav=DATABASE_TABS, subactive="/database/graph")
        rel_counts = {r["rel"]: r["n"] for r in overview["rels"]}
        kind_counts = {k["kind"]: k["n"] for k in overview["kinds"]}
        boxes = "".join(
            f'<label class="check"><input type="checkbox" name="rels" value="{esc(r)}"'
            f'{" checked" if r in chosen else ""}>{esc(r)} <span class="muted">{rel_counts.get(r, 0)}</span></label>'
            for r in RELS)
        legend = "".join(
            f'<span><span class="dot" style="background:{KIND_COLORS.get(k, COLOR_FALLBACK)}"></span> '
            f'{esc(k)} <span class="muted">{n}</span></span>' for k, n in kind_counts.items())
        body = ['<section class="card"><form id="netcontrols" method="get" action="/database/graph">'
                '<div class="netbar">'
                f'<label>Start node <input type="text" id="nodebox" name="node" list="nodelist" value="{esc(node)}" size="30"></label>'
                '<datalist id="nodelist"></datalist>'
                '<label>Depth <select name="depth" id="netdepth">'
                + "".join(f'<option value="{d}"{" selected" if d == depth else ""}>{d}</option>' for d in (1, 2, 3))
                + '</select></label> <button type="submit">Walk</button>'
                '<button type="button" class="example" id="netfit">Fit</button>'
                '<a class="small" href="/database/map">Atlas view →</a></div>'
                f'<p class="small">{boxes}</p>'
                '<p class="muted small">With every relation unchecked the walk follows all of them. In the map: '
                'click a node for details, double-click to expand it, drag to pan, scroll to zoom.</p></form></section>'
                f'<div class="canvasbox netwrap"><canvas id="net"></canvas><div class="tip" id="nettip"></div>'
                f'<div class="drawer" id="drawer"></div><div class="legend">{legend}</div></div>']
        if node.strip():
            try:
                rows = pg.graph_neighbors(node, depth, chosen or None)
            except pg.BadSql as e:
                rows = None
                body.append(_error_box(str(e)))
            except pg.DatabaseError as e:
                rows = None
                body.append(_error_box(str(e)))
            if rows is not None:
                if rows:
                    trs = "".join(
                        f"<tr><td>{esc(r.get('node_id'))}</td><td>{esc(r.get('kind'))}</td><td>{esc(r.get('label'))}</td>"
                        f"<td>{esc(r.get('depth'))}</td><td>{esc(', '.join(str(v) for v in r.get('via') or []))}</td></tr>"
                        for r in rows)
                    body.append('<details class="card"><summary>The same walk as a table (works without JavaScript)</summary>'
                                '<div class="scroll"><table><thead><tr><th>Node</th><th>Kind</th><th>Label</th>'
                                '<th>Depth</th><th>Via</th></tr></thead>'
                                f'<tbody>{trs}</tbody></table></div></details>')
                else:
                    body.append(_section("", '<p class="muted">No neighbors found for that node.</p>'))
        net = json.dumps({"node": node, "depth": depth, "rels": chosen, "kindColors": KIND_COLORS,
                          "relColors": REL_COLORS}).replace("</", "<\\/")
        body.append(f"<script>const NET = {net};\n{GRAPH_JS}</script>")
        return _page("Graph", "".join(body), active="/database", subnav=DATABASE_TABS, subactive="/database/graph")

    async def database_map(request: Request):
        if not pg.configured():
            return _page("Atlas", _db_panel(), active="/database", subnav=DATABASE_TABS, subactive="/database/map")
        try:
            overview = pg.graph_overview()
            counts = pg.counts()
        except pg.DatabaseError as e:
            return _page("Atlas", _error_box(str(e)), active="/database", subnav=DATABASE_TABS, subactive="/database/map")
        stat = "".join(f'<a href="/database"><b>{esc(v)}</b>{esc(k)}</a>' for k, v in counts.items())
        kind_rows = "".join(f'<tr><td>{esc(k["kind"])}</td><td>{k["n"]}</td></tr>' for k in overview["kinds"])
        rel_rows = "".join(f'<tr><td>{esc(r["rel"])}</td><td>{r["n"]}</td></tr>' for r in overview["rels"])
        atlas = json.dumps({"kinds": overview["kinds"], "pairs": overview["pairs"],
                            "kindColors": KIND_COLORS, "relColors": REL_COLORS}).replace("</", "<\\/")
        body = [f'<section class="card"><div class="mapstats">{stat}</div></section>',
                '<section class="card"><h2>Library atlas</h2>'
                '<p class="muted small">Each bubble is one kind of node in the knowledge graph, sized by how many '
                'nodes of that kind the database holds, with one drifting dot per real node (capped at 140 per kind). '
                'Ribbons are the relations between kinds, thicker when there are more edges. Click a bubble to open '
                'the network view at that kind&rsquo;s most connected node; hover a ribbon for the relation.</p>'
                '<div class="canvasbox mapwrap"><canvas id="atlas"></canvas><div class="tip" id="atlastip"></div></div></section>',
                '<details class="card"><summary>The same numbers as tables</summary><div class="scroll">'
                '<table><thead><tr><th>Kind</th><th>Nodes</th></tr></thead><tbody>' + kind_rows + '</tbody></table>'
                '<table><thead><tr><th>Relation</th><th>Edges</th></tr></thead><tbody>' + rel_rows +
                '</tbody></table></div></details>',
                f"<script>const ATLAS = {atlas};\n{ATLAS_JS}</script>"]
        return _page("Atlas", "".join(body), active="/database", subnav=DATABASE_TABS, subactive="/database/map")

    async def graph_overview_json(request: Request):
        if not pg.configured():
            return JSONResponse({"error": "database not configured"}, status_code=503)
        try:
            return JSONResponse(pg.graph_overview())
        except pg.DatabaseError as e:
            return JSONResponse({"error": str(e)}, status_code=502)

    async def graph_nodes_json(request: Request):
        if not pg.configured():
            return JSONResponse({"error": "database not configured"}, status_code=503)
        q = str(request.query_params.get("q") or "")
        if len(q.strip()) < 2:
            return JSONResponse([])
        try:
            return JSONResponse(pg.node_search(q, _int(request.query_params.get("limit"), 12, 1, 30)))
        except pg.DatabaseError as e:
            return JSONResponse({"error": str(e)}, status_code=502)

    async def graph_neighborhood_json(request: Request):
        if not pg.configured():
            return JSONResponse({"error": "database not configured"}, status_code=503)
        qp = request.query_params
        node = str(qp.get("id") or "")
        rels = [r for r in RELS if r in str(qp.get("rels") or "").split(",")]
        try:
            data = pg.neighborhood(node, _int(qp.get("depth"), 1, 1, 3), rels or None,
                                   _int(qp.get("limit"), 150, 10, 300))
        except pg.BadSql as e:
            return JSONResponse({"error": str(e)}, status_code=400)
        except pg.DatabaseError as e:
            return JSONResponse({"error": str(e)}, status_code=502)
        if not data:
            return JSONResponse({"error": "no node with that id"}, status_code=404)
        return JSONResponse(data)

    async def graph_center_json(request: Request):
        if not pg.configured():
            return JSONResponse({"error": "database not configured"}, status_code=503)
        try:
            row = pg.top_node(str(request.query_params.get("kind") or ""))
        except pg.BadSql as e:
            return JSONResponse({"error": str(e)}, status_code=400)
        except pg.DatabaseError as e:
            return JSONResponse({"error": str(e)}, status_code=502)
        if not row:
            return JSONResponse({"error": "no nodes of that kind"}, status_code=404)
        return JSONResponse(row)

    def gated(handler):
        async def with_gate(request: Request):
            userstore.set_dsn_from_header(request.headers.get(userstore.HEADER_DSN))
            account = _account(request, key)
            if account is None:
                return RedirectResponse("/login?next=" + urllib.parse.quote(request.url.path), status_code=303)
            path = request.url.path
            if not path.endswith(".json"):
                who = account["email"] or "key"
                if path == "/search":
                    userstore.record("search", who, str(request.query_params.get("q") or "")[:120], _client_ip(request))
                else:
                    userstore.record("view", who, path, _client_ip(request))
            return await handler(request)
        return with_gate

    def admin_gated(handler):
        async def with_gate(request: Request):
            userstore.set_dsn_from_header(request.headers.get(userstore.HEADER_DSN))
            account = _account(request, key)
            if account is None:
                return RedirectResponse("/login?next=" + urllib.parse.quote(request.url.path), status_code=303)
            if account["role"] != "admin":
                resp = _page("Admin", '<section class="card narrow"><h1>Admin</h1>'
                                      '<p>This area is for administrators.</p></section>')
                resp.status_code = 403
                return resp
            return await handler(request)
        return with_gate

    async def account_page(request: Request):
        """Per-user page: identity and API-key self-service (create/revoke, raw shown once)."""
        account = _account(request, key)
        try:
            store_ok = userstore.configured()
            if store_ok:
                userstore.all_accounts()  # fail fast into the degraded branch below
        except Exception:
            store_ok = False
            note_store = ('<p class="muted small">The account store is unreachable right now '
                          '(USER_STORE_URL); API keys are unavailable.</p>')
        else:
            note_store = ""
        note = ""
        if account["kind"] == "key":
            body_keys = ('<p class="muted small">You are signed in with the master library key, which always '
                         'has admin rights. Per-user API keys are managed on the <a href="/admin">admin page</a> '
                         'or from an account sign-in.</p>')
        elif not store_ok:
            body_keys = (note_store + '<p class="muted small">API keys need the persistent account store '
                         '(USER_STORE_URL), which is not configured on this deployment.</p>')
        else:
            if request.method == "POST":
                label = str((await request.form()).get("label") or "")
                try:
                    raw = userstore.create_key(account["email"], label)
                    note = (f'<p><b>Your new API key (shown once — copy it now):</b><br>'
                            f'<code>{esc(raw)}</code></p>')
                except Exception as exc:
                    note = f'<p><b>Could not create the key:</b> {esc(exc)}</p>'
            my_keys = userstore.keys(email=account["email"])
            rows = "".join(
                f'<tr><td>{esc(r[3] or "(no label)")}</td><td><code>{esc(r[1])}…</code></td>'
                f'<td>{(r[4] or r[5] or "-"):%Y-%m-%d}</td><td>{f"{r[5]:%Y-%m-%d %H:%M} UTC" if r[5] else "never"}</td>'
                f'<td><form method="post" action="/account/keys/delete" class="inline">'
                f'<input type="hidden" name="id" value="{r[0]}">'
                f'<button type="submit" class="small">Revoke</button></form></td></tr>'
                for r in my_keys)
            key_table = (f'<table><tr><th>Label</th><th>Key</th><th>Created</th><th>Last used</th><th></th></tr>'
                         f'{rows}</table>') if rows else '<p class="muted small">No API keys yet.</p>'
            body_keys = (note + key_table +
                         '<h3>Create a key</h3>'
                         '<form method="post" action="/account">'
                         '<p><label>Label <input type="text" name="label" placeholder="my laptop"></label></p>'
                         '<p><button type="submit">Create API key</button></p></form>'
                         '<p class="muted small">Keys act as your account (same rights), work everywhere the '
                         'library key works (web, REST <code>x-api-key</code>, MCP), and can be revoked any time. '
                         'The raw key is never stored — only its hash.</p>')
        body = (f'<section class="card narrow"><h1>Account</h1>'
                f'<p>Signed in as <b>{esc(account.get("email") or "the library key")}</b>'
                + (f' ({esc(account.get("name") or "")})' if account.get("name") else '') +
                f'<br>Role: <b>{esc(account["role"])}</b></p></section>'
                f'<section class="card narrow"><h2>API keys</h2>{body_keys}</section>')
        return _page("Account", body)

    async def account_key_delete(request: Request):
        form = await request.form()
        my = userstore.keys(email=_account(request, key).get("email") or "")
        if any(r[0] == _int(form.get("id"), 0, 0, 10**9) for r in my):
            userstore.delete_key(_int(form.get("id"), 0, 0, 10**9))
        return RedirectResponse("/account", status_code=303)

    async def admin_page(request: Request):
        try:
            store_ok = userstore.configured()
            if store_ok:
                userstore.all_accounts()  # fail fast into the degraded branch below
        except Exception:
            store_ok = False
            store_note = ('<p><b>The account store is unreachable right now (USER_STORE_URL).</b> '
                          'Accounts, keys and analytics are unavailable; the rest of the site works.</p>')
        else:
            store_note = ""
        secret_emails = user_accounts.load_users().keys()

        def delete_cell(r):
            if not store_ok or r["email"] in secret_emails:
                return ""  # secret entries are managed by the owner via the secret, not the page
            return (f'<form method="post" action="/admin/accounts/delete" class="inline">'
                    f'<input type="hidden" name="email" value="{esc(r["email"])}">'
                    f'<button type="submit" class="small">Delete</button></form>')

        rows = sorted(userstore.all_accounts().values(), key=lambda r: r["email"]) if store_ok else []
        account_rows = "".join(
            f'<tr><td>{esc(r["email"])}</td><td>{esc(r.get("name") or "")}</td>'
            f'<td>{esc(r.get("role") or "user")}</td>'
            f'<td>{"secret" if r["email"] in secret_emails else "admin page"}</td>'
            f'<td>{delete_cell(r)}</td></tr>'
            for r in rows) or '<tr><td colspan="5" class="muted">no accounts loaded</td></tr>'
        if store_ok:
            add_form = ('<form method="post" action="/admin/accounts">'
                        '<p><label>Email <input type="email" name="email" required></label></p>'
                        '<p><label>Name <input type="text" name="name"></label></p>'
                        '<p><label>Role <select name="role"><option value="user">user</option>'
                        '<option value="admin">admin</option></select></label></p>'
                        '<p><label>Default password <input type="text" name="password" required autocomplete="off"></label></p>'
                        '<p><button type="submit">Create account</button></p></form>')
        else:
            add_form = ('<p class="muted small">Creating accounts from this page needs the persistent account '
                        'store (USER_STORE_URL). Accounts currently come from the LIBRARY_USERS secret only — '
                        'see docs/HOSTING.md.</p>')
        if store_ok:
            data = userstore.analytics()
            day_rows = "".join(f'<tr><td>{d}</td><td>{v}</td><td>{s}</td></tr>' for d, v, s in data["days"])
            top_rows = "".join(f'<tr><td>{esc(p)}</td><td>{n}</td></tr>' for p, n in data["top"])
            login_rows = "".join(f'<tr><td>{ts:%m-%d %H:%M} UTC</td><td>{esc(k)}</td><td>{esc(w)}</td>'
                                 f'<td>{esc(det)}</td><td>{esc(ipc)}</td></tr>'
                                 for ts, k, w, det, ipc in data["recent"])
            analytics = (f'<p>{data["logins_ok_7d"]} sign-ins and {data["logins_fail_7d"]} failed attempts in 7 days; '
                         f'{data["events_total"]} recorded events.</p>'
                         '<h3>Views and searches per day</h3><table><tr><th>Day</th><th>Views</th><th>Searches</th></tr>'
                         f'{day_rows}</table>'
                         '<h3>Most viewed pages (7 days)</h3><table><tr><th>Path</th><th>Views</th></tr>'
                         f'{top_rows}</table>'
                         '<h3>Recent sign-ins</h3><table><tr><th>When</th><th>Event</th><th>Who</th>'
                         f'<th>Detail</th><th>IP</th></tr>{login_rows}</table>')
        else:
            analytics = ('<p class="muted small">Activity recording needs the persistent account store '
                         '(USER_STORE_URL), so there is nothing to show yet.</p>')
        if store_ok:
            all_keys = userstore.keys()
            account_emails = sorted(userstore.all_accounts())
            key_rows = "".join(
                f'<tr><td>{esc(r[2])}</td><td>{esc(r[3] or "(no label)")}</td><td><code>{esc(r[1])}…</code></td>'
                f'<td>{(r[4] or r[5] or "-"):%Y-%m-%d}</td><td>{f"{r[5]:%Y-%m-%d %H:%M} UTC" if r[5] else "never"}</td>'
                f'<td><form method="post" action="/admin/keys/delete" class="inline">'
                f'<input type="hidden" name="id" value="{r[0]}">'
                f'<button type="submit" class="small">Revoke</button></form></td></tr>'
                for r in all_keys)
            keys_section = ('<h3>API keys</h3>' +
                            (f'<table><tr><th>Owner</th><th>Label</th><th>Key</th><th>Created</th><th>Last used</th><th></th></tr>{key_rows}</table>'
                             if all_keys else '<p class="muted small">No API keys yet.</p>') +
                            '<form method="post" action="/admin/keys">'
                            '<p><label>Account <input type="email" name="email" list="account-emails" required></label> '
                            '<datalist id="account-emails">' +
                            "".join(f'<option value="{esc(e)}">' for e in account_emails) +
                            '</datalist></p>'
                            '<p><label>Label <input type="text" name="label" placeholder="team shared key"></label></p>'
                            '<p><button type="submit">Create key</button></p></form>'
                            '<p class="muted small">A key acts as its owner\'s account (same role and rights) and '
                            'works on the web UI, REST and MCP via the x-api-key header. The raw key is shown once '
                            'after creation; only its hash is stored. Keys die with their account.</p>')
        else:
            keys_section = ('<h3>API keys</h3><p class="muted small">API keys need the persistent account store '
                            '(USER_STORE_URL), which is not configured on this deployment.</p>')
        body = (f'<section class="card"><h1>Admin</h1>{store_note}'
                f'<p class="muted small">The library key always has admin rights; account passwords are '
                f'scrypt-hashed and never shown. Deleting an account revokes its sessions within a minute '
                f'and deletes its API keys.</p></section>'
                f'<section class="card"><h2>Accounts</h2>'
                f'<table><tr><th>Email</th><th>Name</th><th>Role</th><th>Source</th><th></th></tr>{account_rows}</table>'
                f'<h3>Add an account</h3>{add_form}</section>'
                f'<section class="card"><h2>API keys</h2>{keys_section}</section>'
                f'<section class="card"><h2>Login data and analytics</h2>{analytics}</section>')
        return _page("Admin", body, admin_nav=True)

    async def admin_create(request: Request):
        form = await request.form()
        try:
            userstore.create_account(str(form.get("email") or ""), str(form.get("name") or ""),
                                     str(form.get("password") or ""), str(form.get("role") or "user"))
        except Exception as exc:
            resp = _page("Admin", f'<section class="card narrow"><h1>Admin</h1>'
                                  f'<p>Could not create the account: {esc(exc)}</p>'
                                  f'<p><a href="/admin">Back</a></p></section>', admin_nav=True)
            resp.status_code = 400
            return resp
        return RedirectResponse("/admin", status_code=303)

    async def admin_delete(request: Request):
        form = await request.form()
        userstore.delete_account(str(form.get("email") or ""))
        return RedirectResponse("/admin", status_code=303)

    async def admin_key_create(request: Request):
        form = await request.form()
        try:
            raw = userstore.create_key(str(form.get("email") or ""), str(form.get("label") or ""))
        except Exception as exc:
            resp = _page("Admin", f'<section class="card narrow"><h1>Admin</h1>'
                                  f'<p>Could not create the key: {esc(exc)}</p>'
                                  f'<p><a href="/admin">Back</a></p></section>', admin_nav=True)
            resp.status_code = 400
            return resp
        resp = _page("Admin", f'<section class="card narrow"><h1>API key created</h1>'
                              f'<p>For <b>{esc(str(form.get("email") or "").strip().lower())}</b>. '
                              f'Shown once — copy it now:</p>'
                              f'<p><code>{esc(raw)}</code></p>'
                              f'<p><a href="/admin">Back to admin</a></p></section>', admin_nav=True)
        return resp

    async def admin_key_delete(request: Request):
        userstore.delete_key(_int((await request.form()).get("id"), 0, 0, 10**9))
        return RedirectResponse("/admin", status_code=303)

    return [
        Route("/", gated(home)),
        Route("/login", login, methods=["GET", "POST"]),
        Route("/logout", logout, methods=["GET", "POST"]),
        Route("/admin", admin_gated(admin_page)),
        Route("/admin/accounts", admin_gated(admin_create), methods=["POST"]),
        Route("/admin/accounts/delete", admin_gated(admin_delete), methods=["POST"]),
        Route("/admin/keys", admin_gated(admin_key_create), methods=["POST"]),
        Route("/admin/keys/delete", admin_gated(admin_key_delete), methods=["POST"]),
        Route("/account", gated(account_page), methods=["GET", "POST"]),
        Route("/account/keys/delete", gated(account_key_delete), methods=["POST"]),
        Route("/search", gated(search)),
        Route("/technologies", gated(technologies)),
        Route("/technologies/{technology_id}", gated(technology)),
        Route("/vendors", gated(vendors_page)),
        Route("/register", gated(register)),
        Route("/sources", gated(sources)),
        Route("/sources/{source_id}", gated(source)),
        Route("/documents", gated(documents)),
        Route("/gaps", gated(gaps)),
        Route("/database", gated(database)),
        Route("/database/sql", gated(database_sql), methods=["GET", "POST"]),
        Route("/database/search", gated(database_search)),
        Route("/database/map", gated(database_map)),
        Route("/database/graph", gated(database_graph)),
        Route("/database/graph/overview.json", gated(graph_overview_json)),
        Route("/database/graph/nodes.json", gated(graph_nodes_json)),
        Route("/database/graph/neighborhood.json", gated(graph_neighborhood_json)),
        Route("/database/graph/center.json", gated(graph_center_json)),
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


def _vendor_row(hit) -> str:
    ref = hit.get("ref") or ""
    out = [f'<li><a href="/vendors?id={urllib.parse.quote(ref, safe="")}">{esc(hit.get("name") or hit.get("title") or ref)}</a> ']
    if hit.get("country"):
        out.append(f'<span class="muted">{esc(hit["country"])}</span> ')
    if hit.get("roles"):
        out.append(_pill(", ".join(hit["roles"])))
    if hit.get("technologies"):
        out.append(f'<br><span class="muted small">Supplies: {esc(", ".join(hit["technologies"]))}</span>')
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


def _coverage_queue():
    """Supplier names on technology cards that no vendor directory record answers to, by sector.

    Reads the catalog files directly (the same rule as catalog/index/vendors.md); on a hosted server
    without the files it quietly renders nothing.
    """
    try:
        import technologies
        cards = technologies.load_cards()
        records = vendor_records.load_vendors()
    except OSError:
        return []
    covered = set()
    for v in records:
        covered |= vendor_records.vendor_keys(v)
    queue = {}
    for c in cards:
        for s in c["suppliers"]:
            key = vendor_records.name_key(s["name"])
            if key not in covered:
                queue.setdefault(c["sector"], {})[key] = s["name"]
    return sorted((code, sorted(names.values(), key=str.lower)) for code, names in queue.items())
