"""Offline tests for the query-embedding client (agent/embed_client.py, decision #32)."""
import pathlib
import sys

import numpy as np
import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))

import embed_client  # noqa: E402


@pytest.fixture(autouse=True)
def no_env(monkeypatch, tmp_path):
    monkeypatch.delenv("LIBRARY_PUBLIC_URL", raising=False)
    monkeypatch.delenv("LIBRARY_API_KEY", raising=False)
    embed_client._cache.clear()


def test_query_vector_without_config_returns_none():
    assert embed_client.query_vector("acid gas removal") is None
    assert embed_client.query_vector("   ") is None


def test_endpoint_allowlist(monkeypatch):
    monkeypatch.setenv("LIBRARY_PUBLIC_URL", "https://techlib.hilir.app")
    monkeypatch.setenv("LIBRARY_API_KEY", "x" * 32)
    url, key = embed_client._endpoint()
    assert url == "https://techlib.hilir.app/__embed" and key
    for bad in ("http://techlib.hilir.app", "https://evil.example.com", "https://127.0.0.1:8000", ""):
        monkeypatch.setenv("LIBRARY_PUBLIC_URL", bad)
        assert embed_client._endpoint() == (None, None), bad


class _Resp:
    def __init__(self, status=200, payload=None):
        self.status_code, self._payload = status, payload or {}

    def json(self):
        return self._payload


def test_service_vector_success_and_cache(monkeypatch):
    monkeypatch.setenv("LIBRARY_PUBLIC_URL", "https://techlib.hilir.app")
    monkeypatch.setenv("LIBRARY_API_KEY", "x" * 32)
    calls = {"n": 0}
    vec = [0.001] * 384

    def fake_post(url, json=None, headers=None, timeout=None, allow_redirects=None):
        calls["n"] += 1
        assert url == "https://techlib.hilir.app/__embed" and headers["x-api-key"] == "x" * 32
        assert allow_redirects is False
        return _Resp(payload={"vector": vec})

    monkeypatch.setattr("requests.post", fake_post)
    got = embed_client.query_vector("solvent regeneration")
    assert got is not None and len(got) == 384
    assert abs(np.linalg.norm(got) - 1.0) < 1e-5  # unit length
    embed_client.query_vector("solvent regeneration")
    assert calls["n"] == 1  # cached


def test_service_vector_failure_modes(monkeypatch):
    monkeypatch.setenv("LIBRARY_PUBLIC_URL", "https://techlib.hilir.app")
    monkeypatch.setenv("LIBRARY_API_KEY", "x" * 32)
    for resp in (_Resp(status=401), _Resp(payload={"vector": [0.1] * 7}), _Resp(payload={})):
        monkeypatch.setattr("requests.post", lambda *a, **k: resp)
        assert embed_client.query_vector("anything") is None
    # a failed lookup is never cached: a recovered service is used on the next call
    monkeypatch.setattr("requests.post", lambda *a, **k: _Resp(payload={"vector": [0.02] * 384}))
    assert embed_client.query_vector("anything") is not None


def test_local_vector_preferred(monkeypatch):
    """When a local embedder exists for the db, the service is never called."""
    monkeypatch.setenv("LIBRARY_PUBLIC_URL", "https://techlib.hilir.app")
    monkeypatch.setenv("LIBRARY_API_KEY", "x" * 32)
    monkeypatch.setattr("requests.post", lambda *a, **k: pytest.fail("service must not be called"))

    class FakeEmbed:
        def load_embedder(self, db):
            return lambda texts: [np.ones(384, dtype=np.float32)]

    fake_module = sys.modules.get("embed")
    sys.modules["embed"] = FakeEmbed()
    try:
        got = embed_client.query_vector("local first", db=object())
        assert got is not None and abs(np.linalg.norm(got) - 1.0) < 1e-5
    finally:
        if fake_module is not None:
            sys.modules["embed"] = fake_module
