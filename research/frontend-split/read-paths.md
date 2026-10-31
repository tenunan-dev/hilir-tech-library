# Frontend read paths → Neon mapping (Phase 0 audit, P0.1)

2026-10-31. Every `agent/web.py` handler, what it reads today, and its Neon counterpart or gap.
Read paths verified against the code (web.py, server.py, library.py, pg.py, technologies.py,
vendors.py, equipment.py, embed.py, embed_client.py, tools/load_postgres.py, db/schema.sql)
and against live Neon (`\d og.*` over the pooled DSN on 2026-10-31).

Data sources today, as used by the web tier:

- **SQLite** — `server.db()` opens `build/library.db` (built into the container image; `server.db()`
  even builds it on demand). Tables: `sources`, `docs`, `search` (FTS5), `vectors`, `technologies`,
  `vendors`, `equipment`, `info`.
- **Neon (schema og)** — `pg.py` over `$DATABASE_URL` (read-only role `og_mcp_read` in production).
- **Disk** — `catalog/*.json`, `catalog/technology-register.yaml`, `corpus/**/*.md` via the
  `technologies` / `vendors` / `equipment` loader modules and `library.read_document`.
- **User store** — a separate Postgres DSN riding the `x-user-store-dsn` header (`userstore.py`,
  db/library.sql) plus the `LIBRARY_USERS` secret. Not schema `og`; unaffected by the split
  (the frontend Worker keeps `USER_STORE_URL`).

## Route-by-route mapping

| Route | Handler reads today | Neon counterpart | Gap / note |
| --- | --- | --- | --- |
| `/` | `tools.library_stats()` → SQLite `stats()` | `pg.counts()` + per-table `count(embedding)` | No `vectors` number or `embedding_model` in Neon; compute embeddings on chunk/technology/vendor/equipment, omit model key (home skips None). SQLite's vector count also counts `source` rows, which Neon does not embed — number will differ slightly (expected). |
| `/login`, `/logout` | userstore + `LIBRARY_USERS` secret | none needed | Stays as is; both forms always render (owner decision 2026-10-27). |
| `/search` | `tools.search()` SQLite FTS5+vector fusion; SQLite `vectors` count for the badge; `embed_client` (local fastembed or edge `/__embed`) | `pg.hybrid_search()` | **Two gaps.** (1) `hybrid_search` has no `source` kind (SQLite indexes source rows). (2) Result rows carry only kind/ref/title/score; the page renders licence, reuse_level, url, regions/sectors (source), snippet/summary (chunk), country/roles/products/technologies (vendor), equipment_type/vendors (equipment). Also no sector filter. Fix: extend the SQL function (add `source` items, optional `sector`), then enrich rows per-kind in `pg.py` with one query per kind; design shared with the later backend MCP search move (plan §2). |
| `/technologies` | `tools.compare_technologies()` → SQLite `technologies` + `technologies.compare()` (pure) | `SELECT card FROM og.technology` → same pure `compare()` | None. Card jsonb holds everything compare() reads. |
| `/technologies/{id}` | `tools.get_technology()` → SQLite card + `technologies.mermaid()` (pure) | og.technology.card jsonb + mermaid() | None. Licence overlay (TECHNOLOGY_LICENCE) is added in code. |
| `/vendors` | `tools.list_vendors()` SQLite; `tools.compare_technologies()` for card names; `_coverage_queue()` reads catalog from **disk** | og.vendor rows (+ og.technology names; coverage queue from og.technology.card suppliers + og.vendor name/aliases) | **Gap:** og.vendor has no `aliases` column; the coverage-queue classifier (`vendors.vendor_keys`) matches on name+aliases. Add `aliases text[]`. Page also renders only id/name/country/roles/products/url/technologies — all present. |
| `/equipment` | `tools.list_equipment()` SQLite; vendor+card name maps; **detail read from disk** (`equipment_records.load_equipment()`) | og.equipment rows; detail from columns | **Gap:** og.equipment has no `sources` column; the detail panel renders the record's `sources` list (url+note). Add `sources jsonb`. `specifications`, `vendor_models`, `gaps`, `vendors`, `technologies`, `description` all present. |
| `/register` | `tools.list_technology_register()` → `technologies.load_register()` reads the **disk** YAML | og.register_entry (code, area, name, maturity, examples, card_id) | None — the table already mirrors the YAML (306 entries live). |
| `/sources` | `tools.list_by_tag()` SQLite | og.source + og.source_tag | None. Region/reuse/sector filtering and the sea/apac-first sort re-implementable from tags. |
| `/sources/{id}` | `tools.get_source()` SQLite record + docs list, restricted-doc filter | og.source.record jsonb + og.document (title/url/reuse_level) | None. |
| `/documents?path=` | `tools.get_document()` → SQLite docs row + **disk read of the .md body** | og.document (meta jsonb, summary, text_included) | **Gap (the known one): no full text in Neon.** 202 of 317 live documents have `text_included=true` but their text exists only as og.chunk bodies (which lose exact formatting; chunk 0 in SQLite is summary-prefixed, in Neon it is not). Fix: add `document.body text`, loader fills it only when `text_included` (restricted docs stay NULL), web renders the stored body and shows the private-copy notice when NULL. |
| `/gaps` | `tools.list_gaps()` SQLite cards + register | og.v_gap (already UNIONs register entries with no card) | None — v_gap carries technology_id, name, sector, field, item, reason_code, reason, `where` jsonb, action, blocked_by. Sector/field filters become WHERE clauses. |
| `/database` | `pg.counts()`, `pg.tables_doc()` | already Neon | None. |
| `/database/sql` | `pg.run_sql()` | already Neon | None. |
| `/database/search` | `pg.hybrid_search()` + local fastembed or edge `/__embed` | already Neon | None (shares the /search function extension once made; keeps working unchanged meanwhile). |
| `/database/graph` + `/overview.json` `/nodes.json` `/neighborhood.json` `/center.json` | `pg.graph_overview/node_search/neighborhood/top_node` | already Neon | None. |
| `/account`, `/admin`, `/admin/*` | userstore (separate DSN) + `LIBRARY_USERS` secret | none needed | Stays as is. |

## Non-route helpers the split touches

- `web.is_web_path` / `PREFIXES` — must stay in sync with the frontend Worker's `UI_PREFIXES`
  (note: worker list is missing `/equipment` today — fix when the split lands).
- `server.db()` auto-builds the SQLite index when missing; after Phase 1 no page may call it on
  the correctness path (SQLite becomes the automatic fallback only).
- `embed_client.query_vector` — falls back to the edge `/__embed`; after the split both containers
  embed queries locally with fastembed (model cache already in the image), edge call retired (P3.1).
- REST `/api/*` and MCP tools (backend container) still call the `library.*` SQLite functions;
  the plan moves only *search* to Neon hybrid_search at split time (§2). Documented consequence:
  backend `get_*`/`list_*` tools read the image's SQLite, rebuilt at each backend deploy; search-grade
  data freshness (incl. new vendors) comes from Neon. Frontend pages after Phase 1 show data without
  any deploy (the plan's §4 goal).

## Schema gaps to close (P0.2 migration, all idempotent in db/schema.sql + tools/load_postgres.py)

1. `og.document.body text` — full body text, written only when `text_included` (open licence);
   NULL otherwise. (Restricted text keeps staying private; the read-only role serves NULL.)
2. `og.vendor.aliases text[] NOT NULL DEFAULT '{}'` — coverage-queue matching + get_vendor parity.
3. `og.equipment.sources jsonb NOT NULL DEFAULT '[]'` — the equipment page's Sources section.
4. `hybrid_search`: add the `source` kind and an optional `sector` filter; enrich per-kind fields
   in `pg.py` (SQL function keeps kind/ref/title/score and gains nothing else — enrichment happens
   outside so the MCP `sql_query` surface stays stable).
5. `library_stats` vectors: `count(*)` per embedding column, summed; no `embedding_model` key.

## Live Neon verification (2026-10-31, pooled read DSN)

- Tables/cols confirmed equal to db/schema.sql for all 15 tables; views `v_gap`,
  `v_technology_co_citation`; functions `graph_neighbors`, `hybrid_search`, `refresh_similarity`.
- Confirmed missing, as predicted: `document.body`, `vendor.aliases`, `equipment.sources`.
- Counts seen: register_entry 306; documents with text_included=true: 202.
