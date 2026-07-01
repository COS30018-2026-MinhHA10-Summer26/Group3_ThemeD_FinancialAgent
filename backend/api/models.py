from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    ForeignKey,
    Table,
    Enum,
    TIMESTAMP,
    func,
    JSON,
    text,
)

from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from pgvector.sqlalchemy import Vector

import enum
import uuid

from api.database import Base

DEFAULT_EMBEDDING_MODEL = "OpenAIEmbedding"
DEFAULT_LLM_MODEL = "OpenAI"


# =========================
# PROJECT MEMBER ASSOCIATION
# =========================

project_members = Table(
    "project_members",
    Base.metadata,

    Column(
        "user_id",
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True
    ),

    Column(
        "project_id",
        UUID(as_uuid=True),
        ForeignKey("projects.project_id", ondelete="CASCADE"),
        primary_key=True
    ),

    Column("permission", String(50), nullable=False, server_default=text("'member'")),

    Column(
        "join_at",
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )
)


# =========================
# ROLE MODEL
# =========================

class Role(Base):
    __tablename__ = "roles"

    role_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    role_name = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="role")


# =========================
# USER MODEL
# =========================

class User(Base):
    __tablename__ = "users"

    user_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    email = Column(String(255), unique=True, nullable=False)

    password = Column(Text)

    role_id = Column(
        UUID(as_uuid=True),
        ForeignKey("roles.role_id", ondelete="RESTRICT"),
        nullable=False
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    role = relationship("Role", back_populates="users")

    uploaded_documents = relationship(
        "Document",
        back_populates="uploader"
    )

    conversations = relationship(
        "Conversation",
        back_populates="creator"
    )

    projects = relationship(
        "Project",
        secondary=project_members,
        back_populates="members"
    )

    preferences = relationship(
        "UserPreference",
        back_populates="user",
        cascade="all, delete-orphan"
    )


# =========================
# PROJECT MODEL
# =========================

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(String(255), nullable=False)

    description = Column(Text)

    embedding_model = Column(String(100), nullable=False, default=DEFAULT_EMBEDDING_MODEL)

    llm_model = Column(String(100), nullable=False, default=DEFAULT_LLM_MODEL)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    members = relationship(
        "User",
        secondary=project_members,
        back_populates="projects"
    )

    documents = relationship(
        "Document",
        back_populates="project",
        cascade="all, delete"
    )

    conversations = relationship(
        "Conversation",
        back_populates="project",
        cascade="all, delete"
    )


# =========================
# DOCUMENT MODEL
# =========================

class Document(Base):
    __tablename__ = "documents"

    document_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.project_id", ondelete="CASCADE"),
        nullable=False
    )

    uploaded_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="SET NULL")
    )

    file_name = Column(String(255), nullable=False)

    file_type = Column(String(50))

    file_path = Column(Text, nullable=False)

    total_page = Column(Integer, default=0)

    total_chunk = Column(Integer, default=0)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    project = relationship(
        "Project",
        back_populates="documents"
    )

    uploader = relationship(
        "User",
        back_populates="uploaded_documents"
    )

    chunks = relationship(
        "Chunk",
        back_populates="document",
        cascade="all, delete"
    )


# =========================
# CHUNK MODEL
# =========================

class Chunk(Base):
    __tablename__ = "chunks"

    chunk_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    document_id = Column(
        UUID(as_uuid=True),
        ForeignKey("documents.document_id", ondelete="CASCADE"),
        nullable=False
    )

    content = Column(Text, nullable=False)

    embedding = Column(Vector(1536))

    chunk_index = Column(Integer, nullable=False)

    token_count = Column(Integer)

    chunk_metadata = Column("metadata", JSON)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    document = relationship(
        "Document",
        back_populates="chunks"
    )


# =========================
# CONVERSATION MODEL
# =========================

class Conversation(Base):
    __tablename__ = "conversations"

    conversation_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.project_id", ondelete="CASCADE"),
        nullable=False
    )

    created_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="SET NULL")
    )

    title = Column(String(255))

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    project = relationship(
        "Project",
        back_populates="conversations"
    )

    creator = relationship(
        "User",
        back_populates="conversations"
    )

    messages = relationship(
        "Message",
        back_populates="conversation",
        cascade="all, delete"
    )


# =========================
# MESSAGE MODEL
# =========================

class MessageRole(str, enum.Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


class Message(Base):
    __tablename__ = "messages"

    message_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    conversation_id = Column(
        UUID(as_uuid=True),
        ForeignKey("conversations.conversation_id", ondelete="CASCADE"),
        nullable=False
    )

    role = Column(
        Enum(
            MessageRole,
            name="message_role",
            values_callable=lambda enum_cls: [member.value for member in enum_cls],
        ),
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    agent_run_log = Column(
        JSON,
        nullable=True
    )

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    conversation = relationship(
        "Conversation",
        back_populates="messages"
    )


# =========================
# USER PREFERENCE MODEL
# =========================

class UserPreference(Base):
    __tablename__ = "user_preferences"

    preference_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )

    pref_key = Column(String(255), nullable=False)
    pref_value = Column(JSON, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    user = relationship("User", back_populates="preferences")


# =========================
# ENTITY FACT MODEL
# =========================

class EntityFact(Base):
    __tablename__ = "entity_facts"

    fact_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.project_id", ondelete="CASCADE"),
        nullable=False
    )

    conversation_id = Column(
        UUID(as_uuid=True),
        ForeignKey("conversations.conversation_id", ondelete="SET NULL"),
        nullable=True
    )

    entity_name = Column(String(255), nullable=False)
    fact_key = Column(String(255), nullable=False)
    fact_value = Column(JSON, nullable=False)
    fact_text = Column(Text, nullable=False)
    embedding = Column(Vector(1536), nullable=True)
    source = Column(String(255))

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    project = relationship("Project")
    conversation = relationship("Conversation")