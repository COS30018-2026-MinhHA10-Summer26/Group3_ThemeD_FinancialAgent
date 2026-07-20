"""
REST API endpoints for the EntityFact semantic memory store.

These endpoints allow project members and admins to list, search, and delete
entity facts that have been automatically extracted and persisted by the
multi-agent pipeline.

Routes
------
GET  /projects/{project_id}/entity-facts
    List all project-scoped facts (conversation_id IS NULL).
    Optional query param: ?entity_name=Tesla

GET  /projects/{project_id}/conversations/{conversation_id}/entity-facts
    List all conversation-scoped facts for a specific conversation.
    Optional query param: ?entity_name=Tesla

POST /projects/{project_id}/entity-facts/search
    Semantic search: find the most relevant facts for a given query string.
    Returns top-K facts sorted by cosine similarity.

DELETE /projects/{project_id}/entity-facts/{fact_id}
    Delete a single fact by its UUID (admin or project member only).

DELETE /projects/{project_id}/entity-facts
    Bulk-delete all project-scoped facts (admin only).
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, ConfigDict

from api.deps import db_dependency, get_current_user
from api.models import Conversation, EntityFact, Project

router = APIRouter(
    prefix="/projects",
    tags=["entity-facts"],
)


# ──────────────────────────────────────────────────────────────────────────────
# Pydantic schemas
# ──────────────────────────────────────────────────────────────────────────────

class EntityFactRead(BaseModel):
    fact_id: UUID
    project_id: UUID
    conversation_id: Optional[UUID] = None
    entity_name: str
    fact_key: str
    fact_value: Any
    fact_text: str
    source: Optional[str] = None
    scope: str  # "project" or "conversation"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class SemanticSearchRequest(BaseModel):
    query: str
    top_k: int = 5
    similarity_threshold: float = 0.70
    include_conversation_facts: bool = True
    conversation_id: Optional[UUID] = None


class SemanticSearchResult(BaseModel):
    fact_id: str
    entity_name: str
    fact_key: str
    fact_text: str
    fact_value: Any
    score: float
    scope: str
    source: Optional[str] = None


class BulkDeleteResponse(BaseModel):
    deleted_count: int
    message: str


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _require_project_access(
    db,
    project_id: UUID,
    current_user: dict,
) -> Project:
    """Load the project and verify the caller has access."""
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    if current_user.get("role") == "Admin":
        return project

    current_user_id = str(current_user.get("id"))
    member_ids = [str(m.user_id) for m in (project.members or [])]
    if current_user_id not in member_ids:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Project access required"
        )
    return project


def _require_admin(current_user: dict) -> None:
    if current_user.get("role") != "Admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required"
        )


def _fact_to_read(fact: EntityFact) -> EntityFactRead:
    return EntityFactRead(
        fact_id=fact.fact_id,
        project_id=fact.project_id,
        conversation_id=fact.conversation_id,
        entity_name=fact.entity_name,
        fact_key=fact.fact_key,
        fact_value=fact.fact_value,
        fact_text=fact.fact_text,
        source=fact.source,
        scope="project" if fact.conversation_id is None else "conversation",
        created_at=fact.created_at,
        updated_at=fact.updated_at,
    )


# ──────────────────────────────────────────────────────────────────────────────
# Endpoints
# ──────────────────────────────────────────────────────────────────────────────

@router.get(
    "/{project_id}/entity-facts",
    response_model=list[EntityFactRead],
    summary="List project-scoped entity facts",
)
def list_project_facts(
    project_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
    entity_name: Optional[str] = Query(None, description="Filter by entity name (case-insensitive)"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
):
    """Return all project-scoped facts (conversation_id IS NULL) for a project."""
    _require_project_access(db, project_id, current_user)

    query = (
        db.query(EntityFact)
        .filter(
            EntityFact.project_id == str(project_id),
            EntityFact.conversation_id.is_(None),
        )
    )
    if entity_name:
        query = query.filter(
            EntityFact.entity_name.ilike(f"%{entity_name}%")
        )

    facts = query.order_by(EntityFact.entity_name, EntityFact.fact_key).offset(skip).limit(limit).all()
    return [_fact_to_read(f) for f in facts]


@router.get(
    "/{project_id}/conversations/{conversation_id}/entity-facts",
    response_model=list[EntityFactRead],
    summary="List conversation-scoped entity facts",
)
def list_conversation_facts(
    project_id: UUID,
    conversation_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
    entity_name: Optional[str] = Query(None, description="Filter by entity name (case-insensitive)"),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
):
    """Return all conversation-scoped facts for the given conversation."""
    _require_project_access(db, project_id, current_user)

    # Verify conversation belongs to this project
    conv = (
        db.query(Conversation)
        .filter(
            Conversation.conversation_id == str(conversation_id),
            Conversation.project_id == str(project_id),
        )
        .first()
    )
    if not conv:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")

    query = (
        db.query(EntityFact)
        .filter(
            EntityFact.project_id == str(project_id),
            EntityFact.conversation_id == str(conversation_id),
        )
    )
    if entity_name:
        query = query.filter(EntityFact.entity_name.ilike(f"%{entity_name}%"))

    facts = query.order_by(EntityFact.entity_name, EntityFact.fact_key).offset(skip).limit(limit).all()
    return [_fact_to_read(f) for f in facts]


@router.post(
    "/{project_id}/entity-facts/search",
    response_model=list[SemanticSearchResult],
    summary="Semantic search over entity facts",
)
def search_entity_facts(
    project_id: UUID,
    body: SemanticSearchRequest,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """
    Find the most relevant cached facts for a given query using vector similarity.

    Useful for debugging — shows which facts the pipeline will inject into context
    for a given question.
    """
    _require_project_access(db, project_id, current_user)

    try:
        from ai_integration.memory.semantic_memory import SemanticMemoryReader
    except ImportError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Semantic memory module not available",
        )

    reader = SemanticMemoryReader(
        top_k=body.top_k,
        similarity_threshold=body.similarity_threshold,
    )
    conversation_id = body.conversation_id if body.include_conversation_facts else None
    results = reader.recall(
        query=body.query,
        project_id=project_id,
        conversation_id=conversation_id,
    )

    return [
        SemanticSearchResult(
            fact_id=r["fact_id"],
            entity_name=r["entity_name"],
            fact_key=r["fact_key"],
            fact_text=r["fact_text"],
            fact_value=r["fact_value"],
            score=r["score"],
            scope=r["fact_scope"],
            source=r.get("source"),
        )
        for r in results
    ]


@router.delete(
    "/{project_id}/entity-facts/{fact_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a single entity fact",
)
def delete_entity_fact(
    project_id: UUID,
    fact_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """Delete a specific fact by its UUID (project members and admins)."""
    _require_project_access(db, project_id, current_user)

    fact = (
        db.query(EntityFact)
        .filter(
            EntityFact.fact_id == str(fact_id),
            EntityFact.project_id == str(project_id),
        )
        .first()
    )
    if not fact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fact not found")

    db.delete(fact)
    db.commit()


@router.delete(
    "/{project_id}/entity-facts",
    response_model=BulkDeleteResponse,
    summary="Bulk delete all project-scoped entity facts (admin only)",
)
def bulk_delete_project_facts(
    project_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    """
    Delete ALL project-scoped facts for this project.  Admin only.

    Use with caution — this clears the entire semantic memory cache for the project
    and cannot be undone.
    """
    _require_project_access(db, project_id, current_user)
    _require_admin(current_user)

    deleted = (
        db.query(EntityFact)
        .filter(
            EntityFact.project_id == str(project_id),
            EntityFact.conversation_id.is_(None),
        )
        .delete(synchronize_session=False)
    )
    db.commit()

    return BulkDeleteResponse(
        deleted_count=deleted,
        message=f"Deleted {deleted} project-scoped facts for project {project_id}.",
    )
