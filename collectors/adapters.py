"""Source adapters. Each takes a catalog record and yields (title, url, markdown, published, extra).

Adapters only discover and extract documents; common.write_document decides what is stored.
"""
import pathlib
import xml.etree.ElementTree as ET

from common import CORPUS, fetch, to_markdown

ATOM = "{http://www.w3.org/2005/Atom}"
# Title phrases only: abstract matches pulled in mostly unrelated physics papers, and bare
# "pipeline", "flare" and "compressor" matched software, astronomy and audio papers.
ARXIV_QUERY = " OR ".join(f'ti:"{term}"' for term in (
    "natural gas", "LNG", "oil and gas", "petroleum", "refinery", "petrochemical", "hydrocracking",
    "CO2 capture", "carbon capture plant", "post-combustion capture", "CO2 storage", "electrolyzer", "hydrogen production", "gas turbine",
    "gas compressor", "hydrogen compressor", "gas pipeline", "oil pipeline", "hydrogen pipeline",
    "CO2 pipeline", "reservoir simulation", "wellbore", "gas flaring", "flare gas"))


def parse_feed(xml_text):
    """Return (title, link, published) for each item in an RSS 2.0, RSS 1.0 or Atom feed."""
    root = ET.fromstring(xml_text)
    items = []
    for node in root.iter():
        tag = node.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        fields = {child.tag.split("}")[-1]: child for child in node}
        title = (fields["title"].text or "").strip() if "title" in fields else ""
        link = ""
        if "link" in fields:
            link = (fields["link"].text or fields["link"].get("href") or "").strip()
        # Elements without children are falsy, so test for None explicitly.
        date = next((fields[k] for k in ("pubDate", "date", "published", "updated") if k in fields), None)
        items.append((title, link, (date.text or "").strip() if date is not None else None))
    return items


def rss(rec, limit):
    """Follow each feed item to its page and extract the article text."""
    for feed_url in rec.get("feeds", []):
        for title, link, published in parse_feed(fetch(feed_url).text)[:limit]:
            if not link:
                continue
            resp = fetch(link)
            yield title, link, to_markdown(resp.content, resp.headers.get("Content-Type", ""), link), published, None


def arxiv(rec, limit):
    """Metadata and abstracts only: arXiv metadata is CC0, full texts keep per-paper licences."""
    resp = fetch("https://export.arxiv.org/api/query", search_query=ARXIV_QUERY,
                 sortBy="submittedDate", sortOrder="descending", max_results=limit)
    root = ET.fromstring(resp.text)
    for entry in root.findall(f"{ATOM}entry"):
        title = " ".join(entry.findtext(f"{ATOM}title", "").split())
        link = entry.findtext(f"{ATOM}id", "")
        abstract = " ".join(entry.findtext(f"{ATOM}summary", "").split())
        authors = [a.findtext(f"{ATOM}name", "") for a in entry.findall(f"{ATOM}author")]
        body = f"**Authors:** {', '.join(authors)}\n\n**Abstract:** {abstract}"
        yield title, link, body, entry.findtext(f"{ATOM}published"), {"content": "metadata-and-abstract", "licence": "CC0-1.0"}


def osti(rec, limit):
    """OSTI records API. Abstracts are stored; full text is left to per-document rights review."""
    resp = fetch("https://www.osti.gov/api/v1/records", headers={"Accept": "application/json"},  # XML by default
                 q="hydrogen OR \"carbon capture\" OR refining OR \"natural gas\" OR petrochemical",
                 sort="publication_date desc", rows=limit)
    for item in resp.json():
        title = item.get("title", "Untitled")
        link = next((l["href"] for l in item.get("links", []) if l.get("rel") == "citation"),
                    f"https://www.osti.gov/biblio/{item.get('osti_id', '')}")
        body = f"**Authors:** {'; '.join(item.get('authors', []))}\n\n**Abstract:** {item.get('description', '')}"
        yield title, link, body, item.get("publication_date"), {"content": "metadata-and-abstract",
                                                               "rights_note": "Check the record's rights before storing full text."}


def manual(rec, limit):
    """Files placed by hand in corpus/_inbox/<source id>/ (PDF or HTML), for sites that ban crawlers.

    A sidecar <file>.url holding the original URL is used as the citation when present.
    """
    inbox = CORPUS / "_inbox" / rec["id"]
    if not inbox.is_dir():
        return
    for path in sorted(inbox.iterdir())[:limit]:
        if path.suffix.lower() not in (".pdf", ".html", ".htm"):
            continue
        sidecar = path.with_suffix(path.suffix + ".url")
        url = sidecar.read_text(encoding="utf-8").strip() if sidecar.exists() else rec["url"]
        kind = "application/pdf" if path.suffix.lower() == ".pdf" else "text/html"
        yield path.stem.replace("-", " "), url, to_markdown(path.read_bytes(), kind, url), None, {"collected": "manual"}


# Source id -> adapter. Records with feeds use rss unless listed here.
ADAPTERS = {"arxiv": arxiv, "osti": osti}


def adapter_for(rec):
    if rec["id"] in ADAPTERS:
        return ADAPTERS[rec["id"]]
    if rec.get("feeds"):
        return rss
    return None
