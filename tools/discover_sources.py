#!/usr/bin/env python3
"""Channel-1 source discovery: scan the library's own text for uncatalogued sources.

Two extractions:
  urls     — every http(s) URL in corpus markdown (excluding _inbox), technology-card
             evidence (sources[].url, gaps[].where[].url/hint text) and gaps.md, deduped
             against catalog URL domains and per-document hosts (DOIs, preprints).
             Strict mode (default): only domains cited from >= 2 distinct documents.
  phrases  — capitalized org-like phrases from GAP HINTS ONLY (card gaps[].where[].hint
             and catalog/index/gaps.md cells; corpus body text is too noisy without NER).
             Strict mode (default): org-suffix match or >= 2 hint mentions.

Emits candidates.jsonl rows (one JSON object per line) on stdout; count to stderr.
Pass --all for the unfiltered output (report/triage use). Pure stdlib, offline.

    python tools/discover_sources.py [--all] [--no-urls | --no-phrases]
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"
CORPUS = ROOT / "corpus"

STOP_PREFIXES = (
    "the ", "a ", "an ", "no ", "web ", "add ", "look ", "check ", "search ", "open ",
    "full ", "exhibit ", "cross", "download ", "record ", "figure ", "table ",
    "about ", "above", "absolute", "abstract",
)
STOP_WORDS = {
    "wikipedia", "article", "only", "text", "page", "pages", "pdf", "url", "urls",
    "catalog", "catalogue", "corpus", "source", "sources", "report", "reports",
    "database", "handbook", "standard", "standards", "guideline", "press", "release",
    "news", "site", "website", "paper", "papers", "study", "studies", "data",
}
ORG_RE = re.compile(r"\b([A-Z][A-Za-z&./\-]*[A-Za-z](?:\s+[A-Z][A-Za-z&./\-]*[A-Za-z]){0,3})\b")
URL_RE = re.compile(r"https?://[^\s\)\]>\"'\]]+")
PHRASE_NOISE = re.compile(
    r"^(open|full|partial|surging|steam|rankine|methanation|visbreaking|photocatalytic|"
    r"sodium|low|liquid|vendor|peer|simulator|propylene|sulfate|flaring|drilling|"
    r"directional|dividing|ether|flame|hydrogen|chloralkali|performance|progressive|"
    r"absorber|abandonment|abnormal|acetic|zhejiang)\b", re.I)
ORG_SUFFIX_RE = re.compile(
    r"\b(institute|association|agency|authority|bureau|laborator(y|ies)|consortium|"
    r"council|society|programme|program|initiative|partnership|commission|foundation|"
    r"university|centre|center|magazine|journal|weekly|register|intelligence|research|"
    r"group|corp|corporation|inc|ltd|plc|gmbh|ministry|directorate|"
    r"organization|organisation|fund|bank|board|laboratory|services|international)\b", re.I)
DOC_HOSTS_RE = re.compile(
    r"(doi\.org|arxiv\.org|sciencedirect|springer|wiley|tandfonline|acs\.org|ieee|rsc\.org|"
    r"researchgate|semanticscholar|scholar\.google|mdpi\.com|osti\.gov|nrel\.gov|pnnl\.gov|"
    r"onepetro\.org|scribd\.com|docs\.google|dropbox|energy\.gov|netl\.doe|hydrogen\.energy)",
    re.I)


def load_known():
    """Known ids/names/aliases/publishers (lowercase) + catalog URL domains."""
    names, domains = set(), set()
    for line in open(CATALOG / "catalog.jsonl"):
        s = json.loads(line)
        for key in ("id", "name", "publisher_org"):
            if s.get(key):
                names.add(s[key].lower())
        for a in s.get("aliases", []) or []:
            names.add(a.lower())
        d = _domain(s.get("url", ""))
        if d:
            domains.add(d)
    vf = CATALOG / "vendors.jsonl"
    if vf.exists():
        for line in open(vf):
            v = json.loads(line)
            names.add(v["name"].lower())
            for a in v.get("aliases", []) or []:
                names.add(a.lower())
    return names, domains


def _domain(url):
    m = re.match(r"https?://([^/\s]+)", url or "")
    if not m:
        return None
    return m.group(1).lower().removeprefix("www.")


def load_gap_hints():
    """Hint strings from every technology card + gaps.md table cells."""
    hints = []
    for card in (CATALOG / "technologies").glob("*.json"):
        c = json.loads(card.read_text(encoding="utf-8", errors="ignore"))
        for g in c.get("gaps", []):
            for w in g.get("where", []) or []:
                if w.get("hint"):
                    hints.append(w["hint"])
    gaps = CATALOG / "index" / "gaps.md"
    if gaps.exists():
        for line in gaps.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("|") and "---" not in line:
                hints.extend(cell.strip() for cell in line.split("|"))
    return hints


def extract_urls(text):
    return {u.rstrip(".,;") for u in URL_RE.findall(text)}


def extract_phrases(hint):
    out = set()
    for m in ORG_RE.findall(hint):
        phrase = m.strip()
        low = phrase.lower()
        if len(phrase) < 4 or len(phrase) > 60 or PHRASE_NOISE.match(phrase):
            continue
        if any(low.startswith(p) for p in STOP_PREFIXES):
            continue
        words = low.split()
        if all(w in STOP_WORDS for w in words):
            continue
        out.add(phrase)
    return out


def known_phrase(phrase, names):
    low = phrase.lower()
    if low in names:
        return True
    head = low.split()[0]
    return head in names and len(low.split()) <= 3


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--all", action="store_true",
                    help="emit every hit, not only strict ones")
    ap.add_argument("--no-urls", action="store_true")
    ap.add_argument("--no-phrases", action="store_true")
    args = ap.parse_args()

    names, domains = load_known()
    today = "2026-10-29"

    # Phrases: collect with mention counts across hints (keep first original casing).
    if not args.no_phrases:
        counts = {}
        for hint in load_gap_hints():
            for p in extract_phrases(hint):
                if known_phrase(p, names):
                    continue
                low = p.lower()
                if low not in counts:
                    counts[low] = {"n": 0, "phrase": p}
                counts[low]["n"] += 1
        for low, item in sorted(counts.items()):
            n = item["n"]
            words = low.split()
            strict = (len(words) > 1 and (n >= 2 or ORG_SUFFIX_RE.search(low))) or \
                     (len(words) == 1 and low.isupper() and n >= 2)
            if not (args.all or strict):
                continue
            row = {"name": item["phrase"], "url": None, "channel": "citation-mining",
                   "first_seen": today, "kind": "source", "status": "queued",
                   "registered_as": None,
                   "note": f"discover_sources.py: org phrase in gap hints (mentions: {n})"}
            print(json.dumps(row, ensure_ascii=False))

    # URLs: collect domain -> set of citing documents.
    if not args.no_urls:
        url_docs = {}
        for md in CORPUS.rglob("*.md"):
            if "_inbox" in md.parts:
                continue
            for u in extract_urls(md.read_text(encoding="utf-8", errors="ignore")):
                d = _domain(u)
                if d and d not in domains and not DOC_HOSTS_RE.search(d):
                    url_docs.setdefault(d, {"docs": set(), "url": u})["docs"].add(md.name)
        for card in (CATALOG / "technologies").glob("*.json"):
            for u in extract_urls(card.read_text(encoding="utf-8", errors="ignore")):
                d = _domain(u)
                if d and d not in domains and not DOC_HOSTS_RE.search(d):
                    url_docs.setdefault(d, {"docs": set(), "url": u})["docs"].add(card.name)
        for d, item in sorted(url_docs.items()):
            strict = len(item["docs"]) >= 2
            if not (args.all or strict):
                continue
            row = {"name": item["url"], "url": item["url"], "channel": "citation-mining",
                   "first_seen": today, "kind": "source", "status": "queued",
                   "registered_as": None,
                   "note": f"discover_sources.py: domain {d} cited by {len(item['docs'])} docs"}
            print(json.dumps(row, ensure_ascii=False))

    return 0


if __name__ == "__main__":
    sys.exit(main())
