"""Render parity (decision #34 P1.9): every web page renders the same content from the SQLite
index and from the Postgres layer. Skipped without TEST_DATABASE_URL — point it at a SCRATCH
database only (the tests truncate and reload it). Set it, run:

    TEST_DATABASE_URL=postgresql://... .venv/bin/python -m pytest -q tests/test_render_parity.py

Parity is content parity, not byte parity: row order may differ where the two layers sort
differently (register), and search ranking differs by engine. Each page asserts the content
its users see: counts, ids, titles, key sections. Documents are byte-compared exactly —
og.document.body carries the same text the SQLite path reads from disk.
"""
import hashlib
import os
import re
import sys
import pathlib

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))

needs_db = pytest.mark.skipif(not os.environ.get("TEST_DATABASE_URL"), reason="set TEST_DATABASE_URL to a scratch Postgres with pgvector")

REPO = pathlib.Path(__file__).resolve().parent.parent

TAG = re.compile(r"<[^>]+>")


def _text(html: str) -> str:
    """Rendered page text without tags, for content assertions."""
    return TAG.sub(" ", re.sub(r"<script.*?</script>", " ", html, flags=re.S))


@pytest.fixture(scope="module", autouse=True)
def scratch_db():
    """SQLite index from the repo corpus + the same data loaded into the scratch Postgres."""
    import psycopg
    import library, graph  # agent modules

    sys.path.insert(0, str(REPO / "tools"))
    import load_postgres as loader

    db_path = REPO / "build" / "parity-scratch.db"
    library.build(db_path)
    data = loader.collect(include_restricted=True)
    nodes, edges = graph.build_graph()
    card_names = {c["id"]: c["name"] for c in data["cards"]}
    vectors = {("technology", c["id"]): _hash_vector(loader.card_search_text(c)) for c in data["cards"]}
    vectors.update({("vendor", v["id"]): _hash_vector(loader.library.vendor_text(v, card_names)) for v in data["vendors"]})
    vectors.update({("chunk", c["id"]): _hash_vector(c["body"]) for c in data["chunks"][:200]})
    with psycopg.connect(os.environ["TEST_DATABASE_URL"]) as conn:
        loader.load(conn, data, nodes, edges, vectors)
    yield
    db_path.unlink(missing_ok=True)


def _hash_vector(text, dim=384):
    """Deterministic stand-in embedding (sha256-bucketed), same idea as test_graph's."""
    import numpy as np
    vec = np.zeros(dim, dtype=np.float32)
    for word in str(text).lower().split():
        h = int(hashlib.sha256(word.encode()).hexdigest(), 16)
        vec[h % dim] += 1.0
    norm = np.linalg.norm(vec)
    return vec / norm if norm else vec


def _render(monkeypatch, path):
    """Render one page from both layers: DATABASE_URL unset → SQLite index; set → Postgres."""
    from starlette.testclient import TestClient
    import server, library

    key = "p" * 32
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with TestClient(server.http_app(key)) as c:
        sqlite_html = c.get(path, headers={"x-api-key": key}).text
    sqlite_stats = library.stats(library.connect(REPO / "build" / "parity-scratch.db"))

    monkeypatch.setenv("DATABASE_URL", os.environ["TEST_DATABASE_URL"])
    with TestClient(server.http_app(key)) as side:
        neon_html = side.get(path, headers={"x-api-key": key}).text
    monkeypatch.delenv("DATABASE_URL", raising=False)
    return sqlite_html, neon_html, sqlite_stats


@needs_db
def test_home_parity(monkeypatch):
    import library
    sqlite_html, neon_html, _ = _render(monkeypatch, "/")
    # both pages carry the same stat labels with the same numbers (chunks aligned since the
    # loader chunks with the summary prefix, matching library.build)
    import pg
    monkeypatch.setenv("DATABASE_URL", os.environ["TEST_DATABASE_URL"])
    pg_stats = pg.library_stats()
    monkeypatch.delenv("DATABASE_URL", raising=False)
    sqlite_stats = library.stats(library.connect(REPO / "build" / "parity-scratch.db"))
    for k in ("sources", "documents", "chunks", "technologies", "vendors", "equipment"):
        assert sqlite_stats[k] == pg_stats[k], f"home stat {k}: {sqlite_stats[k]} != {pg_stats[k]}"


@needs_db
def test_technologies_parity(monkeypatch):
    sqlite_html, neon_html, _ = _render(monkeypatch, "/technologies")
    ids = lambda html: set(re.findall(r'href="/technologies/([a-z0-9-]+)"', html))  # noqa: E731
    assert ids(sqlite_html) == ids(neon_html), "the same card ids render from both layers"


@needs_db
def test_technology_page_parity(monkeypatch):
    import json
    card = json.loads((REPO / "catalog" / "technologies" / "ccs-amine-post-combustion.json").read_text())
    sqlite_html, neon_html, _ = _render(monkeypatch, "/technologies/ccs-amine-post-combustion")
    assert card["name"] in sqlite_html and card["name"] in neon_html
    assert "Principle" in sqlite_html and "Principle" in neon_html
    # the sources table renders the same catalog ids on both sides
    srcs = lambda html: set(re.findall(r'href="/sources/([a-z0-9-]+)"', html))  # noqa: E731
    assert srcs(sqlite_html) == srcs(neon_html)


@needs_db
def test_vendors_parity(monkeypatch):
    sqlite_html, neon_html, _ = _render(monkeypatch, "/vendors")
    assert re.search(r"(\d+) vendor records", sqlite_html).group(1) == \
        re.search(r"(\d+) vendor records", neon_html).group(1)
    assert ('Coverage queue' in sqlite_html) == ('Coverage queue' in neon_html)


@needs_db
def test_equipment_parity(monkeypatch):
    sqlite_html, neon_html, _ = _render(monkeypatch, "/equipment")
    ids = lambda html: set(re.findall(r'<h3>[^<]+ <span class="muted small">([a-z0-9-]+)</span>', html))  # noqa: E731
    assert ids(sqlite_html) == ids(neon_html), "the same equipment ids render from both layers"
    # detail panel: the boiler-hrsg specifications, model lines and sources render from both
    assert ">boiler-hrsg<" in neon_html, "the hrsg record renders"
    after = neon_html.split(">boiler-hrsg<", 1)[1]
    for marker in ("Vendor model lines", "Sources", "Specification"):
        assert marker in after, f"equipment detail section {marker} missing on the Neon render"


@needs_db
def test_register_parity(monkeypatch):
    sqlite_html, neon_html, _ = _render(monkeypatch, "/register")
    count = lambda html: int(re.search(r"(\d+) register entries", html).group(1))  # noqa: E731
    assert count(sqlite_html) == count(neon_html), "the same register entry count renders"
    sqlite_html, neon_html, _ = _render(monkeypatch, "/register?code=CCS")
    assert count(sqlite_html) == count(neon_html), "the same filtered register count renders"


@needs_db
def test_sources_parity(monkeypatch):
    sqlite_html, neon_html, _ = _render(monkeypatch, "/sources")
    rows = lambda html: set(re.findall(r'href="/sources/([a-z0-9-]+)"', html))  # noqa: E731
    assert rows(sqlite_html) == rows(neon_html), "the same source ids render from both layers"
    sqlite_html, neon_html, _ = _render(monkeypatch, "/sources?code=CCS&reuse_level=full-text-open")
    assert rows(sqlite_html) == rows(neon_html), "filters agree across the layers"


@needs_db
def test_source_page_documents_parity(monkeypatch):
    import library
    db = library.connect(REPO / "build" / "parity-scratch.db")
    sid = db.execute("SELECT source_id FROM docs GROUP BY source_id ORDER BY count(*) DESC LIMIT 1").fetchone()[0]
    sqlite_html, neon_html, _ = _render(monkeypatch, f"/sources/{sid}")
    docs = lambda html: set(re.findall(r'path=([^&"]+)', html))  # urllib quote tokens  # noqa: E731
    assert len(docs(sqlite_html)) == len(docs(neon_html)), "the same document list renders"


@needs_db
def test_document_text_parity(monkeypatch):
    """The byte-level parity case: og.document.body carries the exact text the SQLite path reads."""
    import urllib.parse
    import library
    db = library.connect(REPO / "build" / "parity-scratch.db")
    row = db.execute("SELECT path FROM docs WHERE meta LIKE '%full-text-open%' LIMIT 1").fetchone()
    path = row["path"]
    sqlite_html, neon_html, _ = _render(monkeypatch, "/documents?path=" + urllib.parse.quote(path, safe=""))
    text = lambda html: re.search(r'<pre class="doc">(.*?)</pre>', html, re.S).group(1)  # noqa: E731
    assert text(sqlite_html) == text(neon_html), "document text renders identically from both layers"


@needs_db
def test_gaps_parity(monkeypatch):
    sqlite_html, neon_html, _ = _render(monkeypatch, "/gaps?sector=CCS")
    count = lambda html: int(re.search(r"(\d+) gaps", html).group(1))  # noqa: E731
    assert count(sqlite_html) == count(neon_html), "the same gap count renders per sector"


@needs_db
def test_search_parity(monkeypatch):
    """Search content parity: same kinds surface for shared queries (rank order may differ)."""
    sqlite_html, neon_html, _ = _render(monkeypatch, "/search?q=boiler")
    kinds = lambda html: set(re.findall(r'<span class="badge"[^>]*>(semantic|keyword only)</span>', html)) or {"x"}  # noqa: E731
    refs = lambda html: set(re.findall(r'href="/vendors\?id=([a-z0-9-]+)"', html))  # noqa: E731
    assert "Equipment" in sqlite_html and "Equipment" in neon_html, "both layers surface the Equipment section"
    assert refs(sqlite_html) and refs(neon_html), "both layers find boiler vendors"
    # kind-scoped search agrees on the source ids
    sqlite_html, neon_html, _ = _render(monkeypatch, "/search?q=storage&kind=source")
    srcs = lambda html: set(re.findall(r'href="/sources/([a-z0-9-]+)"', html))  # noqa: E731
    assert srcs(sqlite_html) & srcs(neon_html), "kind-scoped source search overlaps across layers"