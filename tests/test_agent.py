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


@pytest.fixture
def db(tmp_path):
    corpus = tmp_path / "corpus"
    (corpus / "arxiv").mkdir(parents=True)
    (corpus / "_inbox" / "arxiv").mkdir(parents=True)
    (corpus / "arxiv" / "pem.md").write_text(DOC, encoding="utf-8")
    (corpus / "_inbox" / "arxiv" / "ignored.md").write_text(DOC, encoding="utf-8")
    counts = library.build(tmp_path / "lib.db", corpus)
    assert counts["documents"] == 1 and counts["chunks"] >= 2
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
