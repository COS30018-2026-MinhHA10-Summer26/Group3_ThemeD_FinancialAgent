"""
RAG vs Pipeline Metrics -- document_3 / query_6
Query: How did Amazon's international operations perform in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's international operations perform in 2024?"

RAG_RESPONSE = "\nIn 2024, Amazon's international operations performed well, with revenue growth of 9% year-over-year, increasing from $131 billion in 2023 to $143 billion in 2024. This growth was primarily driven by increased unit sales, including sales by third-party sellers, advertising sales, and subscription services. However, it is important to note that changes in foreign exchange rates negatively impacted international net sales by approximately $1.8 billion during the year. Overall, the international segment showed a significant improvement, achieving an operating income of $3.8 billion in 2024, compared to an operating loss of $2.7 billion in the previous year.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_6
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       80 |     +10 |      +0 |
| Risk Assessment      |    15% |       60 |       70 |       85 |     +10 |     +15 |
| Actionable Advice    |    15% |       50 |       75 |       75 |     +25 |      +0 |
| Evidence Usage       |    10% |       70 |       90 |       90 |     +20 |      +0 |
| Completeness         |    10% |       80 |      100 |      100 |     +20 |      +0 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    73.50 |    87.75 |    90.00 |  +14.25 |   +2.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +14.25 pts  |  +19.39%
  V2 vs V1: +2.25 pts  |  +2.56%
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 22.5,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 85,
                "delta_v1_v0": 10,
                "delta_v2_v1": 15,
                "weighted_v0": 9.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 75,
                "v2_score": 75,
                "delta_v1_v0": 25,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 11.25,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 73.5,
        "overall_v1": 87.75,
        "overall_v2": 90.0,
        "v1_vs_v0_abs": 14.25,
        "v1_vs_v0_pct": 19.39,
        "v2_vs_v1_abs": 2.25,
        "v2_vs_v1_pct": 2.56
    }
