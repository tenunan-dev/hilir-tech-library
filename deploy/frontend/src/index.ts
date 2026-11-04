// techlib UI edge handler (Phase 4 / AUTH-REBUILD §4.3).
//
// Auth model changed here: the Worker no longer runs its own OIDC flow and no
// longer mints the container's "v2" session cookie. It is an OIDC *client*:
//
//   GET /login      → shared package builds the PKCE authorization URL
//   GET /auth/callback → shared package exchanges the code (sets our cookies)
//   everything else → verify the stored token locally (jose, EdDSA); refresh it
//                     when expired; forward `Authorization: Bearer <token>` to
//                     the container, which verifies it itself (agent/auth.py)
//
// The container therefore holds no signing key and never sees a password. It
// resolves the token's email to its account row, so roles stay store-driven.
//
// The old key/account form still works through /login?classic=1 until step 3.
//
// Forwarding form is unchanged: the client's URL never travels, the body is
// read once, and redirects stay "manual" so the container's 303s reach the
// browser intact.

import {
  callback as completeLogin,
  cookieNames,
  login as startLogin,
  readCookies,
  refresh as refreshTokens,
  safeNext,
  serializeCookie,
  tokenCookies,
  verify,
  type OidcConfig,
} from "@tenunan-dev/hilir-auth";

// keep in sync with PREFIXES in agent/web.py
const UI_PREFIXES = ["/login", "/logout", "/search", "/technologies", "/vendors", "/equipment", "/register", "/sources", "/documents", "/gaps", "/database", "/admin", "/account"];
const isUi = (p: string) => p === "/" || UI_PREFIXES.some((x) => p.startsWith(x));

/** Key-held read-only surfaces served on this host (the client's own key travels). */
const KEY_HELD = ["/api/stats", "/api/version", "/api/openapi.json"];

interface Env {
  LIBRARY_API_KEY: string;
  DATABASE_URL?: string;
  USER_STORE_URL?: string;
  LIBRARY_ORIGIN: string; // https://techlib-origin.hilir.app
  ORIGIN_TOKEN: string; // shared origin secret Caddy requires
  HILIR_ISSUER: string; // https://access-v2.hilir.app/api/auth
  HILIR_CLIENT_ID: string; // opaque id — not the name "techlib"
  HILIR_CLIENT_SECRET: string;
  APP_ORIGIN: string; // https://techlib.hiril.app
}

function oidcConfig(env: Env): OidcConfig {
  return {
    issuer: env.HILIR_ISSUER,
    clientId: env.HILIR_CLIENT_ID,
    clientSecret: env.HILIR_CLIENT_SECRET,
    redirectUri: `${env.APP_ORIGIN.replace(/\/+$/, "")}/auth/callback`,
    scopes: ["openid", "profile", "email", "offline_access", "catalog:read"],
  };
}

// --- container hop ------------------------------------------------------------

function dsnHeaders(request: Request, env: Env): Headers {
  const headers = new Headers(request.headers);
  // The account-store DSN rides every request; the Worker secret is authoritative
  // so container instances never hold a stale copy.
  headers.set("x-user-store-dsn", env.USER_STORE_URL ?? "");
  return headers;
}

async function toContainer(
  request: Request,
  env: Env,
  token?: string | null,
): Promise<Response> {
  const url = new URL(request.url);
  const headers = dsnHeaders(request, env);
  const body = ["GET", "HEAD"].includes(request.method) ? undefined : await request.arrayBuffer();
  headers.set("x-origin-token", env.ORIGIN_TOKEN);
  if (token) {
    // Replaces anything the browser sent: the edge decides the identity.
    headers.set("authorization", `Bearer ${token}`);
  }
  const upstream = new Request(`${env.LIBRARY_ORIGIN}${url.pathname}${url.search}`, {
    method: request.method,
    headers,
    body,
    redirect: "manual",
  });
  return fetch(upstream);
}

/** Add Set-Cookie headers from a token refresh to a proxied response. */
function withCookies(response: Response, cookies: string[]): Response {
  if (cookies.length === 0) return response;
  const merged = new Response(response.body, response);
  for (const cookie of cookies) merged.headers.append("set-cookie", cookie);
  return merged;
}

function redirect(location: string, cookies: string[] = []): Response {
  const headers = new Headers({ location, "cache-control": "no-store" });
  for (const c of cookies) headers.append("set-cookie", c);
  return new Response(null, { status: 303, headers });
}

function clearSessionCookies(env: Env): string[] {
  const names = cookieNames(oidcConfig(env));
  return [names.access, names.refresh, names.state, names.next].map((name) =>
    serializeCookie({ name, value: "", options: { maxAge: 0 } }),
  );
}

// --- session resolution -------------------------------------------------------

/**
 * The access token to forward, refreshing once if it has expired. Returns null
 * when the caller is not signed in (or the refresh token is dead).
 */
async function resolveToken(
  request: Request,
  env: Env,
): Promise<{ token: string | null; setCookies: string[] }> {
  const cfg = oidcConfig(env);
  const names = cookieNames(cfg);
  const jar = readCookies(request);

  const current = jar.get(names.access);
  if (current) {
    const user = await verify(current, { issuer: cfg.issuer, audience: cfg.clientId });
    if (user) return { token: current, setCookies: [] };
  }

  const refreshToken = jar.get(names.refresh);
  if (!refreshToken) return { token: null, setCookies: [] };
  const fresh = await refreshTokens(cfg, refreshToken);
  if (!fresh) return { token: null, setCookies: [] };
  const user = await verify(fresh.access_token, { issuer: cfg.issuer, audience: cfg.clientId });
  if (!user) return { token: null, setCookies: [] };
  return { token: fresh.access_token, setCookies: tokenCookies(cfg, fresh) };
}

function hasClientKey(request: Request): boolean {
  return Boolean(request.headers.get("x-api-key") || request.headers.get("authorization"));
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === "/health") {
      return Response.json({
        service: "HILIR Technology Library",
        role: "ui",
        api: `/mcp · /api/v1`,
        auth: "hilir Access",
      });
    }

    // Key-held read-only endpoints: the client's own key is forwarded untouched.
    if (KEY_HELD.includes(url.pathname)) {
      return hasClientKey(request) ? toContainer(request, env)
        : Response.json({ error: "missing or wrong API key" }, { status: 401 });
    }

    // Legacy sign-in (container's own key/account form) until step 3.
    if (url.pathname === "/login" && (request.method === "POST" || url.searchParams.get("classic") === "1")) {
      return toContainer(request, env);
    }

    if (url.pathname === "/login") {
      const next = url.searchParams.get("next") ?? undefined;
      const start = await startLogin(oidcConfig(env), next !== undefined ? { next } : {});
      return redirect(start.url, start.cookies);
    }

    if (url.pathname === "/auth/callback") {
      const result = await completeLogin(oidcConfig(env), url, request);
      if (!result.ok) {
        return redirect(`/login?error=${encodeURIComponent(result.error)}`, result.cookies);
      }
      return redirect(safeNext(result.next), result.cookies);
    }

    if (url.pathname === "/logout") {
      return redirect("/", clearSessionCookies(env));
    }

    if (isUi(url.pathname)) {
      const { token, setCookies } = await resolveToken(request, env);
      if (!token) {
        const next = `${url.pathname}${url.search}`;
        return redirect(`/login?next=${encodeURIComponent(next)}`);
      }
      return withCookies(await toContainer(request, env, token), setCookies);
    }

    return Response.json(
      { error: "not found here — the web UI is on this host; MCP is at /mcp" },
      { status: 404 },
    );
  },
};
