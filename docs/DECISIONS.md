# Decisions

Owner decisions and the rules that follow from them. Add new entries at the bottom with a date. Do not change a past decision; add a new one that supersedes it.

| # | Date | Decision | Consequence |
| --- | --- | --- | --- |
| 1 | 2026-10-23 | Scope covers all sectors and disciplines of oil, gas, petrochemicals and energy | Taxonomy has 8 sectors and 6 disciplines |
| 2 | 2026-10-23 | Global coverage, weighted toward Asia Pacific and Southeast Asia | Index pages and search rank `sea` and `apac` sources first |
| 3 | 2026-10-23 | Store the catalog plus full open-licence text. Downloadable text with no stated licence is kept, with notes. Text that cannot be downloaded stays catalog-only | `reuse_level` values `full-text-open`, `full-text-restricted`, `catalog-only` |
| 4 | 2026-10-23 | Agents get all three access routes: plain files, vector index, MCP server | `catalog/`, `corpus/`, `agent/` |
| 5 | 2026-10-23 | Paid or private sources stay in the catalog only until the owner has API keys | Paid records are `catalog-only` |
| 6 | 2026-10-23 | Sites that allow only personal, non-commercial copies: keep full private copies | `full-text-restricted` with `use_note`; the repository stays private |
| 7 | 2026-10-23 | Sites whose terms forbid copying are summary-only; sites that ban AI use (Honeywell, Caterpillar/Solar Turbines) are catalog-only | No collection for these |
| 8 | 2026-10-23 | Where crawling is prohibited, content comes in by hand only | Manual inbox `corpus/_inbox/<id>/` |
| 9 | 2026-10-23 | arXiv: allow the API (`export.arxiv.org/api`) despite arXiv's robots.txt, at 1 request per 3 s, metadata and abstracts only, with a narrowed query | `ROBOTS_EXCEPTIONS` in `collectors/common.py`; evidence https://info.arxiv.org/help/api/tou.html |
| 10 | 2026-10-23 | Repository: `tenunan-dev/og-tech-sources`, private | |
| 11 | 2026-10-23 | Register the MCP server in Claude Desktop and Claude Code on the owner's Mac | Config backup at `claude_desktop_config.json.bak` |
| 12 | 2026-10-23 | Documentation is agent-agnostic: AGENTS.md is the entry point for every AI agent and person | CLAUDE.md only points to AGENTS.md |
| 13 | 2026-10-23 | A hosted (URL-reachable) server serves catalog records and open-licence documents only, behind an API key | Dockerfile excludes restricted documents; `--include-restricted` only for owner-only servers |
| 14 | 2026-10-23 | Hosting on Cloudflare under the owner's account via the tenunan-dev GitHub account | Worker plus Container running the Dockerfile at https://techlibrary.tenunan.com (Workers Paid, $5/month); API key is a Worker secret, never in the repo; see docs/HOSTING.md |
| 15 | 2026-10-24 | Hosted server also offers a REST API and OAuth sign-in so claude.ai web and mobile can connect, at no extra cost | `/api/*` endpoints and OAuth in `deploy/cloudflare` |
| 16 | 2026-10-24 | No Azure subscription. Missing inputs are recorded on the gaps page with why and where to get them | Gaps system: `gaps` on cards, `catalog/index/gaps.md`, MCP tool `list_gaps` |
| 17 | 2026-10-24 | Next sector after the first batch is upstream plus Malaysia and Indonesia sources; the owner has a Power Platform environment for the Dataverse import | `tools/export_dataverse.py`; the owner does the import himself |
| 18 | 2026-10-25 | Finish every technology card first, include sources and summaries for everything, and add a vector and knowledge graph database in Postgres for a later Neon deployment | 293 cards cover all 300 register entries; every document has a `summary`; `db/schema.sql`, `agent/graph.py`, `tools/load_postgres.py` |
| 19 | 2026-10-25 | Cross-cutting disciplines (process design, rotating equipment, instrumentation, materials, HSE, digital) get their own sector codes PRC, ROT, INS, MAT, HSE, DIG instead of being forced into an energy sector | Sector enum in `schema/technology.schema.json`; `agent/graph.py` maps codes to sector or discipline nodes |
| 20 | 2026-10-25 | Wikipedia is catalogued as a secondary source (`wikipedia`, CC BY-SA, tier 3) and may back a card where no primary source could be read | Cards that cite it flag the citation as secondary; replace with OEM, licensor or standards-body sources over time |
| 21 | 2026-10-25 | Every corpus document must carry a hand-written summary; at most 40% of cards may lack a citation to a catalogued source | `tests/test_technologies.py` and `tests/test_graph.py` enforce both |
| 22 | 2026-10-25 | The Neon connection string and the Cloudflare API token stay outside the repository; the owner supplies them | Neon load and GitHub Actions auto-deploy wait for the owner (see STATUS.md handover) |
| 23 | 2026-10-25 | Copilot Studio agents connect to the existing Cloudflare-hosted MCP server (`https://techlibrary.tenunan.com/mcp`) with the API-key header; no new hosting | Connection checklist in docs/HOSTING.md; the public `https://techlibrary.tenunan.com/api/openapi.json` is the REST fallback |
| 24 | 2026-10-25 | Restricted document text may enter the Dataverse export (`--include-restricted`) only in an environment no colleague can read; the hosted server keeps serving open-licence text only (decision 13 unchanged) | Re-export without the flag if the environment is ever shared |
| 25 | 2026-10-26 | Hosted server's home is `https://techlib.hilir.app/mcp` (owner chose hilir.app; same Worker and Cloudflare account — no re-provisioning, no key rotation); `techlibrary.tenunan.com` stays attached during a transition and is retired once clients have moved | Both routes in `deploy/cloudflare/wrangler.jsonc`; OAuth grants are per-URL, so claude.ai connectors are re-added at the new address; retire procedure in docs/HOSTING.md Domain transition |
