"""
RAG vs Pipeline Metrics -- document_2 / query_1
Query: What were Amazon's total revenues and operating income for fiscal year 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's total revenues and operating income for fiscal year 2023?"

RAG_RESPONSE = "\nFor fiscal year 2023, Amazon's total revenues were $575 billion, and its operating income was $36.9 billion.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_2/query_1
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |      100 |      100 |      100 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       70 |       80 |     +70 |     +10 |
| Risk Assessment      |    15% |        0 |       60 |       80 |     +60 |     +20 |
| Actionable Advice    |    15% |        0 |       70 |       80 |     +70 |     +10 |
| Evidence Usage       |    10% |        0 |       90 |       90 |     +90 |      +0 |
| Completeness         |    10% |       20 |      100 |      100 |     +80 |      +0 |
| Query Satisfaction   |    10% |      100 |      100 |      100 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    37.00 |    84.00 |    90.00 |   +47.0 |    +6.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +47.0 pts  |  +127.03%
  V2 vs V1: +6.0 pts  |  +7.14%
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
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 70,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v1_v0": 60,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 70,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 90,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 20,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 80,
                "delta_v2_v1": 0,
                "weighted_v0": 2.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 10.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 37.0,
        "overall_v1": 84.0,
        "overall_v2": 90.0,
        "v1_vs_v0_abs": 47.0,
        "v1_vs_v0_pct": 127.03,
        "v2_vs_v1_abs": 6.0,
        "v2_vs_v1_pct": 7.14
    }
