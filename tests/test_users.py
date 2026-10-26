"""Offline tests for agent/users.py: hashing, the LIBRARY_USERS store and signed session tokens."""
import pathlib
import sys
import time

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "agent"))
import users  # noqa: E402

PASSWORD = "correct horse battery staple"


def test_hash_and_verify_roundtrip():
    stored = users.hash_password(PASSWORD)
    assert stored.startswith("scrypt$16384$8$1$") and users.verify_password(PASSWORD, stored)
    assert not users.verify_password("wrong", stored)
    assert not users.verify_password(PASSWORD, "garbage")
    assert not users.verify_password(PASSWORD, "md5$1$1$abcd$abcd")


def test_hash_is_salted():
    assert users.hash_password(PASSWORD) != users.hash_password(PASSWORD)


def test_load_users_parses_entries():
    entry = f"alice@example.com|Alice Chen|{users.hash_password(PASSWORD)}"
    env = f"{entry} ; bob@example.com||{users.hash_password('another')}  ;  not-an-entry"
    parsed = users.load_users(env)
    assert set(parsed) == {"alice@example.com", "bob@example.com"}
    assert parsed["alice@example.com"]["name"] == "Alice Chen"
    assert parsed["bob@example.com"]["name"] == "bob@example.com"
    assert users.load_users("") == {}


def test_check_login_matches_case_insensitively(monkeypatch):
    entry = f"alice@example.com|Alice|{users.hash_password(PASSWORD)}"
    monkeypatch.setenv("LIBRARY_USERS", entry)
    assert users.check_login("Alice@Example.com ", PASSWORD)["email"] == "alice@example.com"
    assert users.check_login("alice@example.com", "wrong") is None
    assert users.check_login("nobody@example.com", PASSWORD) is None


def test_session_token_roundtrip_and_tamper():
    token = users.session_token("alice@example.com", "k" * 32)
    assert users.session_email(token, "k" * 32) == "alice@example.com"
    assert users.session_email(token, "x" * 32) is None  # wrong secret
    kind, payload, sig = token.split("|")
    other = users.session_token("bob@example.com", "k" * 32)
    assert users.session_email(kind + "|" + other.split("|")[1] + "|" + sig, "k" * 32) is None  # mixed payload
    expired = users.session_token("alice@example.com", "k" * 32, ttl=-10)
    assert users.session_email(expired, "k" * 32) is None
    assert users.session_email("v1|abc|def", "k" * 32) is None
    assert users.session_email("not-a-token", "k" * 32) is None


def test_main_entry_prints_a_working_record(monkeypatch):
    import io
    prompts = iter([PASSWORD, PASSWORD])
    monkeypatch.setattr(users.getpass, "getpass", lambda *_: next(prompts))
    captured = io.StringIO()
    monkeypatch.setattr(sys, "stdout", captured)
    assert users.main(["entry", "carol@example.com", "Carol"]) == 0
    entry = captured.getvalue().strip()
    assert entry.startswith("carol@example.com|Carol|scrypt$")
    assert users.verify_password(PASSWORD, entry.split("|")[2])
