"""
combine_paper_sources.py

Combines text chunks (from text_after_chunking) and media chunks (from
image_table_after_chunking) for all "paper" projects, then writes one Python
source file per paper to evaluation_for_paper/paper_sources/paper_{i}.py.

Each generated file contains CONTEXT_DOCS as a flat list of dicts with
"source" and "text" keys, matching the structure used in evaluation mock data:

    CONTEXT_DOCS = [
        {"source": "filename.pdf (Page 3)", "text": "..."},
        ...
    ]

Tables found in chunk metadata are appended to the text field in Markdown
format.  Images (base64) are noted as a placeholder comment in the text so
the entry is not silently empty.

Run directly:
    python -m evaluation_for_paper.combine_paper_sources
"""

from __future__ import annotations

import os
import pprint
from datetime import datetime

from evaluation_for_paper.text_after_chunking import query_text_chunks
from evaluation_for_paper.image_table_after_chunking import query_media_chunks

# ---------------------------------------------------------------------------
# Output directory
# ---------------------------------------------------------------------------

_OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "paper_sources")


# ---------------------------------------------------------------------------
# Core combine logic
# ---------------------------------------------------------------------------

def _build_source_label(file_name: str, page: int) -> str:
    """Return a source label like 'report.pdf (Page 5)' or 'report.pdf' if page is 0."""
    if page:
        return f"{file_name} (Page {page})"
    return file_name


def _build_text(text: str, tables_markdown: list[str], images_base64: list[str]) -> str:
    """
    Combine raw text with any Markdown tables and an image placeholder.

    Tables are appended after the text, separated by a blank line.
    Images are represented as a one-line placeholder so the entry is not empty.
    """
    parts: list[str] = []

    if text.strip():
        parts.append(text.strip())

    for table in tables_markdown:
        if table.strip():
            parts.append(table.strip())

    if images_base64:
        count = len(images_base64)
        parts.append(f"[{count} image(s) available in base64 format]")

    return "\n\n".join(parts)


def _merge_to_flat_list(
    text_data: dict,   # document_file_name -> [text_chunk_dict, ...]
    media_data: dict,  # document_file_name -> [media_chunk_dict, ...]
) -> list[dict]:
    """
    Merge text and media for a single paper and return a flat list of
    {"source": str, "text": str} dicts, sorted by document name then chunk_index.
    """
    flat: list[dict] = []

    for doc_name in sorted(text_data.keys()):
        text_chunks = text_data.get(doc_name, [])

        # Build lookup: chunk_id -> media chunk
        media_by_id: dict[str, dict] = {
            mc["chunk_id"]: mc
            for mc in media_data.get(doc_name, [])
        }

        for tc in text_chunks:
            mc = media_by_id.get(tc["chunk_id"], {})
            tables_markdown: list[str] = mc.get("tables_markdown", [])
            images_base64: list[str] = mc.get("images_base64", [])

            flat.append(
                {
                    "source": _build_source_label(tc["source"], tc["page"]),
                    "text": _build_text(tc["text"], tables_markdown, images_base64),
                }
            )

    return flat


def combine_and_write() -> None:
    """
    Main entry point: query DB, merge data, write one .py file per paper.
    """
    os.makedirs(_OUTPUT_DIR, exist_ok=True)

    text_all = query_text_chunks()    # paper_name -> doc_name -> [chunk, ...]
    media_all = query_media_chunks()  # paper_name -> doc_name -> [chunk, ...]

    # Sort paper names alphabetically for deterministic file numbering
    paper_names = sorted(set(list(text_all.keys()) + list(media_all.keys())))

    summary_lines: list[str] = []

    for i, paper_name in enumerate(paper_names, start=1):
        text_data = text_all.get(paper_name, {})
        media_data = media_all.get(paper_name, {})

        context_docs = _merge_to_flat_list(text_data, media_data)

        num_docs = len(text_data)
        total_chunks = len(context_docs)

        out_path = os.path.join(_OUTPUT_DIR, f"paper_{i}.py")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write('"""\n')
            fh.write(f'Auto-generated context source for paper: {paper_name}\n')
            fh.write(f'Generated: {timestamp}\n')
            fh.write('"""\n\n')
            fh.write('from __future__ import annotations\n\n')
            fh.write('CONTEXT_DOCS = ')
            fh.write(pprint.pformat(context_docs, indent=4, width=120))
            fh.write('\n')

        summary_lines.append(
            f"  paper_{i}.py -> {paper_name} ({num_docs} documents, {total_chunks} total chunks)"
        )

    print(f"Generated {len(paper_names)} paper source files in evaluation_for_paper/paper_sources/")
    for line in summary_lines:
        print(line)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    combine_and_write()
