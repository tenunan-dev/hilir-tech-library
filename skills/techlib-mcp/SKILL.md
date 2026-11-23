---
name: techlib-mcp
description: Search and read the HILIR Technology Library through its MCP server (techlib-api.hilir.app) — 24 tools over a curated catalogue of public sources on oil, gas, petrochemical and energy technology, holding technology cards, cost and performance figures with their basis, vendor and equipment records, plants and projects, collected source documents, standards and a glossary. Use it when the user asks what technology options exist for X and how mature they are, what X costs or how efficient it is, who supplies X, what an equipment class can do, which plants use X, what a standard or acronym means, or for citable sources on an energy topic. Do NOT use it for drawing generation (JELAS CAD / hilir-cad), process simulation (DWSIM / dwsim-mcp), electrical studies (Thunderbolt / hilir-thunderbolt), Malaysian site facts (mygis-mcp) or man-hour and cost norms (resources-mcp).
---

# HILIR Technology Library — over MCP

`techlib-api.hilir.app` serves the Technology Library over MCP: 24 tools (Streamable
HTTP, stateless; `tools/list` is the live count) and the same functions as a REST API
under `/api`. The library is a curated catalogue of public sources on oil, gas,
petrochemical and energy technologies, built for AI agents to find, cite and read —
catalog sources, collected corpus documents, technology cards, vendors, equipment
classes and named plants/projects. Layer counts change with every publish;
`library_stats()` is the live number, never one quoted from memory.

## Connect

| Door | How |
|---|---|
| Hosted MCP | `POST https://techlib-api.hilir.app/mcp` (Streamable HTTP, stateless). Auth: a hilir Access access token (`Authorization: Bearer …`, `aud` = a registered origin) or a person's estate key (`Authorization: Bearer` / `x-api-key`). By default the hosted endpoint does not serve text from full-text-restricted sources. |
| Local stdio | any MCP client: `claude mcp add -s user hilir-tech-library -- "<repo>/.venv/bin/python" "<repo>/agent/server.py"`. The server builds `build/library.db` on first start; rebuild it after pulling (`python agent/library.py build`). |
| REST | same functions under `/api/*`; OpenAPI at `GET /api/openapi.json` |

Repo (public): `github.com/tenunan-dev/hilir-tech-library`. Authoritative deep reference:
`docs/MCP.md` there — full tool reference, REST mirror table, three worked answers,
troubleshooting. Also: `docs/USER_GUIDE.md` (client setup), `docs/AUTH.md` (auth),
`docs/POSTGRES.md` (the Postgres layer behind `sql_query`).

## Route the question

| The question | Start with | Then |
|---|---|---|
| Options and maturity for X | `compare_technologies(sector=…, application=…)` | `get_technology` on 2–4 ids |
| What X costs / how efficient X is | `find_figures(query=…, sector=…)` | `get_technology` for the whole card |
| Who supplies X / what does vendor Y make | `list_vendors(sector=…, query=…)` | `get_vendor` |
| Limits of an equipment class | `list_equipment(equipment_type=…)` | `get_equipment` |
| Which plants use X / what is built in Z | `list_projects(sector=…, country=…, query=…)` | `get_project` |
| What does this acronym mean | `get_glossary_term("CCGT")` | `list_glossary(q)` to browse |
| Which code/standard applies | `list_standards(org="API")` | `get_standard("API 610")` |
| Sources or text about X | `search(q, kind=…)` | `get_source` / `list_documents` / `get_document` |
| What the library does not know | `list_gaps(…)` | `list_technology_register` for card-less topics |
| How are these connected | `graph_neighbors(node=…)` | `sql_query` for custom joins (read `db_catalog()` first) |
| Counts, freshness, provenance | `library_stats()` | `sql_query` against the Postgres layer |

**Before any filter, call `taxonomy()`.** Sector codes are UPS, MID, GAS, REF, PCH, PWR,
H2, CCS, IDC, WWT; discipline codes are PRC, ROT, ELE, CIV, INS, MAT, HSE, DIG; regions
include `sea`, `apac`, `global`. Every filter is exact-match: a mistyped code returns an
empty page that reads like "no data" and is not.

## The four rules that override everything else

1. **Cite the url.** Every source, card, vendor, project and figure carries `url` /
   `source_url` / `source.url`. An answer without a url is not using this library — it is
   guessing near it.
2. **Respect `reuse_level`.** `full-text-open` may be quoted; `full-text-restricted` is a
   private reference copy — paraphrase, never reproduce or redistribute; `summary-only` and
   `catalog-only` have no stored text, so cite the source and describe its coverage.
3. **A figure without its basis is not usable.** `find_figures` returns `basis` for a
   reason (installed vs overnight vs LCOE, per kW vs per kWh, feed conditions) — carry the
   basis and the dollar year into the answer.
4. **Recorded gaps are admissions, not homework.** Do not fill a gap with an estimate and
   present it as the library's answer; name the gap (field, reason, where the next look
   goes) instead.

## Working habits that keep answers honest

- `search` *finds*; the `get_*`/`list_*` tools *read*. Search rows carry licence and
  `reuse_level` — check them before quoting.
- `search` ranks by **concept coverage, not literal wording**: the query is expanded through
  the library's concept groups (carbon = carbon + co2) and a record covering more of your
  query's concepts outranks one that repeats a word. Ask with the concepts you want answered —
  `carbon capture amine` ranks the amine post-combustion card first although that card is
  written in CO2 — and keep the query short: every extra word is a concept the record must
  also cover.
- An empty `find_figures` result means the cards hold no figure for that question. Answer
  with `list_gaps(field="costs"|"performance")`, not an estimate. An unknown `kind` raises
  on purpose: a silent fallback would hide the typo.
- Unknown ids return empty or null, not an error. An empty page can be a typo or real
  absence — confirm absence through `list_technology_register` (topics with no card yet)
  and `list_gaps` before saying "not in the library".
- `get_document` pages in characters (`offset`/`limit`, default 20,000, hard cap 100,000):
  check `total_chars` first; the corpus holds documents over 2M characters. Documents with
  `text_included: false` serve metadata only — their stored text is never published.
- Vendor ownership lives in `notes` and `aliases`: a brand named on a card may resolve to
  a parent record (acquisitions are common). `get_vendor` on the parent before concluding
  a brand is missing.
- `list_projects(country=…)` canonicalises mixed spellings ("US", "USA", "United States"
  all match). `compare_technologies(technology_ids=[…])` bypasses the filters and compares
  named cards side by side in the order given.
- `library_stats()` answers "how fresh is this". If results disagree with the website:
  both read the same database — check `GET /api/version` for drift.
- `sql_query` runs ONE read-only `SELECT`/`WITH` statement (no semicolon, 15 s timeout,
  500-row cap) against Postgres schema `og`. Read `db_catalog()` first for the tables,
  views and the `hybrid_search`/`graph_neighbors` functions.

Worked chain — "what would it cost to capture CO₂ from a cement plant?":
`compare_technologies(sector="CCS", application="cement")` → `get_technology` on the
relevant cards → `find_figures(technology_id="ccs-amine-post-combustion", kind="cost")` →
answer with the figure **and** its basis and dollar year → `list_gaps(sector="CCS",
field="costs")` to state what the card admits it lacks.
