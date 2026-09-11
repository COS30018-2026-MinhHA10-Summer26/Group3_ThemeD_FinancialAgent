"""
RAG vs Pipeline Metrics -- document_3 / query_2
Query: How did AWS perform in 2024 and what was its contribution to operating profit?
"""
from __future__ import annotations
import json

USER_QUERY = "How did AWS perform in 2024 and what was its contribution to operating profit?"

RAG_RESPONSE = "\nIn 2024, AWS (Amazon Web Services) performed strongly, with revenue increasing by 19% year-over-year, rising from $91 billion in 2023 to $108 billion in 2024. This growth was attributed to increased customer usage and the launch of new services, despite some pricing changes due to long-term customer contracts.\n\nAWS made a significant contribution to Amazon's overall operating profit, with its operating income reaching $39.8 billion in 2024, compared to $24.6 billion in 2023. This increase in operating income was primarily driven by higher sales, reduced payroll and related expenses, and a decrease in depreciation and amortization expenses. Overall, Amazon's consolidated operating income for 2024 was $68.6 billion, indicating that AWS was a major contributor to the company's profitability.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_2
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       50 |       50 |       50 |      +0 |      +0 |
| Actionable Advice    |    15% |       40 |       60 |       60 |     +20 |      +0 |
| Evidence Usage       |    10% |       60 |       80 |       80 |     +20 |      +0 |
| Completeness         |    10% |       80 |       90 |       90 |     +10 |      +0 |
| Query Satisfaction   |    10% |       90 |       85 |       85 |      -5 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    69.50 |    75.00 |    75.00 |    +5.5 |    +0.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +5.5 pts  |  +7.91%
  V2 vs V1: +0.0 pts  |  +0.00%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 90,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 22.5,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 85,
                "v2_score": 85,
                "delta_v1_v0": -5,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 8.5,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 69.5,
        "overall_v1": 75.0,
        "overall_v2": 75.0,
        "v1_vs_v0_abs": 5.5,
        "v1_vs_v0_pct": 7.91,
        "v2_vs_v1_abs": 0.0,
        "v2_vs_v1_pct": 0.0
    }
