"""Verify a hilir Access token forwarded by the edge (AUTH-REBUILD.md §4.3).

The container stops being a login provider. It never sees a password and holds
no signing key: the edge verifies the browser session and forwards
``Authorization: Bearer <access token>``; this module confirms that token
locally against the issuer's JWKS (EdDSA) and returns the caller's identity.

Roles still come from the account row in the user store — identity from the
token, authorisation from our own data. Nothing here mints or stores anything.

Wiring (next pass — see docs/STATUS.md §5b for the ordered migration):
  * ``_account()`` in agent/web.py                       → ``identify(request)``
  * ``_session()`` / ``_require_session``                 → same
  * ``GET/POST /login``, ``/logout``, login templates      → delete
  * ``agent/users.py`` password/session helpers            → delete
  * ``LIBRARY_API_KEY`` / ``LIBRARY_USERS``                → delete

Environment:
  HILIR_ISSUER    default https://access.hilir.app/api/auth
  HILIR_AUDIENCE  default techlib
"""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Any

import jwt
from jwt import PyJWKClient

ISSUER = os.environ.get("HILIR_ISSUER", "https://access.hilir.app/api/auth").rstrip("/")
AUDIENCE = os.environ.get("HILIR_AUDIENCE", "techlib")
JWKS_URL = f"{ISSUER}/jwks"


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


def verify(token: str) -> dict[str, Any] | None:
    """Claims for a valid token, else None. Never raises, never logs the token."""
    try:
        signing_key = _jwks().get_signing_key_from_jwt(token).key
        claims = jwt.decode(
            token,
            signing_key,
            algorithms=["EdDSA"],
            audience=AUDIENCE,
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


def has_scope(identity: dict[str, Any] | None, scope: str) -> bool:
    return identity is not None and scope in identity.get("scopes", [])
