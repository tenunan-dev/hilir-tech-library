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
