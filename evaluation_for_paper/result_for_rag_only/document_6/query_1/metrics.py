"""
RAG vs Pipeline Metrics -- document_6 / query_1
Query: What were Tesla's total revenues and operating income for fiscal year 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's total revenues and operating income for fiscal year 2023?"

RAG_RESPONSE = "\nFor the fiscal year 2023, Tesla's total revenues were $96.77 billion, and the operating income was $17.66 billion.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_6/query_1
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |      100 |      100 |      100 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       60 |       60 |     +60 |      +0 |
| Risk Assessment      |    15% |        0 |       70 |       70 |     +70 |      +0 |
| Actionable Advice    |    15% |        0 |       70 |       70 |     +70 |      +0 |
| Evidence Usage       |    10% |        0 |       70 |       90 |     +70 |     +20 |
| Completeness         |    10% |       20 |      100 |      100 |     +80 |      +0 |
| Query Satisfaction   |    10% |       40 |       90 |       90 |     +50 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    31.00 |    81.00 |    83.00 |   +50.0 |    +2.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +50.0 pts  |  +161.29%
  V2 vs V1: +2.0 pts  |  +2.47%
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
                "v1_score": 60,
                "v2_score": 60,
                "delta_v1_v0": 60,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 70,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 70,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 70,
                "v2_score": 90,
                "delta_v1_v0": 70,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 7.0,
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
                "v0_score": 40,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 50,
                "delta_v2_v1": 0,
                "weighted_v0": 4.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 31.0,
        "overall_v1": 81.0,
        "overall_v2": 83.0,
        "v1_vs_v0_abs": 50.0,
        "v1_vs_v0_pct": 161.29,
        "v2_vs_v1_abs": 2.0,
        "v2_vs_v1_pct": 2.47
    }
