#!/usr/bin/env bash
# Build the two techlib containers on this Mac for linux/amd64 and stream them into the VPS,
# then recreate the stack from those local images.
#
# Why not CI: GitHub is repo storage only (owner decision, 2026-11-16) — its Actions quota is
# exhausted, so `images.yml` no longer runs and ghcr.io is out of the deploy path. This is the
# mygis runbook (AGENT-PLAYBOOK §3) applied to techlib: build on the Mac, `vps load`, `vps up`.
#
# The images are tagged with the ghcr names the VPS compose already references, so no compose
# change is needed — `vps up` simply finds them locally. Never use `vps deploy techlib` after
# this: it pulls :latest from ghcr and would replace what we just loaded.
#
# Usage:
#   deploy/local-images.sh                 # build, ship, activate, gate
#   deploy/local-images.sh --build-only    # build locally, stop before the transfer
#   deploy/local-images.sh --ship-only     # transfer the images already built here
#   deploy/local-images.sh --dry-run       # print every step, touch nothing
#
# The 4 GB VPS must never build these (both images bake the corpus and warm the fastembed model);
# arm64 → amd64 emulation here is slow (roughly 15-30 min cold), which is the price of no registry.
set -euo pipefail

cd "$(dirname "$0")/.." || exit 1
REPO_ROOT=$(pwd)

SSH_HOST=${SSH_HOST:-agent@15.235.248.33}
SSH_KEY=${SSH_KEY:-$HOME/.ssh/agent_dsh}
STACK=${STACK:-techlib}
PLATFORM=${PLATFORM:-linux/amd64}
UI_IMAGE=ghcr.io/tenunan-dev/hilir-tech-library-ui:latest
API_IMAGE=ghcr.io/tenunan-dev/hilir-tech-library-api:latest

DO_BUILD=1
DO_SHIP=1
DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --build-only) DO_SHIP=0 ;;
    --ship-only) DO_BUILD=0 ;;
    --dry-run) DRY_RUN=1 ;;
    -h|--help) sed -n '2,22p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown flag: $arg (see --help)" >&2; exit 2 ;;
  esac
done

run() {
  if [ "$DRY_RUN" = 1 ]; then
    printf 'DRY  %s\n' "$*"
  else
    printf '+ %s\n' "$*"
    "$@"
  fi
}

# Remote steps run through ssh so the local `run` helper can echo them in a dry run; the payload
# is a single quoted string because `sudo vps` is the only sudo verb allowlisted on the box.
remote() {
  local cmd=$1
  if [ "$DRY_RUN" = 1 ]; then
    printf 'DRY  ssh %s %q\n' "$SSH_HOST" "$cmd"
  else
    printf '+ ssh %s %s\n' "$SSH_HOST" "$cmd"
    ssh -i "$SSH_KEY" -o BatchMode=yes "$SSH_HOST" "$cmd"
  fi
}

say() { printf '\n=== %s\n' "$*"; }

say "preflight"
command -v docker >/dev/null || { echo "docker not found" >&2; exit 1; }
if [ "$DRY_RUN" = 0 ]; then
  docker info >/dev/null 2>&1 || { echo "docker daemon not answering" >&2; exit 1; }
  docker buildx version >/dev/null 2>&1 || { echo "buildx missing (need amd64 builds on arm64)" >&2; exit 1; }
  ssh -i "$SSH_KEY" -o BatchMode=yes -o ConnectTimeout=10 "$SSH_HOST" true \
    || { echo "cannot ssh to $SSH_HOST with $SSH_KEY" >&2; exit 1; }
  # Disk: a load of two baked images needs room, and this box has been near full before.
  used=$(ssh -i "$SSH_KEY" -o BatchMode=yes "$SSH_HOST" "df -P / | awk 'NR==2{print \$5}'" | tr -d '%')
  printf 'VPS / used: %s%%\n' "$used"
  if [ "$used" -ge 90 ]; then
    echo "warning: VPS disk at ${used}% — free space before shipping (asks the owner for a prune list)" >&2
  fi
fi

if [ "$DO_BUILD" = 1 ]; then
  say "build (platform $PLATFORM, tags the VPS compose expects)"
  # --load keeps a single-platform docker-format image in the local store so `docker save` works.
  # --provenance/--sbom off: attestation manifests break the remote `docker load`.
  run docker buildx build --platform "$PLATFORM" --provenance=false --sbom=false --load \
    -f deploy/docker/Dockerfile.frontend -t "$UI_IMAGE" .
  run docker buildx build --platform "$PLATFORM" --provenance=false --sbom=false --load \
    -f deploy/docker/Dockerfile.backend -t "$API_IMAGE" .
fi

if [ "$DO_SHIP" = 1 ]; then
  say "ship both images in one stream, then recreate from local images"
  # One archive, one gzip, one ssh: both images land before `vps up` runs, so the stack never
  # starts on a half-updated pair. `vps up` health-gates and rolls back like `vps deploy` does.
  if [ "$DRY_RUN" = 1 ]; then
    printf 'DRY  docker save %s %s | gzip -1 | ssh %s %q\n' "$UI_IMAGE" "$API_IMAGE" "$SSH_HOST" 'gunzip | sudo vps load'
  else
    docker save "$UI_IMAGE" "$API_IMAGE" | gzip -1 \
      | ssh -i "$SSH_KEY" "$SSH_HOST" 'gunzip | sudo vps load'
  fi
  remote "sudo vps up $STACK"

  say "gate"
  remote "sudo vps status"
  remote "sudo vps health"
  remote "tail -n 6 /var/log/vps-deploy.log"

  cat <<'EOF'

Report these in the conversation:
  1. digest of what went in (from /var/log/vps-deploy.log above),
  2. the health line — must read: mygis 303, techlib-origin 403, tlea-origin 403,
  3. the rollback command: re-load the previous image the same way and `sudo vps restart techlib`.
EOF
fi
