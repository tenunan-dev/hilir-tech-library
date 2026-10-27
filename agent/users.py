"""Named accounts for the web interface: email + password, stored outside the repo.

Accounts live in the LIBRARY_USERS environment variable (a wrangler secret on the hosted
server), as `email|name|scrypt-hash` entries separated by ";" or newlines, e.g.

    LIBRARY_USERS='alice@example.com|Alice|$scrypt$16384$8$1$<salt-hex>$<key-hex>;...'

Password hashes are salted scrypt (hashlib, no new dependency). Create entries with:

    python agent/users.py entry alice@example.com Alice   # prompts for the password, prints the entry

then set them as a secret: `wrangler secret put LIBRARY_USERS` (hosted) or export the variable
locally. The API key keeps working for agents and for the owner's own sign-in; accounts are an
additional, per-person way into the web UI. The variable is read on every check, so updates
apply without touching the code.
"""
import base64
import getpass
import hashlib
import hmac
import json
import os
import sys
import time

USERS_ENV = "LIBRARY_USERS"
SESSION_TTL = 30 * 86400  # match the cookie max_age on the login route


def hash_password(password: str) -> str:
    """Salted scrypt in a self-describing scrypt$N$r$p$salt$key string."""
    salt = os.urandom(16)
    dk = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32,
                        maxmem=64 * 1024 * 1024)
    return f"scrypt$16384$8$1${salt.hex()}${dk.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        algo, n, r, p, salt_hex, key_hex = stored.split("$")
        if algo != "scrypt":
            return False
        dk = hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt_hex), n=int(n), r=int(r),
                            p=int(p), dklen=len(key_hex) // 2, maxmem=64 * 1024 * 1024)
        return hmac.compare_digest(dk.hex(), key_hex)
    except (ValueError, TypeError):
        return False


def load_users(env=None) -> dict:
    """{email: {email, name, hash, role}} from LIBRARY_USERS; empty when unset or malformed.

    Entries are `email|name|scrypt-hash` with an optional trailing `|admin` (default role: user).
    """
    users = {}
    for entry in (env if env is not None else os.environ.get(USERS_ENV, "")).split(";"):
        parts = [p.strip() for p in entry.strip().split("|")]
        if len(parts) >= 3 and parts[0] and parts[2]:
            role = parts[3] if len(parts) >= 4 and parts[3] in ("admin", "user") else "user"
            users[parts[0].lower()] = {"email": parts[0], "name": parts[1] or parts[0],
                                       "hash": parts[2], "role": role}
    return users


def check_login(email: str, password: str, env=None) -> dict | None:
    """The account for email if the password verifies, else None (constant-time on the hash)."""
    user = load_users(env).get((email or "").strip().lower())
    if user and verify_password(password or "", user["hash"]):
        return user
    return None


def session_token(email: str, secret: str, ttl: int = SESSION_TTL) -> str:
    """Signed, stateless per-user session: v2|payload|signature (HMAC-SHA256 over the payload)."""
    payload = base64.urlsafe_b64encode(
        json.dumps({"u": email, "exp": int(time.time()) + ttl}).encode()).decode().rstrip("=")
    sig = hmac.new(secret.encode(), ("v2|" + payload).encode(), hashlib.sha256).hexdigest()
    return f"v2|{payload}|{sig}"


def session_email(token: str, secret: str) -> str | None:
    """The email a valid, unexpired v2 session token belongs to, else None."""
    try:
        kind, payload, sig = token.split("|")
        if kind != "v2":
            return None
        good = hmac.new(secret.encode(), (kind + "|" + payload).encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(sig, good):
            return None
        data = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))
        if int(data.get("exp", 0)) < time.time():
            return None
        return str(data.get("u")) or None
    except (ValueError, TypeError):
        return None


def main(argv=None):
    argv = argv or sys.argv[1:]
    if argv[:1] == ["hash"]:
        password = argv[1] if len(argv) > 1 else getpass.getpass("password: ")
        print(hash_password(password))
        return 0
    if argv[:1] == ["entry"]:
        if len(argv) < 2:
            print("usage: python agent/users.py entry <email> [name] [admin|user]", file=sys.stderr)
            return 2
        email = argv[1]
        name = argv[2] if len(argv) > 2 and not argv[2].startswith("_") else email
        role = argv[3] if len(argv) > 3 else ("admin" if len(argv) > 2 and argv[2] in ("admin", "user") else "user")
        if role not in ("admin", "user"):
            print("role must be admin or user", file=sys.stderr)
            return 2
        password = getpass.getpass(f"password for {email}: ")
        again = getpass.getpass("repeat: ")
        if password != again:
            print("passwords do not match", file=sys.stderr)
            return 2
        print(f"{email}|{name}|{hash_password(password)}|{role}")
        return 0
    if argv[:1] == ["verify"]:
        # offline check that an entry works: users.py verify <email> <entry|password-prompt>
        users = load_users(sys.stdin.read() if not sys.stdin.isatty() else "")
        print("ok" if check_login(argv[1], getpass.getpass("password: "),
                                 ";".join(f"{e}|{u['name']}|{u['hash']}" for e, u in users.items())) else "FAIL")
        return 0
    print("usage: python agent/users.py hash [password] | entry <email> [name]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
