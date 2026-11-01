/**
 * hilir Access — drop-in consumer auth for Workers (TypeScript, zero deps).
 *
 * Copy of hilir-access/examples/hilir-auth.ts (estate consumer module).
 * Two capabilities, matching the estate model:
 *
 *   1. verifyHilirJwt()  — human sessions. Local ES256 verification against
 *      a cached /jwks.json; no per-request hop to access.
 *   2. createKeyChecker() — machine credentials (Bearer sk-…). SHA-256 hash
 *      + short-TTL cache + Service-Binding introspection fallback.
 *
 * See docs/INTEGRATION.md in the hilir-access repo for setup per subdomain.
 */

// ---------------------------------------------------------------------------
// shared
// ---------------------------------------------------------------------------

function b64uToBytes(s: string): Uint8Array {
  const b64 = s.replace(/-/g, "+").replace(/_/g, "/");
  const bin = atob(b64 + "=".repeat((4 - (b64.length % 4)) % 4));
  const out = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
  return out;
}

export async function sha256B64u(input: string): Promise<string> {
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(input));
  let bin = "";
  for (const b of new Uint8Array(digest)) bin += String.fromCharCode(b);
  return btoa(bin).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

// ---------------------------------------------------------------------------
// 1) JWT verification (web sessions)
// ---------------------------------------------------------------------------

export interface HilirJwtOptions {
  /** https://access.hilir.app */
  issuer: string;
  /** your app's client_id as registered with hilir-access (e.g. "techlib") */
  audience: string;
  /** override only for tests; default `${issuer}/jwks.json` */
  jwksUrl?: string;
  /** JWKS cache lifetime; default 5 min (rotation has 24 h overlap) */
  jwksTtlMs?: number;
}

export interface HilirClaims {
  iss: string;
  sub: string;
  aud: string;
  email?: string;
  scope: string;
  exp: number;
  iat: number;
}

let jwksCache: { at: number; keys: Array<Record<string, string>> } | null = null;
const cryptoKeys = new Map<string, CryptoKey>();

async function getJwks(opts: HilirJwtOptions): Promise<Array<Record<string, string>>> {
  const ttl = opts.jwksTtlMs ?? 5 * 60_000;
  if (jwksCache && Date.now() - jwksCache.at < ttl) return jwksCache.keys;
  const res = await fetch(opts.jwksUrl ?? `${opts.issuer}/jwks.json`);
  if (!res.ok) throw new Error(`jwks fetch failed: ${res.status}`);
  const doc = (await res.json()) as { keys: Array<Record<string, string>> };
  jwksCache = { at: Date.now(), keys: doc.keys };
  return doc.keys;
}

/**
 * Verify an access JWT locally. Returns claims, or null for any failure
 * (bad signature, expired, wrong audience/issuer). Never throws.
 */
export async function verifyHilirJwt(token: string, opts: HilirJwtOptions): Promise<HilirClaims | null> {
  try {
    const parts = token.split(".");
    if (parts.length !== 3) return null;
    const [h = "", p = "", s = ""] = parts;
    const header = JSON.parse(new TextDecoder().decode(b64uToBytes(h))) as { alg?: string; kid?: string };
    if (header.alg !== "ES256" || !header.kid) return null;

    const jwk = (await getJwks(opts)).find((k) => k.kid === header.kid);
    if (!jwk) return null;
    let key = cryptoKeys.get(header.kid);
    if (!key) {
      key = await crypto.subtle.importKey("jwk", jwk as unknown as JsonWebKey, { name: "ECDSA", namedCurve: "P-256" }, false, ["verify"]);
      cryptoKeys.set(header.kid, key);
    }
    const ok = await crypto.subtle.verify(
      { name: "ECDSA", hash: "SHA-256" },
      key,
      b64uToBytes(s) as BufferSource,
      new TextEncoder().encode(`${h}.${p}`) as BufferSource,
    );
    if (!ok) return null;

    const claims = JSON.parse(new TextDecoder().decode(b64uToBytes(p))) as HilirClaims;
    const now = Math.floor(Date.now() / 1000);
    if (claims.exp <= now) return null;
    if (claims.iss !== opts.issuer) return null;
    const auds = Array.isArray(claims.aud) ? claims.aud : [claims.aud];
    if (!auds.includes(opts.audience)) return null;
    return claims;
  } catch {
    return null;
  }
}

/** Per-endpoint gate: 401 shape + scope check. Apps own authorization. */
export function requireScope(claims: HilirClaims | null, scope: string): Response | null {
  if (!claims) return new Response(JSON.stringify({ error: "unauthorized" }), { status: 401, headers: { "Content-Type": "application/json" } });
  const scopes = claims.scope.split(/\s+/);
  if (!scopes.includes(scope)) {
    return new Response(JSON.stringify({ error: "forbidden", required: scope }), { status: 403, headers: { "Content-Type": "application/json" } });
  }
  return null;
}

// ---------------------------------------------------------------------------
// 2) API-key checking (machines: Bearer sk-…)
// ---------------------------------------------------------------------------

export interface KeyCheckerOptions {
  /** Service Binding to the hilir-access worker (wrangler.toml [[services]] binding = "ACCESS") */
  binding: Fetcher;
  /** the shared INTERNAL_TOKENS value (same csv the access worker holds) */
  internalToken: string;
  /** result cache TTL; default 60 s — revocation lands within one TTL */
  cacheTtlMs?: number;
}

export interface KeyResult {
  active: boolean;
  scopes: string[];
  keyId?: string;
}

/**
 * Check a presented sk- key: local hash cache first, then Service-Binding
 * introspection. Null means the request had no usable Bearer sk- credential.
 */
export function createKeyChecker(opts: KeyCheckerOptions) {
  const cache = new Map<string, { result: KeyResult; at: number }>();
  const ttl = opts.cacheTtlMs ?? 60_000;

  return async function checkKey(rawKey: string): Promise<KeyResult | null> {
    if (!rawKey.startsWith("sk-")) return null;
    const hash = await sha256B64u(rawKey);
    const hit = cache.get(hash);
    if (hit && Date.now() - hit.at < ttl) return hit.result;

    // Service-binding fetch: internal path, no public CF-Connecting-IP header
    const res = await opts.binding.fetch("https://access.internal/keys/introspect", {
      method: "POST",
      headers: { "Content-Type": "application/json", "X-Internal-Token": opts.internalToken },
      body: JSON.stringify({ hash }),
    });
    if (!res.ok) throw new Error(`introspect failed: ${res.status}`);
    const body = (await res.json()) as { active: boolean; scopes?: string[]; key_id?: string };
    const result: KeyResult = { active: body.active === true, scopes: body.scopes ?? [], keyId: body.key_id };
    cache.set(hash, { result, at: Date.now() });
    return result;
  };
}

// ---------------------------------------------------------------------------
// request helper: JWT first, then API key — exactly the estate contract
// ---------------------------------------------------------------------------

export interface HilirAuthConfig extends HilirJwtOptions, Partial<KeyCheckerOptions> {}

/**
 * Authenticate a Request: Bearer JWT (human) or sk- key (machine).
 * Returns { kind, userId, scopes } or null. With a binding configured,
 * machines work; without one, only JWTs.
 */
export function createHilirAuth(config: HilirAuthConfig & { binding?: Fetcher; internalToken?: string }) {
  const checkKey = config.binding && config.internalToken ? createKeyChecker({ binding: config.binding, internalToken: config.internalToken, cacheTtlMs: config.cacheTtlMs }) : null;
  return async function authenticate(request: Request): Promise<{ kind: "jwt" | "key"; userId?: string; scopes: string[] } | null> {
    const header = request.headers.get("Authorization");
    if (!header?.startsWith("Bearer ")) return null;
    const token = header.slice(7).trim();
    if (token.length === 0) return null;

    if (token.startsWith("sk-")) {
      if (!checkKey) return null;
      const result = await checkKey(token);
      if (!result || !result.active) return null;
      return { kind: "key", scopes: result.scopes };
    }
    const claims = await verifyHilirJwt(token, config);
    if (!claims) return null;
    return { kind: "jwt", userId: claims.sub, scopes: claims.scope.split(/\s+/).filter(Boolean) };
  };
}
