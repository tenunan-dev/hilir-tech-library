"""Query-embedding client for search fusion (decision #32).

`query_vector(query, db)` returns a unit-length 384-dim vector for a search query, or
None when no embedder exists (callers then stay keyword-only). Order of preference:

1. local fastembed (the Mac, or any host with fastembed installed and a model row in the
   index) — same code path agent/embed.py's load_embedder uses;
2. the edge Worker's /__embed route, which runs the same model family the index was
   built with (Workers AI @cf/baai/bge-small-en-v1.5, 384 dims) — the hosted container
   has no fastembed, so it lands here; LIBRARY_PUBLIC_URL and LIBRARY_API_KEY (both
   injected by the edge) must be set.

Security: the service destination is allowlist-validated (only this library's own
host), https only, redirects refused, and the library key travels only in the header.
The query text is JSON in the request body — it never forms part of any URL or command
line. Successful vectors are cached (bounded); None is never cached, so a recovering
service is picked up on the next query.
"""
import os
import urllib.parse

# Literal allowlist: the only origin this client may ever call (this library's own edge
# Worker). LIBRARY_PUBLIC_URL selects scheme/host; any host not listed here is refused.
ALLOWED_EMBED_HOSTS = ("techlib.hilir.app",)
EMBED_DIM = 384
_TIMEOUT = 10
_cache = {}


def _endpoint():
    parts = urllib.parse.urlsplit(os.environ.get("LIBRARY_PUBLIC_URL", ""))
    key = os.environ.get("LIBRARY_API_KEY", "")
    if parts.scheme != "https" or parts.hostname not in ALLOWED_EMBED_HOSTS or not key:
        return None, None
    return f"https://{parts.hostname}/__embed", key


def _local_vector(query, db):
    """Unit vector via local fastembed when the index carries one; None otherwise."""
    if db is None:
        return None
    try:
        import embed as _embed  # local module (agent/embed.py)
    except ImportError:
        return None
    embedder = _embed.load_embedder(db)
    if embedder is None:
        return None
    try:
        import numpy as np
        v = np.asarray(embedder([query])[0], dtype=np.float32)
        n = float(np.linalg.norm(v))
        return (v / n).tolist() if n else None
    except Exception:
        return None


def _service_vector(text):
    """Unit vector from the edge /__embed service; None on any failure."""
    import requests
    url, key = _endpoint()
    if not url:
        return None
    try:
        r = requests.post(url, json={"text": text[:2000]},
                          headers={"x-api-key": key}, timeout=_TIMEOUT, allow_redirects=False)
        if r.status_code != 200:
            return None
        vec = r.json().get("vector")
        if not isinstance(vec, list) or len(vec) != EMBED_DIM:
            return None
        import numpy as np
        v = np.asarray(vec, dtype=np.float32)
        n = float(np.linalg.norm(v))
        return (v / n).tolist() if n else None
    except Exception:
        return None


def query_vector(query, db=None):
    """Unit-length EMBED_DIM vector for a search query, or None for keyword-only mode."""
    q = query.strip()
    if not q:
        return None
    if q in _cache:
        return _cache[q]
    vec = _local_vector(q, db) or _service_vector(q)
    if vec is not None and len(_cache) < 256:
        _cache[q] = vec
    return vec
