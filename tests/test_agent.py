"""Offline tests for the search index and MCP tool functions, on a small fixture corpus."""
import json
import pathlib
import sys

import numpy as np
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))

import embed  # noqa: E402
import library  # noqa: E402

DOC = """---
source_id: "arxiv"
title: "PEM electrolyzer degradation"
url: "http://arxiv.org/abs/1"
licence: "CC0-1.0"
---

# PEM electrolyzer degradation

**Abstract:** Membrane thinning under dynamic load cycling.

""" + "Iridium anode dissolution was measured over many cycles. " * 40

CARD = {
    "id": "h2-pem-test", "name": "Test PEM electrolyser", "sector": "H2", "category": "Electrolysis",
    "maturity": "commercial", "principle": "A test electrolyser principle for the fixture.",
    "process_steps": [], "key_equipment": [], "suppliers": [], "sources": [], "last_reviewed": "2026-10-26",
}

VENDOR = {
    "id": "test-vendor", "name": "Test Vendor Electrolyser", "country": "Malaysia",
    "aliases": ["TVE"], "roles": ["oem"], "products": ["PEM stacks"],
    "description": "Fixture vendor building PEM electrolyser stacks for the index tests.",
    "technologies": ["h2-pem-test"], "sources": [], "last_reviewed": "2026-10-26",
}


@pytest.fixture
def db(tmp_path):
    corpus = tmp_path / "corpus"
    (corpus / "arxiv").mkdir(parents=True)
    (corpus / "_inbox" / "arxiv").mkdir(parents=True)
    (corpus / "arxiv" / "pem.md").write_text(DOC, encoding="utf-8")
    (corpus / "_inbox" / "arxiv" / "ignored.md").write_text(DOC, encoding="utf-8")
    (tmp_path / "catalog" / "technologies").mkdir(parents=True)
    (tmp_path / "catalog" / "technologies" / "h2-pem-test.json").write_text(json.dumps(CARD), encoding="utf-8")
    (tmp_path / "catalog" / "vendors").mkdir(parents=True)
    (tmp_path / "catalog" / "vendors" / "test-vendor.json").write_text(json.dumps(VENDOR), encoding="utf-8")
    counts = library.build(tmp_path / "lib.db", corpus)
    assert counts["documents"] == 1 and counts["chunks"] >= 2 and counts["vendors"] == 1
    return library.connect(tmp_path / "lib.db")


def test_chunk_respects_size():
    chunks = library.chunk("\n\n".join(["word " * 100] * 10), size=1200)
    assert len(chunks) > 1 and all(len(c) <= 1200 for c in chunks)


def _card(card_id, name, principle):
    return {"id": card_id, "name": name, "sector": "CCS", "category": "Capture", "maturity": "commercial",
            "principle": principle, "process_steps": [], "key_equipment": [], "suppliers": [],
            "sources": [], "last_reviewed": "2026-11-23"}


# The 2026-11-23 finding, reduced to three cards: the answer is written in CO2 and never says
# "carbon"; the competition repeats "carbon" and never says "amine".
CONCEPT_CARDS = (
    _card("ccs-amine", "Amine solvent post-combustion capture",
          "Flue gas is contacted with an aqueous amine solution, which reacts with CO2."),
    _card("ccs-carbon", "Bioenergy carbon capture",
          "Carbon is captured from carbon-rich biomass combustion; carbon storage follows."),
    _card("ccs-cryogenic", "Cryogenic capture",
          "Flue gas is cooled until the CO2 desublimates."),
)


def test_search_ranks_concept_coverage_and_bridges_vocabulary(tmp_path):
    """A card covering every query concept outranks cards that merely repeat one word.

    "carbon capture amine" is satisfied by ccs-amine (amine + capture in the name, CO2 in the
    principle) through the carbon = carbon|co2 group; the two cards that only say "carbon" or
    only say "capture" rank behind it, however often they repeat the word.
    """
    corpus = tmp_path / "corpus"
    (corpus / "arxiv").mkdir(parents=True)
    (corpus / "arxiv" / "pem.md").write_text(DOC, encoding="utf-8")
    for folder in ("technologies", "vendors", "equipment", "projects"):
        (tmp_path / "catalog" / folder).mkdir(parents=True)
    for card in CONCEPT_CARDS:
        (tmp_path / "catalog" / "technologies" / f"{card['id']}.json").write_text(json.dumps(card), encoding="utf-8")
    library.build(tmp_path / "lib.db", corpus)
    db = library.connect(tmp_path / "lib.db")

    hits = library.search("carbon capture amine", kind="technology", limit=3, db=db)
    assert hits and hits[0]["ref"] == "ccs-amine"
    assert {h["ref"] for h in hits} == {"ccs-amine", "ccs-carbon", "ccs-cryogenic"}
    # bridging runs both ways: "co2" reaches a card written in "carbon"
    assert "ccs-carbon" in [h["ref"] for h in library.search("co2", kind="technology", limit=3, db=db)]
    # subscript digits fold, so CO₂ queries like CO2
    assert [h["ref"] for h in library.search("CO₂", kind="technology", limit=3, db=db)] == \
        [h["ref"] for h in library.search("co2", kind="technology", limit=3, db=db)]


def test_rare_concept_pool_lets_a_code_beat_a_common_word(tmp_path):
    """A user who types a product code gets the card, even when a common word in the same query
    favours a different record on coverage and BM25.

    "solvent ks": both cards cover one query concept, so coverage ties; BM25 prefers the card that
    repeats "solvent". The rare-concept pool (og.hybrid_search's third pool) is what puts the card
    that carries the rare code first — and setting the code's document frequency back to common
    proves that is the cause, not the order of the fixture.
    """
    corpus = tmp_path / "corpus"
    (corpus / "arxiv").mkdir(parents=True)
    (corpus / "arxiv" / "pem.md").write_text(DOC, encoding="utf-8")
    for folder in ("technologies", "vendors", "equipment", "projects"):
        (tmp_path / "catalog" / folder).mkdir(parents=True)
    for card in (
        _card("ccs-code", "Capture with KS", "A licensor process named KS, offered as a package."),
        _card("ccs-plain", "Solvent deasphalting", "Solvent solvent solvent recovery and solvent recycle."),
    ):
        (tmp_path / "catalog" / "technologies" / f"{card['id']}.json").write_text(json.dumps(card), encoding="utf-8")
    library.build(tmp_path / "lib.db", corpus)
    db = library.connect(tmp_path / "lib.db")

    def set_df(**pairs):
        db.execute("DELETE FROM term_df")
        db.executemany("INSERT INTO term_df VALUES (?, ?)", pairs.items())
        db.commit()

    set_df(ks=1, solvent=5000, capture=900, **{"1": 8000, "with": 40, "a": 9000, "and": 9000})
    assert library.rare_groups(library.concept_groups("solvent ks"), db) == [("ks",)]
    assert library.search("solvent ks", kind="technology", limit=2, db=db)[0]["ref"] == "ccs-code"

    set_df(ks=5000, solvent=5000, capture=900, **{"1": 8000, "with": 40, "a": 9000, "and": 9000})
    assert library.rare_groups(library.concept_groups("solvent ks"), db) == []
    assert library.search("solvent ks", kind="technology", limit=2, db=db)[0]["ref"] == "ccs-plain", \
        "with no rare concept the coverage/BM25 order stands — so the pool above is the cause"


def test_rare_groups_ignores_terms_the_index_does_not_hold(db):
    """An unknown word is not rare: promoting it would only add noise, and it lets a schema apply
    whose df table is empty behave exactly as before (no rare pool)."""
    db.execute("DELETE FROM term_df")
    db.commit()
    assert library.rare_groups(library.concept_groups("electrolyzer zzzznotaword"), db) == []


def test_search_survives_an_index_without_the_frequency_table(db):
    """A stale build/library.db (built before term_df) with newer code must degrade, not raise."""
    db.execute("DROP TABLE term_df")
    db.commit()
    assert library.rare_groups(library.concept_groups("electrolyzer"), db) == []
    assert library.search("electrolyzer", db=db), "search still answers without the rare pool"


def test_search_keeps_every_kind_in_the_result_set(tmp_path):
    """One global rank pool let the corpus bury all cards; each kind now contributes its own."""
    corpus = tmp_path / "corpus"
    (corpus / "arxiv").mkdir(parents=True)
    (corpus / "arxiv" / "pem.md").write_text(DOC, encoding="utf-8")
    for folder in ("technologies", "vendors", "equipment", "projects"):
        (tmp_path / "catalog" / folder).mkdir(parents=True)
    (tmp_path / "catalog" / "technologies" / "h2-pem-test.json").write_text(json.dumps(CARD), encoding="utf-8")
    (tmp_path / "catalog" / "vendors" / "test-vendor.json").write_text(json.dumps(VENDOR), encoding="utf-8")
    library.build(tmp_path / "lib.db", corpus)
    db = library.connect(tmp_path / "lib.db")
    kinds = {h["kind"] for h in library.search("electrolyser stack", limit=20, db=db)}
    assert {"technology", "vendor"} <= kinds


def test_search_finds_chunks_and_sources(db):
    hits = library.search("electrolyzer degradation", db=db)
    assert hits[0]["kind"] == "chunk" and hits[0]["path"] == "corpus/arxiv/pem.md"
    assert hits[0]["url"] == "http://arxiv.org/abs/1" and hits[0]["reuse_level"]
    sources = library.search("Malaysia", kind="source", db=db)
    assert sources and all(h["kind"] == "source" for h in sources)


def test_search_filters_and_empty_query(db):
    assert all("sea" in h["regions"] for h in library.search("gas", kind="source", region="sea", db=db))
    assert library.search("!!!", db=db) == []


def test_restricted_results_carry_use_note(db):
    hits = library.search("iridium", kind="chunk", db=db)
    rec = library.get_source("arxiv", db)
    assert ("use_note" in hits[0]) == (rec["reuse_level"] == "full-text-restricted")


def test_get_source_document_and_tags(db):
    rec = library.get_source("arxiv", db)
    assert rec["documents"][0]["path"] == "corpus/arxiv/pem.md"
    assert library.get_source("nope", db) is None
    doc = library.get_document("corpus/arxiv/pem.md#1", db)
    assert doc["meta"]["licence"] == "CC0-1.0" and "Iridium" in doc["text"]
    assert library.get_document("../../etc/passwd", db) is None
    h2 = library.list_by_tag("H2", db=db)
    assert h2 and all({"id", "url", "reuse_level"} <= set(r) for r in h2)
    first_non_asia = next(i for i, r in enumerate(h2) if not {"sea", "apac"} & set(r["regions"]))
    assert all(not {"sea", "apac"} & set(r["regions"]) for r in h2[first_non_asia:])


def test_search_fuses_precomputed_query_vector(db):
    """A query with no keyword overlap can still surface the semantically closest row
    when its 384-dim vector is supplied (edge Workers AI path, decision #32)."""
    rows = db.execute("SELECT rowid, kind, title, text FROM search").fetchall()
    target = next(r for r in rows if r["kind"] == "chunk")
    db.execute("INSERT OR REPLACE INTO info VALUES ('model', 'test')")
    for r in rows:
        base = np.zeros(384, dtype=np.float32)
        base[0 if r["rowid"] == target["rowid"] else 1] = 1.0
        db.execute("INSERT INTO vectors VALUES (?, ?)", (r["rowid"], base.tobytes()))
    db.commit()
    qvec = np.zeros(384, dtype=np.float32)
    qvec[0] = 1.0
    hits = library.search("xylophone zebra quux", db=db, query_vector=qvec.tolist())
    assert hits, "vector fusion should surface the aligned row despite zero keyword overlap"
    assert any(h.get("kind") == "chunk" and "electrolyzer" in (h.get("title") or "") for h in hits)


def test_search_ignores_malformed_query_vector(db):
    rows = db.execute("SELECT rowid FROM search LIMIT 2").fetchall()
    db.execute("INSERT OR REPLACE INTO info VALUES ('model', 'test')")
    for r in rows:
        db.execute("INSERT INTO vectors VALUES (?, ?)", (r["rowid"], np.ones(384, dtype=np.float32).tobytes()))
    db.commit()
    hits = library.search("electrolyzer", db=db, query_vector=[0.1] * 7)  # wrong length: ignored
    assert hits and all(isinstance(h, dict) for h in hits)


class FakeModel:
    """Bag-of-letters vectors: enough to check the plumbing without downloading a model."""
    def _vec(self, text):
        v = np.zeros(26, dtype=np.float32)
        for ch in text.lower():
            if "a" <= ch <= "z":
                v[ord(ch) - 97] += 1
        return v + 1e-3

    def passage_embed(self, texts):
        return [self._vec(t) for t in texts]


def test_vectors_fuse_with_keyword_results(db):
    n = embed.embed_index(db, "fake", model=FakeModel())
    assert n == db.execute("SELECT count(*) FROM search").fetchone()[0]
    model = FakeModel()
    embedder = lambda texts: [v / np.linalg.norm(v) for v in model.passage_embed(texts)]  # noqa: E731
    hits = library.search("electrolyzer", db=db, embedder=embedder, limit=5)
    assert hits and library.stats(db)["embedding_model"] == "fake"


def test_incremental_embeds_once_then_reuses(db, tmp_path):
    """The R6 property: an unchanged index re-attaches all vectors from the cache."""
    cache = tmp_path / "cache.db"
    first = embed.embed_incremental(db, "fake", model=FakeModel(), cache_path=cache)
    assert first["embedded"] == first["total"] and first["reused"] == 0
    second = embed.embed_incremental(db, "fake", model=FakeModel(), cache_path=cache)
    assert second["embedded"] == 0 and second["reused"] == second["total"]


def test_incremental_survives_rebuild_and_picks_up_changes(db, tmp_path):
    """Rebuilding the index (fresh rowids) keeps vectors via the cache; changed text re-embeds."""
    import pathlib
    cache = tmp_path / "cache.db"
    embed.embed_incremental(db, "fake", model=FakeModel(), cache_path=cache)
    root = pathlib.Path(db.execute("SELECT value FROM info WHERE key = 'root'").fetchone()[0])
    doc = next(p for p in (root / "corpus").glob("*/*.md") if "_inbox" not in p.parts)
    doc.write_text(doc.read_text(encoding="utf-8").replace("Iridium anode dissolution",
                                                           "Ruthenium anode dissolution"), encoding="utf-8")
    library.build(root / "lib.db", root / "corpus")
    fresh = library.connect(root / "lib.db")
    result = embed.embed_incremental(fresh, "fake", model=FakeModel(), cache_path=cache)
    assert result["embedded"] >= 1, "the changed document must re-embed"
    assert result["reused"] >= 1, "unchanged rows must come from the cache"
    assert result["missing"] == 0
    assert fresh.execute("SELECT count(*) FROM vectors").fetchone()[0] == result["total"]


def test_incremental_narrows_by_kind_and_ref(db, tmp_path):
    """--kind/--ref: only the narrowed rows embed; the rest stay missing until a later run."""
    cache = tmp_path / "cache.db"
    total = db.execute("SELECT count(*) FROM search").fetchone()[0]
    vendors = db.execute("SELECT count(*) FROM search WHERE kind = 'vendor'").fetchone()[0]
    result = embed.embed_incremental(db, "fake", model=FakeModel(), cache_path=cache, kind="vendor")
    assert result["embedded"] == vendors and result["missing"] == total - vendors
    assert db.execute("SELECT count(*) FROM vectors").fetchone()[0] == vendors
    second = embed.embed_incremental(db, "fake", model=FakeModel(), cache_path=cache)
    assert second["reused"] == vendors and second["embedded"] == total - vendors


def test_incremental_model_change_wipes_cache(db, tmp_path):
    cache = tmp_path / "cache.db"
    embed.embed_incremental(db, "fake", model=FakeModel(), cache_path=cache)
    again = embed.embed_incremental(db, "other", model=FakeModel(), cache_path=cache)
    assert again["embedded"] == again["total"] and again["reused"] == 0


def test_exclude_restricted_hides_private_text(db):
    rec = library.get_source("arxiv", db)
    restricted = rec["reuse_level"] == "full-text-restricted"
    hits = library.search("iridium", kind="chunk", db=db, exclude_restricted=True)
    assert (hits == []) == restricted
    doc = library.get_document("corpus/arxiv/pem.md", db, exclude_restricted=True)
    assert ("error" in doc) == restricted
    assert (library.get_source("arxiv", db, exclude_restricted=True)["documents"] == []) == restricted


def test_open_document_in_restricted_source_is_served(tmp_path):
    corpus = tmp_path / "corpus"
    (corpus / "osti").mkdir(parents=True)
    (corpus / "osti" / "gov.md").write_text(DOC.replace('licence: "CC0-1.0"', 'licence: "public-domain"\nreuse_level: "full-text-open"'),
                                            encoding="utf-8")
    library.build(tmp_path / "lib.db", corpus)
    db = library.connect(tmp_path / "lib.db")
    hits = library.search("iridium", kind="chunk", db=db, exclude_restricted=True)
    assert hits and hits[0]["reuse_level"] == "full-text-open" and "use_note" not in hits[0]


def test_search_finds_vendors(db):
    hits = library.search("electrolyser stacks", kind="vendor", db=db)
    assert hits and hits[0]["kind"] == "vendor" and hits[0]["ref"] == "test-vendor"
    assert hits[0]["country"] == "Malaysia" and hits[0]["technologies"] == ["h2-pem-test"] and hits[0]["hint"]
    v = library.get_vendor("test-vendor", db)
    assert v["name"] == "Test Vendor Electrolyser" and v["roles"] == ["oem"]
    assert library.get_vendor("no-such-vendor", db) is None
    assert library.list_vendors(role="oem", db=db) and library.stats(db)["vendors"] == 1


def test_vendor_sector_filter_comes_from_linked_cards(db):
    assert library.search("electrolyser", kind="vendor", sector="H2", db=db)
    assert library.search("electrolyser", kind="vendor", sector="CCS", db=db) == []


def test_export_public_leaves_out_restricted(tmp_path, monkeypatch):
    import export_public
    corpus = tmp_path / "repo" / "corpus"
    (corpus / "arxiv").mkdir(parents=True)
    (corpus / "arxiv" / "open.md").write_text(DOC.replace('licence: "CC0-1.0"', 'licence: "CC0-1.0"\nreuse_level: "full-text-open"'), encoding="utf-8")
    (corpus / "arxiv" / "private.md").write_text(DOC.replace("PEM", "Private"), encoding="utf-8")
    monkeypatch.setattr(library, "CORPUS", corpus)
    monkeypatch.setattr(library, "ROOT", corpus.parent)
    monkeypatch.setattr(export_public, "KEEP", ())
    monkeypatch.setattr(library, "load_records", lambda: [{"id": "arxiv", "reuse_level": "full-text-restricted"}])
    assert export_public.export(tmp_path / "out") == (1, 1)
    assert (tmp_path / "out" / "corpus" / "arxiv" / "open.md").exists()
    assert not (tmp_path / "out" / "corpus" / "arxiv" / "private.md").exists()


def test_doc_sectors_narrow_inherited_tags():
    assert library.doc_sectors("PEM electrolyzer degradation", "", ["PWR", "H2", "CCS"]) == ["H2"]
    assert library.doc_sectors("Design of carbon capture processes", "", ["PWR", "H2", "CCS"]) == ["CCS"]
    assert library.doc_sectors("Untitled", "nothing relevant", ["PWR"]) == ["PWR"]
    assert library.doc_sectors("TESS light curves", "astronomy", ["UPS", "REF", "H2", "CCS"]) == []


def test_sector_filter_uses_document_tags(db):
    assert library.search("electrolyzer", kind="chunk", sector="CCS", db=db) == []
    assert library.search("electrolyzer", kind="chunk", sector="H2", db=db)


def test_mcp_library_stats_prefers_neon(monkeypatch):
    """Decision #34: the MCP tool must agree with REST /api/stats — Neon first, baked index only
    as the fallback (the slim image bakes no embeddings, so its vector count would read 0)."""
    import pg
    server = pytest.importorskip("server")
    monkeypatch.setattr(pg, "configured", lambda: True)
    monkeypatch.setattr(pg, "library_stats", lambda: {"sources": 399, "vectors": 12586})
    assert server.library_stats() == {"sources": 399, "vectors": 12586}
    monkeypatch.setattr(pg, "configured", lambda: False)
    monkeypatch.setattr(library, "stats", lambda db=None: {"sources": 1})
    monkeypatch.setattr(server, "db", lambda: None)
    assert server.library_stats() == {"sources": 1}


def test_mcp_get_tools_read_neon_first_and_fall_back(monkeypatch):
    """The get_* tools prefer Neon (live layer) and drop to the baked index when it errors."""
    import pg
    server = pytest.importorskip("server")
    monkeypatch.setattr(pg, "configured", lambda: True)
    monkeypatch.setattr(pg, "vendor_row", lambda vid: {"id": vid, "name": "Neon Vendor"})
    assert server.get_vendor("acme") == {"id": "acme", "name": "Neon Vendor"}
    monkeypatch.setattr(pg, "tech_card", lambda tid: {"id": tid, "name": "N", "process_steps": []})
    card = server.get_technology("t1")
    assert card["block_diagram_mermaid"].startswith("flowchart LR")
    assert card["licence"] == library.TECHNOLOGY_LICENCE

    def boom(*a, **k):
        raise pg.DatabaseError("database unreachable (test)")
    monkeypatch.setattr(pg, "vendor_row", boom)
    assert server.get_vendor("wartsila")["id"] == "wartsila"  # served by the repo's baked index


def test_mcp_list_gaps_forwards_filters(monkeypatch):
    import pg
    server = pytest.importorskip("server")
    seen = {}
    monkeypatch.setattr(pg, "configured", lambda: True)
    monkeypatch.setattr(pg, "gap_rows",
                        lambda sector, field, reason_code, include_no_card:
                        seen.update(sector=sector, field=field, reason_code=reason_code,
                                    include_no_card=include_no_card) or [])
    assert server.list_gaps("CCS", "costs", "paid_source", True) == []
    assert seen == {"sector": "CCS", "field": "costs", "reason_code": "paid_source", "include_no_card": True}


def test_mcp_search_forwards_all_filters(monkeypatch):
    """discipline/region/reuse_level reach the Neon search instead of silently dropping."""
    import pg
    server = pytest.importorskip("server")
    seen = {}
    monkeypatch.setattr(pg, "configured", lambda: True)
    monkeypatch.setattr(pg, "search_library",
                        lambda q, kind, sector, limit, qvec, discipline, region, reuse:
                        seen.update(q=q, kind=kind, sector=sector, discipline=discipline,
                                    region=region, reuse=reuse) or [])
    monkeypatch.setattr("embed.load_embedder", lambda db: None)
    monkeypatch.setattr(server, "_query_vector", lambda query: None)
    assert server.search("boiler", "vendor", "PWR", "ROT", "sea", "full-text-open", 5) == []
    assert seen == {"q": "boiler", "kind": "vendor", "sector": "PWR",
                    "discipline": "ROT", "region": "sea", "reuse": "full-text-open"}
