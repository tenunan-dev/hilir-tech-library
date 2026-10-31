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
import { Container, getContainer } from "@cloudflare/containers";

// keep in sync with PREFIXES in agent/web.py
const UI_PREFIXES = ["/login", "/logout", "/search", "/technologies", "/vendors", "/equipment", "/register", "/sources", "/documents", "/gaps", "/database", "/admin", "/account"];
const isUi = (p: string) => p === "/" || UI_PREFIXES.some((x) => p.startsWith(x));

const INTERNAL = "https://library.internal"; // synthetic origin: the container serves by path

interface Env {
  LIBRARY: DurableObjectNamespace<LibraryUI>;
  LIBRARY_API_KEY: string; // set with: wrangler secret put LIBRARY_API_KEY
  DATABASE_URL?: string; // read-only Neon DSN for the container's live reads; wrangler secret put DATABASE_URL
  LIBRARY_USERS?: string; // named web accounts (agent/users.py); wrangler secret put LIBRARY_USERS (optional)
  USER_STORE_URL?: string; // account-store DSN (agent/userstore.py, db/library.sql); optional
  API_ORIGIN?: string; // e.g. https://api.hilir.app — the footer's REST/MCP links point there (LIBRARY_API_PUBLIC_URL)
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

async function toContainer(request: Request, env: Env, injectKey: boolean): Promise<Response> {
  const url = new URL(request.url);
  const headers = storeDsnHeaders(request, env);
  const clientKey = request.headers.get("x-api-key") || (request.headers.get("authorization") ?? "").replace(/^Bearer /, "") || "";
  headers.delete("authorization");
  if (injectKey || !clientKey.startsWith("hlt_")) {
    headers.delete("x-api-key");
    headers.set("x-api-key", env.LIBRARY_API_KEY);
  }
  const body = ["GET", "HEAD"].includes(request.method) ? undefined : await request.arrayBuffer();
  return getContainer(env.LIBRARY, "main").fetch(INTERNAL + url.pathname + url.search,
                                                 { method: request.method, headers, body });
}


export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return Response.json({ service: "HILIR Technology Library", role: "frontend", ui: "/", api: env.API_ORIGIN ?? null });
    }
    // key-held read-only API surfaces kept on this domain (the client's own key travels; the
    // container verifies it — the Worker never injects one for these)
    if (url.pathname === "/api/stats" || url.pathname === "/api/openapi.json") {
      return hasClientKey(request) ? toContainer(request, env, false)
        : Response.json({ error: "missing or wrong API key" }, { status: 401 });
    }
    if (isUi(url.pathname)) return toContainer(request, env, true);
    return Response.json({ error: "the web UI lives here; MCP and the REST API live at " +
                                    (env.API_ORIGIN ?? "the api origin") }, { status: 404 });
  },
};

const hasClientKey = (request: Request) =>
  request.headers.get("x-api-key") !== null || !!request.headers.get("authorization");
