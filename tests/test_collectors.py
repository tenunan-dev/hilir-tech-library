"""Offline tests for the collectors: no network, fetch is replaced with fixtures."""
import json
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "collectors"))

import adapters  # noqa: E402
import common  # noqa: E402

RSS = """<?xml version="1.0"?><rss version="2.0"><channel><title>Energies</title>
<item><title>Hydrogen compression review</title><link>https://example.org/a1</link><pubDate>Mon, 19 Oct 2026 00:00:00 GMT</pubDate></item>
<item><title>No link item</title></item>
</channel></rss>"""

ATOM = """<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">
<entry><id>http://arxiv.org/abs/2610.00001v1</id><published>2026-10-20T00:00:00Z</published>
<title>  Electrolyzer   stack degradation </title><summary> We model  degradation. </summary>
<author><name>A. Author</name></author><author><name>B. Author</name></author></entry></feed>"""

HTML = ("<html><head><title>Article</title></head><body><article><h1>Hydrogen compression review</h1>"
        + "<p>Reciprocating compressors remain the workhorse for hydrogen refuelling stations. </p>" * 12
        + "</article></body></html>")


class FakeResponse:
    def __init__(self, text, content_type="text/html"):
        self.text = text
        self.content = text.encode("utf-8")
        self.headers = {"Content-Type": content_type}

    def json(self):
        return json.loads(self.text)


def record(**over):
    rec = {"id": "test-src", "url": "https://example.org", "licence": "CC-BY-4.0", "reuse_level": "full-text-open",
           "permitted_use": "any", "sectors": ["H2"], "disciplines": ["ROT"], "verification": "verified",
           "automated_access": "unstated", "feeds": ["https://example.org/rss"]}
    rec.update(over)
    return rec


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    monkeypatch.setattr(common, "CORPUS", tmp_path)
    monkeypatch.setattr(common, "MANIFEST", tmp_path / "manifest.jsonl")
    monkeypatch.setattr(adapters, "CORPUS", tmp_path)
    monkeypatch.setattr(common, "ROOT", tmp_path)
    return tmp_path


def test_collectable_rules():
    assert common.collectable(record())
    assert not common.collectable(record(verification="unverified"))
    assert not common.collectable(record(reuse_level="summary-only"))
    assert not common.collectable(record(automated_access="prohibited"))


def test_parse_feed_rss_and_atom():
    assert adapters.parse_feed(RSS)[0] == ("Hydrogen compression review", "https://example.org/a1",
                                           "Mon, 19 Oct 2026 00:00:00 GMT")
    title, link, published = adapters.parse_feed(ATOM)[0]
    assert link == "" and published == "2026-10-20T00:00:00Z"


def test_rss_adapter_writes_document_once(corpus, monkeypatch):
    pages = {"https://example.org/rss": FakeResponse(RSS, "application/rss+xml"), "https://example.org/a1": FakeResponse(HTML)}
    monkeypatch.setattr(adapters, "fetch", lambda url, **kw: pages[url])
    rec = record()
    docs = list(adapters.rss(rec, 10))
    assert len(docs) == 1
    title, url, body, published, _ = docs[0]
    assert "Reciprocating compressors" in body
    path = common.write_document(rec, title, url, body, published)
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\nsource_id: \"test-src\"")
    assert 'licence: "CC-BY-4.0"' in text and "use_note" not in text
    assert common.write_document(rec, title, url, body, published) is None  # duplicate by hash


def test_restricted_documents_carry_use_note(corpus):
    rec = record(reuse_level="full-text-restricted", licence="proprietary", permitted_use="personal-non-commercial")
    path = common.write_document(rec, "Brochure", "https://example.org/b", "Some text")
    assert "Private reference copy" in path.read_text(encoding="utf-8")


def test_arxiv_adapter_keeps_metadata_only(monkeypatch):
    monkeypatch.setattr(adapters, "fetch", lambda url, **kw: FakeResponse(ATOM, "application/atom+xml"))
    title, url, body, published, extra = next(adapters.arxiv(record(id="arxiv"), 5))
    assert title == "Electrolyzer stack degradation"
    assert url == "http://arxiv.org/abs/2610.00001v1"
    assert "A. Author, B. Author" in body and "We model degradation." in body
    assert extra["licence"] == "CC0-1.0"


def test_manual_inbox_uses_sidecar_url(corpus):
    inbox = corpus / "_inbox" / "test-src"
    inbox.mkdir(parents=True)
    (inbox / "compressor-brochure.html").write_text(HTML, encoding="utf-8")
    (inbox / "compressor-brochure.html.url").write_text("https://example.org/brochure\n", encoding="utf-8")
    title, url, body, _, extra = next(adapters.manual(record(), 10))
    assert title == "compressor brochure" and url == "https://example.org/brochure"
    assert "Reciprocating compressors" in body and extra == {"collected": "manual"}


def test_empty_body_is_not_written(corpus):
    assert common.write_document(record(), "Empty", "https://example.org/e", "   ") is None


@pytest.mark.parametrize("status,text,allowed", [
    (403, "Access Denied", False),
    (401, "", False),
    (503, "", False),
    (404, "", True),
    (200, "User-agent: *\nDisallow: /private/", True),
])
def test_robots_status_handling(monkeypatch, status, text, allowed):
    class Resp:
        status_code = status

    Resp.text = text
    monkeypatch.setattr(common, "_robots", {})
    monkeypatch.setattr(common.requests, "get", lambda *a, **kw: Resp())
    assert common.allowed_by_robots("https://example.org/articles/1") is allowed


def test_robots_unreachable_disallows(monkeypatch):
    def boom(*a, **kw):
        raise common.requests.ConnectionError("down")

    monkeypatch.setattr(common, "_robots", {})
    monkeypatch.setattr(common.requests, "get", boom)
    assert common.allowed_by_robots("https://example.org/x") is False


def test_osti_adapter_requests_json(monkeypatch):
    seen = {}
    item = {"osti_id": "3413920", "title": "Lignin dissolution", "publication_date": "2026-09-01T00:00:00Z",
            "authors": ["Steuck, D."], "description": "Abstract.",
            "links": [{"rel": "citation", "href": "https://www.osti.gov/biblio/3413920"}]}

    def fake_fetch(url, headers=None, **kw):
        seen["headers"] = headers
        return FakeResponse(json.dumps([item]), "application/json")
    monkeypatch.setattr(adapters, "fetch", fake_fetch)
    docs = list(adapters.osti(record(id="osti"), 1))
    assert seen["headers"]["Accept"] == "application/json"
    assert docs[0][0] == "Lignin dissolution" and docs[0][1] == "https://www.osti.gov/biblio/3413920"
    assert "Abstract." in docs[0][2]


def test_arxiv_api_is_a_documented_robots_exception(monkeypatch):
    def refuse(*a, **kw):
        raise AssertionError("robots.txt should not be read for an excepted prefix")

    monkeypatch.setattr(common, "_robots", {})
    monkeypatch.setattr(common.requests, "get", refuse)
    assert common.allowed_by_robots("https://export.arxiv.org/api/query?search_query=x") is True


def test_arxiv_query_is_balanced_and_title_scoped():
    assert adapters.ARXIV_QUERY.count("(") == adapters.ARXIV_QUERY.count(")")
    assert "abs:" not in adapters.ARXIV_QUERY and 'ti:"natural gas"' in adapters.ARXIV_QUERY
    for ambiguous in ("pipeline", "flare", "compressor"):
        assert f'ti:"{ambiguous}"' not in adapters.ARXIV_QUERY


def test_open_document_licence_overrides_restricted_source(corpus):
    rec = record(id="arxiv", reuse_level="full-text-restricted", licence="CC0-1.0 metadata; per-paper full text")
    text = common.write_document(rec, "Paper", "http://arxiv.org/abs/1", "Abstract", extra={"licence": "CC0-1.0"}).read_text()
    assert 'reuse_level: "full-text-open"' in text and "use_note" not in text


def test_undouble_collapses_faux_bold_only():
    text = "PPrroocceessss DDeessiiggnn CCoonncceepptt ooff the 1100 MW unit; Mississippi, Process, aabbcc"
    assert common.undouble(text) == "Process Design Concept of the 1100 MW unit; Mississippi, Process, abc"


def test_pdf_page_failure_keeps_other_pages(monkeypatch):
    class Page:
        def __init__(self, text):
            self.text = text

        def extract_text(self):
            if self.text is None:
                raise RuntimeError("Reached maximum number of tokens per stream")
            return self.text

    class Reader:
        def __init__(self, stream):
            self.pages = [Page("First page"), Page(None), Page("Third page")]

    import pypdf
    monkeypatch.setattr(pypdf, "PdfReader", Reader)
    assert common.to_markdown(b"%PDF", "application/pdf") == "First page\n\nThird page"


def test_manual_limit_ignores_sidecars(corpus):
    inbox = corpus / "_inbox" / "test-src"
    inbox.mkdir(parents=True)
    for n in range(3):
        (inbox / f"doc-{n}.html").write_text(HTML, encoding="utf-8")
        (inbox / f"doc-{n}.html.url").write_text(f"https://example.org/{n}\n", encoding="utf-8")
    assert len(list(adapters.manual(record(), 3))) == 3
