"""
Semantic / Knowledge Memory for the multi-agent financial pipeline.

This module persists structured financial facts extracted from ``advisor_report_v2``
(the final validated advisor output) into the ``entity_facts`` Postgres table.
On subsequent requests it recalls relevant facts via pgvector cosine-similarity
search and injects them as additional context documents, so agents do not need to
re-derive known statistics from scratch.

Scope rules
-----------
* **Project-scoped** (``conversation_id = NULL``): facts extracted from grounded
  RAG-document content — objective truths that any conversation in the project
  can read (e.g. "Tesla revenue_2022: 81.46 billion USD").
* **Conversation-scoped** (``conversation_id = <uuid>``): facts that originate
  from a user's hypothetical assumption within the current chat (e.g. "what if
  Tesla revenue grows 50% in 2026?").  Only that conversation reads them back.

Vector strategy
---------------
Facts are stored in JSON (``fact_value``).  Before embedding, the writer builds a
natural-language sentence (``fact_text``) from the structured fields, then calls
``text-embedding-3-small`` to produce a 1536-dim vector stored in the
``embedding`` column.  Cosine-similarity (<=> operator) is used for recall.

Public API
----------
* :class:`SemanticMemoryReader` — recall relevant facts given a query string.
* :class:`SemanticMemoryWriter` — extract facts from a report and persist them.
* :func:`get_reader` / :func:`get_writer` — convenience factory functions that
  read ``ai_integration/config.yaml`` for runtime settings.
"""

from __future__ import annotations

import json
import logging
import os
import re
import traceback
import uuid as _uuid_module
from pathlib import Path
from typing import Any
from uuid import UUID

from dotenv import load_dotenv
from sqlalchemy import or_, text
from sqlalchemy.orm import Session

# ---------------------------------------------------------------------------
# Env / path setup  (mirrors the pattern used across ai_integration)
# ---------------------------------------------------------------------------
_PROJECT_ROOT = Path(__file__).resolve().parents[2]
_ENV_PATH = _PROJECT_ROOT / "backend" / ".env"
load_dotenv(dotenv_path=str(_PROJECT_ROOT / ".env"))
load_dotenv(dotenv_path=str(_ENV_PATH))

_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Lazy imports — kept here so the module is importable even without heavy deps
# at module load time.
# ---------------------------------------------------------------------------

def _get_openai_embedding_model():
    """Return a cached OpenAIEmbeddings instance (text-embedding-3-small)."""
    from langchain_openai import OpenAIEmbeddings  # noqa: PLC0415
    return OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=_OPENAI_API_KEY)


def _get_openai_client():
    from openai import OpenAI  # noqa: PLC0415
    return OpenAI(api_key=_OPENAI_API_KEY)


def _get_db_session() -> Session:
    """Open a new SQLAlchemy session (caller is responsible for closing)."""
    from api.database import SessionLocal  # noqa: PLC0415
    return SessionLocal()


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def _to_uuid(value: Any) -> _uuid_module.UUID | None:
    """Safely convert any UUID-like value to a Python uuid.UUID object.

    pgvector + SQLAlchemy 2.x with UUID(as_uuid=True) columns requires
    Python uuid.UUID objects (not strings) for reliable ORM operations.
    Returns None if the value cannot be converted.
    """
    if value is None:
        return None
    if isinstance(value, _uuid_module.UUID):
        return value
    try:
        return _uuid_module.UUID(str(value))
    except (ValueError, AttributeError):
        return None


def _to_native_float_list(embedding: Any) -> list[float] | None:
    """Convert an embedding (numpy array, list, etc.) to list[float].

    pgvector 0.3+ / SQLAlchemy 2.x requires the embedding to be a plain
    Python list of native Python float values.  numpy.float32 or numpy.float64
    elements cause a JSON serialisation error in pgvector's bind processor
    (the error appears as '"value"' in the exception message).
    """
    if embedding is None:
        return None
    try:
        return [float(x) for x in embedding]
    except (TypeError, ValueError) as exc:
        logger.warning("_to_native_float_list: conversion failed — %s", exc)
        return None


def _build_fact_text(entity_name: str, fact_key: str, fact_value: Any) -> str:
    """Convert structured fact fields to a natural-language sentence for embedding.

    Examples
    --------
    >>> _build_fact_text("Tesla", "revenue_2022", {"value": 81.46, "unit": "billion USD"})
    'Tesla revenue_2022: 81.46 billion USD'
    >>> _build_fact_text("Tesla", "ceo", "Elon Musk")
    'Tesla ceo: Elon Musk'
    """
    if isinstance(fact_value, dict):
        value_part = fact_value.get("value", "")
        unit_part = fact_value.get("unit", "")
        value_str = f"{value_part} {unit_part}".strip() if unit_part else str(value_part)
    else:
        value_str = str(fact_value)

    # Replace underscores in fact_key with spaces for readability
    readable_key = fact_key.replace("_", " ")
    return f"{entity_name} {readable_key}: {value_str}"


def _coerce_fact_value(raw_value: Any) -> Any:
    """Ensure fact_value is a JSON-serialisable Python object.

    The LLM sometimes returns fact_value as a JSON-encoded string (double-
    encoded), e.g. ``'{"value": 81.46, "unit": "billion USD"}'``.  We try to
    parse it back to a dict so the value is stored as proper JSON in Postgres.
    """
    if isinstance(raw_value, str):
        stripped = raw_value.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            try:
                return json.loads(stripped)
            except json.JSONDecodeError:
                pass
        return raw_value  # plain string — still valid JSON

    if isinstance(raw_value, (dict, list, int, float, bool)) or raw_value is None:
        return raw_value

    # Fallback: convert to string
    return {"raw": str(raw_value)}


# ---------------------------------------------------------------------------
# SemanticMemoryReader
# ---------------------------------------------------------------------------

class SemanticMemoryReader:
    """Retrieve relevant EntityFacts from the DB via cosine-similarity search.

    Parameters
    ----------
    top_k:
        Maximum number of facts to return.
    similarity_threshold:
        Minimum cosine similarity (0.0–1.0).  Facts below this threshold are
        discarded.  Cosine distance = 1 - similarity, so threshold 0.75 means
        distance <= 0.25.
    """

    def __init__(self, top_k: int = 5, similarity_threshold: float = 0.75) -> None:
        self.top_k = top_k
        self.similarity_threshold = similarity_threshold

    def recall(
        self,
        query: str,
        project_id: Any,
        conversation_id: Any = None,
    ) -> list[dict[str, Any]]:
        """Return a list of context-doc dicts compatible with the agent pipeline.

        The returned dicts mirror the format produced by
        :func:`api.supabase_adapter._document_to_context` so they can be merged
        directly into ``state["context_docs"]``.

        Scope
        -----
        * Always includes project-scoped facts (``conversation_id IS NULL``).
        * If ``conversation_id`` is provided, also includes that conversation's
          facts.

        Parameters
        ----------
        query:
            The user question or cleaned query string.
        project_id:
            Project UUID (str or UUID object).
        conversation_id:
            Conversation UUID, or ``None`` for project-only recall.

        Returns
        -------
        list[dict]
            Up to ``top_k`` fact dicts, each with keys:
            ``text``, ``content``, ``source``, ``entity_name``,
            ``fact_key``, ``fact_text``, ``score``, ``fact_id``.
        """
        query = query.strip()
        if not query:
            return []

        pid = _to_uuid(project_id)
        if pid is None:
            logger.warning("SemanticMemoryReader: invalid project_id — skipping recall.")
            return []

        try:
            embedding_model = _get_openai_embedding_model()
            raw_embedding = embedding_model.embed_query(query)
            query_embedding = _to_native_float_list(raw_embedding)
            if not query_embedding:
                return []
        except Exception as exc:
            logger.warning("SemanticMemoryReader: embedding failed — %s", exc)
            return []

        db = _get_db_session()
        try:
            return self._query_facts(db, query_embedding, pid, _to_uuid(conversation_id))
        except Exception as exc:
            logger.warning(
                "SemanticMemoryReader: DB query failed — %s\n%s",
                exc, traceback.format_exc(),
            )
            return []
        finally:
            db.close()

    def _query_facts(
        self,
        db: Session,
        query_embedding: list[float],
        project_id: _uuid_module.UUID,
        conversation_id: _uuid_module.UUID | None,
    ) -> list[dict[str, Any]]:
        """Execute the pgvector cosine-distance query and return context dicts."""
        from api.models import EntityFact  # noqa: PLC0415

        import math

        query_obj = (
            db.query(EntityFact)
            .filter(
                EntityFact.project_id == project_id,
                or_(
                    EntityFact.conversation_id.is_(None),
                    EntityFact.conversation_id == conversation_id if conversation_id else False,
                ),
                EntityFact.embedding.isnot(None),
            )
            # Use pgvector's cosine distance operator for sorting; Python-side
            # threshold filtering happens below.
            .order_by(
                text(
                    f"embedding <=> '{json.dumps(query_embedding)}'::vector"
                )
            )
            .limit(self.top_k * 3)  # Fetch extra to filter by threshold
        )

        rows = query_obj.all()
        if not rows:
            return []

        def _cosine_sim(a: list[float], b: list[float]) -> float:
            if not a or not b:
                return 0.0
            dot = sum(x * y for x, y in zip(a, b))
            norm_a = math.sqrt(sum(x * x for x in a))
            norm_b = math.sqrt(sum(x * x for x in b))
            return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0

        results: list[dict[str, Any]] = []
        for row in rows:
            if len(results) >= self.top_k:
                break

            row_embedding = _to_native_float_list(row.embedding)
            if not row_embedding:
                continue
            sim = _cosine_sim(query_embedding, row_embedding)
            if sim < self.similarity_threshold:
                continue

            fact_text = row.fact_text or _build_fact_text(
                row.entity_name, row.fact_key,
                row.fact_value if row.fact_value else {}
            )

            scope = "project" if row.conversation_id is None else "conversation"
            results.append({
                # Agent pipeline compatible fields
                "text": fact_text,
                "content": fact_text,
                "source": f"entity_fact_memory:{scope}",
                "page": 1,
                "score": float(sim),
                "chunk_id": f"fact:{row.fact_id}",
                "document_id": str(row.fact_id),
                # Extra fields for debugging / display
                "fact_id": str(row.fact_id),
                "entity_name": row.entity_name,
                "fact_key": row.fact_key,
                "fact_value": row.fact_value,
                "fact_text": fact_text,
                "fact_scope": scope,
            })

        logger.info(
            "SemanticMemoryReader: recalled %d facts (project=%s, conv=%s)",
            len(results), project_id, conversation_id,
        )
        return results


# ---------------------------------------------------------------------------
# SemanticMemoryWriter
# ---------------------------------------------------------------------------

_EXTRACTION_SYSTEM_PROMPT = """\
You are a financial fact extractor.

Given a financial advisory report and the user query that prompted it, extract
all precise, quantitative facts mentioned in the report.

Return a JSON object with a single key "facts" whose value is an array of fact objects.
Each fact object must have these exact fields:
  - "entity_name"    : string  — the subject (e.g. "Tesla", "Apple", "S&P 500")
  - "fact_key"       : string  — snake_case identifier (e.g. "revenue_2022", "net_income_q3_2023")
  - "fact_value"     : object  — {{"value": <number or string>, "unit": "<unit if applicable>"}}
  - "is_hypothetical": boolean — true if the fact comes from a user assumption or
                                  hypothetical scenario ("giả sử", "assume", "what if",
                                  "suppose", "projected", "estimated scenario").
                                  false if the fact is grounded in real, official data.

Rules:
- Only extract facts explicitly stated in the report (no inference).
- Prefer numeric values; skip vague qualitative statements.
- Use exact numbers from the report (no rounding).
- fact_key should be unique per entity (e.g. "revenue_2022" not just "revenue").
- Limit output to at most {max_facts} facts.
- If no quantitative facts are found, return: {{"facts": []}}

Example output:
{{
  "facts": [
    {{"entity_name": "Tesla", "fact_key": "revenue_2022", "fact_value": {{"value": 81.46, "unit": "billion USD"}}, "is_hypothetical": false}},
    {{"entity_name": "Tesla", "fact_key": "net_income_2022", "fact_value": {{"value": 12.56, "unit": "billion USD"}}, "is_hypothetical": false}}
  ]
}}

Return ONLY the JSON object, no explanation.
"""

_EXTRACTION_USER_TEMPLATE = """\
User Query:
{query}

Advisory Report:
{report}
"""


class SemanticMemoryWriter:
    """Extract key financial facts from advisor_report_v2 and persist to DB.

    Parameters
    ----------
    max_facts:
        Maximum number of facts to extract per report.
    extraction_model:
        OpenAI chat model used for fact extraction.
    """

    def __init__(
        self,
        max_facts: int = 10,
        extraction_model: str = "gpt-4o-mini",
    ) -> None:
        self.max_facts = max_facts
        self.extraction_model = extraction_model

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def extract_and_save(
        self,
        final_report: str,
        query: str,
        project_id: Any,
        conversation_id: Any = None,
        context_docs: list[dict[str, Any]] | None = None,
    ) -> list[dict[str, Any]]:
        """Extract facts from *final_report* and upsert them into ``entity_facts``.

        Parameters
        ----------
        final_report:
            The final (v2+) advisor Markdown report.
        query:
            The user query that generated this report.
        project_id:
            UUID of the owning project.
        conversation_id:
            UUID of the owning conversation (used for hypothetical/scoped facts).
        context_docs:
            The RAG context documents used by the advisor (reserved for future use).

        Returns
        -------
        list[dict]
            The list of raw fact dicts that were successfully persisted.
        """
        final_report = (final_report or "").strip()
        query = (query or "").strip()
        if not final_report:
            logger.warning("SemanticMemoryWriter: empty report, skipping.")
            return []

        pid = _to_uuid(project_id)
        if pid is None:
            logger.warning("SemanticMemoryWriter: invalid project_id '%s', skipping.", project_id)
            return []

        cid = _to_uuid(conversation_id)

        raw_facts = self._extract_facts_with_llm(final_report, query)
        if not raw_facts:
            logger.info("SemanticMemoryWriter: no facts extracted.")
            return []

        try:
            embedding_model = _get_openai_embedding_model()
        except Exception as exc:
            logger.error("SemanticMemoryWriter: could not init embedding model — %s", exc)
            return []

        saved: list[dict[str, Any]] = []

        db = _get_db_session()
        try:
            for raw in raw_facts:
                try:
                    result = self._upsert_fact(
                        db, raw, embedding_model, pid, cid
                    )
                    if result:
                        saved.append(result)
                except Exception as exc:
                    logger.warning(
                        "SemanticMemoryWriter: failed to upsert fact '%s.%s' — %s\n%s",
                        raw.get("entity_name"), raw.get("fact_key"),
                        exc, traceback.format_exc(),
                    )
            db.commit()
        except Exception as exc:
            db.rollback()
            logger.error(
                "SemanticMemoryWriter: DB commit failed — %s\n%s",
                exc, traceback.format_exc(),
            )
        finally:
            db.close()

        logger.info(
            "SemanticMemoryWriter: saved %d/%d facts (project=%s, conv=%s)",
            len(saved), len(raw_facts), pid, cid,
        )
        return saved

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _extract_facts_with_llm(
        self, report: str, query: str
    ) -> list[dict[str, Any]]:
        """Call the LLM to extract structured facts from the report.

        Returns an empty list on any failure (never raises).
        """
        client = _get_openai_client()
        system_prompt = _EXTRACTION_SYSTEM_PROMPT.format(max_facts=self.max_facts)
        user_content = _EXTRACTION_USER_TEMPLATE.format(query=query, report=report)

        try:
            response = client.chat.completions.create(
                model=self.extraction_model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                temperature=0,
                response_format={"type": "json_object"},
            )
            raw_content = (response.choices[0].message.content or "").strip()
        except Exception as exc:
            logger.error(
                "SemanticMemoryWriter: LLM extraction failed — %s\n%s",
                exc, traceback.format_exc(),
            )
            return []

        # Parse JSON
        try:
            parsed = json.loads(raw_content)
        except json.JSONDecodeError:
            # Try to rescue a bare array embedded in text
            match = re.search(r"\[.*\]", raw_content, re.DOTALL)
            if match:
                try:
                    parsed = json.loads(match.group())
                except json.JSONDecodeError:
                    logger.warning(
                        "SemanticMemoryWriter: could not parse LLM JSON output. Raw: %.200s",
                        raw_content,
                    )
                    return []
            else:
                logger.warning(
                    "SemanticMemoryWriter: LLM output not valid JSON. Raw: %.200s",
                    raw_content,
                )
                return []

        # Normalise to list — handle all possible wrapper patterns
        if isinstance(parsed, list):
            facts = parsed
        elif isinstance(parsed, dict):
            # Try all common wrapper keys (including "value" which GPT sometimes uses)
            for key in ("facts", "data", "results", "items", "value", "fact_list"):
                if isinstance(parsed.get(key), list):
                    facts = parsed[key]
                    break
            else:
                # Single-fact top-level dict
                facts = [parsed] if parsed.get("entity_name") else []
        else:
            logger.warning(
                "SemanticMemoryWriter: unexpected parsed type %s, raw: %.200s",
                type(parsed).__name__, raw_content,
            )
            facts = []

        # Validate each fact
        valid: list[dict[str, Any]] = []
        for item in facts:
            if not isinstance(item, dict):
                continue
            if not item.get("entity_name") or not item.get("fact_key"):
                continue
            valid.append(item)

        logger.info(
            "SemanticMemoryWriter: extracted %d valid facts from LLM output.",
            len(valid),
        )
        return valid[: self.max_facts]

    def _upsert_fact(
        self,
        db: Session,
        raw: dict[str, Any],
        embedding_model: Any,
        project_id: _uuid_module.UUID,
        conversation_id: _uuid_module.UUID | None,
    ) -> dict[str, Any] | None:
        """Upsert one fact into the ``entity_facts`` table.

        Scope rules
        -----------
        * ``is_hypothetical = False``  → project-scoped (``conversation_id = NULL``).
          Uses ``UPSERT`` on ``(project_id, entity_name, fact_key)`` so subsequent
          runs overwrite outdated values.
        * ``is_hypothetical = True``   → conversation-scoped (``conversation_id =
          <uuid>``).  Always inserts a new row (no deduplication needed).

        Key bug fixes applied here
        --------------------------
        * ``_to_native_float_list`` converts embeddings to plain Python floats
          (pgvector 0.3+ / SQLAlchemy 2.x rejects numpy floats and raises a
          JSON serialisation error with message '"value"').
        * ``_to_uuid`` ensures all UUID columns receive Python uuid.UUID objects,
          not strings (required by UUID(as_uuid=True) columns in SA 2.x).
        * ``_coerce_fact_value`` parses JSON-string fact_values that the LLM
          sometimes double-encodes.
        """
        from api.models import EntityFact  # noqa: PLC0415

        entity_name: str = str(raw.get("entity_name", "")).strip()
        fact_key: str = str(raw.get("fact_key", "")).strip()
        raw_fact_value: Any = raw.get("fact_value", {})
        is_hypothetical: bool = bool(raw.get("is_hypothetical", False))
        source_label = "advisor_report_v2"

        if not entity_name or not fact_key:
            return None

        # Coerce fact_value to a JSON-safe Python type
        fact_value = _coerce_fact_value(raw_fact_value)

        fact_text = _build_fact_text(entity_name, fact_key, fact_value)

        # Embed the fact text — MUST convert to native Python floats
        try:
            raw_embedding = embedding_model.embed_query(fact_text)
            embedding_vector = _to_native_float_list(raw_embedding)
        except Exception as exc:
            logger.warning(
                "SemanticMemoryWriter: embedding failed for '%s.%s' — %s",
                entity_name, fact_key, exc,
            )
            embedding_vector = None

        # Determine scope — conversation-scoped only for hypothetical facts
        scope_cid: _uuid_module.UUID | None = (
            conversation_id if is_hypothetical else None
        )

        if is_hypothetical:
            # Always INSERT a new row for conversation-scoped hypotheticals
            new_fact = EntityFact(
                project_id=project_id,
                conversation_id=scope_cid,
                entity_name=entity_name,
                fact_key=fact_key,
                fact_value=fact_value,
                fact_text=fact_text,
                embedding=embedding_vector,
                source=source_label,
            )
            db.add(new_fact)
            saved_dict = _fact_to_dict(new_fact)
        else:
            # Project-scoped: UPSERT (find existing → overwrite, or create new)
            existing = (
                db.query(EntityFact)
                .filter(
                    EntityFact.project_id == project_id,
                    EntityFact.entity_name == entity_name,
                    EntityFact.fact_key == fact_key,
                    EntityFact.conversation_id.is_(None),
                )
                .first()
            )
            if existing:
                existing.fact_value = fact_value
                existing.fact_text = fact_text
                existing.embedding = embedding_vector
                existing.source = source_label
                db.add(existing)
                saved_dict = _fact_to_dict(existing)
            else:
                new_fact = EntityFact(
                    project_id=project_id,
                    conversation_id=None,
                    entity_name=entity_name,
                    fact_key=fact_key,
                    fact_value=fact_value,
                    fact_text=fact_text,
                    embedding=embedding_vector,
                    source=source_label,
                )
                db.add(new_fact)
                saved_dict = _fact_to_dict(new_fact)

        return saved_dict


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def _fact_to_dict(fact) -> dict[str, Any]:
    """Convert an EntityFact ORM row to a plain dict (no embedding vector)."""
    return {
        "fact_id": str(fact.fact_id) if fact.fact_id else None,
        "project_id": str(fact.project_id),
        "conversation_id": str(fact.conversation_id) if fact.conversation_id else None,
        "entity_name": fact.entity_name,
        "fact_key": fact.fact_key,
        "fact_value": fact.fact_value,
        "fact_text": fact.fact_text,
        "source": fact.source,
    }


# ---------------------------------------------------------------------------
# Factory helpers (read config.yaml automatically)
# ---------------------------------------------------------------------------

def _load_semantic_config() -> dict[str, Any]:
    config_path = _PROJECT_ROOT / "ai_integration" / "config.yaml"
    try:
        import yaml  # noqa: PLC0415
        with open(config_path) as fh:
            cfg = yaml.safe_load(fh) or {}
        return cfg.get("semantic_memory", {})
    except Exception:
        return {}


def get_reader() -> SemanticMemoryReader:
    """Return a :class:`SemanticMemoryReader` configured from ``config.yaml``."""
    cfg = _load_semantic_config()
    return SemanticMemoryReader(
        top_k=int(cfg.get("recall_top_k", 5)),
        similarity_threshold=float(cfg.get("similarity_threshold", 0.75)),
    )


def get_writer() -> SemanticMemoryWriter:
    """Return a :class:`SemanticMemoryWriter` configured from ``config.yaml``."""
    cfg = _load_semantic_config()
    return SemanticMemoryWriter(
        max_facts=int(cfg.get("max_facts_to_extract", 10)),
        extraction_model=str(cfg.get("extraction_model", "gpt-4o-mini")),
    )


def is_semantic_memory_enabled() -> bool:
    """Return True if semantic memory is enabled in config."""
    cfg = _load_semantic_config()
    return bool(cfg.get("enabled", True))
