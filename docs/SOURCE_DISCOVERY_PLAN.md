# Source discovery plan (v2)

Standing programme (owner decision #30, 2026-10-29): finding, registering and properly
categorizing sources and vendors is the library's main effort now that the initial
gap-closure programme is closed ([GAP_CLOSURE_PLAN.md](GAP_CLOSURE_PLAN.md)). The
library covers not only technologies but **who can supply, build, construct, operate
and maintain them**.

v2 (2026-10-29, owner direction): sequenced for **continuous, multi-agent execution
without owner intervention**, with human-dependent items dropped behind, and a
flexible queue that is re-sequenced after every block completion or failure —
temporarily failed items are revisited later.

## How this plan runs

- **State lives in [research/source-discovery/state.json](../research/source-discovery/state.json)**
  (committed) — one row per block with status `queued | running | done | partial |
  blocked-temporary | blocked-owner`, retry counters and notes. Any agent updates it
  after every block outcome and re-sequences freely; rows are never deleted.
- **Candidates live in `research/source-discovery/candidates.jsonl`** (committed) —
  every candidate from every channel, one JSON per line, statuses `queued |
  rejected | registered | blocked-owner`. The owner inbox
  (`research/source-discovery/inbox.local.txt`, gitignored) is drained into it each session.
- **No owner intervention in the main loop.** Blocks that need money, a human browser
  or an owner decision are marked `blocked-owner`, parked in the state file's
  `parked_owner` list, and skipped — work continues on the next open block.
- **Temporary failures retry.** Site timeout, rate limit, provider down, Docker not
  running → `blocked-temporary` with a `retry_after` hint; the item is revisited after
  other blocks have run or in the next session. Nothing is abandoned for a transient error.
- **Multi-agent contract** (from GAP_CLOSURE_PLAN): mechanical edits and site reads go
  to flash-max workers, dispatched **serially** (user/model concurrency limit);
  the supervisor (session agent) researches, writes prompts, reviews diffs and runs
  gates per batch. IO-bound reads (crawls, OpenAlex, downloads) may run as background
  Bash tasks in parallel with edit batches.
- **Gates per batch, unchanged:** `python tools/build.py` must print N records valid;
  `pytest -q tests` must pass; commit only after both, pushing only this session's files
  (concurrent sessions assumed).

## Discovery channels (into candidates.jsonl)

| # | Channel | Method | Cadence |
| --- | --- | --- | --- |
| 1 | Citation mining (internal) | `tools/discover_sources.py` (block A2) scans corpus markdown, card evidence and gaps.md where-hints for source-like mentions; diff against catalog | Quarterly + after bulk intake |
| 2 | Citation graph (external) | OpenAlex/Crossref venue-frequency sweep over ~50 docs; flag venues cited ≥3× not in catalog | Twice a year |
| 3 | Vendor provenance | Crawl vendor sites' whitepaper/standards/certification pages; extract cited bodies and publications | Quarterly |
| 4 | Event + standards sweeps | Energy-event calendars and standards-body catalogues (API, ASME, ASTM, ISO/IEC, SIRIM, regulators) | Twice a year |
| 5 | Owner inbox | `inbox.local.txt`, drained each session | Continuous |

## Triage workflow (every candidate)

1. Dedup against `catalog/sources/` and `catalog/vendors/` (id, url, name, alias).
2. Blocked-domain check (osti/nrel/pnnl/mdpi from this Mac → mirror route);
   login/registration gate check ([docs/LOGIN_REQUIRED.md](LOGIN_REQUIRED.md)).
3. Verify against a page actually read (fetch → reader MCP → web search, in that order
   of preference); record `verification`, `last_verified`, evidence URL.
4. Register per schema (`catalog/sources/<id>.json` or `catalog/vendors/<id>.json`);
   collect per the record's access class: open → collectors; paywalled → manual extracts
   (owner-held copy); bot-blocked → browser/manual inbox; blocked → compliant mirrors.
5. Paid or owner-decision candidates → `blocked-owner` in the queue, never silently dropped.

## Work blocks (autonomous, sequenced in state.json)

| Id | Block | What done means |
| --- | --- | --- |
| A1 | Seed harvest from gaps.md hints | ✅ done 2026-10-29: 43 candidates queued |
| A2 | `tools/discover_sources.py` + first run | Script committed; diff report appended to candidates |
| A3 | Triage + register queued candidates (~8/batch) | Every queued row reaches registered / rejected / blocked-owner |
| A4 | Vendor categorization: optional `categories` field in vendor schema + backfill sweep | All vendor records carry categories; build+tests green |
| A5 | Source miscategorization audit (source_type, sectors, regions) | Sweep of all source records; fixes applied; report of changes |
| A6 | Verification sweep (193 unverified records) | Terms/about page read or bot-blocked flagged for browser retry |
| A7 | Vendor-provenance crawl (channel 3), contractor cohort first | New candidates queued from vendor sites |
| A8 | OpenAlex venue sweep (channel 2) | Venue frequency report → candidates |
| A9 | Event + standards sweep (channel 4) | New conference/standards candidates queued |
| A10 | EUBCE proceedings batch 1 (bioenergy cards) + intake | Docs in corpus/ with summaries |
| A11 | Vendor cohorts: Western EPC (Fluor, Wood, Petrofac, Worley, Bechtel, McDermott), NOC engineering arms (CNOOC, CPECC, PetroChina), SEA contractors, alias fixes (Kanadevia Inova rename of hitachi-zosen-inova) | Cohort registered, gates green |
| A12 | Publish cycle: build → embed (threads=4) → Neon reload (`--include-restricted`) → wrangler deploy → live check | /api/stats matches local counts |

Order is a default, not a contract: any agent may re-sequence in state.json after a
block outcome (e.g., run A8 in background while A3 batches edit). A12 runs whenever
2+ content blocks have landed and Docker is up; otherwise it stays `blocked-temporary`.

## Categorization (owner direction: proper categorization by type)

Current state (2026-10-29 audit):
- **Sources**: `source_type` enum (11 values; distribution is healthy — 64 agency-data,
  49 oem-supplier, 47 research-institute, 39 journal, 37 association, 36 licensor,
  28 standards-body, 22 trade-media, 20 conference, 17 epc-contractor, 12 patents) +
  sectors/disciplines/regions. Gaps: 193/371 unverified records, some conference/
  association and journal/publisher overlaps → A5 audit.
- **Vendors**: `roles` enum only (oem 177, operator 72, developer 71, supplier 65,
  service 48, licensor 32, epc 28, packager 13, integrator 9, rental 5) — roles say
  what a company *does*, not what *kind* of company it is (Samsung Heavy the shipyard
  vs Samsung Engineering the plant EPC share role values with very different trades).
- **Equipment**: technology cards carry `key_equipment` per process step; there is no
  cross-cutting equipment view.

Target:
- **A4 adds an optional `categories` array to `schema/vendor.schema.json`** with a
  controlled vocabulary (initial cut: plant-epc, offshore-epc, shipyard, equipment-oem,
  process-licensor, operator, materials-supplier, oilfield-service, power-rental,
  engineering-consultancy, fabrication, utility) — additive and optional so nothing
  breaks; backfill by category rules first, flash-worker pass to catch the rest.
- **A5 audits sources** for mis-typed records and inconsistent sector tags; fixes are
  ordinary commits with the diff reported.
- **Equipment index** is a generated view (from `key_equipment`), built by `build.py`
  into `catalog/index/equipment.md` if the owner wants it — proposed, not yet decided.

## Seeded candidates (2026-10-29, block A1 output)

Full list with statuses lives in `candidates.jsonl`. Highlights — 34 source candidates
mined from our own gap hints (IADC, CanmetENERGY, CISA ICS, CERI, European Hydrogen
Backbone, FM Global, Hydraulic Institute, IEA Bioenergy/PVPS, IHS PEP, IMO, Idaho
National Laboratory, NREL ATB (mirror), DOE HDSAM/Wind Market, EPA AP-42/GHGRP, METI
GIF, MIT CCS database, Maritime Executive, Ship & Bunker, Nelson-Farrar (owner),
NFOGM, NRIC DOME, Plastics Recyclers Europe, Queensland CSG, Singapore MPA, NERSA,
Universitas Trisakti, Westwood, Wood Mackenzie (owner), World Bank GGFR, EAGE,
Petroleum Research journal) and 8 vendor candidates (Rongke Power — temporary,
Hengli, BP, Nayara, Soluforce, PLN, Woodside, Kanadevia alias fix).

## Session log

Newest first, one line per session.

- **2026-10-29 (v2):** Owner direction: revisit plan, add sources found along the way,
  categorize by technology/vendor/equipment type, sequence for continuous multi-agent
  execution without owner intervention, human items behind, flexible re-sequencing on
  failure. Manual pre-pass over all gap where-hints seeded 43 candidates (A1 done);
  categorization audit performed (distribution above); plan restructured; state.json
  sequencer + queue committed.
- **2026-10-29:** Plan created; four owner-inbox candidates registered (eubce,
  gas-turbine-world, irecruit sources; uspe-global vendor).
- **2026-10-29 (later):** Owner-directed vendor cohorts: China (wison, sinopec,
  sinopec-engineering) and Korea + Japan (9 more; chiyoda broadened) — vendors 381 → 390.
