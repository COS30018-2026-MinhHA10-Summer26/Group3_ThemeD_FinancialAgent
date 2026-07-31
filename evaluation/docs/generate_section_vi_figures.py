"""
generate_section_vi_figures.py

Generates all figures used in Section VI — Scenarios and Examples
of the COS30018 Financial Agent report.

Output files (saved to evaluation/docs/figures/):
  s6_pipeline_flow.png        — End-to-end pipeline walkthrough diagram
  s6_scenario_comparison.png  — V1 vs V2 score bar chart for four featured scenarios
  s6_step_scores.png          — Stacked quality breakdown across pipeline steps
  s6_query_taxonomy.png       — Donut chart of the 20-scenario query taxonomy
  s6_criterion_radar.png      — Radar chart comparing V1/V2 for S2 (large improvement)

Usage:
    python evaluation/docs/generate_section_vi_figures.py
"""

import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
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

OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# Colour palette (consistent with evaluation figures)
C_PLANNER   = "#4878CF"
C_ADVISOR   = "#6ACC65"
C_CRITIC    = "#D65F5F"
C_EVALUATOR = "#EE854A"
C_SEARCH    = "#956CB4"
C_ARROW     = "#555555"
C_V1        = "#4878CF"
C_V2        = "#6ACC65"
C_NEG       = "#D65F5F"
C_ACCENT    = "#EE854A"


# ---------------------------------------------------------------------------
# Fig S6-1 — Pipeline flow walkthrough (horizontal agent boxes + arrows)
# ---------------------------------------------------------------------------

def fig_pipeline_flow():
    fig, ax = plt.subplots(figsize=(12, 3.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3)
    ax.axis("off")

    # Agent definitions: (x_center, label, sublabel, color)
    agents = [
        (1.0,  "User\nQuery",    "",                       "#BBBBBB"),
        (2.9,  "Planner\nAgent", "Route & Plan",           C_PLANNER),
        (4.8,  "Search\nAgent",  "Web + RAG\nRetrieval",   C_SEARCH),
        (6.7,  "Advisor\nAgent", "Draft Report\n(V1)",     C_ADVISOR),
        (8.6,  "Critic\nAgent",  "Audit &\nFeedback",      C_CRITIC),
        (10.5, "Advisor\nAgent", "Revised Report\n(V2)",   C_ADVISOR),
    ]

    box_w, box_h = 1.55, 1.10
    y_center = 1.5

    for x, label, sublabel, color in agents:
        bbox = FancyBboxPatch(
            (x - box_w / 2, y_center - box_h / 2),
            box_w, box_h,
            boxstyle="round,pad=0.08",
            facecolor=color, edgecolor="white", linewidth=1.5, alpha=0.92,
        )
        ax.add_patch(bbox)
        ax.text(x, y_center + 0.18, label, ha="center", va="center",
                fontsize=8.5, fontweight="bold", color="white",
                path_effects=[pe.withStroke(linewidth=1, foreground=color)])
        if sublabel:
            ax.text(x, y_center - 0.28, sublabel, ha="center", va="center",
                    fontsize=6.8, color="white", alpha=0.90)

    # Arrows between agents
    arrow_pairs = [(1.0, 2.9), (2.9, 4.8), (4.8, 6.7), (6.7, 8.6), (8.6, 10.5)]
    for x_src, x_dst in arrow_pairs:
        ax.annotate(
            "", xy=(x_dst - box_w / 2 - 0.04, y_center),
            xytext=(x_src + box_w / 2 + 0.04, y_center),
            arrowprops=dict(arrowstyle="-|>", color=C_ARROW,
                            lw=1.5, mutation_scale=14),
        )

    # Self-review loop arrow under Advisor V2
    ax.annotate(
        "", xy=(10.5 - 0.35, y_center - box_h / 2 - 0.02),
        xytext=(10.5 + 0.35, y_center - box_h / 2 - 0.02),
        arrowprops=dict(
            arrowstyle="<|-", color=C_ADVISOR,
            lw=1.2, mutation_scale=11,
            connectionstyle="arc3,rad=-0.7",
        ),
    )
    ax.text(10.5, y_center - box_h / 2 - 0.55,
            "self-review\nloop (≤2×)", ha="center", va="center",
            fontsize=6.5, color=C_ADVISOR, style="italic")

    # Evaluator box below the pipeline
    eval_x, eval_y = 6.7, 0.38
    eval_bbox = FancyBboxPatch(
        (eval_x - 1.2, eval_y - 0.30), 2.4, 0.60,
        boxstyle="round,pad=0.06",
        facecolor=C_EVALUATOR, edgecolor="white", linewidth=1.2, alpha=0.92,
    )
    ax.add_patch(eval_bbox)
    ax.text(eval_x, eval_y, "Evaluator Agent — Final Quality Gate",
            ha="center", va="center", fontsize=8, fontweight="bold", color="white")

    # Arrow from Advisor V2 down to Evaluator
    ax.annotate(
        "", xy=(eval_x + 1.2 + 0.04, eval_y),
        xytext=(10.5, y_center - box_h / 2 - 0.04),
        arrowprops=dict(arrowstyle="-|>", color=C_ARROW,
                        lw=1.2, mutation_scale=12,
                        connectionstyle="arc3,rad=0.3"),
    )

    # Output label
    ax.text(11.7, y_center, "Final\nAnswer /\nReport",
            ha="center", va="center", fontsize=7.5, color="#333333",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="#EEEEEE",
                      edgecolor="#AAAAAA", linewidth=1))
    ax.annotate(
        "", xy=(11.7 - 0.28, y_center),
        xytext=(10.5 + box_w / 2 + 0.04, y_center),
        arrowprops=dict(arrowstyle="-|>", color=C_ARROW,
                        lw=1.5, mutation_scale=14),
    )

    ax.set_title("Fig. S6-1 — End-to-End Pipeline Flow: from User Query to Final Report",
                 pad=8)
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "s6_pipeline_flow.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig S6-2 — V1 vs V2 for four featured scenarios
# ---------------------------------------------------------------------------

def fig_scenario_comparison():
    """
    V1 vs V2 bar chart for the four featured scenarios.

    Colour convention (matches every other chart in the report):
      Blue  (C_V1) = V1 (original) bars  — always uniform
      Green (C_V2) = V2 (revised)  bars  — always uniform

    Regression scenarios (V2 < V1) are NOT signalled by changing the bar
    colour.  Instead, a very light-red background band is drawn behind the
    column (same approach used in fig1_overall_scores.png) and the delta
    annotation text above the V2 bar is coloured red.
    """
    scenarios = ["S2\n(Fabricated\nFigures)", "S5\n(Partial-Fix\nRegression)",
                 "S15\n(Missing\nMetrics)", "S16\n(Ceiling\nEffect)"]
    v1 = [28.50, 70.75, 51.00, 83.00]
    v2 = [82.25, 65.75, 74.50, 81.75]

    # Indices (0-based) where V2 < V1
    regression_idx = [i for i, (a, b) in enumerate(zip(v1, v2)) if b < a]

    x = np.arange(len(scenarios))
    w = 0.36

    fig, ax = plt.subplots(figsize=(8, 4.2))

    # Both bar groups use their canonical, uniform colours — no per-bar overrides
    ax.bar(x - w / 2, v1, w, color=C_V1, label="V1 (Original)", edgecolor="white")
    ax.bar(x + w / 2, v2, w, color=C_V2, label="V2 (Revised)",  edgecolor="white")

    # Light-red background shading behind regression columns (alpha very low)
    for idx in regression_idx:
        ax.axvspan(idx - 0.5, idx + 0.5, color=C_NEG, alpha=0.09, zorder=0)

    # Delta annotations above each V2 bar:
    #   green text for improvements, red text for regressions
    for i, (a, b) in enumerate(zip(v1, v2)):
        d = b - a
        sign = "+" if d >= 0 else ""
        ann_color = C_V2 if d >= 0 else C_NEG
        ax.text(x[i] + w / 2, b + 1.2, f"{sign}{d:.2f}",
                ha="center", va="bottom", fontsize=7.5,
                color=ann_color, fontweight="bold")

    # Small italic "regression" label inside each shaded band
    for idx in regression_idx:
        ax.text(idx, 3.5, "regression", ha="center", va="bottom",
                fontsize=6.5, color=C_NEG, style="italic", alpha=0.75)

    ax.set_ylabel("Weighted Score (0–100)")
    ax.set_title("Fig. S6-2 — V1 vs. V2 Scores for Four Featured Scenarios")
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, fontsize=8.5)
    ax.set_ylim(0, 105)
    ax.yaxis.set_minor_locator(MultipleLocator(5))
    ax.legend(loc="lower right", fontsize=8.5)
    ax.grid(axis="y", linestyle=":", alpha=0.4)
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "s6_scenario_comparison.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig S6-3 — Per-criterion breakdown for S2 and S15 (V1 vs V2)
# ---------------------------------------------------------------------------

def fig_criterion_breakdown():
    criteria = ["Financial\nAccuracy", "Business\nAnalysis", "Risk\nAssessment",
                "Actionable\nAdvice", "Evidence\nUsage", "Completeness",
                "Query\nSatisfaction"]

    # S2: large improvement — fabricated figures corrected
    s2_v1 = [10, 30, 35, 30, 25, 40, 35]
    s2_v2 = [80, 80, 85, 85, 80, 85, 85]

    # S15: missing metrics corrected
    s15_v1 = [55, 55, 50, 60, 45, 65, 60]
    s15_v2 = [75, 75, 80, 80, 75, 80, 75]

    x = np.arange(len(criteria))
    w = 0.20

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.2), sharey=True)

    for ax, label, v1_data, v2_data, color_v2 in [
        (axes[0], "S2 — Fabricated Figures Corrected (+53.75 pts)", s2_v1, s2_v2, C_V2),
        (axes[1], "S15 — Missing Metrics Added (+23.50 pts)", s15_v1, s15_v2, C_V2),
    ]:
        b1 = ax.bar(x - w / 2, v1_data, w, color=C_V1, label="V1", edgecolor="white")
        b2 = ax.bar(x + w / 2, v2_data, w, color=color_v2, label="V2", edgecolor="white")
        ax.set_title(label, fontsize=8.5)
        ax.set_xticks(x)
        ax.set_xticklabels(criteria, fontsize=7.2)
        ax.set_ylim(0, 105)
        ax.yaxis.set_minor_locator(MultipleLocator(10))
        ax.grid(axis="y", linestyle=":", alpha=0.4)
        ax.legend(fontsize=8)
        ax.set_ylabel("Score (0–100)")

    fig.suptitle("Fig. S6-3 — Per-Criterion Score Breakdown (V1 vs. V2) for S2 and S15",
                 fontsize=10, y=1.01)
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "s6_criterion_breakdown.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig S6-4 — 20-scenario query taxonomy donut chart
# ---------------------------------------------------------------------------

def fig_query_taxonomy():
    categories = {
        "Financial Health\n& Risk Assessment": 8,
        "Future Outlook\n& Strategy":          5,
        "Metric Comparison\n& Chart Request":  4,
        "Specific Risk\nFactor Analysis":       3,
    }
    labels = list(categories.keys())
    sizes  = list(categories.values())
    colors = [C_V1, C_V2, C_ACCENT, C_CRITIC]

    fig, ax = plt.subplots(figsize=(6, 5))
    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=None,
        autopct=lambda p: f"{p:.0f}%\n(n={int(round(p*sum(sizes)/100))})",
        startangle=90,
        colors=colors,
        pctdistance=0.72,
        wedgeprops=dict(width=0.55, edgecolor="white", linewidth=1.5),
    )
    for at in autotexts:
        at.set_fontsize(8.5)
        at.set_fontweight("bold")

    ax.legend(wedges, labels, loc="lower center",
              bbox_to_anchor=(0.5, -0.18), fontsize=8, ncol=2)
    ax.set_title("Fig. S6-4 — Query Taxonomy across 20 Evaluation Scenarios")
    fig.tight_layout()
    path = os.path.join(OUT_DIR, "s6_query_taxonomy.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Fig S6-5 — Pipeline execution trace timeline for one request
# ---------------------------------------------------------------------------

def fig_execution_trace():
    """
    Horizontal Gantt-style timeline showing relative latency of each pipeline step
    for a representative full-pipeline request (S1 walkthrough).
    """
    steps = [
        ("Planner Agent\n(Query routing)",        0.0,  2.5,  C_PLANNER),
        ("Search + RAG\nRetrieval",               2.5,  7.0,  C_SEARCH),
        ("Advisor Draft\n(V1 generation)",        7.0, 20.0,  C_ADVISOR),
        ("Advisor Self-Review\n(≤2 loops)",      20.0, 25.0,  C_ADVISOR),
        ("Critic Audit\n(4 tools + quality check)", 25.0, 38.0, C_CRITIC),
        ("Advisor Revision\n(V2 generation)",    38.0, 52.0,  C_ADVISOR),
        ("Evaluator\n(3 tools + quality check)", 52.0, 62.0,  C_EVALUATOR),
    ]

    fig, ax = plt.subplots(figsize=(11, 3.8))
    ax.set_xlim(-2, 75)
    ax.set_ylim(-0.5, len(steps) - 0.5)
    ax.set_xlabel("Relative Time (seconds, representative estimate)")
    ax.set_title("Fig. S6-5 — Execution Timeline for a Single Full-Pipeline Request")
    ax.invert_yaxis()
    ax.set_yticks(range(len(steps)))
    ax.set_yticklabels([s[0] for s in steps], fontsize=8.2)
    ax.grid(axis="x", linestyle=":", alpha=0.35)

    for i, (label, t_start, t_end, color) in enumerate(steps):
        duration = t_end - t_start
        ax.barh(i, duration, left=t_start, height=0.55,
                color=color, edgecolor="white", linewidth=0.8, alpha=0.88)
        ax.text(t_start + duration / 2, i,
                f"{duration:.0f}s", ha="center", va="center",
                fontsize=7.5, fontweight="bold", color="white")

    # Total duration marker
    ax.axvline(62, color="#333333", linestyle="--", linewidth=0.9, alpha=0.7)
    ax.text(62.5, -0.3, "≈62s total", fontsize=7.5, color="#333333", va="top")

    fig.tight_layout()
    path = os.path.join(OUT_DIR, "s6_execution_trace.png")
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    fig_pipeline_flow()
    fig_scenario_comparison()
    fig_criterion_breakdown()
    fig_query_taxonomy()
    fig_execution_trace()
    print(f"\nAll Section VI figures saved to: {OUT_DIR}")
