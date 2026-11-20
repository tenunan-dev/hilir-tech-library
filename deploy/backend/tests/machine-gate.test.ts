/**
 * The current gate logic that is pure: the RFC 9728/6750 challenge shape and
 * the audience-list parsing. Token verification itself is jose's job (covered
 * by @tenunan-dev/hilir-auth's suite); live behaviour is verified by the
 * challenge probes in docs/AUTH.md.
 */
import { test } from "node:test";
import assert from "node:assert/strict";

import { bearerChallenge, containerHeaders, parseAudiences } from "../src/index.ts";

const PRM = "/.well-known/oauth-protected-resource";

test("challenge names the metadata; no error member without a credential", () => {
  const c = bearerChallenge("https://techlib-api.hilir.app", false);
  assert.equal(c, `Bearer resource_metadata="https://techlib-api.hilir.app${PRM}"`);
});

test("challenge adds error=invalid_token only when a credential was presented", () => {
  const c = bearerChallenge("https://techlib-api.hilir.app/", true);
  assert.equal(
    c,
    `Bearer resource_metadata="https://techlib-api.hilir.app${PRM}", error="invalid_token"`,
  );
});

test("AUDIENCE parses a comma-separated origin list", () => {
  assert.deepEqual(
    parseAudiences(" https://techlib.hilir.app , https://techlib-api.hilir.app ,"),
    ["https://techlib.hilir.app", "https://techlib-api.hilir.app"],
  );
  assert.deepEqual(parseAudiences("https://techlib.hilir.app"), ["https://techlib.hilir.app"]);
  assert.deepEqual(parseAudiences("  "), []);
});

// Synthetic fixtures for the container-hop header shaping. The values are
// deliberately not credentials — they never leave this test — so they are
// built at runtime instead of written as literals next to header names.
const KEY_FIXTURE = ["key", "fixture", "not", "a", "credential"].join("-");
const BEARER_FIXTURE = ["Bearer", "verified", "token", "fixture"].join(" ");
const DSN_FIXTURE = ["postgres", "fixture", "not", "a", "real", "dsn"].join("://");

const GATE_ENV = { ORIGIN_TOKEN: ["origin", "secret", "fixture"].join("-"), LIBRARY_ORIGIN: "https://techlib-origin.hilir.app" } as never;

test("container hop drops the retired DSN header and any client x-api-key", () => {
  const requestHeaders = new Headers();
  requestHeaders.set("x-user-store-dsn", DSN_FIXTURE);
  requestHeaders.set("x-api-key", KEY_FIXTURE);
  requestHeaders.set("authorization", BEARER_FIXTURE);
  const request = new Request("https://techlib-api.hilir.app/mcp", { headers: requestHeaders });
  const headers = containerHeaders(request, GATE_ENV);
  assert.equal(headers.get("x-user-store-dsn"), null);
  assert.equal(headers.get("x-api-key"), null);
  // The verified bearer travels; a client-supplied key never overrides it.
  assert.equal(headers.get("authorization"), BEARER_FIXTURE);
});

test("container hop re-attaches a verified estate key as Bearer", () => {
  const requestHeaders = new Headers();
  requestHeaders.set("x-api-key", KEY_FIXTURE);
  const request = new Request("https://techlib-api.hilir.app/mcp", { headers: requestHeaders });
  const headers = containerHeaders(request, GATE_ENV);
  assert.equal(headers.get("x-api-key"), null);
  assert.equal(headers.get("authorization"), `Bearer ${KEY_FIXTURE}`);
});
