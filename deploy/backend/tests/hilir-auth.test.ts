/**
 * The re-synced hilir Access consumer module (src/hilir-auth.ts, upstream b5ed348).
 *
 * Covers the additions this re-sync carries — sk- keys now expose their owner (userId) and the
 * key's own id (keyId) — plus proof the JWT path is unchanged.
 *
 * Run: cd deploy/backend && npm test   (node --test, type stripping — no build step)
 */
import assert from "node:assert/strict";
import { test } from "node:test";

import { createHilirAuth, createKeyChecker, verifyHilirJwt } from "../src/hilir-auth.ts";

type Binding = Parameters<typeof createKeyChecker>[0]["binding"];

/** A Service Binding that answers one introspection body and counts the hops. */
function fakeBinding(body: unknown, status = 200) {
  let calls = 0;
  const binding = {
    fetch: async () => {
      calls += 1;
      return new Response(JSON.stringify(body), { status, headers: { "Content-Type": "application/json" } });
    },
  } as unknown as Binding;
  return { binding, calls: () => calls };
}

const INTROSPECTED = {
  active: true,
  key_id: "key-abc",
  user_id: "user-xyz",
  scopes: ["catalog:read"],
  audience: "techlib",
};

test("checkKey: carries the key's owner and id from introspection", async () => {
  const { binding } = fakeBinding(INTROSPECTED);
  const check = createKeyChecker({ binding, internalToken: "t" });
  const result = await check("sk-test-key");
  assert.ok(result);
  assert.equal(result.active, true);
  assert.deepEqual(result.scopes, ["catalog:read"]);
  assert.equal(result.userId, "user-xyz");
  assert.equal(result.keyId, "key-abc");
  assert.equal(result.audience, "techlib");
});

test("checkKey: non sk- credentials are not this module's business", async () => {
  const { binding, calls } = fakeBinding(INTROSPECTED);
  const check = createKeyChecker({ binding, internalToken: "t" });
  assert.equal(await check("Bearer-something"), null);
  assert.equal(calls(), 0);
});

test("checkKey: results are cached for the TTL (revocation lands within one TTL)", async () => {
  const { binding, calls } = fakeBinding(INTROSPECTED);
  const check = createKeyChecker({ binding, internalToken: "t", cacheTtlMs: 60_000 });
  await check("sk-same");
  await check("sk-same");
  assert.equal(calls(), 1);
  await check("sk-other");
  assert.equal(calls(), 2);
});

test("checkKey: an inactive key stays inactive", async () => {
  const { binding } = fakeBinding({ active: false }, 200);
  const check = createKeyChecker({ binding, internalToken: "t" });
  const result = await check("sk-revoked");
  assert.ok(result);
  assert.equal(result.active, false);
});

test("checkKey: a failing introspection throws (the Worker fails closed)", async () => {
  const { binding } = fakeBinding({ error: "upstream down" }, 503);
  const check = createKeyChecker({ binding, internalToken: "t" });
  await assert.rejects(() => check("sk-any"));
});

test("createHilirAuth: sk- keys authenticate as kind=key with identity", async () => {
  const { binding } = fakeBinding(INTROSPECTED);
  const auth = createHilirAuth({
    issuer: "https://access.test", audience: "techlib-api", binding, internalToken: "t",
  });
  const principal = await auth(new Request("https://api.test/api/stats", {
    headers: { Authorization: "Bearer sk-test-key" },
  }));
  assert.deepEqual(principal, {
    kind: "key", userId: "user-xyz", keyId: "key-abc", scopes: ["catalog:read"],
  });
});

test("createHilirAuth: no binding means machines cannot authenticate, JWTs still can", async () => {
  const auth = createHilirAuth({ issuer: "https://access.test", audience: "techlib-api" });
  assert.equal(await auth(new Request("https://api.test/", { headers: { Authorization: "Bearer sk-x" } })), null);
});

test("createHilirAuth: an inactive key is rejected", async () => {
  const { binding } = fakeBinding({ active: false });
  const auth = createHilirAuth({ issuer: "https://access.test", audience: "techlib-api", binding, internalToken: "t" });
  assert.equal(await auth(new Request("https://api.test/", { headers: { Authorization: "Bearer sk-x" } })), null);
});

// ---------------------------------------------------------------------------
// JWT path — unchanged by the re-sync: local ES256 verification, iss/aud/exp enforced
// ---------------------------------------------------------------------------

const enc = new TextEncoder();
const b64u = (bytes: Uint8Array) => Buffer.from(bytes).toString("base64url");
const KID = "test-kid";

const keypair = (await crypto.subtle.generateKey({ name: "ECDSA", namedCurve: "P-256" }, true, ["sign", "verify"])) as CryptoKeyPair;
const publicJwk = { ...(await crypto.subtle.exportKey("jwk", keypair.publicKey)), kid: KID, alg: "ES256", use: "sig" };

// The module caches the JWKS for 5 min, so the stub must serve one stable key set.
const realFetch = globalThis.fetch;
globalThis.fetch = (async (input: RequestInfo | URL) => {
  const url = String(input);
  if (url.endsWith("/jwks.json")) {
    return new Response(JSON.stringify({ keys: [publicJwk] }), { status: 200 });
  }
  throw new Error(`unexpected fetch: ${url}`);
}) as typeof fetch;

async function mintToken(claims: Record<string, unknown>): Promise<string> {
  const header = b64u(enc.encode(JSON.stringify({ alg: "ES256", kid: KID, typ: "JWT" })));
  const payload = b64u(enc.encode(JSON.stringify(claims)));
  const signature = await crypto.subtle.sign(
    { name: "ECDSA", hash: "SHA-256" }, keypair.privateKey, enc.encode(`${header}.${payload}`),
  );
  return `${header}.${payload}.${b64u(new Uint8Array(signature))}`;
}

const now = Math.floor(Date.now() / 1000);
const claims = {
  iss: "https://access.test", sub: "user-1", aud: "techlib-api",
  scope: "catalog:read", exp: now + 300, iat: now,
};
const verify = (token: string) => verifyHilirJwt(token, { issuer: "https://access.test", audience: "techlib-api" });

test("JWT: a valid ES256 token verifies (unchanged path)", async () => {
  const verified = await verify(await mintToken(claims));
  assert.ok(verified);
  assert.equal(verified.sub, "user-1");
  assert.equal(verified.scope, "catalog:read");
});

test("JWT: wrong audience is rejected", async () => {
  assert.equal(await verify(await mintToken({ ...claims, aud: "other-api" })), null);
});

test("JWT: an expired token is rejected", async () => {
  assert.equal(await verify(await mintToken({ ...claims, exp: now - 30 })), null);
});

test("JWT: a tampered signature is rejected", async () => {
  const token = await mintToken(claims);
  const [h, , s] = token.split(".");
  const other = await mintToken({ ...claims, sub: "user-2" });
  const tampered = `${h}.${other.split(".")[1]}.${s}`;
  assert.equal(await verify(tampered), null);
});

test("JWT: authenticate() returns the subject for human sessions", async () => {
  const auth = createHilirAuth({ issuer: "https://access.test", audience: "techlib-api" });
  const principal = await auth(new Request("https://api.test/", {
    headers: { Authorization: `Bearer ${await mintToken(claims)}` },
  }));
  assert.deepEqual(principal, { kind: "jwt", userId: "user-1", scopes: ["catalog:read"] });
});

test.after(() => {
  globalThis.fetch = realFetch;
});
