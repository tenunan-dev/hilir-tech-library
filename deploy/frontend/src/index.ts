// Frontend Worker of the split deployment (decision #34): the web UI at techlib.hilir.app,
// served by a container built from deploy/docker/Dockerfile.frontend (reads Neon live).
//
// Session-cookie auth model: people sign in at /login and the container verifies the signed
// cookie against the library key. The Worker injects the library key solely for the container
// hop; client API keys are never accepted on UI paths. No public API on this domain: /mcp and
// the REST API live at api.hilir.app — except key-held /api/stats and /api/openapi.json, which
// this Worker forwards only when the client presents its own key (never injected for them).
//
// Forwarding form: requests reach the container as <method> https://library.internal<path>?<query>
// with rewritten headers and the body read once — the client's URL never travels (no pass-through
// of caller-controlled URLs); the container serves by path alone.
//
// hilir Access SSO (2026-11-01): GET /login starts an OIDC authorization-code + PKCE flow
// against access.hilir.app, handled entirely at the edge (state + verifier in a short-lived
// HMAC-signed cookie). On success the Worker mints the SAME v2 session cookie the container's
// own account sign-in issues (agent/users.py session_token: "v2|" + b64url({u,exp}) + "|" +
// hex-hmac-sha256("v2|"+payload, LIBRARY_API_KEY)), so the container is unchanged: it resolves
// that cookie to the account row for the email (agent/web.py _account) and roles stay
// store-driven. The legacy key/account form remains at /login?classic=1 (owner's master-key
// sign-in). Sign-out clears the session at the edge.

import { Container, getContainer } from "@cloudflare/containers";
import { sha256B64u, verifyHilirJwt } from "./hilir-auth";

// keep in sync with PREFIXES in agent/web.py
const UI_PREFIXES = ["/login", "/logout", "/search", "/technologies", "/vendors", "/equipment", "/register", "/sources", "/documents", "/gaps", "/database", "/admin", "/account"];
const isUi = (p: string) => p === "/" || UI_PREFIXES.some((x) => p.startsWith(x));

const INTERNAL = "https://library.internal"; // synthetic origin: the container serves by path

// --- hilir Access SSO constants ------------------------------------------------
const OIDC_ISSUER = "https://access.hilir.app";
const OIDC_CLIENT_ID = "techlib"; // registered via `npm run client:add` in hilir-access
const OIDC_SCOPE = "catalog:read";
const OIDC_STATE_COOKIE = "oglib_oidc"; // short-lived PKCE state carrier
const SESSION_COOKIE = "oglib_session"; // must equal COOKIE in agent/web.py
const STATE_TTL = 600; // seconds — the whole browser round-trip to access
const SESSION_TTL = 30 * 86400; // match SESSION_TTL in agent/users.py
const BOUNCE_WINDOW = 120; // session minted this recently + back at /login = no account row

interface Env {
  LIBRARY_API_KEY: string; // set with: wrangler secret put LIBRARY_API_KEY
  DATABASE_URL?: string; // read-only Neon DSN for the container's live reads; wrangler secret put DATABASE_URL
  LIBRARY_USERS?: string; // named web accounts (agent/users.py); wrangler secret put LIBRARY_USERS (optional)
  USER_STORE_URL?: string; // account-store DSN (agent/userstore.py, db/library.sql); optional
  API_ORIGIN?: string; // e.g. https://api.hilir.app — the footer's REST/MCP links point there (LIBRARY_API_PUBLIC_URL)
  ORIGIN_TOKEN: string; // shared origin secret the VPS Caddy requires (VPS-COMPUTE.md §5.3); wrangler secret put ORIGIN_TOKEN
  LIBRARY_ORIGIN: string; // tunnel origin serving the VPS containers, e.g. https://techlib-origin.hilir.app (wrangler var)
}

export class LibraryUI extends Container<Env> {
  defaultPort = 8000;
  sleepAfter = "30m"; // stop after 30 idle minutes; the new request starts it again
  enableInternet = true; // the server must reach Neon Postgres

  constructor(ctx: DurableObjectState<{}>, env: Env) {
    super(ctx, env);
    this.envVars = { LIBRARY_API_KEY: env.LIBRARY_API_KEY,
                     ...(env.DATABASE_URL ? { DATABASE_URL: env.DATABASE_URL } : {}),
                     ...(env.LIBRARY_USERS ? { LIBRARY_USERS: env.LIBRARY_USERS } : {}),
                     ...(env.USER_STORE_URL ? { USER_STORE_URL: env.USER_STORE_URL } : {}),
                     ...(env.API_ORIGIN ? { LIBRARY_API_PUBLIC_URL: env.API_ORIGIN } : {}) };
  }
}

// The account-store DSN rides on every container request (x-user-store-dsn), overwritten from
// the Worker secret so instances that predate a rotation still see the current value. Headers
// only — the body is read once in toContainer, never re-streamed.
function storeDsnHeaders(request: Request, env: Env): Headers {
  const headers = new Headers(request.headers);
  headers.set("x-user-store-dsn", env.USER_STORE_URL ?? "");
  return headers;
}

// Forwarding is strict passthrough: the client's own credential (session cookie for UI paths,
// API key for the key-held endpoints) travels untouched and the container verifies it for real.
// The Worker NEVER injects the library key — injecting it on UI paths would make the container's
// session gate treat every visitor as the key account (observed 2026-10-31: home rendered 200
// unauthenticated). The container exempts web paths from its ASGI key gate, so UI requests need
// no key; the session cookie is checked inside web.py.
async function toContainer(request: Request, env: Env): Promise<Response> {
  const url = new URL(request.url);
  const headers = storeDsnHeaders(request, env);
  const body = ["GET", "HEAD"].includes(request.method) ? undefined : await request.arrayBuffer();
  // redirect:"manual" is load-bearing: the container answers unauthenticated UI paths with a
  // 303 to /login (Set-Cookie on the login POST rides that 303 too). The default "follow"
  // swallowed redirects inside the Worker — the browser never saw the cookie and every gate
  // rendered the sign-in page with a 200 (observed 2026-10-31, fixed the same hour).
  // Phase 3 (VPS-COMPUTE.md §5.3): the container runs on the VPS — same paths over the
  // tunnel origin; Caddy refuses requests without x-origin-token and routes unmarked
  // requests to the UI container. The response body streams through untouched.
  headers.set("x-origin-token", env.ORIGIN_TOKEN);
  const upstream = new Request(`${env.LIBRARY_ORIGIN}${url.pathname}${url.search}`,
                               { method: request.method, headers, body, redirect: "manual" });
  return fetch(upstream);
}

// --- edge SSO helpers -----------------------------------------------------------

function cookieValue(request: Request, name: string): string | null {
  for (const part of (request.headers.get("Cookie") ?? "").split(";")) {
    const eq = part.indexOf("=");
    if (eq > 0 && part.slice(0, eq).trim() === name) return part.slice(eq + 1).trim();
  }
  return null;
}

const sessionCookie = (value: string, maxAge: number) =>
  `${SESSION_COOKIE}=${value}; Max-Age=${maxAge}; Path=/; HttpOnly; Secure; SameSite=Lax`;
const stateCookie = (value: string, maxAge: number) =>
  `${OIDC_STATE_COOKIE}=${value}; Max-Age=${maxAge}; Path=/; HttpOnly; Secure; SameSite=Lax`;
const clearStateCookie = () => `${OIDC_STATE_COOKIE}=; Max-Age=0; Path=/; HttpOnly; Secure; SameSite=Lax`;
const clearSessionCookie = () => `${SESSION_COOKIE}=; Max-Age=0; Path=/; HttpOnly; Secure; SameSite=Lax`;

function bytesB64u(bytes: Uint8Array): string {
  let bin = "";
  for (const b of bytes) bin += String.fromCharCode(b);
  return btoa(bin).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function b64uJson(value: unknown): string {
  return bytesB64u(new TextEncoder().encode(JSON.stringify(value)));
}

function b64uParse<T>(s: string): T | null {
  try {
    const b64 = s.replace(/-/g, "+").replace(/_/g, "/") + "=".repeat((4 - (s.length % 4)) % 4);
    return JSON.parse(atob(b64)) as T;
  } catch {
    return null;
  }
}

async function hmacHex(secret: string, message: string): Promise<string> {
  const key = await crypto.subtle.importKey("raw", new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" }, false, ["sign"]);
  const sig = new Uint8Array(await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(message)));
  let hex = "";
  for (const b of sig) hex += b.toString(16).padStart(2, "0");
  return hex;
}

function fixedEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

/** Same-origin continuation paths only — never a scheme, host or protocol-relative URL. */
function safeNext(raw: string | null): string {
  if (raw && raw.startsWith("/") && !raw.startsWith("//") && !raw.includes("\\")) return raw;
  return "/";
}

function randomToken(bytes = 32): string {
  const buf = new Uint8Array(bytes);
  crypto.getRandomValues(buf);
  return bytesB64u(buf);
}

function redirect(location: string, cookies: string[] = []): Response {
  const headers = new Headers({ Location: location });
  for (const c of cookies) headers.append("Set-Cookie", c);
  return new Response(null, { status: 303, headers });
}

function escapeHtml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

function ssoErrorPage(message: string): Response {
  // A plain page, not a redirect back to /login: /login immediately restarts the
  // OIDC flow, so the user would never see the reason.
  const body = `<!doctype html><html><meta charset="utf-8"><title>Sign-in failed</title>` +
    `<body style="font:16px/1.6 system-ui,sans-serif;max-width:34em;margin:15vh auto;padding:0 24px">` +
    `<h1>Sign-in failed</h1><p>${escapeHtml(message)}</p>` +
    `<p><a href="/login">Try again</a> · <a href="/login?classic=1">Sign in with the library key</a></p></body></html>`;
  return new Response(body, { status: 503, headers: { "content-type": "text/html; charset=utf-8" } });
}

/** Mint the container's v2 session format (agent/users.py session_token). The extra
 *  "iat" field is ignored by the container and is used only by the bounce guard. */
async function mintSession(email: string, key: string): Promise<string> {
  const now = Math.floor(Date.now() / 1000);
  const payload = b64uJson({ u: email, exp: now + SESSION_TTL, iat: now });
  return `v2|${payload}|${await hmacHex(key, "v2|" + payload)}`;
}

/** The email when `token` is a correctly-signed session minted within BOUNCE_WINDOW seconds —
 *  i.e. the container just bounced a brand-new sign-in because the email has no account row. */
async function bouncedFreshSession(token: string | null, key: string): Promise<string | null> {
  if (!token) return null;
  const parts = token.split("|");
  if (parts.length !== 3 || parts[0] !== "v2") return null;
  if (!fixedEqual(parts[2], await hmacHex(key, "v2|" + parts[1]))) return null;
  const data = b64uParse<{ u?: string; iat?: number }>(parts[1]);
  if (!data?.u || typeof data.iat !== "number") return null;
  const age = Math.floor(Date.now() / 1000) - data.iat;
  return age >= 0 && age <= BOUNCE_WINDOW ? data.u : null;
}

async function beginSso(request: Request, env: Env, url: URL): Promise<Response> {
  const key = env.LIBRARY_API_KEY;
  if (!key) return new Response("Sign-in is not configured on this deployment.", { status: 503 });

  // Bounce guard: a session minted seconds ago that led straight back to /login means
  // the hilir identity verified fine but the email has no techlib account row. Explain
  // it once instead of restarting the flow into a loop.
  const bounced = await bouncedFreshSession(cookieValue(request, SESSION_COOKIE), key);
  if (bounced) {
    return ssoErrorPage(`You signed in as ${bounced} at hilir Access, but that email has no account in this library. Ask the owner to add it from the admin page, or use the library-key sign-in below.`);
  }

  const state = randomToken();
  const verifier = randomToken();
  const payload = b64uJson({
    s: state,
    v: verifier,
    n: safeNext(url.searchParams.get("next")),
    exp: Math.floor(Date.now() / 1000) + STATE_TTL,
  });
  const signed = `v1|${payload}|${await hmacHex(key, "v1|" + payload)}`;
  const authorize = new URL(`${OIDC_ISSUER}/authorize`);
  authorize.searchParams.set("client_id", OIDC_CLIENT_ID);
  authorize.searchParams.set("redirect_uri", `${url.origin}/auth/callback`);
  authorize.searchParams.set("response_type", "code");
  authorize.searchParams.set("scope", OIDC_SCOPE);
  authorize.searchParams.set("state", state);
  authorize.searchParams.set("code_challenge", await sha256B64u(verifier));
  authorize.searchParams.set("code_challenge_method", "S256");
  return redirect(authorize.toString(), [stateCookie(signed, STATE_TTL)]);
}

async function completeSso(request: Request, env: Env, url: URL): Promise<Response> {
  const key = env.LIBRARY_API_KEY;
  if (!key) return ssoErrorPage("Sign-in is not configured on this deployment.");

  const raw = cookieValue(request, OIDC_STATE_COOKIE);
  const parts = raw?.split("|") ?? [];
  if (parts.length !== 3 || parts[0] !== "v1" || !fixedEqual(parts[2], await hmacHex(key, "v1|" + parts[1]))) {
    return ssoErrorPage("Your sign-in attempt expired — please try again.");
  }
  const st = b64uParse<{ s: string; v: string; n: string; exp: number }>(parts[1]);
  if (!st || st.exp < Math.floor(Date.now() / 1000)) return ssoErrorPage("Your sign-in attempt expired — please try again.");
  if (!fixedEqual(st.s, url.searchParams.get("state") ?? "")) return ssoErrorPage("Sign-in state mismatch — please try again.");

  let access: string;
  try {
    const res = await fetch(`${OIDC_ISSUER}/token`, {
      method: "POST",
      headers: { "content-type": "application/x-www-form-urlencoded", accept: "application/json" },
      body: new URLSearchParams({
        grant_type: "authorization_code",
        code: url.searchParams.get("code") ?? "",
        client_id: OIDC_CLIENT_ID,
        redirect_uri: `${url.origin}/auth/callback`,
        code_verifier: st.v,
      }),
    });
    if (!res.ok) return ssoErrorPage("Token exchange failed — please try again.");
    const tokens = (await res.json()) as { access_token?: string };
    if (!tokens.access_token) return ssoErrorPage("No access token in the response — please try again.");
    access = tokens.access_token;
  } catch {
    return ssoErrorPage("Could not reach access.hilir.app — please try again.");
  }

  const claims = await verifyHilirJwt(access, { issuer: OIDC_ISSUER, audience: OIDC_CLIENT_ID });
  if (!claims?.email) return ssoErrorPage("The token failed verification — please try again.");
  if (!claims.scope.split(/\s+/).includes(OIDC_SCOPE)) {
    return ssoErrorPage(`Your hilir Access account lacks the ${OIDC_SCOPE} scope for this library.`);
  }

  const session = await mintSession(claims.email, key);
  return redirect(safeNext(st.n), [sessionCookie(session, SESSION_TTL), clearStateCookie()]);
}

function ssoLogout(): Response {
  return redirect("/", [clearSessionCookie(), clearStateCookie()]);
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return Response.json({ service: "HILIR Technology Library", role: "frontend", ui: "/", api: env.API_ORIGIN ?? null });
    }
    // hilir Access SSO routes live at the edge; POST /login and ?classic=1 keep the
    // container's legacy key/account form for the owner.
    if (url.pathname === "/login") {
      if (request.method === "POST" || url.searchParams.get("classic") === "1") return toContainer(request, env);
      return beginSso(request, env, url);
    }
    if (url.pathname === "/auth/callback") return completeSso(request, env, url);
    if (url.pathname === "/logout") return ssoLogout();
    // key-held read-only API surfaces kept on this domain (the client's own key travels; the
    // container verifies it — the Worker never injects one for these)
    if (url.pathname === "/api/stats" || url.pathname === "/api/version" || url.pathname === "/api/openapi.json") {
      return hasClientKey(request) ? toContainer(request, env)
        : Response.json({ error: "missing or wrong API key" }, { status: 401 });
    }
    if (isUi(url.pathname)) return toContainer(request, env);
    return Response.json({ error: "the web UI lives here; MCP and the REST API live at " +
                                    (env.API_ORIGIN ?? "the api origin") }, { status: 404 });
  },
};

const hasClientKey = (request: Request) =>
  request.headers.get("x-api-key") !== null || !!request.headers.get("authorization");
