from pathlib import Path

import yaml
from ai_integration.ingestion.loader import load_documents
from ai_integration.ingestion.chunking import chunk_documents
from ai_integration.rag.embedding_model import EmbeddingModel
from ai_integration.rag.vector_store import VectorStore


PROJECT_ROOT = Path(__file__).resolve().parents[2]



def build_index():
    with (PROJECT_ROOT / "ai_integration" / "config.yaml").open("r", encoding="utf-8") as config_file:
        config = yaml.safe_load(config_file)
    docs = load_documents(str(PROJECT_ROOT / "data" / "raw"))
    chunks = chunk_documents(
        docs,
        config["chunk_size"],
        config["chunk_overlap"]
    )
    texts = [c["text"] for c in chunks]
    model = EmbeddingModel(config["embedding_model"])
    embeddings = model.embed(texts)
    dim = embeddings.shape[1]
    store = VectorStore.create(dim)
    store.add(embeddings, chunks)
    store.save(str(PROJECT_ROOT / "data" / "processed"))