"""Durable accounts and activity events for the admin layer (Neon, schema `library`).

Enabled by the USER_STORE_URL environment variable (a least-privilege DSN with
SELECT/INSERT/DELETE on library.account and library.event only — see db/library.sql
and docs/HOSTING.md). When it is unset the library has no roles: every bearer
identity is refused at the gates (fail-closed).

Accounts hold email/name/role only — sign-in happens at hilir Access, so no
password is stored (the schema's hash column stays, empty). All writes are
single autocommit statements so the store is safe behind transaction-mode
poolers. Event recording never raises: analytics must not break a page. SQL
strings stay on one line each; every value goes in as a %s parameter.
"""
import os
import time

import psycopg

DSN_ENV = "USER_STORE_URL"
CACHE_TTL = 30  # seconds an in-process account snapshot lives; role/delete changes lag by this much

_conn = None
_conn_at = 0.0
_accounts = None
_accounts_at = 0.0


def configured() -> bool:
    return bool(os.environ.get(DSN_ENV))


HEADER_DSN = "x-user-store-dsn"


def set_dsn_from_header(value: str | None):
    """Adopt the Worker-supplied DSN for this request (the edge overwrites the header from its
    secret, so containers predating a rotation still see the current value). None = header absent
    (local runs: leave the env alone); "" = the secret is unset (store off); else the DSN."""
    global _conn, _conn_at, _accounts, _accounts_at
    if value is None:
        return
    value = value.strip()
    if value == os.environ.get(DSN_ENV):
        return
    if _conn is not None:
        try:
            _conn.close()
        except Exception:
            pass
    _conn, _conn_at = None, 0.0
    _accounts, _accounts_at = None, 0.0
    if value:
        os.environ[DSN_ENV] = value
    else:
        os.environ.pop(DSN_ENV, None)


def _db():
    global _conn, _conn_at
    if not configured():
        raise RuntimeError("the account store is not configured (USER_STORE_URL is not set)")
    if _conn is None or time.time() - _conn_at > 300:
        if _conn is not None:
            try:
                _conn.close()
            except Exception:
                pass
            _conn = None
        _conn = psycopg.connect(os.environ[DSN_ENV], autocommit=True, connect_timeout=10)
        _conn_at = time.time()
    return _conn


def accounts() -> dict:
    """{email: {email, name, hash, role}} from library.account, cached CACHE_TTL."""
    global _accounts, _accounts_at
    if not configured():
        return {}
    if _accounts is None or time.time() - _accounts_at > CACHE_TTL:
        rows = _db().execute("SELECT email, name, hash, role FROM library.account").fetchall()
        _accounts = {r[0].lower(): {"email": r[0], "name": r[1], "hash": r[2], "role": r[3]} for r in rows}
        _accounts_at = time.time()
    return _accounts


def create_account(email: str, name: str, role: str = "user") -> dict:
    """Insert or replace an account (re-adding an email updates name and role).

    No password: sign-in happens at hilir Access, and the email here must match
    the person's Access account so their bearer token resolves to this row.
    The schema's hash column stays, written empty."""
    if role not in ("admin", "user"):
        raise ValueError("role must be admin or user")
    email = (email or "").strip().lower()
    if not email or "@" not in email:
        raise ValueError("a valid email is required")
    row = {"email": email, "name": name.strip() or email, "hash": "", "role": role}
    _db().execute("INSERT INTO library.account (email, name, hash, role) VALUES (%s, %s, %s, %s) ON CONFLICT (email) DO UPDATE SET name = EXCLUDED.name, hash = '', role = EXCLUDED.role", (row["email"], row["name"], row["hash"], row["role"]))
    _invalidate()
    return {k: row[k] for k in ("email", "name", "role")}


def delete_account(email: str) -> bool:
    cur = _db().execute("DELETE FROM library.account WHERE email = %s", ((email or "").strip().lower(),))
    _invalidate()
    return cur.rowcount > 0


def _invalidate():
    global _accounts
    _accounts = None


def record(kind: str, who: str, detail: str = "", ip: str = ""):
    """One activity event; best effort — failures are swallowed and the connection resets."""
    global _conn
    if not configured():
        return
    try:
        _db().execute("INSERT INTO library.event (kind, who, detail, ip) VALUES (%s, %s, %s, %s)", (kind[:16], who[:120], (detail or "")[:200], (ip or "")[:64]))
    except Exception:
        try:
            _conn.close()
        except Exception:
            pass
        _conn = None  # reconnect on the next attempt instead of failing every write


def analytics() -> dict:
    """Aggregates for the admin page; {} when the store is off."""
    if not configured():
        return {}
    db = _db()
    days = db.execute("SELECT d::date, count(*) FILTER (WHERE kind = 'view'), count(*) FILTER (WHERE kind = 'search') FROM generate_series(now() - interval '6 days', now(), interval '1 day') d JOIN library.event ON library.event.ts >= d AND library.event.ts < d + interval '1 day' GROUP BY d ORDER BY d").fetchall()
    top = db.execute("SELECT detail, count(*) FROM library.event WHERE kind = 'view' AND ts > now() - interval '7 days' AND detail <> '/' GROUP BY detail ORDER BY count(*) DESC LIMIT 10").fetchall()
    totals = db.execute("SELECT count(*) FROM library.event").fetchone()
    return {"days": days, "top": top, "events_total": totals[0]}
