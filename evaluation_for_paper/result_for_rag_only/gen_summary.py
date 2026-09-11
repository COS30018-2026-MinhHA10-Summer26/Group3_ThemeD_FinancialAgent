"""
Generate SUMMARY.md in result_for_rag_only/ — two aggregated tables across all
56 scenarios (7 documents × 8 queries), similar to Tables I & II in the paper.

Table I  — Per-Scenario Comparison
  Columns: Scenario | V0 Score | V1 Score | V2 Score | dV1-V0 | dV1-V0% | dV2-V1 | dV2-V1%
  Rows: one per (document, query) pair, sorted doc→query; Mean row at bottom.

Table II — Per-Criterion Averages
  Columns: Criterion | Weight | Avg V0 | Avg V1 | Avg V2 | Avg dV1-V0 | Avg dV2-V1
  Rows: one per criterion; Overall (weighted) row at bottom.

Run AFTER run_rag_metrics.py has generated all metrics.py files.

Usage:
    python3 evaluation_for_paper/result_for_rag_only/gen_summary.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SCRIPT_DIR = Path(__file__).resolve().parent

CRITERIA_ORDER = [
    ("financial_accuracy", "Financial Accuracy", 0.25),
    ("business_analysis",  "Business Analysis",  0.15),
    ("risk_assessment",    "Risk Assessment",     0.15),
    ("actionable_advice",  "Actionable Advice",   0.15),
    ("evidence_usage",     "Evidence Usage",      0.10),
    ("completeness",       "Completeness",        0.10),
    ("query_satisfaction", "Query Satisfaction",  0.10),
]


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

def _read_file_vars(path: Path) -> Dict[str, Any]:
    namespace: Dict[str, Any] = {}
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace)
    return namespace


def load_all_metrics() -> List[Dict[str, Any]]:
    """Return a list of dicts, one per metrics.py found, sorted by doc→query."""
    results = []
    doc_dirs = sorted(
        p for p in SCRIPT_DIR.iterdir()
        if p.is_dir() and p.name.startswith("document_")
    )
    for doc_dir in doc_dirs:
        doc_idx = int(doc_dir.name.split("_")[1])
        query_dirs = sorted(
            p for p in doc_dir.iterdir()
            if p.is_dir() and p.name.startswith("query_")
        )
        for q_dir in query_dirs:
            q_idx = int(q_dir.name.split("_")[1])
            mf = q_dir / "metrics.py"
            if not mf.exists():
                print(f"  [MISSING] {doc_dir.name}/{q_dir.name}/metrics.py — skip")
                continue
            try:
                vars_ = _read_file_vars(mf)
                m = vars_.get("METRICS", {})
                if not m:
                    print(f"  [EMPTY] {doc_dir.name}/{q_dir.name} — skip")
                    continue
                results.append({
                    "label":    f"D{doc_idx}Q{q_idx}",
                    "doc_idx":  doc_idx,
                    "q_idx":    q_idx,
                    "metrics":  m,
                })
            except Exception as exc:
                print(f"  [ERROR] {doc_dir.name}/{q_dir.name}: {exc}")
    return results


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sign(v: float) -> str:
    return f"+{v}" if v >= 0 else str(v)


def _pct(new: float, base: float) -> float:
    return round(((new - base) / base) * 100, 2) if base != 0 else 0.0


def _fmt(v) -> str:
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


# ---------------------------------------------------------------------------
# Table I — Per-Scenario
# ---------------------------------------------------------------------------

def build_table1(records: List[Dict[str, Any]]) -> str:
    header = (
        "| Scenario | V0 Score | V1 Score | V2 Score "
        "| Abs Δ (V1-V0) | Rel Δ V1 (%) "
        "| Abs Δ (V2-V1) | Rel Δ V2 (%) |\n"
        "|----------|---------:|---------:|---------:"
        "|--------------:|-------------:"
        "|--------------:|-------------:|\n"
    )

    rows = []
    sum_v0 = sum_v1 = sum_v2 = 0.0
    n = len(records)

    for rec in records:
        m   = rec["metrics"]
        v0  = m.get("overall_v0", 0.0)
        v1  = m.get("overall_v1", 0.0)
        v2  = m.get("overall_v2", 0.0)
        d10 = m.get("v1_vs_v0_abs", round(v1 - v0, 2))
        p10 = m.get("v1_vs_v0_pct", _pct(v1, v0))
        d21 = m.get("v2_vs_v1_abs", round(v2 - v1, 2))
        p21 = m.get("v2_vs_v1_pct", _pct(v2, v1))
        sum_v0 += v0
        sum_v1 += v1
        sum_v2 += v2
        rows.append(
            f"| {rec['label']:<8} | {_fmt(v0):>8} | {_fmt(v1):>8} | {_fmt(v2):>8} "
            f"| {_sign(d10):>13} | {_sign(p10):>12} "
            f"| {_sign(d21):>13} | {_sign(p21):>12} |"
        )

    # Mean row
    if n:
        mv0 = round(sum_v0 / n, 2)
        mv1 = round(sum_v1 / n, 2)
        mv2 = round(sum_v2 / n, 2)
        md10 = round(mv1 - mv0, 2)
        mp10 = _pct(mv1, mv0)
        md21 = round(mv2 - mv1, 2)
        mp21 = _pct(mv2, mv1)
        rows.append(
            f"| **Mean** | **{_fmt(mv0)}** | **{_fmt(mv1)}** | **{_fmt(mv2)}** "
            f"| **{_sign(md10)}** | **{_sign(mp10)}** "
            f"| **{_sign(md21)}** | **{_sign(mp21)}** |"
        )

    return header + "\n".join(rows)


# ---------------------------------------------------------------------------
# Table II — Per-Criterion Averages  (+ Overall increase column)
# ---------------------------------------------------------------------------

def build_table2(records: List[Dict[str, Any]]) -> str:
    n = len(records)
    if n == 0:
        return "_No data_"

    # Accumulate sums per criterion
    sums: Dict[str, Dict[str, float]] = {
        key: {"v0": 0.0, "v1": 0.0, "v2": 0.0}
        for key, _, _ in CRITERIA_ORDER
    }

    for rec in records:
        cd = rec["metrics"].get("criteria_detail", {})
        for key, _, _ in CRITERIA_ORDER:
            d = cd.get(key, {})
            sums[key]["v0"] += d.get("v0_score", 0)
            sums[key]["v1"] += d.get("v1_score", 0)
            sums[key]["v2"] += d.get("v2_score", 0)

    header = (
        "| Criterion              | Weight "
        "| Avg V0 | Avg V1 | Avg V2 "
        "| Avg dV1-V0 | Avg dV2-V1 "
        "| Overall Increase (V0→V2) |\n"
        "|:-----------------------|-------:"
        "|-------:|-------:|-------:"
        "|-----------:|-----------:"
        "|------------------------:|\n"
    )

    rows = []
    overall_sum_v0 = overall_sum_v1 = overall_sum_v2 = 0.0

    for key, label, weight in CRITERIA_ORDER:
        s   = sums[key]
        av0 = round(s["v0"] / n, 1)
        av1 = round(s["v1"] / n, 1)
        av2 = round(s["v2"] / n, 1)
        d10 = round(av1 - av0, 1)
        d21 = round(av2 - av1, 1)
        d20 = round(av2 - av0, 1)   # overall increase V0→V2

        # Weighted contributions for the bottom row
        overall_sum_v0 += av0 * weight
        overall_sum_v1 += av1 * weight
        overall_sum_v2 += av2 * weight

        rows.append(
            f"| {label:<22} | {int(weight*100):>5}% "
            f"| {av0:>6} | {av1:>6} | {av2:>6} "
            f"| {_sign(d10):>10} | {_sign(d21):>10} "
            f"| {_sign(d20):>24} |"
        )

    # Overall (weighted) bottom row
    ov0 = round(overall_sum_v0, 2)
    ov1 = round(overall_sum_v1, 2)
    ov2 = round(overall_sum_v2, 2)
    od10 = round(ov1 - ov0, 2)
    od21 = round(ov2 - ov1, 2)
    od20 = round(ov2 - ov0, 2)
    rows.append(
        f"| **Overall (weighted)** |       "
        f"| **{ov0}** | **{ov1}** | **{ov2}** "
        f"| **{_sign(od10)}** | **{_sign(od21)}** "
        f"| **{_sign(od20)}** |"
    )

    return header + "\n".join(rows)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Loading metrics.py files...\n")
    records = load_all_metrics()

    if not records:
        print("No metrics.py files found. Run run_rag_metrics.py first.")
        return

    print(f"\nBuilding summary for {len(records)} scenarios...\n")

    table1 = build_table1(records)
    table2 = build_table2(records)

    summary_md = f"""\
# RAG vs Pipeline — Evaluation Summary

**Scenarios loaded:** {len(records)} / 56  
**V0** = RAG-only baseline · **V1** = Advisor initial · **V2** = Advisor revised after Critic

---

## Table I — Per-Scenario Comparison (Weighted Overall Scores)

{table1}

---

## Table II — Per-Criterion Averages Across All Scenarios

> "Overall Increase (V0→V2)" = average improvement from RAG baseline to final revised report.

{table2}

---

*Generated by `gen_summary.py`. Re-run after editing `metrics.py` files with `recalc_metrics.py`.*
"""

    out = SCRIPT_DIR / "SUMMARY.md"
    out.write_text(summary_md, encoding="utf-8")
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()
