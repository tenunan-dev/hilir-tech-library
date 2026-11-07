"""Glossary layer: entries parse, terms are unique, related ids resolve to real cards."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
import technologies  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_glossary_entries_parse_and_terms_unique():
    path = ROOT / "catalog" / "glossary.jsonl"
    assert path.exists(), "catalog/glossary.jsonl must exist"
    entries = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(entries) >= 40, f"only {len(entries)} glossary entries"
    terms = [e["term"] for e in entries]
    assert len(terms) == len(set(terms)), "duplicate glossary terms"
    for e in entries:
        assert e.get("term") and e.get("expansion"), e
        assert isinstance(e.get("related", []), list)


def test_glossary_related_ids_resolve():
    path = ROOT / "catalog" / "glossary.jsonl"
    entries = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    card_ids = {c["id"] for c in technologies.load_cards()}
    dangling = sorted({r for e in entries for r in e.get("related", []) if r not in card_ids})
    assert not dangling, f"glossary references unknown card ids: {dangling[:8]}"
