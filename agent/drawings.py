"""Process drawing layer: citable PFDs, P&IDs, schematics and flowsheets."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRAWINGS = ROOT / "catalog" / "drawings"


def load_drawings(folder=None):
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(pathlib.Path(folder or DRAWINGS).glob("*.json"))]


def summary(drawing):
    return {
        "id": drawing["id"], "title": drawing["title"], "diagram_type": drawing["diagram_type"],
        "publisher": drawing.get("publisher"), "description": drawing.get("description", ""),
        "sectors": drawing.get("sectors", []), "equipment": drawing.get("equipment", []),
        "technologies": drawing.get("technologies", []), "url": drawing["url"],
        "reuse_level": drawing.get("reuse_level", "catalog-only"),
    }


def search_text(drawing):
    """Stored in SQLite and og.drawing.search_text so both search paths index identical words."""
    return "\n".join([
        drawing["title"], " ".join(drawing.get("aliases", [])), drawing["diagram_type"],
        drawing.get("description", ""), drawing.get("publisher", ""),
        " ".join(drawing.get("equipment", [])), " ".join(drawing.get("technologies", [])),
        "pfd pid piping instrumentation diagram process flow flowsheet schematic",
    ])
