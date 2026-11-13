"""Guard: the built index must keep its vectors through the publish chain.

The publish chain is build.py -> library.py build -> embed.py -> load_postgres.py.
`library.py build` recreates the index (dropping the `vectors` table), and the
embed step refills it from the cache. Running the loader against an index whose
vectors table is empty publishes a corpus with no semantic search and no error —
it has silently happened three times on 2026-11-13.

The guard reads build/library.db directly, because that table is what the loader
reads. A fresh checkout legitimately has not embedded yet, so the emptiness check
only fires when an embed cache exists to prove an embedding pass has run before.
"""

import pathlib
import sqlite3

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB = ROOT / "build" / "library.db"
CACHE = ROOT / "build" / "embed-cache.db"


def _counts():
    if not DB.exists():
        pytest.skip("no build/library.db (run agent/library.py build first)")
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    try:
        vectors = con.execute("SELECT count(*) FROM vectors").fetchone()[0]
        searchable = con.execute("SELECT count(*) FROM search").fetchone()[0]
    finally:
        con.close()
    return vectors, searchable


def test_vectors_belong_to_live_rows():
    """Every vector must hang off a row that is still searchable (stale embeds are a bug)."""
    vectors, searchable = _counts()
    if vectors == 0:
        pytest.skip("index has not been embedded yet")
    assert vectors <= searchable, (
        f"{vectors} vectors for only {searchable} searchable rows — the index was "
        "rebuilt without re-embedding, so rows carry vectors for rows that no longer exist"
    )


def test_index_is_not_emptied_after_an_embed_pass():
    """A served index that has embedded before must not come back with zero vectors.

    The presence of the embed cache is the evidence that embedding ran. If the
    cache holds rows but the index holds none, `library.py build` has just wiped
    the table and the loader would publish an empty semantic layer.
    """
    vectors, _ = _counts()
    if not CACHE.exists():
        pytest.skip("no embed cache: this checkout has never embedded")
    con = sqlite3.connect(f"file:{CACHE}?mode=ro", uri=True)
    try:
        cached = con.execute("SELECT count(*) FROM cache").fetchone()[0]
    except sqlite3.Error:
        pytest.skip("embed cache has no cache table")
    finally:
        con.close()
    if cached == 0:
        pytest.skip("embed cache is empty")
    assert vectors > 0, (
        f"embed cache holds {cached} vectors but the index holds none — "
        "run agent/embed.py after agent/library.py build before publishing"
    )
