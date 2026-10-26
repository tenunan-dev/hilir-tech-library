# Postgres, vectors and the knowledge graph

An optional second home for the library: one Postgres database (works on Neon) that holds the catalog, the
corpus passages, the technology cards, embeddings for semantic search (pgvector) and a graph that links every
entry to the others. The files in the repository stay the master copy; the database is rebuilt from them.

## What is in it

Schema `og`, defined in [db/schema.sql](../db/schema.sql):

| Table | Holds |
| --- | --- |
| `source`, `source_tag` | One row per catalog record; sector, discipline and region tags |
| `document`, `chunk` | Corpus documents and their passages. `chunk.embedding` is a 384-dimension vector; `chunk.tsv` is the full-text index |
| `technology` and its children | Cards: `technology_alias`, `technology_source`, `technology_figure` (performance and cost figures with unit, year, basis, source URL), `technology_supplier`, `technology_gap` (what is missing, why, where to look) |
| `vendor` | The vendor directory: one row per curated record with roles, products, the card ids it supplies, an embedding and a full-text index |
| `register_entry` | The register of about 300 technologies, linked to a card where one exists |
| `node`, `edge` | The knowledge graph (below) |

Views and functions: `v_gap`, `v_technology_co_citation`, `graph_neighbors(start, depth, rels)`,
`hybrid_search(query, query_vector, k)` (full-text and vector ranks fused over chunks, cards and vendor
records), `refresh_similarity(k, min_sim)`.

## The graph

Every node id is `<kind>:<key>`: `source:netl`, `document:corpus/...md`, `technology:ccs-cryogenic`,
`register:CCS/...`, `org:honeywell-uop`, `vendor:wartsila`, `sector:CCS`, `discipline:PRC`, `region:sea`,
`country:MY`, `gap:<card>:<n>`.

| Relation | From, to | Where it comes from |
| --- | --- | --- |
| `published_by` | source, org | catalog `publisher_org` |
| `in_sector`, `covers_discipline`, `in_region`, `in_country` | source, document, technology, register entry to a code | catalog tags; document sectors as the index computes them |
| `from_source` | document, source | document front matter |
| `cites` | technology, source | the card's `sources[].source_id` |
| `cites_document` | technology, document | a card source URL that equals a collected document's URL |
| `supplied_by` | technology, org | the card's `suppliers` |
| `supplies` | vendor, technology | the vendor record's `technologies` list |
| `alias_of` | org, vendor | a card supplier name matching a vendor record's name or aliases |
| `realised_by` | register entry, technology | the register name matches a card name or alias |
| `example_supplier` | register entry, org | the register's examples column; not verified |
| `alternative_to` | technology, technology | same sector and a shared category head or shared applications; weight explains it |
| `mentions` | document, technology | the card name or an alias appears in the document at least 3 times or in its title; the matched terms are stored in `props` |
| `has_gap`, `look_in` | technology to gap; gap to source | the card's `gaps` |
| `similar_to` | technology, technology | cosine similarity of embeddings, from `refresh_similarity()` |

Every edge except `similar_to` is a recorded fact or a named matching rule with its evidence in `props`; the
graph adds nothing that is not in the catalog, cards, register or documents. `python tools/load_postgres.py
--dump-graph build/graph` writes the same graph as `nodes.jsonl` and `edges.jsonl` for any other graph tool.

## Load it

```
pip install -r requirements-postgres.txt
export DATABASE_URL='postgresql://user:password@host/dbname?sslmode=require'   # never commit this
python tools/load_postgres.py
```

Against Neon, load with the **unpooled** owner connection string; the pooled read-only DSN is for the
server afterwards (see the next section). The load replaces every table in one transaction and runs
inside a psycopg pipeline, which batches the round trips over the WAN: it finishes in about half a
minute, where per-row round trips took 13+ minutes and the connection usually died first.
Because pipeline mode rejects multi-command strings, `db/schema.sql` is executed one statement at a
time. Rules the load keeps:

- Only text with an open licence (`reuse_level: full-text-open`) is loaded. Restricted documents get a metadata row and no passages, because a hosted database may be read by others. `--include-restricted` is for a database that nobody else can reach.
- Embeddings come from the local index `build/library.db` when it has them — run `python agent/library.py build && python agent/embed.py` **before** the load (on the Mac, where fastembed is installed). `--embeddings fastembed` computes them during the load instead. Without either, the database still works with keyword search and the graph; load again once embeddings exist.
- No secrets in the repository: the connection string stays in `DATABASE_URL` or a password manager.

## Read-only access for the MCP server and the web UI

The server never connects as the owner. Run this once, against the **owner** DSN, to create the
read-only role from [db/readonly.sql](../db/readonly.sql) and print the DSNs to use with it:

```
export DATABASE_URL='postgresql://owner:password@host/dbname?sslmode=require'   # owner DSN
export OG_READONLY_PASSWORD='<at least 16 characters>'
python tools/load_postgres.py --grant-readonly
```

The command also sets the role's password and `GRANT CONNECT` itself, so no secret is in the file or
the repository. It is idempotent. The printed **pooled** read-only DSN is the one the server uses:
keep it at `~/.config/og-tech-library/db-readonly.url` (mode 600, never in the repo) and set it as
the Cloudflare secret (`tr -d '\n' < ~/.config/og-tech-library/db-readonly.url | npx wrangler secret
put DATABASE_URL`, see docs/HOSTING.md).

Three layers protect the database:

| Layer | What it enforces |
| --- | --- |
| Role grants | `og_mcp_read` gets `USAGE` on schema `og` and `SELECT` on all its tables, current and future (default privileges); no INSERT, UPDATE, DELETE or DDL |
| Role settings | `ALTER ROLE og_mcp_read SET default_transaction_read_only = on` and `statement_timeout = '15s'`, so even a future grant mistake cannot write or hang |
| `agent/pg.py` | Every statement is one comment-free `SELECT`/`WITH` (banned keywords rejected), run in its own `READ ONLY` transaction that starts with `SET LOCAL statement_timeout` and `SET LOCAL search_path` (the only SET forms the pooler cannot lose); at most 500 rows and 2,000 characters per cell |

Who uses the role: the MCP tools `sql_query`, `db_catalog` and `graph_neighbors` (they answer
`database not configured` when `DATABASE_URL` is unset), and the web pages under `/database` — row
counts, the SQL console, hybrid search and the graph browser.

The Neon project holding the data: `patient-dew-83888795`, branch `production`, region
`ap-southeast-1` (Singapore).

## Neon

Done, 2026-10-26: project `patient-dew-83888795` (branch `production`, region `ap-southeast-1` —
Singapore), Postgres 18.6. `db/schema.sql` creates the pgvector and pg_trgm extensions. Loaded:
348 sources, 168 documents (133 with text; restricted ones are metadata-only rows), 9,835 chunks,
293 cards, 300 register entries, 3,093 nodes and 8,982 edges.

What was done once (repeat only for a new project):

1. Create the project at neon.tech, region Singapore; copy both owner connection strings from the dashboard (pooled and unpooled, `sslmode=require`).
2. Store them in `.env.local` (gitignored): `DATABASE_URL` (pooled) and `DATABASE_URL_UNPOOLED` (for loads).
3. `pip install -r requirements-postgres.txt`, then load with `DATABASE_URL_UNPOOLED` (see *Load it* above).
4. `OG_READONLY_PASSWORD=... python tools/load_postgres.py --grant-readonly` against the owner DSN; keep the printed pooled read-only DSN at `~/.config/og-tech-library/db-readonly.url` and as the Cloudflare secret `DATABASE_URL`.

Refresh after cards or documents change (on the Mac, where fastembed is installed):

```
git pull
python tools/build.py
python agent/library.py build
python agent/embed.py                     # skip for a keyword-only refresh
DATABASE_URL="$DATABASE_URL_UNPOOLED" python tools/load_postgres.py
```

## Example queries

```sql
SET search_path = og, public;

-- Cards that cite the same sources as one card
SELECT * FROM v_technology_co_citation WHERE a = 'ccs-cryogenic' OR b = 'ccs-cryogenic';

-- Everything within two hops of CO2-EOR through citations and suppliers
SELECT * FROM graph_neighbors('technology:ups-co2-eor', 2, ARRAY['cites', 'supplied_by', 'mentions']);

-- Keyword search (pass a query vector as the second argument for semantic ranking)
SELECT * FROM hybrid_search('CO2 storage Malay Basin', NULL, 10);

-- What is still missing for upstream cards, and why
SELECT name, field, item, reason_code, action FROM v_gap WHERE sector = 'UPS' ORDER BY name;

-- Semantic neighbours of a card
SELECT dst, weight FROM edge WHERE src = 'technology:h2-lohc' AND rel = 'similar_to' ORDER BY weight DESC;
```

## Tests

`python -m pytest -q tests/test_graph.py` checks the graph without a database. Set `TEST_DATABASE_URL` to a
scratch Postgres with pgvector to also run the load test (it truncates schema `og`).
