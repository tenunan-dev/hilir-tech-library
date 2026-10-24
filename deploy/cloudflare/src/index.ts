// Cloudflare Worker in front of the library's MCP server, which runs as a Cloudflare Container
// built from the repo's Dockerfile (catalog plus open-licence documents only).
// The Worker checks the API key at the edge so unauthenticated requests never wake the container;
// the server inside checks it again.
import { Container, getContainer } from "@cloudflare/containers";

interface Env {
  LIBRARY: DurableObjectNamespace<Library>;
  LIBRARY_API_KEY: string; // set with: wrangler secret put LIBRARY_API_KEY
}

export class Library extends Container<Env> {
  defaultPort = 8000;
  sleepAfter = "30m"; // stop after 30 idle minutes; the next request starts it again
  enableInternet = false; // the server needs no outbound access

  constructor(ctx: DurableObjectState<{}>, env: Env) {
    super(ctx, env);
    this.envVars = { LIBRARY_API_KEY: env.LIBRARY_API_KEY };
  }
}

function sameKey(a: string, b: string): boolean {
  const x = new TextEncoder().encode(a), y = new TextEncoder().encode(b);
  if (x.length !== y.length) return false;
  let diff = 0;
  for (let i = 0; i < x.length; i++) diff |= x[i] ^ y[i];
  return diff === 0;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === "/" || url.pathname === "/health") {
      return Response.json({ service: "og-tech-sources MCP server", endpoint: "/mcp", auth: "x-api-key header" });
    }
    const given = request.headers.get("x-api-key") ??
      (request.headers.get("authorization") ?? "").replace(/^Bearer\s+/i, "");
    if (!env.LIBRARY_API_KEY || env.LIBRARY_API_KEY.length < 24 || !sameKey(given, env.LIBRARY_API_KEY)) {
      return Response.json({ error: "missing or wrong API key" }, { status: 401 });
    }
    // One instance is enough for personal use; requests share it.
    return getContainer(env.LIBRARY, "main").fetch(request);
  },
};
