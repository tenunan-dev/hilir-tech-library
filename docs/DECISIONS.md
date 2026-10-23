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
