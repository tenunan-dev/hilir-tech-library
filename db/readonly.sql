-- Read-only database access for the MCP server and the web UI. Applied by the maintainer with
--   python tools/load_postgres.py --grant-readonly
-- against the owner DSN; that command also sets the role's password and its GRANT CONNECT ON DATABASE
-- (a bound parameter and a sql.Identifier there), so no secret appears in this file or the repository.
-- The role is read-only twice over: by the GRANT SELECT statements below (including default privileges
-- for tables created later) and by its role settings, which force read-only transactions with a 15s
-- statement timeout. Idempotent: safe to run again.

DO $$ BEGIN IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'og_mcp_read') THEN CREATE ROLE og_mcp_read LOGIN; END IF; END $$;
GRANT USAGE ON SCHEMA og TO og_mcp_read;
GRANT SELECT ON ALL TABLES IN SCHEMA og TO og_mcp_read;
ALTER DEFAULT PRIVILEGES IN SCHEMA og GRANT SELECT ON TABLES TO og_mcp_read;
ALTER ROLE og_mcp_read SET default_transaction_read_only = on;
ALTER ROLE og_mcp_read SET statement_timeout = '15s';
