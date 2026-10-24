"""Technology cards: loading, block diagrams and comparison tables.

Cards live in catalog/technologies/<id>.json (schema/technology.schema.json). Each one is written
in our own words, and every figure carries the source it was read from.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = ROOT / "catalog" / "technologies"
MATURITY_ORDER = {"commercial": 0, "demonstration": 1, "pilot": 2, "lab": 3}


def load_cards(folder=None):
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(pathlib.Path(folder or CARDS).glob("*.json"))]


def edges(card):
    """(from, to, label) for each flow; a step without "to" flows to the next step."""
    steps = card["process_steps"]
    out = []
    for i, step in enumerate(steps):
        targets = step.get("to")
        if targets is None:
            targets = [steps[i + 1]["id"]] if i + 1 < len(steps) else []
        for t in targets:
            out.append((step["id"], t, step.get("streams", {}).get(t, "")))
    return out


def mermaid(card):
    """Block flow diagram as Mermaid flowchart text."""
    def esc(text):
        return text.replace('"', "'")
    lines = ["flowchart LR"]
    for step in card["process_steps"]:
        equipment = "<br/><small>" + esc(", ".join(step["equipment"])) + "</small>" if step.get("equipment") else ""
        lines.append(f'    {step["id"]}["{esc(step["name"])}{equipment}"]')
    for a, b, label in edges(card):
        lines.append(f"    {a} -->|{esc(label)}| {b}" if label else f"    {a} --> {b}")
    return "\n".join(lines)


def check(card):
    """Problems beyond the JSON schema: dangling step links."""
    ids = {s["id"] for s in card["process_steps"]}
    problems = [f"step link to unknown step '{b}'" for _, b, _ in edges(card) if b not in ids]
    for step in card["process_steps"]:
        problems += [f"stream label for unknown target '{t}'" for t in step.get("streams", {}) if t not in (step.get("to") or ids)]
    return problems


def _range(fig):
    lo, hi = fig.get("low"), fig.get("high")
    value = f"{lo:g}" if lo is not None and (hi is None or lo == hi) else (f"{lo:g}-{hi:g}" if lo is not None else f"up to {hi:g}")
    return f"{value} {fig['unit']}" + (f" ({fig['year']}$)" if "USD" in fig["unit"] and fig.get("year") else "")


def summary(card):
    """Compact row for comparisons."""
    trl = card.get("trl")
    return {
        "id": card["id"], "name": card["name"], "category": card["category"], "maturity": card["maturity"],
        "trl": f"{trl['low']}-{trl['high']}" if trl and trl["low"] != trl["high"] else (str(trl["low"]) if trl else None),
        "applications": card.get("applications", []),
        "suppliers": [s["name"] + (f" ({s['product']})" if s.get("product") else "") for s in card["suppliers"]],
        "key_equipment": card["key_equipment"],
        "costs": [f"{c['metric']}: {_range(c)}" for c in card.get("costs", [])],
        "largest_reference": next((f"{p['name']}: {p.get('capacity', '')}" for p in card.get("reference_plants", [])), None),
    }


def compare(cards, sector=None, maturity=None, application=None):
    hits = [c for c in cards if (not sector or c["sector"] == sector) and (not maturity or c["maturity"] == maturity)
            and (not application or any(application.lower() in a.lower() for a in c.get("applications", [])))]
    hits.sort(key=lambda c: (MATURITY_ORDER[c["maturity"]], c["name"]))
    return [summary(c) for c in hits]


def markdown_page(cards, sector):
    """catalog/index/technologies-<SECTOR>.md: comparison table, then one section per card."""
    hits = [c for c in cards if c["sector"] == sector]
    hits.sort(key=lambda c: (MATURITY_ORDER[c["maturity"]], c["name"]))
    lines = [f"# {sector} technology options", "",
             f"{len(hits)} technologies, from commercial to lab stage. Generated from catalog/technologies/; every figure links to its source.", "",
             "| Technology | Category | Maturity | TRL | Suppliers | Cost figures |", "| --- | --- | --- | --- | --- | --- |"]
    for c in hits:
        s = summary(c)
        lines.append(f"| [{c['name']}](#{c['id']}) | {c['category']} | {c['maturity']} | {s['trl'] or ''} | "
                     f"{'; '.join(s['suppliers'])} | {'<br>'.join(s['costs'])} |")
    for c in hits:
        lines += ["", f"## {c['name']}", f'<a id="{c["id"]}"></a>', "", c["principle"], "", "```mermaid", mermaid(c), "```", "",
                  "**Key equipment:** " + ", ".join(c["key_equipment"]) + "."]
        for title, key in (("Performance", "performance"), ("Costs", "costs")):
            if c.get(key):
                lines += ["", f"**{title}:**"] + [f"- {f['metric']}: {_range(f)}; {f['basis']}. [source]({f['source']['url']})" for f in c[key]]
        if c.get("reference_plants"):
            lines += ["", "**Reference plants:**"] + [
                f"- {p['name']}{', ' + p['country'] if p.get('country') else ''}: {p.get('capacity', '')}; {p.get('status', '')}. [source]({p['source']['url']})"
                for p in c["reference_plants"]]
        if c.get("trl"):
            lines += ["", f"TRL source: [{c['trl']['source'].get('note', 'source')}]({c['trl']['source']['url']})"]
        lines += ["", "Sources: " + ", ".join(f"[{i + 1}]({s['url']})" for i, s in enumerate(c["sources"])) + f". Last reviewed {c['last_reviewed']}."]
    return "\n".join(lines) + "\n"
