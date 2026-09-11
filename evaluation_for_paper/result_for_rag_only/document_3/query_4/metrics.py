"""
RAG vs Pipeline Metrics -- document_3 / query_4
Query: How did Amazon's subscription services revenue evolve in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's subscription services revenue evolve in 2024?"

RAG_RESPONSE = "\nIn 2024, Amazon's subscription services revenue, which includes fees associated with Amazon Prime memberships, increased to $44.4 billion, up from $40.2 billion in 2023. This represents a year-over-year growth of approximately 10.5%. The growth in subscription services revenue was driven by increased unit sales, including sales by third-party sellers, advertising sales, and the continued popularity of Amazon Prime.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_4
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       60 |       70 |       80 |     +10 |     +10 |
| Risk Assessment      |    15% |       50 |       60 |       60 |     +10 |      +0 |
| Actionable Advice    |    15% |       40 |       50 |       70 |     +10 |     +20 |
| Evidence Usage       |    10% |       30 |       55 |       70 |     +25 |     +15 |
| Completeness         |    10% |       70 |       80 |       80 |     +10 |      +0 |
| Query Satisfaction   |    10% |       80 |       80 |       90 |      +0 |     +10 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    63.00 |    71.00 |    78.00 |    +8.0 |    +7.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +8.0 pts  |  +12.70%
  V2 vs V1: +7.0 pts  |  +9.86%
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
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 9.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 10,
                "delta_v2_v1": 20,
                "weighted_v0": 6.0,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 30,
                "v1_score": 55,
                "v2_score": 70,
                "delta_v1_v0": 25,
                "delta_v2_v1": 15,
                "weighted_v0": 3.0,
                "weighted_v1": 5.5,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 80,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 8.0,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 63.0,
        "overall_v1": 71.0,
        "overall_v2": 78.0,
        "v1_vs_v0_abs": 8.0,
        "v1_vs_v0_pct": 12.7,
        "v2_vs_v1_abs": 7.0,
        "v2_vs_v1_pct": 9.86
    }
