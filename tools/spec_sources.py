"""The rule that keeps a printed parameter on the record that read it.

A specification belongs to the record whose page printed it. It may sit on an
equipment record only when its `source_url` is a source that record itself
cites; a parameter copied verbatim from another record's page is that record's
evidence, not this one's (finding F3, HILIR health check 2026-11-26: a Risers
record carried 212 specifications, most of them a PV module's and a genset's).

`tools/spec_source_repair.py` applies the rule once to the catalogue;
`tools/build.py` fails the build when a new copy slips back in. Both import this
module so the repair and the gate can never disagree.

Two related facts live here because both need the same normalisation:

* a reader proxy is not a source — `https://r.jina.ai/<publisher-url>` is
  rewritten to `<publisher-url>`, the page an agent should open and cite;
* a chat transcript is not a source either — `chat.mistral.ai`, `chatgpt.com`,
  `claude.ai` … host no page a reader can be sent to.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlsplit

CATALOG = Path(__file__).resolve().parent.parent / "catalog"

PROXIES = ("https://r.jina.ai/", "http://r.jina.ai/")
NON_SOURCE_HOSTS = frozenset({
    "chat.mistral.ai", "chat.openai.com", "chatgpt.com", "claude.ai",
    "gemini.google.com", "copilot.microsoft.com",
})


def norm_url(url: str | None) -> str | None:
    """The publisher URL behind a reader proxy; anything else unchanged."""
    if not url:
        return url
    for prefix in PROXIES:
        if url.startswith(prefix):
            rest = url[len(prefix):]
            return rest if rest.startswith("http") else "https://" + rest
    return url


def host(url: str | None) -> str:
    hostname = urlsplit(norm_url(url) or "").netloc.lower()
    return hostname[4:] if hostname.startswith("www.") else hostname


def source_hosts(rec: dict) -> set[str]:
    return {h for h in (host(s.get("url")) for s in rec.get("sources") or []) if h}


def spec_key(spec: dict) -> tuple:
    """Identity of a printed parameter — the same figure read from the same page."""
    return (norm_url(spec.get("source_url")), str(spec.get("metric")),
            str(spec.get("value")), str(spec.get("unit")))


def records(*patterns: str):
    for pattern in patterns:
        for path in sorted(CATALOG.glob(pattern)):
            yield path, json.loads(path.read_text(encoding="utf-8"))


def spec_index() -> dict[tuple, set[str]]:
    """spec_key -> ids of the records carrying it, across equipment and products."""
    index: dict[tuple, set[str]] = {}
    for _, rec in records("equipment/*.json", "products/*.json"):
        for spec in rec.get("specifications") or []:
            index.setdefault(spec_key(spec), set()).add(rec["id"])
    return index


def foreign_specs(rec: dict, index: dict[tuple, set[str]]) -> list[dict]:
    """This record's specifications that are not its own evidence.

    A spec is foreign when it cites a chat transcript, or when the same printed
    parameter sits on another record and this record does not cite that source.
    A spec whose source this record does cite is kept even if another record
    quotes the same page: a shared OEM datasheet is shared evidence.
    """
    own = source_hosts(rec)
    out = []
    for spec in rec.get("specifications") or []:
        source_host = host(spec.get("source_url"))
        if source_host in NON_SOURCE_HOSTS:
            out.append(spec)
            continue
        if source_host in own:
            continue
        if index.get(spec_key(spec), set()) - {rec["id"]}:
            out.append(spec)
    return out


def vendor_names(vendor_id: str | None, vendors: dict[str, dict]) -> set[str]:
    """The manufacturer's own id plus the aliases its vendor record records."""
    record = vendors.get(vendor_id or "") or {}
    return {vendor_id} | set(record.get("aliases") or []) if vendor_id else set()


def link_is_evidenced(product: dict, equipment_record: dict, vendors: dict[str, dict]) -> bool:
    """`product.equipment` is "equipment classes this product supplies" (schema wording), so the
    class has to name the manufacturer among its vendors. Half the catalogue's links matched an
    equipment *type* instead of a supplier — the Risers class was pointed at by 63 product lines,
    including a solar module's and a generator set's (finding F3, 2026-11-26)."""
    return bool(set(equipment_record.get("vendors") or [])
                & vendor_names(product.get("manufacturer"), vendors))


def vendor_records():
    return {rec["id"]: rec for _, rec in records("vendors/*.json")}
