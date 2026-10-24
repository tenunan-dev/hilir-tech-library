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
                                   agent/server.py (MCP, stdio) ──▶ any MCP client
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

### Technology cards (`catalog/technologies/`, `schema/technology.schema.json`, `agent/technologies.py`)

One JSON card per technology option: sector, category, maturity (commercial, demonstration, pilot, lab), TRL with its source, principle, process steps (each with equipment and links to downstream steps), key equipment, performance and cost figures (each with unit, dollar year, basis and source), suppliers, reference plants, advantages, limitations and sources. Cards are our own words; figures are facts taken from cited sources. `tools/build.py` validates them and writes `catalog/technologies.jsonl` and `catalog/index/technologies-<SECTOR>.md`. `agent/technologies.py` turns process steps into a Mermaid block flow diagram and builds comparison rows. The search index includes cards as `kind = "technology"`.

### Verification (`tools/verification/`)

`log.jsonl` is an append-only log of terms checks: `id`, `checked_on`, `evidence` (URL), `finding`, and any of `url`, `licence`, `reuse_level`, `access`, `update_frequency`, `automated_access`, `permitted_use`. `apply_verification.py` replays the whole log onto the records, so the log is the source of truth for verification state. An entry with `"verified": false` records a check that could not confirm the terms; such records appear in `catalog/index/needs-manual-check.md`.

### Build (`tools/build.py`)

Validates each record against the schema and checks id equals file name, then writes `catalog/catalog.jsonl`, one index page per code in `catalog/index/` (Asia Pacific first), `catalog/index/README.md` (counts) and `needs-manual-check.md`. CI fails if these generated files are out of date.

### Collectors (`collectors/`)

- `common.py`: polite HTTP (`fetch` checks robots.txt, waits 3 s per host, sends user agent `og-tech-sources-collector/0.1`), HTML and PDF to Markdown (trafilatura, pypdf), and `write_document`, which writes front matter from the record and de-duplicates by SHA-256 through `corpus/manifest.jsonl`.
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

A stdio MCP server with `search`, `get_source`, `get_document`, `list_by_tag` and `library_stats`. It works with mcp 1.x (FastMCP) and 2.x (MCPServer), and builds the index on first start if missing. Any MCP client can use it; nothing in it is specific to one AI vendor.

### Automation (`.github/workflows/`)

- `validate.yml`: on every push, build, tests, and a check that generated files are committed.
- `refresh.yml`: Mondays 02:00 UTC collects new arXiv and OSTI records; on the 1st of each month also runs `tools/check_links.py`. Commits changes as github-actions[bot]. Can be run by hand (workflow_dispatch).

## Design choices

- **Files over services.** Records, corpus and logs are JSON and Markdown in git, so any tool or agent can read them without the server.
- **Licence travels with content.** Every document and every search result carries its licence and reuse level.
- **Verification is a log, not edits.** Findings are replayable and auditable.
- **One index, two retrieval modes.** Keyword search works with no model download; embeddings are an add-on.
