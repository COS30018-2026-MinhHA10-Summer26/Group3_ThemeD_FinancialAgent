import importlib
import json
import os
import re
from typing import List

from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from dotenv import load_dotenv


load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=openai_key)
model = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_key=openai_key
)


SENTENCE_BOUNDARY_RE = re.compile(r"(?<=[.!?])\s+")


def chunk_text(text, chunk_size=400, overlap=50):
    return _chunk_units([text], chunk_size, overlap)


def _normalize_whitespace(text):
    return re.sub(r"[ \t]+", " ", text).strip()


def _section_prefix(doc):
    title = (doc.get("section_title") or "").strip()
    section_type = (doc.get("section_type") or "").strip()

    if not title:
        return ""

    if section_type and section_type != "body":
        return f"{title}\n[{section_type}]"

    return title


def _split_paragraphs(text):
    paragraphs = []
    for block in re.split(r"\n\s*\n", text):
        cleaned = _normalize_whitespace(block.replace("\n", " "))
        if cleaned:
            paragraphs.append(cleaned)
    return paragraphs


def _split_sentences(text):
    sentences = []
    for part in SENTENCE_BOUNDARY_RE.split(text):
        cleaned = _normalize_whitespace(part)
        if cleaned:
            sentences.append(cleaned)
    return sentences or [_normalize_whitespace(text)]


def _split_words(text, max_length):
    words = text.split()
    if not words:
        return []

    fragments = []
    current = []
    current_length = 0
    target_size = max(1, min(max_length, 120))

    for word in words:
        additional = len(word) if not current else len(word) + 1
        if current and current_length + additional > target_size:
            fragments.append(" ".join(current))
            current = [word]
            current_length = len(word)
        else:
            current.append(word)
            current_length += additional

    if current:
        fragments.append(" ".join(current))

    return fragments


def _split_oversized_unit(unit, max_length):
    normalized = _normalize_whitespace(unit)
    if len(normalized) <= max_length:
        return [normalized] if normalized else []

    if "\n" in unit:
        pieces = []
        for line in unit.splitlines():
            cleaned = _normalize_whitespace(line)
            if not cleaned:
                continue
            if len(cleaned) <= max_length:
                pieces.append(cleaned)
            else:
                pieces.extend(_split_oversized_unit(cleaned, max_length))
        return pieces

    sentences = _split_sentences(normalized)
    if len(sentences) > 1:
        pieces = []
        for sentence in sentences:
            if len(sentence) <= max_length:
                pieces.append(sentence)
            else:
                pieces.extend(_split_words(sentence, max_length))
        return pieces

    return _split_words(normalized, max_length)


def _chunk_units(units, chunk_size, overlap, prefix=""):
    prefix = prefix.strip()
    prefix_length = len(prefix) + 2 if prefix else 0
    available_size = max(chunk_size - prefix_length, 1)
    expanded_units = []

    for unit in units:
        normalized = unit.strip()
        if not normalized:
            continue

        if len(normalized) > available_size:
            expanded_units.extend(_split_oversized_unit(normalized, available_size))
        else:
            expanded_units.append(normalized)

    chunks = []
    current_units = []
    current_length = 0

    for unit in expanded_units:
        unit_length = len(unit) if not current_units else len(unit) + 2
        if current_units and current_length + unit_length > available_size:
            chunks.append("\n\n".join(current_units))
            current_units = _overlap_tail(current_units, overlap, available_size)
            current_length = len("\n\n".join(current_units)) if current_units else 0

        if current_units:
            current_length += len(unit) + 2
        else:
            current_length = len(unit)
        current_units.append(unit)

    if current_units:
        chunks.append("\n\n".join(current_units))

    if prefix:
        return [f"{prefix}\n\n{chunk}".strip() for chunk in chunks if chunk.strip()]

    return [chunk for chunk in chunks if chunk.strip()]


def _overlap_tail(units, overlap, max_length):
    if overlap <= 0 or not units:
        return []

    kept = []
    kept_length = 0

    for unit in reversed(units):
        additional = len(unit) if not kept else len(unit) + 2
        if kept and kept_length + additional > min(overlap, max_length):
            break
        if not kept and len(unit) > max_length:
            break
        kept.append(unit)
        kept_length += additional

    return list(reversed(kept))


def _units_for_document(doc):
    text = doc["text"].strip()
    section_type = (doc.get("section_type") or "body").strip().lower()

    if section_type == "table":
        lines = []
        for line in text.splitlines():
            cleaned = _normalize_whitespace(line)
            if cleaned:
                lines.append(cleaned)
        return lines or [_normalize_whitespace(text)]

    paragraphs = _split_paragraphs(text)
    if paragraphs:
        return paragraphs

    sentences = _split_sentences(text)
    return sentences or [_normalize_whitespace(text)]


def chunk_documents(documents, chunk_size, overlap):
    chunked_docs = []

    for doc_index, doc in enumerate(documents):
        text = doc["text"].strip()

        if not text:
            continue

        prefix = _section_prefix(doc)
        raw_chunks = _chunk_units(
            _units_for_document(doc),
            chunk_size,
            overlap,
            prefix=prefix,
        )

        for chunk_index, chunk in enumerate(raw_chunks):
            metadata = dict(doc.get("metadata") or {})
            metadata.setdefault(
                "original_content",
                {
                    "raw_text": doc.get("text", "").strip(),
                    "tables_html": [],
                    "images_base64": [],
                },
            )
            metadata["source"] = doc["source"]
            metadata["page"] = doc["page"]
            metadata["section_title"] = doc.get("section_title")
            metadata["section_type"] = doc.get("section_type", "body")
            metadata["chunk_id"] = f"{doc_index}-{chunk_index}"

            chunked_docs.append(
                {
                    "text": chunk,
                    "source": doc["source"],
                    "page": doc["page"],
                    "chunk_id": f"{doc_index}-{chunk_index}",
                    "section_title": doc.get("section_title"),
                    "section_type": doc.get("section_type", "body"),
                    "metadata": metadata,
                }
            )

    return chunked_docs


def _chunk_text(chunk):
    if isinstance(chunk, dict):
        return chunk.get("text", "")

    return getattr(chunk, "text", "")


def _chunk_metadata(chunk):
    if isinstance(chunk, dict):
        return dict(chunk.get("metadata") or {})

    return dict(getattr(chunk, "metadata", {}) or {})


def separate_content_types(chunk):
    """Analyze what types of content are in a chunk."""
    content_data = {
        "text": _chunk_text(chunk),
        "tables": [],
        "images": [],
        "types": ["text"],
    }

    metadata = _chunk_metadata(chunk)
    original_content = metadata.get("original_content", {})

    if isinstance(original_content, str):
        try:
            original_content = json.loads(original_content)
        except json.JSONDecodeError:
            original_content = {"raw_text": original_content}

    if isinstance(original_content, dict):
        tables = original_content.get("tables_html", []) or []
        images = original_content.get("images_base64", []) or []

        if tables:
            content_data["types"].append("table")
            content_data["tables"].extend(tables)

        if images:
            content_data["types"].append("image")
            content_data["images"].extend(images)

    if hasattr(chunk, "metadata") and hasattr(chunk.metadata, "orig_elements"):
        for element in chunk.metadata.orig_elements:
            element_type = type(element).__name__

            if element_type == "Table":
                content_data["types"].append("table")
                table_html = getattr(element.metadata, "text_as_html", element.text)
                content_data["tables"].append(table_html)

            elif element_type == "Image":
                if hasattr(element, "metadata") and hasattr(element.metadata, "image_base64"):
                    content_data["types"].append("image")
                    content_data["images"].append(element.metadata.image_base64)

    content_data["types"] = list(set(content_data["types"]))
    return content_data


def create_ai_enhanced_summary(text: str, tables: List[str], images: List[str]) -> str:
    """Create AI-enhanced summary for mixed content."""
    try:
        prompt_text = f"""You are creating a searchable description for document content retrieval.

CONTENT TO ANALYZE:
TEXT CONTENT:
{text}
"""

        if tables:
            prompt_text += "TABLES:\n"
            for i, table in enumerate(tables):
                prompt_text += f"Table {i + 1}:\n{table}\n\n"

        if images:
            prompt_text += f"\nIMAGES PRESENT: {len(images)} image(s). Describe them as best as possible from the surrounding text context.\n"

        prompt_text += """
YOUR TASK:
Generate a comprehensive, searchable description that covers:

1. Key facts, numbers, and data points from text and tables
2. Main topics and concepts discussed
3. Questions this content could answer
4. Visual content analysis (charts, diagrams, patterns in images)
5. Alternative search terms users might use

Make it detailed and searchable - prioritize findability over brevity.

SEARCHABLE DESCRIPTION:"""

        response = model.invoke(prompt_text)
        return response.content
    except Exception as error:
        summary = f"{text[:300]}..."
        if tables:
            summary += f" [Contains {len(tables)} table(s)]"
        if images:
            summary += f" [Contains {len(images)} image(s)]"
        print(f"     AI summary failed: {error}")
        return summary


def summarise_chunks(chunks):
    """Process chunks with AI summaries while preserving original metadata."""
    print("Processing chunks with AI Summaries...")

    summarised_chunks = []
    total_chunks = len(chunks)

    for i, chunk in enumerate(chunks):
        current_chunk = i + 1
        print(f"   Processing chunk {current_chunk}/{total_chunks}")

        content_data = separate_content_types(chunk)

        print(f"     Types found: {content_data['types']}")
        print(f"     Tables: {len(content_data['tables'])}, Images: {len(content_data['images'])}")

        if content_data["tables"] or content_data["images"]:
            print("     → Creating AI summary for mixed content...")
            enhanced_content = create_ai_enhanced_summary(
                content_data["text"],
                content_data["tables"],
                content_data["images"],
            )
            print("     → AI summary created successfully")
        else:
            print("     → Using raw text (no tables/images)")
            enhanced_content = content_data["text"]

        if isinstance(chunk, dict):
            summarised_chunk = dict(chunk)
        else:
            summarised_chunk = {
                "source": getattr(chunk, "source", None),
                "page": getattr(chunk, "page", None),
                "chunk_id": getattr(chunk, "chunk_id", None),
                "section_title": getattr(chunk, "section_title", None),
                "section_type": getattr(chunk, "section_type", "body"),
                "metadata": _chunk_metadata(chunk),
            }

        summarised_chunk["text"] = enhanced_content
        summarised_chunk["enhanced_content"] = enhanced_content

        metadata = dict(summarised_chunk.get("metadata") or {})
        original_content = metadata.get("original_content", {})
        if isinstance(original_content, str):
            try:
                original_content = json.loads(original_content)
            except json.JSONDecodeError:
                original_content = {"raw_text": original_content}

        if not isinstance(original_content, dict):
            original_content = {"raw_text": content_data["text"]}

        original_content.setdefault("raw_text", content_data["text"])
        original_content["tables_html"] = content_data["tables"]
        original_content["images_base64"] = content_data["images"]

        metadata["original_content"] = original_content
        summarised_chunk["metadata"] = metadata
        summarised_chunks.append(summarised_chunk)

    print(f"Processed {len(summarised_chunks)} chunks")
    return summarised_chunks
