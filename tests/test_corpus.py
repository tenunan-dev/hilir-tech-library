"""The corpus holds one document per source: the same url must not be indexed twice.

A duplicate puts one document in two ranking slots, so a search returns the same passage twice
(the 2026-11-23 finding: 12 documents, about 1,900 duplicate chunks). `tools/build.py` refuses a
build with a duplicate and these tests keep the invariant visible offline.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))

import library  # noqa: E402


def _doc(folder, name, title, url, body="Body text."):
    folder.mkdir(parents=True, exist_ok=True)
    meta = {"source_id": folder.name, "title": title, "url": url, "licence": "public-domain",
            "reuse_level": "full-text-open"}
    front = "\n".join(f"{k}: {json.dumps(v)}" for k, v in meta.items())
    path = folder / name
    path.write_text(f"---\n{front}\n---\n\n# {title}\n\n{body}\n", encoding="utf-8")
    return path


def test_the_corpus_holds_one_document_per_url():
    assert library.duplicate_documents() == {}


def test_duplicate_documents_reports_one_url_with_two_files(tmp_path):
    corpus = tmp_path / "corpus"
    _doc(corpus / "netl", "report-f43dd9c1.md", "DOE/NETL Best Practices", "https://example.org/report.pdf")
    _doc(corpus / "netl", "report-8b88bb67.md", "report", "https://example.org/report.pdf")
    _doc(corpus / "netl", "other.md", "Other", "https://example.org/other.pdf")
    groups = library.duplicate_documents(corpus)
    assert list(groups) == ["example.org/report.pdf"]
    assert sorted(pathlib.Path(p).name for p in groups["example.org/report.pdf"]) == [
        "report-8b88bb67.md", "report-f43dd9c1.md"]


def test_url_variants_of_one_source_are_one_document(tmp_path):
    """Scheme, case, www., a trailing slash, the fragment and an arXiv version suffix do not make a
    different document — a metadata record at abs/IDv1 beside the full text of abs/ID is the case
    that survived the sha256 guard (2026-11-23)."""
    corpus = tmp_path / "corpus"
    _doc(corpus / "arxiv", "paper-fulltext.md", "Paper", "https://arxiv.org/abs/2607.06093")
    _doc(corpus / "arxiv", "paper-abstract.md", "Paper (abstract)", "http://arxiv.org/abs/2607.06093v1")
    groups = library.duplicate_documents(corpus)
    assert list(groups) == ["arxiv.org/abs/2607.06093"]
    assert len(groups["arxiv.org/abs/2607.06093"]) == 2


def test_the_corpus_holds_no_abstract_record_beside_a_full_text():
    """The 2026-11-23 sweep left one arXiv pair open; normalising the version suffix found 23 more.
    They are gone, so the invariant covers metadata records too."""
    assert library.duplicate_documents() == {}


def test_staging_folder_is_not_indexed_so_it_never_counts_as_a_duplicate(tmp_path):
    corpus = tmp_path / "corpus"
    _doc(corpus / "netl", "report.md", "Report", "https://example.org/report.pdf")
    _doc(corpus / "_inbox", "report.md", "Report", "https://example.org/report.pdf")
    _doc(corpus / "_inbox" / "netl", "report.md", "Report", "https://example.org/report.pdf")
    assert library.duplicate_documents(corpus) == {}
