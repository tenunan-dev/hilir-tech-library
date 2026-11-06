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

`python agent/server.py` serves over stdio. Sixteen tools:

| Tool | What it returns |
| --- | --- |
| `search(query, kind, sector, discipline, region, reuse_level, limit)` | Ranked sources and document passages, each with url, licence, reuse_level and (for restricted sources) a use note. `kind` also takes `technology`, `vendor` and `equipment` |
| `get_source(source_id)` | The full catalog record and its collected documents |
| `get_document(path)` | Front matter and full text of one document |
| `list_by_tag(code, region, reuse_level, source_type)` | Catalog sources for a sector or discipline code, Asia Pacific first |
| `list_vendors(role, sector, query)` / `get_vendor(vendor_id)` | The curated vendor directory — roles, products, the cards it supplies, the pages each record was written from |
| `list_equipment(equipment_type, query)` / `get_equipment(equipment_id)` | The equipment catalog — specification ranges with basis and source, vendor model lines, applications, the cards that use the class, gaps |
| `get_technology(technology_id)` | One technology card: principle, process steps with equipment, Mermaid block flow diagram, key equipment, costs with basis, suppliers, reference plants |
| `compare_technologies(sector, maturity, application)` | Comparison table of technology options, commercial first |
| `list_technology_register(code, maturity, query)` | The register of about 300 technologies across all sectors |
| `list_gaps(sector, field, reason_code, include_no_card)` | Inputs the technology cards still lack, with why and where to get them |
| `library_stats()` | Counts read from Neon first (baked index as fallback) |
| `sql_query(sql, max_rows=100)` | Rows from one read-only `SELECT`/`WITH` statement against the Postgres layer (schema `og`): guarded, read-only role, 15 s timeout, at most 500 rows. Answers `database not configured` unless `DATABASE_URL` is set |
| `db_catalog()` | Reference for the Postgres layer — tables and their columns, views, and the `graph_neighbors` / `hybrid_search` functions; read before writing `sql_query` statements |
| `graph_neighbors(node, depth=1, rels=None)` | The knowledge graph within `depth` hops (1-3) of a node such as `technology:ccs-cryogenic`, `source:netl`, `vendor:wartsila` or `org:honeywell-uop`; `rels` limits relations, `None` follows all |

Every `get_*`/`list_*` tool reads Neon first and falls back to the baked SQLite index, so a data
publish reaches all of them without a deploy.

Claude Desktop (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "hilir-tech-library": {
      "command": "/path/to/hilir-tech-library/.venv/bin/python",
      "args": ["/path/to/hilir-tech-library/agent/server.py"]
    }
  }
}
```

Claude Code: `claude mcp add hilir-tech-library -- /path/to/.venv/bin/python /path/to/hilir-tech-library/agent/server.py`

Any MCP client works the same way (Cursor, VS Code, Windsurf, Gemini CLI, Codex CLI, a local model
runner) — a stdio server with that command and argument.

The server builds the index on first start if `build/library.db` is missing. For cloud agents
(Copilot Studio, claude.ai connectors and others) the same tools are served over HTTPS at
**`https://techlib-api.hilir.app/mcp`** (Streamable HTTP, stateless), with a REST API under
`/api/*`; both sit behind hilir Access and accept an Access access token
(`Authorization: Bearer`, `aud` = a registered origin) or a person's estate key in
`Authorization: Bearer` or `x-api-key`. See [docs/AUTH.md](../docs/AUTH.md) and
[docs/HOSTING.md](../docs/HOSTING.md).

HTTP mode also serves `agent/web.py`, an HTML interface: `/` (stats, search, sector grid),
`/search`, `/technologies/{id}`, `/vendors`, `/equipment/{id}`, `/register`, `/sources/{id}`,
`/documents?path=`, `/gaps`, and `/database` with a read-only SQL console, hybrid search and a
graph browser (`/database/sql`, `/database/search`, `/database/graph`). Sign-in is hilir Access
(the container reads identity from the bearer + userinfo and the role from `library.account`).
The database tools need `DATABASE_URL` set to the read-only role's DSN
([docs/POSTGRES.md](../docs/POSTGRES.md)). The hosted containers read Neon live; the image ships no
embedder, so keyword search is the default there while `hybrid_search`'s vector half works anywhere
through the SQL console.

