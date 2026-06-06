import mimetypes
import os
import re
import shutil
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from uuid import UUID, uuid4

import yaml
from dotenv import load_dotenv
from fastapi import HTTPException, UploadFile, status
from unstructured.chunking.title import chunk_by_title
from unstructured.partition.pdf import partition_pdf

from api.ingestion.chunking import embedding_model, summarise_chunks
from api.ingestion.pdf_extractor import extract_documents
from api.models import Chunk, Document

load_dotenv()


def normalize_supabase_url(raw_url: str) -> str:
    url = raw_url.rstrip("/")
    if url.endswith("/rest/v1"):
        url = url[: -len("/rest/v1")]
    if url.endswith("/storage/v1"):
        url = url[: -len("/storage/v1")]
    return url


SUPABASE_URL = normalize_supabase_url(os.getenv("SUPABASE_URL") or os.getenv("SUPABASE_PROJECT_URL") or "")
SUPABASE_SERVICE_ROLE_KEY = (
    os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    or os.getenv("SUPABASE_SERVICE_ROLE")
    or os.getenv("SUPABASE_ANON_KEY")
    or ""
)
RAW_DATA_BUCKET = os.getenv("SUPABASE_RAW_DATA_BUCKET", "raw_data")


def require_storage_config() -> tuple[str, str]:
    if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Supabase storage is not configured. Set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY.",
        )

    return SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY


def sanitize_filename(filename: str) -> str:
    name = Path(filename).name
    stem = Path(name).stem
    suffix = Path(name).suffix.lower() or ".pdf"
    safe_stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip("-_.") or "document"
    return f"{safe_stem}{suffix}"


def save_upload_to_temp_file(upload_file: UploadFile) -> str:
    suffix = Path(upload_file.filename or "document.pdf").suffix or ".pdf"
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    try:
        shutil.copyfileobj(upload_file.file, temp_file)
        return temp_file.name
    finally:
        temp_file.close()


def upload_pdf_to_supabase_storage(file_path: str, object_path: str, content_type: str) -> None:
    # if not SUPABASE_URL or not SUPABASE_SERVICE_ROLE_KEY:
    #     return

    supabase_url, service_role_key = require_storage_config()
    encoded_object_path = urllib.parse.quote(object_path, safe="/-_.~")
    request_url = f"{supabase_url}/storage/v1/object/{RAW_DATA_BUCKET}/{encoded_object_path}"

    with open(file_path, "rb") as file_handle:
        request = urllib.request.Request(
            request_url,
            data=file_handle.read(),
            method="POST",
        )

    request.add_header("Authorization", f"Bearer {service_role_key}")
    request.add_header("apikey", service_role_key)
    request.add_header("x-upsert", "true")
    request.add_header("Content-Type", content_type or "application/pdf")

    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            response.read()
    except urllib.error.HTTPError as error:
        error_message = error.read().decode("utf-8", errors="ignore")
        detail = error_message or error.reason or "Failed to upload file to Supabase storage"
        raise HTTPException(status_code=error.code or status.HTTP_502_BAD_GATEWAY, detail=detail) from error
    except urllib.error.URLError as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to connect to Supabase storage",
        ) from error


def load_ingestion_config() -> dict:
    config_path = Path(__file__).resolve().parents[1] / "config.yaml"
    with open(config_path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def extract_total_pages(documents) -> int:
    page_numbers = set()
    for document in documents:
        page_number = document.get("page")
        if isinstance(page_number, int) and page_number >= 0:
            page_numbers.add(page_number + 1)
    return max(page_numbers) if page_numbers else 0


def _normalize_original_content(metadata: dict, raw_text: str) -> dict:
    original_content = metadata.get("original_content", {})
    if isinstance(original_content, str):
        try:
            import json

            original_content = json.loads(original_content)
        except Exception:
            original_content = {"raw_text": original_content}

    if not isinstance(original_content, dict):
        original_content = {}

    original_content.setdefault("raw_text", raw_text)
    original_content.setdefault("tables_html", [])
    original_content.setdefault("images_base64", [])
    return original_content


def build_chunk_metadata(document_id: UUID, chunk_index: int, chunk: dict) -> dict:
    metadata = dict(chunk.get("metadata") or {})
    raw_text = chunk.get("text", "")
    original_content = _normalize_original_content(metadata, raw_text)

    return {
        "document_id": str(document_id),
        "chunk_index": chunk_index,
        "source": metadata.get("source") or chunk.get("source"),
        "page": metadata.get("page") or chunk.get("page"),
        "section_title": metadata.get("section_title") or chunk.get("section_title"),
        "section_type": metadata.get("section_type") or chunk.get("section_type", "body"),
        "enhanced_content": chunk.get("text", ""),
        "original_content": original_content,
    }


def _chunk_content_from_unstructured(chunk) -> dict:
    text = getattr(chunk, "text", "") or ""
    tables_html = []
    images_base64 = []

    metadata = getattr(chunk, "metadata", None)
    if metadata and hasattr(metadata, "orig_elements"):
        for element in metadata.orig_elements:
            element_type = type(element).__name__

            if element_type == "Table":
                tables_html.append(getattr(element.metadata, "text_as_html", getattr(element, "text", "")))
            elif element_type == "Image":
                image_base64 = getattr(getattr(element, "metadata", None), "image_base64", None)
                if image_base64:
                    images_base64.append(image_base64)

    return {
        "text": text,
        "tables_html": tables_html,
        "images_base64": images_base64,
    }


def chunk_uploaded_pdf_by_title(file_path: str, source: str) -> list[dict]:
    elements = partition_pdf(
        filename=file_path,
        strategy="hi_res",
        infer_table_structure=True,
        extract_image_block_types=["Image"],
        extract_image_block_to_payload=True,
    )

    chunks = chunk_by_title(
        elements,
        max_characters=3000,
        new_after_n_chars=2400,
        combine_text_under_n_chars=500,
    )

    chunked_documents = []
    for chunk_index, chunk in enumerate(chunks):
        content_data = _chunk_content_from_unstructured(chunk)
        metadata = getattr(chunk, "metadata", None)

        chunked_documents.append(
            {
                "text": content_data["text"],
                "source": source,
                "page": getattr(metadata, "page_number", None),
                "chunk_id": f"0-{chunk_index}",
                "section_title": getattr(metadata, "section_title", None),
                "section_type": getattr(metadata, "section_type", "body"),
                "metadata": {
                    "source": source,
                    "page": getattr(metadata, "page_number", None),
                    "section_title": getattr(metadata, "section_title", None),
                    "section_type": getattr(metadata, "section_type", "body"),
                    "original_content": {
                        "raw_text": content_data["text"],
                        "tables_html": content_data["tables_html"],
                        "images_base64": content_data["images_base64"],
                    },
                },
            }
        )

    return chunked_documents


def ingest_uploaded_pdf(db, upload_file: UploadFile, project_id: UUID, uploaded_by: UUID) -> Document:
    if not upload_file.filename:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="A PDF file is required")

    filename = sanitize_filename(upload_file.filename)
    inferred_content_type = upload_file.content_type or mimetypes.guess_type(filename)[0] or "application/pdf"
    if inferred_content_type != "application/pdf" and not filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF files can be uploaded")

    temp_path = save_upload_to_temp_file(upload_file)
    try:
        object_path = f"documents/{uuid4().hex}/{filename}"
        upload_pdf_to_supabase_storage(temp_path, object_path, "application/pdf")

        with open(temp_path, "rb") as handle:
            file_bytes = handle.read()

        extracted_documents = extract_documents(file_bytes, filename)
        chunked_documents = chunk_uploaded_pdf_by_title(temp_path, filename)
        summarised_chunks = summarise_chunks(chunked_documents)

        document_record = Document(
            project_id=project_id,
            uploaded_by=uploaded_by,
            file_name=upload_file.filename,
            file_type="application/pdf",
            file_path=object_path,
            total_page=extract_total_pages(extracted_documents),
            total_chunk=len(summarised_chunks),
        )

        db.add(document_record)
        db.flush()

        if summarised_chunks:
            embeddings = embedding_model.embed_documents([chunk["text"] for chunk in summarised_chunks])
            for chunk_index, (chunk, embedding) in enumerate(zip(summarised_chunks, embeddings), start=1):
                db.add(
                    Chunk(
                        document_id=document_record.document_id,
                        content=chunk["text"],
                        embedding=embedding,
                        chunk_index=chunk_index,
                        chunk_metadata=build_chunk_metadata(document_record.document_id, chunk_index, chunk),
                    )
                )

        db.commit()
        db.refresh(document_record)
        return document_record
    except HTTPException:
        db.rollback()
        raise
    except Exception as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to process uploaded document: {error}",
        ) from error
    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass