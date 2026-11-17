# Using the MCP server

The library exposes 24 tools over MCP (stdio locally, Streamable HTTP at
`https://techlib-api.hilir.app/mcp`) and the same functionality as a REST API under `/api`. This
page is the instruction sheet for an AI agent: what each tool answers, when to reach for it, and the
rules that keep an answer honest.

Read [AUTH.md](AUTH.md) before connecting to the hosted endpoint — HTTP mode needs a hilir Access
bearer token, and by default it does not serve text from full-text-restricted sources.

---

## 1. Four rules that override everything else

1. **Cite the url.** Every source, card, vendor, project and figure carries `url` / `source_url` /
   `source.url`. An answer with no url is not using this library, it is guessing near it.
2. **Respect `reuse_level`.** `full-text-open` may be quoted; `full-text-restricted` is a private
   reference copy — paraphrase, do not reproduce, never redistribute; `summary-only` and
   `catalog-only` have no stored text, so cite the source and say what it covers.
3. **A figure without its basis is not usable.** `find_figures` returns `basis` for a reason
   (installed vs overnight vs LCOE, per kW vs per kWh, feed conditions, dollar year). Carry the
   basis into the answer.
4. **When a card records a gap, say so.** `list_gaps` and each card's `gaps` array are deliberate
   admissions. Do not fill a gap with an estimate and present it as the library's answer.

---

## 2. Route by question

| The question | Start with | Then |
|---|---|---|
| What are the options for X? | `compare_technologies(sector=..., application=...)` | `get_technology` on 2–4 ids |
| What does X cost / how efficient is X? | `find_figures(query=..., sector=...)` | `get_technology` for the whole card |
| Who supplies X, or what does vendor Y make? | `list_vendors(sector=..., query=...)` | `get_vendor` |
| What are the limits of this equipment class? | `list_equipment(equipment_type=...)` | `get_equipment` |
| Which plants/projects use X, or what is built in Z? | `list_projects(sector=..., country=..., query=...)` | `get_project` |
| What does this acronym mean? | `get_glossary_term("CCGT")` | `list_glossary(q)` to browse |
| Which code/standard applies? | `list_standards(org="API")` | `get_standard("API RP 535")` |
| Find sources or text about X | `search(q, kind=...)` — kinds include `project` and `equipment` | `get_source` / `get_document` |
| What does the library not know? | `list_gaps(...)` | `list_technology_register` for cards that do not exist yet |
| How are these connected? | `graph_neighbors(node=...)` | `sql_query` for custom joins |
| Counts, freshness, provenance of the numbers | `library_stats()` | `sql_query` against `db_catalog()` |

**Before any filter, call `taxonomy()`.** Sector codes are UPS, MID, GAS, REF, PCH, PWR, H2, CCS,
IDC, WWT; discipline codes are PRC, ROT, ELE, CIV, INS, MAT, HSE, DIG; regions include `sea`,
`apac`, `global`. A mistyped code returns an empty list, which reads like "no data" and is not.

---

## 3. Tool reference

### Discovery

**`taxonomy() → {sectors[], disciplines[], regions[], note}`**
Codes with names and subtopics. Cache it for the session; it changes only when the taxonomy does.

**`search(query, kind="all", sector=None, discipline=None, region=None, reuse_level=None, limit=10) → [rows]`**
Hybrid keyword + vector search over sources, document passages, cards, vendors, equipment and
projects. Each row carries `kind`, `ref`, `title`, `score`, `licence`, `reuse_level`,
`permitted_use` and a url.
`kind` may be `source`, `chunk`, `technology`, `vendor`, `equipment` or `project` to narrow.
Use it to *find* things; use the `get_*`/`list_*` tools to *read* them.

**`list_by_tag(code=None, region=None, reuse_level=None, source_type=None) → [sources]`**
Catalogue records by sector/discipline code, Asia Pacific ranked first. The right tool for
"what sources do we hold on midstream leak detection" — cheaper than search when you want the
inventory rather than passages.

### Cards and figures

**`compare_technologies(sector=None, maturity=None, application=None) → [cards]`**
Compact comparison table, commercial first. `maturity`: commercial, demonstration, pilot, lab;
`application` is free text ("cement", "power", "hydrogen") matched against the card's applications.

**`get_technology(technology_id) → card`**
The full card: `principle`, `process_steps` (each with equipment), `block_diagram_mermaid`,
`key_equipment`, `performance[]`, `costs[]`, `trl`, `suppliers[]`, `reference_plants[]`, `gaps[]`,
`sources[]`, `notes`. Read this before answering anything detailed about a technology.

**`find_figures(kind="both", sector=None, technology_id=None, query=None, unit=None, limit=50) → [figures]`**
One row per recorded number, across all cards:

```json
{"kind": "cost", "technology": "Heavy-duty gas turbines", "technology_id": "pwr-heavy-duty-gas-turbines",
 "metric": "overnight capital cost, heavy-duty gas turbine", "low": 836, "high": 921, "unit": "USD per kW",
 "year": 2023, "basis": "Simple cycle 1xH-class ... overnight capital, no financing.",
 "source_url": "https://www.eia.gov/...", "licence": "..."}
```

Filters: `kind` (`cost`/`performance`/`both`), `sector`, `technology_id`, `query` (substring over
metric, basis and card name), `unit` (substring, e.g. `USD/kW`, `GJ/t`, `kWh/t`, `%`). Empty results
mean the cards hold no figure for that question — check `list_gaps` rather than estimating.
An unknown `kind` raises, deliberately: silently returning everything hides the typo.

### Vendors, equipment, projects

**`list_vendors(role=None, sector=None, query=None) → [vendors]`** / **`get_vendor(vendor_id) → vendor`**
Directory records: `country`, `roles`, `categories`, `products`, `technologies[]` (the cards it
supplies), `aliases`, `notes`, `sources[]`. Ownership is often in `notes` — many suppliers have been
acquired (Motivair → Schneider Electric, LiquidStack → Trane, LEGRAND owns Raritan/Server
Technology/Starline), and a brand named on a card may resolve to a parent record through `aliases`.

**`list_equipment(equipment_type=None, query=None)`** / **`get_equipment(equipment_id)`**
Equipment classes with specification ranges (each with basis and source), vendor model lines, the
cards that use the class, and gaps.

**`list_projects(status=None, sector=None, country=None, query=None)`** / **`get_project(project_id)`**
Named plants and projects: `status` (proposed, FID, under-construction, commissioning, operating,
suspended, decommissioned), `country`, `capacities[]`, `owners[]`, `contractors[]`, `offtakers[]`,
`milestones[]` (each dated, each sourced), `technologies[]`. The `country` filter takes a full
name or a two-letter code and canonicalises mixed record spellings ("US", "USA" and
"United States" all match). Cards link here through
`reference_plants[].project_id`, so a card's reference plant and the project record are the same
thing seen from two sides.

### Register and gaps

**`list_technology_register(code=None, maturity=None, query=None)`**
The indicative register (~400 entries, all sectors). Entries with a `card` id are verified; the rest
are topics awaiting a card. Maturity and examples here are indicative, not verified.

**`list_gaps(sector=None, field=None, reason_code=None, include_no_card=False)`**
What the library knows it does not know: `field` (trl, performance, costs, reference_plants,
suppliers, status, process, other), `reason_code` (not_in_sources_read, source_unreachable,
source_not_collected, paid_source, status_unchecked, conflicting_sources, general_knowledge_only),
plus `item`, `reason`, `where`, `action`. Use it to answer "can you tell me X?" honestly and to pick
the next thing worth researching.

### Reference

**`list_glossary(query=None)` / `get_glossary_term(term)`**
Terms and abbreviations with expansion and note — resolve PUE, WUE, SMR, DLE, HRSG, MERCON, SRU
before paraphrasing them.

**`list_standards(org=None, query=None)` / `get_standard(ref)`**
Standards and codes with designation, title, scope and url. `org` filters the issuing body (API, ISO,
IEC, ASME, ASCE, CEN, NFPA, UL). When a card's `basis` cites a clause, this is where the code family
lives.

### Data layer

**`library_stats()`** — counts (sources, documents, chunks, technologies, vendors, equipment,
projects, vectors), Neon first, baked index as fallback.

**`sql_query(sql, max_rows=100)`** — one read-only `SELECT`/`WITH` against Postgres schema `og`, for
questions the tools do not express (joins across `technology`, `technology_figure`, `vendor`,
`project`, `technology_gap`, `v_gap`, `v_source`). Read `db_catalog()` first; it lists tables,
columns, views and the `hybrid_search` / `graph_neighbors` functions. 15 s statement timeout, 500-row
cap, single statement, no semicolon.

**`db_catalog()`** — the reference for `sql_query`.

**`graph_neighbors(node, depth=1, rels=None)`** — knowledge graph adjacency for nodes such as
`technology:ccs-cryogenic`, `vendor:wartsila`, `project:...`, `source:netl`, `org:honeywell-uop`.
Relations include `cites`, `supplied_by`, `similar_to`, `mentions`, `uses_technology`.

---

## 4. Three worked answers

**"What would it cost to capture CO₂ from a cement plant?"**
`compare_technologies(sector="CCS", application="cement")` → `get_technology` on the two or three
relevant cards → `find_figures(technology_id="ccs-amine-post-combustion", kind="cost")`. Answer with
the figure **and** its basis (coal vs cement scope, capture rate, dollar year), then check
`list_gaps(sector="CCS", field="costs")` to see whether the card admits a missing metric.

**"Who could supply gas engines for a 200 MW plant in Southeast Asia?"**
`taxonomy()` → `list_vendors(sector="PWR", query="engine")` → `get_vendor("wartsila")` (and INNIO,
Everllence, JEREH) → `list_projects(sector="PWR", query="engine")` for built examples such as
PLTD Pesanggaran. Quote vendor `products`, the cards they supply, and a named reference plant.

**"What is the library weakest on right now?"**
`list_gaps(field="costs")` grouped by sector, plus `list_gaps(field="trl")`. Report the counts and
the `reason_code` mix — "not_in_sources_read" is a research task, "paid_source" is an owner decision.

---

## 5. REST mirror

Same functions, same shapes, for clients without MCP:

| MCP tool | REST |
|---|---|
| `search` | `GET /api/search?q=&kind=&sector=&discipline=&region=&reuse_level=&limit=` |
| `list_by_tag` | `GET /api/sources?code=&region=&reuse_level=&source_type=` |
| `get_source` / `get_document` | `GET /api/sources/{id}` · `GET /api/documents?path=` |
| `compare_technologies` / `get_technology` | `GET /api/technologies?...` · `GET /api/technologies/{id}` |
| `find_figures` | `GET /api/figures?kind=&sector=&technology_id=&q=&unit=&limit=` |
| `list_vendors` / `get_vendor` | `GET /api/vendors?...` · `GET /api/vendors/{id}` |
| `list_equipment` / `get_equipment` | `GET /api/equipment?...` · `GET /api/equipment/{id}` |
| `list_projects` / `get_project` | `GET /api/projects?status=&sector=&country=&q=` · `GET /api/projects/{id}` |
| `list_technology_register` | `GET /api/register?...` |
| `list_gaps` | `GET /api/gaps?field=&reason_code=&include_no_card=` |
| `taxonomy` | `GET /api/taxonomy` |
| `list_glossary` / `get_glossary_term` | `GET /api/glossary?q=` · `GET /api/glossary/{term}` |
| `list_standards` / `get_standard` | `GET /api/standards?org=&q=` · `GET /api/standards/{ref}` |
| `library_stats` | `GET /api/stats` |
| (drift stamp) | `GET /api/version` |

The OpenAPI document is at `GET /api/openapi.json`.

---

## 6. Troubleshooting

| Symptom | Cause and fix |
|---|---|
| Every filtered listing is empty | A code that is not in `taxonomy()` — fetch the codes and retry. |
| `find_figures` empty for a real question | The cards hold no figure for it. `list_gaps(field="costs"|"performance")` names the gap; do not estimate. |
| `database not configured` from `sql_query` | No `DATABASE_URL`; the other tools still work on the baked SQLite index. |
| A brand is not a vendor record | It may be an alias of a parent — `get_vendor` on the parent, or `list_vendors(query=brand)`. |
| A project exists but a card has no reference plant | Cards link by `project_id`; a project can exist without being cited yet. |
| Results disagree with the website | The site and the tools both read Neon; a publish lands in both. If they differ, check `library_stats()` and `/api/version` for drift. |
