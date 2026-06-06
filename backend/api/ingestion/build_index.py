import yaml
from api.ingestion.loader import load_documents
from api.ingestion.chunking import chunk_documents
from api.rag.embedding_model import EmbeddingModel
from api.rag.vector_store import VectorStore



def build_index():
    config = yaml.safe_load(open("../config.yaml"))
    docs = load_documents("data/raw")
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
    store.save("data/processed")