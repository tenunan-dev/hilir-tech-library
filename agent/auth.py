"""Verify a hilir Access token forwarded by the edge (AUTH-REBUILD.md §4.3).

The container stops being a login provider. It never sees a password and holds
no signing key: the edge verifies the browser session and forwards
``Authorization: Bearer <access token>``; this module confirms that token
locally against the issuer's JWKS (EdDSA) and returns the caller's identity.

Roles still come from the account row in the user store — identity from the
token, authorisation from our own data. Nothing here mints or stores anything.
The container's own login/users/key machinery was deleted in step 3
(2026-11-05, AUTH-REBUILD §4.3): this bearer is the only credential.

Environment:
  HILIR_ISSUER    default https://access.hilir.app/api/auth
  HILIR_AUDIENCE  comma-separated registered RFC 8707 resource origins whose
                  tokens this service accepts. Default covers the UI origin
                  (the edge forwards the browser session's token) and this API
                  host's own origin (direct MCP clients). NEVER a client name.
"""

from __future__ import annotations

import base64
import hashlib
import os
import time
from functools import lru_cache
from typing import Any
from urllib.parse import urlparse

import jwt
import requests
from jwt import PyJWKClient

ISSUER = os.environ.get("HILIR_ISSUER", "https://access.hilir.app/api/auth").rstrip("/")
# Comma-separated resource origins; PyJWT accepts an iterable audience and
# requires the token's aud to match ONE of them (RFC 8707).
AUDIENCES = [
    a.strip()
    for a in os.environ.get(
        "HILIR_AUDIENCE",
        "https://techlib.hilir.app,https://techlib-api.hilir.app",
    ).split(",")
    if a.strip()
]
JWKS_URL = f"{ISSUER}/jwks"
USERINFO_URL = os.environ.get("HILIR_USERINFO_URL", f"{ISSUER}/oauth2/userinfo")
_UA = "hilir-techlib/1.0"

# Identity cache: the userinfo endpoint is the standard source for the email
# scope, but it must not be called on every request. Keyed by token hash.
_IDENTITY_CACHE: dict[str, tuple[float, dict[str, Any]]] = {}
_IDENTITY_TTL_S = 60.0
_IDENTITY_CACHE_MAX = 1024


@lru_cache(maxsize=1)
def _jwks() -> PyJWKClient:
    """One cached JWKS client per process; PyJWT refetches on an unknown kid.

    A plain User-Agent is required: Cloudflare's bot protection on hilir.app
    rejects the default ``Python-urllib`` UA with 403, which used to make every
    local verification fail and bounced sign-ins into a redirect loop
    (2026-11-04). ``headers`` is a documented PyJWKClient parameter.
    """
    return PyJWKClient(
        JWKS_URL,
        cache_keys=True,
        lifespan=300,
        headers={"User-Agent": "hilir-techlib/1.0"},
    )


def bearer(request: Any) -> str | None:
    """The token the edge attached, or None. Header only — never a cookie."""
    raw = request.headers.get("authorization", "")
    if not raw.lower().startswith("bearer "):
        return None
    token = raw[7:].strip()
    return token or None


def _looks_like_jwt(token: str) -> bool:
    """An access token is a three-segment JWT; a person's key is opaque."""
    return token.count(".") == 2


# --- person-key verification (RFC 7662 introspection) -----------------------

INTROSPECT_URL = os.environ.get(
    "HILIR_INTROSPECT_URL", f"{ISSUER.rsplit('/api/auth', 1)[0]}/api/v2-introspect"
)
HILIR_CLIENT_ID = os.environ.get("HILIR_CLIENT_ID", "").strip()
HILIR_CLIENT_SECRET = os.environ.get("HILIR_CLIENT_SECRET", "").strip()

_KEY_CACHE: dict[str, tuple[float, dict[str, Any] | None]] = {}
_KEY_CACHE_TTL_S = 60.0
_KEY_CACHE_MAX = 1024


def _form_encode(value: str) -> str:
    """RFC 6749 §2.3.1 / Appendix B encoding for one half of a Basic credential."""
    out = []
    for ch in value:
        if ch == " ":
            out.append("+")
        elif ch.isalnum() or ch in "-._~":
            out.append(ch)
        else:
            out.append(f"%{ord(ch):02X}")
    return "".join(out)


def _introspect_key(token: str) -> dict[str, Any] | None:
    """Verify a person's opaque key at Access (RFC 7662) with this app's own
    client credentials. Cached briefly by token hash; an unreachable verifier
    or a non-200 is fail-closed (None), never a fabricated identity."""
    if not HILIR_CLIENT_ID or not HILIR_CLIENT_SECRET:
        return None
    cache_key = hashlib.sha256(token.encode()).hexdigest()
    now = time.time()
    cached = _KEY_CACHE.get(cache_key)
    if cached and cached[0] > now:
        return cached[1]

    result: dict[str, Any] | None = None
    try:
        response = requests.post(
            INTROSPECT_URL,
            data={"token": token},
            headers={
                "authorization": "Basic "
                + base64.b64encode(
                    f"{_form_encode(HILIR_CLIENT_ID)}:{_form_encode(HILIR_CLIENT_SECRET)}".encode()
                ).decode(),
                "content-type": "application/x-www-form-urlencoded",
                "user-agent": _UA,
            },
            timeout=5,
        )
    except Exception:  # noqa: BLE001 — verifier unreachable = fail closed
        return None
    if response.status_code == 200:
        try:
            body = response.json()
        except ValueError:
            body = {}
        if isinstance(body, dict) and body.get("active") is True:
            scopes = str(body.get("scope") or "").split()
            result = {
                "email": None,
                "sub": body.get("sub") or "agent-key",
                "scopes": scopes,
                "claims": {"sub": body.get("sub"), "scope": scopes},
            }

    if len(_KEY_CACHE) > _KEY_CACHE_MAX:
        _KEY_CACHE.clear()
    _KEY_CACHE[cache_key] = (now + _KEY_CACHE_TTL_S, result)
    return result


def verify(token: str) -> dict[str, Any] | None:
    """Claims for a valid token or key, else None. Never raises, never logs
    the token. Two credentials, one identity shape:
    - an access token (JWT): verified locally against the issuer's JWKS;
    - a person's opaque key: introspected at Access (RFC 7662), because an
      opaque record cannot be verified offline. Roles still come from the
      account row for token callers; a key caller is the owning account."""
    if not _looks_like_jwt(token):
        return _introspect_key(token)
    try:
        signing_key = _jwks().get_signing_key_from_jwt(token).key
        claims = jwt.decode(
            token,
            signing_key,
            algorithms=["EdDSA"],
            audience=AUDIENCES,
            issuer=ISSUER,
            options={"require": ["exp", "iss", "aud", "sub"]},
        )
    except Exception:  # expired, wrong audience/issuer, bad signature, malformed
        return None
    return {
        "email": claims.get("email"),
        "sub": claims.get("sub"),
        "scopes": (claims.get("scope") or "").split(),
        "claims": claims,
    }


def identify(request: Any) -> dict[str, Any] | None:
    """Resolve the caller from the forwarded bearer token."""
    token = bearer(request)
    return verify(token) if token else None


def identity(token: str) -> dict[str, Any] | None:
    """The caller's identity from the provider's userinfo endpoint.

    This is the standard OIDC source for the `email` scope: access and ID
    tokens carry `aud`/`scope` but not the user's profile. Cached per token so
    the endpoint is called once per token per minute, not per request.

    The request goes to a fixed, configured URL (never a caller-supplied one);
    a malformed or non-HTTPS URL simply disables identity resolution.
    """
    parsed = urlparse(USERINFO_URL)
    if parsed.scheme != "https" or not parsed.hostname:
        return None

    cache_key = hashlib.sha256(token.encode()).hexdigest()
    now = time.time()
    cached = _IDENTITY_CACHE.get(cache_key)
    if cached and cached[0] > now:
        return cached[1]

    try:
        response = requests.get(
            USERINFO_URL,
            headers={
                "authorization": f"Bearer {token}",
                "accept": "application/json",
                "user-agent": _UA,
            },
            timeout=10,
        )
    except Exception:  # noqa: BLE001 — network failure = no identity
        return None
    if response.status_code != 200:
        return None
    try:
        data = response.json()
    except ValueError:
        return None
    if not isinstance(data, dict):
        return None
    if len(_IDENTITY_CACHE) > _IDENTITY_CACHE_MAX:
        _IDENTITY_CACHE.clear()
    _IDENTITY_CACHE[cache_key] = (now + _IDENTITY_TTL_S, data)
    return data


def has_scope(identity: dict[str, Any] | None, scope: str) -> bool:
    return identity is not None and scope in identity.get("scopes", [])
