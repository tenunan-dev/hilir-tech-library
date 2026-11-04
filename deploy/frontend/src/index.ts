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
  discover,
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
    // Resource indicator: without it the provider returns an opaque token that
    // cannot be verified locally (this was the sign-in loop). The identifier is
    // the registered resource and becomes the token's `aud`.
    resource: env.APP_ORIGIN.replace(/\/+$/, ""),
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
  email?: string | null,
): Promise<Response> {
  const url = new URL(request.url);
  const headers = dsnHeaders(request, env);
  const body = ["GET", "HEAD"].includes(request.method) ? undefined : await request.arrayBuffer();
  headers.set("x-origin-token", env.ORIGIN_TOKEN);
  if (email) {
    // Estate pattern: the identity rides a trusted-edge header (like tlea's
    // x-tlea-subject), because the access token carries no email claim.
    headers.set("x-hilir-email", email);
  }
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
): Promise<{ token: string | null; setCookies: string[]; email: string | null }> {
  const cfg = oidcConfig(env);
  const names = cookieNames(cfg);
  const jar = readCookies(request);

  const current = jar.get(names.access);
  if (current) {
    const user = await verify(current, { issuer: cfg.issuer, audience: cfg.resource ?? cfg.clientId });
    if (user) {
      return { token: current, setCookies: [], email: jar.get("hilir.email") ?? user.email ?? null };
    }
  }

  const refreshToken = jar.get(names.refresh);
  if (!refreshToken) return { token: null, setCookies: [], email: null };
  const fresh = await refreshTokens(cfg, refreshToken);
  if (!fresh) return { token: null, setCookies: [], email: null };
  const user = await verify(fresh.access_token, { issuer: cfg.issuer, audience: cfg.resource ?? cfg.clientId });
  if (!user) return { token: null, setCookies: [], email: null };
  const setCookies = tokenCookies(cfg, fresh);
  const email = jar.get("hilir.email") ?? user.email ?? null;
  if (!email) {
    // The identity cookie expires with the access token; refresh it too.
    const principal = await principalFromUserinfo(env, fresh.access_token);
    setCookies.push(...principalCookies(principal.email, principal.sub));
    return { token: fresh.access_token, setCookies, email: principal.email };
  }
  return { token: fresh.access_token, setCookies, email };
}

function hasClientKey(request: Request): boolean {
  return Boolean(request.headers.get("x-api-key") || request.headers.get("authorization"));
}

/**
 * Identity from the provider's userinfo endpoint — the documented OIDC source
 * for the `email` scope. The access token carries scopes/aud but no email
 * claim, and the id_token only includes claims an extension adds, so userinfo
 * is where the caller's email actually lives.
 */
async function principalFromUserinfo(
  env: Env,
  token: string,
): Promise<{ email: string | null; sub: string | null }> {
  try {
    const doc = await discover(oidcConfig(env));
    if (!doc.userinfo_endpoint) return { email: null, sub: null };
    const res = await fetch(doc.userinfo_endpoint, {
      headers: { authorization: `Bearer ${token}`, accept: "application/json" },
    });
    if (!res.ok) return { email: null, sub: null };
    const info = (await res.json()) as { email?: unknown; sub?: unknown };
    return {
      email: typeof info.email === "string" ? info.email : null,
      sub: typeof info.sub === "string" ? info.sub : null,
    };
  } catch {
    return { email: null, sub: null };
  }
}

/** Cookies carrying the caller's identity to the container hop. */
function principalCookies(email: string | null, sub: string | null): string[] {
  const out: string[] = [];
  if (email) {
    out.push(serializeCookie({ name: "hilir.email", value: email, options: { maxAge: 900 } }));
  }
  if (sub) {
    out.push(serializeCookie({ name: "hilir.sub", value: sub, options: { maxAge: 900 } }));
  }
  return out;
}

/** Decode a JWT's header and payload for diagnostics. Does not verify. */
function decodeClaims(token: string): { header: Record<string, unknown>; payload: Record<string, unknown> } {
  const parts = token.split(".");
  const decode = (part: string | undefined): Record<string, unknown> => {
    if (!part) return {};
    try {
      const b64 = part.replace(/-/g, "+").replace(/_/g, "/") + "=".repeat((4 - (part.length % 4)) % 4);
      return JSON.parse(atob(b64)) as Record<string, unknown>;
    } catch {
      return {};
    }
  };
  return { header: decode(parts[0]), payload: decode(parts[1]) };
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
        // Show the reason instead of bouncing to /login: a silent bounce turns a
        // single failure into an endless sign-in loop (seen 2026-11-04 in Safari).
        const headers = new Headers({ "content-type": "text/html; charset=utf-8", "cache-control": "no-store" });
        for (const cookie of result.cookies) headers.append("set-cookie", cookie);
        return new Response(
          `<!doctype html><meta charset="utf-8"><title>Sign-in failed</title>` +
            `<body style="font:16px/1.6 system-ui,sans-serif;max-width:36em;margin:15vh auto;padding:0 24px">` +
            `<h1>Sign-in failed</h1><p><code>${result.error}</code></p>` +
            `<p><a href="/login?classic=1">Sign in with the library key</a></p></body>`,
          { status: 400, headers },
        );
      }
      // Identity: userinfo is the documented source (email scope). The id_token
      // decode below is only a fallback for providers without userinfo.
      const principal = await principalFromUserinfo(env, result.tokens.access_token);
      const idToken = result.tokens.id_token;
      let email = principal.email;
      let sub = principal.sub;
      if (!email && idToken) {
        const idClaims = decodeClaims(idToken);
        const idEmail = idClaims.payload.email;
        const idSub = idClaims.payload.sub;
        if (typeof idEmail === "string") email = idEmail;
        if (typeof idSub === "string" && !sub) sub = idSub;
      }
      return redirect(safeNext(result.next), [...result.cookies, ...principalCookies(email, sub)]);
    }

    if (url.pathname === "/logout") {
      return redirect("/", clearSessionCookies(env));
    }

    if (isUi(url.pathname)) {
      const { token, setCookies, email } = await resolveToken(request, env);
      if (!token) {
        const next = `${url.pathname}${url.search}`;
        return redirect(`/login?next=${encodeURIComponent(next)}`);
      }
      return withCookies(await toContainer(request, env, token, email), setCookies);
    }

    return Response.json(
      { error: "not found here — the web UI is on this host; MCP is at /mcp" },
      { status: 404 },
    );
  },
};
