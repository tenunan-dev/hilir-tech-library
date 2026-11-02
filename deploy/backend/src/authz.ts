/**
 * Authorization for the backend Worker: the identity model, the audit label, the audience
 * check and the one catalog:read gate.
 *
 * Pure functions with no Workers-runtime dependency, so the rules are unit-tested on their own
 * (deploy/backend/tests) instead of only through a live deploy.
 *
 * Estate contract: access.hilir.app answers *who* a caller is and what scopes they hold;
 * techlib owns *authorization*. The single rule for API traffic is catalog:read — reads stay
 * allowed for any active key carrying it. Nothing here grants catalogue writes; the REST
 * surface is read-only.
 */

/** The only authorization rule for the API surface. */
export const HILIR_SCOPE = "catalog:read";

/**
 * The service id a machine key must be issued for (api_keys.audience). Estate convention: the
 * audience matches the service, and the Access registry lists this library as "techlib".
 * Overridable per deployment through the AUDIENCE Worker var.
 */
export const DEFAULT_AUDIENCE = "techlib";

export type PrincipalKind = "master" | "hlt" | "key";

export interface Principal {
  kind: PrincipalKind;
  /** the key's owner (Access users.id) for sk- keys */
  userId?: string;
  /** the key's own id for sk- keys — precise audit trail */
  keyId?: string;
  /** the service the sk- key was issued for ("" when the key carries none) */
  audience?: string;
  scopes: string[];
}

/** Audit label for logs: the person, else the key, else the credential class. */
export function actorOf(p: Principal): string {
  return p.userId ?? p.keyId ?? p.kind;
}

export type AudienceVerdict =
  | { ok: true }
  | { ok: false; reason: "mismatch" | "missing"; expected: string; actual?: string };

/**
 * Audience check — a key issued for another service (or for none) must not open this API.
 *
 * Missing/empty audience is REJECTED (2026-11-02): hilir Access now refuses to issue a key
 * without an audience, and every pre-existing key was revoked during the scope restructure, so
 * there is no legacy population to protect. A key that does not name its service is treated as
 * an error, not as an implicit "any service".
 */
export function audienceVerdict(p: Principal, expected: string = DEFAULT_AUDIENCE): AudienceVerdict {
  if (p.kind !== "key") return { ok: true }; // master key and hlt_ keys are not Access keys
  const actual = (p.audience ?? "").trim();
  if (actual.length === 0) return { ok: false, reason: "missing", expected };
  if (actual !== expected) return { ok: false, reason: "mismatch", expected, actual };
  return { ok: true };
}

function json(body: unknown, status: number): Response {
  return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
}

/**
 * The gate. null = allowed.
 * - no usable credential → 401 (no scope detail, no enumeration)
 * - authenticated principal without catalog:read → 403 "forbidden" naming the scope
 *   (any authenticated principal denied here gets the same shape)
 */
export function authorize(p: Principal | null, required: string = HILIR_SCOPE): Response | null {
  if (!p) return json({ error: "missing or wrong API key" }, 401);
  if (!p.scopes.includes(required)) return json({ error: "forbidden", required }, 403);
  return null;
}

/** One-line JSON audit record for Workers logs — identity, never credentials. */
export function auditLine(event: string, p: Principal | null, extra: Record<string, unknown> = {}): string {
  return JSON.stringify({
    event,
    actor: p ? actorOf(p) : null,
    kind: p?.kind ?? null,
    keyId: p?.keyId ?? null,
    audience: p?.audience ?? null,
    ...extra,
  });
}
