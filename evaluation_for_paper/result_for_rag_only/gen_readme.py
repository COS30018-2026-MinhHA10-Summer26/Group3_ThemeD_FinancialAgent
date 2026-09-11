"""
Generate README.md for every query folder in result_for_rag_only/.

Each README.md is placed in the same folder as metrics.py and contains:
  - The user query
  - The RAG response
  - The 7-criterion comparison table

Run AFTER run_rag_metrics.py has generated all metrics.py files.

Usage:
    python3 evaluation_for_paper/result_for_rag_only/gen_readme.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

SCRIPT_DIR = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Load variables from a .py file via exec (no module cache issues)
# ---------------------------------------------------------------------------

def _read_file_vars(path: Path) -> Dict[str, Any]:
    namespace: Dict[str, Any] = {}
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace)
    return namespace


# ---------------------------------------------------------------------------
# README writer
# ---------------------------------------------------------------------------

def write_readme(metrics_path: Path) -> None:
    vars_ = _read_file_vars(metrics_path)

    user_query: str      = vars_.get("USER_QUERY",     "").strip()
    rag_response: str    = vars_.get("RAG_RESPONSE",   "").strip()
    metrics_table: str   = vars_.get("METRICS_TABLE",  "").strip()
    metrics: dict        = vars_.get("METRICS",        {})

    doc_name   = metrics_path.parent.parent.name   # e.g. document_1
    query_name = metrics_path.parent.name           # e.g. query_1

    doc_num   = doc_name.replace("document_", "Document ")
    query_num = query_name.replace("query_", "Query ")

    # --- Overall summary line ---
    ov0 = metrics.get("overall_v0", "N/A")
    ov1 = metrics.get("overall_v1", "N/A")
    ov2 = metrics.get("overall_v2", "N/A")
    v1v0 = metrics.get("v1_vs_v0_abs", "N/A")
    v1v0_pct = metrics.get("v1_vs_v0_pct", "N/A")
    v2v1 = metrics.get("v2_vs_v1_abs", "N/A")
    v2v1_pct = metrics.get("v2_vs_v1_pct", "N/A")

    def _sign(v):
        if isinstance(v, (int, float)):
            return f"+{v}" if v >= 0 else str(v)
        return str(v)

    # --- Markdown table: V0 | V1 | V2 | dV1-V0 | dV2-dV1 (no Criterion column) ---
    cd = metrics.get("criteria_detail", {})
    md_rows = []
    for key, d in cd.items():
        dv1 = _sign(d.get("delta_v1_v0", 0))
        dv2 = _sign(d.get("delta_v2_v1", 0))
        md_rows.append(
            f"| {d.get('v0_score', 0):>8} "
            f"| {d.get('v1_score', 0):>7} "
            f"| {d.get('v2_score', 0):>7} "
            f"| {dv1:>7} "
            f"| {dv2:>8} |"
        )

    ov0 = metrics.get("overall_v0", "N/A")
    ov1 = metrics.get("overall_v1", "N/A")
    ov2 = metrics.get("overall_v2", "N/A")
    v1v0 = metrics.get("v1_vs_v0_abs", "N/A")
    v2v1 = metrics.get("v2_vs_v1_abs", "N/A")

    md_table = "\n".join([
        "| V0 (RAG) | V1 Adv. | V2 Rev. | dV1-V0 | dV2-dV1 |",
        "|---------:|--------:|--------:|-------:|---------:|",
    ] + md_rows + [
        f"| **{ov0}** | **{ov1}** | **{ov2}** | **{_sign(v1v0)}** | **{_sign(v2v1)}** |",
    ])

    readme_content = f"""\
# {doc_num} — {query_num}

## Query

> {user_query}

## 7-Criterion Metrics

{md_table}
"""

    out_path = metrics_path.parent / "README.md"
    out_path.write_text(readme_content, encoding="utf-8")
    print(f"  [OK] {doc_name}/{query_name}/README.md")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    metrics_files = sorted(SCRIPT_DIR.rglob("metrics.py"))

    if not metrics_files:
        print("No metrics.py files found under result_for_rag_only/")
        print("Run run_rag_metrics.py first to generate them.")
        return

    print(f"Generating README.md for {len(metrics_files)} file(s)...\n")
    errors = 0
    for mf in metrics_files:
        try:
            write_readme(mf)
        except Exception as exc:
            errors += 1
            print(f"  [ERROR] {mf}: {exc}")

    print(f"\nDone. {len(metrics_files)} README(s) written, {errors} error(s).")


if __name__ == "__main__":
    main()
