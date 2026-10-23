# User guide

For people and AI agents who want to use the library, not change it.

## 1. Three ways in

| Way | Best for | Needs |
| --- | --- | --- |
| Read the files | Quick look, any tool, any agent | Nothing |
| MCP server | AI assistants that support MCP (Claude Desktop, Claude Code, Cursor, VS Code, others) | Python 3.10+ |
| Python module | Scripts and pipelines | Python 3.10+ |

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
| `search(query, kind, sector, discipline, region, reuse_level, limit)` | Find sources (`kind="source"`), passages from documents (`kind="chunk"`), or both |
| `get_source(source_id)` | Read a source's full record and list its documents |
| `get_document(path)` | Read a document in full, using the `path` from a search result |
| `list_by_tag(code, region, reuse_level, source_type)` | Browse, e.g. all `ROT` sources in `sea` |
| `library_stats()` | Check what is indexed and whether semantic search is on |

Example questions for an assistant with the server connected:

- "Which Southeast Asian sources cover LNG liquefaction technology?"
- "Find recent papers on PEM electrolyzer degradation and summarise them with citations."
- "List open-licence sources for carbon capture."

### Python module

```python
import sys; sys.path.insert(0, "agent")
import library
library.build()
for hit in library.search("hydrogen compressor", region="apac", limit=5):
    print(hit["title"], hit["url"], hit["reuse_level"])
```

Command line: `python agent/library.py search hydrogen compressor`.

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
