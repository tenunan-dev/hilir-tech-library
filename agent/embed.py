"""Add embeddings to the search index so search() can fuse keyword and vector results.

    pip install -r requirements-agent.txt fastembed
    python agent/library.py build && python agent/embed.py

fastembed runs a small ONNX model on the CPU; it downloads the model once on first use.
The default is English; pass --model for a multilingual one, e.g.
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 for Bahasa, Thai, Vietnamese or Chinese text.
"""
import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import library  # noqa: E402

DEFAULT_MODEL = "BAAI/bge-small-en-v1.5"


def _model(name):
    from fastembed import TextEmbedding
    return TextEmbedding(model_name=name)


def embed_index(db, model_name=DEFAULT_MODEL, model=None, batch=64):
    import numpy as np
    model = model or _model(model_name)
    rows = db.execute("SELECT rowid, title, text FROM search").fetchall()
    db.execute("DELETE FROM vectors")
    for start in range(0, len(rows), batch):
        part = rows[start:start + batch]
        vecs = model.passage_embed([f"{r['title']}\n{r['text']}" for r in part])
        for row, vec in zip(part, vecs):
            vec = np.asarray(vec, dtype=np.float32)
            db.execute("INSERT INTO vectors VALUES (?, ?)", (row["rowid"], (vec / np.linalg.norm(vec)).tobytes()))
    db.execute("INSERT OR REPLACE INTO info VALUES ('model', ?)", (model_name,))
    db.commit()
    return len(rows)


def load_embedder(db):
    """Return a query embedder matching the index's model, or None when vectors are unavailable."""
    row = db.execute("SELECT value FROM info WHERE key = 'model'").fetchone()
    if not row:
        return None
    try:
        model = _model(row[0])
    except ImportError:
        return None

    def embed(texts):
        import numpy as np
        return [np.asarray(v, dtype=np.float32) / np.linalg.norm(v) for v in model.query_embed(texts)]
    return embed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    args = parser.parse_args()
    print(f"{embed_index(library.connect(), args.model)} rows embedded with {args.model}")
