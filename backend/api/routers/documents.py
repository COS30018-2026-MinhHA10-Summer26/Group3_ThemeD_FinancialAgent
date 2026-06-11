import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from uuid import UUID

from dotenv import load_dotenv
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import selectinload

from api.deps import db_dependency, get_current_user
from api.ingestion.document_ingestion import ingest_uploaded_pdf
from api.models import Chunk, Document

load_dotenv()

router = APIRouter(prefix="/documents", tags=["documents"])


# ---------------------------------------------------------------------------
# Supabase storage helpers
# ---------------------------------------------------------------------------

def _normalize_supabase_url(raw_url: str) -> str:
    url = raw_url.rstrip("/")
    if url.endswith("/rest/v1"):
        url = url[: -len("/rest/v1")]
    if url.endswith("/storage/v1"):
        url = url[: -len("/storage/v1")]
    return url


SUPABASE_URL = _normalize_supabase_url(
    os.getenv("SUPABASE_URL") or os.getenv("SUPABASE_PROJECT_URL") or ""
)
SUPABASE_SERVICE_ROLE_KEY = (
    os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    or os.getenv("SUPABASE_SERVICE_ROLE")
    or os.getenv("SUPABASE_ANON_KEY")
    or ""
)
RAW_DATA_BUCKET = os.getenv("SUPABASE_RAW_DATA_BUCKET", "raw_data")


# ---------------------------------------------------------------------------
# Pydantic schemas
# ---------------------------------------------------------------------------

class DocumentRead(BaseModel):
    document_id: UUID
    project_id: UUID
    project_name: str
    file_name: str
    file_type: str | None = None
    file_path: str
    total_page: int
    total_chunk: int
    uploader_email: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class ChunkRead(BaseModel):
    chunk_id: UUID
    document_id: UUID
    content: str
    chunk_index: int
    token_count: int | None = None
    chunk_metadata: dict | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class DocumentChunksResponse(BaseModel):
    document_id: UUID
    file_name: str
    total_chunk: int
    chunks: list[ChunkRead]


class SignedUrlResponse(BaseModel):
    signed_url: str


# ---------------------------------------------------------------------------
# Auth helpers
# ---------------------------------------------------------------------------

def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user.get("role") != "Admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return current_user


# ---------------------------------------------------------------------------
# Conversion helpers
# ---------------------------------------------------------------------------

def document_to_read(document: Document) -> DocumentRead:
    return DocumentRead(
        document_id=document.document_id,
        project_id=document.project_id,
        project_name=document.project.name if document.project else "",
        file_name=document.file_name,
        file_type=document.file_type,
        file_path=document.file_path,
        total_page=document.total_page or 0,
        total_chunk=document.total_chunk or 0,
        uploader_email=document.uploader.email if document.uploader else None,
        created_at=document.created_at,
    )


def chunk_to_read(chunk: Chunk) -> ChunkRead:
    return ChunkRead(
        chunk_id=chunk.chunk_id,
        document_id=chunk.document_id,
        content=chunk.content,
        chunk_index=chunk.chunk_index,
        token_count=chunk.token_count,
        chunk_metadata=chunk.chunk_metadata,
        created_at=chunk.created_at,
    )


def _get_document_or_404(db, document_id: UUID) -> Document:
    document = (
        db.query(Document)
        .options(selectinload(Document.project), selectinload(Document.uploader))
        .filter(Document.document_id == document_id)
        .first()
    )
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Document not found")
    return document


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.get("", response_model=list[DocumentRead])
async def list_documents(
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
    project_id: UUID | None = None,
):
    _ = current_user
    query = db.query(Document).options(selectinload(Document.project), selectinload(Document.uploader))
    if project_id is not None:
        query = query.filter(Document.project_id == project_id)

    documents = query.order_by(Document.created_at.desc(), Document.document_id.desc()).all()
    return [document_to_read(document) for document in documents]


@router.get("/{document_id}", response_model=DocumentRead)
async def get_document(
    document_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Get a single document by ID."""
    _ = current_user
    document = _get_document_or_404(db, document_id)
    return document_to_read(document)


@router.get("/{document_id}/chunks", response_model=DocumentChunksResponse)
async def get_document_chunks(
    document_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Get all chunks for a document, ordered by chunk_index. Embeddings are excluded."""
    _ = current_user
    document = _get_document_or_404(db, document_id)

    chunks = (
        db.query(Chunk)
        .filter(Chunk.document_id == document_id)
        .order_by(Chunk.chunk_index.asc())
        .all()
    )

    return DocumentChunksResponse(
        document_id=document.document_id,
        file_name=document.file_name,
        total_chunk=document.total_chunk or 0,
        chunks=[chunk_to_read(c) for c in chunks],
    )


@router.get("/{document_id}/raw-url", response_model=SignedUrlResponse)
async def get_document_raw_url(
    document_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Generate a time-limited signed URL to access the raw PDF from Supabase Storage."""
    _ = current_user
    document = _get_document_or_404(db, document_id)

    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Supabase storage is not configured.",
        )

    object_path = document.file_path
    encoded_path = urllib.parse.quote(object_path, safe="/-_.~")
    sign_url = f"{SUPABASE_URL}/storage/v1/object/sign/{RAW_DATA_BUCKET}/{encoded_path}"

    body = json.dumps({"expiresIn": 3600}).encode("utf-8")
    request = urllib.request.Request(sign_url, data=body, method="POST")
    request.add_header("Authorization", f"Bearer {SUPABASE_SERVICE_ROLE_KEY}")
    request.add_header("apikey", SUPABASE_SERVICE_ROLE_KEY)
    request.add_header("Content-Type", "application/json")

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        error_body = error.read().decode("utf-8", errors="ignore")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Failed to create signed URL: {error_body or error.reason}",
        ) from error
    except urllib.error.URLError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to connect to Supabase storage",
        ) from error

    signed_path = result.get("signedURL") or result.get("signedUrl") or ""
    if not signed_path:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Supabase returned an empty signed URL",
        )

    # signedURL may be a relative path like /object/sign/bucket/...?token=xxx
    if signed_path.startswith("/"):
        signed_url = f"{SUPABASE_URL}/storage/v1{signed_path}"
    else:
        signed_url = signed_path

    return SignedUrlResponse(signed_url=signed_url)


@router.delete("/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(
    document_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(require_admin),
):
    """Delete a document and all its chunks. Also removes the file from Supabase Storage."""
    _ = current_user
    document = _get_document_or_404(db, document_id)

    # Attempt to delete from Supabase Storage (best-effort)
    if SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY and document.file_path:
        try:
            encoded_path = urllib.parse.quote(document.file_path, safe="/-_.~")
            delete_url = f"{SUPABASE_URL}/storage/v1/object/{RAW_DATA_BUCKET}/{encoded_path}"
            request = urllib.request.Request(delete_url, method="DELETE")
            request.add_header("Authorization", f"Bearer {SUPABASE_SERVICE_ROLE_KEY}")
            request.add_header("apikey", SUPABASE_SERVICE_ROLE_KEY)
            with urllib.request.urlopen(request, timeout=30) as response:
                response.read()
        except Exception:
            pass  # Best-effort: DB record will still be deleted

    db.delete(document)
    db.commit()


@router.post("", response_model=DocumentRead, status_code=status.HTTP_201_CREATED)
async def upload_document(
    db: db_dependency,
    project_id: UUID = Form(...),
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user),
):
    document = ingest_uploaded_pdf(
        db=db,
        upload_file=file,
        project_id=project_id,
        uploaded_by=UUID(str(current_user["id"])),
    )

    document = (
        db.query(Document)
        .options(selectinload(Document.project), selectinload(Document.uploader))
        .filter(Document.document_id == document.document_id)
        .first()
    )
    if not document:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Uploaded document could not be loaded")

    return document_to_read(document)