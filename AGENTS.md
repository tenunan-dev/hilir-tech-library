# AGENTS.md

Instructions for any AI agent (Claude, Codex, Gemini, Copilot, Cursor or others) and any person
working in this repository. Read this file first, then the document that matches your task.

## What this repository is

A library of public sources on oil, gas, petrochemical and energy technologies, built for AI
agents to find, cite and (where licences allow) read. It has five layers:

1. **Catalog**: one JSON record per source in `catalog/sources/`, validated against `schema/source.schema.json`.
2. **Corpus**: collected documents in `corpus/<source-id>/`, each tagged with its licence and carrying a hand-written `summary`.
3. **Technology cards**: one JSON card per technology in `catalog/technologies/` (schema `schema/technology.schema.json`), linked to the register `catalog/technology-register.yaml`. Every card has sources; every figure has a URL, a basis and (for costs) a dollar year; anything not found is a recorded gap.
4. **Agent access**: a search index, an MCP server, and a REST API in `agent/`, hosted at https://techlib.hilir.app (see docs/HOSTING.md).
5. **Postgres layer**: schema `og` with pgvector, full-text search and a knowledge graph (`db/schema.sql`, `agent/graph.py`, `tools/load_postgres.py`), meant for Neon. See docs/POSTGRES.md.

## Read next

| If you need to | Read |
| --- | --- |
| Understand how the parts fit together | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Use the library (search, cite, MCP setup) | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) |
| Add sources, verify terms, collect, run refreshes | [docs/MAINTAINER_MANUAL.md](docs/MAINTAINER_MANUAL.md) |
| Host the server for cloud agents (Copilot Studio and others) | [docs/HOSTING.md](docs/HOSTING.md) |
| Export to Dataverse / Power Apps tables | [docs/DATAVERSE.md](docs/DATAVERSE.md) |
| Load into Postgres with vectors and a knowledge graph (Neon) | [docs/POSTGRES.md](docs/POSTGRES.md) |
| Know what is done and what to do next | [docs/STATUS.md](docs/STATUS.md) |
| Know why a rule exists | [docs/DECISIONS.md](docs/DECISIONS.md) |

## Rules you must not break

1. **Respect `reuse_level`.** Store full text only for `full-text-open` and `full-text-restricted` sources. `summary-only` means your own summary plus a link. `catalog-only` means no content at all.
2. **Restricted text stays private.** Files from `full-text-restricted` sources are personal reference copies. Never publish them, paste them into public places or use them commercially. The repository must stay private while it holds them.
3. **Only collect from verified records.** A record must have `verification: verified` before any collector touches it. Collectors enforce this; do not bypass it.
4. **Obey robots.txt and terms.** Never change the user agent, rotate IPs, or otherwise get around a block. Where `automated_access` is `prohibited`, content comes in by hand through `corpus/_inbox/`. The only robots exception is arXiv's API (see DECISIONS.md); a new exception needs the owner's written approval and an entry in DECISIONS.md.
5. **Never invent sources, evidence or figures.** Every licence finding needs an evidence URL you actually read; every number in a technology card needs the URL it came from, and costs need their dollar year and basis. If a figure cannot be found, record it as a gap on the card (why, where to get it, next action) instead of guessing; open gaps are in `catalog/index/gaps.md` and the `list_gaps` tool.
6. **Generated files are not edited by hand.** `catalog/catalog.jsonl` and `catalog/index/*` come from `tools/build.py`; `build/` comes from `agent/library.py build`.
7. **Paid sources wait for the owner.** Records for paid services stay `catalog-only` until the owner provides subscriptions or API keys.
8. **Every corpus document needs a `summary`.** Write one or two sentences in your own words in the front matter (never copied text). `tests/test_technologies.py` fails for any document without one, so a collector run is not finished until the new documents are summarised.
9. **Technology cards follow the card rules.** Card name or alias must match a register entry exactly; `sector` is one of UPS, MID, GAS, REF, PCH, PWR, H2, CCS or a discipline code (PRC, ROT, INS, MAT, HSE, DIG); a `source_id` must exist in `catalog/sources/`; a Wikipedia citation is secondary and must say so in its note; a USD cost needs a `year` or the words "dollar year not stated" in its basis. Missing facts become `gaps` with a valid `reason_code`.
10. **Secrets never enter the repository or the memory notes.** That covers the library API key, Cloudflare tokens and the Neon connection string.

## Before you commit

```
pip install -r requirements.txt -r requirements-collect.txt -r requirements-agent.txt pytest
python tools/build.py      # must print "N records valid"
pytest -q tests            # must pass, offline (Postgres tests run only if TEST_DATABASE_URL is set)
```

Commit the records you changed together with the regenerated `catalog/` files. CI repeats these checks on every push.

## When you finish a piece of work

Update [docs/STATUS.md](docs/STATUS.md): the counts, what you did (with the date), and what is next. Add any new rule or owner decision to [docs/DECISIONS.md](docs/DECISIONS.md). The next agent has only these files to go on.
