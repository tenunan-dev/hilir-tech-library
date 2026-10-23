# Agent access

## Search index

```
pip install -r requirements-agent.txt
python agent/library.py build                 # build/library.db, rebuilt from catalog/ and corpus/
python agent/library.py search hydrogen compressor
```

The index holds every catalog record and every corpus document, split into ~1200-character
chunks, in a SQLite FTS5 table ranked by BM25. Asia Pacific and Southeast Asia sources get a
small ranking boost. `build/` is not committed; rebuild it after pulling.

### Semantic search (optional)

```
pip install fastembed
python agent/embed.py                         # default BAAI/bge-small-en-v1.5
python agent/embed.py --model sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

With vectors present, `search` fuses keyword and vector rankings (reciprocal rank fusion).
Run `embed.py` again after each `library.py build`.

## MCP server

`python agent/server.py` serves over stdio. Tools:

| Tool | What it returns |
| --- | --- |
| `search(query, kind, sector, discipline, region, reuse_level, limit)` | Ranked sources and document passages, each with url, licence, reuse_level and (for restricted sources) a use note |
| `get_source(source_id)` | The full catalog record and its collected documents |
| `get_document(path)` | Front matter and full text of one document |
| `list_by_tag(code, region, reuse_level, source_type)` | Catalog sources for a sector or discipline code, Asia Pacific first |
| `library_stats()` | Counts of sources, documents, chunks and vectors |

Claude Desktop (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "og-tech-sources": {
      "command": "/path/to/og-tech-sources/.venv/bin/python",
      "args": ["/path/to/og-tech-sources/agent/server.py"]
    }
  }
}
```

Claude Code: `claude mcp add og-tech-sources -- /path/to/.venv/bin/python /path/to/og-tech-sources/agent/server.py`

The server builds the index on first start if `build/library.db` is missing.
