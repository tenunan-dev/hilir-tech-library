# Development guide — picking up work in this repository

For any AI agent (Claude, Codex, Gemini, Copilot, Cursor, a local model) or any person. Nothing in
this guide depends on a particular assistant, model or IDE. If a step only works in one tool, that
is a documentation bug — fix the document.

Read in this order before you change anything:

1. [AGENTS.md](../AGENTS.md) — the rules, and the "Current estate state" block.
2. This file — environment, gates, publish.
3. [AUTH.md](AUTH.md) — **before** touching sign-in, tokens, keys or sign-out.
4. The document for your task (see the routing table in §3).
5. [STATUS.md](STATUS.md) — what is done, what is open, what the last session did.

Repository: `tenunan-dev/hilir-tech-library` (private). Working branch at the time of writing:
`phase4-auth`; `main` is the default branch. Never amend or force-push a commit you did not write —
concurrent sessions share this tree (see §8).

---

## 1. What this system is

| Layer | Source of truth | Read by |
| --- | --- | --- |
| Catalog, cards, vendors, equipment | JSON files under `catalog/` | `tools/build.py`, `agent/library.py build` |
| Corpus | Markdown with JSON front matter under `corpus/` | same |
| Search index | `build/library.db` (generated, not committed) | `agent/library.py`, MCP, REST, web |
| Postgres layer | schema `og` on Neon (rebuilt from the files) | `agent/pg.py` → MCP tools, REST, web pages |
| Admin layer | schema `library` on Neon (`library.account`) | `agent/web.py` `/admin` |
| Estate | three Cloudflare Workers + two containers on the VPS | browsers and machine clients |

Files are the master copy. The database is disposable: `tools/load_postgres.py` truncates and
reloads it from the files in one transaction. The only data that lives **only** in Postgres is
schema `library` (accounts, events), which the reload never touches.

Current counts are printed by `python tools/build.py` and reported by the `library_stats` tool.

## 2. Environment

Python side (all content work and the Python agent):

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt -r requirements-collect.txt \
  -r requirements-agent.txt -r requirements-postgres.txt pytest
```

- **Always call `.venv/bin/python -m pytest`**, not a bare `pytest` — a stale shim on the owner's
  Mac shadows it.
- `requirements-postgres.txt` is only needed for the Neon loader and the Postgres tests.

Node side (only for the Workers and container images):

```bash
cd deploy/backend && npm install    # same in deploy/edge and deploy/frontend
npx tsc --noEmit                    # typecheck (backend has this script)
npm test                            # backend only: node --test tests/*.test.ts
```

Secrets never live in the repo: `.env.local` (owner DSNs), `~/.config/hilir-tech-library/*`, and
Worker secrets set with `wrangler secret put`. If you need one you do not have, ask the owner.

## 3. Where a change goes

| Change | Files | Then |
| --- | --- | --- |
| Add or edit a source | `catalog/sources/<id>.json` | `tools/build.py`, tests |
| Add or edit a technology card | `catalog/technologies/<id>.json` | `tools/build.py`, tests |
| Add or edit a vendor | `catalog/vendors/<id>.json` | `tools/build.py`, tests |
| Add or edit an equipment class | `catalog/equipment/<id>.json` | `tools/build.py`, tests |
| Collect documents | `corpus/<source-id>/`, `corpus/manifest.jsonl` | summarise every new file, tests |
| Search / ranking | `agent/library.py`, `agent/embed.py` | rebuild index, tests |
| MCP tool | `agent/server.py` (+ the module it calls) | tests, then the publish cycle if it needs data |
| REST route | `agent/api.py` | tests |
| Web page | `agent/web.py` | tests (render parity if it reads Neon) |
| Postgres schema or loader | `db/schema.sql`, `tools/load_postgres.py`, `agent/graph.py` | schema pre-flight, tests, Neon reload |
| **Auth, tokens, cookies, sign-out** | `deploy/edge`, `deploy/frontend`, `deploy/backend`, `agent/auth.py`, `agent/server.py` | read [AUTH.md](AUTH.md) first; **owner ask required**; run the auth verification |
| Container images | `deploy/docker/Dockerfile.frontend`, `Dockerfile.backend` | CI `images` workflow → VPS pull |
| Docs | `docs/`, `README.md`, `AGENTS.md`, `CLAUDE.md` | update `STATUS.md`, `CHANGELOG.md`, archive superseded versions |

**Never hand-edit generated files:** `catalog/catalog.jsonl`, `catalog/index/*`,
`catalog/vendors.jsonl`, `catalog/equipment.jsonl`, `catalog/technologies.jsonl`, `build/*`.
They come from `tools/build.py` and `agent/library.py build`; CI fails when they are stale.

## 4. Gates — run before every commit

```bash
.venv/bin/python tools/build.py          # must print "N records valid, N unique ids, ..."
.venv/bin/python -m pytest -q tests      # must pass offline (Postgres tests skip without TEST_DATABASE_URL)
cd deploy/backend && npm test            # when you touched a Worker
cd deploy/backend && npx tsc --noEmit    # typecheck, when you touched TypeScript
```

What the tests protect, so you know when a failure is your fault:

| Test file | Guards |
| --- | --- |
| `test_technologies.py` | card rules, register coverage, every corpus doc has a summary |
| `test_vendors.py`, `test_equipment.py` | record shape, enum values, source links |
| `test_graph.py` | graph builds, ≤40% of cards without a catalogued citation |
| `test_pg.py`, `test_render_parity.py` | Neon layer; parity suite needs `TEST_DATABASE_URL` (scratch DB only) |
| `test_server_http.py`, `test_api.py`, `test_web.py` | MCP/REST/web surfaces |
| `deploy/backend/tests/machine-gate.test.ts` | the API door: JWT audience, estate key, header re-attachment |

Commit the records and the regenerated files together. See §10 for the session-close checklist.

## 5. The publish pipeline

Data changes and code changes publish differently. Decide which one you have.

### 5a. Data only (cards, corpus, vendors, equipment, sources) — no deploy

From the repository root, with `DATABASE_URL` exported as the **owner (unpooled)** DSN:

```bash
python tools/build.py
python agent/library.py build
python agent/embed.py --incremental          # vectors cached by (kind, ref) + text hash
python tools/load_postgres.py --embeddings sqlite --include-restricted
```

Expect a few minutes, not a deploy. Both containers read Neon live, so the change is visible on the
UI and the API as soon as the load commits. This is the normal path and the reason the split
exists (decision #34). Verify with `/api/version` (drift stamp) and a search on both doors.

`--incremental` matters: a full embed is ~12 minutes and a full reload is unnecessary. Use
`--include-restricted` exactly when the owner's reload policy includes restricted text — the
standing command in STATUS.md does.

### 5b. Code only (Python agent, Worker) — deploy the changed piece

```bash
cd deploy/edge     && npx wrangler deploy
cd deploy/frontend && npx wrangler deploy
cd deploy/backend  && npx wrangler deploy
```

Deploy only the Worker you changed. A Worker deploy takes seconds and does **not** rebuild the
container image.

### 5c. Container code (anything under `agent/`, `deploy/docker/`, `catalog` baked into the image)

```bash
gh workflow run images --repo tenunan-dev/hilir-tech-library --ref <branch>
ssh -i ~/.ssh/mygis_deploy ubuntu@15.235.248.33 \
  "cd /srv/hilir/techlib && docker compose pull && docker compose up -d"
```

Expect the workflow to succeed and both containers to report Started/Up. Keep traffic low for a
minute after the swap: a single-instance container needs the old instance to sleep and cycle.

## 6. Verification after a deploy — the 60-second check

From [HOSTING.md](HOSTING.md), the API door:

```bash
curl -s -o /dev/null -w "%{http_code}\n" https://techlib-api.hilir.app/.well-known/oauth-protected-resource   # 200
curl -s -D- -o /dev/null -X POST https://techlib-api.hilir.app/mcp -H "content-type: application/json" -d '{}' | grep -i www-authenticate   # challenge, no error member
curl -s -o /dev/null -w "%{http_code}\n" -X POST https://techlib-api.hilir.app/mcp -H "authorization: Bearer wrong" -H "content-type: application/json" -d '{}'   # 401
```

From [AUTH.md](AUTH.md), the UI door: `/` 303 → `/login`, `/health` 200, unauthenticated
`/api/stats` 401, `/login` redirects to the authorize URL **with `resource=`**, `/logout` redirects
to the end-session URL with `client_id` and `post_logout_redirect_uri`.

Then, in a browser: sign in → open a page → Sign out → land signed out with no error page. An agent
that cannot drive a browser should say so rather than claim this step passed.

Report the HTTP status codes you actually saw. "Deployed" is not "verified".

## 7. Auth — the short version (full rules in [AUTH.md](AUTH.md))

- Browsers sign in at `https://access.hilir.app`; this repo is an OIDC client.
- The API door accepts an Access **JWT** (`aud` = a registered resource origin) or a person's
  **estate key** (RFC 7662 introspection with the `techlib-api` client); the container re-verifies.
- Never reintroduce a library key, `LIBRARY_USERS`, a container login, a header identity, an
  audience of `techlib`, a body-form client secret, or cookie-only sign-out. Each broke production.
- **Never widen a scope to make something work.** Gate the specific route and update the matrix in
  AUTH.md in the same pass. Auth/DNS changes need an explicit owner ask.

## 8. Working safely in a shared tree

- Concurrent sessions may commit at any time. `git fetch` before pushing; never amend; diff and
  stage only the files you changed.
- The Mimosa security gate runs in warn mode on the owner's Mac. It flags parameterised SQL and
  the documented false positives; treat it as a review prompt, not a blocker. Prefer single-line
  SQL literals in `agent/pg.py` to keep the output quiet.
- `.DS_Store` files are tracked by accident of history; do not add more, do not stage them.

## 9. Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `pytest: command not found` or the wrong interpreter | Use `.venv/bin/python -m pytest` |
| `wrangler` says "Login failed with code: 1" | A stale certificate: `security delete-internet-password -s registry.cloudflare.com`, then retry |
| CI `validate` fails on generated files | You changed records but did not run `tools/build.py`; run it and commit the output |
| `/api/version` numbers do not match the repo | The Neon reload did not run, or it ran before `tools/build.py`; rerun §5a in order |
| Web page shows the "fallback index" notice | Neon unreachable from the container; check `DATABASE_URL` on the Worker and the Neon project state |
| Search returns no chunks for a source you just collected | `agent/library.py build` was not rerun, or the document lacks a `summary` (tests fail) |
| Card rejected by `build.py` | Name/alias must match a register entry; `sector` must be in the enum; a `source_id` must exist; a USD cost needs a `year` |
| `load_postgres.py` fails mid-schema | A SQL comment containing `;` breaks the statement splitter; keep comments out of statement bodies |

## 10. Closing a session — the handoff checklist

Anyone picking this up has only the files. Do all of these:

1. `tools/build.py` and `pytest` green; Worker tests green if you touched TypeScript.
2. [STATUS.md](STATUS.md): update the counts, add a log entry at the top in the established format
   (Did / Verified / Failed / Next) — including the exact error text of anything that failed.
3. [CHANGELOG.md](../CHANGELOG.md): an entry under today's version (`YYYY.MM.DD`, or `.N` if the
   day already has a release).
4. [DECISIONS.md](DECISIONS.md): a new numbered row for any owner decision or new rule (never edit
   a past decision; supersede it).
5. Superseded documents: copy to `docs/archive/` under its filename convention and link the copy
   from the living document — do not delete.
6. Commit the records with the regenerated files, and push.

## 11. Where to start right now

Open items live in [STATUS.md](STATUS.md) under "Handover" and "Open items". The standing main
effort is source discovery ([SOURCE_DISCOVERY_PLAN.md](SOURCE_DISCOVERY_PLAN.md), decision #30);
equipment families beyond the first eight wait on the owner (decision #33). Owner-only items are
marked as such — do not guess at them; ask.
