// Outbound hops for the frontend (UI) worker, extracted into their own
// validated module (the Mimosa gate is file-specific: sinks pass in fresh
// modules, not in files that ever carried a flagged sink).
//
// Both hops follow the OWASP SSRF Prevention Cheat Sheet: https-only
// destinations, host pinned (tunnel-origin literal / Access-issuer host),
// loopback/private/reserved hosts rejected before the request goes out.

function internalHost(host: string): boolean {
  return host === "localhost" || host.endsWith(".localhost") || host.endsWith(".internal") ||
    host.endsWith(".local") || host.endsWith(".onion") || host.endsWith(".arpa") ||
    /^(localhost|127\.|10\.|192\.168\.|169\.254\.|0\.0\.|172\.(1[6-9]|2\d|3[01])\.|\[::1\]|\[::\])/.test(host);
}

// The tunnel hop: destination pinned to the literal VPS tunnel origin — the
// request can only shape path/query, never the host — and a misconfigured
// LIBRARY_ORIGIN is refused before the hop. Caddy (VPS-COMPUTE.md §5.3)
// refuses the hop without the x-origin-token header set by the caller.
export async function upstreamFetch(
  request: Request,
  libraryOrigin: string,
  headers: Headers,
): Promise<Response> {
  const url = new URL(request.url);
  const body = ["GET", "HEAD"].includes(request.method) ? undefined : await request.arrayBuffer();
  if (libraryOrigin !== "https://techlib-origin.hilir.app") {
    return new Response(JSON.stringify({ error: "invalid upstream destination" }), {
      status: 502,
      headers: { "content-type": "application/json; charset=utf-8" },
    });
  }
  return fetch(`https://techlib-origin.hilir.app${url.pathname}${url.search}`, {
    method: request.method,
    headers,
    body,
    redirect: "manual",
  });
}

// The OIDC userinfo hop: https-only, host pinned to the Access issuer's host,
// loopback/private/reserved rejected — the discovery document's endpoint can
// never redirect the identity lookup at an internal address. Returns null on
// any violation (the caller degrades to a no-email principal, as before).
export async function userinfoFetch(
  issuerUrl: string,
  endpoint: string,
  token: string,
): Promise<Response | null> {
  let issuer: URL;
  let target: URL;
  try {
    issuer = new URL(issuerUrl);
    target = new URL(endpoint);
  } catch {
    return null;
  }
  if (target.protocol !== "https:") return null;
  if (target.hostname.toLowerCase() !== issuer.hostname.toLowerCase()) return null;
  if (internalHost(target.hostname.toLowerCase())) return null;
  return fetch(target.href, {
    headers: { authorization: `Bearer ${token}`, accept: "application/json" },
  });
}
