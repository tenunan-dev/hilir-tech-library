"""Offline tests for agent/pg.py: the SQL guard, DSN rewriting and vector formatting. No database is touched."""
import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
import pg  # noqa: E402

GOOD = ["SELECT 1", "  select * from v_gap", "WITH x AS (SELECT 1) SELECT * FROM x"]
BAD = ["", "SELECT 1;", "select 1; select 2", "INSERT INTO t VALUES (1)", "update t set a=1", "delete from t",
       "DROP TABLE t", "select * into newt from t", "select 1 -- comment", "select 1 /* c */", "explain select 1",
       "copy t to stdout", "create table t (a int)"]


@pytest.mark.parametrize("sql", GOOD)
def test_guard_accepts_single_reads(sql):
    pg._check(sql)


@pytest.mark.parametrize("sql", BAD)
def test_guard_rejects_writes_and_other_shapes(sql):
    with pytest.raises(pg.BadSql):
        pg._check(sql)


def test_readonly_dsn_keeps_host_db_and_query():
    out = pg.readonly_dsn("postgresql://u:p@h/db?sslmode=require", user="og_mcp_read", password="xyz")
    assert out == "postgresql://og_mcp_read:xyz@h/db?sslmode=require"


def test_unpooled_dsn_strips_only_the_pooler_marker():
    pooled = pg.readonly_dsn("postgresql://u:p@ep-x-pooler.ap-southeast-1.aws.neon.tech/db?sslmode=require", password="xyz")
    assert pg._unpooled_dsn(pooled) == "postgresql://og_mcp_read:xyz@ep-x.ap-southeast-1.aws.neon.tech/db?sslmode=require"
    direct = pg.readonly_dsn("postgresql://u:p@h/db?sslmode=require", password="xyz")
    assert pg._unpooled_dsn(direct) == direct


def test_vec_text_matches_the_loader_format():
    assert pg._vec_text([0.1, 0.2]) == "[0.1,0.2]"


def test_run_sql_needs_a_dsn(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    with pytest.raises(pg.NotConfigured):
        pg.run_sql("SELECT 1")


def test_hybrid_search_passes_the_kind_filter_into_the_ranking(monkeypatch):
    """`kind` narrows INSIDE hybrid_search_kind. Filtering a global top-k afterwards returned
    nothing for equipment, projects and passages, because the curated kinds outscore them — live
    `search("boiler blowdown", kind="equipment")` came back empty while the SQLite path listed four
    boiler records (2026-11-23)."""
    captured = {}

    class Cur:
        description = []

        def execute(self, sql, params=None):
            captured["sql"], captured["params"] = sql, params

        def fetchall(self):
            return []

    def fake_execute(work):
        work(Cur())
        return []

    monkeypatch.setattr(pg, "_execute", fake_execute)
    assert pg.hybrid_search("boiler blowdown", 3, None, None, None, None, None, "equipment") == []
    assert "hybrid_search_kind" in captured["sql"], "the kind must reach the SQL function"
    assert captured["params"][-1] == "equipment"
    pg.hybrid_search("boiler blowdown", 3)
    assert captured["params"][-1] is None, "an unfiltered search passes no kind"


def test_guard_runs_before_any_connection(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://nowhere/db")
    with pytest.raises(pg.BadSql):
        pg.run_sql("DROP TABLE t")


def test_node_id_and_kind_guards():
    assert pg.NODE_ID.match("technology:ccs-cryogenic")
    assert pg.NODE_ID.match("document:corpus/netl/x.md")
    assert pg.NODE_ID.match("register:CCS/direct-air-capture")
    assert pg.NODE_ID.match("gap:ccs-cryogenic:3")
    assert pg.NODE_ID.match("vendor:wartsila")
    for bad in ("technology:", "no-colon", "SECTOR:CCS", "drop:table;--", "", "technology: DROP TABLE t"):
        assert not pg.NODE_ID.match(bad)
    assert pg.NODE_KIND.match("vendor")
    assert not pg.NODE_KIND.match("vendor; drop")
