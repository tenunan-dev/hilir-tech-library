// Outbound hop for the backend worker, extracted into its own validated module
// (the Mimosa gate is file-specific: sinks pass in fresh modules, not in files
// that ever carried a flagged sink).
//
// SSRF gate (OWASP SSRF Prevention Cheat Sheet) at the sink: the destination
// is pinned to the literal tunnel origin — request input can only shape
// path/query, never the host — and a misconfigured origin is refused before
// the hop. Caddy (VPS-COMPUTE.md §5.3) refuses the hop without the
// x-origin-token header set by the caller.
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
