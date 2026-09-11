"""
Wilcoxon Signed-Rank Test + Visualizations for RAG vs Pipeline evaluation.

Reads all metrics.py files under result_for_rag_only/ and performs
paired Wilcoxon tests on overall weighted scores (V0, V1, V2) across
all 56 scenarios, plus per-criterion breakdown.

Outputs (all in the same directory as this script):
  wilcoxon_results.md     — summary table (W, p-value, effect size r)
  plot_boxplot.png        — box plot with significance brackets
  plot_criteria_bar.png   — grouped bar chart per criterion
  plot_delta_hist.png     — histogram of per-scenario deltas

Usage:
    python3 evaluation_for_paper/result_for_rag_only/wilcoxon_test.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import numpy as np
import matplotlib
matplotlib.use("Agg")          # headless — no display needed
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats

SCRIPT_DIR = Path(__file__).resolve().parent

CRITERIA_ORDER = [
    ("financial_accuracy", "Fin. Accuracy",  0.25),
    ("business_analysis",  "Biz. Analysis",  0.15),
    ("risk_assessment",    "Risk Assess.",    0.15),
    ("actionable_advice",  "Action. Advice",  0.15),
    ("evidence_usage",     "Evidence Usage",  0.10),
    ("completeness",       "Completeness",    0.10),
    ("query_satisfaction", "Query Satisf.",   0.10),
]

# Significance thresholds
SIG_LEVELS = [(0.001, "***"), (0.01, "**"), (0.05, "*"), (1.0, "ns")]

def sig_label(p: float) -> str:
    for thresh, lbl in SIG_LEVELS:
        if p < thresh:
            return lbl
    return "ns"


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------

def _read_file_vars(path: Path) -> Dict[str, Any]:
    namespace: Dict[str, Any] = {}
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), namespace)
    return namespace


def load_all_metrics() -> List[Dict[str, Any]]:
    records = []
    for doc_dir in sorted(p for p in SCRIPT_DIR.iterdir()
                          if p.is_dir() and p.name.startswith("document_")):
        doc_idx = int(doc_dir.name.split("_")[1])
        for q_dir in sorted(p for p in doc_dir.iterdir()
                            if p.is_dir() and p.name.startswith("query_")):
            q_idx = int(q_dir.name.split("_")[1])
            mf = q_dir / "metrics.py"
            if not mf.exists():
                continue
            try:
                m = _read_file_vars(mf).get("METRICS", {})
                if m:
                    records.append({"doc": doc_idx, "q": q_idx, "metrics": m})
            except Exception as exc:
                print(f"  [WARN] {doc_dir.name}/{q_dir.name}: {exc}")
    return records


# ---------------------------------------------------------------------------
# Wilcoxon helper
# ---------------------------------------------------------------------------

def wilcoxon_pair(
    x: np.ndarray,
    y: np.ndarray,
    label: str = "",
) -> Dict[str, Any]:
    """
    Run Wilcoxon signed-rank test on paired arrays x, y.
    Returns dict with W, p, Z (normal approx), effect_size r, n.
    """
    diff = y - x
    n_nonzero = int(np.sum(diff != 0))

    if n_nonzero < 2:
        return {"label": label, "n": len(x), "n_nonzero": n_nonzero,
                "W": None, "p": None, "Z": None, "r": None, "sig": "—",
                "mean_x": round(float(np.mean(x)), 2),
                "mean_y": round(float(np.mean(y)), 2),
                "mean_diff": round(float(np.mean(diff)), 2)}

    W, p = stats.wilcoxon(x, y, alternative="two-sided")

    # Normal approximation for Z and effect size r
    mu_W  = n_nonzero * (n_nonzero + 1) / 4
    sig_W = np.sqrt(n_nonzero * (n_nonzero + 1) * (2 * n_nonzero + 1) / 24)
    Z     = (W - mu_W) / sig_W
    r     = abs(Z) / np.sqrt(n_nonzero)   # effect size r

    return {
        "label":     label,
        "n":         len(x),
        "n_nonzero": n_nonzero,
        "W":         round(float(W), 1),
        "p":         round(float(p), 4),
        "Z":         round(float(Z), 3),
        "r":         round(float(r), 3),
        "sig":       sig_label(float(p)),
        "mean_x":    round(float(np.mean(x)), 2),
        "mean_y":    round(float(np.mean(y)), 2),
        "mean_diff": round(float(np.mean(diff)), 2),
    }


# ---------------------------------------------------------------------------
# Plot 1: Box plot with significance brackets
# ---------------------------------------------------------------------------

def plot_boxplot(v0: np.ndarray, v1: np.ndarray, v2: np.ndarray,
                 res_v0v1, res_v0v2, res_v1v2, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(7, 5))
    fig.patch.set_facecolor("white")

    data   = [v0, v1, v2]
    labels = ["V0 (RAG)", "V1 Advisor", "V2 Revised"]
    colors = ["#4C72B0", "#DD8452", "#55A868"]

    bp = ax.boxplot(data, patch_artist=True, widths=0.45,
                    medianprops=dict(color="black", linewidth=2))
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.75)

    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylabel("Weighted Score (0–100)", fontsize=11)
    ax.set_title("Overall Score Distribution: V0 vs V1 vs V2", fontsize=13, fontweight="bold")
    ax.yaxis.grid(True, linestyle="--", alpha=0.7)
    ax.set_axisbelow(True)

    # Significance brackets
    y_max = max(v0.max(), v1.max(), v2.max())

    def _bracket(ax, x1, x2, y, label, color="black"):
        h = 1.5
        ax.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.2, color=color)
        ax.text((x1+x2)/2, y+h+0.2, label,
                ha="center", va="bottom", fontsize=11, color=color,
                fontweight="bold" if label != "ns" else "normal")

    base = y_max + 4
    gap  = 7

    def _p_str(res):
        if res["p"] is None:
            return "—"
        return f"{res['sig']} (p={res['p']:.3f})"

    _bracket(ax, 1, 2, base,       _p_str(res_v0v1), color="#2070b0")
    _bracket(ax, 2, 3, base,       _p_str(res_v1v2), color="#b05020")
    _bracket(ax, 1, 3, base+gap,   _p_str(res_v0v2), color="#208040")

    ax.set_ylim(bottom=max(0, min(v0.min(), v1.min(), v2.min()) - 5),
                top=base + gap + 12)

    # Legend: mean values
    means = [np.mean(v0), np.mean(v1), np.mean(v2)]
    patches = [mpatches.Patch(color=c, alpha=0.75, label=f"{l} (μ={m:.1f})")
               for c, l, m in zip(colors, labels, means)]
    ax.legend(handles=patches, loc="lower right", fontsize=9)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {out_path.name}")


# ---------------------------------------------------------------------------
# Plot 2: Grouped bar chart per criterion
# ---------------------------------------------------------------------------

def plot_criteria_bar(records: List[Dict], out_path: Path) -> None:
    n = len(records)
    if n == 0:
        return

    keys   = [k for k, _, _ in CRITERIA_ORDER]
    labels = [lbl for _, lbl, _ in CRITERIA_ORDER]
    avg_v0 = [np.mean([r["metrics"]["criteria_detail"].get(k, {}).get("v0_score", 0) for r in records]) for k in keys]
    avg_v1 = [np.mean([r["metrics"]["criteria_detail"].get(k, {}).get("v1_score", 0) for r in records]) for k in keys]
    avg_v2 = [np.mean([r["metrics"]["criteria_detail"].get(k, {}).get("v2_score", 0) for r in records]) for k in keys]
    std_v0 = [np.std( [r["metrics"]["criteria_detail"].get(k, {}).get("v0_score", 0) for r in records]) for k in keys]
    std_v1 = [np.std( [r["metrics"]["criteria_detail"].get(k, {}).get("v1_score", 0) for r in records]) for k in keys]
    std_v2 = [np.std( [r["metrics"]["criteria_detail"].get(k, {}).get("v2_score", 0) for r in records]) for k in keys]

    x   = np.arange(len(keys))
    w   = 0.26
    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor("white")

    colors = ["#4C72B0", "#DD8452", "#55A868"]
    for i, (avg, std, color, lbl) in enumerate(zip(
            [avg_v0, avg_v1, avg_v2],
            [std_v0, std_v1, std_v2],
            colors,
            ["V0 (RAG)", "V1 Advisor", "V2 Revised"])):
        ax.bar(x + (i-1)*w, avg, w, label=lbl, color=color, alpha=0.8,
               yerr=std, capsize=3, error_kw={"elinewidth": 1, "alpha": 0.6})

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9, rotation=15, ha="right")
    ax.set_ylabel("Average Score (0–100)", fontsize=11)
    ax.set_title("Per-Criterion Average Scores: V0 vs V1 vs V2\n(error bars = ±1 SD)", fontsize=12, fontweight="bold")
    ax.yaxis.grid(True, linestyle="--", alpha=0.6)
    ax.set_axisbelow(True)
    ax.set_ylim(0, 115)
    ax.legend(fontsize=10, loc="upper right")

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {out_path.name}")


# ---------------------------------------------------------------------------
# Plot 3: Delta histograms
# ---------------------------------------------------------------------------

def plot_delta_hist(v0: np.ndarray, v1: np.ndarray, v2: np.ndarray,
                    out_path: Path) -> None:
    d10 = v1 - v0   # V1 - V0
    d21 = v2 - v1   # V2 - V1
    d20 = v2 - v0   # V2 - V0

    fig, axes = plt.subplots(1, 3, figsize=(13, 4), sharey=False)
    fig.patch.set_facecolor("white")

    pairs = [
        (d10, "ΔV1-V0  (Advisor vs RAG)",         "#DD8452"),
        (d21, "ΔV2-V1  (Revised vs Advisor)",      "#55A868"),
        (d20, "ΔV2-V0  (Revised vs RAG baseline)", "#8172B2"),
    ]

    for ax, (delta, title, color) in zip(axes, pairs):
        ax.hist(delta, bins=12, color=color, alpha=0.8, edgecolor="white")
        ax.axvline(0,           color="black",  linestyle="--", linewidth=1.2)
        ax.axvline(delta.mean(), color="darkred", linestyle="-",  linewidth=1.5,
                   label=f"μ = {delta.mean():.1f}")
        ax.set_title(title, fontsize=10, fontweight="bold")
        ax.set_xlabel("Score change (pts)", fontsize=9)
        ax.set_ylabel("Count", fontsize=9)
        ax.yaxis.grid(True, linestyle="--", alpha=0.5)
        ax.set_axisbelow(True)
        ax.legend(fontsize=9)

    fig.suptitle("Distribution of Score Deltas Across All Scenarios", fontsize=12, fontweight="bold")
    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Saved: {out_path.name}")


# ---------------------------------------------------------------------------
# Markdown results table
# ---------------------------------------------------------------------------

def build_markdown(overall_results: List[Dict], crit_results: List[Dict]) -> str:
    def _fmt_p(p: float) -> str:
        if p < 0.0001:
            return "< 0.0001"
        return f"{p:.4f}"

    def _row(r):
        if r["p"] is None:
            return (f"| {r['label']:<28} | {r['n']} | {r['mean_x']:>7} → {r['mean_y']:>7}"
                    f" | — | — | — | — | {r['sig']} |")
        return (
            f"| {r['label']:<28} | {r['n']} "
            f"| {r['mean_x']:>7.2f} → {r['mean_y']:>7.2f} "
            f"| {r['W']:>8} "
            f"| {_fmt_p(r['p']):>10} "
            f"| {r['Z']:>7} "
            f"| {r['r']:>6} "
            f"| {r['sig']:>4} |"
        )

    header = (
        "| Comparison                   | N  | Mean (x → y)        "
        "|        W |       p |       Z |      r | Sig  |\n"
        "|:-----------------------------|---:|:--------------------"
        "|---------:|--------:|--------:|-------:|:----:|\n"
    )

    md = "## Wilcoxon Signed-Rank Test Results\n\n"
    md += "> **H₀**: No difference between paired scores across 56 scenarios.\n"
    md += "> Effect size *r* = |Z| / √N_nonzero  "
    md += "(small ≥ 0.1 · medium ≥ 0.3 · large ≥ 0.5)\n\n"
    md += "### Overall Weighted Scores\n\n"
    md += header
    for r in overall_results:
        md += _row(r) + "\n"

    md += "\n### Per-Criterion (V1 Advisor vs V2 Revised, averaged across all scenarios)\n\n"
    md += header
    for r in crit_results:
        md += _row(r) + "\n"

    md += (
        "\n**Significance**: \\*\\*\\* p<0.001 · \\*\\* p<0.01 · \\* p<0.05 · ns = not significant\n"
    )
    return md


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    print("Loading metrics.py files...")
    records = load_all_metrics()

    if not records:
        print("No metrics.py files found. Run run_rag_metrics.py first.")
        return

    n = len(records)
    print(f"Loaded {n} scenarios.\n")

    # --- Extract overall arrays ---
    v0 = np.array([r["metrics"].get("overall_v0", 0.0) for r in records])
    v1 = np.array([r["metrics"].get("overall_v1", 0.0) for r in records])
    v2 = np.array([r["metrics"].get("overall_v2", 0.0) for r in records])

    # --- Overall Wilcoxon tests ---
    print("Running Wilcoxon tests (overall)...")
    res_v0v1 = wilcoxon_pair(v0, v1, "V0 (RAG) vs V1 (Advisor)")
    res_v0v2 = wilcoxon_pair(v0, v2, "V0 (RAG) vs V2 (Revised)")
    res_v1v2 = wilcoxon_pair(v1, v2, "V1 (Advisor) vs V2 (Revised)")
    overall_results = [res_v0v1, res_v0v2, res_v1v2]
    for r in overall_results:
        print(f"  {r['label']}: W={r['W']}, p={r['p']}, r={r['r']}, {r['sig']}")

    # --- Per-criterion Wilcoxon tests (V1 vs V2) ---
    print("\nRunning Wilcoxon tests (per criterion, V1 vs V2)...")
    crit_results = []
    for key, label, _ in CRITERIA_ORDER:
        cx1 = np.array([r["metrics"]["criteria_detail"].get(key, {}).get("v1_score", 0) for r in records], dtype=float)
        cx2 = np.array([r["metrics"]["criteria_detail"].get(key, {}).get("v2_score", 0) for r in records], dtype=float)
        res = wilcoxon_pair(cx1, cx2, f"{label} (V1→V2)")
        crit_results.append(res)
        print(f"  {label}: W={res['W']}, p={res['p']}, r={res['r']}, {res['sig']}")

    # --- Plots ---
    print("\nGenerating plots...")
    plot_boxplot(v0, v1, v2, res_v0v1, res_v0v2, res_v1v2,
                 SCRIPT_DIR / "plot_boxplot.png")
    plot_criteria_bar(records, SCRIPT_DIR / "plot_criteria_bar.png")
    plot_delta_hist(v0, v1, v2, SCRIPT_DIR / "plot_delta_hist.png")

    # --- Markdown ---
    md = build_markdown(overall_results, crit_results)
    out_md = SCRIPT_DIR / "wilcoxon_results.md"
    out_md.write_text(md, encoding="utf-8")
    print(f"  Saved: {out_md.name}")

    print("\nDone. Files written to:", SCRIPT_DIR)


if __name__ == "__main__":
    main()
