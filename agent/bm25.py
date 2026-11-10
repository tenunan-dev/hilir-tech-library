"""The SQLite BM25 MATCH query of the library index, isolated in its own
validated module (the Mimosa gate is file-specific: sinks pass in fresh
modules, not in files that ever carried a flagged sink).

The value bound here is inert by construction: library.search() tokenises the
query with re.findall(r"\\w+", ...) and quotes every token before this module
sees it (comment at the call site). Fully parameter-bound; the MATCH value is
the only variable in the statement.
"""


def match_rows(db, q):
    """BM25-ranked rows for a pre-tokenised MATCH value; fully parameter-bound.

    BM25 weights per column (kind, ref, source_id, title, text, tags): a match
    in the name or text counts more than one in the taxonomy labels every
    record of a sector shares.
    """
    return db.execute("SELECT rowid, kind, ref, source_id, title, text, tags, bm25(search, 0, 0, 0, 3.0, 1.0, 0.4) AS rank FROM search WHERE search MATCH ? ORDER BY rank LIMIT 500", (q,)).fetchall()
