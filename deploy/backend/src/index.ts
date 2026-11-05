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
import {
  bearerToken,
  PROTECTED_RESOURCE_METADATA_PATH,
  verify,
  keyHasScope,
  looksLikeAgentKey,
  verifyAgentKey,
} from "@tenunan-dev/hilir-auth";

const ORIGIN = "https://techlib-api.hilir.app"; // owner-confirmed 2026-10-31 (P0.3)
const INTERNAL = "https://library.internal"; // synthetic origin: the container serves by path

interface Env {
  USER_STORE_URL?: string; // account-store DSN (roles); forwarded per request
  HILIR_ISSUER: string; // https://access.hilir.app/api/auth
  /** Comma-separated registered RFC 8707 resource origins this API serves —
   *  the token's aud. NEVER a client name: the UI origin (tokens forwarded by
   *  the frontend Worker) and this API host's own origin (direct MCP clients
   *  that discover techlib-api.hilir.app). */
  AUDIENCE: string;
  REQUIRED_SCOPE?: string; // default catalog:read
  ORIGIN_TOKEN: string; // shared origin secret the VPS Caddy requires (VPS-COMPUTE.md §5.3); wrangler secret put ORIGIN_TOKEN
  HILIR_CLIENT_ID?: string; // opaque client id (wrangler var) — techlib-api, introspection only
  HILIR_CLIENT_SECRET?: string; // wrangler secret — used to verify agent keys
  LIBRARY_ORIGIN: string; // tunnel origin serving the VPS containers, e.g. https://techlib-origin.hilir.app (wrangler var)
}

/**
 * The RFC 9728 §5.1 challenge with the RFC 6750 §3.1 conditional: an
 * error="invalid_token" member ONLY when a credential was presented.
 */
export function bearerChallenge(origin: string, presented: boolean): string {
  return [
    `Bearer resource_metadata="${origin.replace(/\/+$/, "")}${PROTECTED_RESOURCE_METADATA_PATH}"`,
    ...(presented ? ['error="invalid_token"'] : []),
  ].join(", ");
}

/** AUDIENCE is a comma-separated list of registered resource origins. */
export function parseAudiences(value: string): string[] {
  return value.split(",").map((a) => a.trim()).filter(Boolean);
}

function jsonError(status: number, body: Record<string, unknown>, request?: Request): Response {
  let challenge = "Bearer";
  if (request) {
    challenge = bearerChallenge(
      new URL(request.url).origin,
      Boolean(request.headers.get("authorization")),
    );
  }
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      ...(status === 401 ? { "www-authenticate": challenge } : {}),
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
    return jsonError(401, { error: "unauthorized" }, request);
  }
  if (looksLikeAgentKey(token)) {
    // A normal account's key (docs/MCP-CLIENTS.md §4b): introspected at Access
    // with this worker's own client credentials, cached ~60 s. Scopes — not an
    // app name — decide what it may do here.
    const info = await verifyAgentKey(
      {
        issuer: env.HILIR_ISSUER,
        clientId: env.HILIR_CLIENT_ID ?? "",
        clientSecret: env.HILIR_CLIENT_SECRET ?? "",
        redirectUri: "",
      },
      token,
    );
    const required = env.REQUIRED_SCOPE ?? "catalog:read";
    if (!info) {
      console.log(JSON.stringify({ event: "denied", actor: null, status: 401, reason: "agent_key", path }));
      return jsonError(401, { error: "unauthorized" }, request);
    }
    if (!keyHasScope(info, required)) {
      console.log(JSON.stringify({ event: "denied", actor: info.userId, status: 403, reason: "scope", required, path }));
      return jsonError(403, { error: "forbidden", required }, request);
    }
    console.log(JSON.stringify({ event: "request", actor: info.userId ?? "agent-key", path, method: request.method }));
    return null;
  }
  // Audiences are the registered resource origins (comma-separated AUDIENCE);
  // any one matching validates the token (RFC 8707 — aud is an origin).
  const audiences = parseAudiences(env.AUDIENCE);
  let user: Awaited<ReturnType<typeof verify>> = null;
  for (const audience of audiences) {
    user = await verify(token, { issuer: env.HILIR_ISSUER, audience });
    if (user) break;
  }
  if (!user) {
    console.log(JSON.stringify({ event: "denied", actor: null, status: 401, reason: "invalid_token", path }));
    return jsonError(401, { error: "unauthorized" }, request);
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
