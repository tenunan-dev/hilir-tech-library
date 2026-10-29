# Source discovery plan

Standing programme (owner decision #30, 2026-10-29): after the initial gap-closure
programme closed ([GAP_CLOSURE_PLAN.md](GAP_CLOSURE_PLAN.md)), finding and registering
sources that are missing from the catalog is the library's main effort. Sources are no
longer handled as one-off gap entries; every unknown source goes through this pipeline.

## Problem

The catalog (368 records) was built top-down from a fixed seed sweep. A source outside
that seed is invisible until someone happens to name it — four examples surfaced in one
owner question on 2026-10-29 (EUBCE, Gas Turbine World, USP&E Global, "iRecruit 2026"),
none of which the catalog knew. Discovery must become systematic, not accidental.

## Channels

| # | Channel | Method | Cadence | Output |
| --- | --- | --- | --- | --- |
| 1 | Citation mining (internal) | Script-scan `corpus/` markdown, card evidence fields and `catalog/index/gaps.md` "where" hints for source-like mentions (domains, publishers, handbook/standard/proceedings names); fuzzy-diff against catalog by name and domain | Quarterly, and after every bulk corpus intake | candidates |
| 2 | Citation graph (external) | Push ~50 representative docs' titles through the OpenAlex/Crossref APIs (free, no login), group cited works by venue, flag venues cited ≥3 times that are not in the catalog | Twice a year | candidates |
| 3 | Vendor provenance | Crawl the vendor directory's sites (whitepaper/standards/certification pages), extract bodies and publications vendors cite | Quarterly | candidates |
| 4 | Event and standards sweeps | Annual pass over energy-event calendars (registers proceedings sources) and standards-body catalogues (API, ASME, ASTM, ISO/IEC, SIRIM, regional regulators) | Twice a year | candidates |
| 5 | Owner inbox | Owner drops any name or link into `research/source-discovery/inbox.local.txt`; batch-processed each session | Continuous | candidates |

Channel 1 needs a script (`tools/discover_sources.py`, not yet written) — that plus the
channel-3 crawler are Wave 0 of this plan. Channel 5 costs nothing and already works.

## Triage workflow (all channels)

1. Append the candidate to `research/source-discovery/candidates.jsonl` (name, url if
   known, channel, first_seen, status).
2. Auto-checks: already in `catalog/sources/` (by id/url/name)? domain blocked from this
   Mac (osti/nrel/pnnl/mdpi rule, `docs/LOGIN_REQUIRED.md`)? login- or registration-gated?
3. Score: sector fit, source_type, access class, quality tier.
4. Register: `catalog/sources/<id>.json` per `schema/source.schema.json` (mirror
   `catalog/sources/ghgt.json` for conferences) or `catalog/vendors/<id>.json` per the
   vendor schema; run `python tools/build.py`.
5. Collect according to the recorded access class — no exceptions:
   - `open` → collectors;
   - `paywalled` → manual extracts only, via the owner's own copy, into `corpus/_inbox/`;
   - login/registration-gated or bot-blocked → browser use or manual inbox;
   - blocked domains → compliant mirrors only.
6. Verify the record (`verification`, `last_verified`, evidence URL read), then publish:
   `python tools/build.py && python agent/library.py build` (+ `agent/embed.py` when
   corpus grew) → Neon reload → `wrangler deploy` → live check `/api/stats`.

## Vendor coverage: who can supply, build, construct and maintain

The library is not only about technologies but also about who can deliver them. The
vendor directory (decision #28) is that layer — roles (oem, licensor, packager, epc,
developer, operator, rental, service, supplier, integrator), products and
per-technology links, wired into search, MCP, REST, web, Neon and the graph (`vendor:`
nodes with `supplies` edges). Contractor and supplier discovery rides the same five
channels and the same queue; candidates come from card supplier lists, the owner's
inbox and the channel-3 provenance crawl.

Regional contractor cohorts (owner-directed sweeps):

- **2026-10-29, China:** `wison`, `sinopec`, `sinopec-engineering` registered.
- **2026-10-29, Korea + Japan:** `samsung-engineering`, `hyundai-ec`, `sk-ecoplant`,
  `daelim`, `gs-ec`, `kepco-ec`, `doosan-enerbility`, `jgc`, `toyo` registered;
  `chiyoda` broadened from H2-licensor-only to full LNG/refinery EPC.
- **Next cohorts:** Western EPC gaps (Fluor, Wood, Petrofac, Worley, Bechtel, McDermott
  — KBR, Technip, Saipem, MODEC and the Korean shipyards already in), NOC engineering
  arms (CNOOC, CPECC, PetroChina engineering), Southeast Asian contractors; then the
  channel-3 provenance crawl starts from this cohort.

## Wave 0 (next session)

1. Write `tools/discover_sources.py` (channel 1) and run it once over the current corpus.
2. Crawl the first vendor batch (channel 3): the new CN/KR/JP contractor cohort plus
   all PWR + H2 vendors.
3. Collect a first EUBCE proceedings batch into `corpus/_inbox/eubce/` (papers for the
   bioenergy cards: BECCS, biochar, pyrolysis/HTL, cellulosic ethanol, WTE).
4. OpenAlex run #1 (channel 2) over 50 representative docs.

## Seeded candidates (2026-10-29)

| Candidate | Resolution |
| --- | --- |
| EUBCE | Registered as source `eubce` (conference, open proceedings) — done |
| Gas Turbine World | Registered as source `gas-turbine-world` (paid handbook, summary-only, manual extracts) — done |
| USP&E Global | Registered as vendor `uspe-global` — done |
| "iRecruit 2026" | Registered as source `irecruit` after the owner supplied the site: irecruit.co is a US construction/AEC recruiting firm whose free 2026 reports (data-center cost per MW, salary guides, nuclear/SMR and renewables construction) carry usable market data — tier 3 trade media. Done |

## Session log

Newest first, one line per session: what ran, candidates found, registered, collected.

- **2026-10-29:** Plan created after the owner named four unknown sources. Channels 5
  output processed (4 candidates): all 4 registered (the owner's `irecruit.co` link
  resolved the fourth — iRecruit is a construction/AEC recruiting firm with 2026 market
  reports; `catalog/sources/irecruit.json`, tier 3 trade media). Wave 0 not started.
- **2026-10-29 (later):** Owner-directed vendor cohorts: China (Wison, Sinopec, Sinopec
  Engineering) and Korea + Japan (Samsung Engineering/E&A, Hyundai E&C, SK Ecoplant,
  Daelim, GS E&C, KEPCO E&C, Doosan Enerbility, JGC, Toyo; Chiyoda broadened to LNG
  EPC) — vendors 381 → 390. A "who can supply, build, construct and maintain" section
  added above; Western-EPC and NOC-engineering cohorts queued next.
