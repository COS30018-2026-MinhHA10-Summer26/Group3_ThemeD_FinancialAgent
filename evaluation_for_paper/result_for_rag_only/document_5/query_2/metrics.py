"""
RAG vs Pipeline Metrics -- document_5 / query_2
Query: How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?
"""
from __future__ import annotations
import json

USER_QUERY = "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?"

RAG_RESPONSE = "\nIn 2022, Tesla delivered a total of 1,313,851 vehicles. This represented an increase of 385,000 vehicles compared to 2021, when Tesla delivered 928,000 vehicles.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_5/query_2
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |      100 |      100 |      100 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |        0 |       50 |      +0 |     +50 |
| Risk Assessment      |    15% |       20 |       50 |       70 |     +30 |     +20 |
| Actionable Advice    |    15% |        0 |       90 |       90 |     +90 |      +0 |
| Evidence Usage       |    10% |       30 |       80 |       80 |     +50 |      +0 |
| Completeness         |    10% |        0 |       50 |       70 |     +50 |     +20 |
| Query Satisfaction   |    10% |       30 |       80 |      100 |     +50 |     +20 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    34.00 |    67.00 |    81.50 |   +33.0 |   +14.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +33.0 pts  |  +97.06%
  V2 vs V1: +14.5 pts  |  +21.64%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 100,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 25.0,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v1_v0": 0,
                "delta_v2_v1": 50,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 20,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 30,
                "delta_v2_v1": 20,
                "weighted_v0": 3.0,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 90,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 13.5,
                "weighted_v2": 13.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 30,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 50,
                "delta_v2_v1": 0,
                "weighted_v0": 3.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 50,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 5.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 30,
                "v1_score": 80,
                "v2_score": 100,
                "delta_v1_v0": 50,
                "delta_v2_v1": 20,
                "weighted_v0": 3.0,
                "weighted_v1": 8.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 34.0,
        "overall_v1": 67.0,
        "overall_v2": 81.5,
        "v1_vs_v0_abs": 33.0,
        "v1_vs_v0_pct": 97.06,
        "v2_vs_v1_abs": 14.5,
        "v2_vs_v1_pct": 21.64
    }
