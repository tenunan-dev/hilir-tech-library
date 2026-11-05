# Authentication — how techlib signs people in (READ BEFORE TOUCHING AUTH)

Status: **live** since 2026-11-05. Estate authority:
`hilir-access/docs/STATUS.md` (FINAL STATE section). This file is the
self-contained version for anyone working in *this* repo.

## The one-sentence model

Browsers sign in at **https://access.hilir.app**; techlib is an OIDC client.
Every request that reaches the containers carries
`Authorization: Bearer <access token>`, and **each hop verifies that token
locally** (EdDSA via the issuer's JWKS). There is no library key, no container
login form, no password anywhere in this repo, and no per-request call to Access.

```
browser ──/login──▶ techlib-edge ──303──▶ https://access.hilir.app/api/auth/oauth2/authorize
                       │                        (PKCE + state + resource=https://techlib.hilir.app)
                       │◀── /auth/callback?code=… ──┘
                       │  exchanges the code (client_secret_basic) → access/refresh/id_token cookies
                       ▼
              verify locally (jose, EdDSA, iss + aud) ──▶ Authorization: Bearer … ──▶ container
                                                                                      │
                                                                   agent/auth.py verifies again
                                                                   + userinfo email + Neon row = role
```

## Where the code lives

| File | Job |
|---|---|
| `deploy/edge/src/index.ts` | one Worker, both hostnames; dispatches UI vs API handlers |
| `deploy/frontend/src/index.ts` | UI: `/login`, `/auth/callback`, `/logout`, token resolve/refresh, forwards the bearer |
| `deploy/backend/src/index.ts` | API/MCP gate: verifies the bearer (jose) before anything crosses the tunnel |
| `agent/auth.py` | container-side verifier (`PyJWT` + `PyJWKClient`, EdDSA), userinfo identity cache |
| `agent/web.py` | `_account()` — bearer → email (userinfo) → account row → role; all pages gated |
| `agent/server.py` | `RequireHilirToken` ASGI gate for `/mcp` and `/api/*` |

## Configuration (values never in git)

| Key | Where | Meaning |
|---|---|---|
| `HILIR_ISSUER` | edge var + container env | `https://access.hilir.app/api/auth` |
| `HILIR_CLIENT_ID` | edge var | opaque id (`YBUSRWpUyOKWcnrxJPITRYptIBsqtYFL`) — **never** the name `techlib` |
| `HILIR_CLIENT_SECRET` | edge **secret** | confidential client; sent as `Authorization: Basic` |
| `APP_ORIGIN` | edge var | `https://techlib.hilir.app` — also the token's `aud` |
| `AUDIENCE` | API worker var | `https://techlib.hilir.app` (a **resource URL**, not the client id) |
| `REQUIRED_SCOPE` | API worker var | `catalog:read` |
| `USER_STORE_URL` | edge var → header | Neon DSN; roles live in `library.account` |
| `HILIR_AUDIENCE` | container env | `https://techlib.hilir.app` |

## Verify after any change (copy-paste)

```bash
curl -s -o /dev/null -w "%{http_code} %{redirect_url}\n" https://techlib.hilir.app/            # 303 → /login
curl -s -o /dev/null -w "%{http_code}\n"                 https://techlib.hilir.app/health       # 200
curl -s -o /dev/null -w "%{http_code}\n"                 https://techlib.hilir.app/api/stats     # 401
curl -s -o /dev/null -w "%{http_code}\n"                 https://techlib-api.hilir.app/mcp       # 401
curl -s -o /dev/null -w "%{redirect_url}\n"              https://techlib.hilir.app/login         # authorize URL on access.hilir.app, with resource=
curl -s -o /dev/null -w "%{redirect_url}\n"              https://techlib.hilir.app/logout        # end-session URL with client_id + post_logout_redirect_uri
```

Then in a browser: sign in → open a page → Sign out → you must land back
signed out with no error page.

## Who may do what

Authority: `hilir-access/docs/ROLES.md`. Access decides *who*; this app decides *what*.

| Actor | May | Gate (code) |
|---|---|---|
| signed-in `user` | read every library page: search, cards, vendors, sources, documents, database views | any valid token → `_account()` (`agent/web.py`) + the `catalog:read` gate on `/api/*` and `/mcp` |
| `admin` (this app's `library.account.role`) | the above **plus** create/delete account rows and roles | `admin_gated` — `agent/web.py:1639-1640`, `role != "admin"` ⇒ 403 at `:1541` |
| machine client | read only (`catalog:read`) | edge + container verifier |

**The only write in this app is an account row.** There is no scope that lets
anyone modify catalog content, and no write endpoint in the Worker at all.
Being an Access admin does **not** confer this app's admin — the role comes
from `library.account`.

Becoming admin: the owner sets `role = admin` on the person's row on
`/admin` (or the row is created that way).

**People are created at `https://access.hilir.app/admin/users`** (admin only):
email + name + roles (a comma-separated list). The password is shown once —
send it to the person. This app's own role (its `library.account.role`) is still set on techlib's `/admin`: creating the Access account does not create the app row.

## Do not (each of these broke production once)

1. **Do not reintroduce a key or password login.** The library key, `LIBRARY_USERS`,
   `users.py`, the container's `/login` and the edge's `?classic=1` were deleted on
   purpose. Access is the only door.
2. **Do not use the client name as the audience.** Tokens carry `aud = the resource
   origin`. `audience: "techlib"` rejects every real token.
3. **Do not send the secret in the body.** The client is registered
   `client_secret_basic`; body secrets get `invalid_client`.
4. **Do not drop the `resource` parameter.** Without it the provider mints an
   opaque token that cannot be verified locally.
5. **Do not "fix" sign-out by clearing more cookies.** The session belongs to
   Access; the browser must visit the end-session endpoint (RP-Initiated Logout).
6. **Do not make sign-out a form POST.** Cross-origin redirects after a
   form-initiated navigation are dropped by browsers — it must be a link/navigation.
7. **Do not cache HTML.** Auth-dependent pages are `no-store`; a stale copy shows
   the signed-out chrome with dead controls.
8. **Do not read identity from a header** (`x-hilir-email` is gone). Identity comes
   from the userinfo endpoint, cached per token inside `agent/auth.py`.
9. **Do not fetch Access with a library-default User-Agent** from the VPS
   (Cloudflare answers error 1010). `agent/auth.py` sends its own UA — keep it.

## Failure signatures

| Symptom | Cause |
|---|---|
| `invalid_scope` at the authorize step | scope missing from the provider catalogue (`oauthProvider({scopes})` in the Access repo) or not on the client |
| `invalid_client` at the token step | wrong secret, or the wrong auth method (body instead of Basic) |
| Sign-in loops back to `/login` | local verify failing — check `iss`, `aud`, `alg=EdDSA`, and the token actually being a JWT |
| Signed in but "no account" | the person's email has no row in `library.account` (roles are store-driven) |
| "Logout error — confirmation invalid or expired" | the CSP `form-action` rewrite in the Access worker is missing |
