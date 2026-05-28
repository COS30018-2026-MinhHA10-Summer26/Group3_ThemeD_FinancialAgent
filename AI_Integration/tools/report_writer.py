"""
Structured markdown report writer for the financial agent.
"""

from __future__ import annotations

from typing import Any


def write_report(
    *,
    query: str,
    response: str,
    context_documents: list[dict[str, Any]],
) -> str:
    """Generate a markdown report from the final response and evidence."""

    lines = [
        f"# Financial Research Report",
        "",
        f"## Query",
        query,
        "",
        f"## Analysis",
        response,
        "",
        "## Supporting Context",
    ]

    if not context_documents:
        lines.append("- No supporting context was available.")
    else:
        for document in context_documents:
            source = str(document.get("source", document.get("title", "unknown")))
            content = str(document.get("content", "")).strip()
            snippet = content[:300] + ("..." if len(content) > 300 else "")
            lines.append(f"- **{source}**: {snippet}")

    return "\n".join(lines)
