"""REST API: key gate, public schema, and each endpoint answering from the built index, in-process."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
starlette_testclient = pytest.importorskip("starlette.testclient")
server = pytest.importorskip("server")

KEY = "k" * 32
AUTH = {"x-api-key": KEY}


@pytest.fixture(scope="module")
def c():
    with starlette_testclient.TestClient(server.http_app(KEY)) as client:
        yield client


def test_data_endpoints_need_the_key(c):
    assert c.get("/api/stats").status_code == 401
    assert c.get("/api/search", params={"q": "hydrogen"}, headers={"x-api-key": "wrong"}).status_code == 401


def test_openapi_is_public_and_lists_paths(c):
    spec = c.get("/api/openapi.json").json()
    assert spec["openapi"].startswith("3.1") and "/api/search" in spec["paths"]
    assert spec["components"]["securitySchemes"]["ApiKey"]["name"] == "x-api-key"


def test_search_stats_and_not_found(c):
    assert c.get("/api/search", headers=AUTH).status_code == 400
    hits = c.get("/api/search", params={"q": "hydrogen", "limit": 3}, headers=AUTH).json()
    assert 0 < len(hits) <= 3 and all("url" in h or "path" in h or "id" in h for h in hits)
    assert c.get("/api/stats", headers=AUTH).json()["sources"] > 0
    assert c.get("/api/sources/no-such-source", headers=AUTH).status_code == 404
    assert c.get("/api/technologies/no-such-card", headers=AUTH).status_code == 404


def test_lists_and_records(c):
    sources = c.get("/api/sources", params={"code": "CCS"}, headers=AUTH).json()
    assert sources and c.get(f"/api/sources/{sources[0]['id']}", headers=AUTH).status_code == 200
    cards = c.get("/api/technologies", params={"sector": "CCS"}, headers=AUTH).json()
    assert cards and c.get(f"/api/technologies/{cards[0]['id']}", headers=AUTH).json()["id"] == cards[0]["id"]
    assert isinstance(c.get("/api/register", params={"code": "H2"}, headers=AUTH).json(), list)
    assert isinstance(c.get("/api/gaps", params={"sector": "CCS"}, headers=AUTH).json(), list)


def test_vendors_endpoints(c):
    listed = c.get("/api/vendors", headers=AUTH)
    assert listed.status_code == 200 and listed.json()
    assert {"id", "name", "roles", "technologies"} <= set(listed.json()[0])
    assert c.get("/api/vendors", params={"role": "oem"}, headers=AUTH).json()
    one = c.get("/api/vendors/wartsila", headers=AUTH)
    assert one.status_code == 200 and one.json()["name"] and one.json()["sources"]
    assert c.get("/api/vendors/no-such-vendor", headers=AUTH).status_code == 404


def test_search_finds_vendors(c):
    hits = c.get("/api/search", params={"q": "Wärtsilä", "kind": "vendor"}, headers=AUTH).json()
    assert hits and hits[0]["kind"] == "vendor" and hits[0]["ref"] == "wartsila"


def test_openapi_lists_vendors(c):
    spec = c.get("/api/openapi.json").json()
    assert "/api/vendors" in spec["paths"] and "/api/vendors/{vendor_id}" in spec["paths"]
