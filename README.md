# O&G technology source library

A curated catalog of public sources on oil, gas, petrochemical and energy technologies, built so AI agents can find, cite and (where the licence allows) read them.

It holds 348 catalog sources across 8 sectors and 6 engineering disciplines, weighted toward Asia Pacific and Southeast Asia; a licence-tagged corpus of 168 collected documents; 293 technology cards covering the 300-entry technology register; and a search index, a Postgres layer, an MCP server, a REST API and a web interface so agents and people can query all of it (see [Roadmap](#roadmap)).

## Documentation

| Read | For |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Start here: rules and pointers for any AI agent or person working on the repo |
| [docs/USER_GUIDE.md](docs/USER_GUIDE.md) | Using the library: files, MCP server, licence handling |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | How the parts fit together |
| [docs/MAINTAINER_MANUAL.md](docs/MAINTAINER_MANUAL.md) | Adding sources, verifying terms, collecting, refreshing |
| [docs/STATUS.md](docs/STATUS.md) | Current numbers and backlog |
| [CHANGELOG.md](CHANGELOG.md) | What shipped in each release |
| [docs/DECISIONS.md](docs/DECISIONS.md) | Owner decisions and the rules they set |
| [docs/HOSTING.md](docs/HOSTING.md) | The hosted server for cloud agents and browsers (techlib.hilir.app) |
| [docs/POSTGRES.md](docs/POSTGRES.md) | The Postgres/Neon layer: vectors, knowledge graph, read-only access |
| [docs/DATAVERSE.md](docs/DATAVERSE.md) | Exporting to Power Platform tables |

## Layout

| Path | What it holds |
| --- | --- |
| `taxonomy.yaml` | Sector codes (UPS, MID, GAS, REF, PCH, PWR, H2, CCS), discipline codes (PRC, ROT, INS, MAT, HSE, DIG), sub-topics and regions |
| `schema/source.schema.json` | JSON Schema every catalog record must pass |
| `catalog/sources/<id>.json` | One record per source; this is the source of truth |
| `catalog/catalog.jsonl` | Generated: all records, one per line, for loaders and embedding pipelines |
| `catalog/index/<CODE>.md` | Generated: one page per code, Asia Pacific and Southeast Asia sources listed first |
| `catalog/index/README.md` | Generated: counts by code, region, type, reuse level and verification |
| `catalog/technologies/` | One JSON card per technology option (schema `schema/technology.schema.json`) |
| `catalog/technology-register.yaml` | The ~300-technology register the cards cover |
| `corpus/` | Collected content, as Markdown files with licence and provenance front matter |
| `collectors/` | Licence-aware collectors (see `collectors/README.md`) |
| `agent/` | Search index, MCP server, REST API and web interface (see `agent/README.md`) |
| `db/` | Postgres schema (`schema.sql`) and the read-only role (`readonly.sql`) |
| `deploy/cloudflare/` | The hosted server: Cloudflare Worker and Container configuration |
| `tools/check_links.py` | Checks every catalog url and writes `catalog/index/link-check.md` |
| `tools/build.py` | Validates every record and regenerates the generated files |
| `tools/seed/*.psv`, `tools/seed_to_json.py` | The one-time seed lists the records were created from |

## Reuse levels

Each record's `reuse_level` decides what the collector may store. Collectors act only on records marked `verification: verified`.

| Level | Meaning | Where content may go |
| --- | --- | --- |
| `full-text-open` | Open licence (CC BY, public domain, OGL, NLOD and similar) | Corpus, with attribution |
| `full-text-restricted` | Downloadable with no open licence, where the terms allow personal or internal copies or publish no terms at all | This private repo only; each file carries a use note (personal reference, no redistribution or commercial use) |
| `summary-only` | Terms forbid copying, or the value is in facts rather than text | Our own summaries and extracted facts, with a link |
| `catalog-only` | Paywalled, login-only, or not downloadable | Catalog record only, kept for retrieval once a licence or API key is available |

Paid sources (API, ASTM, OnePetro full text, ICIS and others) are catalog-only until subscriptions or API keys are added.

## Verification

Each record's licence and reuse level is checked against the live terms page, and the evidence URL and finding are logged in `tools/verification/log.jsonl`. `python tools/apply_verification.py` writes them into the records. Verified records also carry:

- `automated_access`: `allowed`, `prohibited` (manual download only) or `unstated`
- `permitted_use`: `any`, `internal-organisation`, `personal-non-commercial`, `none` or `unstated` (no terms published)

Sites whose terms forbid copying are `summary-only`; Honeywell and Caterpillar, whose terms ban AI use, are `catalog-only`. Records still `unverified` either have not been checked or their terms page could not be read automatically (the log says which).

## Using it from an agent

- Simplest: load `catalog/catalog.jsonl` and filter by `sectors`, `disciplines`, `regions` or `reuse_level`.
- For browsing or a Claude Project: attach `catalog/index/*.md`.
- Search and retrieval: run the MCP server in `agent/` — 12 tools for search and reading, technology cards, gaps, and (`sql_query`, `db_catalog`, `graph_neighbors`) a read-only SQL window over the Postgres layer — optionally with embeddings for semantic search.
- Cloud agents and browsers: https://techlib.hilir.app serves the same tools at `/mcp` (API key header), a REST API under `/api`, and an HTML interface where you sign in with the key. See [docs/HOSTING.md](docs/HOSTING.md).
- Always cite `url` and respect `reuse_level` and `licence` when quoting.

## Adding or changing a source

1. Add or edit `catalog/sources/<id>.json` (the id must match the file name).
2. Run `pip install -r requirements.txt` once, then `python tools/build.py`.
3. Commit the record together with the regenerated files. CI runs the same check on every push.

## Roadmap

1. **Catalog (done):** taxonomy, schema, 348 records, generated indexes.
2. **Verification and corpus (ongoing):** records verified against live terms; collectors in `collectors/` (RSS, arXiv, OSTI, manual inbox) write licence-tagged Markdown into `corpus/<id>/`. See `collectors/README.md`.
3. **Agent access (done):** SQLite FTS5 keyword index with optional embeddings, an MCP server with 12 tools, a REST API and an HTML interface, hosted on Cloudflare at https://techlib.hilir.app (open-licence text only, behind an API key).
4. **Postgres layer (done):** pgvector, full-text search and a knowledge graph on Neon, reloaded from the files by `tools/load_postgres.py` and queried read-only by agents (`sql_query`) and the web console as role `og_mcp_read`. See [docs/POSTGRES.md](docs/POSTGRES.md).
