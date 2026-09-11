"""
RAG vs Pipeline Metrics -- document_5 / query_6
Query: What were Tesla's capital expenditures and free cash flow in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's capital expenditures and free cash flow in 2022?"

RAG_RESPONSE = "\nIn 2022, Tesla's capital expenditures amounted to $7.16 billion. The cash flows provided by operating activities during the same year were $14.72 billion, which indicates that Tesla generated significant free cash flow, although the exact figure for free cash flow is not explicitly stated in the documents. Free cash flow can be calculated as cash flows from operating activities minus capital expenditures, which would be approximately $7.56 billion ($14.72 billion - $7.16 billion).\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_5/query_6
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |        0 |       70 |       75 |     +70 |      +5 |
| Risk Assessment      |    15% |        0 |       60 |       75 |     +60 |     +15 |
| Actionable Advice    |    15% |        0 |        0 |       60 |      +0 |     +60 |
| Evidence Usage       |    10% |        0 |       90 |       90 |     +90 |      +0 |
| Completeness         |    10% |       50 |      100 |      100 |     +50 |      +0 |
| Query Satisfaction   |    10% |       80 |      100 |      100 |     +20 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    35.50 |    73.50 |    85.50 |   +38.0 |   +12.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +38.0 pts  |  +107.04%
  V2 vs V1: +12.0 pts  |  +16.33%
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
                "v0_score": 0,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 70,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 60,
                "v2_score": 75,
                "delta_v1_v0": 60,
                "delta_v2_v1": 15,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 0,
                "v2_score": 60,
                "delta_v1_v0": 0,
                "delta_v2_v1": 60,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 9.0
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
                "v0_score": 50,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 50,
                "delta_v2_v1": 0,
                "weighted_v0": 5.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 35.5,
        "overall_v1": 73.5,
        "overall_v2": 85.5,
        "v1_vs_v0_abs": 38.0,
        "v1_vs_v0_pct": 107.04,
        "v2_vs_v1_abs": 12.0,
        "v2_vs_v1_pct": 16.33
    }
