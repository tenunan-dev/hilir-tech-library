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
import { Container, getContainer } from "@cloudflare/containers";
import OAuthProvider, { type ConsentDescription, type OAuthHelpers } from "@cloudflare/workers-oauth-provider";
import { createKeyChecker, type KeyResult } from "./hilir-auth";
import {
  DEFAULT_AUDIENCE, HILIR_SCOPE, auditLine, audienceVerdict, authorize, type Principal,
} from "./authz";

const ORIGIN = "https://techlib-api.hilir.app"; // owner-confirmed 2026-10-31 (P0.3)
const INTERNAL = "https://library.internal"; // synthetic origin: the container serves by path

interface Env {
  LIBRARY_API_KEY: string; // set with: wrangler secret put LIBRARY_API_KEY
  DATABASE_URL?: string; // read-only Neon DSN; set with: wrangler secret put DATABASE_URL
  USER_STORE_URL?: string; // account-store DSN (per-user keys + OAuth account resolution); optional
  OAUTH_KV: KVNamespace;
  OAUTH_PROVIDER: OAuthHelpers;
  ACCESS: Fetcher; // Service Binding to hilir-access (sk- key introspection)
  INTERNAL_TOKENS: string; // shared internal token csv; wrangler secret put INTERNAL_TOKENS
  AUDIENCE?: string; // machine-key audience this API accepts; default "techlib" (wrangler var)
  ORIGIN_TOKEN: string; // shared origin secret the VPS Caddy requires (VPS-COMPUTE.md §5.3); wrangler secret put ORIGIN_TOKEN
  LIBRARY_ORIGIN: string; // tunnel origin serving the VPS containers, e.g. https://techlib-origin.hilir.app (wrangler var)
}

export class LibraryApi extends Container<Env> {
  defaultPort = 8000;
  sleepAfter = "30m";
  enableInternet = true; // the server must reach Neon Postgres

  constructor(ctx: DurableObjectState<{}>, env: Env) {
    super(ctx, env);
    this.envVars = { LIBRARY_API_KEY: env.LIBRARY_API_KEY, LIBRARY_PUBLIC_URL: ORIGIN, LIBRARY_WEB: "off",
                     ...(env.DATABASE_URL ? { DATABASE_URL: env.DATABASE_URL } : {}),
                     ...(env.USER_STORE_URL ? { USER_STORE_URL: env.USER_STORE_URL } : {}) };
  }
}

function sameKey(a: string, b: string): boolean {
  const x = new TextEncoder().encode(a), y = new TextEncoder().encode(b);
  if (x.length !== y.length) return false;
  let diff = 0;
  for (let i = 0; i < x.length; i++) diff |= x[i] ^ y[i];
  return diff === 0;
}

function keyOk(env: Env, given: string | null): boolean {
  if (!given) return false;
  if (given.startsWith("hlt_")) return true; // resolved inside the container against the account store
  return !!env.LIBRARY_API_KEY && env.LIBRARY_API_KEY.length >= 24 && sameKey(given, env.LIBRARY_API_KEY);
}

// hilir Access machine keys (sk-…): introspected through the Service Binding with a
// 60 s result cache (checker cached per-env so the cache survives requests). The principal
// carries the key's owner and id, so request/denial logs name the actor. Fail closed on any
// introspection error: unreachable access = no machine access, never open access.
const hilirCheckers = new WeakMap<Env, (rawKey: string) => Promise<KeyResult | null>>();

/** Resolve any accepted credential to a principal, or null when it is not usable. */
async function principalOf(env: Env, given: string | null): Promise<Principal | null> {
  if (!given) return null;
  if (!given.startsWith("sk-")) {
    // master key (owner) or a per-user hlt_ key resolved inside the container
    if (!keyOk(env, given)) return null;
    return { kind: given.startsWith("hlt_") ? "hlt" : "master", scopes: [HILIR_SCOPE] };
  }
  let checker = hilirCheckers.get(env);
  if (!checker) {
    checker = createKeyChecker({ binding: env.ACCESS, internalToken: env.INTERNAL_TOKENS });
    hilirCheckers.set(env, checker);
  }
  try {
    const result = await checker(given);
    if (!result?.active) return null;
    return { kind: "key", userId: result.userId, keyId: result.keyId, audience: result.audience, scopes: result.scopes };
  } catch (err) {
    console.error(`hilir introspect failed (${err instanceof Error ? err.message : "error"}) — failing closed`);
    return null;
  }
}

/**
 * The Machine-facing gate for /api and machine Bearer on /mcp: authenticate → catalog:read →
 * audience. Logs the actor for every machine request and every denial. Returns null to proceed.
 */
async function machineGate(request: Request, env: Env, presented: string | null): Promise<Response | null> {
  const principal = await principalOf(env, presented);
  const denied = authorize(principal);
  if (denied) {
    console.log(auditLine("denied", principal, { path: new URL(request.url).pathname, status: denied.status }));
    return denied;
  }
  const audience = audienceVerdict(principal as Principal, env.AUDIENCE ?? DEFAULT_AUDIENCE);
  if (!audience.ok) {
    console.log(auditLine("denied_audience", principal, {
      path: new URL(request.url).pathname,
      status: 403,
      detail: audience.reason,
      expected: audience.expected,
      actual: audience.actual ?? "",
    }));
    return Response.json(
      { error: "forbidden", reason: "audience", detail: audience.reason, expected: audience.expected },
      { status: 403 },
    );
  }
  console.log(auditLine("request", principal, {
    method: request.method, path: new URL(request.url).pathname,
  }));
  return null;
}

function storeDsnHeaders(request: Request, env: Env): Headers {
  const headers = new Headers(request.headers);
  headers.set("x-user-store-dsn", env.USER_STORE_URL ?? "");
  return headers;
}

async function toContainer(request: Request, env: Env): Promise<Response> {
  const headers = storeDsnHeaders(request, env);
  const given = request.headers.get("x-api-key") || (request.headers.get("authorization") ?? "").replace(/^Bearer /, "") || "";
  headers.delete("authorization");
  if (!given.startsWith("hlt_")) {
    headers.delete("x-api-key");
    headers.set("x-api-key", env.LIBRARY_API_KEY);
  }
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

const escape = (value: string) => value.replace(/[&<>"']/g, (c) => `&#${c.charCodeAt(0)};`);

function consentPage(d: ConsentDescription, handle: string, error = ""): string {
  const origin = d.clientDomain
    ? `Published by <strong>${escape(d.clientDomain)}</strong>.`
    : "This app registered itself; its name is not verified.";
  return `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Connect ${escape(d.clientName)} to the HILIR Technology Library</title>
<style>body{font:16px system-ui,sans-serif;max-width:32rem;margin:3rem auto;padding:0 1rem}input[type=password]{width:100%;padding:.5rem;font:inherit}button{padding:.5rem 1rem;font:inherit;margin-right:.5rem}.err{color:#b00020}</style>
<h1>Connect ${escape(d.clientName)}?</h1>
<p>${origin} Access will be sent to <strong>${escape(d.redirectHost)}</strong>.</p>
${d.redirectIsLoopback ? "<p><strong>This sends access to an app on your computer.</strong> Continue only if you just started connecting from it.</p>" : ""}
<p>It will be able to search the library and read its open-licence documents and technology cards (read only).</p>
${error ? `<p class="err">${escape(error)}</p>` : ""}
<form method="post">
<input type="hidden" name="handle" value="${escape(handle)}">
<label>Library API key<br><input type="password" name="key" autocomplete="current-password" required></label>
<p><button name="decision" value="approve">Allow</button><button name="decision" value="deny" formnovalidate>Deny</button></p>
</form>`;
}

const authPages = {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname !== "/authorize") return new Response("Not found", { status: 404 });
    const oauth = env.OAUTH_PROVIDER;
    if (request.method === "GET") {
      const authRequest = await oauth.parseAuthRequest(request);
      const details = await oauth.describeConsent(authRequest);
      const consent = await oauth.beginConsent(authRequest);
      consent.headers.set("Content-Type", "text/html; charset=utf-8");
      return new Response(consentPage(details, consent.handle), { headers: consent.headers });
    }
    const form = await request.formData();
    const handle = String(form.get("handle"));
    if (form.get("decision") !== "approve") {
      const denied = await oauth.denyConsent(request, handle);
      return new Response(null, { status: 302, headers: denied.headers });
    }
    if (!keyOk(env, String(form.get("key") ?? ""))) {
      const denied = await oauth.denyConsent(request, handle);
      return new Response(null, { status: 302, headers: denied.headers });
    }
    const approved = await oauth.approveConsent(request, handle, { scope: ["mcp:read"] });
    const { redirectTo } = await oauth.completeAuthorization({
      request: approved.request,
      userId: "owner",
      metadata: {},
      scope: ["mcp:read"],
      props: { userId: "owner" },
    });
    approved.headers.set("Location", redirectTo);
    return new Response(null, { status: 302, headers: approved.headers });
  },
};

const oauthProvider = new OAuthProvider<Env>({
  apiRoute: "/mcp",
  apiHandler: { fetch: (request: Request, env: Env) => toContainer(request, env) },
  defaultHandler: authPages,
  authorizeEndpoint: "/authorize",
  tokenEndpoint: "/oauth/token",
  clientRegistrationEndpoint: "/register",
  clientIdMetadataDocumentEnabled: true,
  scopesSupported: ["mcp:read", "offline_access"],
  requiredScopes: ["mcp:read"],
  resourceMetadata: { resource: `${ORIGIN}/mcp`, authorization_servers: [ORIGIN] },
});

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return Response.json({ service: "HILIR Technology Library", role: "backend", mcp: "/mcp", rest: "/api", openapi: "/api/openapi.json" });
    }
    if (url.pathname === "/api/openapi.json") {
      return toContainer(request, env);
    }
    const apiKey = request.headers.get("x-api-key");
    const bearer = (request.headers.get("authorization") ?? "").replace(/^Bearer\s+/i, "");
    if (apiKey !== null || url.pathname.startsWith("/api/")) {
      // x-api-key wins when present (estate docs: never send both)
      const denied = await machineGate(request, env, apiKey ?? bearer);
      return denied ?? toContainer(request, env);
    }
    if (bearer && (bearer.startsWith("sk-") || keyOk(env, bearer))) {
      // older clients send the library key as a bearer token; Access sk- keys are machine auth
      const denied = await machineGate(request, env, bearer);
      return denied ?? toContainer(request, env);
    }
    return oauthProvider.fetch(request, env, ctx); // /mcp with OAuth tokens, and the OAuth endpoints
  },
};
