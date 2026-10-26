# User guide

For people and AI agents who want to use the library, not change it.

## 1. Ways in

| Way | Best for | Needs |
| --- | --- | --- |
| Read the files | Quick look, any tool, any agent | Nothing |
| MCP server | AI assistants that support MCP (Claude Desktop, Claude Code, Cursor, VS Code, others) | Python 3.10+ |
| Python module | Scripts and pipelines | Python 3.10+ |
| Hosted MCP server by URL | Cloud agents such as Microsoft Copilot Studio | A deployed server and API key, see [HOSTING.md](HOSTING.md) |
| Web interface | Browsing in a browser | The API key, at https://techlib.hilir.app (see below) |

### Read the files

- `catalog/index/README.md`: counts by sector, region and reuse level.
- `catalog/index/<CODE>.md`: sources per sector or discipline, Asia Pacific and Southeast Asia first. Example: `catalog/index/H2.md` for hydrogen.
- `catalog/catalog.jsonl`: every record, one JSON object per line. Load it into a dataframe, a vector store or an agent's context.
- `corpus/<source-id>/*.md`: collected documents. The front matter says the licence.

### MCP server

```
git clone https://github.com/tenunan-dev/og-tech-sources.git
cd og-tech-sources
python -m venv .venv && . .venv/bin/activate
pip install -r requirements-agent.txt
python agent/library.py build
pip install fastembed && python agent/embed.py      # optional: semantic search
```

Register it with your MCP client, using absolute paths:

- Claude Desktop: in `claude_desktop_config.json`, under `mcpServers`, add `"og-tech-sources": {"command": "<repo>/.venv/bin/python", "args": ["<repo>/agent/server.py"]}`, then restart the app.
- Claude Code: `claude mcp add -s user og-tech-sources -- "<repo>/.venv/bin/python" "<repo>/agent/server.py"`.
- Other clients (Cursor, VS Code, Windsurf, Gemini CLI, Codex CLI and so on): add a stdio server with the same command and argument in that client's MCP settings.

Tools:

| Tool | Use it to |
| --- | --- |
| `search(query, kind, sector, discipline, region, reuse_level, limit)` | Find sources (`kind="source"`), passages from documents (`kind="chunk"`), technology cards (`kind="technology"`), vendor records (`kind="vendor"`), or all of them |
| `get_source(source_id)` | Read a source's full record and list its documents |
| `get_document(path)` | Read a document in full, using the `path` from a search result |
| `list_by_tag(code, region, reuse_level, source_type)` | Browse, e.g. all `ROT` sources in `sea` |
| `compare_technologies(sector, maturity, application)` | Compare technology options (e.g. all CCS routes for cement), commercial first |
| `list_vendors(role, sector, query)` and `get_vendor(vendor_id)` | The curated vendor directory: who supplies a technology, with roles, products and the pages each record was written from |
| `list_technology_register(code, maturity, query)` | The register of about 300 technologies across all sectors (indicative); entries with a card link to `get_technology` |
| `list_gaps(sector, field, reason_code, include_no_card)` | What the cards still lack (costs, TRL, performance, plants, status), why, where to get it and the next action; tell users when the library cannot answer yet |
| `get_technology(technology_id)` | One technology card: principle, process steps and equipment, a Mermaid block flow diagram, costs with basis, suppliers, reference plants, sources |
| `library_stats()` | Check what is indexed and whether semantic search is on |
| `db_catalog()` | The Postgres layer's tables, views and functions — read this before writing `sql_query` statements |
| `sql_query(sql, max_rows=100)` | Run one read-only `SELECT`/`WITH` against schema `og` (needs `DATABASE_URL`; on the hosted server it is already set) |
| `graph_neighbors(node, depth, rels)` | Walk the knowledge graph from a node such as `technology:ccs-cryogenic`, `vendor:wartsila` or `source:netl` |

Example questions for an assistant with the server connected:

- "Which Southeast Asian sources cover LNG liquefaction technology?"
- "Find recent papers on PEM electrolyzer degradation and summarise them with citations."
- "List open-licence sources for carbon capture."
- "What CCS options exist for a cement plant, on the market and in the lab, with block diagrams, equipment and costs?" The assistant should call `compare_technologies(sector="CCS", application="cement")`, then `get_technology` for each, and render the Mermaid diagrams.

- "Which technology cards cite the same sources as amine capture?" The assistant can call `sql_query` with `SELECT * FROM v_technology_co_citation WHERE a = 'ccs-amine-post-combustion' OR b = 'ccs-amine-post-combustion'` (after `db_catalog`).

Technology cards are also readable without the server: `catalog/index/technologies-CCS.md` (comparison table and diagrams) and `catalog/technologies.jsonl`. Costs are only comparable when their basis matches: check the dollar year, plant type, capture rate and scope given with each figure.

### Python module

```python
import sys; sys.path.insert(0, "agent")
import library
library.build()
for hit in library.search("hydrogen compressor", region="apac", limit=5):
    print(hit["title"], hit["url"], hit["reuse_level"])
```

Command line: `python agent/library.py search hydrogen compressor`.

### Browse in a browser

The hosted server also serves an HTML interface at https://techlib.hilir.app. Sign in once at
`/login` — with the library API key (the same key agents send in the `x-api-key` header) or, if
the owner has set up named accounts, with your email and password; a session cookie keeps you
signed in for 30 days. Every page also accepts the `x-api-key` header instead of
the cookie, and any page without a valid session redirects to the sign-in page.

| Page | Shows |
| --- | --- |
| `/` | Counts, search box, sector grid |
| `/search?q=...` | Ranked sources, passages, technology cards and vendor records |
| `/technologies`, `/technologies/{id}` | Comparison table; one card in full: block diagram, figures with unit/year/basis/source, suppliers, reference plants, gaps, sources |
| `/vendors` | The vendor directory with its coverage queue of supplier names not yet recorded |
| `/register`, `/sources`, `/documents?path=...`, `/gaps` | The register, catalog records with their documents, document text, missing inputs |
| `/database` | Row counts, schema reference, example queries |
| `/database/sql` | Read-only SQL console |
| `/database/search` | Hybrid keyword + vector search over passages, cards and vendor records |
| `/database/map` | The atlas: the whole knowledge graph as a constellation of node kinds, with live row counts |
| `/database/graph` | The knowledge graph as an interactive network: search a node, filter relations, click for details, double-click to expand |

SQL console rules: one `SELECT` or `WITH` statement against schema `og`, no semicolons and no
comments, at most 500 rows (default 100). The statement runs as a read-only role with a 15 second
statement timeout, so it cannot change anything.

`/database/search` fuses keyword and vector ranking when the server can embed the query: the local
server (with fastembed installed and the index embedded) shows a "semantic" badge; the hosted copy
shows "keyword only" because its image ships no embedder — the vectors are in Postgres (the SQL
console's `hybrid_search` vector half works there), but a query vector needs the Mac-side server.
Run `SELECT * FROM hybrid_search('CO2 storage', NULL, 10)` in the console for keyword ranking anywhere.

The graph browser takes node ids of the form `<kind>:<key>`, for example `technology:ccs-cryogenic`,
`source:netl`, `org:honeywell-uop`, `vendor:wartsila`, `region:sea` or `register:CCS/<name>`. The
atlas at `/database/map` shows every node kind as a bubble sized by its live count with the relations
between them; clicking a bubble opens the network view at that kind's most connected node. The full
node id and relation list is in [POSTGRES.md](POSTGRES.md).

## 2. Using results responsibly

Every result carries `licence`, `reuse_level` and `permitted_use`. Follow them:

| reuse_level | You may |
| --- | --- |
| `full-text-open` | Quote and reuse with attribution under the stated licence |
| `full-text-restricted` | Read and summarise for personal or internal reference. Do not republish, share outside, or use commercially. Results include a `use_note` |
| `summary-only` | Cite and link; write your own summary. No text is stored |
| `catalog-only` | Cite and link only |

Always cite the `url`. Records marked `unverified` have not had their terms checked yet; treat their `reuse_level` as provisional.

## 3. What is in it

See `catalog/index/README.md` for current numbers and [STATUS.md](STATUS.md) for what has been collected. The corpus currently holds metadata and abstracts from OSTI and arXiv; most catalog sources are reference links.

## 4. Keeping your copy current

```
git pull
python agent/library.py build && python agent/embed.py   # rebuild after each pull
```

A scheduled job on GitHub adds new arXiv and OSTI records weekly and checks links monthly.

## 5. Troubleshooting

| Symptom | Fix |
| --- | --- |
| MCP client shows no tools | Use absolute paths; restart the client fully; run the command by hand to see errors |
| `library_stats` shows 0 vectors | Run `python agent/embed.py` after `library.py build` |
| Search misses new documents | Rebuild the index after `git pull` |
| Path contains `&` or spaces | Quote it in shell commands; JSON configs need no escaping |
