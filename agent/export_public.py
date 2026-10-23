"""Copy the parts of the repo a hosted server needs, leaving out full-text-restricted documents.

    python agent/export_public.py <target-dir>

Used by the Dockerfile so restricted private copies never enter a container image.
"""
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import library  # noqa: E402

KEEP = ("agent", "catalog", "schema", "taxonomy.yaml", "requirements-agent.txt")


def export(target):
    target = pathlib.Path(target)
    for name in KEEP:
        src = library.ROOT / name
        (shutil.copytree if src.is_dir() else shutil.copy2)(src, target / name)
    records = {r["id"]: r for r in library.load_records()}
    kept = skipped = 0
    for path in sorted(library.CORPUS.glob("*/*.md")):
        if path.parent.name.startswith("_"):
            continue
        meta, _ = library.read_document(path)
        level = meta.get("reuse_level") or records.get(meta.get("source_id"), {}).get("reuse_level")
        if level != "full-text-open":
            skipped += 1
            continue
        dest = target / path.relative_to(library.ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, dest)
        kept += 1
    return kept, skipped


if __name__ == "__main__":
    kept, skipped = export(sys.argv[1])
    print(f"{kept} open documents exported, {skipped} restricted documents left out")
