# Source discovery runbook (v3)

Standing main effort (owner decision #30, 2026-10-29; v2 autonomous sequencing 2026-10-29;
**v3 2026-10-29: rewritten as a precise runbook — any agent with zero session context can
execute it**). Goal: find, verify, register and properly categorize every source and
vendor the library should hold — the library covers technologies AND who can supply,
build, construct, operate and maintain them.

If anything here conflicts with [AGENTS.md](../AGENTS.md), AGENTS.md wins. Stop and ask
the owner only for items in §9.

## 1. Entry protocol (every session, every agent)

1. Read [AGENTS.md](../AGENTS.md) (repo rules — binding).
2. Read `research/source-discovery/state.json` (the sequencer — what is done/queued/blocked).
3. Read `research/source-discovery/candidates.jsonl` (the queue — one JSON object per line).
4. Drain the owner inbox `research/source-discovery/inbox.local.txt` (gitignored): append
   each non-comment line as a candidate row (channel `owner-inbox`, status `queued`),
   then clear the inbox file's used lines.
5. Pick the first block with status `queued` in `state.json` (order in the file is the
   default order; any `blocked-temporary` whose `retry_after` condition is now met may be
   taken first). Set it to `running`, save state.json.
6. Execute that block per §5. After every outcome — done, partial or failed — update
   state.json (§7) and continue with the next open block. Do not stop between blocks.
7. Never take a block listed in `parked_owner`. Never delete state/candidate rows.

Session boundary rule: if gates fail twice on the same edit, stop that block, mark it
`blocked-temporary` with the error text, and move on.

## 2. The two driving files

**`research/source-discovery/state.json`** — sequencer. Shape:

```json
{"updated": "YYYY-MM-DD", "blocks": [
  {"id": "A2", "name": "...", "status": "queued|running|done|partial|blocked-temporary|blocked-owner",
   "runs": 0, "retries": 0, "retry_after": "...condition...", "note": "free text, last outcome"}],
 "parked_owner": ["..."]}
```

- `runs` +1 every attempt. `note` always carries the latest outcome (counts, error text).
- `blocked-temporary` requires `retry_after` (e.g. "after 3 other blocks", "next session",
  "when Docker is up"). When the condition is met at step 1.5, the item is runnable again.
- Re-sequencing is allowed and expected: reorder, split, or add blocks; keep ids stable.

**`research/source-discovery/candidates.jsonl`** — queue. One object per line; fields:

```json
{"name": "...", "url": "https://... | null", "channel": "citation-mining|citation-graph|vendor-provenance|event-sweep|owner-inbox",
 "first_seen": "YYYY-MM-DD", "kind": "source|vendor", "status": "queued|registered|rejected|blocked-owner|blocked-temporary",
 "registered_as": "catalog/sources/<id>.json | catalog/vendors/<id>.json | null",
 "note": "why queued / outcome / evidence"}
```

Prefer appending over editing; edit a row only to change `status`/`registered_as`/`note`.

## 3. Standing rules (bind every block)

1. **Fetch ladder** for evidence: `WebFetch` → zai `webReader` MCP → `WebSearch`
   (search-verified facts must say so in the record's sources note). Known gotchas:
   uspeglobal.com and gasturbineworld.com reject plain WebFetch (reader works);
   sinopecgroup.com connect-times out from this Mac (search-verify); MDPI/OSTI/NREL/PNNL
   domains are blocked from this Mac — use the mirrors in [LOGIN_REQUIRED.md](LOGIN_REQUIRED.md)
   and `docs/HUMAN_ACTION_KIV.md` routes instead.
2. **Schema facts.** Source record required fields: `id, name, url, source_type, sectors,
   disciplines, publisher_org, regions, access, licence, reuse_level, quality_tier,
   verification, last_verified`. Enums — source_type: standards-body | licensor |
   oem-supplier | epc-contractor | journal | agency-data | association | conference |
   patents | trade-media | research-institute; access: open | free-registration |
   paywalled | mixed; reuse_level: full-text-open | full-text-restricted | summary-only |
   catalog-only; update_frequency: daily | weekly | monthly | quarterly | annual |
   irregular; automated_access: allowed | prohibited | unstated; permitted_use: any |
   internal-organisation | personal-non-commercial | none | unstated; sectors: UPS MID
   GAS REF PCH PWR H2 CCS; disciplines: PRC ROT INS MAT HSE DIG; regions: global apac
   sea me eu na latam af; quality_tier 1–3 (1 standards/peer-review, 2 agency/licensor/
   association, 3 marketing/trade). Vendor required: `id, name, country, roles,
   description, technologies, sources, last_reviewed`; roles: oem licensor packager epc
   developer operator rental service supplier integrator (no `contractor`/`producer`).
   id = kebab-case matching the filename. `technologies` items must exist as card ids.
3. **Traps already hit** (do not repeat): card `suppliers[]` allows only
   name/product/source_id/url; gap `where[]` needs `hint` (+url/source_id), never `note`;
   heredoc python breaks on apostrophes — write scripts to a temp file instead; never
   pipe `build.py` through `tail` (masks non-zero exit); `library.py build` clears the
   vectors table (embed AFTER build); loader rejects NUL bytes; vendor `name_key()`
   truncates at " (" so parenthesized sub-brand names collide with parents.
4. **Verification evidence** goes in two places: the record (`notes`, `verification`,
   `last_verified`) and `tools/verification/log.jsonl` as
   `{"id": ..., "evidence": "<url>", "finding": "<what the page says, with date>"}`.
5. **Gates after every batch:** `python tools/build.py` (must print "N records valid …")
   and `pytest -q tests` (must pass). Both green before commit. Commit and push after
   every block or batch; assume concurrent sessions — `git fetch` first, stage ONLY your
   files, never amend.
6. **Access-class collection** (AGENTS.md rules 3–4, 7): only verified records get
   collectors; paywalled → record-only + manual extracts from an owner-held copy;
   bot-blocked → browser/manual inbox; blocked domains → compliant mirrors. Never guess
   content that was not fetched.
7. **Every new corpus document needs a hand-written `summary`** in its front matter.
8. Mimosa commit/push warnings about `deploy/cloudflare/src/index.ts` (SSRF),
   `agent/library.py` search (SQL injection), `tools/load_postgres.py` (SQL) are
   ADJUDICATED FALSE POSITIVES in warn mode — proceed; report any NEW finding to the owner.

## 4. Worker contract (flash-max subagents)

Use for mechanical multi-file edits and bulk site reads. Dispatch **serially** (one at a
time — parallel dispatches hit the user/model concurrency limit). Supervisor (you)
researches, writes the prompt, reviews the full diff, runs gates, commits.

Prompt template (fill in, keep the constraints):

```
Task: <exact edits or reads, file by file>
Rules: schema fields/enums that apply (copy from §3.2); do not touch generated files
(catalog/catalog.jsonl, catalog/index/*, build/); read-only fetches only via the tool
named below; report every file you changed.
For site reads: fetch <url>; extract <facts wanted>; return as a bullet list with the URL
for each fact. If a fetch fails, report the URL and error — do NOT guess content.
For large files: use grep/rg with offset+limit — do not read whole files.
```

Acceptance: diff shows only intended changes; gates green. If a worker output fails
review, re-dispatch with the specific correction; if it fails twice, do the batch inline.

## 5. Block procedures

### A2 — tools/discover_sources.py (channel 1 script)

1. Write `tools/discover_sources.py`: scan `corpus/**/*.md`, `catalog/technologies/*.json`
   (`sources[].url`, `gaps[].where[].hint`) and `catalog/index/gaps.md`; extract
   (a) all http(s) URLs, (b) capitalized org-like phrases from hints; normalise
   (lowercase, strip punctuation); diff against catalog ids/names/publisher_org/URL
   domains; emit new candidates as §2 JSONL lines to stdout.
2. Add a small offline test (`tests/test_discover_sources.py`) with a fixture proving
   dedup and URL-domain matching.
3. Run: `.venv/bin/python tools/discover_sources.py >> research/source-discovery/candidates.jsonl`
   after de-duplicating against existing queue names.
4. Gates; commit script + test + queue.
Done = script + test committed, run output appended, count in state note.
Fail = none expected; if corpus scan crashes on an odd file, skip that file with a note.

### A3 — triage + register queued candidates (repeat until queue empty)

Batch = 8 `queued` rows. For each row, in order:

1. Dedup: search `catalog/sources/` and `catalog/vendors/` by name/url/alias (grep). Hit →
   status `rejected`, note `duplicate of <id>`.
2. Classify: paywalled and the value is the data itself (subscription databases,
   Nelson-Farrar, IHS PEP, Wood Mackenzie) → `blocked-owner` with note; everything else proceeds.
3. Evidence: fetch ladder (§3.1). Record what the page says (evidence URL + date).
4. Write the record per §3.2 (mirror an existing record of the same type, e.g.
   `catalog/sources/ghgt.json` for conferences, `catalog/vendors/licella.json` for vendors).
   Choose `sectors`/`disciplines` from the pages actually read; `quality_tier` per §3.2.
5. Set candidate row `status: registered`, `registered_as: <path>`.
6. After the batch: gates, commit ("Sources: <ids> registered" / "Vendors: …"),
   push, update state note with counts. Continue with the next batch.
Done = no `queued` rows remain. Fail = a fetch that fails the whole ladder → row
`blocked-temporary`, `retry_after: next session`; continue the batch.

### A4 — vendor categories field + backfill

1. Edit `schema/vendor.schema.json`: add optional property `categories`, array of enum
   strings, vocab: `plant-epc, offshore-epc, shipyard, equipment-oem, process-licensor,
   operator, materials-supplier, oilfield-service, power-rental, engineering-consultancy,
   fabrication, utility`.
2. Extend `tests/test_vendors.py`: categories, when present, must be within the enum.
3. Rule-based backfill script `tools/categorise_vendors.py`: map roles+products+description
   keywords to categories (e.g. epc + "refinery/petrochemical/LNG plant" → plant-epc;
   oem + "shipyard/LNG carrier/FPSO hull" → shipyard; rental + "power" → power-rental).
   Writes `categories` into every vendor JSON that has none.
4. Flash sweep (§4) to review/fix wrong rule assignments (all 390 records, 3 batches).
5. Gates; commit.
Done = every vendor record carries valid categories; tests green.

### A5 — source miscategorization audit

1. Script or flash pass over `catalog/sources/*.json`: flag (a) `source_type` inconsistent
   with publisher_org/name (e.g. a standards body typed `association`), (b) empty or
   clearly wrong `sectors`/`regions`, (c) conference records whose `url` is a dead event page.
2. Fix by editing the record (keep `notes` trail: "re-typed X→Y, evidence …"). No
   verification claims without a fetched page.
3. Gates; commit; state note lists the changes.
Done = sweep report (counts per fix type) in state note.

### A6 — verification sweep (193 unverified records)

Batch = 10 records from `catalog/sources/*.json` where `verification == "unverified"`:

1. Fetch `url` (ladder §3.1). If reachable: set `verification: verified`, `last_verified`
   today; fill `access`, `automated_access`, `permitted_use` from what the page/terms say;
   append the evidence line to `tools/verification/log.jsonl` (§3.4).
2. If terms page needs a real browser (Cloudflare wall etc.): leave unverified, add note
   `terms bot-walled, needs browser` — these feed the parked list, not a failure.
3. Dead domain → note it; if a replacement domain is found by search, fix the URL with
   evidence; else note `domain dead`.
4. Gates per 2 batches; commit ("Verification: N records verified …").
Done = unverified count < 30 or all remaining are bot-walled/dead (listed in note).
Fail rows → `blocked-temporary` inside the candidate queue only if they were candidates.

### A7 — vendor-provenance crawl (channel 3)

1. Background Bash loop over vendor URLs from `catalog/vendors.jsonl`, contractor cohort
   first (wison, sinopec, sinopec-engineering, samsung-engineering, hyundai-ec,
   sk-ecoplant, daelim, gs-ec, kepco-ec, doosan-enerbility, jgc, toyo, chiyoda, uspe-global):
   fetch `<url>` + common subpages (`/resources`, `/whitepapers`, `/standards`,
   `/certifications`, `/news`) via the ladder; save raw text under
   `research/provenance/<vendor-id>.txt` (gitignored scratch).
2. Extract mentioned standards bodies, associations, journals, regulators → append
   candidates (channel `vendor-provenance`).
3. A3 consumes them next time it runs.
Done = cohort crawled; candidates appended; crawl summary (hits/blocks) in state note.

### A8 — OpenAlex venue sweep (channel 2)

1. Take ~50 document titles from `corpus/manifest.jsonl`.
2. For each: `curl -s "https://api.openalex.org/works?filter=title.search:<title>&per-page=1"`
   → take `id`; then `curl -s "https://api.openalex.org/works?filter=cites:<id>&per-page=200"`
   → group cited works by `primary_location.source.display_name`.
3. Flag venues cited ≥3 times (across the doc set) that are absent from the catalog →
   append candidates (channel `citation-graph`).
4. Rate-limit friendly (≥1 req/s sleep); background task; results to
   `research/source-discovery/openalex-venues.txt` (scratch, gitignored) + queue rows.
Done = 50 docs processed; venue table in state note.

### A9 — event + standards sweep (channel 4)

1. Search energy-event calendars (Gastech/ADIPEC/Offshore Technology Conference/EGU/SEA
   events) for proceedings-publishing conferences missing from the catalog.
2. Search standards-body catalogues already catalogued (API, ASME, ASTM, ISO/IEC, SIRIM,
   PETRONAS PTS, SKK Migas) for sibling programmes worth their own record.
3. Append candidates (channel `event-sweep`). A3 consumes.
Done = one full pass; candidates appended.

### A10 — EUBCE proceedings batch 1

1. From eubce.com proceedings (open access), pick papers matching the bioenergy cards:
   `ccs-beccs, ccs-biochar, h2-pyrolysis-htl, h2-cellulosic-ethanol, pwr-biomass-waste-to-energy`.
2. Download PDFs to `corpus/_inbox/eubce/` with `.url` sidecars.
3. Convert + intake: `.venv/bin/python collectors/collect.py --manual --source eubce`
   (or place converted markdown and register in the manifest per MAINTAINER_MANUAL).
4. Write a hand-made `summary` per document (§3.7).
5. Gates; commit corpus + summaries.
Done = 10–20 documents in corpus/ with summaries; counts in state note.

### A11 — vendor cohorts

Cohorts in order: (1) Western EPC gaps — Fluor, Wood (energy arm), Petrofac, Worley,
Bechtel, McDermott; (2) NOC engineering arms — CNOOC (engineering), CPECC, PetroChina
engineering; (3) SEA contractors — Toyo-Kalimantan, Tripatra, Senko/Saipem Indonesia
KG, PTT EN, PTSC (verify which exist independently); (4) alias fixes —
hitachi-zosen-inova → note Kanadevia Inova rename (2025) in aliases/notes.
Per company: dedup (§5 A3.1), fetch ladder for evidence, register per §3.2, queue row
update, gates+commit per cohort.
Done = all four sub-cohorts registered or explicitly rejected with reasons.

### A12 — publish cycle

Preconditions: 2+ content blocks landed since last publish; Docker running
(`docker info` OK) for deploy; else mark `blocked-temporary`, retry_when Docker up.

```
python tools/build.py
python agent/library.py build
OMP_NUM_THREADS=4 python agent/embed.py          # up to ~2 h; run in background
# after embed finishes:
export DATABASE_URL=$(grep '^DATABASE_URL_UNPOOLED' .env.local | cut -d= -f2- | tr -d '"')
python tools/load_postgres.py --embeddings sqlite --include-restricted
cd deploy/cloudflare && npx wrangler deploy      # ~25 min container upload; do NOT pipe or kill
```

Verify live: `curl -s https://techlib.hilir.app/api/stats` (compare to local counts) and
`/health`. Update STATUS "Where things run"/counts and CHANGELOG if release-worthy.
Done = /api/stats matches local; deploy id + counts in state note.

## 6. Categorization reference (why A4/A5 exist)

- Sources: 11 `source_type` enums, distribution healthy (2026-10-29: agency-data 64,
  oem-supplier 49, research-institute 47, journal 39, association 37, licensor 36,
  standards-body 28, trade-media 22, conference 20, epc-contractor 17, patents 12);
  193/371 unverified → A6.
- Vendors: roles describe activities (oem 177, operator 72, developer 71, supplier 65,
  service 48, licensor 32, epc 28, packager 13, integrator 9, rental 5), not company
  kind — Samsung Heavy (shipyard) vs Samsung Engineering (plant EPC) → A4 categories.
- Equipment: cards carry `key_equipment` per step; a generated
  `catalog/index/equipment.md` view is PROPOSED, not approved — owner decides (§9).

## 7. State update protocol (after every block outcome)

1. `runs` +1; set `status`: `done` (criteria met), `partial` (some criteria, note says
   what remains — partial blocks stay runnable), `blocked-temporary` (transient: site,
   provider, Docker; write `retry_after` + error in note), `blocked-owner` (§9 territory).
2. `note` = one-line outcome with counts/dates/errors. `updated` = today.
3. Commit state.json + candidates.jsonl together with the work they describe.
4. Pick next block (§1.5). Continue. Do not end a session with a block left `running` —
   resolve it or mark `blocked-temporary` first.

## 8. Candidate outcome rules

- `registered` — record exists, gates green.
- `rejected` — duplicate (`duplicate of <id>`), out of scope (no energy/O&G relevance,
  say why), or dead with no successor.
- `blocked-owner` — needs money or an owner account (paid databases, subscriptions).
- `blocked-temporary` — fetch failed the whole ladder; retry next session (max 3 retries,
  then `rejected` with the error as reason).

## 9. Parked: owner-only (never taken by agents)

Purchases and subscriptions (Gas Turbine World handbook, Nelson-Farrar, IHS PEP, Wood
Mackenzie); human-browser items in `docs/HUMAN_ACTION_KIV.md` (18 bot-walled terms pages,
PetroWiki/OnePetro); the equipment-index decision (§6); future inbox drops (continuous);
infra owner items (auto-deploy Cloudflare token, Dataverse import, LIBRARY_USERS first
account, claude.ai connector, Copilot Studio connect).

## 10. Session log

Newest first.

- **2026-10-29 (v3):** Rewritten as a precise runbook per owner direction: entry
  protocol, per-block procedures with exact commands, schema/enum reference, worker
  contract, state and queue protocols, outcome rules, parked list. No scope change.
- **2026-10-29 (v2):** Autonomous multi-agent sequencing; A1 done (43 candidates);
  categorization stream (A4–A6); queue + state committed.
- **2026-10-29:** Plan created; eubce, gas-turbine-world, irecruit, uspe-global
  registered; CN then KR/JP contractor cohorts (vendors → 390).
