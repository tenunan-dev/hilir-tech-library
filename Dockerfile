# Hosted MCP server for agents that connect by URL (Copilot Studio, claude.ai connectors, others).
# Only catalog records and open-licence documents go into the image; see agent/export_public.py.
# A comment-only change still produces a new image digest, which cycles the running container
# (used 2026-10-27 to pick up a rotated USER_STORE_URL secret — containers keep old env until replaced).
FROM python:3.12-slim AS export
WORKDIR /src
COPY . .
RUN pip install --no-cache-dir pyyaml && python agent/export_public.py /public

FROM python:3.12-slim
WORKDIR /app
COPY --from=export /public .
RUN pip install --no-cache-dir -r requirements-agent.txt "psycopg[binary]>=3.1" && python agent/library.py build
ENV PORT=8000
EXPOSE 8000
# LIBRARY_API_KEY must be set at run time (a secret), never baked into the image.
CMD ["python", "agent/server.py", "--http"]
