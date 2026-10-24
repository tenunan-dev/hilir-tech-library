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

## Live deployment: Cloudflare (techlibrary.tenunan.com)

The hosted server runs on Cloudflare Containers, in the Cloudflare account that holds tenunan.com
(Faisal.muthalib@gmail.com's account, Workers Paid plan). Endpoint: `https://techlibrary.tenunan.com/mcp`.

- `deploy/cloudflare/src/index.ts`: a Worker that checks the API key at the edge, then forwards to one container instance (Durable Object "main"). `/health` answers without a key.
- `deploy/cloudflare/wrangler.jsonc`: builds the repo's `Dockerfile` (open-licence copy only), instance type `basic`, `max_instances` 1, custom domain route.
- The container stops after 30 idle minutes (`sleepAfter`) and restarts on the next request, so the first call after a quiet spell takes a few seconds longer.
- The API key is the Worker secret `LIBRARY_API_KEY`. The owner's copy is in `~/.config/og-tech-library/api-key` on their Mac (mode 600). It is never in the repo.
- The image is built from the repo at deploy time: **redeploy after collecting new documents** so the hosted copy matches.
- Keyword search only (no embeddings in the image).

```
cd deploy/cloudflare
npm install                      # once
npx wrangler deploy              # needs Docker running; builds ../../Dockerfile
# rotate the key:
python3 -c 'import secrets;print(secrets.token_urlsafe(32))' > ~/.config/og-tech-library/api-key
tr -d '\n' < ~/.config/og-tech-library/api-key | npx wrangler secret put LIBRARY_API_KEY
npx wrangler tail                # live logs
```

Connect a client: URL `https://techlibrary.tenunan.com/mcp`, header `x-api-key: <key>`. For example, Claude Code:
`claude mcp add --transport http og-tech-library-remote https://techlibrary.tenunan.com/mcp --header "x-api-key: <key>"`.

## Deploy to Azure Container Apps (alternative, not used: no Azure subscription) (recommended for Copilot Studio)

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
3. Server URL: `https://<fqdn>/mcp`.
4. Authentication: **API key**, type **Header**, header name `x-api-key`. Enter the key when creating the connection.
5. Add the server's tools (`search`, `get_source`, `get_document`, `list_by_tag`, `library_stats`) to the agent and test in the test pane, e.g. *"Which Southeast Asian sources cover LNG liquefaction?"*

Notes:
- Copilot Studio supports only the streamable HTTP transport (SSE ended in August 2025), which this server uses. Reference: https://learn.microsoft.com/microsoft-copilot-studio/mcp-add-existing-server-to-agent
- If your tenant has Power Platform data policies, they apply to MCP connectors too; an admin may need to allow the connector.
- For an agent shared across an organisation, consider replacing the API key with OAuth 2.0 (Microsoft Entra ID) so each user signs in; Copilot Studio supports OAuth for MCP servers. That needs an app registration and token validation added to the server.

## Alternatives considered

| Route | Verdict |
| --- | --- |
| MCP server by URL (above) | Recommended: live search, licence fields in every result, one setup for Copilot Studio and other MCP clients |
| Custom connector or REST/OpenAPI action | Works, but needs a separate REST API and Power Platform connector to maintain; Copilot Studio's MCP support covers the same need |
| SharePoint or OneDrive knowledge source (upload `catalog/index/*.md` and open documents) | No server, but a manual copy that goes stale, no filtering by sector or region, and restricted text must be kept out by hand |
