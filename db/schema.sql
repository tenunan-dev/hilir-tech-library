-- Postgres schema for the O&G technology library: relational tables, pgvector embeddings,
-- full-text search and a property-graph layer (node, edge) that links every entry to the others.
-- Works on plain Postgres 15+ with the pgvector extension, and on Neon (run CREATE EXTENSION vector once).
-- Loaded by tools/load_postgres.py, which truncates and refills the tables, so nothing in
-- the database is hand-edited. Embedding size 384 matches BAAI/bge-small-en-v1.5; for another model,
-- change every vector(384) here and re-embed.

CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE SCHEMA IF NOT EXISTS og;
SET search_path = og, public;

-- ---------------------------------------------------------------- catalog
CREATE TABLE IF NOT EXISTS source (
    id               text PRIMARY KEY,
    name             text NOT NULL,
    url              text NOT NULL,
    source_type      text NOT NULL,
    publisher_org    text NOT NULL,
    country          text,
    access           text NOT NULL,
    licence          text NOT NULL,
    reuse_level      text NOT NULL,
    permitted_use    text,
    automated_access text,
    quality_tier     integer,
    verification     text NOT NULL,
    last_verified    date,
    update_frequency text,
    notes            text,
    record           jsonb NOT NULL,
    embedding        vector(384),
    tsv              tsvector GENERATED ALWAYS AS (
                       to_tsvector('english', name || ' ' || publisher_org || ' ' || source_type || ' ' || coalesce(notes, ''))) STORED
);
CREATE TABLE IF NOT EXISTS source_tag (
    source_id text NOT NULL REFERENCES source(id) ON DELETE CASCADE,
    kind      text NOT NULL CHECK (kind IN ('sector', 'discipline', 'region')),
    code      text NOT NULL,
    PRIMARY KEY (source_id, kind, code)
);

-- ---------------------------------------------------------------- corpus
CREATE TABLE IF NOT EXISTS document (
    id            text PRIMARY KEY,                 -- path under the repo, e.g. corpus/netl/name-hash.md
    source_id     text REFERENCES source(id) ON DELETE SET NULL,
    title         text,
    url           text,
    licence       text,
    reuse_level   text,
    retrieved_at  timestamptz,
    sha256        text,
    sectors       text[] NOT NULL DEFAULT '{}',
    text_included boolean NOT NULL DEFAULT false,   -- false: metadata only (restricted text stays private)
    summary       text,                             -- our own short summary, never copied text
    body          text,                             -- full text, open-licence documents only (text_included); NULL otherwise
    meta          jsonb NOT NULL
);
CREATE INDEX IF NOT EXISTS document_source_idx ON document (source_id);

CREATE TABLE IF NOT EXISTS chunk (
    id          text PRIMARY KEY,                   -- <document id>#<n>, same ids as the SQLite index
    document_id text NOT NULL REFERENCES document(id) ON DELETE CASCADE,
    ord         integer NOT NULL,
    title       text,
    body        text NOT NULL,
    embedding   vector(384),
    tsv         tsvector GENERATED ALWAYS AS (to_tsvector('english', coalesce(title, '') || ' ' || body)) STORED
);
CREATE INDEX IF NOT EXISTS chunk_tsv_idx ON chunk USING gin (tsv);

-- ---------------------------------------------------------------- technology cards
CREATE TABLE IF NOT EXISTS technology (
    id            text PRIMARY KEY,
    name          text NOT NULL,
    sector        text NOT NULL,
    category      text NOT NULL,
    maturity      text NOT NULL,
    principle     text NOT NULL,
    trl_low       integer,
    trl_high      integer,
    last_reviewed date NOT NULL,
    card          jsonb NOT NULL,                   -- the full card, as in catalog/technologies
    embedding     vector(384),
    tsv           tsvector GENERATED ALWAYS AS (
                    to_tsvector('english', name || ' ' || category || ' ' || principle)) STORED
);
CREATE INDEX IF NOT EXISTS technology_tsv_idx ON technology USING gin (tsv);
CREATE INDEX IF NOT EXISTS technology_sector_idx ON technology (sector, maturity);

CREATE TABLE IF NOT EXISTS technology_alias (
    technology_id text NOT NULL REFERENCES technology(id) ON DELETE CASCADE,
    alias         text NOT NULL,
    PRIMARY KEY (technology_id, alias)
);
CREATE TABLE IF NOT EXISTS technology_source (
    technology_id text NOT NULL REFERENCES technology(id) ON DELETE CASCADE,
    url           text NOT NULL,
    source_id     text REFERENCES source(id) ON DELETE SET NULL,
    note          text,
    PRIMARY KEY (technology_id, url)
);
CREATE TABLE IF NOT EXISTS technology_figure (        -- performance and cost figures, each with basis and source
    id            bigserial PRIMARY KEY,
    technology_id text NOT NULL REFERENCES technology(id) ON DELETE CASCADE,
    kind          text NOT NULL CHECK (kind IN ('performance', 'cost')),
    metric        text NOT NULL,
    low           double precision,
    high          double precision,
    unit          text NOT NULL,
    year          integer,
    basis         text NOT NULL,
    source_url    text NOT NULL
);
CREATE TABLE IF NOT EXISTS technology_supplier (
    technology_id text NOT NULL REFERENCES technology(id) ON DELETE CASCADE,
    supplier      text NOT NULL,
    product       text,
    source_id     text REFERENCES source(id) ON DELETE SET NULL,
    PRIMARY KEY (technology_id, supplier)
);
CREATE TABLE IF NOT EXISTS technology_gap (            -- missing inputs, with why and where to get them
    id            bigserial PRIMARY KEY,
    technology_id text NOT NULL REFERENCES technology(id) ON DELETE CASCADE,
    field         text NOT NULL,
    item          text NOT NULL,
    reason_code   text NOT NULL,
    reason        text NOT NULL,
    action        text NOT NULL,
    blocked_by    text,
    "where"       jsonb NOT NULL DEFAULT '[]'
);

CREATE TABLE IF NOT EXISTS vendor (                    -- curated vendor directory records
    id           text PRIMARY KEY,
    name         text NOT NULL,
    aliases      text[] NOT NULL DEFAULT '{}',          -- alternate names, also matched by the coverage queue
    country      text,
    roles        text[] NOT NULL DEFAULT '{}',         -- oem, licensor, packager, epc, developer, operator, ...
    description  text NOT NULL,
    products     text[] NOT NULL DEFAULT '{}',
    url          text,
    technologies text[] NOT NULL DEFAULT '{}',         -- ids of the technology cards this vendor supplies
    embedding    vector(384),
    tsv          tsvector GENERATED ALWAYS AS (
                    to_tsvector('english', name || ' ' || coalesce(country, '') || ' ' || description)) STORED
);
CREATE INDEX IF NOT EXISTS vendor_tsv_idx ON vendor USING gin (tsv);

CREATE TABLE IF NOT EXISTS equipment (                     -- curated equipment catalog records
    id              text PRIMARY KEY,
    name            text NOT NULL,
    equipment_type  text NOT NULL,                         -- equipment family, e.g. boiler
    sector          text,
    sector_codes    text[] NOT NULL DEFAULT '{}',
    description     text NOT NULL,
    specifications  jsonb NOT NULL DEFAULT '[]',           -- metric, range/value, unit, basis, source
    vendor_models   jsonb NOT NULL DEFAULT '[]',           -- per-vendor model lines with stated ranges
    vendors         text[] NOT NULL DEFAULT '{}',          -- vendor directory ids supplying this class
    technologies    text[] NOT NULL DEFAULT '{}',          -- technology cards using this class
    gaps            jsonb NOT NULL DEFAULT '[]',
    sources         jsonb NOT NULL DEFAULT '[]',           -- the record's own sources (url, note)
    embedding       vector(384),
    tsv             tsvector GENERATED ALWAYS AS (
                      to_tsvector('english', name || ' ' || description)) STORED
);
CREATE INDEX IF NOT EXISTS equipment_tsv_idx ON equipment USING gin (tsv);

CREATE TABLE IF NOT EXISTS register_entry (            -- the indicative register of about 300 technologies
    id       text PRIMARY KEY,
    sector   text NOT NULL,
    area     text NOT NULL,
    name     text NOT NULL,
    maturity text NOT NULL,
    examples text,
    card_id  text REFERENCES technology(id) ON DELETE SET NULL
);

-- ---------------------------------------------------------------- knowledge graph
-- Node ids are "<kind>:<key>": source:netl, document:corpus/netl/x.md, technology:ccs-cryogenic,
-- register:CCS/..., org:honeywell-uop, vendor:wartsila, sector:CCS, discipline:PRC, region:sea,
-- country:MY, gap:<card>:<n>.
CREATE TABLE IF NOT EXISTS node (
    id        text PRIMARY KEY,
    kind      text NOT NULL,
    label     text NOT NULL,
    props     jsonb NOT NULL DEFAULT '{}',
    embedding vector(384)
);
CREATE INDEX IF NOT EXISTS node_kind_idx ON node (kind);
CREATE INDEX IF NOT EXISTS node_label_trgm_idx ON node USING gin (label gin_trgm_ops);

-- Relations: published_by, in_sector, covers_discipline, in_region, in_country, from_source, cites,
-- cites_document, supplied_by, realises, example_supplier, alternative_to, mentions, has_gap, look_in,
-- supplies (vendor record to the cards it supplies), supplies_equipment (equipment class to vendor),
-- uses_equipment (card to equipment class), alias_of (free-text org to its curated vendor
-- record), similar_to (semantic, from refresh_similarity).
CREATE TABLE IF NOT EXISTS edge (
    src    text NOT NULL REFERENCES node(id) ON DELETE CASCADE,
    dst    text NOT NULL REFERENCES node(id) ON DELETE CASCADE,
    rel    text NOT NULL,
    weight double precision NOT NULL DEFAULT 1,
    props  jsonb NOT NULL DEFAULT '{}',
    PRIMARY KEY (src, dst, rel)
);
CREATE INDEX IF NOT EXISTS edge_dst_idx ON edge (dst, rel);

-- ---------------------------------------------------------------- indexes for vectors
-- Created by the loader after the data is in (building HNSW on an empty table is wasted work), but safe to run here.
CREATE INDEX IF NOT EXISTS chunk_embedding_idx ON chunk USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS technology_embedding_idx ON technology USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS node_embedding_idx ON node USING hnsw (embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS source_tsv_idx ON source USING gin (tsv);
CREATE INDEX IF NOT EXISTS source_embedding_idx ON source USING hnsw (embedding vector_cosine_ops);

-- ---------------------------------------------------------------- upgrades
-- Idempotent upgrades for databases created by older schema versions; the loader re-runs this
-- file on every load, and each statement is a no-op once applied (2026-10-31, decision #34 Phase 0).
ALTER TABLE document ADD COLUMN IF NOT EXISTS body text;
ALTER TABLE vendor ADD COLUMN IF NOT EXISTS aliases text[] NOT NULL DEFAULT '{}';
ALTER TABLE equipment ADD COLUMN IF NOT EXISTS sources jsonb NOT NULL DEFAULT '[]';
ALTER TABLE source ADD COLUMN IF NOT EXISTS embedding vector(384);
ALTER TABLE source ADD COLUMN IF NOT EXISTS tsv tsvector GENERATED ALWAYS AS (
    to_tsvector('english', name || ' ' || publisher_org || ' ' || source_type || ' ' || coalesce(notes, ''))) STORED;

-- ---------------------------------------------------------------- views and functions
-- Technologies that cite the same source: a quick way to find related cards.
CREATE OR REPLACE VIEW v_technology_co_citation AS
SELECT a.technology_id AS a, b.technology_id AS b, count(*) AS shared_sources
FROM technology_source a
JOIN technology_source b ON a.url = b.url AND a.technology_id < b.technology_id
GROUP BY 1, 2;

-- Everything missing, with the reason and where to look.
CREATE OR REPLACE VIEW v_gap AS
SELECT t.id AS technology_id, t.name, t.sector, g.field, g.item, g.reason_code, g.reason, g."where", g.action, g.blocked_by
FROM technology_gap g JOIN technology t ON t.id = g.technology_id
UNION ALL
SELECT NULL, r.name, r.sector, 'card', 'technology card', 'no_card_yet',
       'Listed in the register but no card has been written.', '[]'::jsonb, 'Write a card.', NULL
FROM register_entry r WHERE r.card_id IS NULL;

-- Walk the graph from one node. rels = NULL follows every relation, in both directions.
-- Example: SELECT * FROM graph_neighbors('technology:ccs-cryogenic', 2, ARRAY['cites','supplied_by']);
CREATE OR REPLACE FUNCTION graph_neighbors(start_id text, max_depth integer DEFAULT 2, rels text[] DEFAULT NULL)
RETURNS TABLE (node_id text, kind text, label text, depth integer, via text[]) LANGUAGE sql STABLE AS $$
    WITH RECURSIVE walk(node_id, depth, via, seen) AS (
        SELECT start_id, 0, ARRAY[]::text[], ARRAY[start_id]
        UNION ALL
        SELECT n.next_id, w.depth + 1, w.via || n.rel, w.seen || n.next_id
        FROM walk w
        JOIN LATERAL (
            SELECT e.dst AS next_id, e.rel FROM edge e WHERE e.src = w.node_id AND (rels IS NULL OR e.rel = ANY (rels))
            UNION ALL
            SELECT e.src, e.rel FROM edge e WHERE e.dst = w.node_id AND (rels IS NULL OR e.rel = ANY (rels))
        ) n ON true
        WHERE w.depth < max_depth AND NOT n.next_id = ANY (w.seen)
    )
    SELECT DISTINCT ON (w.node_id) w.node_id, x.kind, x.label, w.depth, w.via
    FROM walk w JOIN node x ON x.id = w.node_id
    WHERE w.depth > 0
    ORDER BY w.node_id, w.depth;
$$;

-- Hybrid search over passages, cards, vendor records, equipment classes and catalog sources:
-- reciprocal rank fusion of full-text and vector ranks. qvec may be NULL (keyword only); sector
-- (optional) narrows to one taxonomy code, matching how the SQLite search filters each kind.
-- Example: SELECT * FROM hybrid_search('CO2 storage Malay Basin', NULL, 10);
CREATE OR REPLACE FUNCTION hybrid_search(q text, qvec vector(384) DEFAULT NULL, k integer DEFAULT 10, sector text DEFAULT NULL)
RETURNS TABLE (kind text, ref text, title text, score double precision) LANGUAGE sql STABLE AS $$
    WITH items AS (
        SELECT 'chunk'::text AS kind, c.id AS ref, c.title, c.tsv, c.embedding, d.sectors
        FROM chunk c JOIN document d ON d.id = c.document_id
        UNION ALL
        SELECT 'technology', t.id, t.name, t.tsv, t.embedding, ARRAY[t.sector] FROM technology t
        UNION ALL
        SELECT 'vendor', v.id, v.name, v.tsv, v.embedding,
               (SELECT array_agg(DISTINCT t.sector) FROM technology t WHERE t.id = ANY (v.technologies))
        FROM vendor v
        UNION ALL
        SELECT 'equipment', e.id, e.name, e.tsv, e.embedding, e.sector_codes FROM equipment e
        UNION ALL
        SELECT 'source', s.id, s.name, s.tsv, s.embedding,
               (SELECT array_agg(code) FROM source_tag st WHERE st.source_id = s.id AND st.kind = 'sector')
        FROM source s
    ),
    tq AS (SELECT websearch_to_tsquery('english', regexp_replace(trim(q), '\s+', ' or ', 'g')) AS query),
    kw AS (
        SELECT kind, ref, row_number() OVER (ORDER BY ts_rank_cd(tsv, tq.query) DESC) AS r
        FROM items, tq WHERE tsv @@ tq.query AND (sector IS NULL OR sector = ANY (sectors)) LIMIT 50
    ),
    vec AS (
        SELECT kind, ref, row_number() OVER (ORDER BY embedding <=> qvec) AS r
        FROM items WHERE qvec IS NOT NULL AND embedding IS NOT NULL AND (sector IS NULL OR sector = ANY (sectors))
        ORDER BY embedding <=> qvec LIMIT 50
    ),
    fused AS (
        SELECT kind, ref, sum(1.0 / (60 + r)) AS score FROM (SELECT * FROM kw UNION ALL SELECT * FROM vec) u GROUP BY kind, ref
    )
    SELECT f.kind, f.ref, i.title, f.score
    FROM fused f JOIN items i ON i.kind = f.kind AND i.ref = f.ref
    ORDER BY f.score DESC LIMIT k;
$$;

-- Add semantic similar_to edges between technology cards: each card gets edges to its k nearest
-- cards by cosine similarity above min_sim. Re-run after embeddings change.
CREATE OR REPLACE FUNCTION refresh_similarity(k integer DEFAULT 5, min_sim double precision DEFAULT 0.6)
RETURNS integer LANGUAGE plpgsql AS $$
DECLARE n integer;
BEGIN
    DELETE FROM edge WHERE rel = 'similar_to';
    INSERT INTO edge (src, dst, rel, weight, props)
    SELECT 'technology:' || a.id, 'technology:' || nn.id, 'similar_to', nn.sim, '{"method": "embedding cosine"}'
    FROM technology a
    CROSS JOIN LATERAL (
        SELECT b.id, 1 - (a.embedding <=> b.embedding) AS sim
        FROM technology b WHERE b.id <> a.id AND b.embedding IS NOT NULL
        ORDER BY a.embedding <=> b.embedding LIMIT k
    ) nn
    WHERE a.embedding IS NOT NULL AND nn.sim >= min_sim
    ON CONFLICT DO NOTHING;
    GET DIAGNOSTICS n = ROW_COUNT;
    RETURN n;
END $$;
