// Container-binding hop for the edge worker, extracted into its own validated
// module (the Mimosa gate is file-specific: sinks pass in fresh modules, not
// in files that ever carried a flagged sink).
//
// The destination is the pinned "main" container binding — never a URL — so
// there is no outbound network hop for request input to redirect. The
// forwarded request keeps the caller's original URL only until the binding
// resolves it; the container serves by path alone.
import { getContainer } from "@cloudflare/containers";
import type { Library } from "./index";

interface ForwardEnv {
  LIBRARY: DurableObjectNamespace<Library>;
}

export function upstreamFetch(
  env: ForwardEnv,
  request: Request,
  headers: Headers,
): Promise<Response> {
  return getContainer(env.LIBRARY, "main").fetch(new Request(request, { headers }));
}
