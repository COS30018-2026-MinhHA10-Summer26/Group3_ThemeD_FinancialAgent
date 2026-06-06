import os
from dataclasses import dataclass
from uuid import UUID

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from api.database import SessionLocal
from api.models import Message

load_dotenv()

HISTORY_WINDOW = int(os.getenv("CHAT_HISTORY_WINDOW", "10"))
openai_key = os.getenv("OPENAI_API_KEY")
model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=openai_key,
)


@dataclass(slots=True)
class ConversationTurn:
    role: str
    content: str


def load_recent_conversation_turns(conversation_id: UUID, limit: int = HISTORY_WINDOW) -> list[ConversationTurn]:
    db = SessionLocal()
    try:
        rows = (
            db.query(Message)
            .filter(Message.conversation_id == conversation_id)
            .order_by(Message.created_at.asc(), Message.message_id.asc())
            .all()
        )

        if not rows:
            return []

        recent_rows = rows[-limit:] if limit > 0 else rows
        return [
            ConversationTurn(
                role=(row.role.value if getattr(row, "role", None) else "user"),
                content=row.content,
            )
            for row in recent_rows
        ]
    finally:
        db.close()


def format_conversation_history(turns: list[ConversationTurn]) -> str:
    if not turns:
        return ""

    return "\n".join(f"{turn.role.upper()}: {turn.content}" for turn in turns)


def rewrite_query_with_history(question: str, turns: list[ConversationTurn]) -> str:
    question = question.strip()
    if not question or not turns:
        return question

    history_text = format_conversation_history(turns)
    prompt = f"""You rewrite user questions into standalone search queries for a RAG system.

Conversation history:
{history_text}

User question:
{question}

Rewrite the user question so it is fully self-contained, keeps the same intent, and is optimized for retrieval over project documents.
Return only the rewritten question."""

    try:
        response = model.invoke(prompt)
        rewritten = response.content.strip()
        return rewritten or question
    except Exception:
        return question


def prepare_history_aware_query(question: str, conversation_id: UUID | None) -> tuple[str, list[ConversationTurn]]:
    if conversation_id is None:
        return question.strip(), []

    turns = load_recent_conversation_turns(conversation_id, limit=HISTORY_WINDOW)
    return rewrite_query_with_history(question, turns), turns