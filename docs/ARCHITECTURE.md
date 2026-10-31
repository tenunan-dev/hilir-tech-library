# Architecture

## Overview

```
 taxonomy.yaml ─┐
 schema/ ───────┤
                ▼
 catalog/sources/<id>.json ──tools/build.py──▶ catalog/catalog.jsonl, catalog/index/*.md
        ▲                                             │
        │ tools/apply_verification.py                 │ collectors/collect.py (verified records only)
 tools/verification/log.jsonl                         ▼
                                   corpus/<id>/*.md + corpus/manifest.jsonl
                                   corpus/_inbox/<id>/ (hand-downloaded files)
                                                      │
                                   agent/library.py build (+ agent/embed.py)
                                                      ▼
                                   build/library.db (SQLite: FTS5 + optional vectors)
                                                      │
                                   agent/server.py (MCP over stdio, or --http behind techlib.hilir.app)
                                      ├─ agent/api.py   REST API under /api
                                      ├─ agent/web.py   HTML interface (session cookie from the API key)
                                      └─ agent/pg.py ──▶ Neon Postgres, schema og (read-only role og_mcp_read)
                                                                     ▲
                                   tools/load_postgres.py ──────────┘ (full reload from the same files, owner DSN)
```

Everything is plain files in git except `build/`, which is rebuilt locally.

## Components

### Taxonomy (`taxonomy.yaml`)

Two tag axes plus regions. Every record has at least one sector and one discipline.

- Sectors: `UPS` upstream, `MID` midstream, `GAS` gas processing and LNG, `REF` refining, `PCH` petrochemicals, `PWR` power and renewables, `H2` hydrogen and low-carbon fuels, `CCS` CCUS.
- Disciplines: `PRC` process systems, `ROT` rotating and static equipment, `INS` instrumentation and control, `MAT` materials and integrity, `HSE` health, safety and environment, `DIG` digital.
- Regions: `global`, `apac`, `sea`, `me`, `eu`, `na`, `latam`, `af`. The library is weighted toward `apac` and `sea`.

### Catalog record (`schema/source.schema.json`)

| Field | Meaning |
| --- | --- |
| `id` | Kebab-case, equals the file name |
| `name`, `url`, `publisher_org`, `country` | Identity |
| `source_type` | standards-body, licensor, oem-supplier, epc-contractor, journal, agency-data, association, conference, patents, trade-media, research-institute |
| `sectors`, `disciplines`, `subtopics`, `regions` | Tags |
| `access` | open, free-registration, paywalled, mixed |
| `licence` | Free text or SPDX id (e.g. CC-BY-4.0, public-domain, proprietary) |
| `reuse_level` | What may be stored (see below) |
| `automated_access` | allowed, prohibited, unstated: whether crawlers are allowed |
| `permitted_use` | any, internal-organisation, personal-non-commercial, none, unstated |
| `feeds` | RSS/Atom URLs; a record with feeds is collected by the `rss` adapter |
| `quality_tier` | 1 (authoritative) to 3 |
| `verification`, `last_verified` | Whether a person or agent checked the live terms, and when |
| `notes` | Finding and `Evidence: <url>` after verification |

Reuse levels:

| Level | Stored |
| --- | --- |
| `full-text-open` | Full text, with attribution |
| `full-text-restricted` | Full text as a private reference copy, with a `use_note` |
| `summary-only` | Nothing collected; agents write their own summaries and link |
| `catalog-only` | Nothing; waits for a licence or API key |

These levels gate only the corpus pipeline above. Under decision #29, agent acquisition is
unrestricted and the owner decides inclusion manually; the labels describe what the terms say.

### Technology cards (`catalog/technologies/`, `schema/technology.schema.json`, `agent/technologies.py`)

One JSON card per technology option: sector, category, maturity (commercial, demonstration, pilot, lab), TRL with its source, principle, process steps (each with equipment and links to downstream steps), key equipment, performance and cost figures (each with unit, dollar year, basis and source), suppliers, reference plants, advantages, limitations and sources. Cards are our own words; figures are facts taken from cited sources. `tools/build.py` validates them and writes `catalog/technologies.jsonl` and `catalog/index/technologies-<SECTOR>.md`. `agent/technologies.py` turns process steps into a Mermaid block flow diagram and builds comparison rows. The search index includes cards as `kind = "technology"`.

### Technology register (`catalog/technology-register.yaml`)

About 300 technologies across all sectors and cross-cutting disciplines, one line each: name, indicative maturity, example licensors or vendors. It is the backlog for technology cards and is drafted from general knowledge, so it is not evidence. `tools/build.py` links entries to cards by name or alias and writes `catalog/index/technology-register.md`.

### Verification (`tools/verification/`)

`log.jsonl` is an append-only log of terms checks: `id`, `checked_on`, `evidence` (URL), `finding`, and any of `url`, `licence`, `reuse_level`, `access`, `update_frequency`, `automated_access`, `permitted_use`. `apply_verification.py` replays the whole log onto the records, so the log is the source of truth for verification state. An entry with `"verified": false` records a check that could not confirm the terms; such records appear in `catalog/index/needs-manual-check.md`.

### Build (`tools/build.py`)

Validates each record against the schema and checks id equals file name, then writes `catalog/catalog.jsonl`, one index page per code in `catalog/index/` (Asia Pacific first), `catalog/index/README.md` (counts) and `needs-manual-check.md`. CI fails if these generated files are out of date.

### Collectors (`collectors/`)

- `common.py`: polite HTTP (`fetch` checks robots.txt, waits 3 s per host, sends user agent `hilir-tech-library-collector/0.1`), HTML and PDF to Markdown (trafilatura, pypdf), and `write_document`, which writes front matter from the record and de-duplicates by SHA-256 through `corpus/manifest.jsonl`.
- `adapters.py`: `rss` (feed items to article pages), `arxiv` (Atom API, metadata and abstracts), `osti` (OSTI API, metadata and abstracts), `manual` (files in `corpus/_inbox/<id>/`). `adapter_for(rec)` picks a named adapter from `ADAPTERS`, else `rss` when the record has `feeds`.
- `collect.py`: CLI that runs adapters for collectable records.
- robots.txt handling: 401/403/5xx or unreachable means disallow all; 404 means allow all. `ROBOTS_EXCEPTIONS` lists URL prefixes allowed despite robots.txt, each with its terms page.

### Corpus file format

```
---
source_id: "arxiv"
title: "..."
url: "http://arxiv.org/abs/..."
published: "..."
retrieved_at: "2026-10-23T14:18:07+00:00"
licence: "..."
reuse_level: "full-text-restricted"
permitted_use: "..."
sectors: [...]
disciplines: [...]
sha256: "..."
use_note: "Private reference copy. ..."    # restricted sources only
content: "metadata-and-abstract"            # adapter extras
---

# Title

Body in Markdown
```

Each front-matter value is JSON, so any language can parse it line by line.

### Search index (`agent/library.py`, `agent/embed.py`)

`build/library.db` (SQLite) holds `sources`, `docs`, an FTS5 table `search` (catalog records plus corpus chunks of about 1200 characters, with a `tags` column of codes, taxonomy names and country names) and an optional `vectors` table.

Ranking: rows matching more of the query's words first, then BM25 (name weighted 3, text 1, tags 0.4), then a boost for `sea` (1.25) and `apac` (1.15). With vectors present, keyword and vector rankings are merged by reciprocal rank fusion. Embeddings use fastembed (default `BAAI/bge-small-en-v1.5`, configurable).

### MCP server (`agent/server.py`)

One server, three doors. Over stdio it serves local MCP clients; with `--http` it also serves the
REST API under `/api` (`agent/api.py`) and the HTML interface (`agent/web.py`). Twelve tools:
`search`, `get_source`, `get_document`, `list_by_tag`, `get_technology`, `compare_technologies`,
`list_technology_register`, `list_gaps`, `library_stats`, and — when `DATABASE_URL` holds the
read-only role's DSN — `sql_query`, `db_catalog` and `graph_neighbors` over the Postgres layer.
It works with mcp 1.x (FastMCP) and 2.x (MCPServer), builds the index on first start if missing,
and nothing in it is specific to one AI vendor.

### Postgres layer (`db/`, `agent/graph.py`, `tools/load_postgres.py`, `agent/pg.py`)

An optional second home for the data: schema `og` on Neon with pgvector embeddings, full-text
search and a property graph (`node`/`edge`) that links sources, documents, cards, register
entries, organisations and gaps; every edge is a recorded fact or a named matching rule with its
evidence in `props`. `tools/load_postgres.py` replaces every table in one transaction (pipeline
mode over the WAN), open-licence text only by default. The server, the REST API's SQL console and
the web UI read it through `agent/pg.py` as role `og_mcp_read` — SELECT-only grants plus forced
read-only transactions plus a single-statement guard. Details in [POSTGRES.md](POSTGRES.md).

**Neon is the live read layer (decision #34):** the web pages and the MCP/REST `search` read it
first and fall back to the SQLite index automatically (a page shows a notice when the fallback
answered). `document.body`, `vendor.aliases`, `equipment.sources` and `source.embedding` back the
UI's full-document renders, the coverage queue, the equipment detail panel and source search.
Publish pipeline: `tools/build.py` → `agent/library.py build` → `agent/embed.py --incremental`
(vectors cached by (kind, ref) + text hash, so only changed rows embed) →
`tools/load_postgres.py` (one transaction) — data changes go live on both readers with no deploy.

### Hosting (`deploy/cloudflare/`, plus `deploy/frontend/` + `deploy/backend/` for the split)

A Cloudflare Worker checks the API key at the edge and forwards to one Cloudflare Container built
from the repo Dockerfile (open-licence copy only, built at deploy time). `/mcp` also accepts
OAuth for URL-only clients such as claude.ai; web UI paths pass through to the container, which
checks a session cookie derived from the same key. The optional secret `DATABASE_URL` gives the
container the read-only Postgres DSN. Details in [HOSTING.md](HOSTING.md).

The split deployment (decision #34, code in the repo, deploy pending the owner's domain
confirmation) separates the two: `deploy/frontend/` serves the web UI (session cookies) at
`techlib.hilir.app`, `deploy/backend/` serves MCP + REST (API-key/OAuth) at `api.hilir.app`;
both containers are slim (no embed step) and read Neon live.

### Automation (`.github/workflows/`)

- `validate.yml`: on every push, build, tests, and a check that generated files are committed.
- `refresh.yml`: Mondays 02:00 UTC collects new arXiv and OSTI records; on the 1st of each month also runs `tools/check_links.py`. Commits changes as github-actions[bot]. Can be run by hand (workflow_dispatch).

## Design choices

- **Files over services.** Records, corpus and logs are JSON and Markdown in git, so any tool or agent can read them without the server.
- **Licence travels with content.** Every document and every search result carries its licence and reuse level.
- **Verification is a log, not edits.** Findings are replayable and auditable.
- **One index, two retrieval modes.** Keyword search works with no model download; embeddings are an add-on.
- **The database is read-only by construction.** Agent-written SQL runs as `og_mcp_read`: SELECT-only grants, forced read-only transactions and a single-statement guard — independent layers, so one mistake cannot expose writes.
