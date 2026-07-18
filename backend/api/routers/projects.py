import asyncio
import base64
import json
import queue
from datetime import datetime, timedelta
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import selectinload
from starlette.responses import StreamingResponse

from api.deps import db_dependency, get_current_user
from api.generate_answer import answer_query
from api.ingestion.pdf_chat_processor import process_pdf_for_chat
from api.multi_agent_handler import run_multi_agent_chat
from api.models import DEFAULT_EMBEDDING_MODEL, DEFAULT_LLM_MODEL, Conversation, Message, MessageRole, Project, User, project_members

router = APIRouter(prefix="/projects", tags=["projects"])


class ProjectMemberRead(BaseModel):
    user_id: UUID
    email: str
    role_name: str

    model_config = ConfigDict(from_attributes=True)


class ProjectRead(BaseModel):
    project_id: UUID
    name: str
    description: Optional[str] = None
    embedding_model: str
    llm_model: str
    member_ids: list[UUID] = []
    members: list[ProjectMemberRead] = []
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ProjectCreate(BaseModel):
    name: str
    description: Optional[str] = None
    embedding_model: Optional[str] = None
    llm_model: Optional[str] = None
    member_ids: list[UUID] = []


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    embedding_model: Optional[str] = None
    llm_model: Optional[str] = None
    member_ids: Optional[list[UUID]] = None


class ConversationCreatorRead(BaseModel):
    user_id: UUID
    email: str
    role_name: str

    model_config = ConfigDict(from_attributes=True)


class ConversationRead(BaseModel):
    conversation_id: UUID
    project_id: UUID
    title: str
    creator: Optional[ConversationCreatorRead] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


class ConversationCreate(BaseModel):
    title: Optional[str] = None


class MessageRead(BaseModel):
    message_id: UUID
    conversation_id: UUID
    role: str
    content: str
    agent_run_log: dict | None = None
    created_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)




class ChatResponse(BaseModel):
    answer: str
    query_variations: list[str]
    sources: list[dict]
    agent_run_log: dict | None = None
    user_message: MessageRead
    assistant_message: MessageRead


def require_admin(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user.get("role") != "Admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")
    return current_user


def normalize_embedding_model(value: Optional[str]) -> str:
    return value or DEFAULT_EMBEDDING_MODEL


def normalize_llm_model(value: Optional[str]) -> str:
    return value or DEFAULT_LLM_MODEL


def resolve_members(db, member_ids: list[UUID]) -> list[User]:
    unique_member_ids = list(dict.fromkeys(member_ids))
    if not unique_member_ids:
        return []

    members = db.query(User).filter(User.user_id.in_(unique_member_ids)).all()
    found_member_ids = {member.user_id for member in members}
    missing_member_ids = [member_id for member_id in unique_member_ids if member_id not in found_member_ids]
    if missing_member_ids:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="One or more project members were not found")

    return members


def project_to_read(project: Project) -> ProjectRead:
    members = list(project.members or [])
    return ProjectRead(
        project_id=project.project_id,
        name=project.name,
        description=project.description,
        embedding_model=project.embedding_model or DEFAULT_EMBEDDING_MODEL,
        llm_model=project.llm_model or DEFAULT_LLM_MODEL,
        member_ids=[member.user_id for member in members],
        members=[
            ProjectMemberRead(
                user_id=member.user_id,
                email=member.email,
                role_name=member.role.role_name if member.role else "",
            )
            for member in members
        ],
        created_at=project.created_at,
        updated_at=project.updated_at,
    )


def project_is_accessible(project: Project, current_user: dict) -> bool:
    if current_user.get("role") == "Admin":
        return True

    current_user_id = str(current_user.get("id"))
    return any(str(member.user_id) == current_user_id for member in project.members)


def require_project_access(project: Project, current_user: dict) -> None:
    if not project_is_accessible(project, current_user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Project access required")


def load_project(db, project_id: UUID) -> Project:
    project = (
        db.query(Project)
        .options(selectinload(Project.members).selectinload(User.role))
        .filter(Project.project_id == project_id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")
    return project


def load_conversation(db, project_id: UUID, conversation_id: UUID) -> Conversation:
    conversation = (
        db.query(Conversation)
        .filter(Conversation.project_id == project_id, Conversation.conversation_id == conversation_id)
        .first()
    )
    if not conversation:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversation not found")
    return conversation


def conversation_to_read(conversation: Conversation) -> ConversationRead:
    return ConversationRead(
        conversation_id=conversation.conversation_id,
        project_id=conversation.project_id,
        title=conversation.title or "Conversation",
        creator=(
            ConversationCreatorRead(
                user_id=conversation.creator.user_id,
                email=conversation.creator.email,
                role_name=conversation.creator.role.role_name if conversation.creator and conversation.creator.role else "",
            )
            if conversation.creator
            else None
        ),
        created_at=conversation.created_at,
        updated_at=conversation.updated_at,
    )


def message_to_read(message: Message) -> MessageRead:
    return MessageRead(
        message_id=message.message_id,
        conversation_id=message.conversation_id,
        role=message.role.value if getattr(message, "role", None) else "user",
        content=message.content,
        agent_run_log=message.agent_run_log,
        created_at=message.created_at,
    )


def assign_project_members(db, project: Project, member_ids: Optional[list[UUID]]) -> None:
    if member_ids is None:
        return
    members = resolve_members(db, member_ids)

    db.execute(project_members.delete().where(project_members.c.project_id == project.project_id))
    for member in members:
        db.execute(
            project_members.insert().values(
                user_id=member.user_id,
                project_id=project.project_id,
                permission="member",
            )
        )


@router.get("", response_model=list[ProjectRead])
async def list_projects(db: db_dependency, current_user: dict = Depends(get_current_user)):
    projects = (
        db.query(Project)
        .options(selectinload(Project.members).selectinload(User.role))
        .order_by(Project.created_at.desc())
        .all()
    )

    if current_user.get("role") == "Admin":
        visible_projects = projects
    else:
        visible_projects = [project for project in projects if project_is_accessible(project, current_user)]

    return [project_to_read(project) for project in visible_projects]


@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(project_id: UUID, db: db_dependency, current_user: dict = Depends(get_current_user)):
    project = load_project(db, project_id)
    require_project_access(project, current_user)
    return project_to_read(project)


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
async def create_project(project_request: ProjectCreate, db: db_dependency, _: dict = Depends(require_admin)):
    project = Project(
        name=project_request.name,
        description=project_request.description,
        embedding_model=normalize_embedding_model(project_request.embedding_model),
        llm_model=normalize_llm_model(project_request.llm_model),
    )
    db.add(project)
    db.flush()
    assign_project_members(db, project, project_request.member_ids)
    db.commit()
    db.refresh(project)
    project = load_project(db, project.project_id)
    return project_to_read(project)


@router.put("/{project_id}", response_model=ProjectRead)
async def update_project(project_id: UUID, project_request: ProjectUpdate, db: db_dependency, _: dict = Depends(require_admin)):
    project = load_project(db, project_id)

    if project_request.name is not None:
        project.name = project_request.name

    if project_request.description is not None:
        project.description = project_request.description

    if project_request.embedding_model is not None:
        project.embedding_model = normalize_embedding_model(project_request.embedding_model)

    if project_request.llm_model is not None:
        project.llm_model = normalize_llm_model(project_request.llm_model)

    assign_project_members(db, project, project_request.member_ids)

    db.commit()
    db.refresh(project)
    project = load_project(db, project.project_id)
    return project_to_read(project)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(project_id: UUID, db: db_dependency, _: dict = Depends(require_admin)):
    project = db.query(Project).filter(Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    db.delete(project)
    db.commit()


@router.get("/{project_id}/conversations", response_model=list[ConversationRead])
async def list_conversations(project_id: UUID, db: db_dependency, current_user: dict = Depends(get_current_user)):
    project = load_project(db, project_id)
    require_project_access(project, current_user)

    conversations = (
        db.query(Conversation)
        .options(selectinload(Conversation.creator).selectinload(User.role))
        .filter(Conversation.project_id == project_id)
        .order_by(Conversation.created_at.desc())
        .all()
    )
    return [conversation_to_read(conversation) for conversation in conversations]


@router.post("/{project_id}/conversations", response_model=ConversationRead, status_code=status.HTTP_201_CREATED)
async def create_conversation(
    project_id: UUID,
    conversation_request: ConversationCreate,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    project = load_project(db, project_id)
    require_project_access(project, current_user)

    conversation_count = db.query(Conversation).filter(Conversation.project_id == project_id).count()
    conversation = Conversation(
        project_id=project_id,
        created_by=UUID(str(current_user["id"])),
        title=conversation_request.title or f"Conversation {conversation_count + 1}",
    )
    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    conversation = (
        db.query(Conversation)
        .options(selectinload(Conversation.creator).selectinload(User.role))
        .filter(Conversation.conversation_id == conversation.conversation_id)
        .first()
    )
    return conversation_to_read(conversation)


@router.get("/{project_id}/conversations/{conversation_id}/messages", response_model=list[MessageRead])
async def list_conversation_messages(
    project_id: UUID,
    conversation_id: UUID,
    db: db_dependency,
    current_user: dict = Depends(get_current_user),
):
    project = load_project(db, project_id)
    require_project_access(project, current_user)
    load_conversation(db, project_id, conversation_id)

    messages = (
        db.query(Message)
        .filter(Message.conversation_id == conversation_id)
        .order_by(Message.created_at.asc(), Message.message_id.asc())
        .all()
    )
    return [message_to_read(message) for message in messages]


@router.post("/{project_id}/conversations/{conversation_id}/messages", response_model=ChatResponse)
async def send_conversation_message(
    project_id: UUID,
    conversation_id: UUID,
    db: db_dependency,
    query: str = Form(...),
    image: UploadFile | None = File(None),
    pdf: UploadFile | None = File(None),
    current_user: dict = Depends(get_current_user),
):
    project = load_project(db, project_id)
    require_project_access(project, current_user)
    conversation = load_conversation(db, project_id, conversation_id)

    query_text = query.strip()
    if not query_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query is required")

    # Process optional image upload
    image_base64 = None
    if image and image.filename:
        allowed_types = {"image/png", "image/jpeg", "image/gif", "image/webp"}
        if image.content_type not in allowed_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported image type: {image.content_type}. Allowed: {', '.join(allowed_types)}",
            )
        image_bytes = await image.read()
        if len(image_bytes) > 10 * 1024 * 1024:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Image too large (max 10MB)",
            )
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # Process optional PDF upload (temporary, in-memory)
    pdf_chunks = None
    if pdf and pdf.filename:
        pdf_filename = pdf.filename or "document.pdf"
        if pdf.content_type not in {"application/pdf"} and not pdf_filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only PDF files are supported. Please upload a .pdf file.",
            )
        pdf_bytes = await pdf.read()
        if len(pdf_bytes) > 5 * 1024 * 1024:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="PDF too large (max 5MB)",
            )
        pdf_chunks = process_pdf_for_chat(pdf_bytes, pdf_filename)

    rag_result = answer_query(
        query=query_text,
        project_id=project_id,
        conversation_id=conversation_id,
        max_results=5,
        image_data_url=image_base64,
        pdf_chunks=pdf_chunks,
    )

    now = datetime.utcnow()
    user_message = Message(
        conversation_id=conversation.conversation_id,
        role=MessageRole.USER,
        content=query_text,
        created_at=now,
    )
    assistant_message = Message(
        conversation_id=conversation.conversation_id,
        role=MessageRole.ASSISTANT,
        content=rag_result["answer"],
        agent_run_log=rag_result.get("agent_run_log"),
        created_at=now + timedelta(microseconds=1),
    )

    db.add(user_message)
    db.add(assistant_message)
    db.commit()
    db.refresh(user_message)
    db.refresh(assistant_message)

    return ChatResponse(
        answer=rag_result["answer"],
        query_variations=rag_result.get("query_variations", []),
        sources=rag_result.get("sources", []),
        agent_run_log=rag_result.get("agent_run_log"),
        user_message=message_to_read(user_message),
        assistant_message=message_to_read(assistant_message),
    )


def _sse_event(event: str, payload: dict) -> str:
    return f"event: {event}\ndata: {json.dumps(payload, default=str)}\n\n"


@router.post("/{project_id}/conversations/{conversation_id}/messages/stream")
async def send_conversation_message_stream(
    project_id: UUID,
    conversation_id: UUID,
    db: db_dependency,
    query: str = Form(...),
    image: UploadFile | None = File(None),
    pdf: UploadFile | None = File(None),
    current_user: dict = Depends(get_current_user),
):
    """Run the project-scoped multi-agent workflow and stream its progress."""
    project = load_project(db, project_id)
    require_project_access(project, current_user)
    conversation = load_conversation(db, project_id, conversation_id)

    query_text = query.strip()
    if not query_text:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Query is required")

    image_base64 = None
    if image and image.filename:
        allowed_types = {"image/png", "image/jpeg", "image/gif", "image/webp"}
        if image.content_type not in allowed_types:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported image type: {image.content_type}. Allowed: {', '.join(allowed_types)}",
            )
        image_bytes = await image.read()
        if len(image_bytes) > 10 * 1024 * 1024:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Image too large (max 10MB)")
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    pdf_chunks = None
    if pdf and pdf.filename:
        pdf_filename = pdf.filename or "document.pdf"
        if pdf.content_type not in {"application/pdf"} and not pdf_filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Only PDF files are supported. Please upload a .pdf file.")
        pdf_bytes = await pdf.read()
        if len(pdf_bytes) > 5 * 1024 * 1024:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="PDF too large (max 5MB)")
        pdf_chunks = process_pdf_for_chat(pdf_bytes, pdf_filename)

    progress_events: queue.Queue[tuple[str, str]] = queue.Queue()

    def emit_progress(step: str, message: str) -> None:
        progress_events.put((step, message))

    async def event_stream():
        task = asyncio.create_task(
            asyncio.to_thread(
                run_multi_agent_chat,
                query_text,
                project_id,
                conversation_id,
                image_base64,
                pdf_chunks,
                emit_progress,
            ),
        )
        try:
            while not task.done() or not progress_events.empty():
                sent_progress = False
                try:
                    while True:
                        step, message = progress_events.get_nowait()
                        sent_progress = True
                        yield _sse_event("progress", {"step": step, "message": message})
                except queue.Empty:
                    pass
                if not task.done() and not sent_progress:
                    await asyncio.sleep(0.08)

            result = await task
            now = datetime.utcnow()
            user_message = Message(
                conversation_id=conversation.conversation_id,
                role=MessageRole.USER,
                content=query_text,
                created_at=now,
            )
            assistant_message = Message(
                conversation_id=conversation.conversation_id,
                role=MessageRole.ASSISTANT,
                content=result["answer"],
                agent_run_log=result.get("agent_run_log"),
                created_at=now + timedelta(microseconds=1),
            )
            db.add(user_message)
            db.add(assistant_message)
            db.commit()
            db.refresh(user_message)
            db.refresh(assistant_message)

            response = ChatResponse(
                answer=result["answer"],
                query_variations=result.get("query_variations", []),
                sources=result.get("sources", []),
                agent_run_log=result.get("agent_run_log"),
                user_message=message_to_read(user_message),
                assistant_message=message_to_read(assistant_message),
            )
            yield _sse_event("done", response.model_dump(mode="json"))
        except Exception as exc:
            db.rollback()
            yield _sse_event("error", {"detail": f"Multi-agent chat failed: {exc}"})

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
