# Hosted MCP server for agents that connect by URL (Copilot Studio, claude.ai connectors, others).
# Only catalog records and open-licence documents go into the image; see agent/export_public.py.
# A comment-only change still produces a new image digest, which cycles the running container
# (used 2026-10-27 to pick up a rotated USER_STORE_URL secret — containers keep old env until replaced).
FROM python:3.12-slim AS export
WORKDIR /src
COPY . .
RUN pip install --no-cache-dir pyyaml && python agent/export_public.py /public

# Index stage: build + embed from the stable inputs ONLY (catalog, the open corpus, taxonomy
# and the four agent modules they import). UI/API code changes (web.py, server.py, api.py…)
# never touch these layers, so their deploys reuse the embedded index instead of re-running
# the ~25-minute embed; a catalog or corpus change re-embeds, as it should.
FROM python:3.12-slim AS index
WORKDIR /app
COPY --from=export /public/catalog catalog/
COPY --from=export /public/corpus corpus/
COPY --from=export /public/taxonomy.yaml taxonomy.yaml
COPY --from=export /public/requirements-agent.txt requirements-agent.txt
COPY --from=export /public/agent/library.py agent/library.py
COPY --from=export /public/agent/technologies.py agent/technologies.py
COPY --from=export /public/agent/vendors.py agent/vendors.py
COPY --from=export /public/agent/embed.py agent/embed.py
RUN pip install --no-cache-dir -r requirements-agent.txt "psycopg[binary]>=3.1" \
 && python agent/library.py build \
 && OMP_NUM_THREADS=4 python agent/embed.py

FROM python:3.12-slim
WORKDIR /app
# the built-and-embedded index (build/) plus the index stage's agent subset…
COPY --from=index /app .
# …then the full public tree (brings the remaining agent modules, schema), overwriting nothing else
COPY --from=export /public .
# fastembed's model cache, so the runtime query embedder never downloads on first search
COPY --from=index /root/.cache /root/.cache
ENV PORT=8000
EXPOSE 8000
RUN pip install --no-cache-dir -r requirements-agent.txt "psycopg[binary]>=3.1"
# LIBRARY_API_KEY must be set at run time (a secret), never baked into the image.
CMD ["python", "agent/server.py", "--http"]
