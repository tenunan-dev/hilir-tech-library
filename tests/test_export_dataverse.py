import csv
import pathlib
import sys

csv.field_size_limit(sys.maxsize)

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "tools"))
import export_dataverse  # noqa: E402


def test_export_hides_restricted_text_by_default(tmp_path):
    counts = export_dataverse.export(tmp_path)
    rows = list(csv.DictReader((tmp_path / "documents.csv").open(encoding="utf-8-sig")))
    assert len(rows) == counts["documents_with_text"] + counts["documents_without_text"]
    for row in rows:
        assert (row["body"] != "") == (row["reuse_level"] == "full-text-open")
    sources = list(csv.DictReader((tmp_path / "sources.csv").open(encoding="utf-8-sig")))
    assert len(sources) == counts["sources"] and all(r["source_id"] and r["name"] for r in sources)
    assert any(r["code"] == "GAS" for r in csv.DictReader((tmp_path / "taxonomy.csv").open(encoding="utf-8-sig")))


def test_long_bodies_are_truncated_with_link():
    out = export_dataverse._fit("x" * (export_dataverse.MAX_BODY + 10), "https://example.org/r")
    assert len(out) < 1_048_576 and out.endswith("full text at https://example.org/r]")
    assert export_dataverse._fit("short", "u") == "short"
