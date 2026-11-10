# AGENTS.md

### Current estate state (2026-11-06) — read before planning anything

- Auth: hilir Access (`access.hilir.app`). Browser = OIDC PKCE (client `techlib` at the edge);
  the API/MCP door (`techlib-api.hilir.app`, worker `og-tech-library-api`) accepts an Access
  JWT (aud = registered origins `https://techlib.hilir.app` /
  `https://techlib-api.hilir.app`) or a person's estate key, introspected at Access
  (RFC 7662) with the **techlib-api** client. Headers: `Authorization: Bearer` or
  `x-api-key` (re-attached as Bearer for the container hop). Scopes are the boundary
  (`docs/AUTH.md`).
- MCP: `POST https://techlib-api.hilir.app/mcp` (stateless; PRM anonymous). REST: `/api/*`.
- Publish: **docs/HOSTING.md** (current-state section at the top) — three workers via wrangler
  (deploy/edge, deploy/frontend, deploy/backend); containers via CI `images` workflow →
  VPS `sudo vps deploy techlib` (the `vps` wrapper is the only sudo verb; it health-gates and
  auto-rolls back).
- VPS: both containers run at `/srv/hilir/techlib` on 15.235.248.33 behind Caddy + tunnel. VPS
  operations follow the owner's playbook (`~/Documents/VibeProject/VPS Control/operations/AGENT-PLAYBOOK.md`):
  connect only with the `~/.ssh/agent_dsh` key; sudo is allowlisted to `vps *` only; after every
  change run `sudo vps status` + `sudo vps health` (must print `mygis 303, techlib-origin 403,
  tlea-origin 403`) and report digest + gate + rollback; mygis ships as a Mac build →
  `docker save | ssh 'gunzip | sudo vps load'` → `sudo vps up mygis`, never `vps deploy mygis`.
- The dead `LibraryApi` Durable Object and the sk-/ACCESS-binding design are deleted; the
  stale tests were replaced by `deploy/backend/tests/machine-gate.test.ts`.
- Do not touch auth internals, DNS, or application content without an explicit owner ask.
  Estate record: `hilir-access/docs/STATUS.md`.

### Where the work stands (2026-11-11)

| Item | Count (from `python tools/build.py`) |
| --- | --- |
| Catalog sources | 407 valid, 407 unique ids |
| Technology cards | 334 (341-entry register) |
| Vendor records | 457 |
| Equipment classes | 8 (five boiler classes, centrifugal compressor, centrifugal pump, industrial gas turbine) |
| Corpus documents | 287, each with a hand-written summary (14,948 chunks) |

Verified live 2026-11-11: Neon reloaded (407 sources / 457 vendors / 334 cards / 8 equipment /
14,948 chunks / 3,720 nodes / 13,140 edges / 16,154 vectors) and both containers re-deployed from
CI `images` run 42864857287 (ui sha256:f0aa7d4a…, api sha256:2a2f1b5e…, both healthy as user
`library`); VPS gate `mygis 303, techlib-origin 403, tlea-origin 403` green. Standing main
effort is source discovery (`docs/SOURCE_DISCOVERY_PLAN.md`, decision #30); the next equipment
families wait on the owner (decision #33). Open owner items and the session log are in
`docs/STATUS.md`.

Permission boundary, restated: the only write in this application is an account row in
`library.account` (admin-gated). There is no endpoint that writes catalog content, and the
Postgres layer is read-only by construction. A task that needs a new write path is an owner
decision, not an implementation detail.

Instructions for any AI agent (Claude, Codex, Gemini, Copilot, Cursor or others) and any person
working in this repository. Read this file first, then the document that matches your task.
This file and `docs/DEVELOPMENT.md` are deliberately vendor-neutral: no step depends on a
particular assistant, model or IDE.

## ⚠️ AUTH IS LOAD-BEARING — read `docs/AUTH.md` before touching anything auth-related

Sign-in is **hilir Access** (`https://access.hilir.app`); this repo is an OIDC client that
verifies access tokens locally. **Do not add, restore or "simplify" any of these — each was
deliberately deleted on 2026-11-05 and each broke production when present:**

- a library key / `LIBRARY_API_KEY` / `LIBRARY_USERS`, the container's `/login`, or the edge's
  `?classic=1` path (Access is the only door);
- a password, session or key store of any kind in this repo;
- identity from a header (`x-hilir-email` is gone) — identity comes from the provider's
  userinfo endpoint;
- an audience of `techlib` (the name) — tokens carry `aud = https://techlib.hilir.app`
  (the registered **resource**);
- a body-form client secret (the client is registered `client_secret_basic`);
- a form-POST sign-out, or cookie-clearing-only sign-out (sign-out is a browser navigation to
  the provider's end-session endpoint).

If a task seems to need any of the above, stop and say so instead of implementing it.

Permissions are route-level: a scope is only a precondition, and each app checks it at the
exact route or tool that acts (`docs/AUTH.md` → "Who may do what"; estate rule book:
`hilir-access/docs/ROLES.md`). **Never widen a scope to make something work** — gate the
specific route instead, keep machine clients separate from people, and update the matrix in
the same pass.

Verification commands and failure signatures: **`docs/AUTH.md`**. Estate-wide authority:
`hilir-access/docs/STATUS.md` (FINAL STATE).

## What this repository is

A library of public sources on oil, gas, petrochemical and energy technologies, built for AI
agents to find, cite and read. It has six layers:

1. **Catalog**: one JSON record per source in `catalog/sources/`, validated against `schema/source.schema.json`.
2. **Corpus**: collected documents in `corpus/<source-id>/`, each tagged with its licence and carrying a hand-written `summary`.
3. **Technology cards**: one JSON card per technology in `catalog/technologies/` (schema `schema/technology.schema.json`), linked to the register `catalog/technology-register.yaml`. Every card has sources; every figure has a URL, a basis and (for costs) a dollar year; anything not found is a recorded gap.
4. **Vendors and equipment**: one vendor record per supplier in `catalog/vendors/` (schema `schema/vendor.schema.json`) and one equipment record per equipment class in `catalog/equipment/` (schema `schema/equipment.schema.json`, opened with boilers) — specification ranges, vendor model lines and sources; no guessed figures.
5. **Agent access**: a search index, an MCP server, a REST API and a web interface (`agent/web.py`) in `agent/`, hosted at https://techlib.hilir.app (see docs/HOSTING.md).
6. **Postgres layer**: schema `og` with pgvector, full-text search and a knowledge graph (`db/schema.sql`, `agent/graph.py`, `tools/load_postgres.py`), meant for Neon and served through the read-only role `og_mcp_read` (`agent/pg.py`). See docs/POSTGRES.md.

## Read next

| If you need to | Read |
| --- | --- |
| **Pick up development work (start of any coding session)** | **[docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)** |
| Touch sign-in, tokens, keys or sign-out (**read first**) | [docs/AUTH.md](docs/AUTH.md) |
| Understand how the parts fit together | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| Use the library (search, cite, MCP setup) | [docs/USER_GUIDE.md](docs/USER_GUIDE.md) |
| Add sources, verify terms, collect, run refreshes | [docs/MAINTAINER_MANUAL.md](docs/MAINTAINER_MANUAL.md) |
| Find sources the catalog does not know yet | [docs/SOURCE_DISCOVERY_PLAN.md](docs/SOURCE_DISCOVERY_PLAN.md) |
| Host the server for cloud agents (Copilot Studio and others) | [docs/HOSTING.md](docs/HOSTING.md) |
| Operate on the VPS (deploy, health gate, rollback, mygis) | **`~/Documents/VibeProject/VPS Control/operations/AGENT-PLAYBOOK.md`** |
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
