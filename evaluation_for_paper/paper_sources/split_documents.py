"""
split_documents.py

Reads CONTEXT_DOCS from paper_1.py, partitions entries by PDF filename,
and writes 7 document_N.py files to the same directory.
"""

from __future__ import annotations

import os
import pprint

from evaluation_for_paper.paper_sources.paper_1 import CONTEXT_DOCS

# ---------------------------------------------------------------------------
# Document order (determines output file numbering 1–7)
# ---------------------------------------------------------------------------
DOC_ORDER = [
    "NASDAQ_AMZN_2022.pdf",
    "NASDAQ_AMZN_2023.pdf",
    "NASDAQ_AMZN_2024.pdf",
    "NASDAQ_AMZN_2025.pdf",
    "NASDAQ_TSLA_2022.pdf",
    "NASDAQ_TSLA_2023.pdf",
    "NASDAQ_TSLA_2024.pdf",
]

# ---------------------------------------------------------------------------
# Per-document user queries (8 questions each)
# ---------------------------------------------------------------------------
USER_QUERIES = {
    "NASDAQ_AMZN_2022.pdf": [
        "What were Amazon's total net sales and net income for fiscal year 2022?",
        "How did Amazon's AWS segment perform in 2022 compared to prior years?",
        "What were the major cost drivers that impacted Amazon's operating income in 2022?",
        "What is Amazon's free cash flow position and how did it change in 2022?",
        "What key risks does Amazon identify in its 2022 annual report?",
        "How did Amazon's international segment perform financially in 2022?",
        "What were Amazon's capital expenditure and investment priorities in 2022?",
        "What is Amazon's outlook and strategic priorities discussed in the 2022 annual report?",
    ],
    "NASDAQ_AMZN_2023.pdf": [
        "What were Amazon's total revenues and operating income for fiscal year 2023?",
        "How did AWS revenue growth trend in 2023 and what drove it?",
        "What cost optimization measures did Amazon undertake in 2023?",
        "How did Amazon's advertising revenue segment grow in 2023?",
        "What were the key balance sheet highlights for Amazon at the end of 2023?",
        "How did Amazon's North America segment margin recover in 2023?",
        "What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?",
        "What generative AI and technology investments did Amazon highlight in 2023?",
    ],
    "NASDAQ_AMZN_2024.pdf": [
        "What were Amazon's total net sales and earnings per share for fiscal year 2024?",
        "How did AWS perform in 2024 and what was its contribution to operating profit?",
        "What were the highlights of Amazon's logistics and fulfillment network in 2024?",
        "How did Amazon's subscription services revenue evolve in 2024?",
        "What were Amazon's major capital allocation decisions in 2024?",
        "How did Amazon's international operations perform in 2024?",
        "What were the significant legal and regulatory risks Amazon faced in 2024?",
        "What AI and cloud strategy shifts did Amazon announce or execute in 2024?",
    ],
    "NASDAQ_AMZN_2025.pdf": [
        "What were Amazon's key financial results and revenue breakdown for fiscal year 2025?",
        "How did Amazon's AWS segment grow in 2025 and what products drove demand?",
        "What is Amazon's profitability trend and operating margin outlook for 2025?",
        "What strategic acquisitions or investments did Amazon make in 2025?",
        "How did macroeconomic conditions affect Amazon's business in 2025?",
        "What is Amazon's cash and debt position at the end of fiscal year 2025?",
        "How did Amazon's Prime membership and subscription services perform in 2025?",
        "What does Amazon's 2025 annual report say about its long-term growth strategy?",
    ],
    "NASDAQ_TSLA_2022.pdf": [
        "What were Tesla's total revenues and net income for fiscal year 2022?",
        "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?",
        "What were the key financial ratios and margins for Tesla in 2022?",
        "How did Tesla's energy generation and storage segment perform in 2022?",
        "What were the main risks Tesla identified in its 2022 annual report?",
        "What were Tesla's capital expenditures and free cash flow in 2022?",
        "How did supply chain challenges impact Tesla's production in 2022?",
        "What is Tesla's growth strategy and future product roadmap as outlined in 2022?",
    ],
    "NASDAQ_TSLA_2023.pdf": [
        "What were Tesla's total revenues and operating income for fiscal year 2023?",
        "How did Tesla's vehicle average selling price and gross margin trend in 2023?",
        "What were Tesla's total vehicle deliveries and production volumes in 2023?",
        "How did Tesla's energy storage deployment grow in 2023?",
        "What cost reduction initiatives did Tesla implement in 2023?",
        "What were the key balance sheet metrics for Tesla at the end of 2023?",
        "What risks related to competition and pricing pressure did Tesla disclose in 2023?",
        "What is Tesla's outlook for new vehicle models and production expansion in 2023?",
    ],
    "NASDAQ_TSLA_2024.pdf": [
        "What were Tesla's total revenues, operating income, and net income for fiscal year 2024?",
        "How did Tesla's vehicle delivery volumes and production change in 2024?",
        "What was Tesla's gross margin on automotive sales in 2024 and how did it compare to 2023?",
        "How did Tesla's Full Self-Driving and AI initiatives progress in 2024?",
        "What were the highlights of Tesla's energy and services segments in 2024?",
        "What major capital investments did Tesla make in 2024?",
        "What regulatory and competitive risks did Tesla highlight in its 2024 annual report?",
        "What does Tesla's 2024 annual report say about its Optimus robot and future technology roadmap?",
    ],
}


def _company_name(pdf_filename: str) -> str:
    """Map ticker abbreviation to full company name."""
    if "AMZN" in pdf_filename:
        return "Amazon"
    if "TSLA" in pdf_filename:
        return "Tesla"
    return pdf_filename


def _fiscal_year(pdf_filename: str) -> str:
    """Extract the 4-digit year from the filename."""
    # e.g. NASDAQ_AMZN_2022.pdf -> 2022
    for part in pdf_filename.replace(".pdf", "").split("_"):
        if part.isdigit() and len(part) == 4:
            return part
    return "Unknown"


def _format_queries_block(queries: list[str]) -> str:
    """Render USER_QUERY and USER_QUERIES as clean Python literals."""
    lines: list[str] = []

    # USER_QUERY — single string (first question)
    first = queries[0].replace('"', '\\"')
    lines.append(f'USER_QUERY = (')
    lines.append(f'    "{first}"')
    lines.append(f')')
    lines.append("")

    # USER_QUERIES — list of all 8 questions
    lines.append("USER_QUERIES = [")
    for q in queries:
        escaped = q.replace('"', '\\"')
        lines.append(f'    "{escaped}",')
    lines.append("]")

    return "\n".join(lines)


def split(output_dir: str | None = None) -> None:
    """Partition CONTEXT_DOCS by PDF source and write document_N.py files."""

    if output_dir is None:
        output_dir = os.path.dirname(os.path.abspath(__file__))

    # Partition chunks by PDF filename
    partitions: dict[str, list[dict]] = {pdf: [] for pdf in DOC_ORDER}
    for entry in CONTEXT_DOCS:
        key = entry["source"].split(" (")[0]
        if key in partitions:
            partitions[key].append(entry)
        # Entries with unknown keys are silently skipped

    print("Split paper_1.py into 7 document files:")

    for i, pdf_filename in enumerate(DOC_ORDER, start=1):
        chunks = partitions[pdf_filename]
        year = _fiscal_year(pdf_filename)
        company = _company_name(pdf_filename)
        queries = USER_QUERIES[pdf_filename]

        # Build the file content
        doc_lines: list[str] = []

        # Module docstring
        doc_lines.append(f'"""')
        doc_lines.append(f"Context source for: {pdf_filename}")
        doc_lines.append(f"Fiscal Year: {year}")
        doc_lines.append(f'"""')
        doc_lines.append("")

        # Future import
        doc_lines.append("from __future__ import annotations")
        doc_lines.append("")

        # USER_QUERY + USER_QUERIES block
        doc_lines.append(_format_queries_block(queries))
        doc_lines.append("")

        # CONTEXT_DOCS
        if chunks:
            formatted = pprint.pformat(chunks, width=120, indent=4)
            doc_lines.append(f"CONTEXT_DOCS = {formatted}")
        else:
            doc_lines.append("# No chunks found for this document")
            doc_lines.append("CONTEXT_DOCS = []")

        doc_lines.append("")  # trailing newline

        # Write the file
        out_path = os.path.join(output_dir, f"document_{i}.py")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(doc_lines))

        n = len(chunks)
        print(f"  document_{i}.py -> {pdf_filename} ({n} chunks)")


if __name__ == "__main__":
    split()
