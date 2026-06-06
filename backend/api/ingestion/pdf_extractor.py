import base64
import json
import re
from html import escape
from io import BytesIO

from pypdf import PdfReader


HEADING_RE = re.compile(r"^(\d+(\.\d+)*)[\s.)-]+[A-Z].*")


def _extract_page_text(page):
    try:
        text = page.extract_text(extraction_mode="layout")
    except TypeError:
        text = page.extract_text()

    return text or ""


def _normalize_block(block):
    lines = [line.rstrip() for line in block.splitlines()]
    cleaned = [line for line in lines if line.strip()]
    return "\n".join(cleaned).strip()


def _is_heading(block):
    if "\n" in block:
        return False

    line = block.strip()
    if not line or len(line) > 120:
        return False

    if HEADING_RE.match(line):
        return True

    words = line.split()
    if not words or len(words) > 12:
        return False

    uppercase_ratio = sum(1 for char in line if char.isupper()) / max(sum(1 for char in line if char.isalpha()), 1)
    titlecase_words = sum(1 for word in words if word[:1].isupper())

    return uppercase_ratio > 0.7 or titlecase_words / len(words) > 0.8


def _is_table_block(block):
    lines = [line for line in block.splitlines() if line.strip()]
    if len(lines) < 2:
        return False

    numeric_lines = sum(1 for line in lines if re.search(r"\d", line))
    multi_space_lines = sum(1 for line in lines if re.search(r"\S\s{2,}\S", line))

    return numeric_lines >= max(2, len(lines) // 2) and multi_space_lines >= max(1, len(lines) // 3)


def _section_type_from_heading(heading):
    normalized = heading.lower()

    if "conclusion" in normalized or "summary" in normalized:
        return "conclusion"
    if "table" in normalized or "schedule" in normalized:
        return "table"

    return "body"


def _table_title(block, fallback_heading=None):
    first_line = next((line.strip() for line in block.splitlines() if line.strip()), "")

    if first_line and len(first_line) <= 140:
        return first_line

    return fallback_heading or "Table"


def _extract_page_images(page):
    images = []
    for image in getattr(page, "images", []) or []:
        image_data = getattr(image, "data", None) or getattr(image, "image", None)
        if hasattr(image_data, "getvalue"):
            image_data = image_data.getvalue()

        if isinstance(image_data, bytes) and image_data:
            images.append(base64.b64encode(image_data).decode("utf-8"))

    return images


def _block_to_table_html(block):
    rows = []
    for line in block.splitlines():
        cleaned = line.strip()
        if not cleaned:
            continue

        cells = [cell.strip() for cell in re.split(r"\s{2,}|\t+", cleaned) if cell.strip()]
        if not cells:
            cells = [cleaned]

        rows.append(cells)

    if not rows:
        return ""

    max_columns = max(len(row) for row in rows)
    html_rows = []

    for row_index, row in enumerate(rows):
        tag = "th" if row_index == 0 and len(rows) > 1 else "td"
        cells = row + [""] * (max_columns - len(row))
        html_rows.append(
            "<tr>"
            + "".join(f"<{tag}>{escape(cell)}</{tag}>" for cell in cells)
            + "</tr>"
        )

    return "<table>" + "".join(html_rows) + "</table>"


def _build_original_content(text, tables_html=None, images_base64=None):
    return {
        "raw_text": text,
        "tables_html": tables_html or [],
        "images_base64": images_base64 or [],
    }


def _make_section(
    text,
    source,
    page,
    section_title=None,
    section_type="body",
    tables_html=None,
    images_base64=None,
):
    paragraphs = []
    for block in re.split(r"\n\s*\n", text):
        lines = [re.sub(r"\s+", " ", line).strip() for line in block.splitlines()]
        compact = " ".join(line for line in lines if line).strip()
        if compact:
            paragraphs.append(compact)

    normalized = "\n\n".join(paragraphs).strip()
    if not normalized:
        return None

    original_content = _build_original_content(
        normalized,
        tables_html=tables_html,
        images_base64=images_base64,
    )

    return {
        "text": normalized,
        "source": source,
        "page": page,
        "section_title": section_title,
        "section_type": section_type,
        "metadata": {
            "source": source,
            "page": page,
            "section_title": section_title,
            "section_type": section_type,
            "original_content": original_content,
        },
    }


def extract_sections_from_pdf(pdf_bytes, source):
    reader = PdfReader(BytesIO(pdf_bytes))
    sections = []
    current_heading = None
    current_type = "body"
    buffered_paragraphs = []
    buffered_images = []
    buffer_page = 0

    def flush_buffer():
        nonlocal buffered_paragraphs, buffered_images, buffer_page

        if not buffered_paragraphs:
            return

        merged = "\n\n".join(buffered_paragraphs)
        section = _make_section(
            merged,
            source=source,
            page=buffer_page,
            section_title=current_heading,
            section_type=current_type,
            images_base64=list(dict.fromkeys(buffered_images)),
        )
        if section:
            sections.append(section)
        buffered_paragraphs = []
        buffered_images = []

    for page_number, page in enumerate(reader.pages):
        page_text = _extract_page_text(page)
        if not page_text.strip():
            continue

        page_images = _extract_page_images(page)

        blocks = [_normalize_block(block) for block in re.split(r"\n\s*\n", page_text)]
        blocks = [block for block in blocks if block]

        for block in blocks:
            if _is_heading(block):
                flush_buffer()
                current_heading = block
                current_type = _section_type_from_heading(block)
                buffer_page = page_number
                buffered_images = list(page_images)
                continue

            if _is_table_block(block):
                flush_buffer()
                table_title = _table_title(block, current_heading)
                table_html = _block_to_table_html(block)
                section = _make_section(
                    block,
                    source=source,
                    page=page_number,
                    section_title=table_title,
                    section_type="table",
                    tables_html=[table_html] if table_html else [],
                    images_base64=list(dict.fromkeys(page_images)),
                )
                if section:
                    sections.append(section)
                continue

            if not buffered_paragraphs:
                buffer_page = page_number
            if page_images:
                buffered_images.extend(page_images)
            buffered_paragraphs.append(block)

    flush_buffer()
    return sections


def extract_sections_from_text(text, source):
    section = _make_section(text, source=source, page=0)
    return [section] if section else []


def extract_documents(file_bytes, source):
    if source.lower().endswith(".pdf"):
        sections = extract_sections_from_pdf(file_bytes, source)
        if sections:
            return sections

    try:
        text = file_bytes.decode("utf-8", errors="ignore")
    except AttributeError:
        text = str(file_bytes)

    return extract_sections_from_text(text, source)
