from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import selectinload

from api.deps import db_dependency, get_current_user
from api.ingestion.document_ingestion import ingest_uploaded_pdf
from api.models import Document

router = APIRouter(prefix="/documents", tags=["documents"])


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


def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user.get("role") != "Admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return current_user


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


@router.post("", response_model=DocumentRead, status_code=status.HTTP_201_CREATED)
async def upload_document(
    db: db_dependency,
    project_id: UUID = Form(...),
    file: UploadFile = File(...),
    current_user: dict = Depends(require_admin),
):
    _ = current_user
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