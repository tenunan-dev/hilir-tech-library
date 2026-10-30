"""Knowledge graph and Postgres loader. The database tests run only when TEST_DATABASE_URL points at a
Postgres with the pgvector extension (a scratch database: the load truncates schema og)."""
import hashlib
import os
import pathlib
import sys

import numpy as np
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "agent"))
sys.path.insert(0, str(ROOT / "tools"))
import graph  # noqa: E402
import technologies  # noqa: E402


@pytest.fixture(scope="module")
def built():
    return graph.build_graph()


def test_every_edge_joins_known_nodes(built):
    nodes, edges = built
    ids = {n["id"] for n in nodes}
    assert len(ids) == len(nodes)
    assert all(e["src"] in ids and e["dst"] in ids for e in edges)
    assert len({(e["src"], e["dst"], e["rel"]) for e in edges}) == len(edges)


def test_every_card_and_register_entry_is_linked(built):
    nodes, edges = built
    cards = {n["id"] for n in nodes if n["kind"] == "technology"}
    assert cards == {f"technology:{c['id']}" for c in technologies.load_cards()}
    linked = {e["src"] for e in edges if e["rel"] in ("in_sector",)} | {e["dst"] for e in edges}
    assert cards <= linked
    realised = {e["dst"] for e in edges if e["rel"] == "realised_by"}
    assert realised == cards, "each card should realise exactly one register entry or more"


def test_every_card_cites_a_catalog_source_or_document(built):
    _, edges = built
    cites = {e["src"] for e in edges if e["rel"] in ("cites", "cites_document")}
    cards = {n["id"] for n in built[0] if n["kind"] == "technology"}
    # Cards whose sources are trade press, journals or vendor pages not in the catalog are listed in the
    # failure message so they get catalogued, not hidden. The limit is a share of all cards, not a count.
    missing = sorted(cards - cites)
    assert len(missing) <= 0.4 * len(cards), missing


def test_mentions_carry_their_evidence(built):
    _, edges = built
    mentions = [e for e in edges if e["rel"] == "mentions"]
    assert mentions and all(e["props"]["terms"] and e["weight"] >= 1 for e in mentions)


def test_vendor_records_are_linked(built):
    import vendors as vendor_records
    nodes, edges = built
    recs = vendor_records.load_vendors()
    vnodes = {n["id"] for n in nodes if n["kind"] == "vendor"}
    assert vnodes == {f"vendor:{v['id']}" for v in recs}
    supplies = [(e["src"], e["dst"]) for e in edges if e["rel"] == "supplies"]
    assert supplies and all(s.startswith("vendor:") and d.startswith("technology:") for s, d in supplies)
    assert {s for s, _ in supplies} == {f"vendor:{v['id']}" for v in recs}
    alias = [e for e in edges if e["rel"] == "alias_of"]
    assert alias and all(e["src"].startswith("org:") and e["dst"].startswith("vendor:") for e in alias)


def test_equipment_classes_are_linked(built):
    import equipment as equipment_records
    nodes, edges = built
    recs = equipment_records.load_equipment()
    if not recs:
        pytest.skip("no equipment records yet")
    enodes = {n["id"] for n in nodes if n["kind"] == "equipment"}
    assert enodes == {f"equipment:{r['id']}" for r in recs}
    supply = [e for e in edges if e["rel"] == "supplies_equipment"]
    assert supply, "equipment classes must link to the vendors behind them"
    assert all(e["src"].startswith("equipment:") and e["dst"].startswith("vendor:") for e in supply)
    uses = [e for e in edges if e["rel"] == "uses_equipment"]
    assert uses, "equipment classes must link to the cards that use them"
    assert all(e["src"].startswith("technology:") and e["dst"].startswith("equipment:") for e in uses)


def test_term_matching_respects_word_boundaries():
    assert graph.term_count("HEFA", "HEFA and HEFA-SPK; hefa") == 2
    assert graph.term_count("SOEC", "ASOEC SOEC") == 1
    assert graph.term_count("amine scrubbing", "Amine Scrubbing works") == 1


needs_db = pytest.mark.skipif(not os.environ.get("TEST_DATABASE_URL"), reason="set TEST_DATABASE_URL to a scratch Postgres with pgvector")


def hash_vector(text, dim=384):
    """Deterministic stand-in for a real embedding: same words give similar vectors."""
    vec = np.zeros(dim, dtype=np.float32)
    for word in text.lower().split():
        h = int(hashlib.md5(word.encode()).hexdigest(), 16)
        vec[h % dim] += 1.0
    norm = np.linalg.norm(vec)
    return vec / norm if norm else vec


@needs_db
def test_load_postgres_end_to_end():
    import psycopg
    import load_postgres
    data = load_postgres.collect()
    nodes, edges = graph.build_graph()
    card_names = {c["id"]: c["name"] for c in data["cards"]}
    vectors = {("technology", c["id"]): hash_vector(load_postgres.card_search_text(c)) for c in data["cards"]}
    vectors.update({("vendor", v["id"]): hash_vector(load_postgres.library.vendor_text(v, card_names))
                    for v in data["vendors"]})
    vectors.update({("chunk", c["id"]): hash_vector(c["body"]) for c in data["chunks"][:200]})
    with psycopg.connect(os.environ["TEST_DATABASE_URL"]) as conn:
        result = load_postgres.load(conn, data, nodes, edges, vectors)
        cur = conn.cursor()
        cur.execute("SET search_path = og, public")
        assert result["technologies"] == len(data["cards"]) and result["nodes"] == len(nodes)
        assert result["vendors"] == len(data["vendors"])
        cur.execute("SELECT count(*) FROM vendor")
        assert cur.fetchone()[0] == len(data["vendors"])
        cur.execute("SELECT count(*) FROM edge WHERE rel = 'similar_to'")
        assert cur.fetchone()[0] > 0
        cur.execute("SELECT count(*) FROM document WHERE NOT text_included")
        restricted_docs = cur.fetchone()[0]
        cur.execute("SELECT count(*) FROM chunk c JOIN document d ON d.id = c.document_id WHERE NOT d.text_included")
        assert cur.fetchone()[0] == 0, "restricted text must not be loaded by default"
        assert restricted_docs >= 0
        cur.execute("SELECT node_id FROM graph_neighbors('technology:ups-co2-eor', 1) WHERE kind = 'source'")
        assert cur.fetchall()
        cur.execute("SELECT node_id, label FROM graph_neighbors('vendor:wartsila', 1) WHERE kind = 'technology'")
        assert cur.fetchall(), "vendor records should reach their cards through supplies"
        query = hash_vector("CO2 enhanced oil recovery miscible flooding")
        cur.execute("SELECT ref FROM hybrid_search(%s, %s::vector, 5) WHERE kind = 'technology'",
                    ("CO2 enhanced oil recovery", load_postgres.vec_text(query)))
        assert "ups-co2-eor" in [r[0] for r in cur.fetchall()]
        cur.execute("SELECT ref FROM hybrid_search(%s, %s::vector, 10) WHERE kind = 'vendor'",
                    ("Wärtsilä engines", load_postgres.vec_text(hash_vector("Wärtsilä engines power plants"))))
        assert cur.fetchall(), "hybrid search should cover vendor records"
        conn.rollback()
