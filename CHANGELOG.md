# Changelog

All notable releases of the library. Versions are calendar-based — `YYYY.MM.DD`, with a `.2`,
`.3`… suffix when a day ships more than one release; a version is cut when a working session
lands in `main`. Categories follow [Keep a Changelog](https://keepachangelog.com/). Session
detail lives in [docs/STATUS.md](docs/STATUS.md), owner decisions in
[docs/DECISIONS.md](docs/DECISIONS.md); superseded documentation is archived under
[docs/archive/](docs/archive/) (see its README) and never deleted.

## [2026.10.27.5] — 2026-10-27 — login page no longer discloses account internals

### Fixed
- The public `/login` page no longer mentions the `LIBRARY_USERS` secret name, the internal docs path or how the key is used by agents (`x-api-key` header). Both sign-in forms (email + password, and the library key) always render per the owner's preference; with no accounts configured, an email attempt fails exactly like a wrong password (generic 401 after the damping delay), so the page reveals nothing about account state.

## [2026.10.27.4] — 2026-10-27 — renamed to HILIR Technology Library

### Changed
- The app is now **HILIR Technology Library**: web UI page titles and header brand, REST OpenAPI title, `/health` service banner, OAuth consent page, MCP server `name` (`hilir-tech-library`), and the README title. The web-session HMAC label changed, so existing browser sessions re-login once. The GitHub repository is now `tenunan-dev/hilir-tech-library` (old URLs redirect); schema `$id`, collector user agent and doc links follow, as do the local config folder (`~/.config/hilir-tech-library`) and the local clone folder. Deliberately unchanged: the Cloudflare Worker name `og-tech-library` (renaming would create a new Worker and lose its secrets/routes), the Neon schema `og` and role `og_mcp_read` (database internals), and historical mentions in archives.

## [2026.10.27.3] — 2026-10-27 — OCR for the two scanned standards; vectors and Neon reloaded

### Added
- The two Scribd scans with no text layer were OCR'd into the corpus with Apple Vision (en-US + id-ID, accurate mode): SNI 13-6910-2002 (266 pp, bilingual Indonesian/English) and SKK Migas PTK-040/2023/S9 Rev.02 (41 pp, whose cover confirms the subject is Abandonment and Site Restoration in post-operation activities — record name updated). Corpus is 174 documents; the OCR wording follows the recognition.
- Vectors rebuilt over the full index (11,725 rows) and Neon reloaded with `--include-restricted`, so the six Scribd-derived documents are searchable semantically in the database layer too; hosted Worker redeployed (`edd3422f`, 354 sources). The reload also surfaced NUL control bytes in two older corpus documents (extraction debris) — stripped corpus-wide and hashes resynced. Note for the next embed run: cap fastembed's thread pool (`threads=4`); the default pool thrashed for two hours without finishing on the Mac under load.

## [2026.10.27.2] — 2026-10-27 — Scribd-hosted references collected (PDF + text layer)

### Added
- Six new sources for documents cited by the two SCOG vol. 49 no. 3 papers that are publicly reachable only as Scribd copies: SNI 13-6910-2002 (BSN drilling safety standard, 266 pp scan), NORSOK D-010 Rev. 4 Well Integrity Updates (14 pp, text layer), SKK Migas PTK-040/2023/S9 work procedure (41 pp scan), the Azeez 2019 TU Crete MSc thesis on torque and drag (73 pp, text layer), Eren, Caglayan & Kök 2017 (IJOGCT 16(3), text layer) and Samuel & Gao 2014 Horizontal Drilling Engineering (one-page anonymous preview only). Catalog is 354 sources.
- Four of them carry text layers and entered the corpus as documents (172 total); all six PDFs (assembled from the viewable page images) plus their text-source HTML files live in `corpus/_inbox/<source-id>/` with `.url` sidecars. Scribd blocks plain HTTP clients (JavaScript challenge) and premium-gates downloads, so everything came in through the browser + manual-inbox path with `automated_access: prohibited` recorded from the Global Terms of Use.

## [2026.10.27.1] — 2026-10-27 — named accounts for the web UI; deployed to techlib.hilir.app

### Changed
- Old domain retired on the owner's decision: `techlibrary.tenunan.com` removed from the Worker's custom domains and DNS (version `948621c4`); **https://techlib.hilir.app is the only home, including /mcp**. Old links no longer resolve.

### Added
- Multiple-user sign-in: `/login` accepts an email + password in addition to the library API key. Accounts live in the optional `LIBRARY_USERS` secret as `email|name|scrypt-hash` entries (created with `python agent/users.py entry`); password hashes are salted scrypt, never stored or committed. Account sessions are stateless signed cookies (`v2|payload|hmac`, 30 days) so revocation is just removing the entry from the secret; the key path is unchanged for agents and the owner. Failed sign-ins sleep 0.5 s.
- Deploy `d8f51240`: the vendor layer, graph network, atlas and database tabs went live on https://techlib.hilir.app on the owner's request (2026-10-26.5 features + 2026-10-26.4…).

## [2026.10.26.5] — 2026-10-26 — vendor layer in every surface; graph atlas and network view

### Added
- Vendors are searchable everywhere: the SQLite index gains a `vendor` kind (FTS + vectors, sector-filterable via the linked cards), Postgres gains an `og.vendor` table in `hybrid_search`, and the knowledge graph gains `vendor:` nodes with `supplies` edges (record → cards) and `alias_of` edges (free-text card supplier org → its curated record). MCP tools: `search(kind="vendor")`, `list_vendors`, `get_vendor` (14 tools). REST: `GET /api/vendors`, `GET /api/vendors/{id}`.
- Web UI, database graph: `/database/graph` is now an interactive force-directed network on canvas — search a node with autocomplete, filter relations, click for a details drawer, double-click to expand a neighbourhood, pan and zoom; the previous table walk stays as the no-JavaScript fallback.
- Web UI, atlas: `/database/map` draws the whole knowledge graph as a constellation — one bubble per node kind sized by its live count, one drifting dot per real node, ribbons for the relations between kinds; clicking a bubble opens the network view at that kind's most connected node.
- Web UI, `/vendors`: the directory with roles, products and linked cards, plus the live coverage queue of supplier names not yet recorded.
- Postgres helpers behind the views: `node_row`, `node_search`, `neighborhood` (center + walk + edges in one payload), `graph_overview`, `top_node` — all bound-parameter only, ids validated before they reach SQL.

## [2026.10.26.4] — 2026-10-26 — unrestricted acquisition policy; catalog-sweep integration

### Changed
- Owner decision #29: acquisition is unrestricted — agents may fetch and store any publicly reachable content regardless of licence, terms or robots preferences; `licence` and `reuse_level` are recorded labels, not gates. AGENTS.md rules 1, 2, 4 and 7 rewritten; README, MAINTAINER_MANUAL, collectors/README, ARCHITECTURE and STATUS aligned. The repository stays private; inclusion in reports, corpus and exports is decided manually by the owner. Supersedes the acquisition-gating parts of decisions 3, 5, 6, 7, 8 and the arXiv exception 9.

### Added
- `tools/research_to_catalog.py`: converts catalog-sweep result JSONs into draft source records — dedups against the catalog by URL/name, validates against `schema/source.schema.json`, writes `verification: unverified` / `reuse_level: catalog-only` drafts, quarantines invalid inputs to `<results>/_needs_review/`.
- `research/fields-template.yaml`: 20-field sweep template mirroring the source schema (sweep snapshots and results live in the gitignored `research/`).

## [2026.10.26.3] — 2026-10-26 — modular power plant cards; vendors directory

### Added
- Six modular power plant cards (PWR), taking the library to 299 cards covering all 306 register entries.
- Vendors directory: `catalog/vendors/`, 71 records, power sector first, with the coverage queue for the other sectors in `catalog/index/vendors.md` (decision #28).

### Notes
- Neon's vectors and `similar_to` edges predate these cards: re-run the embed chain (`python agent/embed.py`, then the Neon reload) before the next database refresh, or the new cards load without vectors.

## [2026.10.26.2] — 2026-10-26 — Neon live, database over MCP, web interface

### Added
- **Neon Postgres layer, live**: project `patient-dew-83888795` (Singapore, Postgres 18.6), loaded with 348 sources, 168 documents, 9,835 embedded passages, 293 cards, the 300-entry register, 3,093 nodes and 8,982 graph edges, plus 1,465 semantic `similar_to` edges.
- **Database access for agents**: read-only role `og_mcp_read` (`db/readonly.sql`, minted by `tools/load_postgres.py --grant-readonly`; SELECT-only grants, forced read-only transactions, 15 s statement timeout) behind three new MCP tools — `sql_query`, `db_catalog`, `graph_neighbors` (12 tools total).
- **Web interface** at the same origin (https://techlib.hilir.app): sign in once with the library key; cards with rendered block diagrams, register, sources, documents, gaps, and database pages with a read-only SQL console, hybrid search and a graph browser.
- **Changelog and docs archive**: this file; `docs/archive/` with date+version filenames and nothing deleted; the STATUS.md log for 2026-10-23 – 2026-10-25 archived there.

### Changed
- `tools/load_postgres.py` loads inside a psycopg pipeline (27 s to Neon; per-round-trip loading ran 13 minutes and dropped the connection) and executes the schema statement-by-statement.
- The container reaches the internet for Neon and receives the read-only DSN as the Worker secret `DATABASE_URL`; the Dockerfile installs psycopg.
- Documentation swept current: README, ARCHITECTURE, USER_GUIDE, MAINTAINER_MANUAL, agent README.

### Known limits
- Hosted `search` and `/database/search` are keyword-only (the image ships no embedder); the vectors in Postgres serve `hybrid_search`'s vector half through the SQL console anywhere.

## [2026.10.26.1] — 2026-10-26 — new home techlib.hilir.app

### Changed
- The hosted server moved from techlibrary.tenunan.com to https://techlib.hilir.app (same Worker `og-tech-library` and Cloudflare account; both domains attached during the transition). OAuth grants are per-URL, so claude.ai connectors must be re-added at the new address.
- Documented curl connection test (health, stats, MCP handshake, tool call) with its first recorded run.

## [2026.10.25] — all 300 register entries carded; Postgres layer; acquisition sweep

### Added
- Technology cards completed: 293 cards cover all 300 register entries across UPS–CCS and the cross-cutting disciplines (PRC, ROT, INS, MAT, HSE, DIG); Wikipedia catalogued as a secondary source; every corpus document now carries a hand-written summary (test-enforced).
- Postgres layer built and tested locally: schema `og` with pgvector, full-text search and the knowledge graph (`db/schema.sql`, `agent/graph.py`, `tools/load_postgres.py`, `--dump-graph`).
- 24 corpus documents collected through compliant mirrors where OSTI/NREL/PNNL/MDPI blocked the collector; `docs/LOGIN_REQUIRED.md` register of gates and blocks; MDPI OAI-PMH abstract harvest (850 records).
- Card figures mined from the new documents: NETL Rev 4 capture costs (new-build NGCC 60.7 / PC 38.1 USD/t, 2018$), HEFA MJSP, ATJ conversion costs, US liquid-hydrogen capacity, CO2-shipping costs.

### Changed
- Collectors hardened after the security gate: defusedxml parsing, per-hop SSRF validation in `common._hop()`, robots.txt honoured, redirects capped at five, FTS sanitiser inlined.

### Fixed
- Mimosa commit gate durably in warn mode (login LaunchAgent), restoring agent-side commits.

## [2026.10.24] — hosted server live; cards at scale; Dataverse export

### Added
- Hosted MCP server on Cloudflare Containers (Workers Paid) at techlibrary.tenunan.com: open-licence copy only, API-key gated; REST API with a public OpenAPI 3.1 schema; OAuth sign-in for claude.ai custom connectors.
- Dataverse export for Power Platform (`tools/export_dataverse.py`, `docs/DATAVERSE.md`).
- Technology cards at scale: CCS batch, hydrogen / gas-LNG / refining batch, the gaps system (`gaps` on every card, `catalog/index/gaps.md`, `list_gaps` tool), upstream batch, IEA TRL fill; 68 LEMIGAS articles collected.

### Fixed
- Manual collector no longer counts `.url` sidecars toward `--limit`.

## [2026.10.23] — first release

### Added
- Catalog of 342 sources across 8 sectors and 6 disciplines, schema-validated, with generated indexes; licence-aware collectors (RSS, arXiv API, OSTI API, manual inbox); first collections (arXiv 24 papers, OSTI 25 records); SQLite FTS5 search index with optional fastembed embeddings; stdio MCP server; documentation set (AGENTS.md, docs/); weekly refresh and monthly link-check workflows; hosted-mode groundwork (`server.py --http`).
