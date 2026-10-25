"""Shared plumbing for collectors: polite HTTP, text extraction, and corpus writing.

Every document written to corpus/ carries the licence terms of its catalog record in its
front matter, so agents can decide whether a passage may be quoted, summarised or only cited.
"""
import datetime
import hashlib
import io
import ipaddress
import json
import pathlib
import re
import socket
import time
import urllib.parse
import urllib.robotparser

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
CORPUS = ROOT / "corpus"
MANIFEST = CORPUS / "manifest.jsonl"
USER_AGENT = "og-tech-sources-collector/0.1 (+https://github.com/tenunan-dev/og-tech-sources)"
MIN_DELAY_SECONDS = 3.0
ALLOWED_SCHEMES = ("http", "https")
MAX_REDIRECTS = 5
# Document-level licences that make a document open even when its source is restricted overall
# (e.g. arXiv metadata and abstracts are CC0 while the papers keep their own licences).
OPEN_LICENCES = {"CC0-1.0", "CC-BY-4.0", "CC-BY-SA-4.0", "public-domain", "OGL-UK-3.0", "NLOD-2.0"}

_last_hit = {}
_robots = {}

# URL prefixes whose own published terms invite programmatic access even though the host's
# robots.txt bars crawlers. Each entry names the terms page; fetch() still keeps the delay.
ROBOTS_EXCEPTIONS = {
    "https://export.arxiv.org/api/": "https://info.arxiv.org/help/api/tou.html",
}


def load_catalog():
    path = ROOT / "catalog" / "catalog.jsonl"
    return {r["id"]: r for r in map(json.loads, path.read_text(encoding="utf-8").splitlines())}


def collectable(rec):
    """A record may be collected automatically only when its terms were checked and allow it."""
    return (rec["verification"] == "verified"
            and rec["reuse_level"] in ("full-text-open", "full-text-restricted")
            and rec.get("automated_access", "unstated") != "prohibited")


def assert_public(url):
    """Refuse anything but http(s), and loopback, private or link-local destinations.

    The collector only ever fetches public publisher sites, so an internal address or an
    unexpected scheme means a mistaken or tampered record. Unresolvable names are allowed
    through: the request itself will fail anyway, and this keeps offline tests working.
    """
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ALLOWED_SCHEMES:
        raise PermissionError(f"scheme not allowed: {parts.scheme or '(none)'}")
    host = parts.hostname or ""
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast or ip.is_unspecified:
            raise PermissionError(f"non-public destination {host}")


def allowed_by_robots(url):
    if any(url.startswith(prefix) for prefix in ROBOTS_EXCEPTIONS):
        return True
    assert_public(url)
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


def _hop(method, url, headers, params=None, stream=False, redirects=0, raise_status=True):
    """One request hop. Validation sits inline on the request path so it cannot drift from
    the sinks: only http(s) is allowed, the host must resolve to public addresses only,
    robots.txt is honoured, redirects are followed by hand (re-resolving every hop, which
    also narrows DNS-rebinding windows) and the chain is capped at MAX_REDIRECTS."""
    parts = urllib.parse.urlsplit(url)
    if parts.scheme not in ("http", "https"):
        raise PermissionError(f"scheme not allowed: {parts.scheme or '(none)'}")
    host = parts.hostname or ""
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        infos = []  # unresolvable: the request itself will fail; keeps offline tests working
    for info in infos:
        ip = ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved or ip.is_multicast or ip.is_unspecified:
            raise PermissionError(f"non-public destination {host}")
    if not allowed_by_robots(url):
        raise PermissionError(f"robots.txt disallows {url}")
    if method == "HEAD":
        resp = requests.head(url, params=params, headers=headers, timeout=60, allow_redirects=False)
    else:
        resp = requests.get(url, params=params, headers=headers, timeout=60, stream=stream, allow_redirects=False)
    if resp.status_code in (301, 302, 303, 307, 308) and redirects < MAX_REDIRECTS:
        target = urllib.parse.urljoin(url, resp.headers.get("Location", ""))
        if target:
            return _hop("GET" if resp.status_code == 303 else method, target, headers,
                        params, stream, redirects + 1, raise_status)
    if raise_status:
        resp.raise_for_status()
    return resp


def fetch(url, headers=None, **params):
    """GET with a per-host delay; every hop is validated in _hop (scheme, public
    destination, robots.txt, capped redirects). Returns a requests.Response."""
    host = urllib.parse.urlsplit(url).netloc
    wait = MIN_DELAY_SECONDS - (time.monotonic() - _last_hit.get(host, 0.0))
    if wait > 0:
        time.sleep(wait)
    _last_hit[host] = time.monotonic()
    return _hop("GET", url, {"User-Agent": USER_AGENT, **(headers or {})}, params=params or None)


def check_url(url):
    """HEAD a url, GET when HEAD is refused: the link checker's liveness probe.

    Sits on _hop, so it gets the same scheme, destination and redirect validation.
    """
    headers = {"User-Agent": USER_AGENT}
    try:
        resp = _hop("HEAD", url, headers, raise_status=False)
        if resp.status_code in (403, 405, 501):
            resp = _hop("GET", url, headers, stream=True, raise_status=False)
            resp.close()
        moved = resp.url.rstrip("/") != url.rstrip("/")
        return resp.status_code, resp.url if moved else ""
    except requests.RequestException as exc:
        return None, type(exc).__name__


def undouble(text):
    """Collapse words a PDF extractor doubled letter by letter ("PPrroocceessss" -> "Process").

    Faux-bold headings are often drawn twice, so every character comes out twice. Only
    all-letter words of four or more characters with every character doubled are touched,
    so numbers ("1100") and real words stay as they are.
    """
    return re.sub(r"\b[A-Za-z]{4,}\b",
                  lambda m: m.group(0)[::2] if len(m.group(0)) % 2 == 0 and m.group(0)[::2] == m.group(0)[1::2] else m.group(0),
                  text)


def to_markdown(content, content_type, url=""):
    """Convert an HTML page or PDF to plain Markdown text."""
    if "pdf" in content_type or url.lower().endswith(".pdf"):
        from pypdf import PdfReader
        reader = PdfReader(io.BytesIO(content))
        pages = []
        for page in reader.pages:
            try:
                pages.append((page.extract_text() or "").strip())
            except Exception:  # pypdf can fail on single pages (e.g. LimitReachedError); keep the rest
                continue
        return undouble("\n\n".join(pages).strip())
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
    meta.update(extra or {})
    if meta["licence"] in OPEN_LICENCES:
        meta.update(reuse_level="full-text-open", permitted_use="any")
    elif meta["reuse_level"] == "full-text-restricted":
        meta["use_note"] = "Private reference copy. Do not redistribute or use commercially; cite the url."
    folder = CORPUS / rec["id"]
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{slugify(title)}-{digest[:8]}.md"
    front = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in meta.items() if v is not None)
    path.write_text(f"---\n{front}\n---\n\n# {title}\n\n{body}\n", encoding="utf-8")
    with MANIFEST.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps({"sha256": digest, "path": str(path.relative_to(ROOT)), "url": url}) + "\n")
    return path
