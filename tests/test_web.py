"""Web interface: sign-in and session cookie, each page answering from the built index, in-process."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
starlette_testclient = pytest.importorskip("starlette.testclient")
server = pytest.importorskip("server")
import web  # noqa: E402

KEY = "k" * 32


@pytest.fixture(scope="module")
def c():
    # https base_url so the Secure session cookie is stored and sent (the transport does no real TLS)
    with starlette_testclient.TestClient(server.http_app(KEY), base_url="https://testserver") as client:
        yield client


def test_home_and_login_gate_the_site(c):
    r = c.get("/", follow_redirects=False)
    assert r.status_code == 303 and r.headers["location"].startswith("/login?next=")
    page = c.get("/login")
    assert page.status_code == 200 and 'type="password"' in page.text


def test_login_rejects_a_wrong_key(c):
    assert c.post("/login", data={"key": "wrong", "next": "/"}, follow_redirects=False).status_code == 401


def test_account_login_sets_a_user_session(c, monkeypatch):
    import users as user_accounts
    entry = f"alice@example.com|Alice|{user_accounts.hash_password('library-pass-1')}"
    monkeypatch.setenv("LIBRARY_USERS", entry)
    page = c.get("/login")
    assert page.status_code == 200 and 'name="email"' in page.text and 'name="password"' in page.text
    ok = c.post("/login", data={"email": "Alice@Example.com", "password": "library-pass-1", "next": "/technologies"},
                follow_redirects=False)
    assert ok.status_code == 303 and ok.headers["location"] == "/technologies"
    assert "oglib_session" in ok.cookies
    # the account cookie, not the key, now opens pages (fresh client without the key header)
    with starlette_testclient.TestClient(server.http_app(KEY), base_url="https://testserver") as fresh:
        fresh.cookies.set(web.COOKIE, ok.cookies.get(web.COOKIE))
        assert fresh.get("/technologies").status_code == 200
        assert fresh.get("/vendors").status_code == 200
    bad = c.post("/login", data={"email": "alice@example.com", "password": "wrong", "next": "/"},
                 follow_redirects=False)
    assert bad.status_code == 401
    monkeypatch.delenv("LIBRARY_USERS")
    none_page = c.get("/login")
    # both forms always render; the page must not disclose account state or internals
    assert 'name="email"' in none_page.text and 'name="key"' in none_page.text
    assert "LIBRARY_USERS" not in none_page.text and "No accounts" not in none_page.text
    # with no accounts configured, an email attempt fails exactly like a wrong password
    none_try = c.post("/login", data={"email": "nobody@example.com", "password": "x", "next": "/"},
                      follow_redirects=False)
    assert none_try.status_code == 401 and "Wrong email or password" in none_try.text


def test_tampered_user_sessions_are_rejected(c):
    from starlette.testclient import TestClient
    forged = "v2|eyJ1IjogImFsaWNlQGV4YW1wbGUiLCAiZXhwIjogOTk5OTk5OTk5OX0|0" * 64
    with TestClient(server.http_app(KEY), base_url="https://testserver") as fresh:
        fresh.cookies.set(web.COOKIE, forged)
        r = fresh.get("/technologies", follow_redirects=False)
        assert r.status_code == 303 and r.headers["location"].startswith("/login?next=")


def _session(client, email):
    import users as user_accounts
    client.cookies.clear()  # drop cookies from earlier tests in this module (form logins set their own)
    client.cookies.set(web.COOKIE, user_accounts.session_token(email, KEY))


def test_admin_page_gating(c, monkeypatch):
    admin = f"admin@example.com|Ada|{__import__('users').hash_password('pw-admin-1')}|admin"
    plain = f"bob@example.com|Bob|{__import__('users').hash_password('pw-bob-1')}"
    monkeypatch.setenv("LIBRARY_USERS", f"{admin};{plain}")
    # anonymous -> login
    anon = starlette_testclient.TestClient(server.http_app(KEY), base_url="https://testserver")
    r = anon.get("/admin", follow_redirects=False)
    assert r.status_code == 303 and "/login" in r.headers["location"]
    # non-admin session -> 403
    _session(c, "bob@example.com")
    assert c.get("/admin").status_code == 403
    # admin session -> the page with the add form and the store-off notice
    _session(c, "admin@example.com")
    page = c.get("/admin")
    assert page.status_code == 200 and "Add an account" in page.text and "USER_STORE_URL" in page.text
    # a signed session for an account that does not exist is not authenticated
    _session(c, "ghost@example.com")
    assert c.get("/admin", follow_redirects=False).status_code == 303
    # the library key is always admin
    c.headers["x-api-key"] = KEY
    page = c.get("/admin")
    assert page.status_code == 200
    del c.headers["x-api-key"]
    # creating accounts from the page needs the store; without it the POST says so
    _session(c, "admin@example.com")
    r = c.post("/admin/accounts", data={"email": "new@example.com", "name": "New", "password": "pw", "role": "user"})
    assert r.status_code == 400 and "USER_STORE_URL" in r.text


def test_login_sets_the_cookie_and_pages_answer(c):
    r = c.post("/login", data={"key": KEY, "next": "/"}, follow_redirects=False)
    assert r.status_code == 303 and r.headers["location"] == "/" and "oglib_session" in r.cookies
    home = c.get("/")
    assert home.status_code == 200 and "technology" in home.text.lower()
    for path in ("/technologies", "/vendors", "/register", "/sources", "/gaps"):
        assert c.get(path).status_code == 200
    search = c.get("/search", params={"q": "hydrogen"})
    assert search.status_code == 200 and ("/technologies/" in search.text or "/documents?path=" in search.text
                                          or "/sources/" in search.text)


def test_vendors_page_lists_records_and_filters(c):
    page = c.get("/vendors")
    assert page.status_code == 200 and "vendor records" in page.text and "Coverage queue" in page.text
    assert "Wärtsilä" in page.text
    one = c.get("/vendors", params={"id": "wartsila"})
    assert one.status_code == 200 and one.text.count("Wärtsilä") >= 1
    empty = c.get("/vendors", params={"id": "no-such-vendor"})
    assert empty.status_code == 200 and "0 vendor records" in empty.text


def test_database_pages_answer_unconfigured(c, monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for path in ("/database", "/database/map", "/database/graph"):
        page = c.get(path)
        assert page.status_code == 200 and "Postgres layer not configured" in page.text


def test_graph_json_endpoints_need_the_database(c, monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for path in ("/database/graph/overview.json", "/database/graph/nodes.json?q=co2",
                 "/database/graph/neighborhood.json?id=technology:ccs-cryogenic",
                 "/database/graph/center.json?kind=vendor"):
        r = c.get(path)
        assert r.status_code == 503 and "not configured" in r.json()["error"]


def test_database_unconfigured_and_documents_needs_path(c, monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    page = c.get("/database")
    assert page.status_code == 200 and "requirements-postgres.txt" in page.text
    assert c.get("/documents").status_code == 400


def test_database_pages_carry_the_second_level_tabs(c, monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for path, tab in (("/database", "/database"), ("/database/sql", "/database/sql"),
                      ("/database/search", "/database/search"), ("/database/graph", "/database/graph"),
                      ("/database/map", "/database/map")):
        page = c.get(path)
        assert page.status_code == 200
        assert 'class="subnav"' in page.text and "Atlas" in page.text and "Network" in page.text
        assert f'<a href="{tab}" class="active">' in page.text, f"{tab} tab not active on {path}"


def test_search_escapes_html(c):
    page = c.get("/search", params={"q": "<script>alert(1)</script>"})
    assert page.status_code == 200 and "<script>alert" not in page.text


def test_missing_card_and_source_are_404(c):
    assert c.get("/technologies/no-such-card").status_code == 404
    assert c.get("/sources/no-such-source").status_code == 404


def test_is_web_path():
    assert web.is_web_path("/") and web.is_web_path("/technologies/x") and web.is_web_path("/database/sql")
    assert not any(web.is_web_path(p) for p in ("/api/stats", "/mcp", "/api", "/technologiesx"))


def test_session_token_is_deterministic_and_key_bound():
    assert web.session_token(KEY) == web.session_token(KEY)
    assert web.session_token(KEY) != web.session_token("x" * 32)
    assert len(web.session_token(KEY)) == 64


def test_header_auth_without_cookie():
    with starlette_testclient.TestClient(server.http_app(KEY), base_url="https://testserver") as fresh:
        assert fresh.get("/technologies", headers={"x-api-key": KEY}).status_code == 200
        assert fresh.get("/technologies", headers={"authorization": f"Bearer {KEY}"}).status_code == 200
