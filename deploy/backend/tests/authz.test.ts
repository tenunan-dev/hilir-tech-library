/**
 * Authorization rules for the backend Worker (src/authz.ts), tested without the Workers runtime.
 *
 * Run: cd deploy/backend && npm test   (node --test, type stripping — no build step)
 */
import assert from "node:assert/strict";
import { test } from "node:test";

import { HILIR_SCOPE, actorOf, auditLine, audienceVerdict, authorize, type Principal } from "../src/authz.ts";

const key = (over: Partial<Principal> = {}): Principal => ({ kind: "key", scopes: [HILIR_SCOPE], ...over });

test("authorize: no usable credential → 401", async () => {
  const res = authorize(null);
  assert.ok(res);
  assert.equal(res.status, 401);
  assert.equal((await res.json()).error, "missing or wrong API key");
});

test("authorize: a key without catalog:read → 403 forbidden naming the scope", async () => {
  const res = authorize(key({ scopes: ["estimate:run"] }));
  assert.ok(res);
  assert.equal(res.status, 403);
  const body = await res.json();
  assert.equal(body.error, "forbidden");
  assert.equal(body.required, "catalog:read");
});

test("authorize: any key carrying catalog:read passes (reads only)", () => {
  assert.equal(authorize(key()), null);
  assert.equal(authorize(key({ scopes: ["catalog:read", "estimate:run"] })), null);
});

test("authorize: every authenticated class is denied as forbidden, never unauthorized", async () => {
  for (const kind of ["master", "hlt", "key"] as const) {
    const res = authorize({ kind, scopes: [] });
    assert.ok(res);
    assert.equal(res.status, 403);
    assert.equal((await res.json()).error, "forbidden");
  }
});

test("audienceVerdict: a key issued for this service passes", () => {
  assert.deepEqual(audienceVerdict(key({ audience: "techlib" })), { ok: true });
});

test("audienceVerdict: a key issued for another service is rejected", () => {
  const verdict = audienceVerdict(key({ audience: "tlea-api" }));
  assert.equal(verdict.ok, false);
  assert.deepEqual(verdict.ok === false ? { reason: verdict.reason, expected: verdict.expected, actual: verdict.actual } : null,
                   { reason: "mismatch", expected: "techlib", actual: "tlea-api" });
});

test("audienceVerdict: missing/empty audience is rejected", () => {
  for (const audience of ["", undefined, "  "]) {
    const verdict = audienceVerdict(key({ audience }));
    assert.equal(verdict.ok, false);
    assert.equal(verdict.ok === false ? verdict.reason : null, "missing");
    assert.equal(verdict.ok === false ? verdict.expected : null, "techlib");
  }
});

test("audienceVerdict: the expected audience is configurable", () => {
  assert.equal(audienceVerdict(key({ audience: "techlib" }), "techlib").ok, true);
  assert.equal(audienceVerdict(key({ audience: "techlib" }), "other-service").ok, false);
});

test("audienceVerdict: master and hlt_ credentials are not Access keys", () => {
  assert.deepEqual(audienceVerdict({ kind: "master", scopes: [HILIR_SCOPE], audience: "" }), { ok: true });
  assert.deepEqual(audienceVerdict({ kind: "hlt", scopes: [HILIR_SCOPE] }), { ok: true });
});

test("actorOf: userId first, then keyId, then the credential class", () => {
  assert.equal(actorOf(key({ userId: "user-1", keyId: "key-1" })), "user-1");
  assert.equal(actorOf(key({ keyId: "key-1" })), "key-1");
  assert.equal(actorOf({ kind: "master", scopes: [] }), "master");
});

test("auditLine: names the actor and never carries a credential", () => {
  const line = auditLine("request", key({ userId: "user-1", keyId: "key-1", audience: "techlib" }), { path: "/api/stats" });
  assert.deepEqual(JSON.parse(line), {
    event: "request", actor: "user-1", kind: "key", keyId: "key-1", audience: "techlib", path: "/api/stats",
  });
  assert.equal(/sk-|bearer|authorization/i.test(line), false);
});
