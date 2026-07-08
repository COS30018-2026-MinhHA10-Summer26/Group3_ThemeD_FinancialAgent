import re
from io import BytesIO
import pdfplumber
from pypdf import PdfReader
import fitz

def _build_header_from_multirow(data):
    """
    Detects and merges multi-row headers by propagating non-empty cells
    downward (simulating colspan/rowspan) and combining row levels with ' > '.
    Stops when a row looks like data (contains numbers).
    """
    header_rows = []
    data_start = 0

    for i, row in enumerate(data):
        # A row is a data row if >50% of cells contain digits
        numeric_cells = sum(
            1 for cell in row
            if cell and re.search(r"\d", str(cell))
        )
        non_empty = sum(1 for cell in row if cell and str(cell).strip())
        is_data_row = non_empty > 0 and numeric_cells / max(non_empty, 1) > 0.5

        if is_data_row and header_rows:
            data_start = i
            break
        header_rows.append([str(cell or "").strip() for cell in row])
    else:
        # All rows were headers (shouldn't happen), treat first row as only header
        if not data_start:
            return [" | ".join(str(c or "") for c in data[0])], 1

    if not header_rows:
        return [" | ".join(str(c or "") for c in data[0])], 1

    # Forward-fill empty cells horizontally within each header row
    # (handles colspan: "Three Months Ended | | | Twelve Months Ended | |")
    filled_rows = []
    for row in header_rows:
        filled = []
        last = ""
        for cell in row:
            if cell:
                last = cell
                filled.append(cell)
            else:
                filled.append(last)  # propagate left neighbor into empty cell
        filled_rows.append(filled)

    # Combine header levels per column: "Three Months Ended > Sep 27, 2025"
    num_cols = max(len(row) for row in filled_rows)
    combined_cols = []
    for col_idx in range(num_cols):
        parts = []
        seen = set()
        for row in filled_rows:
            cell = row[col_idx] if col_idx < len(row) else ""
            # Deduplicate repeated labels across rows
            if cell and cell not in seen:
                parts.append(cell)
                seen.add(cell)
        combined_cols.append(" > ".join(parts) if parts else "")

    header_line = " | ".join(combined_cols)
    return [header_line], data_start

def _extract_table_section(table, source, page_number, table_idx):
    data = table.extract()
    if not data:
        return None

    # Replace nulls with empty strings throughout
    data = [
        [str(cell or "").strip() for cell in row]
        for row in data
    ]

    # Build merged header, get index where data rows start
    header_lines, data_start = _build_header_from_multirow(data)

    # Format data rows using the resolved column count
    rows = []
    for row in data[data_start:]:
        if not any(cell.strip() for cell in row):
            continue  # skip blank rows
        rows.append(" | ".join(row))

    table_text = "\n".join(header_lines + rows)

    return {
        "text": table_text,
        "source": source,
        "page": page_number,
        "section_title": f"table_{table_idx}",
        "section_type": "table",
    }
def _make_section(text, source, page, section_title=None, section_type="body"):
    paragraphs = []
    for block in re.split(r"\n\s*\n", text):
        lines = [re.sub(r"\s+", " ", line).strip() for line in block.splitlines()]
        compact = " ".join(line for line in lines if line).strip()
        if compact:
            paragraphs.append(compact)

    normalized = "\n\n".join(paragraphs).strip()
    if not normalized:
        return None

    return {
        "text": normalized,
        "source": source,
        "page": page,
        "section_title": section_title,
        "section_type": section_type,
    }

def extract_sections_from_pdf(source):
    doc = fitz.open(source)
    sections = []
    for page_number, page in enumerate(doc):
        #
        # 1. Extract Tables
        #
        try:
            tables = page.find_tables()
            for table_idx, table in enumerate(tables.tables):
                section = _extract_table_section(table, source, page_number, table_idx)
                if section:
                    sections.append(section)

        except Exception as e:
            print(
                f"Table extraction failed on page "
                f"{page_number}: {e}"
            )
        blocks = page.get_text("blocks")

        text_blocks = []

        for block in blocks:

            text = block[4]

            if not text:
                continue

            cleaned = text.strip()

            if not cleaned:
                continue

            text_blocks.append(cleaned)

        page_text = "\n\n".join(text_blocks)

        section = _make_section(
            page_text,
            source=source,
            page=page_number,
            section_type="body",
        )

        if section:
            sections.append(section)

    return sections

def extract_documents(source):
    sections = extract_sections_from_pdf(source)
    if sections:
        return sections
    else:
        print(f"No text extracted from PDF: {source}")
        return []