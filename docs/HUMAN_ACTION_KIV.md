# Human-action KIV register (2026-10-28/29 closure effort closeout)

The automatable programme is complete (register 1,118 -> 905; 213 gaps closed).
Everything below needs a human or an owner decision. Regenerate anytime:
`general_knowledge_only`, `not_in_sources_read` etc. remain in catalog/index/gaps.md.

## 1. Paid sources — owner buys access (12 gaps, all PCH costs + 3)

All nine "capital cost and production cost" gaps on PCH cards (electric steam cracking,
methanol-to-olefins, paraxylene adsorption, PET depolymerisation, plastics pyrolysis,
polyethylene, polypropylene, propane dehydrogenation, steam cracking) need a petrochemical
cost database (SRIC/Nexant/PEP class). Plus: pwr-heavy-duty-gas-turbines installed cost,
ups-digital-core-analysis service price, ups-seismic-acquisition survey cost per km2.

## 2. Bot-walled sources — human browser or manual inbox (15 gaps)

mid-composite-reinforced-thermoplastic-pipe (TCP specs), mid-crude-product-tankers (IMO
sulphur cap compliance), mid-heated-pipe-in-pipe-flowlines (U-values), pch-engineering-plastics
(PC/nylon process data), pwr-biomass-waste-to-energy (efficiency/throughput),
pwr-compressed-liquid-air-storage (Highview Carrington), pwr-enhanced-geothermal (Fervo Cape
Station), pwr-flow-batteries (Rongke Dalian), pwr-gravity-storage (Rudong project),
pwr-lithium-ion-bess (installed $/kWh), pwr-offshore-wind-fixed (installed cost/CF),
pwr-onshore-wind (turbine ratings/cost), pwr-perovskite-tandem (certified records),
ups-gas-injection-wag (WAG recovery evidence), ups-heavy-oil-upgrading-in-field (CAPRI results).

## 3. Terms pages — human browser (18 remaining of 26)

Automated pass fetched 6 (findings recorded in source notes; evidence in
docs/archive/2026-10-28_terms-check-pass1.json). Remaining 18 are bot-walled to plain HTTP;
interactively confirmed blocked: PetroWiki/OnePetro (Cloudflare). List in
catalog/index/needs-manual-check.md.

## 4. Time-gated re-checks (3)

Stratos DAC start-up (after Jan 2027), e-cracking demo measured results,
microreactor licensing milestones.

## 5. Not a gap but pending

collect.py --manual review pass over the 28 new arXiv full-text documents (summaries are
abstract-derived; review before citing figures from them).
