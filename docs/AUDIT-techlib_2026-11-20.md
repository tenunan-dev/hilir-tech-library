# techlib audit — code, live MCP, and Access compliance (2026-11-20)

Scope: the whole `hilir-tech-library` codebase, the tool test findings in
`~/VibeProject/Hilir/docs/HILIR_MCP_Tool_Test_2026-11-19/02_hilir-techlib_Technology_Library.md`
(verified live and in code), and compliance with the 2026-11-20 update to
`access.hilir.app` (estate audit closure: hardened `/api/v2-introspect`,
Cloudflare rate limit, hilir-auth 0.5.4, admin gates).
Focus per owner: techlib + techlib auth only.

Method: full read of `agent/` (24-tool MCP server, auth, gate, web), the three
Workers (`deploy/{edge,frontend,backend}`), `db/`, `catalog/glossary.jsonl`,
config files; every test-doc finding replayed against the **live** MCP server;
suites run (`pytest` 1428 passed / 12 skipped; `deploy/backend npm test`
**fails** — see F13).

## 1. Test-doc findings — verification result

| # | Test-doc finding | Verdict | Evidence |
|---|---|---|---|
| 1 | `list_glossary("PUE")` → `[]` while the description names PUE/WUE/SRU/MERCON/DLE | **Confirmed** | Live call returns `[]`; `catalog/glossary.jsonl` has 70 terms, none of the five named. Docstring says "60 entries" (`agent/library.py:510`) — stale. |
| 2 | `get_document` returns huge text, no `offset`/`limit` | **Confirmed, worse than reported** | Signature is path-only (`agent/server.py:183`, `agent/library.py:677-691`, `agent/pg.py:532-552`); no cap anywhere. Largest open document in Neon: **2,138,151 chars** (`corpus/netl/compendium-of-carbon-capture-technology-2024-6fe0c9fb.md`); three docs exceed 800k. The tester saw 106k. |
| 3 | `sql_query` on `og.sources` errors; `db_catalog` never says schema `og` | **Confirmed** | Live error reproduced; `pg.tables_doc` (`agent/pg.py:815-898`) lists bare names, no `og.` prefix, no worked example. Unqualified names only work because `_execute` sets `search_path = og, public` (`agent/pg.py:90`). |
| 4 | Duplicate Malaysia projects, conflicting statuses | **Confirmed** | Live: PFLNG SATU ×3 (proposed / operating / operating), PFLNG DUA ×2, Kasawari ×2 (`kasawari-ccs-sarawak` FID/CCS vs `petronas-kasawari-ccs-block-sk316-offshore-sarawak` operating/GAS). 12 of 15 Malaysian rows have `location: null`, `capacities: []`, `owners: []` (tester said 11/15 — drift, same shape). |
| 5 | Kasawari milestone "start-up" is really the FID | **Confirmed** | `get_project("kasawari-ccs-sarawak")`: status FID, sole milestone "start-up (per card source)" dated 2022, note says FID October 2022. Source: `catalog/projects/kasawari-ccs-sarawak.json`. |
| 6 | Malaysian projects blank with no gap hint | **Confirmed** | Project `summary()` (`agent/projects.py:20-28`) omits the `gaps` array 36/299 records carry; no MCP `list_*` row anywhere surfaces a gap/stub marker (vendors have none at all — see F9). |
| 7 | Honeywell vendor records with `products: []` | **Confirmed** | Live: `honeywell`, `honeywell-analytics` — `products: []`; vendor schema has no stub/gap concept (`agent/vendors.py:30-35`). |
| 8 | `compare_technologies` CCS/commercial: blank trl/applications/costs with no gap hint | **Confirmed** | Live: 5 of 12 rows `trl: null`, several `applications: []` / `costs: []`; summary rows (`agent/technologies.py:59-70`) carry no gap flag. |
| 9 | `search("carbon capture amine")` top-3 misses the amine card | **Confirmed + root cause found** | Live top-3: MTR vendor, enzyme project, urea condenser. Root cause: the Neon `hybrid_search` (what the live server uses) has **no technology boost and no region boost** (`db/schema.sql:344-387`), while the SQLite fallback applies `TECHNOLOGY_BOOST = 1.3` (`agent/library.py:41-42`, `bm25.py:19` title weight 3.0). Ranking parity was never carried into the Neon function. |

Untested items in §5 of the doc, now exercised: `graph_neighbors` depth 2 +
`rels` filter — works; `find_figures(kind="cost", unit="USD/kW")` — works
(substring match, returns USD/kWe too, as documented); `hybrid_search` via SQL
not exercised (needs a `vector(384)` argument).

Suggested tools/params (§4): `compare_technologies(technology_ids=[…])` does
not exist (params are sector/maturity/application only, `agent/server.py:216`);
no `list_documents` tool (REST `/api/documents` needs `?path=`;
`pg.document_index` exists but is web-only, `agent/pg.py:515-529`); no
`get_register_entry` (register list only, `agent/server.py:303-310`).

## 2. New findings from the code audit

**P1 — security / correctness**

- **F1. Reflected XSS in the sign-in-failed page (verified live).**
  `deploy/frontend/src/index.ts:255` interpolates `result.error` raw into HTML.
  hilir-auth's `callback()` short-circuits **before** state validation and
  returns the caller-controlled `?error=` query param verbatim
  (hilir-access `packages/hilir-auth/src/oidc.ts:190-192`), so
  `https://techlib.hilir.app/auth/callback?error=<img src=x onerror=…>` is
  reflected unescaped — reproduced live with a benign marker (`<b>bold</b>`
  landed raw in the page). hilir-auth 0.5.4 makes provider-relayed codes the
  standard path, widening what this string can be. Fix is one line (escape),
  plus a redeploy.
- **F2. hilir-auth pinned `^0.5.3` in all three Workers**
  (`deploy/{frontend,backend,edge}/package.json`). The 2026-11-20 Access
  standard is 0.5.4 (RFC 6749 §5.2 code relay on failed token exchange). The
  frontend is the only exchange client, so it is the one that behaves wrong
  today: a failed exchange shows the invented `token_exchange_failed_502`
  instead of the provider's code. Bump + redeploy.
- **F3. `deploy/backend` `npm test` fails as committed.** `node --test`
  cannot resolve `./proxy` (no extension) under plain Node ESM —
  `ERR_MODULE_NOT_FOUND`, 0 tests pass. HOSTING.md names this suite as the
  gate for the API door, so the gate currently cannot run. Fix the import
  specifier or run via tsx.
- **F4. Latent crash in `agent/technologies.py:53-56`** — `_range` raises
  `TypeError` for a schema-valid figure with neither `low` nor `high`
  (`f"up to {hi:g}"` on None). Schema only requires metric/unit/basis/source
  (`schema/technology.schema.json` `$defs.figure`). No such row in Neon today
  (checked), so latent — but it would 500 `compare_technologies`, search rows
  and markdown rendering for one bad figure.

**P2 — MCP interface (matches the test doc's §4 asks)**

- **F5.** No `offset`/`limit` on `get_document` (2.1M-char worst case).
- **F6.** No `compare_technologies` by id list; no `list_documents`; no
  `get_register_entry`.
- **F7.** Neon `hybrid_search` missing the SQLite boosts (technology 1.3,
  region sea 1.25 / apac 1.15) — the parity gap behind test-doc finding 9;
  also chunk rows hardcode `permitted_use: "unstated"` and equipment rows
  `spec_metrics: []` on the Neon path (`agent/pg.py:766, 802`).
- **F8.** REST contract mismatch: `/api/documents` with a restricted/unknown
  path returns **HTTP 200 with an error body** (`api.py:24-25, 45-49` wrap the
  truthy error dict with `_found`).
- **F9.** `list_*` rows never carry a gap/stub marker (projects, equipment,
  compare rows, vendors) — blank reads as "unknown", not "known gap".
- **F10.** openapi metadata stale: sector enum omits IDC and WWT
  (`api.py:156`), discipline enum omits ELE/CIV (`api.py:180`), search kind
  enum omits `project` (`api.py:179`).
- **F11.** `search` docstring never says a `discipline` filter silently drops
  all technology/vendor/equipment/project rows (guard at
  `agent/library.py:353-380`; same on Neon, `db/schema.sql:353-360`).

**P3 — hardening / hygiene**

- **F12.** `og.refresh_similarity` (a DELETE+INSERT function) is executable by
  `og_mcp_read` — Postgres grants EXECUTE to PUBLIC and `db/readonly.sql`
  never revokes it. The READ ONLY transaction blocks it in practice
  (`pg.py:87-89`), but defense-in-depth says `REVOKE EXECUTE ON FUNCTION
  og.refresh_similarity(int, double precision) FROM PUBLIC;`.
- **F13.** UI-host machine endpoints (`/api/stats`, `/api/version`) answer 401
  **without** the RFC 9728 `WWW-Authenticate` challenge (live-verified); the
  API host and container send it correctly.
- **F14.** Stdio mode never sets `EXCLUDE_RESTRICTED` (`server.py:88`,
  set only in HTTP mode at `server.py:487`) — a stdio session serves
  restricted text. Containers run HTTP, so exposure is local-dev only.
- **F15.** Stale docs/comments that will bite the next deployer:
  - `deploy/edge/wrangler.jsonc` comment lists retired secrets
    (`LIBRARY_API_KEY`, `INTERNAL_TOKENS`) and says "secrets come from the
    same keys as before".
  - `deploy/backend/wrangler.jsonc` comment references the deleted
    `src/authz.ts` and the retired sk-key model.
  - `deploy/frontend/src/index.ts:52,55` — issuer comment says
    `access-v2.hilir.app`, `APP_ORIGIN` comment says `techlib.hiril.app`.
  - HOSTING.md "How to publish" lists three `wrangler deploy` steps with no
    statement of which worker is actually live (see F16), and claims the
    machine-gate suite covers "JWT audience, estate key, header re-attachment"
    — it contains only 3 pure-function tests (challenge shape, audience parse)
    and currently fails (F3).
  - Count drift: register "~300" (`pg.py:868`) vs 406 actual vs "400+"
    (`server.py:305`); glossary "60" vs 70.
- **F16. Deploy footgun, same class as the one hilir-access closed
  2026-11-19.** Three wrangler configs each claim live custom domains:
  `edge` claims `techlib.hilir.app` + `techlib-api.hilir.app` (custom_domain),
  `frontend` claims the first, `backend` the second. Live probes show the
  **edge is not deployed** (PRM 404 on the UI host answers the UI handler's
  404 page): the split pair (`og-tech-library-ui`, `og-tech-library-api`) is
  what serves production. Deploying from `deploy/edge` as committed would also
  present a single-origin `AUDIENCE` (`"https://techlib.hilir.app"` only) to
  the API handler — direct MCP clients minted for the
  `techlib-api.hilir.app` resource would be rejected. Any of the three
  `npx wrangler deploy` commands is a live outage button. This is exactly the
  pattern hilir-access fixed in `9754bc2` (both configs claimed the domain;
  `npm run deploy` ran the legacy one).

## 3. Compliance with the 2026-11-20 access.hilir.app update

The update (hilir-access `9754bc2`, `222633a`): introspection hardened
(disabled-client rejection before secret compare, constant-time compare),
Cloudflare zone rate limit on `/api/v2-introspect` (50 req / 10 s per
colo+IP, 10 s block), hilir-auth 0.5.4 (RFC 6749 §5.2 code relay), admin
surface gates.

| Requirement | techlib status |
|---|---|
| Disabled clients rejected at Access before secret compare | **Compliant.** techlib sends correct Basic creds as the dedicated `techlib-api` client (`afRPzPMPgvTxROtxPODjFLeKCkbKJxEz`); if the client is ever disabled, the 401 fails closed in both the Worker (`verifyAgentKey`, hilir-auth) and the container (`agent/auth.py:114-160` — non-200 ⇒ None, negative-cached 60 s). |
| `/api/v2-introspect` rate limit (50 / 10 s per colo+IP) | **Compliant with one caveat.** Both verifiers cache verdicts ≤60 s by token hash; normal traffic is ~1-5 calls/min, ~100× under the ceiling. Caveat: a 429 is a non-200 ⇒ fail-closed ⇒ the key is locked out for the full 60 s negative-cache window (container) — acceptable, but worth a distinct log line so "key failed" vs "verifier rate-limited" is distinguishable (`agent/auth.py:141-149` swallows both silently). |
| hilir-auth 0.5.4 (§5.2 code relay) | **Not adopted** — all Workers pin `^0.5.3` (F2). STATUS.md says "VPS servers pick it up on rebuild"; the Workers do not rebuild, they deploy from this repo, so the bump is ours. |
| Admin gates / `/forgot` / landing hardening | Access-side only; no techlib action. |
| ROLES.md estate model (`catalog:read`, app role from `library.account`) | **Compliant** — frontend scopes `openid profile email offline_access catalog:read` match ROLES.md §clients; backend checks `REQUIRED_SCOPE`; container re-verifies (PyJWT + JWKS, EdDSA, both registered origins) and resolves roles from Neon. |

Auth architecture itself is sound: bearer-only container hop (no cookies,
no keys, no client-supplied DSN — the retired `x-user-store-dsn` is dropped
at the Worker, `deploy/backend/src/index.ts:155`), `x-api-key` re-attached as
Bearer after verification (Power Automate shape), PRM + RFC 6750 challenges on
the API door (live-verified), SSRF-pinned upstream hops in both Workers.

## 4. Proposed fixes (owner decision points marked ⚑)

**P1 — do now**
1. **Escape `result.error`** in the sign-in-failed page
   (`deploy/frontend/src/index.ts:255`) — HTML-escape, keep the code visible.
   Redeploy `og-tech-library-ui`, then re-run the live probe
   (`/auth/callback?error=<b>bold</b>` must render escaped).
2. **Bump `@tenunan-dev/hilir-auth` to `^0.5.4`** in
   `deploy/{frontend,backend,edge}/package.json` (+ locks), redeploy frontend
   (exchange path) and backend (uniformity). Post-deploy: docs/AUTH.md
   copy-paste probe block.
3. **Fix `deploy/backend` `npm test`** (extension-ful import or tsx) and add
   the missing pure tests HOSTING.md already claims (audience on the key path
   can stay live-verified per AUTH.md, but the challenge/`x-api-key`
   re-attachment shaping can be unit-tested by extracting it — it already is a
   function, `containerHeaders`).

**P2 — MCP surface (needs container rebuild + Neon schema apply)** ⚑
4. `get_document(path, offset=0, limit=20000)` — cap, return `total_chars` so
   clients can page; apply on both paths (`agent/library.py:677-691`,
   `agent/pg.py:532-552`) + server signature + docstring + REST.
5. `db_catalog`: state "all tables live in schema `og`", add one worked
   example (`select count(*) from og.source`), correct "~300" → 406.
6. Glossary: add PUE, WUE (the description names them; sector IDC is live),
   plus SRU/MERCON/DLE or trim the description to terms that exist. Fix the
   "60 entries" docstring. Data-only: `catalog/glossary.jsonl` + publish cycle
   (no deploy).
7. `compare_technologies` gains `technology_ids: list[str] | None` — when
   given, compare those cards by id (ordered); ignores sector/maturity. Plus
   make `_range` None-safe (F4).
8. **Neon parity**: add the 1.3 technology boost and region boosts into
   `og.hybrid_search` (`db/schema.sql:344-387`); apply via psql (schema rule),
   then re-run the `search("carbon capture amine")` probe — the amine card
   should surface top-3.
9. Gap surfacing: `projects.summary`/`equipment.summary`/`technologies.summary`
   add `"gaps": <n>` (or `"stub": true` when the record is a placeholder);
   vendor records: add a `stub` flag in the catalog record for
   `honeywell`, `honeywell-analytics` (and fix products where cheap).
   Data-only for vendors; code for the summaries.
10. New MCP tools (small): `list_documents(source_id=None, sector=None)` over
    `pg.document_index` (+ REST list mode), `get_register_entry(id)`.
11. `/api/documents` error path → 4xx status; openapi enums gain IDC, WWT,
    ELE, CIV, kind `project`; `search` docstring gains the discipline-filter
    caveat (F10, F11, F8).
12. ⚑ **Project data merges** (catalog work, owner-approved): merge PFLNG
    SATU ×3 → one record (status: operating — it has been onstream since
    2016); merge PFLNG DUA ×2 → one; Kasawari ×2 → one record carrying both
    the CCS project and the gas plant, one status, both technologies; fix the
    Kasawari milestone (FID, not start-up). Per
    [catalogue validation traps]: unique names, dollar years, plant links.

**P3 — hygiene**
13. UI-host `TOKEN_HELD` 401 gains the RFC 9728 challenge (mirror
    `bearerChallenge`, `deploy/frontend/src/index.ts:228-232`).
14. `REVOKE EXECUTE ON FUNCTION og.refresh_similarity(int, double precision)
    FROM PUBLIC;` in `db/readonly.sql` (run via `tools/load_postgres.py
    --grant-readonly` path or psql).
15. Stdio default `EXCLUDE_RESTRICTED = True` (`server.py:88`) —
    `--include-restricted` already exists for HTTP; give stdio the same flag.
16. Container-side introspection: log 429/rate-limit distinctly from a
    key-verify failure (`agent/auth.py:141-149`).
17. ⚑ **Deploy-footgun fix, mirroring hilir-access `9754bc2`**: decide the
    deploy story — either finish the Phase-4 consolidation (deploy edge,
    with `AUDIENCE` as the comma list, retire the split configs) or stay on
    the split pair and mark `deploy/edge` reference-only (remove its
    `routes` block). Update HOSTING.md's publish section to name the live
    workers and forbid the others; fix the stale comments (F15).
18. Count drift cleanups (register/glossary docstrings, HOSTING.md test claim).

## 5. Not tested here

- A live estate-key call (needs a key from the owner); the 60 s cache and
  fail-closed paths are code-verified only.
- `hybrid_search` through `sql_query` (needs a `vector(384)` argument —
  vector SQL from a text-only client).
- The full `deploy/edge` consolidation path (not deployed; config review only).
- Web UI pages (`agent/web.py` beyond `_account`/gate wiring) — out of scope
  per owner: techlib + techlib auth only.

## 6. Implementation status (same day — everything above is shipped)

Every P1/P2/P3 item in §4 was implemented, published and verified live; the
details and the deploy facts are in the [CHANGELOG 2026.11.20 entry](../CHANGELOG.md).

| Item | Status |
|---|---|
| F1 XSS escape + redeploy | shipped; live probe returns `&lt;b&gt;` |
| F2 hilir-auth 0.5.4 (3 Workers) | shipped; 0.5.4 installed, frontend+backend redeployed |
| F3 `deploy/backend npm test` | fixed; 5/5 pass, 2 new container-hop tests |
| F4 `_range` None-safe | fixed |
| F5 `get_document` offset/limit | shipped; live: `total_chars` 2,138,151, window 20,000 |
| F6 `technology_ids` / `list_documents` / `get_register_entry` | shipped; register fetch verified on a real id |
| F7 Neon boosts + row parity | applied live; amine query now returns technology cards first |
| F8 `/api/documents` 403 + list mode | shipped |
| F9 gap/stub markers | shipped; live: Bakun shows `stub: true`, compare rows carry `gaps` |
| F10 openapi enums | shipped |
| F11 search docstring caveat | shipped |
| F12 `refresh_similarity` revoke | applied live |
| F13 UI-host 401 challenge | shipped; live header present |
| F14 stdio restricted default | shipped (`EXCLUDE_RESTRICTED = True`) |
| F15 stale docs/comments | fixed (edge/backend configs, frontend comments, HOSTING.md, MCP.md) |
| F16 deploy footgun | `deploy/edge` routes removed; AUDIENCE corrected; HOSTING.md names the live pair |
| Data: PFLNG/Kasawari merges, milestone fix, vendor stubs, glossary terms | published to Neon (295 projects); live-verified |

One bug the audit itself introduced and the live probe caught: the first container
ship of `pg.document_row` raised `UnboundLocalError` because the new `offset`/`limit`
were assigned inside the nested `work()` (shadowing the parameters). Fixed by
resolving the window before `work()`; the corrected image (`118d022ee121`) is the one
running.
