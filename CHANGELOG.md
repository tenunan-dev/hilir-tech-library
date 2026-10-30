# Changelog

All notable releases of the library. Versions are calendar-based — `YYYY.MM.DD`, with a `.2`,
`.3`… suffix when a day ships more than one release; a version is cut when a working session
lands in `main`. Categories follow [Keep a Changelog](https://keepachangelog.com/). Session
detail lives in [docs/STATUS.md](docs/STATUS.md), owner decisions in
[docs/DECISIONS.md](docs/DECISIONS.md); superseded documentation is archived under
[docs/archive/](docs/archive/) (see its README) and never deleted.

## [2026.10.30.3] — 2026-10-30 — Handover refresh; Neon and search-mode status

### Changed
- docs/STATUS.md Handover rewritten to the current state (399 sources, 202 documents, 299 cards, 414 vendors, 830 gaps) with numbers checked against the repository; the Current numbers table updated to match.
- Neon status stated plainly: embeddings finished, last reload 2026-10-30 holds 12,577 vectors and 413 vendors (one behind the repo); hosted `search` and `/database/search` are keyword-only because the image ships no embedder.
- Decisions 14, 23 and 25 now name https://techlib.hilir.app instead of the retired techlibrary.tenunan.com.

## [2026.10.30.2] — 2026-10-30 — Coverage queue closes empty; queue behaviour change (decision #31)

### Added
- Vendor `qatargas` (QatarEnergy LNG; aliases Qatargas, RasGas) and Foster Wheeler/Amec aliases on `wood`. Vendors 413 → 414.

### Changed
- `tools/build.py` and `agent/web.py` coverage-queue logic (decision #31): '/'-compounds split and matched part by part; descriptive phrases moved to a "Card notes" section. The queue is empty — every named supplier on all 299 cards is in the directory. Short-form aliases added to blue-planet/carboncure/planetary (card-string mismatch class).
- Deploy `ea521ee2` live-verified (399 sources / 414 vendors; /vendors shows empty queue + notes).

## [2026.10.30.1] — 2026-10-30 — Vendor queue closure + categories refinement; catalog 399, vendors 413

### Added
- 23 vendor records closing the named-vendor coverage queue (incl. boiler OEMs Babcock & Wilcox, Cleaver-Brooks, Sumitomo SHI FW per owner request; fusion/CSP/floating-solar/utilities cluster; Alfa Laval, Koch-Glitsch); alias fixes for ihi/drax/yokogawa/worley/mitsubishi-power. Vendors 394 → 413; remaining queue = non-vendor placeholders only.
- 5 sources (METI Green Innovation Fund, MIT CCS Project Database, World Bank GFMR flaring partnership, EAGE, Petroleum Research journal). Catalog 394 → 399.

### Changed
- A4b: vendor `categories` refined by two serial flash batches — 200 of 413 records corrected.
- A6: 14 more source records verified (batches 1-2); EUBCE record corrected to free-registration (proceedings behind a free account at etaflorence.it/proceedings).
- A9: 10 event/standards candidates queued (SPE ATCE, WGC, ISO 19880/14687, ASME BPVC, SIRIM…); republish deploy 82aeca5c live-verified.

## [2026.10.29.8] — 2026-10-29 — Runbook execution: A2/A3/A4/A5/A6/A8/A11, catalog 394, vendors 394

### Added
- tools/discover_sources.py (+6 tests): channel-1 miner, 172 candidates queued; tools/categorise_vendors.py: rule-based categories backfill of all 390 vendor records; vendor schema gains optional `categories` enum (12 values) + presence test.
- 23 sources registered via A3 batches 1-3 (IADC, CISA ICS, Hydraulic Institute, FM Global, CanmetENERGY, CERI, EHB, Energy Intelligence, IEA Bioenergy, IEA PVPS, IMO/MARPOL, INL, NREL ATB, DOE H2 records/HDSAM, DOE Wind Market, EPA AP-42, Maritime Executive, Ship & Bunker, NFOGM, Plastics Recyclers EU, SG MPA, NERSA, GSQ Queensland); 8 vendors (fluor, wood, petrofac, worley, bechtel, mcdermott, cooec, cpecc) + Kanadevia Inova alias fix.
- A8 OpenAlex sweep: 8 high-frequency venues queued as candidates; A5 audit clean; A6 batch 1 verified 8 records (incl. aep-journal rename fix, aker-carbon-capture dead domain).

## [2026.10.29.7] — 2026-10-29 — Plan v3: rewritten as a precise agent runbook

### Changed
- docs/SOURCE_DISCOVERY_PLAN.md restructured into an operational runbook any zero-context agent can execute: entry protocol, driving-file shapes, standing rules with full schema/enum reference and documented traps, flash-max worker contract with prompt template, per-block procedures A2–A12 with exact commands, state-update and candidate-outcome protocols, parked owner-only list. Scope unchanged from v2.

## [2026.10.29.6] — 2026-10-29 — Source discovery plan v2: autonomous sequencing, 43 seeded candidates, categorization stream

### Changed
- docs/SOURCE_DISCOVERY_PLAN.md rewritten (owner direction): continuous multi-agent execution without owner intervention — blocks A1–A12 tracked in a committed sequencer (research/source-discovery/state.json), human-dependent items parked behind, temporary failures retried and re-sequenced after every block outcome.
- research/source-discovery/ (candidates.jsonl queue + state.json) now versioned (gitignore exception); inbox stays local.

### Added
- Block A1 done: 43 candidates mined from gap where-hints (34 sources incl. IADC, IMO, INL, EPA AP-42/GHGRP, World Bank GGFR, EAGE, Maritime Executive, Ship & Bunker; 8 vendors incl. BP, Hengli, Rongke retry, Kanadevia rename fix).
- Categorization work stream: vendor `categories` enum (A4), source_type audit (A5), verification sweep of 193 unverified records (A6); equipment index proposed, undecided.

## [2026.10.29.5] — 2026-10-29 — Korean and Japanese plant-EPC cohort; plan gains vendor-coverage section

### Added
- Nine contractor records: `samsung-engineering` (Samsung E&A — TA'ZIZ methanol, Jubail refinery package), `hyundai-ec` (Al-Zour, first Korean EPC US nuclear win), `sk-ecoplant` (ex-SK E&C), `daelim`, `gs-ec` (USD 7.2 bn Saudi gas-plant expansion with Samsung E&A), `kepco-ec` (APR1400 design/E&C), `doosan-enerbility` (turbines/HRSG/nuclear forgings), `jgc` (LNG-dominated EPC, PFLNG Satu, PNG LNG, JGC-Toyo fuel-ammonia alliance) and `toyo` (ammonia-plant EPC leader). `chiyoda` broadened from H2 licensor to full LNG/refinery EPC. Vendors 378 → 390.
- docs/SOURCE_DISCOVERY_PLAN.md: new "who can supply, build, construct and maintain" vendor-coverage section with the regional cohort log (CN done, KR/JP done) and next cohorts (Western EPC, NOC engineering arms).

## [2026.10.29.4] — 2026-10-29 — Chinese EPC/supplier coverage: Wison, Sinopec, Sinopec Engineering registered

### Added
- Vendor records `wison` (Wison Engineering + Wison New Energies — FLNG/FPSO EPCIC from the Nantong yard, Baleine Phase 3 FPSO EPCIC, Tango FLNG, Shell-licensed DMR FLNG collaboration), `sinopec` (operator/developer/supplier; Kuqa green hydrogen; licensor via source sinopec-tech) and `sinopec-engineering` (SEG, HKEX 2386 — epc/licensor; SATORP expansion and Kazakhstan butadiene EPC). Vendors 378 → 381.
- Closes the owner's check: the vendor layer already models who can supply/build/construct/maintain (roles + products + per-technology links in search, MCP, REST, web, Neon and the graph); the gap was Chinese-EPC coverage.

## [2026.10.29.3] — 2026-10-29 — iRecruit candidate resolved: source `irecruit` registered

### Added
- Source record `irecruit` (irecruit.co — US construction/AEC recruiting firm; its free 2026 reports — data-center cost per MW benchmarks, salary guides, nuclear/SMR and renewables construction — are tier-3 market context on PWR cards). Catalog now 371 records; all four owner-named candidates registered; candidates queue and plan table updated.

## [2026.10.29.2] — 2026-10-29 — Source discovery plan; EUBCE, Gas Turbine World, USP&E registered

### Added
- docs/SOURCE_DISCOVERY_PLAN.md (decision #30): the standing programme for finding sources the catalog does not know — five channels (corpus citation mining, OpenAlex/Crossref venue analysis, vendor provenance, event/standards sweeps, owner inbox) into one triage queue with access-class collection rules; Wave 0 scoped (discover_sources.py, vendor crawl, first EUBCE batch, first OpenAlex run).
- Source record `eubce` (conference, open-access proceedings via ETA-Florence, tier 1) and source record `gas-turbine-world` (Pequot handbook, paywalled, summary-only, manual extracts only). Catalog now 370 records.
- Vendor record `uspe-global` (frontier-markets power-station EPC/rental/operation; 378 vendors total).
- Owner inbox `research/source-discovery/inbox.local.txt` + candidate queue `candidates.jsonl` (gitignored working files).

### Changed
- docs/STATUS.md backlog now leads with source discovery as the main effort; docs/DECISIONS.md #30; AGENTS.md read-next table points at the plan.

## [2026.10.29.1] — 2026-10-29 — Wave 4 verified: 91 process gaps closed, register 905 → 830

### Changed
- Flash workers restored (agent model-account fix); four serial verification batches ran per-page article checks over the 111 Wave-4 kept leads, closing 91 general-knowledge process gaps whose attached Wikipedia authorities genuinely cover the card's process descriptions (each closed gap cites its article as a marked secondary source). 20 honest keeps with per-article scope shortfalls recorded.
- 28 arXiv full-text PDFs downloaded and converted to corpus-markdown drafts in corpus/_inbox/arxiv-fulltext/ (intake next session).

## [2026.10.27.14] — 2026-10-28 — vendor directory complete (378), Wave 4 executed, citation binding, terms-check pass

### Added
- Vendor directory completed across all 15 sectors (205 → 378 records); the coverage queue now lists only non-vendor category placeholders.
- Wave 4 executed in two passes: 132 verified open process-authority leads attached to general-knowledge gaps, then automated secondary-source cross-checks closed 18 (the 111 below threshold keep the lead and a verification action).
- 14 new catalog source records for the most frequently-cited uncatalogued URLs (catalog now 368 records).
- Automated terms-check pass over all 26 flagged sources (6 fetched with findings recorded, 20 confirmed needing browser sessions).

## [2026.10.27.13] — 2026-10-28 — vendor directory +71: UPS and H2 sectors fully covered

### Added
- 134 new vendor records (71 → 205): the entire UPS coverage queue (SLB, Halliburton, Weatherford, NOV, Nabors, SBM Offshore, MODEC, MISC, BiSN, Wellstrom, Exedra, Axter, Interwell, seismic contractors, NOCs and operators) and the entire H2 queue (electrolyser makers Nel/ITM/Enapter/John Cockerill/HydrogenPro/PERIC/LONGi/nucera, fuel cells Ballard/Bloom/Toyota, storage Hexagon Purus and HyStock, liquefaction Kawasaki, crackers Hazer/Monolith/BASF, DRI Midrex/HYBRIT/Stegra, e-fuels INERATEC/Infinium/Velocys, industrials Air Liquide/Air Products/Linde/Topsoe/Johnson Matthey/KBR/Casale/Yara). Aliases matched to every card supplier string; the coverage queue now lists only genuinely unrecorded names.

## [2026.10.27.12] — 2026-10-28 — Wave 3 complete: all 36 sector batches swept, 1,012 → 921 open gaps

### Changed
- All 15 sectors swept (CCS-2/3, H2 all four batches, ROT/MAT/INS/DIG/LNG/HSE/PRC included; 153 closures in the wave). Highlights: Carbfix injection below USD 25/t, MCi Myrtle ex-situ plant, UNDO basalt trials, Verdox 1 GJ/t electro-swing, Sleipner and Northern Lights storage references with costs, ammonia marine world-firsts (Singapore 2024), biogas-upgrading energy by route, Stegra Boden, natural-hydrogen cost estimates (IEAGHG), e-fuel cost ranges, STH efficiency records, PCHE design envelope, OSC/OSDU licence resolved (Apache-2.0), Sakhalin-2 DMR trains, PFLNG Satu, and OEM supplier entries across compressors, pumps, valves, heat exchangers, NDT, FRP, RBI, APC, DCS, OT security, analysers, SIS, IIoT, AI-maintenance and process simulation. Every kept gap now carries a dated clause recording what was searched.

## [2026.10.27.11] — 2026-10-28 — Wave 3 continues: 1,012 → 957 open gaps

### Changed
- Wave 3 sector sweeps extended: PCH, GAS and MID sectors complete plus CCS-1 (register 1,012 → 957). Highlights: Motunui methanol-to-gasoline (14,500 bpd, 1985), Pearl GTL conversion scale, helium supply by plant (USGS), Hammerfest all-electric LNG, NGV fleet numbers (DOE AFDC), Mont Belvieu NGL hub, Northern Lights four 7,500 m3 LCO2 carriers, HyDeploy 20% hydrogen blends, LNG newbuild price (~$248m, Clarksons 2025), Suiso Frontier first LH2 shipment, TAPS first drag-reducer use (1979), Porthos 55 km CO2 pipeline, Allam-cycle status resolved negative (no utility-scale plant; NET Power hub withdrawn), Exomad Green biochar, CarbonCure mineralisation figures.

## [2026.10.27.10] — 2026-10-28 — Wave 3 sector sweeps begun: 1,074 → 1,012 open gaps

### Changed
- Wave 3 of the gap-closure plan started: the whole UPS sector (six batches) and PWR batches 1–2 swept by web research, 62 gaps closed with dated sources (Asgard subsea compression, Clair Ridge LoSal, Johan Sverdrup electrification, nanofluid-EOR first field trial, HTR-PM, JERA Hekinan ammonia co-firing, Hywind Tampen, Hornsdale grid-forming, ±1,100 kV UHVDC, MEOR field costs, Dubai WTE, Noor CSP, CAES references, and more); about 90 kept gaps gained dated search-evidence clauses. Executed inline after the flash subagent provider became unavailable.

## [2026.10.27.9] — 2026-10-28 — gap-closure Waves 1–2 executed: 1,118 → 1,074 open gaps

### Changed
- 44 card gaps closed with quoted, corpus- or web-sourced figures: amine reboiler duty 2.4–2.7 GJ/t CO2 from the NETL Baseline stream tables, six operating BECCS plants from the Global CCS Institute 2026 status, UKCS P&A cost benchmarks (GBP 4.95m/well 2025) and named plug-technology suppliers, PEM stack lifetime settled at 40,000 h (newer DOE record resolves the conflicting-source gap), Kasawari CCS start-up conflict resolved (no injection yet; first injection targeted 2027), CCGT costs from AEO2026 (1,086 USD/kW single-shaft, 2025$), salt-cavern H2 storage costs (2.30 USD/kg levelized, 51m USD capex per cavern), CO2-EOR utilisation 0.3–0.6 t CO2/bbl, ATR-CCS reference plants and 2024 LCOH ranges from the IEA Global Hydrogen Review, TRL citations from the July 2026 ETP guide (depleted-field storage 8, CO2 compression/pipeline 9, CO2 shipping 7–8, instrumented air 9), LEMIGAS polymer-flood recovery figures, and eight dated status re-checks (Longlaville, Seville, Sukowati, Siluria OCM, Fram Sør, oxyfuel cement, PureCycle operating rate, e-cracking checked — nothing published). Kept gaps gained dated search-evidence clauses; the ETP guide's absence of upstream O&G rows and the abstract-only state of the arXiv and OSTI corpus files are recorded per gap.
- Fixed wrong data on ups-well-plug-abandonment: the H-11 cost entries carried the paper's 2066 projections (USD 505,737.59 / 1,170,558.11); corrected to its 2026 calculations (USD 179,276.30 SNI / USD 414,945.09 NORSOK).

## [2026.10.27.8] — 2026-10-28 — per-user API keys; account page

### Added
- Accounts get API keys: self-service at `/account` (create with a label — the raw `hlt_…` key is shown once, only its sha256 stored; revoke; last-used shown) and admin-wide management at `/admin` (mint for any account, revoke any). A key acts as its owning account — same role and rights, recorded in analytics — and works on the web UI, REST and MCP via `x-api-key`. Keys cascade-delete with the account; revocation is immediate.
- The edge worker passes `hlt_` keys through to the container (which resolves them against the account store) and injects the `USER_STORE_URL` DSN per request (`x-user-store-dsn`), so container instances predating a secret rotation still see the current DSN; a client cannot inject its own.

## [2026.10.27.7] — 2026-10-27 — admin view: roles, account management, login data and analytics

### Added
- Roles: `LIBRARY_USERS` entries take an optional trailing `|admin` (default `user`); the library key always has admin rights. `user` sessions get 403 on admin pages.
- `/admin`: account list with roles and source, account creation with a default password, account deletion (revoking sessions within the account-cache window), plus login data (who, when, success/failure, IP) and analytics (sign-ins and failed attempts over 7 days, views and searches per day, most-viewed pages). An Admin link appears in the nav for admins.
- Durable store for accounts created on the page and all activity events: Neon schema `library` (`db/library.sql`, deliberately outside the reload-truncated schema `og`), written through the least-privilege role `library_app` via the new `USER_STORE_URL` secret (provision or rotate with `python tools/provision_userstore.py`). Sessions are now only valid while the account still exists. Without the secret the library runs env-only: accounts come from the `LIBRARY_USERS` secret, the admin page says creation and analytics are unavailable, and no events are recorded.

## [2026.10.27.6] — 2026-10-27 — gap closure plan

### Added
- [docs/GAP_CLOSURE_PLAN.md](docs/GAP_CLOSURE_PLAN.md): the programme for closing the 1,118 open card gaps — a 13-method toolbox in escalation order (local corpus mining, semantic search, web fetch/search, blocked-host mirrors, alternate reader, search agent, Wayback, browser use, computer use, manual inbox, catalog binding, flash workers, publish ops), seven waves starting with offline mining of the already-collected 2026-10-25 documents, and the flash-worker task contract with build/pytest gates per batch.

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
