# techlib × hilir Access — where the integration documentation lives now

**Superseded 2026-11-06.** The long integration guide that used to be this file described the
retired design (`sk-` keys, the `ACCESS` Service Binding, `INTERNAL_TOKENS`, `aud: "techlib-api"`,
the container login, `/login?classic=1`). It is archived verbatim at
[docs/archive/2026-11-06_HILIR-ACCESS-INTEGRATION_v2026.11.03.md](docs/archive/2026-11-06_HILIR-ACCESS-INTEGRATION_v2026.11.03.md)
and must not be followed.

## Live documentation

| Question | Read |
| --- | --- |
| How sign-in works, where the code lives, what never to reintroduce | [docs/AUTH.md](docs/AUTH.md) |
| Topology, secrets, publish procedure, post-deploy verification | [docs/HOSTING.md](docs/HOSTING.md) — **current-state section at the top only** |
| Estate-wide authority (roles, keys, other apps) | `hilir-access/docs/STATUS.md` (FINAL STATE) |
| Why the estate looks like this | [docs/DECISIONS.md](docs/DECISIONS.md) decision #35 |

## The model in five lines

1. Browsers sign in at `https://access.hilir.app`; this repo is an OIDC client (PKCE, client id an
   opaque string, never the name `techlib`).
2. Every hop verifies locally: the Workers with `jose`, the container with `PyJWT` + JWKS (EdDSA).
3. `aud` is a **registered resource origin** (`https://techlib.hilir.app` or
   `https://techlib-api.hilir.app`), never a client name.
4. Machine callers send an Access access token, or a person's estate key introspected at Access
   (RFC 7662) with the dedicated `techlib-api` client — one credential per role.
5. Authorization is route-level and lives here; a scope is a precondition, not a permission.
