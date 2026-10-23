"""Shared plumbing for collectors: polite HTTP, text extraction, and corpus writing.

Every document written to corpus/ carries the licence terms of its catalog record in its
front matter, so agents can decide whether a passage may be quoted, summarised or only cited.
"""
import datetime
import hashlib
import io
import json
import pathlib
import re
import time
import urllib.parse
import urllib.robotparser

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
MANIFEST = CORPUS / "manifest.jsonl"
USER_AGENT = "og-tech-sources-collector/0.1 (+https://github.com/tenunan-dev/og-tech-sources)"
MIN_DELAY_SECONDS = 3.0

_last_hit = {}
_robots = {}


def load_catalog():
    path = ROOT / "catalog" / "catalog.jsonl"
    return {r["id"]: r for r in map(json.loads, path.read_text(encoding="utf-8").splitlines())}


def collectable(rec):
    """A record may be collected automatically only when its terms were checked and allow it."""
    return (rec["verification"] == "verified"
            and rec["reuse_level"] in ("full-text-open", "full-text-restricted")
            and rec.get("automated_access", "unstated") != "prohibited")


def allowed_by_robots(url):
    parts = urllib.parse.urlsplit(url)
    base = f"{parts.scheme}://{parts.netloc}"
    if base not in _robots:
        parser = urllib.robotparser.RobotFileParser()
        try:
            resp = requests.get(base + "/robots.txt", headers={"User-Agent": USER_AGENT}, timeout=30)
        except requests.RequestException:
            resp = None
        # Same rules as urllib.robotparser.read(): 401/403 means the site refuses us, so
        # disallow everything; another 4xx means no robots.txt, so allow. If we cannot
        # read it at all, stay out.
        if resp is None or resp.status_code in (401, 403) or resp.status_code >= 500:
            parser.disallow_all = True
        elif resp.status_code >= 400:
            parser.allow_all = True
        else:
            parser.parse(resp.text.splitlines())
        _robots[base] = parser
    return _robots[base].can_fetch(USER_AGENT, url)


def fetch(url, **params):
    """GET with robots.txt check and a per-host delay. Returns a requests.Response."""
    if not allowed_by_robots(url):
        raise PermissionError(f"robots.txt disallows {url}")
    host = urllib.parse.urlsplit(url).netloc
    wait = MIN_DELAY_SECONDS - (time.monotonic() - _last_hit.get(host, 0.0))
    if wait > 0:
        time.sleep(wait)
    _last_hit[host] = time.monotonic()
    resp = requests.get(url, params=params or None, headers={"User-Agent": USER_AGENT}, timeout=60)
    resp.raise_for_status()
    return resp


def to_markdown(content, content_type, url=""):
    """Convert an HTML page or PDF to plain Markdown text."""
    if "pdf" in content_type or url.lower().endswith(".pdf"):
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(content))
        return "\n\n".join((page.extract_text() or "").strip() for page in reader.pages).strip()
    import trafilatura
    html = content.decode("utf-8", errors="replace") if isinstance(content, bytes) else content
    return (trafilatura.extract(html, output_format="markdown", include_tables=True, url=url) or "").strip()


def slugify(text, limit=80):
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:limit].rstrip("-") or "untitled"


def known_hashes():
    if not MANIFEST.exists():
        return set()
    return {json.loads(line)["sha256"] for line in MANIFEST.read_text(encoding="utf-8").splitlines() if line}


def write_document(rec, title, url, body, published=None, extra=None):
    """Write one document under corpus/<source id>/ unless identical text is already stored.

    Returns the path written, or None for a duplicate or empty document.
    """
    body = body.strip()
    if not body:
        return None
    digest = hashlib.sha256(body.encode("utf-8")).hexdigest()
    if digest in known_hashes():
        return None
    meta = {
        "source_id": rec["id"],
        "title": title,
        "url": url,
        "published": published,
        "retrieved_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "licence": rec["licence"],
        "reuse_level": rec["reuse_level"],
        "permitted_use": rec.get("permitted_use", "unstated"),
        "sectors": rec["sectors"],
        "disciplines": rec["disciplines"],
        "sha256": digest,
    }
    if rec["reuse_level"] == "full-text-restricted":
        meta["use_note"] = "Private reference copy. Do not redistribute or use commercially; cite the url."
    meta.update(extra or {})
    folder = CORPUS / rec["id"]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{slugify(title)}-{digest[:8]}.md"
    front = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items() if v is not None)
    path.write_text(f"---\n{front}\n---\n\n# {title}\n\n{body}\n", encoding="utf-8")
    with MANIFEST.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"sha256": digest, "path": str(path.relative_to(ROOT)), "url": url}) + "\n")
    return path
