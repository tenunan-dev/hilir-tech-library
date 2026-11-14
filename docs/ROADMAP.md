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
| 1.2 | Doc-coverage targeting: **27 sources hold all 289 corpus documents**; 483 of 510 catalogued sources have none (measured 2026-11-14 — the earlier "205 of 404 sources have docs" figure counted citations, not documents, and read as far better coverage than exists). The 28-arXiv corpus was already converted; its summaries were raw stubs and are now authored (2026-11-14) | open | **re-measured 2026-11-14**; /sources now shows the per-source count and a coverage filter, so the hole is visible on the site |
| 1.3 | Discipline sources: electrical/civil/C&I publishers and OEMs found while authoring round 2 | open |

## 2. Content expansion

### 2.1 Discipline layer (decision #37)

Batch 1 **done 2026-11-07** (commit `56cb1e0`): codes ELE + CIV added, 27 cards
(12 ELE, 10 CIV, 5 INS deepening), 4 sources (`selinc`, `hitachi-energy`, `iecex`, `hse-uk`),
tests 884 passed. Tracking tables for the 27 cards live in the archived plan; remaining work:

| # | Item | Status |
|---|---|---|
| 2.1a | Discipline vendor round into `catalog/vendors/` | **done 2026-11-07, extended 2026-11-11** (15 added 2026-11-07; 21 more 2026-11-11: Anvil/ASC, BK Vibro, Carboline, Carpenter & Paterson, CCC, Chromalox, Aker Solutions, DEHN, Eurecat, Heerema, Hempel, Honeywell Analytics, IBM, IFS, KROHNE, Lisega, MSA Safety, Nalco Water, Nidec, Seatrium, WEG; 457 total; queue largely stale — short-form names need aliases, 4 unfetched vendors Dräger/Furse/Kiewit/LS Cable remain) |
| 2.1b | Discipline round 2 cards on the owner's word: PIP (piping), HVAC, telecom/naval architecture, plus deepening PRC/MAT/HSE/DIG | proposed |
| 2.1c | Equipment classes for the discipline layer (switchgear, transformers, e-houses) — decision #33 pattern | owner gate |
| 2.1d | Neon publish cycle + deploy so batch 1 shows live | **done 2026-11-07** (Neon 326 cards/12,625 vectors; containers rebuilt via CI images + VPS compose; live checks green) |

### 2.2 Fill thin spots (no new pages needed)

| # | Item | Size | Status |
|---|---|---|---|
| 2.2a | Costs fill: staged by sector, dollar-year basis mandatory, every figure evidence-fetched. **2026-11-08 pass 1 (CCS + H2, 10 cards)**: IEA figures on 5 CCS-chain cards and 5 H2 cards. **2026-11-14 pass 2 (15 cards)**: 11 ELE figures reusing the owner-accepted export-price basis already on the equipment records, plus 13 EPA fact-sheet figures across 8 WWT cards. Costs gaps 271 → 275 (4 closed, 10 new IDC cards and 29 CIV gaps recorded) | L | **two passes done**; 275 cards still carry no cost figure |
| 2.2b | Reference plants / verified figures on cards without them | M | **partial 2026-11-07** (first verified figures on ele-transformers and civ-floating-structures-fpso from cited vendor pages; systematic sweep continues) |
| 2.2c | Thin sectors: PRC 5, MAT 8, HSE 6, DIG 7 cards after the 2026-11-08 batch (OTS, catalyst management, corrosion monitoring, CUI, methane/LDAR, flare recovery, CMMS, cloud SCADA) | M–L | **batch done 2026-11-08**; further deepening open |
| 2.2d | Register entries without cards (list_gaps) | M | **open again 2026-11-14** — the 2026-11-08 "closed, 0 of 333" claim did not survive the IDC sector: 17 IDC entries were uncovered, 3 of them because duplicate register rows had been added instead of linking the originals. Duplicates removed, 10 cards authored, **7 remain** (fuel-cell power, district heating tie-ins, battery load smoothing, modular data halls, commissioning and IST, DCIM and digital twins, leak detection) — each needs a source read before a card can be written |

### 2.3 New content layers

| # | Item | Size | Status |
|---|---|---|---|
| 2.3a | **Standards registry** — 27 seeded records (`catalog/standards.jsonl`) at /standards, linked to cards + equipment, with integrity tests | M | **done 2026-11-08** |
| 2.3b | Glossary: 60 authored term/expansion entries with related-card links, /glossary page | S | **done 2026-11-07** |

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
