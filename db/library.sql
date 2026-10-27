-- Library app data: admin-managed accounts and login/activity events.
-- Lives outside schema `og` on purpose: tools/load_postgres.py truncates and
-- reloads `og` on every library reload, and must not wipe accounts or analytics.
-- Idempotent: safe to run again. Run once per database as the owner:
--   psql "$DATABASE_URL" -f db/library.sql
-- The container writes through the least-privilege role created next (see
-- docs/HOSTING.md, "Admin accounts and analytics"): SELECT/INSERT/DELETE on
-- these two tables only.

CREATE SCHEMA IF NOT EXISTS library;

CREATE TABLE IF NOT EXISTS library.account (
  email      text PRIMARY KEY,
  name       text NOT NULL,
  hash       text NOT NULL,
  role       text NOT NULL DEFAULT 'user' CHECK (role IN ('user', 'admin')),
  created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS library.event (
  ts     timestamptz NOT NULL DEFAULT now(),
  kind   text NOT NULL,                -- login_ok | login_fail | view | search
  who    text NOT NULL,                -- account email, or 'key' for the library key
  detail text NOT NULL DEFAULT '',     -- path, search query, or failure detail
  ip     text NOT NULL DEFAULT ''
);

CREATE TABLE IF NOT EXISTS library.api_key (
  id         integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  key_hash   text NOT NULL UNIQUE,     -- sha256 hex of the raw key; the raw key is never stored
  prefix     text NOT NULL,            -- display prefix, e.g. hlt_ab12
  email      text NOT NULL REFERENCES library.account (email) ON DELETE CASCADE,
  label      text NOT NULL DEFAULT '',
  created_at timestamptz NOT NULL DEFAULT now(),
  last_used  timestamptz
);

CREATE INDEX IF NOT EXISTS library_event_ts_idx ON library.event (ts DESC);
CREATE INDEX IF NOT EXISTS library_event_kind_ts_idx ON library.event (kind, ts DESC);
