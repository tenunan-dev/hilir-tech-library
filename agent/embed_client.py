"""Query-embedding client for search fusion (decision #32).

`query_vector(query, db)` returns a unit-length 384-dim vector for a search query, or
None when no embedder exists (callers then stay keyword-only). Embedding is local
fastembed (the same code path agent/embed.py's load_embedder uses); the edge /__embed
service was retired 2026-10-31 (decision #34 P3.1) and its client — which also
carried the library key — was removed with the key system (step 3, AUTH-REBUILD §4.3).

Successful vectors are cached (bounded); None is never cached, so a recovering
embedder is picked up on the next query.
"""

EMBED_DIM = 384
_cache = {}


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


def query_vector(query, db=None):
    """Unit-length EMBED_DIM vector for a search query, or None for keyword-only mode."""
    q = query.strip()
    if not q:
        return None
    if q in _cache:
        return _cache[q]
    vec = _local_vector(q, db)
    if vec is not None and len(_cache) < 256:
        _cache[q] = vec
    return vec
