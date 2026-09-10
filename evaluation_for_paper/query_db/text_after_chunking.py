"""
text_after_chunking.py

Queries the database for all projects whose name contains "paper" and returns
the raw text content from each chunk's metadata (original_content -> raw_text),
organised as a nested dict: paper_name -> document_file_name -> list of chunk dicts.

Standalone file — does NOT import from backend/api to avoid path/import conflicts.
All required SQLAlchemy models are defined inline.
"""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv
from sqlalchemy import Column, ForeignKey, Integer, JSON, String, Text, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# ---------------------------------------------------------------------------
# Environment / DB setup
# ---------------------------------------------------------------------------

dotenv_path = os.path.join(os.path.dirname(__file__), "..", "backend", ".env")
load_dotenv(dotenv_path=dotenv_path, override=True)

_DATABASE_URL = os.getenv("SQL_ALCHEMY_DATABASE_URL")

_engine1 = create_engine(_DATABASE_URL)
_Session1 = sessionmaker(autocommit=False, autoflush=False, bind=_engine1)

Base1 = declarative_base()


# ---------------------------------------------------------------------------
# Inline SQLAlchemy models (suffixed *Txt to avoid mapper conflicts)
# ---------------------------------------------------------------------------

class ProjectTxt(Base1):
    __tablename__ = "projects"

    project_id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)

    documents = relationship("DocumentTxt", back_populates="project")


class DocumentTxt(Base1):
    __tablename__ = "documents"

    document_id = Column(UUID(as_uuid=True), primary_key=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id", ondelete="CASCADE"), nullable=False)
    file_name = Column(String(255), nullable=False)

    project = relationship("ProjectTxt", back_populates="documents")
    chunks = relationship("ChunkTxt", back_populates="document", order_by="ChunkTxt.chunk_index")


class ChunkTxt(Base1):
    __tablename__ = "chunks"

    chunk_id = Column(UUID(as_uuid=True), primary_key=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.document_id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    chunk_index = Column(Integer, nullable=False)
    chunk_metadata = Column("metadata", JSON)

    document = relationship("DocumentTxt", back_populates="chunks")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_metadata(raw) -> dict:
    """Return chunk_metadata as a dict, parsing from JSON string if needed."""
    if raw is None:
        return {}
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {}
    if isinstance(raw, dict):
        return raw
    return {}


def _extract_text(metadata: dict) -> str:
    """Extract raw_text from metadata -> original_content -> raw_text."""
    original_content = metadata.get("original_content")
    if original_content is None:
        return ""
    if isinstance(original_content, str):
        try:
            original_content = json.loads(original_content)
        except json.JSONDecodeError:
            return ""
    if isinstance(original_content, dict):
        return original_content.get("raw_text", "") or ""
    return ""


def _extract_page(metadata: dict) -> int:
    """Return page number from metadata, trying common key names."""
    for key in ("page_number", "page"):
        value = metadata.get(key)
        if value is not None:
            try:
                return int(value)
            except (TypeError, ValueError):
                pass
    return 0


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def query_text_chunks() -> dict:
    """
    Query all projects with 'paper' in the name and return their text chunks.

    Returns
    -------
    dict of shape:
        {
            paper_name: {
                document_file_name: [
                    {
                        "chunk_id": str,
                        "chunk_index": int,
                        "text": str,
                        "source": str,
                        "page": int,
                    },
                    ...
                ],
                ...
            },
            ...
        }
    """
    result: dict = {}

    with _Session1() as db:
        projects = (
            db.query(ProjectTxt)
            .filter(ProjectTxt.name.ilike("%paper%"))
            .order_by(ProjectTxt.name)
            .all()
        )

        for project in projects:
            paper_entry: dict = {}

            for document in project.documents:
                chunks_list = []

                chunks = (
                    db.query(ChunkTxt)
                    .filter(ChunkTxt.document_id == document.document_id)
                    .order_by(ChunkTxt.chunk_index.asc())
                    .all()
                )

                for chunk in chunks:
                    metadata = _parse_metadata(chunk.chunk_metadata)
                    text = _extract_text(metadata)
                    page = _extract_page(metadata)

                    chunks_list.append(
                        {
                            "chunk_id": str(chunk.chunk_id),
                            "chunk_index": chunk.chunk_index,
                            "text": text,
                            "source": document.file_name,
                            "page": page,
                        }
                    )

                paper_entry[document.file_name] = chunks_list

            result[project.name] = paper_entry

    return result


def query_text_chunks_for_project(project_name: str) -> dict:
    """
    Same as query_text_chunks() but filtered to a single project by exact name.

    Parameters
    ----------
    project_name:
        Exact name of the project to retrieve.

    Returns
    -------
    dict of shape:
        {
            document_file_name: [chunk_dict, ...],
            ...
        }
    """
    all_data = query_text_chunks()
    return all_data.get(project_name, {})
