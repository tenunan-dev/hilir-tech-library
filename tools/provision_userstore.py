"""One-off Neon provisioning: schema `library` + least-privilege role library_app.

Run from the repo root on the Mac (reads owner DSNs from .env.local, never prints secrets):
    .venv/bin/python tools/provision_userstore.py
Idempotent: re-running re-applies the DDL, rotates the role password, and rewrites
~/.config/hilir-tech-library/user-store.url (mode 600).

The DDL below mirrors db/library.sql statement-for-statement (the drift check fails
loudly if the two part ways). db/library.sql remains the source of truth for
psql-based setups.
"""
import os
import pathlib
import secrets
import sys
import urllib.parse

import psycopg

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = pathlib.Path.home() / ".config" / "hilir-tech-library"


def dsn_env():
    env = {}
    for line in (ROOT / ".env.local").read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            key, value = line.split("=", 1)
            env[key.strip()] = value.strip().strip('"').strip("'")
    return env


def main():
    env = dsn_env()
    owner = env.get("DATABASE_URL_UNPOOLED")
    pooled = env.get("DATABASE_URL")
    if not owner or not pooled:
        sys.exit("DATABASE_URL / DATABASE_URL_UNPOOLED missing in .env.local")

    # drift check: every statement of db/library.sql appears verbatim in this file
    parts = [line.split("--", 1)[0] for line in (ROOT / "db" / "library.sql").read_text().splitlines()]
    file_sql = "".join("".join(parts).split())
    ddl = [
        "CREATE SCHEMA IF NOT EXISTS library",
        "CREATE TABLE IF NOT EXISTS library.account ( email text PRIMARY KEY, name text NOT NULL, hash text NOT NULL, role text NOT NULL DEFAULT 'user' CHECK (role IN ('user', 'admin')), created_at timestamptz NOT NULL DEFAULT now())",
        "CREATE TABLE IF NOT EXISTS library.event ( ts timestamptz NOT NULL DEFAULT now(), kind text NOT NULL, who text NOT NULL, detail text NOT NULL DEFAULT '', ip text NOT NULL DEFAULT '')",
        "CREATE INDEX IF NOT EXISTS library_event_ts_idx ON library.event (ts DESC)",
        "CREATE INDEX IF NOT EXISTS library_event_kind_ts_idx ON library.event (kind, ts DESC)",
    ]
    for compact in ddl:
        if "".join(compact.split()) not in file_sql:
            sys.exit(f"DDL drifted from db/library.sql: {compact[:60]}…")

    with psycopg.connect(owner, autocommit=True) as conn:
        conn.execute("CREATE SCHEMA IF NOT EXISTS library")
        conn.execute("CREATE TABLE IF NOT EXISTS library.account ( email text PRIMARY KEY, name text NOT NULL, hash text NOT NULL, role text NOT NULL DEFAULT 'user' CHECK (role IN ('user', 'admin')), created_at timestamptz NOT NULL DEFAULT now())")
        conn.execute("CREATE TABLE IF NOT EXISTS library.event ( ts timestamptz NOT NULL DEFAULT now(), kind text NOT NULL, who text NOT NULL, detail text NOT NULL DEFAULT '', ip text NOT NULL DEFAULT '')")
        conn.execute("CREATE INDEX IF NOT EXISTS library_event_ts_idx ON library.event (ts DESC)")
        conn.execute("CREATE INDEX IF NOT EXISTS library_event_kind_ts_idx ON library.event (kind, ts DESC)")

        # least-privilege role (create or rotate its password). Utility statements cannot
        # use server-side binds, so the password goes through a client-side cursor, which
        # quotes it safely into the static statement.
        password = secrets.token_urlsafe(24)
        cur = psycopg.ClientCursor(conn)
        exists = cur.execute("SELECT 1 FROM pg_roles WHERE rolname = 'library_app'").fetchone()
        if exists:
            cur.execute("ALTER ROLE library_app WITH LOGIN PASSWORD %s", (password,))
        else:
            cur.execute("CREATE ROLE library_app WITH LOGIN PASSWORD %s", (password,))
        conn.execute("GRANT USAGE ON SCHEMA library TO library_app")
        conn.execute("GRANT SELECT, INSERT, DELETE ON ALL TABLES IN SCHEMA library TO library_app")

    # the app DSN: the role on the pooled endpoint (same host the read-only role uses)
    parts = urllib.parse.urlsplit(pooled)
    app_dsn = f"postgresql://library_app:{password}@{parts.hostname}:{parts.port or 5432}{parts.path}"

    # verify the role can do exactly its job — and nothing more
    with psycopg.connect(app_dsn, autocommit=True) as conn:
        conn.execute("INSERT INTO library.event (kind, who, detail) VALUES ('login_ok', 'provision-check', '')")
        count = conn.execute("SELECT count(*) FROM library.event WHERE who = 'provision-check'").fetchone()[0]
        conn.execute("DELETE FROM library.event WHERE who = 'provision-check'")
        assert count == 1
        try:
            conn.execute("SELECT 1 FROM og.source LIMIT 1")
            sys.exit("role can read og.source — grants are too wide")
        except psycopg.errors.InsufficientPrivilege:
            pass

    CONFIG.mkdir(mode=0o700, parents=True, exist_ok=True)
    out = CONFIG / "user-store.url"
    out.write_text(app_dsn + "\n")
    os.chmod(out, 0o600)
    print(f"provisioned: schema library + role library_app; DSN written to {out}")


if __name__ == "__main__":
    main()
