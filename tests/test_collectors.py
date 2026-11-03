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


def test_fetch_refuses_non_public_destinations():
    for bad in ("http://127.0.0.1:8000/admin", "http://10.1.2.3/report", "http://[::1]/x", "ftp://example.org/x"):
        with pytest.raises(PermissionError):
            common.fetch(bad)


def test_check_url_falls_back_to_get_and_notes_redirect(monkeypatch):
    class Resp:
        def __init__(self, status, url, text=""):
            self.status_code, self.url, self.text = status, url, text

        def close(self):
            pass

    monkeypatch.setattr(common, "_robots", {})
    monkeypatch.setattr(common.requests, "head", lambda url, **kw: Resp(405, "https://example.org/a"))
    monkeypatch.setattr(common.requests, "get", lambda url, **kw: Resp(200, "https://example.org/final"))
    assert common.check_url("https://example.org/a") == (200, "https://example.org/final")


def test_parse_feed_rejects_entity_expansion():
    from defusedxml import DefusedXmlException
    evil = ('<?xml version="1.0"?><!DOCTYPE rss [<!ENTITY xxe "stolen">]>'
            '<rss version="2.0"><channel><title>&xxe;</title></channel></rss>')
    with pytest.raises(DefusedXmlException):
        adapters.parse_feed(evil)


# --- OSTI full-text policy: report-style products under uncontrolled distribution store a
# private reference copy; journal articles stay metadata-and-abstract. --------------------

def _minimal_pdf(paragraph: str) -> bytes:
    """A one-page PDF pypdf can parse and extract, built inline so the test stays offline."""
    stream = f"BT /F1 12 Tf 72 700 Td ({paragraph}) Tj ET".encode()
    header = b"%PDF-1.4\n"
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R "
        b"/Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out, offsets = header, []
    for i, body in enumerate(objs, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"
    xref_at = len(out)
    out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
    out += b"".join(f"{off:010d} 00000 n \n".encode() for off in offsets)
    out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_at}\n%%EOF".encode()
    return out


OSTI_REPORT = {"osti_id": "1234567", "title": "CO2 network assessment",
               "product_type": "Technical Report",
               "availability": "External/unlimited (No CUI, UCNI, or other controlled access information)",
               "publication_date": "2026-08-01T00:00:00Z", "authors": ["A. Analyst"],
               "description": "Report abstract.",
               "links": [{"rel": "citation", "href": "https://www.osti.gov/biblio/1234567"},
                         {"rel": "fulltext", "href": "https://www.osti.gov/servlets/purl/1234567"}]}
OSTI_JOURNAL = {"osti_id": "1234568", "title": "Capture solvents reviewed",
                "product_type": "Journal Article",
                "publication_date": "2026-09-01T00:00:00Z", "authors": ["B. Researcher"],
                "description": "Journal abstract.",
                "links": [{"rel": "citation", "href": "https://www.osti.gov/biblio/1234568"},
                          {"rel": "fulltext", "href": "https://www.osti.gov/servlets/purl/1234568"}]}


def test_osti_report_product_stores_full_text_as_private_copy(monkeypatch):
    pdf = _minimal_pdf("Analysis of CO2 transport network compression and pipeline design. " * 10)
    pdf_response = FakeResponse("", "application/pdf")
    pdf_response.content = pdf
    monkeypatch.setattr(
        adapters, "fetch",
        lambda url, headers=None, **kw: pdf_response if "servlets/purl" in url
        else FakeResponse(json.dumps([OSTI_REPORT]), "application/json"))
    docs = list(adapters.osti(record(id="osti", licence="mixed-per-document",
                                     reuse_level="full-text-restricted"), 5))
    report = next(d for d in docs if d[0] == "CO2 network assessment")
    assert "Analysis of CO2 transport network" in report[2], "full text should lead the body"
    assert "Report abstract." in report[2]
    assert report[4]["content"] == "full-text-report"
    assert "private reference copy" in report[4]["rights_note"]


def test_osti_journal_article_stays_metadata_and_abstract(monkeypatch):
    monkeypatch.setattr(adapters, "fetch",
                        lambda url, headers=None, **kw:
                        FakeResponse(json.dumps([OSTI_JOURNAL]), "application/json"))
    docs = list(adapters.osti(record(id="osti"), 5))
    title, url, body, _, extra = docs[0]
    assert title == "Capture solvents reviewed" and "Journal abstract." in body
    assert extra["content"] == "metadata-and-abstract"
    assert url == "https://www.osti.gov/biblio/1234568"


def test_osti_report_without_uncontrolled_availability_stays_abstract(monkeypatch):
    item = dict(OSTI_REPORT, availability=None)
    monkeypatch.setattr(adapters, "fetch",
                        lambda url, headers=None, **kw:
                        FakeResponse(json.dumps([item]), "application/json"))
    docs = list(adapters.osti(record(id="osti"), 5))
    assert docs[0][4]["content"] == "metadata-and-abstract"


def test_osti_fulltext_fetch_failure_falls_back_to_abstract(monkeypatch):
    def fetch(url, headers=None, **kw):
        if "api/v1/records" in url:
            return FakeResponse(json.dumps([OSTI_REPORT]), "application/json")
        raise RuntimeError("purl down")
    monkeypatch.setattr(adapters, "fetch", fetch)
    docs = list(adapters.osti(record(id="osti"), 5))
    assert docs[0][4]["content"] == "metadata-and-abstract" and "Report abstract." in docs[0][2]
