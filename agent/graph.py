"""Knowledge graph over the library: nodes and edges that link catalog sources, corpus documents,
technology cards, register entries, organisations, taxonomy codes and gaps.

Pure Python, no database: tools/load_postgres.py writes the result to Postgres (tables node and edge),
and `python tools/load_postgres.py --dump-graph DIR` writes JSON lines for any other graph tool.
Every edge comes from a recorded fact (a catalog field, a card's sources, a register name) or from a
named matching rule whose evidence is stored in the edge's props. Semantic similar_to edges are added
later in the database from embeddings (see db/schema.sql, refresh_similarity).
"""
import collections
import pathlib
import re

import library
import technologies

ROOT = library.ROOT
GENERIC_NAMES = {"operators", "operator", "various", "research", "major drilling contractors", "service companies",
                 "operators and service companies"}


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def register_id(entry):
    return f"register:{entry['code']}/{slug(entry['name'])[:80]}"


def mention_terms(card):
    """Names and aliases of a card that are specific enough to search document text for."""
    terms = {card["name"].split(" (")[0]}
    terms.update(card.get("aliases", []))
    out = []
    for term in terms:
        term = term.strip()
        if len(term) >= 6 or (len(term) >= 4 and term.isupper()):
            out.append(term)
    return out


def term_count(term, text, lowered=None):
    """Whole-word occurrences of term in text (acronyms case-sensitive). `lowered` is text.lower(), to skip the regex fast."""
    if (lowered if lowered is not None else text.lower()).find(term.lower()) < 0:
        return 0
    flags = 0 if term.isupper() else re.IGNORECASE
    return len(re.findall(rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])", text, flags))


class Graph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def node(self, node_id, kind, label, **props):
        if node_id not in self.nodes:
            self.nodes[node_id] = {"id": node_id, "kind": kind, "label": label, "props": props}
        return node_id

    def edge(self, src, dst, rel, weight=1.0, **props):
        if src in self.nodes and dst in self.nodes and src != dst:
            self.edges.setdefault((src, dst, rel), {"src": src, "dst": dst, "rel": rel, "weight": weight, "props": props})


def build_graph(root=None, corpus=None):
    root = pathlib.Path(root or ROOT)
    corpus = pathlib.Path(corpus or root / "corpus")
    g = Graph()
    labels = library.taxonomy_labels()
    records = library.load_records()
    cards = technologies.load_cards(root / "catalog" / "technologies")
    entries = technologies.load_register(root / "catalog" / "technology-register.yaml", cards)

    for code, name in labels.items():
        kind = "sector" if code in {"UPS", "MID", "GAS", "REF", "PCH", "PWR", "H2", "CCS"} else (
            "discipline" if code in {"PRC", "ROT", "INS", "MAT", "HSE", "DIG"} else "region")
        g.node(f"{kind}:{code}", kind, name)
    for code, name in library.COUNTRIES.items():
        g.node(f"country:{code}", "country", name.rsplit(" ", 1)[0] if code in ("GB", "US") else name)

    # Sources and their organisations
    url_to_source = {}
    for rec in records:
        sid = f"source:{rec['id']}"
        g.node(sid, "source", rec["name"], url=rec["url"], licence=rec["licence"], reuse_level=rec["reuse_level"],
               verification=rec["verification"], source_type=rec["source_type"])
        url_to_source[rec["url"].rstrip("/")] = sid
        org = g.node(f"org:{slug(rec['publisher_org'])}", "org", rec["publisher_org"])
        g.edge(sid, org, "published_by")
        for code in rec.get("sectors", []):
            g.edge(sid, f"sector:{code}", "in_sector")
        for code in rec.get("disciplines", []):
            g.edge(sid, f"discipline:{code}", "covers_discipline")
        for code in rec.get("regions", []):
            g.edge(sid, f"region:{code}", "in_region")
        if rec.get("country"):
            g.edge(sid, f"country:{rec['country']}", "in_country")

    # Technology cards
    card_nodes = {}
    for card in cards:
        tid = g.node(f"technology:{card['id']}", "technology", card["name"], sector=card["sector"], maturity=card["maturity"],
                     category=card["category"])
        card_nodes[card["id"]] = tid
        g.edge(tid, f"sector:{card['sector']}", "in_sector")
        for s in card["sources"]:
            if s.get("source_id"):
                g.edge(tid, f"source:{s['source_id']}", "cites", note=s.get("note", ""), url=s["url"])
        for sup in card["suppliers"]:
            org = g.node(f"org:{slug(sup['name'])}", "org", sup["name"])
            g.edge(tid, org, "supplied_by", product=sup.get("product", ""))
            if sup.get("source_id"):
                g.edge(org, f"source:{sup['source_id']}", "has_source")
        for i, gap in enumerate(card.get("gaps", [])):
            gid = g.node(f"gap:{card['id']}:{i}", "gap", gap["item"], field=gap["field"], reason_code=gap["reason_code"],
                         reason=gap["reason"], action=gap["action"])
            g.edge(tid, gid, "has_gap")
            for w in gap.get("where", []):
                if w.get("source_id"):
                    g.edge(gid, f"source:{w['source_id']}", "look_in", access=w.get("access", ""), hint=w["hint"])

    # Register entries
    for e in entries:
        rid = g.node(register_id(e), "register", e["name"], area=e["area"], maturity=e["maturity"], examples=e["examples"])
        g.edge(rid, f"sector:{e['code']}", "in_sector")
        if e["card"]:
            g.edge(rid, card_nodes[e["card"]], "realised_by")
        for part in e["examples"].split(","):
            name = part.strip()
            if name and name.lower() not in GENERIC_NAMES and len(name) < 60:
                g.edge(rid, g.node(f"org:{slug(name)}", "org", name), "example_supplier", verified=False)

    # Alternatives: cards in one sector that share a category head or an application
    for i, a in enumerate(cards):
        for b in cards[i + 1:]:
            if a["sector"] != b["sector"]:
                continue
            apps_a, apps_b = set(a.get("applications", [])), set(b.get("applications", []))
            jac = len(apps_a & apps_b) / len(apps_a | apps_b) if apps_a | apps_b else 0
            same_head = a["category"].split(" / ")[0].lower() == b["category"].split(" / ")[0].lower()
            weight = jac + (0.5 if same_head else 0)
            if weight >= 0.25:
                g.edge(card_nodes[a["id"]], card_nodes[b["id"]], "alternative_to", weight=round(weight, 3),
                       method="shared category head or applications")

    # Documents: link to their source, sectors, cited cards and mentioned cards
    cited_urls = {s["url"]: card_nodes[c["id"]] for c in cards for s in c["sources"]}
    terms = {c["id"]: mention_terms(c) for c in cards}
    for path in sorted(corpus.glob("*/*.md")):
        if path.parent.name.startswith("_"):
            continue
        meta, body = library.read_document(path)
        rel = str(path.relative_to(corpus.parent))
        did = g.node(f"document:{rel}", "document", meta.get("title") or path.stem, url=meta.get("url", ""),
                     licence=meta.get("licence", ""), reuse_level=meta.get("reuse_level", ""))
        if meta.get("source_id"):
            g.edge(did, f"source:{meta['source_id']}", "from_source")
        for code in library.doc_sectors(meta.get("title", ""), body, meta.get("sectors", [])):
            g.edge(did, f"sector:{code}", "in_sector")
        if meta.get("url") in cited_urls:
            g.edge(cited_urls[meta["url"]], did, "cites_document")
        head = f"{meta.get('title', '')}\n{body}"
        lowered = head.lower()
        for card in cards:
            hits = {t: term_count(t, head, lowered) for t in terms[card["id"]]}
            hits = {t: n for t, n in hits.items() if n}
            total = sum(hits.values())
            in_title = any(term_count(t, meta.get("title", "")) for t in hits)
            if total >= 3 or in_title:
                g.edge(did, card_nodes[card["id"]], "mentions", weight=float(min(total, 50)),
                       method="name or alias match", terms=hits)
    return list(g.nodes.values()), list(g.edges.values())


def stats(nodes, edges):
    return {"nodes": dict(collections.Counter(n["kind"] for n in nodes)),
            "edges": dict(collections.Counter(e["rel"] for e in edges))}
