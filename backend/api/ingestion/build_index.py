import yaml
from api.ingestion.loader import load_documents
from api.ingestion.chunking import chunk_documents, summarise_chunks
from api.ingestion.multi_model_chunk import chunk_by_title
from api.rag.embedding_model import EmbeddingModel
from api.rag.vector_store import VectorStore



def build_index():
    config = yaml.safe_load(open("../config.yaml"))
    chunks = chunk_by_title(
        max_characters=3000,
        new_after_n_chars=2400,
        combine_text_under_n_chars=500
    )
    summarised_chunks = summarise_chunks(chunks)
    texts = [c["text"] for c in summarised_chunks]
    model = EmbeddingModel(config["embedding_model"])
    embeddings = model.embed(texts)
    dim = embeddings.shape[1]
    store = VectorStore.create(dim)
    store.add(embeddings, summarised_chunks)
    store.save("data/processed")