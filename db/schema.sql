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
    body          text,                             -- full text, open-licence documents only (text_included), NULL otherwise
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
    search_text   text NOT NULL DEFAULT '',         -- the card's index text (agent/technologies.search_text)
    embedding     vector(384),
    -- The name is weighted above the body, and the body is the SAME string the SQLite index
    -- carries, so the two search paths cannot index different words. A card written in CO2 where
    -- the user types "carbon" is bridged by og.search_concept at query time, not by rewriting cards.
    tsv           tsvector GENERATED ALWAYS AS (
                    setweight(to_tsvector('english', name), 'A') ||
                    setweight(to_tsvector('english', search_text), 'B')) STORED
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
    record       jsonb NOT NULL DEFAULT '{}'::jsonb,   -- the full catalog record, as in catalog/vendors
    search_text  text NOT NULL DEFAULT '',             -- index text (agent/library.vendor_text)
    embedding    vector(384),
    tsv          tsvector GENERATED ALWAYS AS (
                    setweight(to_tsvector('english', name), 'A') ||
                    setweight(to_tsvector('english', search_text), 'B')) STORED
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
    record          jsonb NOT NULL DEFAULT '{}'::jsonb,    -- the full catalog record, as in catalog/equipment
    search_text     text NOT NULL DEFAULT '',              -- index text (agent/library.equipment_text)
    embedding       vector(384),
    tsv             tsvector GENERATED ALWAYS AS (
                      setweight(to_tsvector('english', name), 'A') ||
                      setweight(to_tsvector('english', search_text), 'B')) STORED
);
CREATE INDEX IF NOT EXISTS equipment_tsv_idx ON equipment USING gin (tsv);

CREATE TABLE IF NOT EXISTS project (                        -- curated project and operating-plant records
    id            text PRIMARY KEY,
    name          text NOT NULL,
    project_type  text,                                    -- greenfield, expansion, retrofit, operating-asset
    sector        text,
    sector_codes  text[] NOT NULL DEFAULT '{}',
    country       text,
    location      text,
    status        text NOT NULL,                           -- proposed, FID, under-construction, commissioning, operating, suspended, decommissioned
    description   text NOT NULL,
    capacities    jsonb NOT NULL DEFAULT '[]',             -- rated capacity per metric, phases separated
    capex         jsonb NOT NULL DEFAULT '[]',             -- announced capital cost figures, each with dollar year
    owners        jsonb NOT NULL DEFAULT '[]',             -- owners, sponsors, JV partners
    contractors   jsonb NOT NULL DEFAULT '[]',             -- EPC, FEED, construction and O&M contractors
    offtakers     jsonb NOT NULL DEFAULT '[]',
    technologies  text[] NOT NULL DEFAULT '{}',            -- technology cards this project deploys
    milestones    jsonb NOT NULL DEFAULT '[]',             -- dated milestones, each with its source
    gaps          jsonb NOT NULL DEFAULT '[]',
    sources       jsonb NOT NULL DEFAULT '[]',             -- the record's own sources (url, note)
    record        jsonb NOT NULL DEFAULT '{}'::jsonb,      -- the full catalog record, as in catalog/projects
    search_text   text NOT NULL DEFAULT '',                -- index text (agent/library.project_text)
    embedding     vector(384),
    tsv           tsvector GENERATED ALWAYS AS (
                    setweight(to_tsvector('english', name), 'A') ||
                    setweight(to_tsvector('english', search_text), 'B')) STORED
);
CREATE INDEX IF NOT EXISTS project_tsv_idx ON project USING gin (tsv);

CREATE TABLE IF NOT EXISTS register_entry (            -- the indicative technology register (see library_stats for the live count)
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

-- ---------------------------------------------------------------- upgrades
-- Idempotent upgrades for databases created by older schema versions; the loader re-runs this
-- file on every load, and each statement is a no-op once applied (2026-10-31, decision #34 Phase 0).
-- The source tsv/embedding indexes live here too, after the columns they need exist on old databases.
ALTER TABLE document ADD COLUMN IF NOT EXISTS body text;
ALTER TABLE vendor ADD COLUMN IF NOT EXISTS aliases text[] NOT NULL DEFAULT '{}';
ALTER TABLE equipment ADD COLUMN IF NOT EXISTS sources jsonb NOT NULL DEFAULT '[]';
ALTER TABLE source ADD COLUMN IF NOT EXISTS embedding vector(384);
ALTER TABLE source ADD COLUMN IF NOT EXISTS tsv tsvector GENERATED ALWAYS AS (
    to_tsvector('english', name || ' ' || publisher_org || ' ' || source_type || ' ' || coalesce(notes, ''))) STORED;
CREATE INDEX IF NOT EXISTS source_tsv_idx ON source USING gin (tsv);
CREATE INDEX IF NOT EXISTS source_embedding_idx ON source USING hnsw (embedding vector_cosine_ops);
-- full catalog records so the get_* tools serve everything without a column per field
ALTER TABLE vendor ADD COLUMN IF NOT EXISTS record jsonb NOT NULL DEFAULT '{}'::jsonb;
ALTER TABLE equipment ADD COLUMN IF NOT EXISTS record jsonb NOT NULL DEFAULT '{}'::jsonb;
-- 2026-11-23: the four curated record kinds are full-text indexed by the text the loader writes
-- (the same string the SQLite index carries), with the name weighted above the body. Rewrites a
-- small table each run (about 1,150 rows across the four) and is a no-op on a fresh database.
ALTER TABLE technology ADD COLUMN IF NOT EXISTS search_text text NOT NULL DEFAULT '';
ALTER TABLE vendor     ADD COLUMN IF NOT EXISTS search_text text NOT NULL DEFAULT '';
ALTER TABLE equipment  ADD COLUMN IF NOT EXISTS search_text text NOT NULL DEFAULT '';
ALTER TABLE project    ADD COLUMN IF NOT EXISTS search_text text NOT NULL DEFAULT '';
DROP INDEX IF EXISTS technology_tsv_idx;
DROP INDEX IF EXISTS vendor_tsv_idx;
DROP INDEX IF EXISTS equipment_tsv_idx;
DROP INDEX IF EXISTS project_tsv_idx;
ALTER TABLE technology DROP COLUMN IF EXISTS tsv;
ALTER TABLE vendor     DROP COLUMN IF EXISTS tsv;
ALTER TABLE equipment  DROP COLUMN IF EXISTS tsv;
ALTER TABLE project    DROP COLUMN IF EXISTS tsv;
ALTER TABLE technology ADD COLUMN tsv tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('english', name), 'A') ||
    setweight(to_tsvector('english', search_text), 'B')) STORED;
ALTER TABLE vendor ADD COLUMN tsv tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('english', name), 'A') ||
    setweight(to_tsvector('english', search_text), 'B')) STORED;
ALTER TABLE equipment ADD COLUMN tsv tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('english', name), 'A') ||
    setweight(to_tsvector('english', search_text), 'B')) STORED;
ALTER TABLE project ADD COLUMN tsv tsvector GENERATED ALWAYS AS (
    setweight(to_tsvector('english', name), 'A') ||
    setweight(to_tsvector('english', search_text), 'B')) STORED;
CREATE INDEX IF NOT EXISTS technology_tsv_idx ON technology USING gin (tsv);
CREATE INDEX IF NOT EXISTS vendor_tsv_idx ON vendor USING gin (tsv);
CREATE INDEX IF NOT EXISTS equipment_tsv_idx ON equipment USING gin (tsv);
CREATE INDEX IF NOT EXISTS project_tsv_idx ON project USING gin (tsv);
-- the pre-2026-11-03 hybrid_search had four arguments; CREATE OR REPLACE cannot change a
-- signature, so the old overload is dropped explicitly (no-op once gone)
DROP FUNCTION IF EXISTS hybrid_search(text, vector, integer, text);
-- the pre-2026-10-31 hybrid_search had three arguments; CREATE OR REPLACE cannot change a
-- signature, so the old overload is dropped explicitly (no-op once gone)
DROP FUNCTION IF EXISTS hybrid_search(text, vector, integer);

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

-- Concept groups the query is expanded through: a query word is replaced by every term of its
-- group, and ranking counts CONCEPTS matched rather than words. Seeded from
-- catalog/search-concepts.yaml by tools/load_postgres.py (the SQLite path reads the same file),
-- so "carbon" also searches "co2" and a card written in molecules still answers an element.
CREATE TABLE IF NOT EXISTS search_concept (
    concept text NOT NULL,
    term    text NOT NULL,
    PRIMARY KEY (concept, term)
);

-- Document frequency per term across everything searchable, in the same raw-token form the query
-- is tokenised to. It is the signal that separates a rare qualifier — a product or process code,
-- "KS-1", "Benfield", "Sulfinol" — from an ordinary domain word, and it feeds hybrid_search's
-- rare-concept pool. The loader copies it from the baked index (agent/library.py build), so both
-- search paths decide rarity from the same numbers; absent rows mean "not rare" (unknown or
-- common), which is the safe reading.
CREATE TABLE IF NOT EXISTS search_term (
    term text PRIMARY KEY,
    df   integer NOT NULL
);

-- Hybrid search over passages, cards, vendor records, equipment classes, projects and catalog
-- sources: reciprocal rank fusion of full-text and vector ranks. qvec may be NULL (keyword only);
-- the optional sector/discipline/region/reuse_level filters mirror the SQLite search exactly:
-- sector narrows per kind, a discipline or region keeps only sources and their passages (cards,
-- vendors, equipment and projects carry no such tags on the SQLite path either), and reuse_level
-- compares the source's level for chunk/source kinds while the library's own records pass only
-- when the filter is unset or full-text-open. Passages of full-text-restricted documents NEVER
-- surface: their text may sit in this database (owner load), but search must not serve it.
-- Example: SELECT * FROM hybrid_search('CO2 storage Malay Basin', NULL, 10);
-- Ranking parity with the SQLite fallback (agent/library.py): the keyword pool orders by concept
-- coverage then density, technology cards are boosted 1.3 (TECHNOLOGY_BOOST) and chunk/source rows
-- get the region boost of their source's tags (sea 1.25, apac 1.15), so the two paths rank alike.
-- Coverage first is what fixed 2026-11-23: "carbon capture amine" ranked cards that say "carbon"
-- often above the card named "Amine solvent post-combustion capture", which is written in CO2 and
-- therefore matched only two of the three words however well it answered the question.
-- kind_filter narrows inside the ranking (search(kind=...) must not filter a global top-k
-- afterwards: the curated kinds score higher than equipment and projects, so every non-curated
-- kind came back empty). hybrid_search() below is the 7-argument form and keeps working.
CREATE OR REPLACE FUNCTION hybrid_search_kind(q text, qvec vector(384) DEFAULT NULL, k integer DEFAULT 10,
                                         sector text DEFAULT NULL, discipline text DEFAULT NULL,
                                         region text DEFAULT NULL, reuse_level text DEFAULT NULL,
                                         kind_filter text DEFAULT NULL)
RETURNS TABLE (kind text, ref text, title text, score double precision) LANGUAGE sql STABLE AS $$
    WITH items AS (
        SELECT 'chunk'::text AS kind, c.id AS ref, c.title, c.tsv, c.embedding, d.sectors,
               d.source_id AS src_id, s.reuse_level AS src_reuse,
               (SELECT array_agg(code) FROM source_tag st
                WHERE st.source_id = d.source_id AND st.kind = 'region') AS regions
        FROM chunk c
        JOIN document d ON d.id = c.document_id
        JOIN source s ON s.id = d.source_id
        WHERE coalesce(d.reuse_level, s.reuse_level) <> 'full-text-restricted'
        UNION ALL
        SELECT 'technology', t.id, t.name, t.tsv, t.embedding, ARRAY[t.sector], NULL::text, NULL::text, NULL::text[]
        FROM technology t
        UNION ALL
        SELECT 'vendor', v.id, v.name, v.tsv, v.embedding,
               (SELECT array_agg(DISTINCT t.sector) FROM technology t WHERE t.id = ANY (v.technologies)),
               NULL::text, NULL::text, NULL::text[]
        FROM vendor v
        UNION ALL
        SELECT 'equipment', e.id, e.name, e.tsv, e.embedding, e.sector_codes, NULL::text, NULL::text, NULL::text[]
        FROM equipment e
        UNION ALL
        SELECT 'source', s.id, s.name, s.tsv, s.embedding,
               (SELECT array_agg(code) FROM source_tag st WHERE st.source_id = s.id AND st.kind = 'sector'),
               s.id, s.reuse_level,
               (SELECT array_agg(code) FROM source_tag st WHERE st.source_id = s.id AND st.kind = 'region')
        FROM source s
        UNION ALL
        SELECT 'project', p.id, p.name, p.tsv, p.embedding, p.sector_codes, NULL::text, NULL::text, NULL::text[]
        FROM project p
    ),
    -- Every pool draws from `keep`, so a filter cannot drift between them.
    keep AS (
        SELECT i.* FROM items i
        WHERE (sector IS NULL OR sector = ANY (i.sectors))
          AND (discipline IS NULL OR (
                i.kind IN ('chunk', 'source')
                AND EXISTS (SELECT 1 FROM source_tag st WHERE st.source_id = i.src_id
                            AND st.kind = 'discipline' AND st.code = discipline)))
          AND (region IS NULL OR (
                i.kind IN ('chunk', 'source')
                AND EXISTS (SELECT 1 FROM source_tag st WHERE st.source_id = i.src_id
                            AND st.kind = 'region' AND st.code = region)))
          AND (reuse_level IS NULL OR (
                (i.kind IN ('chunk', 'source') AND i.src_reuse = reuse_level)
                OR (i.kind IN ('technology', 'vendor', 'equipment', 'project') AND reuse_level = 'full-text-open')))
          AND (kind_filter IS NULL OR i.kind = kind_filter)
    ),
    -- Query terms (subscript digits folded, so CO₂ tokenises like CO2), each replaced by its
    -- concept group; a word in no group is its own concept.
    qtok AS (
        SELECT DISTINCT tok FROM unnest(regexp_split_to_array(
                   lower(regexp_replace(translate(q, '₀₁₂₃₄₅₆₇₈₉', '0123456789'), '[^[:alnum:]]+', ' ', 'g')),
                   '\s+')) AS t(tok)
        WHERE tok <> ''
    ),
    qexp AS (
        SELECT coalesce(sc.concept, qtok.tok) AS concept, e.term
        FROM qtok
        LEFT JOIN search_concept sc ON sc.term = qtok.tok
        CROSS JOIN LATERAL (
            SELECT unnest(coalesce(
                (SELECT array_agg(s2.term) FROM search_concept s2 WHERE s2.concept = sc.concept),
                ARRAY[qtok.tok])) AS term
        ) e
    ),
    qconcept AS (SELECT concept, array_agg(DISTINCT term) AS terms FROM qexp GROUP BY concept),
    -- Per-concept document frequency: how many searchable records carry the concept at all. A
    -- rare concept is a *qualifier* — "KS-1", "Benfield", "Sulfinol", "cryogenic" — and the record
    -- that carries it is very likely the answer, even when its vector neighbourhood is a different
    -- topic. Measured over the whole corpus by the loader into og.search_term.
    qdf AS (
        SELECT qc.concept, qc.terms,
               (SELECT min(st.df) FROM search_term st WHERE st.term = ANY (qc.terms)) AS df
        FROM qconcept qc
    ),
    corpus_size AS (SELECT count(*) AS n FROM items),
    tq AS (SELECT to_tsquery('english',
                   string_agg('(' || array_to_string(terms, ' | ') || ')', ' | ' ORDER BY concept)) AS query
           FROM qconcept),
    -- The rare subset of the query (a NULL query when every concept is common, so the pool dies).
    -- Production corpus 2026-11-23: product codes sit at 0.03–0.8% of records, ordinary domain
    -- words at 3–27%, so 1% (floor 8) separates them; the floor keeps small corpora usable.
    -- `df BETWEEN 1 AND ...` matters: an unknown term (or a search_term table that has not been
    -- filled yet) is NOT rare, so the pool stays empty instead of doubling the keyword pool.
    rq AS (
        SELECT to_tsquery('english',
                   string_agg('(' || array_to_string(terms, ' | ') || ')', ' | ' ORDER BY concept)) AS query
        FROM qdf, corpus_size
        WHERE qdf.df BETWEEN 1 AND greatest(8, corpus_size.n / 100)
    ),
    -- one rank pool per kind: 15k passages must not crowd cards, vendors, equipment and
    -- sources out of the candidate set (each kind contributes up to 50 candidates to the fusion).
    -- Coverage leads the order, density breaks the tie: the query is an implicit conjunction,
    -- so answering all of it beats answering one word often.
    kw AS (
        SELECT kind, ref, r FROM (
            SELECT i.kind, i.ref,
                   row_number() OVER (PARTITION BY i.kind
                                      ORDER BY
                                        (SELECT count(*) FROM qconcept qc
                                         WHERE i.tsv @@ to_tsquery('english', array_to_string(qc.terms, ' | ')))
                                        DESC,
                                        ts_rank_cd(i.tsv, tq.query) DESC,
                                        i.ref) AS r
            FROM keep i, tq
            WHERE i.tsv @@ tq.query
        ) ranked WHERE r <= 50
    ),
    -- The third pool: records carrying a rare query concept, ranked by how strongly they carry it.
    -- Fusion sums pools, so this is what stops a common word's vector neighbourhood from outvoting
    -- the one record that actually names the code the user typed (2026-11-23: "KS-1 solvent" put
    -- the amine card keyword-1st but 4th overall, behind solvent-deasphalting cards).
    rare AS (
        SELECT kind, ref, r FROM (
            SELECT i.kind, i.ref,
                   row_number() OVER (PARTITION BY i.kind
                                      ORDER BY ts_rank_cd(i.tsv, rq.query) DESC, i.ref) AS r
            FROM keep i, rq
            WHERE rq.query IS NOT NULL AND i.tsv @@ rq.query
        ) ranked WHERE r <= 50
    ),
    vec AS (
        SELECT kind, ref, r FROM (
            SELECT i.kind, i.ref,
                   row_number() OVER (PARTITION BY i.kind ORDER BY i.embedding <=> qvec) AS r
            FROM keep i
            WHERE qvec IS NOT NULL AND i.embedding IS NOT NULL
        ) ranked WHERE r <= 50
    ),
    fused AS (
        -- Parity boosts with the SQLite fallback: technology 1.3; chunk/source rows carry their
        -- source's region tags, so sea/apac sources rank up the same way library.search does.
        -- (regions is functionally dependent on kind+ref via the items join; it rides in the
        -- GROUP BY so the multiplier outside the aggregate is legal.)
        SELECT u.kind, u.ref, u.regions,
               sum(1.0 / (60 + u.r))
               * (CASE WHEN u.kind = 'technology' THEN 1.3 ELSE 1.0 END)
               * (CASE WHEN u.regions IS NULL THEN 1.0 ELSE
                      greatest(CASE WHEN 'sea' = ANY (u.regions) THEN 1.25 ELSE 1.0 END,
                               CASE WHEN 'apac' = ANY (u.regions) THEN 1.15 ELSE 1.0 END) END) AS score
        FROM (SELECT k.*, i.regions FROM (SELECT * FROM kw UNION ALL SELECT * FROM vec
                                          UNION ALL SELECT * FROM rare) k
              JOIN items i ON i.kind = k.kind AND i.ref = k.ref) u
        GROUP BY u.kind, u.ref, u.regions
    )
    SELECT f.kind, f.ref, i.title, f.score
    FROM fused f JOIN items i ON i.kind = f.kind AND i.ref = f.ref
    -- a query with no words has no concept to cover: return nothing rather than the nearest
    -- vectors of the punctuation (the SQLite path returns [] for the same input)
    WHERE EXISTS (SELECT 1 FROM qtok)
    ORDER BY f.score DESC, f.kind, f.ref LIMIT k;
$$;

-- The 7-argument form every existing caller uses (the container, docs, worked examples): the same
-- search without a kind filter. Kept as a wrapper so a schema apply never breaks a running client.
CREATE OR REPLACE FUNCTION hybrid_search(q text, qvec vector(384) DEFAULT NULL, k integer DEFAULT 10,
                                         sector text DEFAULT NULL, discipline text DEFAULT NULL,
                                         region text DEFAULT NULL, reuse_level text DEFAULT NULL)
RETURNS TABLE (kind text, ref text, title text, score double precision) LANGUAGE sql STABLE AS $$
    SELECT * FROM hybrid_search_kind(q, qvec, k, sector, discipline, region, reuse_level, NULL);
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
