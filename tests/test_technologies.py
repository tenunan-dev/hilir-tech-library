"""Technology cards: every card is valid, diagrams are well formed, and tools return them."""
import json
import pathlib
import sys

import jsonschema
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "agent"))
import library  # noqa: E402
import technologies  # noqa: E402

CARDS = technologies.load_cards()
SCHEMA = json.loads((ROOT / "schema" / "technology.schema.json").read_text(encoding="utf-8"))


@pytest.mark.parametrize("card", CARDS, ids=[c["id"] for c in CARDS])
def test_card_is_valid_and_sourced(card):
    jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker()).validate(card)
    assert technologies.check(card) == []
    for fig in card.get("costs", []) + card.get("performance", []):
        assert fig["source"]["url"].startswith("http") and fig["basis"]
        if "USD" in fig["unit"]:
            assert fig.get("year") or "not stated" in fig["basis"], f"{card['id']}: cost without dollar year"


def test_mermaid_has_every_step_and_edge():
    card = {"process_steps": [{"id": "A", "name": "Feed"}, {"id": "B", "name": "Split", "to": ["C", "D"], "streams": {"C": "gas"}},
                              {"id": "C", "name": "Out 1", "to": []}, {"id": "D", "name": 'Out "2"', "to": []}]}
    text = technologies.mermaid(card)
    assert text.startswith("flowchart LR") and "A --> B" in text and "B -->|gas| C" in text and "B --> D" in text
    assert '"' not in text.split('D["')[1].split('"]')[0]


def test_check_flags_dangling_links():
    card = {"process_steps": [{"id": "A", "name": "x", "to": ["Z"]}, {"id": "B", "name": "y"}]}
    assert technologies.check(card) == ["step link to unknown step 'Z'"]


def test_compare_orders_commercial_first():
    rows = technologies.compare(CARDS, sector="CCS")
    order = [technologies.MATURITY_ORDER[r["maturity"]] for r in rows]
    assert rows and order == sorted(order)


def test_library_tools_return_cards(tmp_path):
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (tmp_path / "catalog").symlink_to(ROOT / "catalog")
    library.build(tmp_path / "lib.db", corpus)
    db = library.connect(tmp_path / "lib.db")
    hits = library.search("calcium looping carbonator", kind="technology", db=db)
    assert hits and hits[0]["ref"] == "ccs-calcium-looping"
    card = library.get_technology("ccs-calcium-looping", db)
    assert card["block_diagram_mermaid"].startswith("flowchart LR")
    assert library.compare_technologies("CCS", maturity="commercial", db=db)
    assert library.search("calcium looping", kind="technology", sector="H2", db=db) == []
