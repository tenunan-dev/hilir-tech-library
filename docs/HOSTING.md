# Hosting the library for agents that connect by URL

Agents that run in the cloud (Microsoft Copilot Studio, claude.ai connectors, other hosted
agents) cannot start a local process. They connect to an MCP server by URL over streamable
HTTP. `agent/server.py --http` provides that.

## What the hosted server serves

- All catalog records (metadata and links).
- Documents whose own licence is open (`reuse_level: full-text-open` in their front matter), e.g. arXiv metadata and abstracts (CC0).
- **Not** documents from `full-text-restricted` sources (private reference copies, e.g. OSTI abstracts today). The Dockerfile leaves them out of the image entirely (`agent/export_public.py`), and the server hides them too. `--include-restricted` exists only for a server that no one but the owner can reach; do not use it for a shared agent.

Every request needs the API key, sent as header `x-api-key: <key>` or `Authorization: Bearer <key>`. The key comes from the `LIBRARY_API_KEY` environment variable (at least 24 characters) and must be stored as a secret, never in the repo or image.

## Run it locally

```
pip install -r requirements-agent.txt
python agent/library.py build
LIBRARY_API_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')" python agent/server.py --http --port 8000
# endpoint: http://localhost:8000/mcp
```

## Live deployment: Cloudflare (techlib.hilir.app)

The hosted server runs on Cloudflare Containers, in the Cloudflare account that holds hilir.app and tenunan.com
(Faisal.muthalib@gmail.com's account, Workers Paid plan). Endpoint: `https://techlib.hilir.app/mcp`.

- `deploy/cloudflare/src/index.ts`: a Worker that checks the API key at the edge, then forwards to one container instance (Durable Object "main"). `/health` answers without a key.
- `deploy/cloudflare/wrangler.jsonc`: builds the repo's `Dockerfile` (open-licence copy only), instance type `basic`, `max_instances` 1, custom domain route.
- The container has internet access (`enableInternet = true` in the worker) so it can reach Neon Postgres when `DATABASE_URL` is set.
- The container stops after 30 idle minutes (`sleepAfter`) and restarts on the next request, so the first call after a quiet spell takes a few seconds longer.
- The API key is the Worker secret `LIBRARY_API_KEY`. The owner's copy is in `~/.config/og-tech-library/api-key` on their Mac (mode 600). It is never in the repo.
- Optional Worker secret `DATABASE_URL`: the read-only Neon DSN (see docs/POSTGRES.md). It enables the three database tools (`sql_query`, `db_catalog`, `graph_neighbors`) and the `/database` web pages; without it they answer `database not configured`.
- The image is built from the repo at deploy time: **redeploy after collecting new documents** so the hosted copy matches.
- After a deploy, the running instance keeps serving the **old** image until Cloudflare cycles it (`npx wrangler containers list` shows `provisioning` with 0 live instances during the swap). The swap can take several minutes; until it completes the new UI paths answer 401 or 404 (the old image has no web routes). Verify the new build only after the swap: `curl -H "x-api-key: $KEY" https://techlib.hilir.app/api/stats` should show the current source and card counts.
- Keyword search only (no embeddings in the image).

```
cd deploy/cloudflare
npm install                      # once
npx wrangler deploy              # needs Docker running; builds ../../Dockerfile
# database tools + /database pages (optional):
tr -d '\n' < ~/.config/og-tech-library/db-readonly.url | npx wrangler secret put DATABASE_URL
# rotate the key:
python3 -c 'import secrets;print(secrets.token_urlsafe(32))' > ~/.config/og-tech-library/api-key
tr -d '\n' < ~/.config/og-tech-library/api-key | npx wrangler secret put LIBRARY_API_KEY
npx wrangler tail                # live logs
```

### Web interface (agent/web.py)

The same container serves a server-rendered HTML interface at the same origin, live since 2026-10-26
(container image `affe1dfa`). `https://techlib.hilir.app/` is now the UI home page (counts, search box,
sector grid); `/health` still answers the JSON service banner.

| Path | Shows |
| --- | --- |
| `/login`, `/logout` | Sign in / sign out |
| `/search?q=...` | Ranked sources, passages and technology cards |
| `/technologies`, `/technologies/{id}` | Comparison table; one card in full: block diagram, figures (unit, year, basis, source), suppliers, reference plants, gaps, sources |
| `/register` | The ~300-technology register |
| `/sources`, `/sources/{id}`, `/documents?path=...` | Catalog records and document text |
| `/gaps` | Missing inputs on the cards |
| `/database`, `/database/sql`, `/database/search`, `/database/graph`, `/database/map` | Row counts, schema reference and example queries; read-only SQL console; hybrid keyword+vector search; interactive knowledge-graph network; the whole graph as an atlas |

- Sign-in: enter the library API key once at `/login` (the same key agents send in the `x-api-key`
  header); the server sets a session cookie (`oglib_session`, HMAC-SHA256 of the key, HttpOnly /
  Secure / SameSite=Lax) that lasts 30 days. Any page without a valid session redirects (303) to
  `/login?next=...`. Every page also accepts the usual `x-api-key` header instead of the cookie.
- **Named accounts (multiple users):** besides the key, people can sign in at `/login` with an
  email + password. Accounts live in the optional `LIBRARY_USERS` secret — `email|name|scrypt-hash`
  entries separated by `;` (agent/users.py documents the format). Create an entry locally and set
  it as a secret; the hash is salted scrypt, never the password:

  ```
  python agent/users.py entry alice@example.com "Alice Chen"     # prints alice@example.com|Alice Chen|scrypt$...
  cd deploy/cloudflare && npx wrangler secret put LIBRARY_USERS  # paste the entries; no redeploy needed
  ```

  Account sessions are stateless signed cookies (`v2|payload|hmac`, 30 days) that carry the email;
  the API key keeps working unchanged for agents and for the owner. Set the same variable locally
  for `python agent/server.py --http` runs. Failed sign-ins (key or password) sleep half a second
  to damp online guessing.
- Licence: the pages serve the same open-licence text as the REST API (`full-text-open` only);
  restricted sources appear as metadata-only records.
- Diagrams load Mermaid 11 from jsdelivr; if that script cannot load, the diagram shows as its plain
  code block.
- The edge worker forwards UI paths to the container **without** requiring or injecting the API key
  (the container checks the session cookie), so `UI_PREFIXES` in `deploy/cloudflare/src/index.ts` must
  stay in sync with `PREFIXES` in `agent/web.py`: a new UI path missing from `UI_PREFIXES` gets a 401
  at the edge, and one missing from `PREFIXES` gets a 404 from the container.

### Old domain retired (2026-10-27)

The only home is **https://techlib.hilir.app** (Worker routes in wrangler.jsonc: hilir.app only).
`techlibrary.tenunan.com` was removed from the Worker's custom domains on the owner's decision —
its DNS record went with it, so old links fail DNS resolution rather than redirecting. If old
links should forward after all: re-create a proxied DNS record for the hostname on the tenunan.com
zone and add a zone redirect rule to the new host (dashboard or API; not managed by wrangler).
OAuth grants are per-URL: claude.ai connectors and OAuth clients must use the new URL. API-key
clients (Copilot Studio, ChatGPT Actions, curl) only need the new base URL.

Connect a client: URL `https://techlib.hilir.app/mcp`, header `x-api-key: <key>`. For example, Claude Code:
`claude mcp add --transport http og-tech-library-remote https://techlib.hilir.app/mcp --header "x-api-key: <key>"`.

### Test the connection (run from the Mac after any deploy or client setup)

```sh
KEY=$(cat ~/.config/og-tech-library/api-key)
# 1. edge is alive (no key needed)
curl -s https://techlib.hilir.app/health
# 2. REST API + container answer with the current counts
curl -s -H "x-api-key: $KEY" https://techlib.hilir.app/api/stats
# 3. MCP handshake
curl -s -X POST https://techlib.hilir.app/mcp -H "x-api-key: $KEY" \
  -H "content-type: application/json" -H "accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"test","version":"0"}}}'
# 4. one real tool call
curl -s -X POST https://techlib.hilir.app/mcp -H "x-api-key: $KEY" \
  -H "content-type: application/json" -H "accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"library_stats","arguments":{}}}'
# 5. web interface: the unsigned home page redirects to /login
curl -s -o /dev/null -w '%{http_code} %{redirect_url}\n' https://techlib.hilir.app/
#    sign in once (saves the session cookie), then load the home page with it
curl -s -o /dev/null -w '%{http_code}\n' -c /tmp/oglib.cookies \
  --data-urlencode "key=$KEY" --data-urlencode "next=/" https://techlib.hilir.app/login
curl -s -o /dev/null -w '%{http_code}\n' -b /tmp/oglib.cookies https://techlib.hilir.app/
rm -f /tmp/oglib.cookies
# 6. one database tool call (needs the DATABASE_URL secret on the Worker)
curl -s -X POST https://techlib.hilir.app/mcp -H "x-api-key: $KEY" \
  -H "content-type: application/json" -H "accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"sql_query","arguments":{"sql":"SELECT count(*) AS cards FROM technology"}}}'
```

Expected: 1 answers the service banner; 2 returns the source/document/chunk/card counts; 3 returns a JSON-RPC
result with the server's capabilities; 4 returns the same counts as 2 wrapped in a tool result (`"isError":false`);
5 prints `303` with a `/login?next=...` redirect for the unsigned page, then `303` from the sign-in POST and
`200` for the signed-in home page; 6 returns the card count inside a tool result, or a `"database not configured"`
error result when `DATABASE_URL` is not set.
The server runs the MCP session statelessly (no `mcp-session-id` header) and answers `application/json`; a
`notifications/initialized` POST between 3 and 4 gets a 202 but is not required. Full walkthrough of the
first run of this test (including `tools/list` and `search`): STATUS.md, log entry 2026-10-26.

### REST API (for agents without MCP)

The same server answers plain HTTPS GET requests under `/api`, with the same `x-api-key` header and
the same licence filtering as the MCP tools (`agent/api.py`). The OpenAPI 3.1 schema is public at
`https://techlib.hilir.app/api/openapi.json` (it holds no data), so tools can import it.

| Endpoint | Returns |
| --- | --- |
| `GET /api/search?q=...&kind=&sector=&discipline=&region=&reuse_level=&limit=` | Ranked sources, passages and technology cards |
| `GET /api/sources?code=&region=&reuse_level=&source_type=` | Catalog sources, Asia Pacific first |
| `GET /api/sources/{source_id}` | One record with its documents |
| `GET /api/documents?path=...` | One document's front matter and text |
| `GET /api/technologies?sector=&maturity=&application=` | Comparison table of options |
| `GET /api/technologies/{technology_id}` | One technology card |
| `GET /api/register?code=&maturity=&q=` | The ~300-technology register |
| `GET /api/gaps?sector=&field=&reason_code=&include_no_card=` | Missing inputs and where to get them |
| `GET /api/stats` | Counts |

Examples:
- curl: `curl -H "x-api-key: $KEY" "https://techlib.hilir.app/api/search?q=LNG%20liquefaction&limit=5"`
- ChatGPT custom GPT: Configure > Actions > Import from URL `https://techlib.hilir.app/api/openapi.json`; Authentication: API key, Custom header `x-api-key`.
- LangChain, n8n, Make, Zapier or any HTTP tool: GET requests with the `x-api-key` header.

### OAuth sign-in for claude.ai and other URL-only clients

`/mcp` also accepts OAuth 2.1 access tokens (Cloudflare `workers-oauth-provider`, pinned 1.2.3, tokens in the
KV namespace `OAUTH_KV`). Clients discover it from the 401 challenge
(`/.well-known/oauth-protected-resource/mcp`, `/.well-known/oauth-authorization-server`) and register
themselves (`/register`, or a Client ID Metadata Document). The sign-in page at `/authorize` asks for the
**library API key**, so only someone holding the key (the owner) can grant access; a wrong key denies the
request. Scope `mcp:read` (read only). The REST API under `/api` stays key-only.

Add to claude.ai: Settings > Connectors > Add custom connector, URL `https://techlib.hilir.app/mcp`,
leave the OAuth client fields empty, Connect, then paste the key from `~/.config/og-tech-library/api-key`
on the sign-in page and Allow. The connection then works in claude.ai on web and in the mobile apps.

## Deploy to Azure Container Apps (alternative, not used: no Azure subscription)

Same cloud as Copilot Studio, scales to zero when idle (pay only for use), HTTPS by default. Uses the `Dockerfile` in the repo root. Needs the Azure CLI (`az login`) and an Azure subscription.

```
az group create -n rg-og-library -l southeastasia
az containerapp up -n og-tech-library -g rg-og-library -l southeastasia \
  --source . --ingress external --target-port 8000
az containerapp secret set -n og-tech-library -g rg-og-library \
  --secrets library-api-key="<generated key>"
az containerapp update -n og-tech-library -g rg-og-library \
  --set-env-vars LIBRARY_API_KEY=secretref:library-api-key --min-replicas 0 --max-replicas 1
az containerapp show -n og-tech-library -g rg-og-library --query properties.configuration.ingress.fqdn -o tsv
```

The server URL is `https://<fqdn>/mcp`. Re-run `az containerapp up ... --source .` after pulling new corpus documents to redeploy. Optionally set `LIBRARY_ALLOWED_HOSTS=<fqdn>` to enable Host header checks.

Any other container host (Azure App Service, Google Cloud Run, Fly.io, a VM) works the same way: build the Dockerfile, set `LIBRARY_API_KEY` as a secret, expose port 8000 over HTTPS.

## Connect Microsoft Copilot Studio

1. Open the agent in Copilot Studio, go to **Tools**, then **Add a tool > New tool > Model Context Protocol**.
2. Server name: `O&G technology library`. Server description (the orchestrator uses it to decide when to call the server): *Searches a curated library of oil, gas, petrochemical, hydrogen, CCUS and power technology sources, weighted to Asia Pacific and Southeast Asia. Returns sources and passages with url, licence and reuse level.*
3. Server URL: `https://techlib.hilir.app/mcp` (the live deployment above).
4. Authentication: **API key**, type **Header**, header name `x-api-key`. Enter the key when creating the connection.
5. Add the server's tools (`search`, `get_source`, `get_document`, `list_by_tag`, `get_technology`, `compare_technologies`, `list_technology_register`, `list_gaps`, `library_stats`, `sql_query`, `db_catalog`, `graph_neighbors`) to the agent and test in the test pane, e.g. *"Which Southeast Asian sources cover LNG liquefaction?"* or *"Compare post-combustion capture technologies with their costs."* The three database tools need the `DATABASE_URL` secret on the Worker; without it they answer `database not configured`.

Notes:
- Copilot Studio supports only the streamable HTTP transport (SSE ended in August 2025), which this server uses. Reference: https://learn.microsoft.com/microsoft-copilot-studio/mcp-add-existing-server-to-agent
- If tenant data policies block MCP connectors, import the REST schema instead: create a custom tool from the public `https://techlib.hilir.app/api/openapi.json` with the same `x-api-key` header authentication.
- If your tenant has Power Platform data policies, they apply to MCP connectors too; an admin may need to allow the connector.
- For an agent shared across an organisation, consider replacing the API key with OAuth 2.0 (Microsoft Entra ID) so each user signs in; Copilot Studio supports OAuth for MCP servers. That needs an app registration and token validation added to the server.

## Alternatives considered

| Route | Verdict |
| --- | --- |
| MCP server by URL (above) | Recommended: live search, licence fields in every result, one setup for Copilot Studio and other MCP clients |
| Custom connector or REST/OpenAPI action | Works, but needs a separate REST API and Power Platform connector to maintain; Copilot Studio's MCP support covers the same need |
| SharePoint or OneDrive knowledge source (upload `catalog/index/*.md` and open documents) | No server, but a manual copy that goes stale, no filtering by sector or region, and restricted text must be kept out by hand |
