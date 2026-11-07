# ROADMAP — the one combined plan

**Status: ACTIVE 2026-11-07.** This is the library's single plan. Everything new — content
expansion, fills, layers, features and the standing discovery effort — sequences through here so
the batches align: one register, one evidence standard, one publish path, one documentation pass.
Supersedes the standalone docs/DISCIPLINE_EXPANSION_PLAN.md (archived verbatim under
`docs/archive/2026-11-07_DISCIPLINE_EXPANSION_PLAN_v1.md`, decision #38).

Alignment rules (apply to every item below):

1. **Register first.** Every planned card/layer gets a register entry when planned, so the
   every-card-links-to-register tests stay the alignment gate.
2. **No invented figures.** Cards and equipment carry only figures with `basis` + `source`
   (decision #33 rule, extended to the discipline layer by decision #37).
3. **One evidence bar.** New sources are catalogued with access/verification; cards cite
   catalogued sources wherever possible (≤40% uncatalogued-citation cap, decision #21).
4. **One publish path.** Content batches run `tools/build.py` + pytest, then the Neon publish
   cycle, then deploy — per docs/DEVELOPMENT.md; auth/DNS/deploy changes stay owner-gated
   (decision #35).
5. **Docs in the same pass** (decision #36): STATUS, CHANGELOG, plan doc, decision file.

## 1. Standing effort — source discovery and document coverage

Unchanged as the standing main effort (decision #30); docs/SOURCE_DISCOVERY_PLAN.md remains its
execution detail. The roadmap folds in one targeted track:

| # | Item | Status |
|---|---|---|
| 1.1 | Five-channel discovery pipeline, triage per access class | standing |
| 1.2 | Doc-coverage targeting: the ~200 of 404 sources with zero collected documents, prioritised where cards cite them but no doc exists | open |
| 1.3 | Discipline sources: electrical/civil/C&I publishers and OEMs found while authoring round 2 | open |

## 2. Content expansion

### 2.1 Discipline layer (decision #37)

Batch 1 **done 2026-11-07** (commit `56cb1e0`): codes ELE + CIV added, 27 cards
(12 ELE, 10 CIV, 5 INS deepening), 4 sources (`selinc`, `hitachi-energy`, `iecex`, `hse-uk`),
tests 884 passed. Tracking tables for the 27 cards live in the archived plan; remaining work:

| # | Item | Status |
|---|---|---|
| 2.1a | Discipline vendor round: switchgear, e-houses, Ex equipment, modular fabricators, Malaysian/SEA EPC + IBS players into `catalog/vendors/` | open |
| 2.1b | Discipline round 2 cards on the owner's word: PIP (piping), HVAC, telecom/naval architecture, plus deepening PRC/MAT/HSE/DIG | proposed |
| 2.1c | Equipment classes for the discipline layer (switchgear, transformers, e-houses) — decision #33 pattern | owner gate |
| 2.1d | Neon publish cycle + deploy so batch 1 shows live | **done 2026-11-07** (Neon 326 cards/12,625 vectors; containers rebuilt via CI images + VPS compose; live checks green) |

### 2.2 Fill thin spots (no new pages needed)

| # | Item | Size | Status |
|---|---|---|---|
| 2.2a | Costs fill: only ~73 of 326 cards carry costs; staged by sector, dollar-year basis mandatory | L | open |
| 2.2b | Reference plants on cards without them (was 132 of 299 before batch 1; recount after batch 1) | M | open |
| 2.2c | Thin sectors: MAT 6, DIG 5, HSE 4, PRC 3 cards (INS lifted by batch 1) | M–L | open |
| 2.2d | Register entries still without cards (list_gaps), after batch-1 additions | M | open |

### 2.3 New content layers

| # | Item | Size | Status |
|---|---|---|---|
| 2.3a | **Standards registry** — API/ASME/ISO/NORSOK/IEC as first-class records linked to equipment + cards (30 standards-body sources already catalogued; batch 1 added IEC links on ELE cards) | M | open |
| 2.3b | Glossary of acronyms, seeded from card aliases | S | open |

## 3. Product features (on existing data)

| # | Item | Size | Status |
|---|---|---|---|
| 3.1 | **Compare view** — 2–4 technologies side by side (maturity/TRL/performance/costs/suppliers) at /compare with ?ids= deep links | S–M | **done 2026-11-07** |
| 3.2 | Export: CSV of technologies/vendors/sources/equipment at /export?kind= (XLSX + citation export follow) | S | **done 2026-11-07** (CSV) |
| 3.3 | Charts: sector/discipline and maturity distribution bars on the home page | S | **done 2026-11-07** |
| 3.4 | Discipline/region search filters on /search (backend already supported both; UI selects added) | S | **done 2026-11-07** |
| 3.5 | API reference page at /database/api, generated from openapi_spec (Swagger try-it-out is not possible cross-door with Access auth; reference + SQL console cover the need) | S | **done 2026-11-07** |
| 3.6 | Saved items (pin cards/vendors to account; userstore exists) | M | open |
| 3.7 | "Ask the library" — RAG web endpoint over the indexed chunks | L | owner gate (key routing) |

## 4. Sequencing

Recommended order for the next sessions, each a self-contained batch (build → tests → docs →
commit; Neon publish + deploy bundled when the owner says go):

1. **Publish batch 1** (2.1d) — get the 27 discipline cards + web changes live.
2. **Quick wins** — 3.1 compare, 3.3 charts, 3.5 playground, 3.4 filters, 3.2 export.
3. **Vendor round** (2.1a) — aligns with the card supplier lists batch 1 introduced.
4. **Fills** (2.2b reference plants, then 2.2a costs staged by sector) — every new card from any
   track joins the same fill backlog, so costs/reference-plant sweeps cover discipline cards too.
5. **Layers** (2.3b glossary → 2.3a standards registry) — glossary seeds cheaply from the now
   larger alias pool; standards registry builds on the IEC links batch 1 started.
6. **Round 2 disciplines** (2.1b) and remaining sectors (2.2c) on the owner's word.

## 5. Where things live

| Thing | File |
|---|---|
| This plan (single source) | docs/ROADMAP.md |
| Source discovery execution | docs/SOURCE_DISCOVERY_PLAN.md (decision #30) |
| Equipment layer rules | decision #33 |
| Publish/runbook | docs/DEVELOPMENT.md |
| Card tracking (batch 1) | docs/archive/2026-11-07_DISCIPLINE_EXPANSION_PLAN_v1.md |
| Decisions | docs/DECISIONS.md |
