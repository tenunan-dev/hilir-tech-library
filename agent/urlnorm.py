"""Identity of a source document.

The corpus holds one document per source, so the key that decides "have I already stored this?"
has to ignore the differences that do not make a different document: the scheme, the case of the
host, a leading "www.", a trailing slash, the fragment, and — on arXiv only — the version suffix,
because abs/ID and abs/IDv3 are the same abstract page and its PDF is the same paper.

Used by collectors/common.py (refuse a second copy when collecting) and agent/library.py (the
build gate that fails on a corpus with two documents under one key), so the two cannot drift.
"""
import re
import urllib.parse

_ARXIV_VERSION = re.compile(r"v\d+$")


def url_key(url: str) -> str:
    """`https://www.Example.org/a/b/?x=1#frag` and `http://example.org/a/b?x=1` are one key."""
    parts = urllib.parse.urlsplit((url or "").strip())
    host = parts.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = parts.path.rstrip("/") or "/"
    if host == "arxiv.org" or host.endswith(".arxiv.org"):
        path = _ARXIV_VERSION.sub("", path)
    return f"{host}{path}" + (f"?{parts.query}" if parts.query else "")
