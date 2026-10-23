"""HTTP mode: the API key gate and an MCP initialize over streamable HTTP, all in-process."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
starlette_testclient = pytest.importorskip("starlette.testclient")
server = pytest.importorskip("server")

KEY = "k" * 32
INIT = {"jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t", "version": "0"}}}
HEADERS = {"accept": "application/json, text/event-stream", "content-type": "application/json"}


def client():
    return starlette_testclient.TestClient(server.http_app(KEY))


def test_rejects_missing_or_wrong_key():
    with client() as c:
        assert c.post("/mcp", json=INIT, headers=HEADERS).status_code == 401
        assert c.post("/mcp", json=INIT, headers={**HEADERS, "x-api-key": "wrong"}).status_code == 401


@pytest.mark.parametrize("auth", [{"x-api-key": KEY}, {"authorization": f"Bearer {KEY}"}])
def test_initialize_with_key(auth):
    with client() as c:
        resp = c.post("/mcp", json=INIT, headers={**HEADERS, **auth})
        assert resp.status_code == 200 and "og-tech-sources" in resp.text


def test_http_mode_refuses_short_key(monkeypatch):
    monkeypatch.setenv("LIBRARY_API_KEY", "short")
    assert server.main(["--http"]) == 2
