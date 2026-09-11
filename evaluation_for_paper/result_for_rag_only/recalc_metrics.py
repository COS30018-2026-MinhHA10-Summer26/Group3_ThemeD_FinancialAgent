"""
Recalculate OVERALL weighted scores in metrics.py after manually editing scores.

EDIT WORKFLOW:
  1. Open a metrics.py file
  2. Edit the V0 / V1 / V2 numbers DIRECTLY IN THE METRICS_TABLE ASCII table, e.g.:
       | Financial Accuracy   |    25% |       70 |  ...   <-- change 70 to 85
  3. Run this script — it reads the edited table, recalculates every delta,
     weighted contribution, and OVERALL, then overwrites the file in-place.

Usage:
    # Recalculate a single file:
    python3 evaluation_for_paper/result_for_rag_only/recalc_metrics.py \\
        evaluation_for_paper/result_for_rag_only/document_1/query_1/metrics.py

    # Recalculate ALL metrics.py files under result_for_rag_only/:
    python3 evaluation_for_paper/result_for_rag_only/recalc_metrics.py
"""

from __future__ import annotations

import json
import sys
import textwrap
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Criterion weights (must match run_rag_metrics.py)
# ---------------------------------------------------------------------------

CRITERIA: List[Dict[str, Any]] = [
    {"key": "financial_accuracy", "label": "Financial Accuracy", "weight": 0.25},
    {"key": "business_analysis",  "label": "Business Analysis",  "weight": 0.15},
    {"key": "risk_assessment",    "label": "Risk Assessment",    "weight": 0.15},
    {"key": "actionable_advice",  "label": "Actionable Advice",  "weight": 0.15},
    {"key": "evidence_usage",     "label": "Evidence Usage",     "weight": 0.10},
    {"key": "completeness",       "label": "Completeness",       "weight": 0.10},
    {"key": "query_satisfaction", "label": "Query Satisfaction", "weight": 0.10},
]


# ---------------------------------------------------------------------------
# Parse scores from the METRICS_TABLE ASCII table
# ---------------------------------------------------------------------------

def parse_scores_from_table(
    metrics_table_text: str,
    criteria: List[Dict[str, Any]],
) -> Dict[str, Dict[str, int]]:
    """
    Read v0_score / v1_score / v2_score per criterion from the ASCII table.

    Each data row looks like:
        | Financial Accuracy   |    25% |       70 |      100 |       80 |     +30 |     -20 |
    After split on '|' and strip:
        parts[1] = Criterion label
        parts[2] = Weight
        parts[3] = V0 score   <-- edit this
        parts[4] = V1 score   <-- edit this
        parts[5] = V2 score   <-- edit this
        parts[6] = dV1-V0  (recalculated, ignore when reading)
        parts[7] = dV2-dV1 (recalculated, ignore when reading)

    Returns: { criterion_key: {"v0": int, "v1": int, "v2": int} }
    """
    label_to_key = {c["label"]: c["key"] for c in criteria}
    scores: Dict[str, Dict[str, int]] = {}

    for line in metrics_table_text.splitlines():
        stripped = line.strip()
        # Only process data rows (not separator lines or header rows)
        if not stripped.startswith("|") or stripped.startswith("+"):
            continue
        parts = [p.strip() for p in stripped.split("|")]
        # parts[0] == '' (empty before first |), parts[1] == label, etc.
        if len(parts) < 7:
            continue
        label = parts[1]
        if label not in label_to_key:
            continue  # Skip header row, OVERALL row, etc.
        try:
            v0 = max(0, min(100, int(parts[3])))
            v1 = max(0, min(100, int(parts[4])))
            v2 = max(0, min(100, int(parts[5])))
        except (ValueError, IndexError):
            continue
        scores[label_to_key[label]] = {"v0": v0, "v1": v1, "v2": v2}

    return scores


# ---------------------------------------------------------------------------
# Recompute full METRICS dict from parsed scores
# ---------------------------------------------------------------------------

def recompute_metrics(
    parsed_scores: Dict[str, Dict[str, int]],
    criteria: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Rebuild the full METRICS dict from {key: {v0, v1, v2}} scores."""
    details: Dict[str, Any] = {}
    wv0 = wv1 = wv2 = 0.0

    for c in criteria:
        key = c["key"]
        w   = c["weight"]
        entry = parsed_scores.get(key, {"v0": 0, "v1": 0, "v2": 0})
        v0 = entry["v0"]
        v1 = entry["v1"]
        v2 = entry["v2"]

        c0 = round(v0 * w, 2)
        c1 = round(v1 * w, 2)
        c2 = round(v2 * w, 2)
        wv0 += c0
        wv1 += c1
        wv2 += c2

        details[key] = {
            "label":       c["label"],
            "weight_pct":  int(w * 100),
            "v0_score":    v0,
            "v1_score":    v1,
            "v2_score":    v2,
            "delta_v1_v0": v1 - v0,
            "delta_v2_v1": v2 - v1,
            "weighted_v0": c0,
            "weighted_v1": c1,
            "weighted_v2": c2,
        }

    ov0 = round(wv0, 2)
    ov1 = round(wv1, 2)
    ov2 = round(wv2, 2)

    def _pct(new: float, base: float) -> float:
        return round(((new - base) / base) * 100, 2) if base != 0 else 0.0

    return {
        "criteria_detail": details,
        "overall_v0": ov0,
        "overall_v1": ov1,
        "overall_v2": ov2,
        "v1_vs_v0_abs": round(ov1 - ov0, 2),
        "v1_vs_v0_pct": _pct(ov1, ov0),
        "v2_vs_v1_abs": round(ov2 - ov1, 2),
        "v2_vs_v1_pct": _pct(ov2, ov1),
    }


# ---------------------------------------------------------------------------
# Table formatter (identical to run_rag_metrics.py)
# ---------------------------------------------------------------------------

def format_metrics_table(metrics: Dict[str, Any], label: str) -> str:
    details = metrics["criteria_detail"]
    col_widths = [22, 8, 10, 10, 10, 9, 9]
    sep = "+" + "+".join("-" * w for w in col_widths) + "+"

    def _cell(val, width, is_label=False):
        s = str(val)
        return f" {s:<{width - 2}} " if is_label else f" {s:>{width - 2}} "

    def _row(cells):
        parts = [_cell(cells[i], col_widths[i], is_label=(i == 0))
                 for i in range(len(col_widths))]
        return "|" + "|".join(parts) + "|"

    def _d(n):
        return f"+{n}" if n >= 0 else str(n)

    lines = [
        "",
        "=" * 82,
        f"  RAG vs Pipeline Metrics -- {label}",
        "  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised",
        "=" * 82,
        sep,
        _row(["Criterion", "Weight", "V0 (RAG)", "V1 Adv.", "V2 Rev.", "dV1-V0", "dV2-dV1"]),
        sep,
    ]
    for key, d in details.items():
        lines.append(_row([
            d["label"],
            f"{d['weight_pct']}%",
            d["v0_score"],
            d["v1_score"],
            d["v2_score"],
            _d(d["delta_v1_v0"]),
            _d(d["delta_v2_v1"]),
        ]))
    lines.append(sep)
    lines.append(_row([
        "OVERALL (weighted)", "",
        f"{metrics['overall_v0']:.2f}",
        f"{metrics['overall_v1']:.2f}",
        f"{metrics['overall_v2']:.2f}",
        _d(metrics["v1_vs_v0_abs"]),
        _d(metrics["v2_vs_v1_abs"]),
    ]))
    lines.append(sep)
    lines += [
        f"  V1 vs V0: {_d(metrics['v1_vs_v0_abs'])} pts  |  {metrics['v1_vs_v0_pct']:+.2f}%",
        f"  V2 vs V1: {_d(metrics['v2_vs_v1_abs'])} pts  |  {metrics['v2_vs_v1_pct']:+.2f}%",
        "=" * 82,
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File reader (exec-based, avoids module cache issues)
# ---------------------------------------------------------------------------

def _read_file_vars(path: Path) -> Dict[str, Any]:
    """Execute the .py file in a fresh namespace and return all its variables."""
    namespace: Dict[str, Any] = {}
    source = path.read_text(encoding="utf-8")
    exec(compile(source, str(path), "exec"), namespace)
    return namespace


# ---------------------------------------------------------------------------
# File rewriter — preserves header (docstring + imports + USER_QUERY + RAG_RESPONSE)
# ---------------------------------------------------------------------------

def rewrite_metrics_py(
    path: Path,
    new_metrics: Dict[str, Any],
    table_str: str,
) -> None:
    old_text = path.read_text(encoding="utf-8")

    # Keep everything before the first comment-block marker
    marker = "# -------------------------------------------------------------------"
    marker_idx = old_text.find(marker)
    if marker_idx == -1:
        # Fallback: find METRICS_TABLE variable declaration
        marker_idx = old_text.find("METRICS_TABLE")
    if marker_idx == -1:
        # Last resort: keep first 10 lines
        header = "\n".join(old_text.splitlines()[:10]) + "\n\n"
    else:
        header = old_text[:marker_idx]

    metrics_repr = json.dumps(new_metrics, indent=4, ensure_ascii=False)
    metrics_repr_indented = textwrap.indent(metrics_repr, "    ")

    new_text = (
        header
        + "# -------------------------------------------------------------------\n"
        "# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)\n"
        "#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:\n"
        "#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL\n"
        "# -------------------------------------------------------------------\n"
        'METRICS_TABLE = """\n'
        f"{table_str}\n"
        '"""\n\n'
        "# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)\n"
        "METRICS = \\\n"
        f"{metrics_repr_indented}\n"
    )
    path.write_text(new_text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Process one file
# ---------------------------------------------------------------------------

def process_file(path: Path) -> None:
    file_vars = _read_file_vars(path)

    metrics_table_text: str = file_vars.get("METRICS_TABLE", "")
    if not metrics_table_text.strip():
        print(f"  [SKIP] {path} -- METRICS_TABLE is empty or missing")
        return

    # Derive label from folder structure  (e.g. document_1/query_2)
    label = f"{path.parent.parent.name}/{path.parent.name}"

    # Parse scores from the ASCII table (what the user edited)
    parsed_scores = parse_scores_from_table(metrics_table_text, CRITERIA)

    if len(parsed_scores) < len(CRITERIA):
        missing = [c["key"] for c in CRITERIA if c["key"] not in parsed_scores]
        print(f"  [WARN] {path} -- could not parse scores for: {missing}")
        if not parsed_scores:
            print("  [SKIP] no scores parsed at all")
            return

    # Recompute all weighted fields
    new_metrics = recompute_metrics(parsed_scores, CRITERIA)

    # Rebuild and print the updated table
    new_table_str = format_metrics_table(new_metrics, label)
    print(new_table_str)

    # Overwrite the file
    rewrite_metrics_py(path, new_metrics, new_table_str)
    print(f"  [OK] Updated: {path}\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    script_dir = Path(__file__).resolve().parent  # result_for_rag_only/

    if len(sys.argv) > 1:
        targets = [Path(a).resolve() for a in sys.argv[1:]]
    else:
        targets = sorted(script_dir.rglob("metrics.py"))

    if not targets:
        print("No metrics.py files found.")
        print("Pass a path as argument, or run from the result_for_rag_only/ directory.")
        return

    print(f"Recalculating {len(targets)} file(s)...\n")
    errors = 0
    for t in targets:
        if not t.exists():
            print(f"  [MISSING] {t}")
            errors += 1
            continue
        try:
            process_file(t)
        except Exception as exc:
            errors += 1
            print(f"  [ERROR] {t}: {exc}")

    print(f"Done. {len(targets)} file(s) processed, {errors} error(s).")


if __name__ == "__main__":
    main()
