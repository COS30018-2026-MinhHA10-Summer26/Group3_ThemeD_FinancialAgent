"""
image_table_after_chunking.py

Queries the database for all projects whose name contains "paper" and returns
the tables (converted from HTML to Markdown) and base64-encoded images found in
each chunk's metadata (original_content -> tables_html / images_base64).

Only chunks that contain at least one table OR one image are included in the output.

Standalone file — does NOT import from backend/api or from text_after_chunking to
avoid path/import conflicts. All required SQLAlchemy models are defined inline.
"""

from __future__ import annotations

import json
import os
from html.parser import HTMLParser

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

_engine2 = create_engine(_DATABASE_URL)
_Session2 = sessionmaker(autocommit=False, autoflush=False, bind=_engine2)

Base2 = declarative_base()


# ---------------------------------------------------------------------------
# Inline SQLAlchemy models (suffixed *Media to avoid mapper conflicts)
# ---------------------------------------------------------------------------

class ProjectMedia(Base2):
    __tablename__ = "projects"

    project_id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String(255), nullable=False)

    documents = relationship("DocumentMedia", back_populates="project")


class DocumentMedia(Base2):
    __tablename__ = "documents"

    document_id = Column(UUID(as_uuid=True), primary_key=True)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.project_id", ondelete="CASCADE"), nullable=False)
    file_name = Column(String(255), nullable=False)

    project = relationship("ProjectMedia", back_populates="documents")
    chunks = relationship("ChunkMedia", back_populates="document", order_by="ChunkMedia.chunk_index")


class ChunkMedia(Base2):
    __tablename__ = "chunks"

    chunk_id = Column(UUID(as_uuid=True), primary_key=True)
    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.document_id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    chunk_index = Column(Integer, nullable=False)
    chunk_metadata = Column("metadata", JSON)

    document = relationship("DocumentMedia", back_populates="chunks")


# ---------------------------------------------------------------------------
# HTML → Markdown table converter (stdlib only)
# ---------------------------------------------------------------------------

class _TableParser(HTMLParser):
    """Minimal HTML parser that extracts rows and cells from a single <table>."""

    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[str]] = []
        self._current_row: list[str] | None = None
        self._current_cell: str | None = None
        self._in_cell = False

    def handle_starttag(self, tag: str, attrs) -> None:  # noqa: ANN001
        tag = tag.lower()
        if tag == "tr":
            self._current_row = []
        elif tag in ("th", "td"):
            self._current_cell = ""
            self._in_cell = True

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in ("th", "td"):
            if self._current_row is not None and self._current_cell is not None:
                self._current_row.append(self._current_cell.strip())
            self._current_cell = None
            self._in_cell = False
        elif tag == "tr":
            if self._current_row is not None:
                self.rows.append(self._current_row)
            self._current_row = None

    def handle_data(self, data: str) -> None:
        if self._in_cell and self._current_cell is not None:
            self._current_cell += data


def html_table_to_markdown(html: str) -> str:
    """Convert a basic HTML table to Markdown table format.

    Uses only the Python stdlib html.parser — no external dependencies.
    The first row is treated as the header row; a separator line is inserted
    after it.  Remaining rows are data rows.
    """
    parser = _TableParser()
    try:
        parser.feed(html)
    except Exception:
        return html  # fallback: return raw HTML if parsing fails

    rows = parser.rows
    if not rows:
        return ""

    lines: list[str] = []

    # Header row
    header = rows[0]
    lines.append("| " + " | ".join(cell.replace("|", "\\|") for cell in header) + " |")
    lines.append("| " + " | ".join("---" for _ in header) + " |")

    # Data rows
    for row in rows[1:]:
        # Pad or trim to match header column count
        padded = list(row) + [""] * max(0, len(header) - len(row))
        padded = padded[: len(header)]
        lines.append("| " + " | ".join(cell.replace("|", "\\|") for cell in padded) + " |")

    return "\n".join(lines)


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


def _extract_media(metadata: dict) -> tuple[list[str], list[str]]:
    """
    Extract tables_html and images_base64 from metadata -> original_content.

    Returns (tables_html, images_base64) as lists of strings.
    """
    original_content = metadata.get("original_content")
    if original_content is None:
        return [], []
    if isinstance(original_content, str):
        try:
            original_content = json.loads(original_content)
        except json.JSONDecodeError:
            return [], []
    if not isinstance(original_content, dict):
        return [], []

    tables_html: list[str] = original_content.get("tables_html") or []
    images_base64: list[str] = original_content.get("images_base64") or []

    # Ensure we always return plain lists of strings
    if not isinstance(tables_html, list):
        tables_html = []
    if not isinstance(images_base64, list):
        images_base64 = []

    return tables_html, images_base64


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def query_media_chunks() -> dict:
    """
    Query all projects with 'paper' in the name and return their media chunks
    (tables converted to Markdown + base64 images).  Only chunks that have at
    least one table or one image are included.

    Returns
    -------
    dict of shape:
        {
            paper_name: {
                document_file_name: [
                    {
                        "chunk_id": str,
                        "chunk_index": int,
                        "source": str,
                        "tables_markdown": [str, ...],
                        "images_base64": [str, ...],
                    },
                    ...   # only chunks with at least one table or image
                ],
                ...
            },
            ...
        }
    """
    result: dict = {}

    with _Session2() as db:
        projects = (
            db.query(ProjectMedia)
            .filter(ProjectMedia.name.ilike("%paper%"))
            .order_by(ProjectMedia.name)
            .all()
        )

        for project in projects:
            paper_entry: dict = {}

            for document in project.documents:
                media_chunks: list[dict] = []

                chunks = (
                    db.query(ChunkMedia)
                    .filter(ChunkMedia.document_id == document.document_id)
                    .order_by(ChunkMedia.chunk_index.asc())
                    .all()
                )

                for chunk in chunks:
                    metadata = _parse_metadata(chunk.chunk_metadata)
                    tables_html, images_base64 = _extract_media(metadata)

                    # Skip chunks with no media content
                    if not tables_html and not images_base64:
                        continue

                    tables_markdown = [html_table_to_markdown(t) for t in tables_html]

                    media_chunks.append(
                        {
                            "chunk_id": str(chunk.chunk_id),
                            "chunk_index": chunk.chunk_index,
                            "source": document.file_name,
                            "tables_markdown": tables_markdown,
                            "images_base64": images_base64,
                        }
                    )

                paper_entry[document.file_name] = media_chunks

            result[project.name] = paper_entry

    return result


def query_media_chunks_for_project(project_name: str) -> dict:
    """
    Same as query_media_chunks() but filtered to a single project by exact name.

    Parameters
    ----------
    project_name:
        Exact name of the project to retrieve.

    Returns
    -------
    dict of shape:
        {
            document_file_name: [media_chunk_dict, ...],
            ...
        }
    """
    all_data = query_media_chunks()
    return all_data.get(project_name, {})
