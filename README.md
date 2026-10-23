# O&G technology source library

A curated catalog of public sources on oil, gas, petrochemical and energy technologies, built so AI agents can find, cite and (where the licence allows) read them.

Phase 1 is the catalog: 342 sources across 8 sectors and 6 engineering disciplines, weighted toward Asia Pacific and Southeast Asia. Later phases add the content corpus, a search index and an MCP server (see [Roadmap](#roadmap)).

## Layout

| Path | What it holds |
| --- | --- |
| `taxonomy.yaml` | Sector codes (UPS, MID, GAS, REF, PCH, PWR, H2, CCS), discipline codes (PRC, ROT, INS, MAT, HSE, DIG), sub-topics and regions |
| `schema/source.schema.json` | JSON Schema every catalog record must pass |
| `catalog/sources/<id>.json` | One record per source; this is the source of truth |
| `catalog/catalog.jsonl` | Generated: all records, one per line, for loaders and embedding pipelines |
| `catalog/index/<CODE>.md` | Generated: one page per code, Asia Pacific and Southeast Asia sources listed first |
| `catalog/index/README.md` | Generated: counts by code, region, type, reuse level and verification |
| `corpus/` | Phase 2: collected content, as Markdown chunks with provenance |
| `tools/build.py` | Validates every record and regenerates the generated files |
| `tools/seed/*.psv`, `tools/seed_to_json.py` | The one-time seed lists the records were created from |

## Reuse levels

Each record's `reuse_level` decides what the collector may store. Collectors act only on records marked `verification: verified`.

| Level | Meaning | Where content may go |
| --- | --- | --- |
| `full-text-open` | Open licence (CC BY, public domain, OGL, NLOD and similar) | Corpus, with attribution |
| `full-text-restricted` | Downloadable but no open licence, and the site's terms do not forbid keeping a reference copy | This private repo only, with a note of the terms |
| `summary-only` | Terms forbid copying, or the value is in facts rather than text | Our own summaries and extracted facts, with a link |
| `catalog-only` | Paywalled, login-only, or not downloadable | Catalog record only, kept for retrieval once a licence or API key is available |

Paid sources (API, ASTM, OnePetro full text, ICIS and others) are catalog-only until subscriptions or API keys are added.

## Verification

All records start as `unverified`: the URL, licence and reuse level were drafted from the publisher's known terms and must be checked against the live terms page before any content is collected. Records with "verify" in `notes` have a specific doubt (URL path, licence wording or access terms). To verify a record, open the URL and terms page, correct the fields, and set `verification` to `verified` and `last_verified` to the date.

## Using it from an agent

- Simplest: load `catalog/catalog.jsonl` and filter by `sectors`, `disciplines`, `regions` or `reuse_level`.
- For browsing or a Claude Project: attach `catalog/index/*.md`.
- Always cite `url` and respect `reuse_level` and `licence` when quoting.

## Adding or changing a source

1. Add or edit `catalog/sources/<id>.json` (the id must match the file name).
2. Run `pip install -r requirements.txt` once, then `python tools/build.py`.
3. Commit the record together with the regenerated files. CI runs the same check on every push.

## Roadmap

1. **Catalog (done):** taxonomy, schema, 342 records, generated indexes.
2. **Verification and open corpus:** verify records, then collect `full-text-open` and `full-text-restricted` content through APIs and feeds into `corpus/<id>/`, chunked with licence and citation metadata.
3. **Agent access and refresh:** keyword and vector search index, MCP server (`search`, `get_source`, `list_by_tag`), scheduled refresh and link and licence checks.
