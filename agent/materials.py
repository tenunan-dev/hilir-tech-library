"""Engineering material layer: properties with a source for every figure."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
MATERIALS = ROOT / "catalog" / "materials"


def load_materials(folder=None):
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(pathlib.Path(folder or MATERIALS).glob("*.json"))]


def summary(material):
    return {
        "id": material["id"], "name": material["name"],
        "material_category": material["material_category"], "description": material.get("description", ""),
        "spec_metrics": [s["metric"] for s in material.get("specifications", [])],
        "applications": material.get("applications", []), "standards": material.get("standards", []),
        "suppliers": material.get("suppliers", []),
    }


def search_text(material):
    return "\n".join([
        material["name"], " ".join(material.get("aliases", [])), material["material_category"],
        material.get("description", ""), " ".join(material.get("applications", [])),
        " ".join(material.get("standards", [])), " ".join(material.get("suppliers", [])),
        " ".join(f'{s["metric"]} {s.get("unit", "")} {s.get("basis", "")}' for s in material.get("specifications", [])),
        "material specification properties grade strength durability engineering",
    ])
