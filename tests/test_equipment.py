"""Equipment catalog: every record is valid, ids are unique, and vendor/technology links resolve."""
import json
import jsonschema
import pathlib
import sys
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402

SCHEMA = json.loads((ROOT / "schema" / "equipment.schema.json").read_text(encoding="utf-8"))
EQUIPMENT = [
    json.loads(p.read_text(encoding="utf-8"))
    for p in sorted((ROOT / "catalog" / "equipment").glob("*.json"))
]
CARDS = {c["id"]: c for c in build.technologies.load_cards()}
VENDORS = {
    v["id"] for v in build.load_vendors(set(CARDS), set())[0]
}


@pytest.mark.parametrize("rec", EQUIPMENT, ids=[r["id"] for r in EQUIPMENT])
def test_record_is_valid(rec):
    jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker()).validate(rec)
    for v in rec["vendors"]:
        assert v in VENDORS, f"{rec['id']}: vendor {v} is not in the directory"
    for t in rec.get("technologies", []):
        assert t in CARDS, f"{rec['id']}: technology {t} has no card"
    for m in rec.get("vendor_models", []):
        assert m["vendor"] in VENDORS, f"{rec['id']}: model line vendor {m['vendor']} is not in the directory"
    for s in rec["sources"]:
        assert s["url"].startswith(("http://", "https://")), f"{rec['id']}: source without http(s) url"


def test_every_record_has_a_spec_with_basis_or_a_gap():
    """A printed parameter carries the basis it was read with; a record whose page printed none
    says so as a gap rather than borrowing a figure (finding F3, 2026-11-26)."""
    for rec in EQUIPMENT:
        if rec["specifications"]:
            for s in rec["specifications"]:
                assert s.get("basis") or s.get("note"), f"{rec['id']}: spec '{s['metric']}' without basis"
        else:
            assert rec.get("gaps"), f"{rec['id']}: no specifications and no gap — the absence is hidden"


def test_specifications_belong_to_the_record_that_read_them():
    """The gate behind finding F3: a Risers record carried 212 specifications, most of them a PV
    module's and a genset's, copied in from other records' pages."""
    index = build.spec_sources.spec_index()
    for rec in EQUIPMENT:
        stray = build.spec_sources.foreign_specs(rec, index)
        assert not stray, (f"{rec['id']}: {len(stray)} specification(s) belong to another record, "
                           f"e.g. '{stray[0].get('metric')}' from {stray[0].get('source_url')}")


def test_the_provenance_gate_catches_a_copied_spec():
    """A copy is a spec another record also carries while this record does not cite the publisher."""
    helper = build.spec_sources
    donor = {"id": "donor", "sources": [{"url": "https://donor.example/page"}],
             "specifications": [{"metric": "Thing", "value": 1, "unit": "kW",
                                 "source_url": "https://donor.example/page", "basis": "read there"}]}
    thief = {"id": "thief", "sources": [{"url": "https://thief.example/page"}],
             "specifications": [dict(donor["specifications"][0])]}
    index = {}
    for rec in (donor, thief):
        for spec in rec["specifications"]:
            index.setdefault(helper.spec_key(spec), set()).add(rec["id"])
    assert helper.foreign_specs(donor, index) == []                        # its own page
    assert helper.foreign_specs(thief, index) == thief["specifications"]   # not its own
    thief["sources"].append({"url": "https://donor.example/page"})         # shared page = shared evidence
    assert helper.foreign_specs(thief, index) == []
    # a chat transcript is never a source, cited or not
    chat = {"id": "chat", "sources": [{"url": "https://chat.mistral.ai/work/x"}],
            "specifications": [{"metric": "List membership", "value": "x", "unit": "n/a",
                                "source_url": "https://chat.mistral.ai/work/x"}]}
    index.setdefault(helper.spec_key(chat["specifications"][0]), set()).add("chat")
    assert helper.foreign_specs(chat, index) == chat["specifications"]


def test_record_ids_unique():
    ids = [r["id"] for r in EQUIPMENT]
    assert len(ids) == len(set(ids)), "duplicate equipment ids"


def test_search_index_carries_equipment():
    import equipment
    import library
    rows = {r["id"]: json.loads(r["record"]) for r in library.connect().execute("SELECT id, record FROM equipment")}
    assert set(rows) == {r["id"] for r in EQUIPMENT}, "library.db equipment table stale or missing"
    hits = library.search("boiler specification", kind="equipment")
    assert hits, "equipment kind search returned nothing"
    first = equipment.summary(EQUIPMENT[0])
    assert first["id"] in {h["ref"] for h in hits} | {h["ref"] for h in library.search(EQUIPMENT[0]["name"], kind="equipment")}, \
        f"{first['id']}: does not surface in equipment search"
