# Gap closure plan

Written 2026-10-27 after the gap review. Target: the **1,118 open gaps on 297 cards**
(`catalog/index/gaps.md`) plus the adjacent registers that close card fields: the 10
date-driven status re-checks, 2 conflicting-source gaps, and the vendor coverage queue that
feeds `suppliers` gaps. Execution is designed for **GLM-5.3-Flash workers** ("flash",
dispatched with the Agent tool, subagent type `flash-max`) doing mechanical work under a
supervising session that does the research, reviews every diff and runs the gates.

Current state (verified this session): 354 catalog records, 174 corpus documents, 299 cards,
71 vendors, `tools/build.py` clean, `pytest -q tests` 479 passed / 1 skipped.

## 1. Scope — the numbers the plan attacks

By reason code:

| Reason | Count | Meaning for method |
| --- | --- | --- |
| not_in_sources_read | 848 | Not found yet — corpus mining first, then web sweep |
| general_knowledge_only | 231 | Card text rests on general practice (230 of them `process`) — needs a citable authority |
| source_unreachable | 15 | Fetch failed — browser/computer-use retry list |
| paid_source | 12 | Owner decision only; leave |
| status_unchecked | 10 | Date-driven re-checks; 9 due now, Stratos due after Jan 2027 |
| conflicting_sources | 2 | Adjudicate by reading both sources |

By field type: costs 262, process 235, reference_plants 222, trl 202, performance 150,
suppliers 29, other 9, status 9 (plus the 10 re-checks above).

Sector order for sweeps (by open gaps): UPS 239, PWR 130, PCH 107, CCS 93, REF 90, GAS 89,
MID 88, H2 85, ROT 61, MAT 33, INS 28, DIG 25, HSE 18, LNG 17, PRC 15.

## 2. Ground rules (non-negotiable, from AGENTS.md)

1. **Never invent** (rule 5). Every figure added to a card needs the URL it came from and the
   date read; costs need dollar year and basis; no dollar year → basis must say "dollar year
   not stated". If it cannot be found, the gap stays (or its reason/where/action is updated).
2. **Closing a gap** = remove the entry from the card's `gaps[]` AND add the fact with its
   source to the right card field (`figures`, `reference_plants`, `suppliers`, `status`,
   `maturity`…), or, when the item is resolved as "no better source exists", rewrite the gap's
   `where`/`action` to reflect the new best lead. A gap is never deleted without its fact.
3. **Card rules** (rule 9): register-matching names, sector codes, `source_id` only when the
   record exists in `catalog/sources/` (bare `url` citations are allowed and are how the ~100
   uncatalogued citations are recorded), Wikipedia citations must say "secondary" in the note.
4. **Generated files are never hand-edited** (rule 6): only `catalog/technologies/*.json`,
   `catalog/vendors/*.json` and `catalog/sources/*.json` are edited; `catalog/catalog.jsonl`,
   `catalog/index/*` and `build/` come from the tools.
5. **Gates after every batch**: `python tools/build.py` (must print records valid) and
   `pytest -q tests` (must pass). Commit per batch; fetch before push; never amend.
6. **New corpus documents** go through `collect.py --manual` (or the inbox) and need a
   hand-written `summary` before commit (rule 8). Strip NUL/control bytes from any extracted
   text before ingest — the Postgres loader rejects them.
7. **Acquisition is unrestricted, inclusion is manual** (decision #29): fetch and store freely,
   record licence/access labels truthfully, never simulate unfetchable content (rule 7).
8. **Mimosa gate runs in warn mode**: expect false-positive warnings on commits; adjudicate in
   the report, do not rewrite working SQL to please it.
9. Secrets (API key, Cloudflare token, Neon DSN) never enter the repo, worksheets or reports.

## 3. Method toolbox — every method, in escalation order

Per gap, try the cheapest method that can plausibly answer, then escalate. Methods M1–M2 are
offline; M3–M7 are plain HTTP (fail fast, record the block); M8–M9 need the Mac desktop;
M10+ are processing rather than fetching.

- **M1 — Local corpus mining.** `rg -i` over `corpus/**/*.md` (documents are markdown with
  front matter; filenames carry a content hash). The 2026-10-25 sweep was collected
  specifically for gap figures — most Wave-1 targets are already on disk. Flash workers can
  do this alone: read the doc, quote the passage, extract the figure.
- **M2 — Semantic mining on the local index / Neon.** `hybrid_search()` in Postgres (Neon,
  read-only role) and the local SQLite index find passages by meaning when keywords fail
  (e.g. "reboiler duty" phrased as "stripper steam draw"). Query embeddings exist only
  Mac-side (threads=4 fastembed). Use for cross-mapping gap items to corpus passages at wave
  start, not per gap.
- **M3 — WebFetch / WebSearch.** Default for anything not on disk. Works for most publisher,
  OEM, standards-body and government pages from this Mac.
- **M4 — Mirror route for blocked hosts.** osti.gov, nrel.gov, pnnl.gov and mdpi.com block
  this Mac outright. Equivalents that answer: netl.doe.gov, energy.gov, hydrogen.energy.gov,
  rosap, Europe-PMC REST. Record the block and use the mirror; do not retry the blocked host.
- **M5 — zai web-reader MCP** (`web_reader`). Second fetcher with a different engine;
  sometimes passes where WebFetch gets a JS challenge.
- **M6 — web-search-agent** (workspace agent, `.zcode/agents/` with the `og-tech.md` search
  module). Fan out per-sector evidence hunts; it returns sourced candidates that the
  supervisor still verifies by reading.
- **M7 — Wayback Machine.** Dead, moved or paywalled-since pages (proven: APR Energy 522).
  Cite the original URL + capture date.
- **M8 — Browser use** (`browser-use:control-browser` skill). JS-rendered apps, anti-bot
  pages, scroll-to-load lists, charts as images. Includes the **Scribd recipe** (proven
  2026-10-27): open the document page in the browser → read the per-page JSONP `contentUrl`
  assets → fetch text layer + page JPEGs from the scribdassets CDN → assemble PDF. Save
  everything to `corpus/_inbox/<source-id>/` with `.url` sidecars. MDPI metadata via OAI-PMH
  (`https://oai.mdpi.com/oai/oai2.php`) belongs to this tier too.
- **M9 — Computer use** (`computer-use` skill). The full desktop, for what a headless browser
  cannot do: viewer-only PDFs (print-to-PDF), interactive configurators/catalogues, pages that
  fingerprint headless browsers, and anything needing a real user session the owner has
  logged in. Same inbox path. OCR of scanned results with Apple Vision (pyobjc, en-US+id-ID,
  ~0.2 s/page warm) is the proven companion step in this tier.
- **M10 — Manual inbox ingestion.** `collect.py --manual` for everything collected by M8/M9;
  hand-written `summary` per document; manifest resync.
- **M11 — Catalog binding.** `tools/research_to_catalog.py` + the catalog skills
  (`catalog-plan`, `catalog-add-items`, …) turn repeated bare-URL citations into proper
  source records, which also strengthens the graph citation test.
- **M12 — Flash workers.** `flash-max` subagents for card/vendor edits, extraction tables and
  sweeps over worksheets. Supervisor reviews every diff (established pattern: mechanical
  edits by flash, reviewed as diffs, committed by the supervisor).
- **M13 — Publish ops** (supervisor only, end of programme or per milestone): `tools/build.py`
  → `agent/library.py build` → `agent/embed.py` (threads=4; hours, run chained in background)
  → `tools/load_postgres.py --embeddings sqlite --include-restricted` with the unpooled owner
  DSN → `npx wrangler deploy` from `deploy/cloudflare` (Docker must be running). See
  docs/POSTGRES.md and docs/HOSTING.md.

Escalation: M1 → M2 → M3 → M4/M5 (parallel) → M6 → M7 → M8 → M9 → owner (only `paid_source`
items reach the owner tier).

## 4. Waves

### Wave 0 — Preparation (supervisor, ~30 min, offline)

Generate the worksheet set under `research/gap-closure/` (gitignored scratch): one
`batches/<sector>.md` listing that sector's open gaps (card id, gap item, field, reason,
current where/action) and one `evidence/` directory for evidence packs. Freeze the counts in
this plan as the baseline. No card edits.

### Wave 1 — Mine the collected corpus into cards (offline, flash-heavy, highest leverage)

STATUS names this the highest-leverage step: ~20 documents collected 2026-10-25 were aimed at
specific gaps and none of their figures are on cards yet. Named extractions:

| Gap target (card) | Corpus document(s) |
| --- | --- |
| Amine solvent regeneration energy (GJ/t CO2) — extract stripper steam draw from stream tables | `corpus/netl/cost-and-performance-baseline-fossil-energy-plants-vol1-rev4-2022-*` |
| CO2 transport and storage costs (pipeline, shipping, injection) across CCS/GAS cards | `corpus/netl/qgess-carbon-dioxide-transport-and-storage-costs-in-netl-studies-2024-*` |
| CO2-EOR utilisation factors and incremental recovery | `corpus/netl/netl-carbon-dioxide-enhanced-oil-recovery-primer-*`, `netl-next-generation-co2-eor-*` |
| Capture cost benchmarks (industrial sources, NGCC retrofit) | `corpus/netl/cost-of-capturing-co2-from-industrial-sources-2022-*`, `cost-and-performance-of-retrofitting-ngcc-units-*`, `examination-of-factors-affecting-*` |
| CCS facility list / operating BECCS + reference plants | `corpus/global-ccs-institute/global-status-of-ccs-2026*` |
| CO2 shipping costs and specs | `corpus/global-ccs-institute/needs-opportunities-prospects-co2-shipping-in-ccs-projects-2025*` |
| LDAR / methane abatement costs | `corpus/iea-methane-tracker/*` (2025 + documentation) |
| P&A and decommissioning cost benchmarks | `corpus/uk-nsta/*` (2026 update first, 2020 estimate for comparison) |
| Polymer flood results (light oil, high salinity HPAM) | `corpus/lemigas-scog/scog-polymer-*`, `rheological-screening-of-hpam-*`, `scog-microemulsion-flooding-*` |
| H2 production/liquefaction/delivery costs, PEM electrolysis today | `corpus/doe-hfto/*` (program records, Hydrogen Shot assessment) |
| Salt-cavern H2 storage costs — locate by `rg -i "salt cavern|solution-mined"` corpus-wide | to be located (M1) |

Then the generic pass: for every remaining `reference_plants` and `trl` gap, ripgrep the
corpus for the technology name and aliases (all 306 register entries are covered by cards, so
aliases are on the cards). Anything not answered locally falls through to Wave 3.

Flash contract per extraction batch: input = card file(s) + document path(s); output = figure
rows with value/unit/dollar year/basis/quote + the edited card; gates = build + pytest. The
supervisor spot-checks quotes against the documents before commit.

### Wave 2 — Quick wins on the network (small, supervisor + web tools)

The 9 due status re-checks and 2 conflicts. Each is one search-and-read with a named method:

| Item (card) | Method hint |
| --- | --- |
| Longlaville PET depolymerisation construction/start-up (pch-pet-depolymerisation) | M3: Loop Industries / SEQENS news, partner releases |
| Seville pyrolysis start-up (pch-plastics-pyrolysis) | M3: Plastic Energy news |
| Sukowati full-scale CO2 injection (ups-co2-eor) | M3/M5: PETRONAS + SKK Migas releases |
| OCM after the 2014 demonstration (pch-oxidative-coupling-methane) | M3: Siluria successor status, review papers |
| Fram Sør all-electric subsea start-up (ups-all-electric-subsea) | M3: Equinor project pages |
| Colleferro and Retznei oxyfuel cement status (ccs-oxyfuel-cement) | M3: Heidelberg Materials / Buzzi |
| e-cracking demo measured results (pch-electric-steam-cracking) | M3: BASF/SABIC/Linde releases |
| PureCycle operating rate since 2023 (pch-solvent-based-plastics-purification) | M3: PureCycle investor updates, SEC filings |
| Microreactor milestones refresh (pwr-microreactors) | M3: eVinci/Oklo/BWXT news since 26 Oct |
| PEM stack lifetime conflict 60k vs 40k h (h2-pem-electrolysis) | M1: both DOE docs are in `corpus/doe-hfto/` — record both with dates, prefer the newer assessment as the headline |
| Kasawari CCS start-up conflict 2025/end-2025/2026 (gas-high-co2-reinjection) | M3/M5: PETRONAS, SKK Migas, news wire |
| Stratos start-up (ccs-dac-liquid-solvent) | **Parked until after January 2027** — not this programme |

### Wave 3 — Sector sweeps of `not_in_sources_read` (the 848; main body)

Sector by sector in the order in §1. Per sector, split by field type and run the matching
playbook; batch ~15–25 gaps per flash task; the supervisor (or web-search-agent under
verification) builds the evidence pack, flash applies it.

- **costs (248)** — techno-economic studies: arXiv (collector already runs), NETL/DOE via
  netl.doe.gov and energy.gov (M4), IRENA/IEA reports (many already catalogued), company
  investor/annual reports ($/kW averages). Record metric + range + unit + dollar year + basis
  or the gap stays.
- **reference_plants (217)** — Global CCS Institute 2026 status doc (on disk), IEA CCUS
  Projects Database (free registration → M8 if the form fights back), OEM project reference
  lists, operator news pages. One to three plants with country, capacity, year, status.
- **trl (202)** — IEA ETP Clean Energy Technology Guide (collected, `corpus/iea-reports/`),
  EU SETIS TRL pages, DOE program records. If no table lists the technology, leave the gap
  with maturity resting on card evidence (recorded as the action).
- **performance (138)** — OEM datasheets and brochures for the suppliers already named on the
  card (M3, M5 for JS pages), standards-body fact sheets.
- **process (5 not_in_sources_read + Wave 4's 230)** — licensor process descriptions (UOP,
  Axens, Lummus, Topsoe, Technip Energies, KBR — all catalogued sources), open textbooks and
  handbooks, standards scopes (API/ISO/IEC catalogues are fetchable). Replace general
  knowledge with one named authority; the gap closes only when the card cites it.
- **suppliers (29)** — closes via Wave 6 vendor work; a named supplier list with URLs.

### Wave 4 — `general_knowledge_only` (231, almost all `process`)

Run inside each sector sweep (same playbook as `process` above), tracked separately because
success means *finding any citable authority*, not a number. Where nothing authoritative is
reachable after M3–M9, the gap is kept and its `where` is updated with the best rejected
lead — recorded honestly, never force-closed.

### Wave 5 — Unreachable-source retries (15 + Wave 3 leftovers)

Dedicated browser/computer-use session over everything plain fetch could not reach: the M8
and M9 playbooks, Scribd recipe included, Wayback as fallback. Output either closes the gap,
lands a new corpus document (M10), or converts the gap to `source_unreachable` with a precise
block note for the owner.

### Wave 6 — Adjacent registers that close card fields

- **Vendor batches** (queue in `catalog/index/vendors.md`; 403 names): suppliers gaps close
  when the named suppliers land in `catalog/vendors/` and on the card. Order to match the
  gap counts: UPS 75, H2 61, PCH 50, GAS 43, CCS 41, REF 39, MID 37, ROT 12, MAT 9, INS 8,
  DIG 4, PRC 4, HSE 3, PWR 18 remainder. Research per vendor is M3/M5/M8; flash writes the
  records against `schema/vendor.schema.json` (established batch-1 pattern).
- **Citation binding sweep** (M11): the ~100 cards citing uncatalogued sources →
  `research_to_catalog.py` drafts → catalogued records; keeps the graph citation test happy
  as cards gain citations.

### Wave 7 — Publish and report

`tools/build.py` → `pytest` → `agent/library.py build` → `agent/embed.py` (threads=4,
background chain) → Neon reload `--embeddings sqlite --include-restricted` → `wrangler
deploy` → STATUS log entry + CHANGELOG version + memory update. `catalog/index/gaps.md` and
the vendors queue regenerate from the cards, so the new counts are the plan's scorecard.

## 5. Flash task contract

Every flash dispatch carries exactly this shape (worked example = Wave 1 amine item):

```
Task:   Close <gap item> on <card id>.
Input:  catalog/technologies/<card>.json; corpus/<doc paths>; worksheet rows <n–m>.
Method: M1 only (read the listed documents; no network). Quote every figure's passage.
Edit:   figures[] += {value, unit, metric, basis, year?, source{url, note}} — copy the
        schema field names from an existing figure on the card; delete the matching gaps[]
        entry; add the document to sources[] if absent (bare url + title when not
        catalogued).
Gates:  python tools/build.py  → "354 records valid"
        pytest -q tests        → 479 passed, 1 skipped
Report: per gap — closed / kept-why; every quote with its document path; gate tails.
Commit: none (supervisor commits after diff review).
```

Supervisor duties per batch: verify two quotes per flash task against the documents, review
the full diff, run gates, commit (`Gaps W<n> <sector>: <one-line>`), push, tally the
worksheet.

## 6. Risks and standing notes

- **Blocked-from-Mac hosts** (osti, nrel, pnnl, mdpi): never retried directly; M4 mirrors or
  M8 browser; blocks recorded per rule 4/7.
- **Login/registration gates**: consult `docs/LOGIN_REQUIRED.md`; free-registration sources
  may need M8/M9 with the owner's accounts only if the owner volunteers them.
- **Embed runtime**: full-corpus embed is hours — chain it in background at Wave 7 only, not
  per batch; the hosted search stays keyword-only in between (known limit).
- **Concurrency**: no other sessions are active (owner 2026-10-26), keep the cheap habits —
  fetch before push, never amend.
- **Mimosa**: warn mode; single-line SQL literals if any pg.py change ever lands (none
  expected in this plan).
- **What this plan cannot close**: the 12 `paid_source` costs (owner decision), Stratos
  before January 2027, and anything the owner must buy credentials for.
