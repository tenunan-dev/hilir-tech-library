"""HTTP mode: the hilir bearer gate and an MCP initialize over streamable HTTP, all in-process.

The gate (server.RequireHilirToken) accepts only a hilir Access bearer token; tests
stub the verifier (agent/auth.py) the same way every app stubs jose/PyJWT."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
starlette_testclient = pytest.importorskip("starlette.testclient")
server = pytest.importorskip("server")

TOKEN = "st." + "p" * 40 + "." + "s" * 40  # three segments, matched by the stub verifier
BAD = "w" * 60  # single segment junk — never reaches the verifier
INIT = {"jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "t", "version": "0"}}}
HEADERS = {"accept": "application/json, text/event-stream", "content-type": "application/json"}


class StubAuth:
    """verify/identity for exactly TOKEN — anything else is unauthenticated."""

    def verify(self, token):
        return {"sub": "user-1"} if token == TOKEN else None

    def identity(self, token):
        return {"email": "admin@example.com"} if token == TOKEN else None


@pytest.fixture(autouse=True)
def stub_verifier(monkeypatch):
    stub = StubAuth()
    monkeypatch.setattr(server, "hilir_auth", stub)
    import web
    monkeypatch.setattr(web, "hilir_auth", stub)
    return stub


def client():
    return starlette_testclient.TestClient(server.http_app())


def test_rejects_missing_or_malformed_token():
    with client() as c:
        assert c.post("/mcp", json=INIT, headers=HEADERS).status_code == 401
        assert c.post("/mcp", json=INIT, headers={**HEADERS, "authorization": f"Bearer {BAD}"}).status_code == 401


def test_initialize_with_bearer_token():
    with client() as c:
        resp = c.post("/mcp", json=INIT, headers={**HEADERS, "authorization": f"Bearer {TOKEN}"})
        assert resp.status_code == 200 and "hilir-tech-library" in resp.text


def test_openapi_is_public():
    """The schema is served without a credential so tools can import it (api.PUBLIC_PATHS)."""
    with client() as c:
        assert c.get("/api/openapi.json").status_code == 200


def test_backend_mode_serves_no_ui():
    """LIBRARY_WEB=off (the split backend container): no UI routes, the token gate covers everything."""
    with starlette_testclient.TestClient(server.http_app(with_web=False)) as c:
        assert c.get("/technologies", headers={"authorization": f"Bearer {TOKEN}"}).status_code == 404
        assert c.get("/", headers={"authorization": f"Bearer {TOKEN}"}).status_code == 404
        assert c.get("/", headers={"authorization": f"Bearer {BAD}"}).status_code == 401
