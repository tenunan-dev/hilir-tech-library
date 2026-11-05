<!-- CURRENT STATE — 2026-11-05 (Phase 4 cutover). The body below is HISTORICAL:
     it describes the retired design (old access.hilir.app, sk- keys, service-binding
     introspection, container login). It is kept for history and must not be followed. -->

> **Current auth for this app (verified 2026-11-05):** browsers sign in at **https://access.hilir.app** through `techlib-edge` (OIDC code + PKCE + resource indicator); the edge forwards the bearer to the container, which verifies it locally (EdDSA via `PyJWT` + the issuer's JWKS) and reads the role from the Neon `library.account` row. Machine callers send a hilir Access access token with `aud = https://techlib.hilir.app`, scope `catalog:read`. **No library key, no `LIBRARY_USERS`, no container login.** Sign-out is RP-Initiated Logout. Config: `HILIR_ISSUER=https://access.hilir.app/api/auth`, `HILIR_CLIENT_ID` (opaque), `HILIR_CLIENT_SECRET` (edge secret), `APP_ORIGIN`, `AUDIENCE=https://techlib.hilir.app`, `REQUIRED_SCOPE=catalog:read`.
> Authoritative record: `hilir-access/docs/STATUS.md`.

# techlib × hilir Access — Integration Instructions

> **⚠️ Superseded (2026-11-04).** techlib no longer uses API keys, introspection
> or the `v2` cookie. It is an OIDC client of `access-v2.hilir.app`: the edge
> verifies the access token (EdDSA/JWKS), forwards it, and the container resolves
> identity from the userinfo endpoint. Sign-out is RP-initiated logout. See
> `hilir-access/docs/STATUS.md` §5b and `docs/SIGNOUT.md` for the current state.


Wire techlib to use **access.hilir.app** as its access management (SSO + API keys). Read the estate guide first:

- `/Users/faisal.muthalib/Documents/VibeProject/hilir-access/docs/INTEGRATION.md`
- `/Users/faisal.muthalib/Documents/VibeProject/hilir-access/examples/hilir-auth.ts`

**Status:** SHIPPED (2026-11-01). UI SSO is live edge-only — the frontend
worker (`deploy/frontend/src/index.ts`) intercepts `/login` → OIDC
authorization-code + PKCE (state in the HMAC-signed `oglib_oidc` cookie),
`/auth/callback` verifies the ES256 JWT via the copied `hilir-auth.ts`, then
mints the container's own v2 session cookie (container code unchanged). The
backend worker (`deploy/backend`) carries the `[[services]]` ACCESS binding +
`INTERNAL_TOKENS` and its `credentialOk()` checks `sk-` keys via
`createKeyChecker` (60 s cache, fail-closed). Legacy paths preserved:
`/login?classic=1` master-key form, legacy master key, `hlt_` keys until
sunset. Remaining: positive-path test once a real `sk-` key exists
(Service `techlib`), and the owner's own techlib account row (below).

## Treat hilir Access as a plugin

You do **not** build login, sessions, password reset, or key management.
Access owns all of it. techlib's part is minimal (already executed 2026-11-01 —
kept as reference for re-provisioning or new environments):

1. **Register your OIDC client** (one command, run from the hilir-access repo — needs the owner's go-ahead since it writes to production D1):
   ```sh
   cd /Users/faisal.muthalib/Documents/VibeProject/hilir-access
   npm run client:add -- --name techlib --redirect https://techlib.hilir.app/auth/callback --remote
   ```
   The `client_id` equals the slugified name (`techlib`).
2. **Bind + secret** (Worker deploy) — add to your `wrangler.toml`:
   ```toml
   [[services]]
   binding = "ACCESS"
   service = "hilir-access"
   ```
   then `npx wrangler secret put INTERNAL_TOKENS` (value = the csv the owner
   keeps in `hilir-access/.wrangler/internal-token.txt`; never in code, git,
   or chat).
3. **Copy the verification module** — `hilir-access/examples/hilir-auth.ts`
   → your repo as `src/auth/hilir-auth.ts`. Zero dependencies, Workers-native
   (`verifyHilirJwt`, `requireScope`, `createHilirAuth`).

That is the whole plugin. Everything else is *your* authorization choices.

## What you edit — and what you never touch

| You edit (your repo only) | You never touch |
|---|---|
| Your `wrangler.toml` (add the `ACCESS` binding) | The `hilir-access` repo (no code, no D1, no dashboard settings beyond your own users/keys) |
| Your auth wiring: the callback route, the middleware that calls `createHilirAuth` | The landing page repo — except adding/updating your own card (see `hilir-landing/docs/subdomain-playbook.md` §Step 4) |
| Your per-endpoint scope checks (authorization lives HERE) | DNS for `techlib.hilir.app` — a worker custom domain is auto-provisioned by deploy |
| Your `INTERNAL_TOKENS` secret (via `wrangler secret put`) | Passwords, raw `sk-` keys, user tables — Access owns them; you only see hashes/claims |

## Estate contract (unchanged from the estate guide)

access.hilir.app owns **authentication and identity**; techlib owns its own
**authorization**. techlib never stores passwords or raw API keys, never
reads any user table directly, and verifies JWTs **locally** from
`/jwks.json` (no per-request network call to access — an access outage does
not log users out).

techlib is a "both" app per the estate integration map:

| Subdomain | Worker | Kind | Integration |
|---|---|---|---|
| `techlib.hilir.app` | `og-tech-library-ui` | human UI | **OIDC authorization-code + PKCE web login** |
| `techlib-api.hilir.app` | `og-tech-library-api` | API | **JWT** (`aud: "techlib-api"`) + **Bearer sk- API keys** for machines |

## Wiring the web login (UI)

"Sign in" button → server-driven **303** redirect to:

```
https://access.hilir.app/authorize
  ?client_id=techlib
  &redirect_uri=https://techlib.hilir.app/auth/callback
  &response_type=code
  &scope=catalog:read
  &state=<random>
  &code_challenge=<S256(verifier)>
  &code_challenge_method=S256
```

The `/auth/callback` route exchanges the code at `POST https://access.hilir.app/token`
(form-encoded: `grant_type=authorization_code`, `code`, `client_id`,
`redirect_uri`, `code_verifier` — PKCE is mandatory) → receives
`{access_token, refresh_token}` → set the access token in an **httpOnly
cookie** (SameSite=Lax), refresh token server-side or in a second cookie.
Subsequent API calls carry `Authorization: Bearer <access_token>`, verified
locally by `verifyHilirJwt` — no hop to access. Redirects must be
server-driven (303s), not client-side JS.

## Wiring the API (JWT + machine keys)

```ts
import { createHilirAuth, requireScope } from "./auth/hilir-auth";

const auth = createHilirAuth({
  issuer: "https://access.hilir.app",
  audience: "techlib-api",           // JWT audience
  binding: env.ACCESS,               // [[services]] binding
  internalToken: env.INTERNAL_TOKENS, // consumer's secret
});

// per request:
const principal = await auth(request);   // kind: "jwt" (human) | "key" (machine sk-)
const denied = requireScope(principal, "catalog:read");
if (denied) return denied;
// principal.userId / principal.scopes ready for techlib logic
```

- Handles Bearer JWT (human) and Bearer `sk-…` (machine) automatically.
- Key checks: SHA-256 **base64url** hash + 60 s cache + Service-Binding
  introspection fallback — revocation lands within one TTL.
- Treat `principal === null` and `!result.active` as plain **401** — no user
  enumeration, no detail leaking.

### If the Python app serves traffic directly (not via Workers)

The repo is Python-first (`agent/` holds the server; `deploy/cloudflare/`
wraps it). Workers recipes above apply to the Worker path. If a Python
process authenticates requests itself:

- **JWTs (humans):** verify ES256 against `https://access.hilir.app/jwks.json`
  locally with any ES256-capable JWT library (e.g. PyJWT with the
  `crypto` extra) — same checks as `verifyHilirJwt`: `alg=ES256`, `iss`,
  `aud`, `exp`. Cache JWKS ~5 min. No network call per request.
- **sk- keys (machines):** Workers-only Service Bindings don't exist from a
  VPS — use the same bridge mygis uses: `hilir-introspect` (tiny Worker,
  see `/Users/faisal.muthalib/Documents/VibeProject/MyMapAPI/HILIR-ACCESS-INTEGRATION.md`
  §Architecture) over HTTPS with a **dedicated techlib-only token**. Hash =
  SHA-256 base64url of the raw key; 60 s cache; fail-closed.

## Guardrails (non-negotiable)

- Apps never see or store passwords or raw `sk-` keys — only hashes/claims
- All database queries use prepared statements / bound parameters
- Authorization (scope checks) lives **in techlib**, per endpoint; access
  only answers "who is this and what scopes do they hold"
- Local verification is the availability model — do NOT add a per-request
  network call to access for JWTs
- Old local accounts: users are migrated; do not re-add `library.account`
  writes — new accounts are created via dashboard invites only

## Users

Users were imported **identities-only** (3 Petronas users, no credentials at
rest) — each sets a password via the emailed single-use reset link; new
users are invited from the access.hilir.app dashboard (Users tab →
"Admin · invite user": email + display name + scope preset). Scope presets:
read-only (`catalog:read`) / +estimate:run / full-catalog-no-admin /
+admin:keys. Legacy `hlt_` API keys are **not** migrated — re-issue as
`sk-` keys from the dashboard and sunset `hlt_` on a communicated date.

**Owner note:** the SSO path checks only that an account *row* exists in
techlib's own store. `dev@tenunan.com` has no techlib account row, so its
SSO correctly lands on the bounce-guard page ("signed in but no techlib
account") — fix by adding that email as a techlib account (any password;
the SSO path never checks it) or using `/login?classic=1`.

## Test end-to-end

1. Full anonymous web flow at techlib.hilir.app: typed credentials at
   access → interstitial → callback → signed-in library (verified live
   2026-11-01 with a throwaway test identity).
2. Already-signed-in flow: access session reuse → silent chain → callback.
3. An email with no techlib account row lands on the bounce-guard page —
   expected, not a bug (see Users).
4. **Pending:** issue a real `sk-` key (Service `techlib`), call
   `techlib-api` with `Authorization: Bearer sk-…` — must pass; revoke and
   confirm it dies within 60 s. (The negative path — garbage `sk-` → 401 —
   is already verified live.)
5. Legacy `/login?classic=1` still signs in until sunset.
