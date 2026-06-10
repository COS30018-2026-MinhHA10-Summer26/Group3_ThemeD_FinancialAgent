"""
Temporary in-memory PDF processing for RAG chat.

Extracts text/tables from an uploaded PDF, chunks it, and creates embeddings
without persisting anything to the database.  The resulting IndexedChunk list
is merged with DB chunks inside HybridMultiQueryRetriever for a single query
session.
"""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from langchain_core.documents import Document

from api.ingestion.chunking import chunk_documents, embedding_model
from api.ingestion.pdf_extractor import extract_documents

if TYPE_CHECKING:
    from api.generate_answer import IndexedChunk


def process_pdf_for_chat(pdf_bytes: bytes, filename: str) -> "list[IndexedChunk]":
    """Process a PDF upload into in-memory IndexedChunks for chat retrieval.

    Pipeline:
        1. extract_documents()  – parse PDF into sections (text + tables + images)
        2. chunk_documents()    – split sections into retrieval-sized chunks
        3. embed_documents()    – create vector embeddings for each chunk
        (summarise_chunks is intentionally skipped for speed)

    Returns a list of IndexedChunk ready to be merged with DB chunks.
    """
    # Lazy import to avoid circular dependency at module level
    from api.generate_answer import IndexedChunk

    # 1. Extract sections from PDF bytes
    sections = extract_documents(pdf_bytes, filename)
    if not sections:
        return []

    # 2. Chunk the extracted sections
    chunks = chunk_documents(sections, chunk_size=400, overlap=50)
    if not chunks:
        return []

    # 3. Create embeddings (skip summarise_chunks for speed)
    texts = [chunk["text"] for chunk in chunks]
    embeddings = embedding_model.embed_documents(texts)

    # 4. Build IndexedChunk objects with upload-specific metadata
    indexed_chunks: list[IndexedChunk] = []
    for chunk, embedding in zip(chunks, embeddings):
        metadata = dict(chunk.get("metadata") or {})
        chunk_id = str(uuid.uuid4())

        page_content = chunk["text"]
        page_metadata = {
            "_chunk_id": chunk_id,
            "chunk_id": chunk_id,
            "source_file": filename,
            "source_type": "user_upload",
            **metadata,
        }

        indexed_chunks.append(
            IndexedChunk(
                document=Document(page_content=page_content, metadata=page_metadata),
                embedding=list(embedding),
            )
        )

    return indexed_chunks
