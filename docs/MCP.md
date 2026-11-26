# Using the MCP server

The library exposes 32 tools over MCP (stdio locally, Streamable HTTP at
`https://techlib-api.hilir.app/mcp`) and the same functionality as a REST API under `/api`. This
page is the instruction sheet for an AI agent: what each tool answers, when to reach for it, and the
rules that keep an answer honest. `tools/list` is the live count — this number tracks it.

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
| Which code/standard applies? | `list_standards(org="API")` | `get_standard("API 610")` |
| Find sources or text about X | `search(q, kind=...)` — kinds include `project` and `equipment` | `get_source` / `list_documents` / `get_document` |
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
`kind` may be `source`, `chunk`, `technology`, `vendor`, `equipment`, `project`, `product`, `drawing` or `material` to narrow.
Use it to *find* things; use the `get_*`/`list_*` tools to *read* them.

Ranking is **concept coverage, then density** — not literal wording. The query is expanded through
the library's concept groups (`catalog/search-concepts.yaml` — carbon = carbon + co2), each kind
contributes its own candidate pool to the reciprocal-rank fusion, and a record covering more of the
query's concepts outranks one that repeats a single word. So `q=carbon capture amine` returns
*Amine solvent post-combustion capture* first even though that card is written in CO2. Query the
concepts you want answered and keep the query short: every extra word is a concept a record must
also cover.

A word that is **rare in the library** — a product or process code such as `KS-1`, `MDEA`,
`Sulfinol`, `Benfield` — acts as a *qualifier*: it forms a third ranking pool, so records that carry
it rank above records that merely share the common words. `q=KS-1 solvent` returns the amine card
first, and `q=MDEA` returns amine acid gas removal. Rarity is measured (1% of records, floor 8), not
a hand-written list, so a code you have not seen before behaves the same way.

`kind` narrows **inside** the ranking on both layers (the SQL function `hybrid_search_kind`), so
`kind=equipment` returns equipment records rather than whatever survived a global top-k. A query
with no searchable words returns `[]`.

**`list_by_tag(code=None, region=None, reuse_level=None, source_type=None) → [sources]`**
Catalogue records by sector/discipline code, Asia Pacific ranked first. The right tool for
"what sources do we hold on midstream leak detection" — cheaper than search when you want the
inventory rather than passages.

**`list_documents(source_id=None, sector=None, limit=50) → [documents]`**
The collected-documents index: `path` (the handle `get_document` takes), `title`, `source_id`,
`source_name`, `source_url`, `reuse_level`, `sectors`, and `text_included` — false for
full-text-restricted documents, whose stored text is never served (the metadata is). One row per
source document: the corpus holds **one document per source url** (decision 40 — scheme, case,
`www.`, a trailing slash, the fragment and an arXiv version suffix are the same document), so a url
never appears twice and a `path` is a stable handle.

**`get_document(path, offset=0, limit=20000) → {meta, text, total_chars, ...}`**
Front matter and text of one document. `offset`/`limit` page through the text in characters
(default 20,000, hard cap 100,000); the corpus holds documents over 2M characters, so check
`total_chars` and page rather than asking for everything. A metadata-only record is not kept beside
the full text of the same source (an arXiv abstract record was removed where the paper itself is
stored), so there is no second copy to hunt for.

### Cards and figures

**`compare_technologies(sector=None, maturity=None, application=None, technology_ids=None) → [cards]`**
Compact comparison table, commercial first; each row carries a `gaps` count so a blank
`trl`/`costs` cell can be told apart from an unrecorded one. `maturity`: commercial,
demonstration, pilot, lab; `application` is free text ("cement", "power", "hydrogen") matched
against the card's applications. `technology_ids` compares named cards side by side in the order
given (filters do not apply; unknown ids are skipped).

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
Equipment classes with specification ranges (each with basis and `source.url`), vendor model lines,
the cards that use the class, and gaps. Listing rows and equipment search hits carry `source_urls`:
the original OEM datasheet/catalogue pages for that class. Open those URLs as primary sources when
quoting a limit; a parameter's `basis` states the printed qualifier and `source.url` is the page it
came from.

**`list_projects(status=None, sector=None, country=None, query=None)`** / **`get_project(project_id)`**
Named plants and projects: `status` (proposed, FID, under-construction, commissioning, operating,
suspended, decommissioned), `country`, `capacities[]`, `owners[]`, `contractors[]`, `offtakers[]`,
`milestones[]` (each dated, each sourced), `technologies[]`. The `country` filter takes a full
name or a two-letter code and canonicalises mixed record spellings ("US", "USA" and
"United States" all match). Cards link here through
`reference_plants[].project_id`, so a card's reference plant and the project record are the same
thing seen from two sides.

### Product catalog and process drawings

**`list_products(product_type=None, manufacturer=None, query=None)`** / **`get_product(product_id)`**
Vendor product lines with **every parameter printed on the manufacturer's catalogue/datasheet**.
`product_type` is an equipment type (call with no arguments to see them); `manufacturer` is a vendor
id. Each listing row returns `url` (the primary OEM catalogue link) and `source_urls` (all original
datasheets cited by its specifications); product search hits carry the same fields. `get_product`
returns every parameter with `metric`, `value`/`low`/`high`, `unit`, the exact printed `basis`, and
`source_url` — the original OEM catalogue/datasheet page that figure came from. The record's
`description` ends with `Primary source: <url>`. Quote that URL and the basis together, and open the
URL to re-check before reuse; a parameter without `source_url` is unsourced and should be reported
as a gap, not guessed. Values printed in two variants (e.g. 50 Hz and 60 Hz, or
conflicting sources) are recorded as separate specs, not reconciled. Unknowns are gaps, never
estimates.

**`list_drawings(diagram_type=None, sector=None, query=None)`** / **`get_drawing(drawing_id)`**
Citable PFDs, P&IDs, schematics and flowsheets. Each record says what the diagram shows, who
published it, where it lives, which equipment and technology cards it covers, and the reuse terms.
The diagram itself is not copied into the repository — open the URL and respect its licence.

### Engineering materials

**`list_materials(material_category=None, query=None)`** / **`get_material(material_id)`**
Engineering materials with the properties printed on a source the author read — concrete, steel, bolts,
coatings, fenders, anodes and more. Each figure carries a `basis` and source URL; `material_category`
groups them (call with no arguments to see the categories), `query` is text.

### Register and gaps

**`list_technology_register(code=None, maturity=None, query=None)`**
The indicative register (~400 entries, all sectors). Entries with a `card` id are verified; the rest
are topics awaiting a card. Maturity and examples here are indicative, not verified. Rows carry
their `id`, which `get_register_entry(id)` takes.

**`get_register_entry(entry_id)`**
One register entry by its id (`code/slug-of-name`, e.g. `CCS/amine-solvent-post-combustion-capture`).

**`list_gaps(sector=None, field=None, reason_code=None, include_no_card=False, limit=100)`**
What the library knows it does not know: `field` (trl, performance, costs, reference_plants,
suppliers, status, process, other), `reason_code` (not_in_sources_read, source_unreachable,
source_not_collected, paid_source, status_unchecked, conflicting_sources, general_knowledge_only),
plus `item`, `reason`, `where`, `action`. Use it to answer "can you tell me X?" honestly and to pick
the next thing worth researching. The full set is several hundred rows — mostly one per card with
near-identical text — so narrow with `sector`/`field`/`reason_code`; `limit` (default 100, cap 1000)
is a backstop, not a browsing parameter. `/gaps` on the web UI reads the dataset directly and is not
capped.

### Reference

**`list_glossary(query=None)` / `get_glossary_term(term)`**
Terms and abbreviations with expansion and note — resolve PUE, WUE, SMR, DLE, HRSG, SRU
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
| `get_source` / `get_document` | `GET /api/sources/{id}` · `GET /api/documents?path=&offset=&limit=` (no `path` → the index) |
| `compare_technologies` / `get_technology` | `GET /api/technologies?...` · `GET /api/technologies/{id}` |
| `find_figures` | `GET /api/figures?kind=&sector=&technology_id=&q=&unit=&limit=` |
| `list_vendors` / `get_vendor` | `GET /api/vendors?...` · `GET /api/vendors/{id}` |
| `list_equipment` / `get_equipment` | `GET /api/equipment?...` · `GET /api/equipment/{id}` |
| `list_projects` / `get_project` | `GET /api/projects?status=&sector=&country=&q=` · `GET /api/projects/{id}` |
| `list_products` / `get_product` | `GET /api/products?product_type=&manufacturer=&q=` · `GET /api/products/{id}` |
| `list_drawings` / `get_drawing` | `GET /api/drawings?diagram_type=&sector=&q=` · `GET /api/drawings/{id}` |
| `list_materials` / `get_material` | `GET /api/materials?material_category=&q=` · `GET /api/materials/{id}` |
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
