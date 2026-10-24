# AGENTS.md

Instructions for any AI agent (Claude, Codex, Gemini, Copilot, Cursor or others) and any person
working in this repository. Read this file first, then the document that matches your task.

## What this repository is

A library of public sources on oil, gas, petrochemical and energy technologies, built for AI
agents to find, cite and (where licences allow) read. It has three layers:

1. **Catalog**: one JSON record per source in `catalog/sources/`, validated against `schema/source.schema.json`.
2. **Corpus**: collected documents in `corpus/<source-id>/`, each tagged with its licence.
3. **Agent access**: a search index and an MCP server in `agent/`.

## Read next

| If you need to | Read |
| --- | --- |
| Understand how the parts fit together | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Use the library (search, cite, MCP setup) | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) |
| Add sources, verify terms, collect, run refreshes | [docs/MAINTAINER_MANUAL.md](docs/MAINTAINER_MANUAL.md) |
| Host the server for cloud agents (Copilot Studio and others) | [docs/HOSTING.md](docs/HOSTING.md) |
| Export to Dataverse / Power Apps tables | [docs/DATAVERSE.md](docs/DATAVERSE.md) |
| Know what is done and what to do next | [docs/STATUS.md](docs/STATUS.md) |
| Know why a rule exists | [docs/DECISIONS.md](docs/DECISIONS.md) |

## Rules you must not break

1. **Respect `reuse_level`.** Store full text only for `full-text-open` and `full-text-restricted` sources. `summary-only` means your own summary plus a link. `catalog-only` means no content at all.
2. **Restricted text stays private.** Files from `full-text-restricted` sources are personal reference copies. Never publish them, paste them into public places or use them commercially. The repository must stay private while it holds them.
3. **Only collect from verified records.** A record must have `verification: verified` before any collector touches it. Collectors enforce this; do not bypass it.
4. **Obey robots.txt and terms.** Never change the user agent, rotate IPs, or otherwise get around a block. Where `automated_access` is `prohibited`, content comes in by hand through `corpus/_inbox/`. The only robots exception is arXiv's API (see DECISIONS.md); a new exception needs the owner's written approval and an entry in DECISIONS.md.
5. **Never invent sources, evidence or figures.** Every licence finding needs an evidence URL you actually read; every number in a technology card needs the URL it came from, and costs need their dollar year and basis.
6. **Generated files are not edited by hand.** `catalog/catalog.jsonl` and `catalog/index/*` come from `tools/build.py`; `build/` comes from `agent/library.py build`.
7. **Paid sources wait for the owner.** Records for paid services stay `catalog-only` until the owner provides subscriptions or API keys.

## Before you commit

```
pip install -r requirements.txt -r requirements-collect.txt -r requirements-agent.txt pytest
python tools/build.py      # must print "N records valid"
pytest -q tests            # must pass, offline
```

Commit the records you changed together with the regenerated `catalog/` files. CI repeats these checks on every push.

## When you finish a piece of work

Update [docs/STATUS.md](docs/STATUS.md): the counts, what you did (with the date), and what is next. Add any new rule or owner decision to [docs/DECISIONS.md](docs/DECISIONS.md). The next agent has only these files to go on.
