// techlib UI edge handler (Phase 4 / AUTH-REBUILD §4.3).
//
// Auth model: the Worker is an OIDC *client* of hilir Access:
//
//   GET /login      → shared package builds the PKCE authorization URL
//   GET /auth/callback → shared package exchanges the code (sets our cookies)
//   everything else → verify the stored token locally (jose, EdDSA); refresh it
//                     when expired; forward `Authorization: Bearer <token>` to
//                     the container, which verifies it itself (agent/auth.py)
//
// The container holds no signing key, no password and no login form (step 3,
// 2026-11-05): the bearer token is the only credential in the whole hop. It
// resolves the token's email to its account row, so roles stay store-driven.
//
// Forwarding form is unchanged: the client's URL never travels, the body is
// read once, and redirects stay "manual" so the container's 303s reach the
// browser intact.

import {
  callback as completeLogin,
  cookieNames,
  discover,
  endSessionUrl,
  login as startLogin,
  readCookies,
  refresh as refreshTokens,
  safeNext,
  serializeCookie,
  tokenCookies,
  verify,
  type OidcConfig,
} from "@tenunan-dev/hilir-auth";
import { upstreamFetch, userinfoFetch } from "./proxy";

// keep in sync with PREFIXES in agent/web.py
const UI_PREFIXES = ["/search", "/technologies", "/compare", "/export", "/database", "/glossary", "/standards", "/vendors", "/equipment", "/projects", "/register", "/sources", "/documents", "/gaps", "/admin", "/account"];
const isUi = (p: string) => p === "/" || UI_PREFIXES.some((x) => p.startsWith(x));

/**
 * Read-only machine surfaces on this host. Since step 3 they need a hilir
 * bearer token (the same verify/refresh path as the pages) — the library key
 * they used to accept no longer exists. /api/openapi.json stays public to
 * match the backend worker and the container's api.PUBLIC_PATHS.
 */
const TOKEN_HELD = ["/api/stats", "/api/version"];

interface Env {
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
  _email?: string | null,
): Promise<Response> {
  const headers = dsnHeaders(request, env);
  headers.set("x-origin-token", env.ORIGIN_TOKEN);
  if (token) {
    // Replaces anything the browser sent: the edge decides the identity.
    headers.set("authorization", `Bearer ${token}`);
  }
  // The outbound hop itself lives in ./proxy.ts — destination pinned to the
  // literal tunnel origin (SSRF gate), validated in its own module.
  return upstreamFetch(request, env.LIBRARY_ORIGIN, headers);
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
  return [names.access, names.refresh, names.idToken, names.state, names.next].map((name) =>
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
    // The userinfo hop itself lives in ./proxy.ts — https-only, host pinned
    // to the Access issuer, loopback/private rejected (SSRF gate).
    const res = await userinfoFetch(env.HILIR_ISSUER, doc.userinfo_endpoint, token);
    if (!res || !res.ok) return { email: null, sub: null };
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

    // Machine-held read-only endpoints: a hilir bearer token is required — the
    // same verify/refresh path as the pages. No token = 401 JSON, not a redirect.
    if (TOKEN_HELD.includes(url.pathname)) {
      const { token, setCookies } = await resolveToken(request, env);
      if (!token) return Response.json({ error: "missing or invalid token" }, { status: 401 });
      return withCookies(await toContainer(request, env, token), setCookies);
    }

    // The schema is public (matches the backend worker and the container's api.PUBLIC_PATHS).
    if (url.pathname === "/api/openapi.json") {
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
            `<p><a href="/login">Try again</a></p></body>`,
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
      // RP-Initiated Logout (OIDC): clearing our own cookies is not enough —
      // the session lives at Access on .hilir.app, so the browser must visit the
      // provider's end-session endpoint. The persisted id_token goes along as
      // id_token_hint (RP-Initiated Logout §3): the provider then ends the
      // matching session directly and returns here — no confirmation
      // interstitial (its signed state cookie proved browser-fragile,
      // 2026-11-05), and it works even when the SSO cookie is already gone.
      // Without a stored hint the provider falls back to its confirmation page.
      const idToken = readCookies(request).get(cookieNames(oidcConfig(env)).idToken);
      const end = await endSessionUrl(oidcConfig(env), {
        postLogoutRedirectUri: `${env.APP_ORIGIN.replace(/\/+$/, "")}/`,
        ...(idToken ? { idTokenHint: idToken } : {}),
      });
      return redirect(end ?? "/", clearSessionCookies(env));
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
