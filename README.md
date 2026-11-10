# HILIR Technology Library

A curated catalog of public sources on oil, gas, petrochemical and energy technologies, built so AI agents can find, cite and read them.

It holds **407 catalog sources** across 8 sectors and 6 engineering disciplines, weighted toward Asia Pacific and Southeast Asia; a licence-tagged corpus of **287 collected documents**; **334 technology cards** covering the 341-entry technology register; a **vendor directory of 457 records**; and an **equipment catalog of 8 equipment classes** (five boiler classes plus centrifugal compressor, centrifugal pump and industrial gas turbine). A search index, a Postgres layer, an MCP server, a REST API and a web interface expose all of it to agents and people.

## Documentation

| Read | For |
| --- | --- |
| [AGENTS.md](AGENTS.md) | **Start here.** Rules and pointers for any AI agent or person working on the repo (agent-agnostic: Claude, Codex, Gemini, Copilot, Cursor, or a human) |
| [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md) | Picking up development: environment, gates, publish pipeline, verification, where each kind of change goes |
| [docs/AUTH.md](docs/AUTH.md) | **Auth is load-bearing.** The hilir Access model, where the code lives, what never to reintroduce |
| [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | Using the library: files, MCP server, REST, web UI, licence handling |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | How the parts fit together |
| [docs/MAINTAINER_MANUAL.md](docs/MAINTAINER_MANUAL.md) | Adding sources, verifying terms, collecting, refreshing |
| [docs/HOSTING.md](docs/HOSTING.md) | Topology, publishing, and the post-deploy verification (current-state section at the top) |
| [docs/STATUS.md](docs/STATUS.md) | Current numbers, open items and the session log |
| [CHANGELOG.md](CHANGELOG.md) | What shipped in each release |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Owner decisions and the rules they set |
| [docs/POSTGRES.md](docs/POSTGRES.md) | The Postgres/Neon layer: vectors, knowledge graph, read-only access |
| [docs/DATAVERSE.md](docs/DATAVERSE.md) | Exporting to Power Platform tables |

## Layout

| Path | What it holds |
| --- | --- |
| `taxonomy.yaml` | Sector codes (UPS, MID, GAS, REF, PCH, PWR, H2, CCS), discipline codes (PRC, ROT, INS, MAT, HSE, DIG), sub-topics and regions |
| `schema/` | JSON Schemas for sources, technology cards, vendors and equipment classes |
| `catalog/sources/<id>.json` | One record per source; this is the source of truth |
| `catalog/catalog.jsonl` | Generated: all records, one per line, for loaders and embedding pipelines |
| `catalog/index/<CODE>.md` | Generated: one page per code, Asia Pacific and Southeast Asia sources listed first |
| `catalog/technologies/` | One JSON card per technology option |
| `catalog/technology-register.yaml` | The ~300-technology register the cards cover |
| `catalog/vendors/` | One record per vendor, supplier, EPC or packager |
| `catalog/equipment/` | One record per equipment class (specification ranges with sources, vendor model lines) |
| `corpus/` | Collected content, as Markdown files with licence and provenance front matter |
| `collectors/` | Licence-aware collectors (see `collectors/README.md`) |
| `agent/` | Search index, MCP server, REST API and web interface (see `agent/README.md`) |
| `db/` | Postgres schema (`schema.sql`), admin layer (`library.sql`) and the read-only role (`readonly.sql`) |
| `deploy/edge/` · `deploy/frontend/` · `deploy/backend/` | The three Workers: sign-in/edge, UI, and the API/MCP door |
| `deploy/docker/` | The two container images (UI and API) built by CI and run on the VPS |
| `deploy/cloudflare/` | **Retired** pre-split single Worker, kept for rollback only (see docs/HOSTING.md) |
| `tools/check_links.py` | Checks every catalog url and writes `catalog/index/link-check.md` |
| `tools/build.py` | Validates every record and regenerates the generated files |
| `tools/load_postgres.py` | Reloads the Neon Postgres layer from the same files |
| `tools/seed/*.psv`, `tools/seed_to_json.py` | The one-time seed lists the records were created from |

## Reuse levels

Each record's `reuse_level` decides what the collector may store. Collectors act only on records marked `verification: verified`.

Since decision #29, `licence` and `reuse_level` are recorded labels: they describe what the terms say and gate only the corpus pipeline (collectors), not what agents may fetch or keep. Agent acquisition is unrestricted, and the owner decides inclusion in reports, corpus and exports manually.

| Level | Meaning | Where content may go |
| --- | --- | --- |
| `full-text-open` | Open licence (CC BY, public domain, OGL, NLOD and similar) | Corpus, with attribution |
| `full-text-restricted` | Downloadable with no open licence, where the terms allow personal or internal copies or publish no terms at all | This private repo only; each file carries a use note (personal reference, no redistribution or commercial use) |
| `summary-only` | Terms forbid copying, or the value is in facts rather than text | Our own summaries and extracted facts, with a link |
| `catalog-only` | Paywalled, login-only, or not downloadable | Catalog record only, kept for retrieval once a licence or API key is available |

Paid sources (API, ASTM, OnePetro full text, ICIS and others) are recorded `catalog-only` with `access: paywalled` — they are unreachable without credentials, and whether to buy them is the owner's call.

## Verification

Each record's licence and reuse level is checked against the live terms page, and the evidence URL and finding are logged in `tools/verification/log.jsonl`. `python tools/apply_verification.py` writes them into the records. Verified records also carry:

- `automated_access`: `allowed`, `prohibited` (manual download only) or `unstated`
- `permitted_use`: `any`, `internal-organisation`, `personal-non-commercial`, `none` or `unstated` (no terms published)

Terms findings are recorded as labels — e.g. terms-forbid-copying sites carry `summary-only`, and Honeywell and Caterpillar carry `catalog-only` because their terms ban AI use. Under decision #29 these labels inform the owner's manual review; they do not stop agents from fetching publicly reachable pages. Records still `unverified` either have not been checked or their terms page could not be read automatically (the log says which).

## Using it from an agent

- Simplest: load `catalog/catalog.jsonl` and filter by `sectors`, `disciplines`, `regions` or `reuse_level`.
- For browsing or a Claude Project: attach `catalog/index/*.md`.
- Search and retrieval: run the MCP server in `agent/` — **16 tools** for search and reading, technology cards, vendors, equipment classes, gaps, library stats, and (`sql_query`, `db_catalog`, `graph_neighbors`) a read-only SQL window and knowledge graph over the Postgres layer — optionally with embeddings for semantic search.
- Cloud agents and browsers: **two doors behind hilir Access**.
  - MCP + REST: `https://techlib-api.hilir.app` (`POST /mcp`, `/api/*`, OpenAPI at `/api/openapi.json`).
  - Web UI: `https://techlib.hilir.app` (browser sign-in at `https://access.hilir.app`).
  - A machine sends either an Access **access token** (`Authorization: Bearer`, `aud` = a registered resource origin such as `https://techlib-api.hilir.app`) or a person's **estate key** in `Authorization: Bearer` or `x-api-key`; both are verified at the Worker and again in the container. There is no library API key any more (Phase 4, 2026-11-05; estate migration 2026-11-06). See [docs/AUTH.md](docs/AUTH.md).
- Always cite `url`. `licence` and `reuse_level` are recorded labels the owner weighs when deciding what to include.

## Adding or changing a source

1. Add or edit `catalog/sources/<id>.json` (the id must match the file name).
2. Run `pip install -r requirements.txt` once, then `python tools/build.py`.
3. Commit the record together with the regenerated files. CI runs the same check on every push.

## Roadmap

1. **Catalog (done):** taxonomy, schema, 400 records, generated indexes.
2. **Verification and corpus (ongoing):** records verified against live terms; collectors in `collectors/` (RSS, arXiv, OSTI, manual inbox) write licence-tagged Markdown into `corpus/<id>/`. See `collectors/README.md`.
3. **Agent access (done):** SQLite FTS5 keyword index with optional embeddings, an MCP server with 16 tools, a REST API and an HTML interface, hosted at techlib.hilir.app / techlib-api.hilir.app behind hilir Access (open-licence text only).
4. **Postgres layer (done):** pgvector, full-text search and a knowledge graph on Neon, reloaded from the files by `tools/load_postgres.py` and queried read-only by agents (`sql_query`) and the web console as role `og_mcp_read`. See [docs/POSTGRES.md](docs/POSTGRES.md).
5. **Vendors and equipment (in progress):** 421 vendor records and 8 equipment classes; the next families (compressors, turbines, pumps beyond the first of each, then exchangers) arrive on the owner's word (decision #33).
