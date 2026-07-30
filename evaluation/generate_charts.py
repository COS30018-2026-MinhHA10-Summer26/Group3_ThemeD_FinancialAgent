"""
generate_charts.py

Generates all evaluation charts for Section V of the COS30018 report.
Run this script once to produce the figure files referenced in the report.

Output files (saved to evaluation/figures/):
  fig1_overall_scores.png       - Grouped bar chart: V1 vs V2 overall scores per scenario
  fig2_improvement_pct.png      - Bar chart: % improvement per scenario (highlights regressions)
  fig3_criterion_delta.png      - Horizontal bar chart: per-criterion average delta
  fig4_v2_distribution.png      - Donut/pie chart: V2 score distribution bands
  fig5_v1_v2_scatter.png        - Scatter plot: V1 vs V2 scores with regression line

Usage:
    python evaluation/generate_charts.py
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import MultipleLocator

matplotlib.rcParams.update({
    "font.family": "serif",
    "font.size": 9,
    "axes.titlesize": 10,
    "axes.labelsize": 9,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "figure.dpi": 150,
})

# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------

SCENARIOS = [f"S{i}" for i in range(1, 21)]

OVERALL_V1 = [
    70.50, 28.50, 72.75, 63.00, 70.75, 81.75, 81.50, 73.75, 60.50, 76.25,
    65.00, 72.25, 66.75, 66.00, 51.00, 83.00, 79.00, 58.50, 76.50, 76.00,
]

OVERALL_V2 = [
    85.00, 82.25, 82.75, 81.50, 65.75, 80.00, 82.00, 86.25, 68.50, 86.75,
    83.00, 85.25, 81.75, 78.00, 74.50, 81.75, 76.00, 82.50, 86.25, 79.50,
]

ABS_DELTA   = [v2 - v1 for v1, v2 in zip(OVERALL_V1, OVERALL_V2)]
PCT_DELTA   = [(d / v1) * 100 for d, v1 in zip(ABS_DELTA, OVERALL_V1)]

# Per-criterion averages (V1, V2)
CRITERIA_LABELS = [
    "Financial\nAccuracy",
    "Business\nAnalysis",
    "Risk\nAssessment",
    "Actionable\nAdvice",
    "Evidence\nUsage",
    "Completeness",
    "Query\nSatisfaction",
]
CRITERIA_V1_AVG = [77.0, 64.8, 61.3, 60.8, 59.5, 80.0, 75.3]
CRITERIA_V2_AVG = [84.3, 74.3, 78.8, 73.3, 74.0, 88.5, 84.8]
CRITERIA_DELTA  = [v2 - v1 for v1, v2 in zip(CRITERIA_V1_AVG, CRITERIA_V2_AVG)]

# Colour palette
C_V1      = "#4878CF"   # muted blue
C_V2      = "#6ACC65"   # muted green
C_POS     = "#6ACC65"
C_NEG     = "#D65F5F"
C_ACCENT  = "#EE854A"

# Output directory
OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# Fig 1 — Grouped bar chart: V1 vs V2 overall scores
# ---------------------------------------------------------------------------

def fig1_overall_scores():
    fig, ax = plt.subplots(figsize=(11, 4))
    x = np.arange(len(SCENARIOS))
    w = 0.38

    bars_v1 = ax.bar(x - w / 2, OVERALL_V1, w, color=C_V1, label="V1 (Original)",
                     edgecolor="white", linewidth=0.5)
    bars_v2 = ax.bar(x + w / 2, OVERALL_V2, w, color=C_V2, label="V2 (Revised)",
                     edgecolor="white", linewidth=0.5)

    # Shade regression scenarios
    for idx in [4, 5, 6, 15, 16]:          # 0-indexed: S5,S6,S7,S16,S17
        ax.axvspan(idx - 0.5, idx + 0.5, color=C_NEG, alpha=0.07)

    ax.set_xlabel("Evaluation Scenario")
    ax.set_ylabel("Weighted Score (0–100)")
    ax.set_title("Fig. 1 — Overall Weighted Scores: V1 (Original) vs. V2 (Revised) across 20 Scenarios")
    ax.set_xticks(x)
    ax.set_xticklabels(SCENARIOS, fontsize=7.5)
    ax.set_ylim(0, 105)
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.axhline(sum(OVERALL_V1) / len(OVERALL_V1), color=C_V1, linestyle="--",
               linewidth=0.8, alpha=0.7, label=f"V1 mean ({sum(OVERALL_V1)/len(OVERALL_V1):.1f})")
    ax.axhline(sum(OVERALL_V2) / len(OVERALL_V2), color=C_V2, linestyle="--",
               linewidth=0.8, alpha=0.7, label=f"V2 mean ({sum(OVERALL_V2)/len(OVERALL_V2):.1f})")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.tight_layout()
    path = os.path.join(OUT_DIR, "fig1_overall_scores.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig 2 — Bar chart: % improvement per scenario
# ---------------------------------------------------------------------------

def fig2_improvement_pct():
    fig, ax = plt.subplots(figsize=(11, 4))
    x = np.arange(len(SCENARIOS))
    colors = [C_NEG if d < 0 else (C_ACCENT if d < 5 else C_POS) for d in PCT_DELTA]

    bars = ax.bar(x, PCT_DELTA, color=colors, edgecolor="white", linewidth=0.5)

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axhline(sum(PCT_DELTA) / len(PCT_DELTA), color="#555555", linestyle="--",
               linewidth=0.9, label=f"Mean: +{sum(PCT_DELTA)/len(PCT_DELTA):.1f}%")

    # Annotate each bar with the % value
    for bar, pct in zip(bars, PCT_DELTA):
        y_pos = bar.get_height() + (1.5 if pct >= 0 else -4.5)
        ax.text(bar.get_x() + bar.get_width() / 2, y_pos,
                f"{pct:+.1f}%", ha="center", va="bottom", fontsize=6.5, rotation=90)

    ax.set_xlabel("Evaluation Scenario")
    ax.set_ylabel("Relative Improvement (%)")
    ax.set_title("Fig. 2 — Relative Score Improvement (%) per Scenario (V2 vs. V1)")
    ax.set_xticks(x)
    ax.set_xticklabels(SCENARIOS, fontsize=7.5)
    ax.set_ylim(-25, 225)

    legend_patches = [
        mpatches.Patch(color=C_POS,     label="Improvement ≥ 5%"),
        mpatches.Patch(color=C_ACCENT,  label="Near-zero (0–5%)"),
        mpatches.Patch(color=C_NEG,     label="Regression (< 0%)"),
    ]
    ax.legend(handles=legend_patches, loc="upper right", fontsize=8)
    ax.grid(axis="y", linestyle=":", alpha=0.4)

    fig.tight_layout()
    path = os.path.join(OUT_DIR, "fig2_improvement_pct.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig 3 — Horizontal bar chart: per-criterion average delta
# ---------------------------------------------------------------------------

def fig3_criterion_delta():
    fig, ax = plt.subplots(figsize=(7, 4))
    y = np.arange(len(CRITERIA_LABELS))
    colors = [C_POS if d >= 0 else C_NEG for d in CRITERIA_DELTA]

    bars = ax.barh(y, CRITERIA_DELTA, color=colors, edgecolor="white", linewidth=0.5)
    ax.set_yticks(y)
    ax.set_yticklabels(CRITERIA_LABELS, fontsize=8.5)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("Mean Score Delta (V2 − V1)")
    ax.set_title("Fig. 3 — Per-Criterion Average Score Delta (V2 − V1) across 20 Scenarios")

    for bar, d in zip(bars, CRITERIA_DELTA):
        x_pos = d + 0.3 if d >= 0 else d - 0.3
        ha = "left" if d >= 0 else "right"
        ax.text(x_pos, bar.get_y() + bar.get_height() / 2,
                f"+{d:.1f}" if d >= 0 else f"{d:.1f}",
                va="center", ha=ha, fontsize=8.5, fontweight="bold")

    ax.grid(axis="x", linestyle=":", alpha=0.4)
    ax.set_xlim(-3, 22)
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "fig3_criterion_delta.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig 4 — Donut chart: V2 score distribution bands
# ---------------------------------------------------------------------------

def fig4_v2_distribution():
    bands = {
        "Excellent (≥85)":     sum(1 for s in OVERALL_V2 if s >= 85),
        "Good (75–84)":        sum(1 for s in OVERALL_V2 if 75 <= s < 85),
        "Moderate (65–74)":    sum(1 for s in OVERALL_V2 if 65 <= s < 75),
        "Below target (< 65)": sum(1 for s in OVERALL_V2 if s < 65),
    }
    labels = list(bands.keys())
    sizes  = list(bands.values())
    colors = ["#6ACC65", "#4878CF", "#EE854A", "#D65F5F"]

    fig, ax = plt.subplots(figsize=(6, 5))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=None,
        autopct="%1.0f%%",
        startangle=90,
        colors=colors,
        pctdistance=0.72,
        wedgeprops=dict(width=0.55, edgecolor="white", linewidth=1.5),
    )
    for at in autotexts:
        at.set_fontsize(10)
        at.set_fontweight("bold")

    ax.legend(
        wedges,
        [f"{l} (n={s})" for l, s in zip(labels, sizes)],
        loc="lower center",
        bbox_to_anchor=(0.5, -0.12),
        fontsize=8.5,
        ncol=2,
    )
    ax.set_title("Fig. 4 — Distribution of V2 Scores across 20 Scenarios")
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "fig4_v2_distribution.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig 5 — Scatter plot: V1 vs V2 with regression line
# ---------------------------------------------------------------------------

def fig5_v1_v2_scatter():
    v1 = np.array(OVERALL_V1)
    v2 = np.array(OVERALL_V2)

    fig, ax = plt.subplots(figsize=(6, 5.5))

    # Regression line
    m, b = np.polyfit(v1, v2, 1)
    x_line = np.linspace(v1.min() - 5, v1.max() + 5, 200)
    ax.plot(x_line, m * x_line + b, color="#888888", linewidth=1.0,
            linestyle="--", label=f"Regression (y={m:.2f}x+{b:.1f})")

    # y = x line (no change baseline)
    ax.plot(x_line, x_line, color="black", linewidth=0.7, linestyle=":",
            label="y = x (no change)")

    # Scatter points
    special = {4, 5, 6, 15, 16}     # 0-indexed
    for i, (x, y) in enumerate(zip(v1, v2)):
        color = C_NEG if i in special else (C_ACCENT if abs(y - x) < 2 else C_V2)
        ax.scatter(x, y, color=color, s=55, zorder=4, edgecolors="white", linewidths=0.4)
        ax.annotate(
            SCENARIOS[i], (x, y),
            textcoords="offset points", xytext=(5, 4),
            fontsize=6.5, color="dimgray",
        )

    legend_patches = [
        mpatches.Patch(color=C_V2,    label="Normal improvement"),
        mpatches.Patch(color=C_ACCENT, label="Near-zero improvement"),
        mpatches.Patch(color=C_NEG,   label="Regression"),
    ]
    handles, _ = ax.get_legend_handles_labels()
    ax.legend(handles=handles + legend_patches, fontsize=7.5, loc="upper left")

    ax.set_xlabel("V1 Score (Original Report)")
    ax.set_ylabel("V2 Score (Revised Report)")
    ax.set_title("Fig. 5 — V1 vs. V2 Score Scatter Plot with Regression Fit")
    ax.grid(linestyle=":", alpha=0.4)
    ax.set_xlim(20, 95)
    ax.set_ylim(55, 100)
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "fig5_v1_v2_scatter.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    fig1_overall_scores()
    fig2_improvement_pct()
    fig3_criterion_delta()
    fig4_v2_distribution()
    fig5_v1_v2_scatter()
    print("\nAll figures saved to:", OUT_DIR)
