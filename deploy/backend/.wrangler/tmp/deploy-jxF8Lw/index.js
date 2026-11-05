var __defProp = Object.defineProperty;
var __name = (target, value) => __defProp(target, "name", { value, configurable: true });

// node_modules/jose/dist/webapi/lib/buffer_utils.js
var encoder = new TextEncoder();
var decoder = new TextDecoder();
var strictDecoder = new TextDecoder("utf-8", { fatal: true });
var UINT32_RANGE = 2 ** 32;
function concat(...buffers) {
  const size = buffers.reduce((acc, { length }) => acc + length, 0), buf = new Uint8Array(size);
  let i = 0;
  for (const buffer of buffers)
    buf.set(buffer, i), i += buffer.length;
  return buf;
}
__name(concat, "concat");
var NON_ASCII = /[^\x00-\x7f]/;
function encode(string) {
  if (typeof string == "string" && string.length >= 128) {
    if (NON_ASCII.test(string))
      throw new TypeError("non-ASCII string encountered in encode()");
    return encoder.encode(string);
  }
  const bytes = new Uint8Array(string.length);
  for (let i = 0; i < string.length; i++) {
    const code = string.charCodeAt(i);
    if (code > 127)
      throw new TypeError("non-ASCII string encountered in encode()");
    bytes[i] = code;
  }
  return bytes;
}
__name(encode, "encode");
function decodeBase64(encoded, url = false) {
  if (Uint8Array.fromBase64)
    return Uint8Array.fromBase64(encoded, { alphabet: url ? "base64url" : "base64" });
  if (url) {
    if (encoded.includes("+") || encoded.includes("/"))
      throw new TypeError("Invalid base64url");
    encoded = encoded.replace(/-/g, "+").replace(/_/g, "/");
  }
  const binary = atob(encoded), bytes = new Uint8Array(binary.length);
  for (let i = 0; i < binary.length; i++)
    bytes[i] = binary.charCodeAt(i);
  return bytes;
}
__name(decodeBase64, "decodeBase64");

// node_modules/jose/dist/webapi/util/errors.js
var JOSEError = class extends Error {
  static {
    __name(this, "JOSEError");
  }
  static code = "ERR_JOSE_GENERIC";
  code = "ERR_JOSE_GENERIC";
  constructor(message2, options) {
    super(message2, options), this.name = this.constructor.name, Error.captureStackTrace?.(this, this.constructor);
  }
};
var JWTClaimValidationFailed = class extends JOSEError {
  static {
    __name(this, "JWTClaimValidationFailed");
  }
  static code = "ERR_JWT_CLAIM_VALIDATION_FAILED";
  code = "ERR_JWT_CLAIM_VALIDATION_FAILED";
  claim;
  reason;
  payload;
  constructor(message2, payload, claim = "unspecified", reason = "unspecified") {
    super(message2, { cause: { claim, reason, payload } }), this.claim = claim, this.reason = reason, this.payload = payload;
  }
};
var JWTExpired = class extends JOSEError {
  static {
    __name(this, "JWTExpired");
  }
  static code = "ERR_JWT_EXPIRED";
  code = "ERR_JWT_EXPIRED";
  claim;
  reason;
  payload;
  constructor(message2, payload, claim = "unspecified", reason = "unspecified") {
    super(message2, { cause: { claim, reason, payload } }), this.claim = claim, this.reason = reason, this.payload = payload;
  }
};
var JOSEAlgNotAllowed = class extends JOSEError {
  static {
    __name(this, "JOSEAlgNotAllowed");
  }
  static code = "ERR_JOSE_ALG_NOT_ALLOWED";
  code = "ERR_JOSE_ALG_NOT_ALLOWED";
};
var JOSENotSupported = class extends JOSEError {
  static {
    __name(this, "JOSENotSupported");
  }
  static code = "ERR_JOSE_NOT_SUPPORTED";
  code = "ERR_JOSE_NOT_SUPPORTED";
};
var JWSInvalid = class extends JOSEError {
  static {
    __name(this, "JWSInvalid");
  }
  static code = "ERR_JWS_INVALID";
  code = "ERR_JWS_INVALID";
};
var JWTInvalid = class extends JOSEError {
  static {
    __name(this, "JWTInvalid");
  }
  static code = "ERR_JWT_INVALID";
  code = "ERR_JWT_INVALID";
};
var JWKSInvalid = class extends JOSEError {
  static {
    __name(this, "JWKSInvalid");
  }
  static code = "ERR_JWKS_INVALID";
  code = "ERR_JWKS_INVALID";
};
var JWKSNoMatchingKey = class extends JOSEError {
  static {
    __name(this, "JWKSNoMatchingKey");
  }
  static code = "ERR_JWKS_NO_MATCHING_KEY";
  code = "ERR_JWKS_NO_MATCHING_KEY";
  constructor(message2 = "no applicable key found in the JSON Web Key Set", options) {
    super(message2, options);
  }
};
var JWKSMultipleMatchingKeys = class extends JOSEError {
  static {
    __name(this, "JWKSMultipleMatchingKeys");
  }
  [Symbol.asyncIterator] = async function* () {
  };
  static code = "ERR_JWKS_MULTIPLE_MATCHING_KEYS";
  code = "ERR_JWKS_MULTIPLE_MATCHING_KEYS";
  constructor(message2 = "multiple matching keys found in the JSON Web Key Set", options) {
    super(message2, options);
  }
};
var JWKSTimeout = class extends JOSEError {
  static {
    __name(this, "JWKSTimeout");
  }
  static code = "ERR_JWKS_TIMEOUT";
  code = "ERR_JWKS_TIMEOUT";
  constructor(message2 = "request timed out", options) {
    super(message2, options);
  }
};
var JWSSignatureVerificationFailed = class extends JOSEError {
  static {
    __name(this, "JWSSignatureVerificationFailed");
  }
  static code = "ERR_JWS_SIGNATURE_VERIFICATION_FAILED";
  code = "ERR_JWS_SIGNATURE_VERIFICATION_FAILED";
  constructor(message2 = "signature verification failed", options) {
    super(message2, options);
  }
};

// node_modules/jose/dist/webapi/util/base64url.js
var invalid = "The input to be decoded is not correctly encoded.";
function decode(input) {
  try {
    return decodeBase64(typeof input == "string" ? input : decoder.decode(input), true);
  } catch (cause) {
    throw new TypeError(invalid, { cause });
  }
}
__name(decode, "decode");

// node_modules/jose/dist/webapi/lib/validate.js
function isObject(input) {
  if (typeof input != "object" || input === null || Object.prototype.toString.call(input) !== "[object Object]")
    return false;
  const prototype = Object.getPrototypeOf(input);
  return prototype === null || Object.getPrototypeOf(prototype) === null;
}
__name(isObject, "isObject");
function isJwkSet(input) {
  return isObject(input) && Array.isArray(input.keys) && Array.from(input.keys).every(isObject);
}
__name(isJwkSet, "isJwkSet");
function isDisjoint(...headers) {
  const parameters = /* @__PURE__ */ new Set();
  for (const header of headers)
    if (header)
      for (const parameter of Object.keys(header)) {
        if (parameters.has(parameter))
          return false;
        parameters.add(parameter);
      }
  return true;
}
__name(isDisjoint, "isDisjoint");
function decodeBase64url(value, label, ErrorClass) {
  try {
    return decode(value);
  } catch (cause) {
    throw new ErrorClass(`Failed to base64url decode the ${label}`, { cause });
  }
}
__name(decodeBase64url, "decodeBase64url");
function encodeAsciiMember(value, label, ErrorClass) {
  try {
    return encode(value);
  } catch (cause) {
    throw new ErrorClass(`The ${label} is not a valid base64url string`, { cause });
  }
}
__name(encodeAsciiMember, "encodeAsciiMember");
function parseJoseHeader(encodedProtectedHeader, ErrorClass, message2) {
  let parsed;
  try {
    parsed = JSON.parse(strictDecoder.decode(decode(encodedProtectedHeader)));
  } catch (cause) {
    throw new ErrorClass(message2, { cause });
  }
  if (!isObject(parsed))
    throw new ErrorClass(message2);
  return parsed;
}
__name(parseJoseHeader, "parseJoseHeader");
var JWS_RECOGNIZED = { __proto__: null, b64: true };
function validateAlgorithms(option, algorithms) {
  if (algorithms !== void 0 && (!Array.isArray(algorithms) || algorithms.some((s) => typeof s != "string")))
    throw new TypeError(`"${option}" option must be an array of strings`);
  return algorithms === void 0 ? void 0 : new Set(algorithms);
}
__name(validateAlgorithms, "validateAlgorithms");
function validateCrit(Err, recognizedDefault, recognizedOption, protectedHeader, joseHeader) {
  if (joseHeader.crit !== void 0 && protectedHeader?.crit === void 0)
    throw new Err('"crit" (Critical) Header Parameter MUST be integrity protected');
  if (!protectedHeader || protectedHeader.crit === void 0)
    return [];
  if (!Array.isArray(protectedHeader.crit) || protectedHeader.crit.length === 0 || protectedHeader.crit.some((input) => typeof input != "string" || input.length === 0))
    throw new Err('"crit" (Critical) Header Parameter MUST be an array of non-empty strings when present');
  const recognized = recognizedOption === void 0 ? recognizedDefault : { __proto__: null, ...recognizedOption, ...recognizedDefault };
  for (const parameter of protectedHeader.crit) {
    if (!(parameter in recognized))
      throw new JOSENotSupported(`Extension Header Parameter "${parameter}" is not recognized`);
    if (!Object.hasOwn(joseHeader, parameter) || joseHeader[parameter] === void 0)
      throw new Err(`Extension Header Parameter "${parameter}" is missing`);
    if (recognized[parameter] && (!Object.hasOwn(protectedHeader, parameter) || protectedHeader[parameter] === void 0))
      throw new Err(`Extension Header Parameter "${parameter}" MUST be integrity protected`);
  }
  return protectedHeader.crit;
}
__name(validateCrit, "validateCrit");
function validateB64(protectedHeader, extensions) {
  if (extensions.includes("b64")) {
    const b64 = protectedHeader.b64;
    if (typeof b64 != "boolean")
      throw new JWSInvalid('The "b64" (base64url-encode payload) Header Parameter must be a boolean');
    return b64;
  }
  return true;
}
__name(validateB64, "validateB64");

// node_modules/jose/dist/webapi/lib/key.js
var tag = /* @__PURE__ */ __name((key) => key[Symbol.toStringTag], "tag");
var jwkMatchesOp = /* @__PURE__ */ __name((entry, key, usage) => {
  const { alg } = entry;
  if (key.use !== void 0) {
    const expected = usage === "sign" || usage === "verify" ? "sig" : "enc";
    if (key.use !== expected)
      throw new TypeError(`Invalid key for this operation, its "use" must be "${expected}" when present`);
  }
  if (key.alg !== void 0 && key.alg !== alg)
    throw new TypeError(`Invalid key for this operation, its "alg" must be "${alg}" when present`);
  if (Array.isArray(key.key_ops)) {
    const expectedKeyOp = usage === "encrypt" || usage === "decrypt" ? entry.ops?.[usage === "encrypt" ? 0 : 1] : usage;
    if (expectedKeyOp && !key.key_ops.includes(expectedKeyOp))
      throw new TypeError(`Invalid key for this operation, its "key_ops" must include "${expectedKeyOp}" when present`);
  }
}, "jwkMatchesOp");
async function prepareKey(entry, key, usage) {
  const { alg, secret } = entry, requiresPrivateKey = usage === "decrypt" || usage === "sign";
  if (secret && key instanceof Uint8Array)
    return key;
  let normalized, keyObject;
  if (isObject(key)) {
    if (normalized = normalizeJwk(key), typeof normalized.kty != "string")
      throw invalidKeyType(alg, key, secret);
    if (!(secret ? normalized.kty === "oct" && typeof normalized.k == "string" : normalized.kty !== "oct" && (requiresPrivateKey ? normalized.kty === "AKP" && typeof normalized.priv == "string" || typeof normalized.d == "string" : normalized.d === void 0 && normalized.priv === void 0)))
      throw new TypeError(secret ? 'JSON Web Key for symmetric algorithms must have JWK "kty" (Key Type) equal to "oct" and the JWK "k" (Key Value) present' : `JSON Web Key for this operation must be a ${requiresPrivateKey ? "private" : "public"} JWK`);
    if (jwkMatchesOp(entry, normalized, usage), normalized.kty === "oct")
      return decode(normalized.k);
    if (!Object.isFrozen(key)) {
      const { key_ops } = key;
      Array.isArray(key_ops) && Object.freeze(key_ops), Object.freeze(key);
    }
  } else {
    if (!isKeyLike(key))
      throw invalidKeyType(alg, key, secret);
    const expectedType = secret ? "secret" : requiresPrivateKey ? "private" : "public";
    if (key.type !== expectedType && (secret || ["secret", "public", "private"].includes(key.type)))
      throw new TypeError(`${tag(key)} instances must be of type "${expectedType}" for the ${alg} algorithm`);
    if (isCryptoKey(key))
      return key;
    if (keyObject = key, keyObject.type === "secret")
      return keyObject.export();
  }
  cache ||= /* @__PURE__ */ new WeakMap();
  const cacheKey = key;
  let cached = cache.get(cacheKey);
  if (cached?.[alg])
    return cached[alg];
  if (cached || cache.set(cacheKey, cached = {}), keyObject && typeof keyObject.toCryptoKey == "function") {
    const isPublic = keyObject.type === "public", crv = nist[keyObject.asymmetricKeyDetails?.namedCurve], params = entry.resolve?.({ crv, asymmetricKeyType: keyObject.asymmetricKeyType }) ?? entry.subtle;
    return cached[alg] = keyObject.toCryptoKey(params, isPublic, entry.usages[isPublic ? 0 : 1]);
  }
  return normalized ??= keyObject.export({ format: "jwk" }), normalized.alg = alg, cached[alg] = await jwkToKey(entry, normalized);
}
__name(prepareKey, "prepareKey");
var cache;
var nist = {
  __proto__: null,
  prime256v1: "P-256",
  secp384r1: "P-384",
  secp521r1: "P-521"
};
var isCryptoKey = /* @__PURE__ */ __name((key) => {
  if (key?.[Symbol.toStringTag] === "CryptoKey")
    return true;
  try {
    return key instanceof CryptoKey;
  } catch {
    return false;
  }
}, "isCryptoKey");
var isKeyObject = /* @__PURE__ */ __name((key) => key?.[Symbol.toStringTag] === "KeyObject", "isKeyObject");
var isKeyLike = /* @__PURE__ */ __name((key) => isCryptoKey(key) || isKeyObject(key), "isKeyLike");
function message(msg, actual, ...types) {
  if (types.length > 2) {
    const last = types.pop();
    msg += `one of type ${types.join(", ")}, or ${last}.`;
  } else types.length === 2 ? msg += `one of type ${types[0]} or ${types[1]}.` : msg += `of type ${types[0]}.`;
  return actual == null ? msg += ` Received ${actual}` : typeof actual == "function" && actual.name ? msg += ` Received function ${actual.name}` : typeof actual == "object" && actual != null && actual.constructor?.name && (msg += ` Received an instance of ${actual.constructor.name}`), msg;
}
__name(message, "message");
function invalidKeyType(alg, actual, secret) {
  const types = ["CryptoKey", "KeyObject", "JSON Web Key"];
  return secret && types.push("Uint8Array"), new TypeError(message(`Key for the ${alg} algorithm must be `, actual, ...types));
}
__name(invalidKeyType, "invalidKeyType");
var unusable = /* @__PURE__ */ __name((name, prop = "algorithm.name") => new TypeError(`CryptoKey does not support this operation, its ${prop} must be ${name}`), "unusable");
function checkUsage(key, usage) {
  if (usage && !key.usages.includes(usage))
    throw new TypeError(`CryptoKey does not support this operation, its usages must include ${usage}.`);
}
__name(checkUsage, "checkUsage");
function checkModulusLength(alg, key) {
  const { modulusLength } = key.algorithm;
  if (typeof modulusLength != "number" || modulusLength < 2048)
    throw new TypeError(`${alg} requires key modulusLength to be 2048 bits or larger`);
}
__name(checkModulusLength, "checkModulusLength");
function checkCryptoKey(key, expected, usage) {
  const algorithm = key.algorithm;
  if (algorithm.name !== expected.name)
    throw unusable(expected.name);
  if (expected.hash && algorithm.hash?.name !== expected.hash)
    throw unusable(expected.hash, "algorithm.hash");
  if (expected.namedCurve && algorithm.namedCurve !== expected.namedCurve)
    throw unusable(expected.namedCurve, "algorithm.namedCurve");
  if (expected.length !== void 0 && algorithm.length !== expected.length)
    throw unusable(expected.length, "algorithm.length");
  checkUsage(key, usage);
}
__name(checkCryptoKey, "checkCryptoKey");
function snapshotJwk(jwk) {
  return { __proto__: null, ...jwk };
}
__name(snapshotJwk, "snapshotJwk");
function normalizeJwk(jwk) {
  const normalized = snapshotJwk(jwk);
  if (normalized.ext !== void 0 && typeof normalized.ext != "boolean")
    throw new TypeError('"ext" (Extractable) Parameter must be a boolean');
  if (normalized.key_ops !== void 0) {
    const value = normalized.key_ops, keyOps = Array.isArray(value) ? [...value] : void 0;
    if (!keyOps || keyOps.some((operation) => typeof operation != "string") || new Set(keyOps).size !== keyOps.length)
      throw new TypeError('"key_ops" (Key Operations) Parameter must be an array of unique strings');
    normalized.key_ops = keyOps;
  }
  return normalized;
}
__name(normalizeJwk, "normalizeJwk");
async function jwkToKey(entry, jwk, extractable) {
  if (!entry.kty.includes(jwk.kty))
    throw new JOSENotSupported('Invalid or unsupported JWK "alg" (Algorithm) Parameter value');
  const algorithm = entry.resolve?.({ kty: jwk.kty, crv: jwk.crv }) ?? entry.subtle, isPrivate = !!(jwk.d || jwk.priv), keyData = { ...jwk, ext: extractable ?? jwk.ext };
  return keyData.kty !== "AKP" && delete keyData.alg, delete keyData.use, crypto.subtle.importKey("jwk", keyData, algorithm, keyData.ext ?? !isPrivate, jwk.key_ops ?? entry.usages[isPrivate ? 1 : 0]);
}
__name(jwkToKey, "jwkToKey");
async function rawKey(key, expected, usage, extractable = false) {
  return key instanceof Uint8Array && (key = await crypto.subtle.importKey("raw", key, expected, extractable, [usage])), checkCryptoKey(key, expected, usage), key;
}
__name(rawKey, "rawKey");

// node_modules/jose/dist/webapi/lib/key_descriptor.js
function table(entries) {
  const out = { __proto__: null };
  for (const alg in entries)
    out[alg] = { ...entries[alg], alg };
  return out;
}
__name(table, "table");

// node_modules/jose/dist/webapi/lib/jws_algorithms.js
var sig = [["verify"], ["sign"]];
function hmac(bits) {
  const subtle = { name: "HMAC", hash: `SHA-${bits}` };
  return { kty: ["oct"], secret: true, subtle, signing: subtle, usages: sig };
}
__name(hmac, "hmac");
function rsa(bits, saltLength) {
  const subtle = { name: saltLength ? "RSA-PSS" : "RSASSA-PKCS1-v1_5", hash: `SHA-${bits}` };
  return {
    kty: ["RSA"],
    subtle,
    signing: saltLength ? { ...subtle, saltLength } : subtle,
    usages: sig,
    minRsaBits: 2048
  };
}
__name(rsa, "rsa");
function ecdsa(crv, bits) {
  return {
    kty: ["EC"],
    crv,
    subtle: { name: "ECDSA", namedCurve: crv },
    signing: { name: "ECDSA", hash: `SHA-${bits}` },
    usages: sig
  };
}
__name(ecdsa, "ecdsa");
function eddsa() {
  const subtle = { name: "Ed25519" };
  return {
    kty: ["OKP"],
    crv: "Ed25519",
    subtle,
    signing: subtle,
    usages: sig
  };
}
__name(eddsa, "eddsa");
function mldsa(parameterSet) {
  const subtle = { name: `ML-DSA-${parameterSet}` };
  return {
    kty: ["AKP"],
    subtle,
    signing: subtle,
    usages: sig
  };
}
__name(mldsa, "mldsa");
var JWS = table({
  HS256: hmac(256),
  HS384: hmac(384),
  HS512: hmac(512),
  RS256: rsa(256),
  RS384: rsa(384),
  RS512: rsa(512),
  PS256: rsa(256, 32),
  PS384: rsa(384, 48),
  PS512: rsa(512, 64),
  ES256: ecdsa("P-256", 256),
  ES384: ecdsa("P-384", 384),
  ES512: ecdsa("P-521", 512),
  EdDSA: eddsa(),
  Ed25519: eddsa(),
  "ML-DSA-44": mldsa(44),
  "ML-DSA-65": mldsa(65),
  "ML-DSA-87": mldsa(87)
});
function jwsAlgorithm(alg) {
  const entry = typeof alg == "string" ? JWS[alg] : void 0;
  if (!entry)
    throw new JOSENotSupported(`alg ${alg} is not supported either by JOSE or your javascript runtime`);
  return entry;
}
__name(jwsAlgorithm, "jwsAlgorithm");

// node_modules/jose/dist/webapi/lib/jws_verify.js
function prepareVerify(options) {
  return [options && validateAlgorithms("algorithms", options.algorithms), options?.crit];
}
__name(prepareVerify, "prepareVerify");
function parseProtectedHeader(encodedProtectedHeader) {
  return encodedProtectedHeader === void 0 ? {} : parseJoseHeader(encodedProtectedHeader, JWSInvalid, "JWS Protected Header is invalid");
}
__name(parseProtectedHeader, "parseProtectedHeader");
function encodeCompactUnencodedPayload(payload) {
  try {
    return encode(payload);
  } catch (cause) {
    throw new JWSInvalid("JWS Compact Serialization payload must use only ASCII characters", {
      cause
    });
  }
}
__name(encodeCompactUnencodedPayload, "encodeCompactUnencodedPayload");
async function verifySignature(jws, shared, key, encodeUnencodedPayload, parsedProtected) {
  const { protected: encodedProtectedHeader, header, payload: inputPayload } = jws, protectedHeader = parsedProtected ?? parseProtectedHeader(encodedProtectedHeader);
  if (!isDisjoint(protectedHeader, header))
    throw new JWSInvalid("JWS Protected and JWS Unprotected Header Parameter names must be disjoint");
  const joseHeader = { ...protectedHeader, ...header }, b64 = validateB64(protectedHeader, validateCrit(JWSInvalid, JWS_RECOGNIZED, shared[1], protectedHeader, joseHeader)), { alg } = joseHeader;
  if (typeof alg != "string" || !alg)
    throw new JWSInvalid('JWS "alg" (Algorithm) Header Parameter missing or invalid');
  if (shared[0] && !shared[0].has(alg))
    throw new JOSEAlgNotAllowed('"alg" (Algorithm) Header Parameter value not allowed');
  if (b64) {
    if (typeof inputPayload != "string")
      throw new JWSInvalid("JWS Payload must be a string");
  } else if (typeof inputPayload != "string" && !(inputPayload instanceof Uint8Array))
    throw new JWSInvalid("JWS Payload must be a string or an Uint8Array instance");
  const signingPayload = b64 || typeof inputPayload != "string" ? inputPayload : encodeUnencodedPayload(inputPayload);
  let resolvedKey = false;
  typeof key == "function" && (key = await key(protectedHeader, jws), resolvedKey = true);
  const entry = jwsAlgorithm(alg), signingInput = concat(encodedProtectedHeader !== void 0 ? encode(encodedProtectedHeader) : new Uint8Array(), encode("."), typeof signingPayload == "string" ? shared[2] ??= encodeAsciiMember(signingPayload, "payload", JWSInvalid) : signingPayload), signature = decodeBase64url(jws.signature, "signature", JWSInvalid), verificationKey = await prepareKey(entry, key, "verify"), cryptoKey = await rawKey(verificationKey, entry.subtle, "verify");
  entry.minRsaBits && checkModulusLength(entry.alg, cryptoKey);
  let verified = false;
  try {
    verified = await crypto.subtle.verify(entry.signing, cryptoKey, signature, signingInput);
  } catch (cause) {
    throw new JWSSignatureVerificationFailed(void 0, { cause });
  }
  if (!verified)
    throw new JWSSignatureVerificationFailed();
  const result = { payload: typeof signingPayload == "string" ? decodeBase64url(signingPayload, "payload", JWSInvalid) : signingPayload };
  return encodedProtectedHeader !== void 0 && (result.protectedHeader = protectedHeader), header !== void 0 && (result.unprotectedHeader = header), resolvedKey ? [{ ...result, key: verificationKey }, b64] : [result, b64];
}
__name(verifySignature, "verifySignature");
async function verifyCompact(jws, shared, key) {
  if (jws instanceof Uint8Array && (jws = decoder.decode(jws)), typeof jws != "string")
    throw new JWSInvalid("Compact JWS must be a string or Uint8Array");
  const { 0: protectedHeader, 1: payload, 2: signature, length } = jws.split(".");
  if (length !== 3)
    throw new JWSInvalid("Invalid Compact JWS");
  return verifySignature({ payload, protected: protectedHeader, signature }, shared, key, encodeCompactUnencodedPayload);
}
__name(verifyCompact, "verifyCompact");

// node_modules/jose/dist/webapi/lib/jwt_claims_set.js
var epoch = /* @__PURE__ */ __name((date) => Math.floor(date.getTime() / 1e3), "epoch");
var multipliers = {
  s: 1,
  m: 60,
  h: 3600,
  d: 86400,
  w: 604800,
  y: 31557600
};
var REGEX = /^(\+|\-)? ?(\d+|\d+\.\d+) ?(seconds?|secs?|s|minutes?|mins?|m|hours?|hrs?|h|days?|d|weeks?|w|years?|yrs?|y)(?: (ago|from now))?$/i;
var checkFailed = "check_failed";
function invalidDuration() {
  throw new TypeError("Invalid time period format");
}
__name(invalidDuration, "invalidDuration");
function secs(str) {
  typeof str != "string" && invalidDuration();
  const matched = REGEX.exec(str);
  (!matched || matched[4] && matched[1]) && invalidDuration();
  const value = parseFloat(matched[2]), durationSeconds = Math.round(value * multipliers[matched[3][0].toLowerCase()]);
  return Number.isFinite(durationSeconds) || invalidDuration(), matched[1] === "-" || matched[4] === "ago" ? -durationSeconds : durationSeconds;
}
__name(secs, "secs");
function validateInput(label, input) {
  if (!Number.isFinite(input))
    throw new TypeError(`Invalid ${label} input`);
  return input;
}
__name(validateInput, "validateInput");
var normalizeTyp = /* @__PURE__ */ __name((value) => {
  const normalized = value.toLowerCase();
  return value.includes("/") ? normalized : `application/${normalized}`;
}, "normalizeTyp");
var checkAudiencePresence = /* @__PURE__ */ __name((audPayload, audOption) => typeof audPayload == "string" ? audOption.includes(audPayload) : Array.isArray(audPayload) ? audOption.some((aud) => audPayload.includes(aud)) : false, "checkAudiencePresence");
function validateNumericDate(claimsSet, claim, required = false) {
  const value = claimsSet[claim];
  if (!(value === void 0 && !required)) {
    if (typeof value != "number")
      throw new JWTClaimValidationFailed(`"${claim}" claim must be a number`, claimsSet, claim, "invalid");
    return value;
  }
}
__name(validateNumericDate, "validateNumericDate");
function unexpectedClaim(claimsSet, claim) {
  throw new JWTClaimValidationFailed(`unexpected "${claim}" claim value`, claimsSet, claim, checkFailed);
}
__name(unexpectedClaim, "unexpectedClaim");
function validateClaimsSet(protectedHeader, claimsSetBytes, options = {}) {
  let claimsSet;
  try {
    claimsSet = JSON.parse(strictDecoder.decode(claimsSetBytes));
  } catch (cause) {
    throw new JWTInvalid("JWT Claims Set must be a top-level JSON object", { cause });
  }
  if (!isObject(claimsSet))
    throw new JWTInvalid("JWT Claims Set must be a top-level JSON object");
  const { typ } = options;
  if (typ !== void 0 && (typeof protectedHeader.typ != "string" || normalizeTyp(protectedHeader.typ) !== normalizeTyp(typ)))
    throw new JWTClaimValidationFailed('unexpected "typ" JWT header value', claimsSet, "typ", checkFailed);
  const { requiredClaims = [], issuer, subject, audience, maxTokenAge } = options, presenceCheck = [...requiredClaims];
  maxTokenAge !== void 0 && presenceCheck.push("iat"), audience !== void 0 && presenceCheck.push("aud"), subject !== void 0 && presenceCheck.push("sub"), issuer !== void 0 && presenceCheck.push("iss");
  for (const claim of new Set(presenceCheck.reverse()))
    if (!Object.hasOwn(claimsSet, claim))
      throw new JWTClaimValidationFailed(`missing required "${claim}" claim`, claimsSet, claim, "missing");
  issuer !== void 0 && !(Array.isArray(issuer) ? issuer : [issuer]).includes(claimsSet.iss) && unexpectedClaim(claimsSet, "iss"), subject !== void 0 && claimsSet.sub !== subject && unexpectedClaim(claimsSet, "sub"), audience !== void 0 && !checkAudiencePresence(claimsSet.aud, typeof audience == "string" ? [audience] : audience) && unexpectedClaim(claimsSet, "aud");
  const { clockTolerance } = options;
  let tolerance = 0;
  if (typeof clockTolerance == "string")
    tolerance = secs(clockTolerance);
  else if (clockTolerance !== void 0) {
    if (typeof clockTolerance != "number")
      throw new TypeError("Invalid clockTolerance option type");
    tolerance = clockTolerance;
  }
  if (validateInput("clockTolerance option", tolerance), tolerance < 0)
    throw new TypeError("Invalid clockTolerance option input");
  const { currentDate } = options, now = validateInput("currentDate option", epoch(currentDate === void 0 ? /* @__PURE__ */ new Date() : currentDate)), iat = validateNumericDate(claimsSet, "iat", maxTokenAge !== void 0), nbf = validateNumericDate(claimsSet, "nbf");
  if (nbf !== void 0 && nbf > now + tolerance)
    throw new JWTClaimValidationFailed('"nbf" claim timestamp check failed', claimsSet, "nbf", checkFailed);
  const exp = validateNumericDate(claimsSet, "exp");
  if (exp !== void 0 && exp <= now - tolerance)
    throw new JWTExpired('"exp" claim timestamp check failed', claimsSet, "exp", checkFailed);
  if (maxTokenAge !== void 0) {
    const age = now - iat, max = validateInput("maxTokenAge option", typeof maxTokenAge == "number" ? maxTokenAge : secs(maxTokenAge));
    if (age - tolerance > max)
      throw new JWTExpired('"iat" claim timestamp check failed (too far in the past)', claimsSet, "iat", checkFailed);
    if (age < -tolerance)
      throw new JWTClaimValidationFailed('"iat" claim timestamp check failed (it should be in the past)', claimsSet, "iat", checkFailed);
  }
  return claimsSet;
}
__name(validateClaimsSet, "validateClaimsSet");

// node_modules/jose/dist/webapi/jwt/verify.js
async function jwtVerify(jwt, key, options) {
  const [verified, b64] = await verifyCompact(jwt, prepareVerify(options), key);
  if (!b64)
    throw new JWTInvalid("JWTs MUST NOT use unencoded payload");
  const payload = validateClaimsSet(verified.protectedHeader, verified.payload, options);
  return { ...verified, payload };
}
__name(jwtVerify, "jwtVerify");

// node_modules/jose/dist/webapi/jwks/local.js
function isUsableJWK(jwk, entry, alg, kid) {
  const { kty, key_ops: keyOps, ext, kid: jwkKid, alg: jwkAlg, use, crv } = jwk;
  return (ext === void 0 || typeof ext == "boolean") && (keyOps === void 0 || Array.isArray(keyOps) && keyOps.every((operation, index) => typeof operation == "string" && keyOps.indexOf(operation) === index) && keyOps.includes("verify")) && entry.kty.includes(kty) && (kid === void 0 || typeof kid == "string" && kid === jwkKid) && (jwkAlg === void 0 ? kty !== "AKP" : alg === jwkAlg) && (use === void 0 || use === "sig") && (!entry.crv || crv === entry.crv);
}
__name(isUsableJWK, "isUsableJWK");
async function importWithAlgCache(cache3, jwk, entry) {
  const cached = cache3.get(jwk) || cache3.set(jwk, {}).get(jwk), { alg } = entry;
  if (cached[alg] === void 0) {
    const pending = jwkToKey(entry, jwk, true).then((key) => {
      if (key.type !== "public")
        throw new JWKSInvalid("JSON Web Key Set members must be public keys");
      return cached[alg] = key, key;
    }).catch((error) => {
      throw cached[alg] === pending && delete cached[alg], error;
    });
    cached[alg] = pending;
  }
  return cached[alg];
}
__name(importWithAlgCache, "importWithAlgCache");
function createLocalJWKSet(jwks) {
  let snapshot;
  try {
    snapshot = structuredClone(jwks);
  } catch (cause) {
    throw new JWKSInvalid("JSON Web Key Set malformed", { cause });
  }
  if (!isJwkSet(snapshot))
    throw new JWKSInvalid("JSON Web Key Set malformed");
  const metadata = snapshot.keys.map((jwk) => {
    const normalized = snapshotJwk(jwk);
    return Array.isArray(normalized.key_ops) && (normalized.key_ops = [...normalized.key_ops]), normalized;
  }), cached = /* @__PURE__ */ new WeakMap();
  return Object.defineProperty(async (protectedHeader, token) => {
    const { alg, kid } = { ...protectedHeader, ...token?.header }, entry = typeof alg == "string" ? JWS[alg] : void 0;
    if (!entry || entry.secret)
      throw new JOSENotSupported('Unsupported "alg" value for a JSON Web Key Set');
    const candidates = snapshot.keys.filter((_, index) => isUsableJWK(metadata[index], entry, alg, kid)), { 0: jwk, length } = candidates;
    if (!length)
      throw new JWKSNoMatchingKey();
    if (length !== 1) {
      const error = new JWKSMultipleMatchingKeys();
      throw error[Symbol.asyncIterator] = async function* () {
        for (const jwk2 of candidates)
          try {
            yield await importWithAlgCache(cached, jwk2, entry);
          } catch {
          }
      }, error;
    }
    return importWithAlgCache(cached, jwk, entry);
  }, "jwks", {
    value: /* @__PURE__ */ __name(() => structuredClone(snapshot), "value")
  });
}
__name(createLocalJWKSet, "createLocalJWKSet");

// node_modules/jose/dist/webapi/jwks/remote.js
function isCloudflareWorkers() {
  return typeof WebSocketPair < "u" || typeof navigator < "u" && true || typeof EdgeRuntime < "u" && EdgeRuntime === "vercel";
}
__name(isCloudflareWorkers, "isCloudflareWorkers");
var USER_AGENT;
(typeof navigator > "u" || !"Cloudflare-Workers"?.startsWith?.("Mozilla/5.0 ")) && (USER_AGENT = "jose/v6.2.15");
var customFetch = /* @__PURE__ */ Symbol();
async function fetchJwks(url, headers, signal, fetchImpl = fetch) {
  const response = await fetchImpl(url, {
    method: "GET",
    signal,
    redirect: "manual",
    headers
  }).catch((err) => {
    throw err.name === "TimeoutError" ? new JWKSTimeout(void 0, { cause: err }) : err;
  });
  if (response.status !== 200)
    throw new JOSEError("Expected 200 OK from the JSON Web Key Set HTTP response");
  try {
    return await response.json();
  } catch (cause) {
    throw new JOSEError("Failed to parse the JSON Web Key Set HTTP response as JSON", { cause });
  }
}
__name(fetchJwks, "fetchJwks");
var jwksCache = /* @__PURE__ */ Symbol();
function isFreshFor(timestamp, duration) {
  return Number.isFinite(timestamp) && Date.now() < timestamp + duration;
}
__name(isFreshFor, "isFreshFor");
function validateDuration(value, fallback, option) {
  if (Number.isNaN(value))
    throw new TypeError(`"${option}" option must not be NaN`);
  if (typeof value == "number" && value < 0)
    throw new TypeError(`"${option}" option must not be negative`);
  return typeof value == "number" ? value : fallback;
}
__name(validateDuration, "validateDuration");
function createRemoteJWKSet(url, options) {
  if (!(url instanceof URL))
    throw new TypeError("url must be an instance of URL");
  const href = new URL(url.href).href, opts = options ?? {}, timeoutOption = opts.timeoutDuration;
  if (typeof timeoutOption == "number" && (!Number.isInteger(timeoutOption) || timeoutOption < 0))
    throw new TypeError('"timeoutDuration" option must be a non-negative integer');
  const timeoutDuration = typeof timeoutOption == "number" ? timeoutOption : 5e3, cooldownDuration = validateDuration(opts.cooldownDuration, 3e4, "cooldownDuration"), cacheMaxAge = validateDuration(opts.cacheMaxAge, 6e5, "cacheMaxAge"), headers = new Headers(opts.headers);
  USER_AGENT && !headers.has("User-Agent") && headers.set("User-Agent", USER_AGENT), headers.has("accept") || headers.set("accept", "application/json, application/jwk-set+json");
  const fetchImpl = opts[customFetch], cache3 = opts[jwksCache];
  let jwksTimestamp, pendingFetch, reloadSequence = 0, appliedSequence = 0, local;
  if (cache3 && typeof cache3 == "object") {
    const { uat, jwks } = cache3;
    isFreshFor(uat, cacheMaxAge) && isJwkSet(jwks) && (jwksTimestamp = uat, local = createLocalJWKSet(jwks));
  }
  const reload = /* @__PURE__ */ __name(async () => {
    if (pendingFetch && isCloudflareWorkers() && (pendingFetch = void 0), !pendingFetch) {
      const sequence = ++reloadSequence, current = pendingFetch = fetchJwks(href, headers, AbortSignal.timeout(timeoutDuration), fetchImpl).then((json) => {
        const next = createLocalJWKSet(json);
        if (sequence <= appliedSequence)
          return;
        local = next;
        const updatedAt = Date.now();
        cache3 && (cache3.uat = updatedAt, cache3.jwks = json), jwksTimestamp = updatedAt, appliedSequence = sequence;
      }).finally(() => {
        pendingFetch === current && (pendingFetch = void 0);
      });
    }
    await pendingFetch;
  }, "reload");
  return Object.defineProperties(async (protectedHeader, token) => {
    (!local || !isFreshFor(jwksTimestamp, cacheMaxAge)) && await reload();
    try {
      return await local(protectedHeader, token);
    } catch (err) {
      if (err instanceof JWKSNoMatchingKey && !isFreshFor(jwksTimestamp, cooldownDuration))
        return await reload(), local(protectedHeader, token);
      throw err;
    }
  }, {
    coolingDown: {
      get: /* @__PURE__ */ __name(() => isFreshFor(jwksTimestamp, cooldownDuration), "get"),
      enumerable: true
    },
    fresh: {
      get: /* @__PURE__ */ __name(() => isFreshFor(jwksTimestamp, cacheMaxAge), "get"),
      enumerable: true
    },
    reload: {
      value: reload,
      enumerable: true
    },
    reloading: {
      get: /* @__PURE__ */ __name(() => !!pendingFetch, "get"),
      enumerable: true
    },
    jwks: {
      value: /* @__PURE__ */ __name(() => local?.jwks(), "value"),
      enumerable: true
    }
  });
}
__name(createRemoteJWKSet, "createRemoteJWKSet");

// node_modules/@tenunan-dev/hilir-auth/dist/verify.js
var jwksByUrl = /* @__PURE__ */ new Map();
function jwksFor(url) {
  let set = jwksByUrl.get(url);
  if (!set) {
    set = createRemoteJWKSet(new URL(url), {
      cacheMaxAge: 5 * 6e4,
      cooldownDuration: 3e4
    });
    jwksByUrl.set(url, set);
  }
  return set;
}
__name(jwksFor, "jwksFor");
async function verify(token, opts) {
  try {
    const jwksUrl = opts.jwksUrl ?? `${opts.issuer.replace(/\/+$/, "")}/jwks`;
    const { payload } = await jwtVerify(token, jwksFor(jwksUrl), {
      issuer: opts.issuer,
      audience: opts.audience,
      // EdDSA/Ed25519 only — the estate decision (PLAN.md §1). Never ES256.
      algorithms: ["EdDSA"],
      clockTolerance: opts.clockToleranceSec ?? 5
    });
    const claimed = typeof payload.scope === "string" ? payload.scope : "";
    const scope = claimed.split(" ").filter((part) => part.length > 0);
    return {
      sub: String(payload.sub ?? ""),
      ...typeof payload.email === "string" ? { email: payload.email } : {},
      ...typeof payload.name === "string" ? { name: payload.name } : {},
      scope,
      claims: payload
    };
  } catch {
    return null;
  }
}
__name(verify, "verify");
function bearerToken(request) {
  const raw = (request.headers.get("authorization") ?? "").trim();
  if (raw.toLowerCase().startsWith("bearer ") !== true)
    return null;
  const token = raw.slice(7).trim();
  return token.length > 0 ? token : null;
}
__name(bearerToken, "bearerToken");

// node_modules/@tenunan-dev/hilir-auth/dist/mcp.js
var PROTECTED_RESOURCE_METADATA_PATH = "/.well-known/oauth-protected-resource";
function protectedResourceMetadata(cfg, opts = {}) {
  const resource = (opts.resource ?? cfg.resource ?? "").replace(/\/+$/, "");
  return {
    resource,
    authorization_servers: [cfg.issuer.replace(/\/+$/, "")],
    ...opts.scopes && opts.scopes.length > 0 ? { scopes_supported: opts.scopes } : {},
    bearer_methods_supported: ["header"],
    ...opts.documentation ? { resource_documentation: opts.documentation } : {}
  };
}
__name(protectedResourceMetadata, "protectedResourceMetadata");

// node_modules/@tenunan-dev/hilir-auth/dist/agentkey.js
var cache2 = /* @__PURE__ */ new Map();
var DEFAULT_TTL_MS = 6e4;
var REQUEST_TIMEOUT_MS = 5e3;
function verifyEndpoint(issuer) {
  const origin = issuer.replace(/\/+$/, "").replace(/\/api\/auth$/, "");
  return `${origin}/api/v2-introspect`;
}
__name(verifyEndpoint, "verifyEndpoint");
function formEncode(value) {
  return encodeURIComponent(value).replace(/%20/g, "+").replace(/[!'()*]/g, (c) => `%${c.charCodeAt(0).toString(16).toUpperCase()}`);
}
__name(formEncode, "formEncode");
async function sha256Hex(value) {
  const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(value));
  return [...new Uint8Array(digest)].map((b) => b.toString(16).padStart(2, "0")).join("");
}
__name(sha256Hex, "sha256Hex");
function expToMs(exp) {
  return typeof exp === "number" && Number.isFinite(exp) ? exp * 1e3 : null;
}
__name(expToMs, "expToMs");
async function verifyAgentKey(cfg, key, opts = {}) {
  if (!key || !cfg.clientSecret)
    return null;
  const ttl = opts.ttlMs ?? DEFAULT_TTL_MS;
  const cacheKey = await sha256Hex(`${cfg.clientId}:${key}`);
  const hit = cache2.get(cacheKey);
  if (hit && Date.now() < hit.until)
    return hit.info;
  let info = null;
  let authoritative = false;
  try {
    const abort = new AbortController();
    const timer = setTimeout(() => abort.abort(), REQUEST_TIMEOUT_MS);
    let res;
    try {
      res = await fetch(verifyEndpoint(cfg.issuer), {
        method: "POST",
        headers: {
          "content-type": "application/x-www-form-urlencoded",
          authorization: `Basic ${btoa(`${formEncode(cfg.clientId)}:${formEncode(cfg.clientSecret)}`)}`
        },
        body: new URLSearchParams({ token: key }).toString(),
        signal: abort.signal
      });
    } finally {
      clearTimeout(timer);
    }
    if (res.ok) {
      const body = await res.json();
      authoritative = true;
      if (body.active) {
        info = {
          userId: body.sub ?? null,
          scopes: typeof body.scope === "string" ? body.scope.split(" ").filter(Boolean) : [],
          expiresAt: body.exp ?? null
        };
      }
    }
  } catch {
    info = null;
  }
  if (authoritative) {
    const expMs = expToMs(info?.expiresAt);
    const until = Math.min(Date.now() + ttl, expMs ?? Number.POSITIVE_INFINITY);
    if (cache2.size > 512)
      cache2.clear();
    if (until > Date.now())
      cache2.set(cacheKey, { at: Date.now(), until, info });
  }
  return info;
}
__name(verifyAgentKey, "verifyAgentKey");
function keyHasScope(info, scope) {
  return info.scopes.includes(scope);
}
__name(keyHasScope, "keyHasScope");
function looksLikeAgentKey(token) {
  return token.length > 0 && token.split(".").length !== 3;
}
__name(looksLikeAgentKey, "looksLikeAgentKey");

// node_modules/@tenunan-dev/hilir-auth/dist/oidc.js
var DISCOVERY_TTL_MS = 10 * 6e4;

// node_modules/@tenunan-dev/hilir-auth/dist/middleware.js
var MAX_ACCESS_COOKIE_AGE = 30 * 86400;

// src/index.ts
function bearerChallenge(origin, presented) {
  return [
    `Bearer resource_metadata="${origin.replace(/\/+$/, "")}${PROTECTED_RESOURCE_METADATA_PATH}"`,
    ...presented ? ['error="invalid_token"'] : []
  ].join(", ");
}
__name(bearerChallenge, "bearerChallenge");
function parseAudiences(value) {
  return value.split(",").map((a) => a.trim()).filter(Boolean);
}
__name(parseAudiences, "parseAudiences");
function jsonError(status, body, request) {
  let challenge = "Bearer";
  if (request) {
    challenge = bearerChallenge(
      new URL(request.url).origin,
      Boolean(request.headers.get("authorization"))
    );
  }
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      ...status === 401 ? { "www-authenticate": challenge } : {}
    }
  });
}
__name(jsonError, "jsonError");
function oidcConfigFrom(env) {
  return {
    issuer: env.HILIR_ISSUER,
    clientId: env.HILIR_CLIENT_ID ?? "",
    clientSecret: "",
    redirectUri: ""
  };
}
__name(oidcConfigFrom, "oidcConfigFrom");
async function machineGate(request, env) {
  const path = new URL(request.url).pathname;
  const token = bearerToken(request) ?? (request.headers.get("x-api-key") || null);
  if (!token) {
    console.log(JSON.stringify({ event: "denied", actor: null, status: 401, reason: "unauthenticated", path }));
    return jsonError(401, { error: "unauthorized" }, request);
  }
  if (looksLikeAgentKey(token)) {
    const info = await verifyAgentKey(
      {
        issuer: env.HILIR_ISSUER,
        clientId: env.HILIR_CLIENT_ID ?? "",
        clientSecret: env.HILIR_CLIENT_SECRET ?? "",
        redirectUri: ""
      },
      token
    );
    const required2 = env.REQUIRED_SCOPE ?? "catalog:read";
    if (!info) {
      console.log(JSON.stringify({ event: "denied", actor: null, status: 401, reason: "agent_key", path }));
      return jsonError(401, { error: "unauthorized" }, request);
    }
    if (!keyHasScope(info, required2)) {
      console.log(JSON.stringify({ event: "denied", actor: info.userId, status: 403, reason: "scope", required: required2, path }));
      return jsonError(403, { error: "forbidden", required: required2 }, request);
    }
    console.log(JSON.stringify({ event: "request", actor: info.userId ?? "agent-key", path, method: request.method }));
    return null;
  }
  const audiences = parseAudiences(env.AUDIENCE);
  let user = null;
  for (const audience of audiences) {
    user = await verify(token, { issuer: env.HILIR_ISSUER, audience });
    if (user) break;
  }
  if (!user) {
    console.log(JSON.stringify({ event: "denied", actor: null, status: 401, reason: "invalid_token", path }));
    return jsonError(401, { error: "unauthorized" }, request);
  }
  const required = env.REQUIRED_SCOPE ?? "catalog:read";
  if (!user.scope.includes(required)) {
    console.log(JSON.stringify({ event: "denied", actor: user.sub, status: 403, reason: "scope", required, path }));
    return jsonError(403, { error: "forbidden", required });
  }
  console.log(JSON.stringify({ event: "request", actor: user.sub, path, method: request.method }));
  return null;
}
__name(machineGate, "machineGate");
function storeDsnHeaders(request, env) {
  const headers = new Headers(request.headers);
  headers.set("x-user-store-dsn", env.USER_STORE_URL ?? "");
  headers.delete("x-api-key");
  if (!headers.get("authorization")) {
    const presented = request.headers.get("x-api-key");
    if (presented) headers.set("authorization", `Bearer ${presented.trim()}`);
  }
  return headers;
}
__name(storeDsnHeaders, "storeDsnHeaders");
async function toContainer(request, env) {
  const headers = storeDsnHeaders(request, env);
  const url = new URL(request.url);
  const body = ["GET", "HEAD"].includes(request.method) ? void 0 : await request.arrayBuffer();
  headers.set("x-origin-token", env.ORIGIN_TOKEN);
  headers.set("x-origin-route", "api");
  const upstream = new Request(
    `${env.LIBRARY_ORIGIN}${url.pathname}${url.search}`,
    { method: request.method, headers, body, redirect: "manual" }
  );
  return fetch(upstream);
}
__name(toContainer, "toContainer");
var index_default = {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === "/health") {
      return Response.json({ service: "HILIR Technology Library", role: "backend", mcp: "/mcp", rest: "/api", openapi: "/api/openapi.json" });
    }
    if (url.pathname === "/api/openapi.json") {
      return toContainer(request, env);
    }
    if (url.pathname === PROTECTED_RESOURCE_METADATA_PATH) {
      return Response.json(
        protectedResourceMetadata(oidcConfigFrom(env), { resource: url.origin, scopes: ["catalog:read"], documentation: `${url.origin}/` })
      );
    }
    const denied = await machineGate(request, env);
    if (denied) return denied;
    return toContainer(request, env);
  }
};
export {
  bearerChallenge,
  index_default as default,
  parseAudiences
};
//# sourceMappingURL=index.js.map
