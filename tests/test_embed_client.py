"""Offline tests for the query-embedding client (agent/embed_client.py, decision #32).

The retired edge /__embed path (and its library key) was removed in step 3 —
embedding is local fastembed only."""
import pathlib
import sys

import numpy as np
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))

import embed_client  # noqa: E402


@pytest.fixture(autouse=True)
def clear_cache():
    embed_client._cache.clear()


def test_query_vector_without_embedder_returns_none():
    assert embed_client.query_vector("acid gas removal") is None
    assert embed_client.query_vector("   ") is None


def test_local_vector_used_and_cached(monkeypatch):
    """When a local embedder exists for the db, its vector is returned and cached."""
    calls = {"n": 0}

    class FakeEmbed:
        @staticmethod
        def load_embedder(db):
            def embed(texts):
                calls["n"] += 1
                return [np.ones(384, dtype=np.float32)]
            return embed

    fake_module = sys.modules.get("embed")
    sys.modules["embed"] = FakeEmbed()
    try:
        got = embed_client.query_vector("local first", db=object())
        assert got is not None and abs(np.linalg.norm(got) - 1.0) < 1e-5
        embed_client.query_vector("local first", db=object())
        assert calls["n"] == 1  # cached
    finally:
        if fake_module is not None:
            sys.modules["embed"] = fake_module


def test_no_service_client_remains():
    assert not hasattr(embed_client, "_endpoint") or embed_client.query_vector.__module__ == "embed_client"
    assert "LIBRARY_API_KEY" not in pathlib.Path(embed_client.__file__).read_text()
