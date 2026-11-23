"""Product catalog layer: one record per vendor product line, with printed specifications."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PRODUCTS = ROOT / "catalog" / "products"


def load_products(folder=None):
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(pathlib.Path(folder or PRODUCTS).glob("*.json"))]


def summary(product):
    return {
        "id": product["id"], "name": product["name"], "manufacturer": product["manufacturer"],
        "product_type": product["product_type"], "description": product.get("description", ""),
        "equipment": product.get("equipment", []),
        "spec_metrics": [s["metric"] for s in product.get("specifications", [])],
        "url": product["url"],
    }


def search_text(product):
    """The same string is stored in SQLite and og.product.search_text, so both paths rank alike."""
    return "\n".join([
        product["name"], " ".join(product.get("aliases", [])), product["manufacturer"],
        product.get("description", ""), " ".join(product.get("equipment", [])),
        " ".join(f'{s["metric"]} {s.get("unit", "")} {s.get("basis", "")}' for s in product.get("specifications", [])),
        "product catalog specification datasheet vendor product line",
    ])
