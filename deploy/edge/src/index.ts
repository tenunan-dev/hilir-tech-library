/**
 * techlib edge — one Worker, two containers (Phase 4 consolidation).
 *
 * Before: `og-tech-library-ui` (techlib.hilir.app) and `og-tech-library-api`
 * (techlib-api.hilir.app) — two Workers whose only job was auth + proxy, since
 * the app code lives in two VPS containers. Two copies of one job.
 *
 * Now: this Worker serves both hostnames and decides per request:
 *
 *   host techlib-api.hilir.app        → API handler   (unchanged URLs: /mcp, /api/*)
 *   techlib.hilir.app/mcp*            → API handler   (new, consolidated path)
 *   techlib.hilir.app/authorize       → API handler   (connector OAuth)
 *   techlib.hilir.app/api/v1/*        → API handler   (new prefix for API REST)
 *   everything else                   → UI handler    (unchanged URLs)
 *
 * Both handlers are the existing, proven modules — imported rather than
 * rewritten, so UI session/SSO behaviour and the API's key/token checks are
 * byte-for-byte what shipped in Phase 3. The auth rewrite (AUTH-REBUILD §4.3)
 * happens next, in one place instead of two.
 *
 * Keeping techlib-api.hilir.app answering means no machine client breaks on
 * day one; it can 308 to the consolidated paths after clients migrate.
 */

import api from "../../backend/src/index";
import ui from "../../frontend/src/index";
import { PROTECTED_RESOURCE_METADATA_PATH, protectedResourceMetadata } from "@tenunan-dev/hilir-auth";

/** Union of both workers' bindings — each handler reads only what it knows. */
type Env = Parameters<typeof ui.fetch>[1] & Parameters<typeof api.fetch>[1];

const API_HOST = "techlib-api.hilir.app";
const API_PATH_PREFIXES = ["/mcp", "/authorize", "/api/v1/"];

function isApiPath(pathname: string): boolean {
  return API_PATH_PREFIXES.some((prefix) => pathname === prefix || pathname.startsWith(prefix));
}

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    const url = new URL(request.url);

    // RFC 9728: this MCP server's protected-resource metadata, served on BOTH
    // hostnames (each names itself as the resource, i.e. the token audience).
    if (url.pathname === PROTECTED_RESOURCE_METADATA_PATH) {
      return Response.json(
        protectedResourceMetadata(
          { issuer: (env as { HILIR_ISSUER?: string }).HILIR_ISSUER ?? "", clientId: "", redirectUri: "" },
          { resource: url.origin, scopes: ["catalog:read"], documentation: `${url.origin}/` },
        ),
      );
    }

    // A request that arrived on the API hostname is API traffic by definition,
    // whatever its path — that keeps every existing machine client working.
    const chosen = url.hostname === API_HOST || isApiPath(url.pathname) ? api : ui;
    // Both modules export a Worker-style handler; the union of the two default
    // exports is not directly callable, so pin the common shape once.
    const handler = chosen as unknown as {
      fetch: (request: Request, env: Env, ctx: ExecutionContext) => Promise<Response>;
    };
    return handler.fetch(request, env, ctx);
  },
};
