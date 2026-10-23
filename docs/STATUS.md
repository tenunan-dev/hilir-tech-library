# Status

Living document. Update it at the end of every working session (newest entry on top in the log).

## Current numbers (2026-10-23)

| Item | Count |
| --- | --- |
| Catalog records | 343 |
| Verified | 126 (31 full-text-open, 75 full-text-restricted, 16 summary-only, 4 catalog-only) |
| Unverified | 217, of which 50 need a manual terms check (`catalog/index/needs-manual-check.md`) |
| Corpus documents | 49 (25 OSTI, 24 arXiv; metadata and abstracts) |

Check live numbers with `catalog/index/README.md`, `wc -l corpus/manifest.jsonl` and the MCP tool `library_stats`.

## Phases

1. Catalog: done.
2. Verification and corpus: in progress.
3. Agent access (search index, embeddings, MCP server) and scheduled refresh: done.

## Backlog (in rough priority order)

1. **Manual terms checks:** 50 records listed in `catalog/index/needs-manual-check.md`.
2. **Unchecked collectable records:** chula-petroleum, itb-indonesia, kaust, keei, khalifa-university, mycite, myipo, nea-china, th-dmf, vn-pvj, uq-energy, weatherford.
3. **Remaining unverified records:** verify the rest of the 217, Southeast Asia and Asia Pacific first.
4. **MDPI:** its CDN returns 403 to the collector (nothing collected). Options: manual inbox for chosen articles; ask MDPI to allow-list the user agent; OAI-PMH at `oai.mdpi.com` works but cannot filter by journal and gives abstracts only.
5. **More adapters** for verified full-text-open sources (government agencies, open-access journals).
6. **Asia Pacific coverage gaps:** e.g. LNG-specific Malaysian and Indonesian sources; add and verify records.
7. **Paid sources:** stay catalog-only until the owner provides API keys or subscriptions.

## Where things run

- Repository: https://github.com/tenunan-dev/og-tech-sources (private; must stay private while it holds restricted text).
- Collection works from the owner's Mac and should work from GitHub Actions. The cloud sandbox used for development blocks most publisher hosts.
- The MCP server is registered in Claude Desktop and Claude Code on the owner's Mac (user scope), pointing at the clone's `.venv`.

## Log

- **2026-10-23:** Documentation set added (AGENTS.md, docs/). MCP server registered on the owner's Mac. Search ranking improved (taxonomy and country labels indexed, ranking by query coverage); MISC Group added. Phase 3 built: search index, embeddings, MCP server, link check, weekly refresh workflow. arXiv collected (24 papers) after narrowing the query; OSTI collected (25). robots.txt handling fixed (403 now disallows). 126 records verified. Catalog of 342 records created.
