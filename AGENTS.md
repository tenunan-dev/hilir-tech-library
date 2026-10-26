# AGENTS.md

Instructions for any AI agent (Claude, Codex, Gemini, Copilot, Cursor or others) and any person
working in this repository. Read this file first, then the document that matches your task.

## What this repository is

A library of public sources on oil, gas, petrochemical and energy technologies, built for AI
agents to find, cite and read. It has five layers:

1. **Catalog**: one JSON record per source in `catalog/sources/`, validated against `schema/source.schema.json`.
2. **Corpus**: collected documents in `corpus/<source-id>/`, each tagged with its licence and carrying a hand-written `summary`.
3. **Technology cards**: one JSON card per technology in `catalog/technologies/` (schema `schema/technology.schema.json`), linked to the register `catalog/technology-register.yaml`. Every card has sources; every figure has a URL, a basis and (for costs) a dollar year; anything not found is a recorded gap.
4. **Agent access**: a search index, an MCP server, a REST API and a web interface (`agent/web.py`) in `agent/`, hosted at https://techlib.hilir.app (see docs/HOSTING.md).
5. **Postgres layer**: schema `og` with pgvector, full-text search and a knowledge graph (`db/schema.sql`, `agent/graph.py`, `tools/load_postgres.py`), meant for Neon and served through the read-only role `og_mcp_read` (`agent/pg.py`). See docs/POSTGRES.md.

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
| Know what shipped, release by release | [CHANGELOG.md](CHANGELOG.md) |
| Know why a rule exists | [docs/DECISIONS.md](docs/DECISIONS.md) |
| Find a superseded version of a document | [docs/archive/](docs/archive/) |

## Rules you must not break

1. **Acquisition is unrestricted; inclusion is manual.** Agents may fetch and store any publicly reachable content regardless of `licence`, `reuse_level` or robots preferences (decision 29). Those fields are recorded labels that support the owner's review — they do not gate what may be fetched or kept. The owner alone decides what enters final reports, `corpus/`, exports or anything that leaves the repository.
2. **The repository stays private.** Agents never publish, paste into public places, or export to shared environments anything from the repository. What leaves the repository leaves by the owner's hand.
3. **Only collect from verified records.** A record must have `verification: verified` before any collector touches it. Collectors enforce this; do not bypass it.
4. **Fetch with standard tools; record blocks.** Use the normal fetch tooling as-is. When a site blocks or limits a fetch, record that in the record or sweep output (`access`, `automated_access`, `notes`) and move on. Content from sites that block automation still comes in by hand through `corpus/_inbox/`.
5. **Never invent sources, evidence or figures.** Every licence finding needs an evidence URL you actually read; every number in a technology card needs the URL it came from, and costs need their dollar year and basis. If a figure cannot be found, record it as a gap on the card (why, where to get it, next action) instead of guessing; open gaps are in `catalog/index/gaps.md` and the `list_gaps` tool.
6. **Generated files are not edited by hand.** `catalog/catalog.jsonl` and `catalog/index/*` come from `tools/build.py`; `build/` comes from `agent/library.py build`.
7. **Record access reality.** Paywalled or login-only pages are recorded with their real `access` value (`paywalled`, `free-registration`); whether to buy credentials is the owner's call. Never simulate or guess content that could not be fetched.
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

Update [docs/STATUS.md](docs/STATUS.md): the counts, what you did (with the date), and what is next. Add any new rule or owner decision to [docs/DECISIONS.md](docs/DECISIONS.md). Add an entry to [CHANGELOG.md](CHANGELOG.md) under today's version (`YYYY.MM.DD`, or the next `.N` suffix if the day already has a release), and archive any superseded document in [docs/archive/](docs/archive/) following its README instead of deleting it. The next agent has only these files to go on.
