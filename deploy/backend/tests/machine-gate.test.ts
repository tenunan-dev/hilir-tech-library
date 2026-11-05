/**
 * The current gate logic that is pure: the RFC 9728/6750 challenge shape and
 * the audience-list parsing. Token verification itself is jose's job (covered
 * by @tenunan-dev/hilir-auth's suite); live behaviour is verified by the
 * challenge probes in docs/AUTH.md.
 */
import { test } from "node:test";
import assert from "node:assert/strict";

import { bearerChallenge, parseAudiences } from "../src/index.ts";

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
