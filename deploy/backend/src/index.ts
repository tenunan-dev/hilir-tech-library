// Backend Worker of the split deployment (decision #34): MCP + REST at techlib-api.hilir.app,
// served by a container built from deploy/docker/Dockerfile.backend (LIBRARY_WEB=off — no UI on
// this domain). Owner-confirmed domain 2026-10-31 (P0.3); /__embed retired the same day (P3.1) —
// both split containers embed queries locally, so the edge service had no callers left.
//
// Two ways in:
// - API key (x-api-key or Authorization: Bearer) for /api; the Worker checks it at the edge so
//   unauthenticated requests never wake the container.
// - OAuth for /mcp, for clients that only connect by URL with a sign-in (claude.ai connectors).
//   The sign-in page asks for the same API key, so only the owner can grant access.
// Per-user keys (hlt_…) are resolved inside the container, which owns the account store.
//
// Forwarding form: requests reach the container as <method> https://library.internal<path>?<query>
// with rewritten headers — the client's URL never travels (no pass-through of caller-controlled
// URLs); the container serves by path alone.
import { bearerToken, verify } from "@tenunan-dev/hilir-auth";

const ORIGIN = "https://techlib-api.hilir.app"; // owner-confirmed 2026-10-31 (P0.3)
const INTERNAL = "https://library.internal"; // synthetic origin: the container serves by path

interface Env {
  USER_STORE_URL?: string; // account-store DSN (roles); forwarded per request
  HILIR_ISSUER: string; // https://access-v2.hilir.app/api/auth
  AUDIENCE: string; // the app's resource identifier - the token's aud
  REQUIRED_SCOPE?: string; // default catalog:read
  ORIGIN_TOKEN: string; // shared origin secret the VPS Caddy requires (VPS-COMPUTE.md §5.3); wrangler secret put ORIGIN_TOKEN
  LIBRARY_ORIGIN: string; // tunnel origin serving the VPS containers, e.g. https://techlib-origin.hilir.app (wrangler var)
}

function jsonError(status: number, body: Record<string, unknown>): Response {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      ...(status === 401 ? { "www-authenticate": "Bearer" } : {}),
    },
  });
}

/**
 * The edge gate for machine traffic: a hilir Access access token, verified
 * locally with jose. Replaces the sk-/hlt_/master key checker and the Service
 * Binding introspection (AUTH-REBUILD §4.3, step 2b).
 */
async function machineGate(request: Request, env: Env): Promise<Response | null> {
  const path = new URL(request.url).pathname;
  const token = bearerToken(request);
  if (!token) {
    console.log(JSON.stringify({ event: "denied", actor: null, status: 401, reason: "unauthenticated", path }));
    return jsonError(401, { error: "unauthorized" });
  }
  const user = await verify(token, { issuer: env.HILIR_ISSUER, audience: env.AUDIENCE });
  if (!user) {
    console.log(JSON.stringify({ event: "denied", actor: null, status: 401, reason: "invalid_token", path }));
    return jsonError(401, { error: "unauthorized" });
  }
  const required = env.REQUIRED_SCOPE ?? "catalog:read";
  if (!user.scope.includes(required)) {
    console.log(JSON.stringify({ event: "denied", actor: user.sub, status: 403, reason: "scope", required, path }));
    return jsonError(403, { error: "forbidden", required });
  }
  console.log(JSON.stringify({ event: "request", actor: user.sub, path, method: request.method }));
  return null;
}

function storeDsnHeaders(request: Request, env: Env): Headers {
  const headers = new Headers(request.headers);
  headers.set("x-user-store-dsn", env.USER_STORE_URL ?? "");
  // Step 3 (2026-11-05): the verified bearer travels to the container — it is
  // the only credential (machineGate already checked iss/aud/scope; the
  // container verifies it again and resolves the role row). No API keys exist.
  headers.delete("x-api-key");
  return headers;
}

async function toContainer(request: Request, env: Env): Promise<Response> {
  const headers = storeDsnHeaders(request, env);
  const url = new URL(request.url);
  const body = ["GET", "HEAD"].includes(request.method) ? undefined : await request.arrayBuffer();
  // Phase 3 (VPS-COMPUTE.md §5.3): the container runs on the VPS now — the
  // same path-only contract over the tunnel origin instead of the binding.
  // Caddy refuses requests without the token and routes marked requests to
  // the API container; the response body streams through untouched (MCP).
  headers.set("x-origin-token", env.ORIGIN_TOKEN);
  headers.set("x-origin-route", "api");
  const upstream = new Request(`${env.LIBRARY_ORIGIN}${url.pathname}${url.search}`,
                               { method: request.method, headers, body, redirect: "manual" });
  return fetch(upstream);
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return Response.json({ service: "HILIR Technology Library", role: "backend", mcp: "/mcp", rest: "/api", openapi: "/api/openapi.json" });
    }
    if (url.pathname === "/api/openapi.json") {
      return toContainer(request, env);
    }
    const denied = await machineGate(request, env);
    if (denied) return denied;
    return toContainer(request, env); // /mcp with OAuth tokens, and the OAuth endpoints
  },
};
