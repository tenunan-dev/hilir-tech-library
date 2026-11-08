"""Standards registry: entries parse, designations unique, org_source_ids resolve to catalogued
standards-body sources, related ids resolve to real cards or equipment classes."""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
import technologies  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent


def test_standards_parse_and_unique():
    path = ROOT / "catalog" / "standards.jsonl"
    assert path.exists(), "catalog/standards.jsonl must exist"
    entries = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(entries) >= 20, f"only {len(entries)} standards entries"
    ids = [e["id"] for e in entries]
    assert len(ids) == len(set(ids)), "duplicate standard ids"
    designations = [e["designation"] for e in entries]
    assert len(designations) == len(set(designations)), "duplicate designations"
    for e in entries:
        assert e.get("designation") and e.get("title") and e.get("org") and e.get("scope"), e
        assert isinstance(e.get("related", []), list)


def test_standards_org_sources_are_catalogued():
    entries = [json.loads(line) for line in (ROOT / "catalog" / "standards.jsonl").read_text().splitlines() if line.strip()]
    for e in entries:
        sid = e.get("org_source_id")
        if sid:
            assert (ROOT / "catalog" / "sources" / f"{sid}.json").exists(), f"{e['id']}: unknown org_source_id {sid}"


def test_standards_related_ids_resolve():
    entries = [json.loads(line) for line in (ROOT / "catalog" / "standards.jsonl").read_text().splitlines() if line.strip()]
    card_ids = {c["id"] for c in technologies.load_cards()}
    equip = set()
    for line in (ROOT / "catalog" / "equipment.jsonl").read_text().splitlines():
        if line.strip():
            equip.add("equipment:" + json.loads(line)["id"])
    known = card_ids | equip
    dangling = sorted({r for e in entries for r in e.get("related", []) if r not in known})
    assert not dangling, f"standards reference unknown ids: {dangling[:8]}"
