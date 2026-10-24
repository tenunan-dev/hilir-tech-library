# Status

Living document. Update it at the end of every working session (newest entry on top in the log).

## Current numbers (2026-10-24)

| Item | Count |
| --- | --- |
| Catalog records | 344 |
| Verified | 126 (31 full-text-open, 75 full-text-restricted, 16 summary-only, 4 catalog-only) |
| Unverified | 217, of which 50 need a manual terms check (`catalog/index/needs-manual-check.md`) |
| Corpus documents | 64 (OSTI and arXiv abstracts; NETL, DOE and IEA reports in full text; IEA technology guide dataset) |
| Technology cards | 61 (CCS 14, H2 12, GAS 13, REF 13, PCH 9); register of about 300 technologies in `catalog/technology-register.yaml` |

Check live numbers with `catalog/index/README.md`, `wc -l corpus/manifest.jsonl` and the MCP tool `library_stats`.

## Phases

1. Catalog: done.
2. Verification and corpus: in progress.
3. Agent access (search index, embeddings, MCP server) and scheduled refresh: done.

## Backlog (in rough priority order)

1. **Technology cards:** cards exist for CCS, H2, GAS and REF; all open gaps are listed in `catalog/index/gaps.md`. Main ones: NETL baseline figures for CCS (regeneration energy, power-plant cost of capture); LNG specific power by liquefaction process (kWh/t); liquid hydrogen liquefaction energy; HEFA and alcohol-to-jet selling prices (NREL/PNNL reports on osti.gov, unreachable so far); SAF Grand Challenge Roadmap (record `doe-affo` now added, collect it). Next sectors: UPS, MID, PWR; PCH partly done.
1. **Manual terms checks:** 50 records listed in `catalog/index/needs-manual-check.md`.
2. **Unchecked collectable records:** chula-petroleum, itb-indonesia, kaust, keei, khalifa-university, mycite, myipo, nea-china, th-dmf, vn-pvj, uq-energy, weatherford.
3. **Remaining unverified records:** verify the rest of the 217, Southeast Asia and Asia Pacific first.
4. **MDPI:** its CDN (Akamai) returns 403 "Access Denied" to the collector for the RSS feeds, article pages and robots.txt itself (nothing collected). Options: manual inbox for chosen articles; ask MDPI to allow-list the user agent; OAI-PMH at `https://oai.mdpi.com/oai/oai2.php` answers (no robots.txt, formats `oai_dc` and `oai_agris`) but its sets are article types, not journals (the journal shows only as an ISSN inside the identifier, e.g. `oai:mdpi.com:/2036-7449/14/1/9/`), a `from=` date filter returned records from 2022, and it holds metadata and abstracts only, since full text sits on the blocked www.mdpi.com.
5. **More adapters** for verified full-text-open sources (government agencies, open-access journals).
6. **Asia Pacific coverage gaps:** e.g. LNG-specific Malaysian and Indonesian sources; add and verify records.
7. **Paid sources:** stay catalog-only until the owner provides API keys or subscriptions.
8. **OSTI full text for US Government Works:** the osti adapter stores metadata and abstracts only, because rights vary per document. Records marked as US Government Works are not copyrightable (https://www.osti.gov/disclaim). An adapter change could read each record's rights statement and store full text only for those, with an offline test.

## Where things run

- Repository: https://github.com/tenunan-dev/og-tech-sources (private; must stay private while it holds restricted text).
- Collection works from the owner's Mac and should work from GitHub Actions. The cloud sandbox used for development blocks most publisher hosts.
- The MCP server is registered in Claude Desktop and Claude Code on the owner's Mac (user scope), pointing at the clone's `.venv`.

## Log

Add one entry per working session, newest on top, in this format, so an agent with no memory of the session can continue:

```
- **YYYY-MM-DD, <who or which agent>:** Did: <changes, with commit hashes>. Verified: <checks run and results, e.g. build.py N records valid, pytest N passed, trial run looked right>. Failed: <what did not work, with the exact error message>. Next: <the concrete next step, or the owner decision it waits on>.
```

- **2026-10-24 (petrochemicals):** 9 PCH cards added: steam cracking, electric steam cracking, propane dehydrogenation, methanol-to-olefins, paraxylene adsorption, polyethylene, polypropylene, plastics pyrolysis, PET depolymerisation. 61 cards in total. Not yet carded in PCH: aromatics complex, metathesis, oxidative coupling, methanol, ammonia and urea, EO/EG (Shell page returned no body text), propylene oxide, phenol, butadiene, alpha olefins, other circular routes. Hosting parked: owner has no Azure subscription.
- **2026-10-24 (gap fill):** Status checks done for NET Power (Project Permian now gas turbines with post-combustion capture, FID H2 2026), Stratos (start moved to end of 2026), Mammoth (675 t captured H1 2026 vs 36,000 t/yr nameplate), oxyfuel cement (CI4C Mergelstetten plant inaugurated July 2026). Added reference plants (Great Plains Synfuels, Shute Creek, Brazos RSV2, Vadinar coker, Xinhai isomerisation), liquid hydrogen energy and cost (DOE record 19001), LNG specific power for C3MR, DMR and MFC (OGST 2020, CC BY). ATR with capture moved to pilot to match the IEA TRL. Open gaps 99 not_in_sources_read, 3 source_unreachable.
- **2026-10-24 (late night):** Mac collected the DOE SAF Grand Challenge Roadmap and Implementation Framework (doe-affo) and the IEA ETP Clean Energy Technology Guide dataset (634 technologies, TRL by year, CC BY 4.0). TRLs filled on 17 cards from the IEA guide; 25 cards have no IEA entry (gap updated). Neither SAF document gives HEFA or ATJ production costs. Open gaps now 119 on 51 cards.
- **2026-10-24 (night):** Missing inputs are now recorded: `gaps` field on every card (132 gaps: what, why, where to get it, next action, blocker), `catalog/index/gaps.md`, MCP tool `list_gaps`, `gaps.csv` in the Dataverse export. 243 register technologies still have no card.
- **2026-10-24 (evening):** 38 technology cards added: hydrogen (SMR, ATR with capture, alkaline, PEM, SOEC, AEM, methane pyrolysis, ammonia cracking, LOHC, liquid hydrogen, salt cavern storage, green and blue ammonia), gas and LNG (amine and membrane treating, dehydration, mercury removal, sulfur recovery, turbo-expander NGL, C3MR/AP-X, Optimized Cascade, DMR, MFC, FLNG, FSRU, GTL) and refining (CDU/VDU, hydrotreating, FCC, hydrocracking, resid hydrocracking, coking, reforming, isomerisation, alkylation, HEFA, co-processing, alcohol-to-jet, crude-to-chemicals). Every card links to its register entry. The Mac collected 8 NETL, DOE and IEA hydrogen and LNG reports. Record `doe-affo` added (DOE Alternative Fuels and Feedstocks Office, formerly BETO).
- **2026-10-24 (later):** CCS pilot: technology card schema, 14 CCS cards (amine, high-purity, physical and syngas solvents, membranes, sorbents, cryogenic, calcium looping, oxyfuel cement, Allam cycle, two DAC routes, chemical looping, emerging), Mermaid block diagrams, `compare_technologies` and `get_technology` MCP tools, technologies.csv in the Dataverse export, per-document sector tags. Next: add regeneration energy and power-plant costs from the NETL baseline, and re-check statuses noted in each card's `notes`.
- **2026-10-24:** Dataverse export added (`tools/export_dataverse.py`, docs/DATAVERSE.md): sources, documents and taxonomy CSVs; restricted document text left out by default. Not yet imported: needs the owner's Power Platform environment.
- **2026-10-23 (later):** Hosted mode added for cloud agents such as Copilot Studio: `server.py --http` (streamable HTTP, API key), Dockerfile that leaves restricted documents out, Azure Container Apps and Copilot Studio steps in docs/HOSTING.md. Documents whose own licence is open (arXiv CC0 abstracts) are now marked full-text-open. Not yet deployed: needs the owner's Azure subscription.
- **2026-10-23:** Documentation set added (AGENTS.md, docs/). MCP server registered on the owner's Mac. Search ranking improved (taxonomy and country labels indexed, ranking by query coverage); MISC Group added. Phase 3 built: search index, embeddings, MCP server, link check, weekly refresh workflow. arXiv collected (24 papers) after narrowing the query; OSTI collected (25). robots.txt handling fixed (403 now disallows). 126 records verified. Catalog of 342 records created.
