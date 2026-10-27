// Cloudflare Worker in front of the library's server, which runs as a Cloudflare Container built
// from the repo's Dockerfile (catalog plus open-licence documents only).
//
// Two ways in:
// - API key (x-api-key header, or Authorization: Bearer <key>) for /mcp and the REST API under /api.
//   The Worker checks it at the edge so unauthenticated requests never wake the container.
// - OAuth for /mcp, for clients that only connect by URL with a sign-in (claude.ai custom connectors).
//   The sign-in page asks for the same API key, so only the owner can grant access.
import { Container, getContainer } from "@cloudflare/containers";
import OAuthProvider, { type ConsentDescription, type OAuthHelpers } from "@cloudflare/workers-oauth-provider";

const ORIGIN = "https://techlib.hilir.app";

// keep in sync with PREFIXES in agent/web.py
const UI_PREFIXES = ["/login", "/logout", "/search", "/technologies", "/vendors", "/register", "/sources", "/documents", "/gaps", "/database"];
const isUi = (p: string) => p === "/" || UI_PREFIXES.some((x) => p.startsWith(x));

interface Env {
  LIBRARY: DurableObjectNamespace<Library>;
  LIBRARY_API_KEY: string; // set with: wrangler secret put LIBRARY_API_KEY
  DATABASE_URL?: string; // read-only Neon DSN for the Postgres layer; set with: wrangler secret put DATABASE_URL (optional)
  LIBRARY_USERS?: string; // named web accounts, email|name|scrypt-hash entries (agent/users.py); set with: wrangler secret put LIBRARY_USERS (optional)
  OAUTH_KV: KVNamespace;
  OAUTH_PROVIDER: OAuthHelpers;
}

export class Library extends Container<Env> {
  defaultPort = 8000;
  sleepAfter = "30m"; // stop after 30 idle minutes; the next request starts it again
  enableInternet = true; // the server must reach Neon Postgres when DATABASE_URL is set

  constructor(ctx: DurableObjectState<{}>, env: Env) {
    super(ctx, env);
    this.envVars = { LIBRARY_API_KEY: env.LIBRARY_API_KEY, LIBRARY_PUBLIC_URL: ORIGIN,
                     ...(env.DATABASE_URL ? { DATABASE_URL: env.DATABASE_URL } : {}),
                     ...(env.LIBRARY_USERS ? { LIBRARY_USERS: env.LIBRARY_USERS } : {}) };
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
  return !!given && !!env.LIBRARY_API_KEY && env.LIBRARY_API_KEY.length >= 24 && sameKey(given, env.LIBRARY_API_KEY);
}

// Forward to the container with the library key; the client's own credentials are not passed on.
function toContainer(request: Request, env: Env): Promise<Response> {
  const headers = new Headers(request.headers);
  headers.delete("authorization");
  headers.set("x-api-key", env.LIBRARY_API_KEY);
  return getContainer(env.LIBRARY, "main").fetch(new Request(request, { headers }));
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
      // The handle is single-use, so a wrong key ends this attempt; the client can start again.
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
      return Response.json({ service: "HILIR Technology Library", mcp: "/mcp", rest: "/api", openapi: "/api/openapi.json",
                             auth: "x-api-key header, or OAuth for /mcp" });
    }
    if (url.pathname === "/api/openapi.json") {
      // The schema holds no data; tools such as ChatGPT Actions import it before they have a key.
      return getContainer(env.LIBRARY, "main").fetch(request);
    }
    // the web UI authenticates with a session cookie derived from the library key, so the edge
    // must NOT require or inject the API key on these paths
    if (isUi(url.pathname)) return getContainer(env.LIBRARY, "main").fetch(request);
    const apiKey = request.headers.get("x-api-key");
    const bearer = (request.headers.get("authorization") ?? "").replace(/^Bearer\s+/i, "");
    if (apiKey !== null || url.pathname.startsWith("/api/")) {
      return keyOk(env, apiKey ?? bearer) ? toContainer(request, env)
        : Response.json({ error: "missing or wrong API key" }, { status: 401 });
    }
    if (bearer && keyOk(env, bearer)) return toContainer(request, env); // older clients sending the key as a bearer token
    return oauthProvider.fetch(request, env, ctx); // /mcp with OAuth tokens, and the OAuth endpoints
  },
};
