"""Web interface: the hilir bearer gate and role resolution, each page answering from the built
index, in-process. The verifier and the account store are stubbed — no Neon, no real JWKS."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
starlette_testclient = pytest.importorskip("starlette.testclient")
server = pytest.importorskip("server")
import userstore  # noqa: E402
import web  # noqa: E402

ADMIN_TOKEN = "ad." + "p" * 40 + "." + "s" * 40   # three segments, matched by the stub verifier
USER_TOKEN = "us." + "p" * 40 + "." + "s" * 40
GHOST_TOKEN = "gh." + "p" * 40 + "." + "s" * 40   # verifies, but no account row (fail-closed)

ACCOUNTS = {
    "admin@example.com": {"email": "admin@example.com", "name": "Ada", "hash": "", "role": "admin"},
    "bob@example.com": {"email": "bob@example.com", "name": "Bob", "hash": "", "role": "user"},
}


class StubAuth:
    """verify/identity keyed by token, like the real verifier's per-token identity cache."""

    def __init__(self):
        self._emails = {ADMIN_TOKEN: "admin@example.com", USER_TOKEN: "bob@example.com",
                        GHOST_TOKEN: "ghost@example.com"}

    def verify(self, token):
        return {"sub": "user-1"} if token in self._emails else None

    def identity(self, token):
        email = self._emails.get(token)
        return {"email": email} if email else None


@pytest.fixture(autouse=True)
def stub_auth_and_store(monkeypatch):
    stub = StubAuth()
    monkeypatch.setattr(server, "hilir_auth", stub)
    monkeypatch.setattr(web, "hilir_auth", stub)
    monkeypatch.setattr(userstore, "accounts", lambda: dict(ACCOUNTS))
    monkeypatch.setattr(userstore, "configured", lambda: True)
    # never touch a real Neon connection from page renders
    monkeypatch.setattr(userstore, "record", lambda *a, **k: None)
    monkeypatch.setattr(userstore, "analytics",
                        lambda: {"days": [], "top": [], "events_total": 0})
    return stub


@pytest.fixture(scope="module")
def c():
    # https base_url so Secure cookies would be stored and sent (the transport does no real TLS)
    with starlette_testclient.TestClient(server.http_app(), base_url="https://testserver") as client:
        yield client


def admin(c):
    c.headers["authorization"] = f"Bearer {ADMIN_TOKEN}"
    return c


def test_home_gates_the_site(c):
    r = c.get("/", follow_redirects=False)
    assert r.status_code == 303 and r.headers["location"].startswith("/login?next=")


def test_pages_answer_with_a_bearer(c):
    admin(c)
    for path in ("/", "/technologies", "/vendors", "/register", "/sources", "/gaps", "/account"):
        assert c.get(path).status_code == 200, path
    search = c.get("/search", params={"q": "hydrogen"})
    assert search.status_code == 200 and ("/technologies/" in search.text or "/documents?path=" in search.text
                                          or "/sources/" in search.text)


def test_documents_index_and_restricted_viewer(c):
    """/documents without a path is the menu's index (no Bad request, 2026-11-09); restricted
    documents are listed and their viewer shows metadata + source url but never the body."""
    admin(c)
    index = c.get("/documents")
    assert index.status_code == 200 and "documents?path=" in index.text
    # find a restricted doc in the baked index (the container build owns the corpus; here the
    # SQLite fallback runs against build/library.db)
    import json as _json
    import library as _lib
    db = _lib.connect()
    restricted = None
    for dpath, srec in db.execute("SELECT d.path, s.record FROM docs d JOIN sources s ON s.id = d.source_id"):
        meta = _lib.read_document(_lib.ROOT / dpath)[0] if (_lib.ROOT / dpath).exists() else {}
        # doc-level restriction wins (a source-level restriction with an open doc meta stays open)
        if meta.get("reuse_level", _json.loads(srec).get("reuse_level")) == "full-text-restricted":
            restricted = dpath
            break
    assert restricted, "no full-text-restricted doc in the baked index to test with"
    view = c.get("/documents", params={"path": restricted})
    assert view.status_code == 200
    assert "Source url:" in view.text and "full text is not served" in view.text
    assert '<pre class="doc">' not in view.text, "restricted body leaked into the viewer"


def test_token_without_an_account_row_is_refused(c):
    """The token proves who; the store decides the role. No row = no access (fail-closed),
    and a 403 page — never a redirect to /login, which would loop forever: Access silently
    re-issues the same valid identity every time (Safari's too-many-redirects, 2026-11-07)."""
    c.headers["authorization"] = f"Bearer {GHOST_TOKEN}"
    r = c.get("/technologies", follow_redirects=False)
    assert r.status_code == 403
    assert "location" not in r.headers  # the anti-loop contract: no /login bounce
    assert "not registered" in r.text


def test_invalid_token_still_redirects_to_login(c):
    """No (or a bad) token is the anonymous case: the standard sign-in flow applies."""
    c.headers.pop("authorization", None)  # the client is module-scoped; clear leaked headers
    r = c.get("/technologies", follow_redirects=False)
    assert r.status_code == 303 and r.headers["location"].startswith("/login?next=")
    c.headers["authorization"] = "Bearer not.a.jwt"
    r = c.get("/technologies", follow_redirects=False)
    assert r.status_code == 303 and r.headers["location"].startswith("/login?next=")


def test_admin_gating(c):
    c.headers["authorization"] = f"Bearer {USER_TOKEN}"
    assert c.get("/admin").status_code == 403
    admin(c)
    page = c.get("/admin")
    assert page.status_code == 200 and "Add an account" in page.text
    # step 3: the key machinery is gone from the page as well
    assert "API keys" not in page.text and "library key" not in page.text


def test_create_account_without_store_answers_400(c, monkeypatch):
    admin(c)
    monkeypatch.setattr(userstore, "configured", lambda: False)
    r = c.post("/admin/accounts", data={"email": "new@example.com", "name": "New", "role": "user"})
    assert r.status_code == 400 and "USER_STORE_URL" in r.text


def test_account_page_shows_identity_only(c):
    admin(c)
    page = c.get("/account")
    assert page.status_code == 200 and "admin@example.com" in page.text and "Role" in page.text
    assert "API keys" not in page.text


def test_search_escapes_html(c):
    admin(c)
    page = c.get("/search", params={"q": "<script>alert(1)</script>"})
    assert page.status_code == 200 and "<script>alert" not in page.text


def test_vendors_page_lists_records_and_filters(c):
    admin(c)
    page = c.get("/vendors")
    assert page.status_code == 200 and "vendor records" in page.text and "Coverage queue" in page.text
    assert "Wärtsilä" in page.text


def test_database_pages_answer_unconfigured(c, monkeypatch):
    admin(c)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for path in ("/database", "/database/map", "/database/graph"):
        page = c.get(path)
        assert page.status_code == 200 and "Postgres layer not configured" in page.text


def test_graph_json_endpoints_need_the_database(c, monkeypatch):
    admin(c)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for path in ("/database/graph/overview.json", "/database/graph/nodes.json?q=co2",
                 "/database/graph/neighborhood.json?id=technology:ccs-cryogenic",
                 "/database/graph/center.json?kind=vendor"):
        r = c.get(path)
        assert r.status_code == 503 and "not configured" in r.json()["error"]


def test_missing_card_and_source_are_404(c):
    admin(c)
    assert c.get("/technologies/no-such-card").status_code == 404
    assert c.get("/sources/no-such-source").status_code == 404


def test_is_web_path():
    assert web.is_web_path("/") and web.is_web_path("/technologies/x") and web.is_web_path("/database/sql")
    # /login and /logout are the edge's now — the container neither serves nor exempts them
    assert not any(web.is_web_path(p) for p in ("/api/stats", "/mcp", "/api", "/login", "/logout", "/technologiesx"))


def test_neon_down_shows_fallback_notice(c, monkeypatch):
    """R5: when the configured database is unreachable, pages say so instead of failing silently
    (the SQLite fallback still renders, and the notice tells the reader it may be stale)."""
    def boom(*a, **k):
        raise web.pg.DatabaseError("connection refused (test)")
    admin(c)
    monkeypatch.setattr(web.pg, "configured", lambda: True)
    monkeypatch.setattr(web.pg, "library_stats", boom)
    r = c.get("/")
    assert r.status_code == 200 and "unreachable" in r.text


def test_compare_page_renders_side_by_side(c):
    admin(c)
    r = c.get("/compare", params={"ids": "ele-transformers,rot-heat-exchangers"})
    assert r.status_code == 200
    assert "Side by side" in r.text
    assert "Power and distribution transformers" in r.text
    assert "heat exchangers" in r.text.lower()
    solo = c.get("/compare", params={"ids": "ele-transformers"})
    assert solo.status_code == 200 and "at least two" in solo.text


def test_export_csv_answers_and_sets_download(c):
    technologies = c.get("/export", params={"kind": "technologies"})
    assert technologies.status_code == 200
    assert technologies.headers["content-type"].startswith("text/csv")
    assert "attachment" in technologies.headers.get("content-disposition", "")
    assert technologies.text.splitlines()[0].startswith("id,name,sector")
    vendors = c.get("/export", params={"kind": "vendors"})
    assert vendors.status_code == 200 and vendors.text.splitlines()[0].startswith("id,name,country")
    assert c.get("/export", params={"kind": "nope"}).status_code == 400


def test_api_reference_lists_endpoints(c):
    r = c.get("/database/api")
    assert r.status_code == 200
    assert "/api/stats" in r.text and "/api/search" in r.text


def test_search_form_has_discipline_and_region_filters(c):
    r = c.get("/search", params={"q": "boiler", "discipline": "ELE", "region": "sea"})
    assert r.status_code == 200
    assert 'name="discipline"' in r.text and 'name="region"' in r.text


def test_glossary_page_lists_terms_and_links_cards(c):
    r = c.get("/glossary")
    assert r.status_code == 200
    assert "HRSG" in r.text and "terms" in r.text
    filtered = c.get("/glossary", params={"q": "compressor"})
    assert filtered.status_code == 200


def test_standards_page_lists_and_filters(c):
    r = c.get("/standards")
    assert r.status_code == 200
    assert "IEC 61511" in r.text and "API 610" in r.text
    iec = c.get("/standards", params={"org": "IEC"})
    assert iec.status_code == 200 and "API 610" not in iec.text
    search = c.get("/standards", params={"q": "pumps"})
    assert search.status_code == 200
