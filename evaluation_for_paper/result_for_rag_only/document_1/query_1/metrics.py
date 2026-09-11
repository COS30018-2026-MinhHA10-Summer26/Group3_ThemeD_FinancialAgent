"""
RAG vs Pipeline Metrics -- document_1 / query_1
Query: What were Amazon's total net sales and net income for fiscal year 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's total net sales and net income for fiscal year 2022?"

RAG_RESPONSE = "\nFor the fiscal year 2022, Amazon's total net sales were $513.98 billion, and the net income was a loss of $2.72 billion.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_1
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |      100 |      100 |      100 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       30 |       50 |     +30 |     +20 |
| Risk Assessment      |    15% |        0 |       20 |       50 |     +20 |     +30 |
| Actionable Advice    |    15% |        0 |       60 |       80 |     +60 |     +20 |
| Evidence Usage       |    10% |        0 |        0 |       50 |      +0 |     +50 |
| Completeness         |    10% |       20 |       50 |       70 |     +30 |     +20 |
| Query Satisfaction   |    10% |      100 |      100 |      100 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    37.00 |    56.50 |    74.00 |   +19.5 |   +17.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +19.5 pts  |  +52.70%
  V2 vs V1: +17.5 pts  |  +30.97%
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
                "v1_score": 30,
                "v2_score": 50,
                "delta_v1_v0": 30,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 4.5,
                "weighted_v2": 7.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 20,
                "v2_score": 50,
                "delta_v1_v0": 20,
                "delta_v2_v1": 30,
                "weighted_v0": 0.0,
                "weighted_v1": 3.0,
                "weighted_v2": 7.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
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
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v1_v0": 0,
                "delta_v2_v1": 50,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 5.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 20,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 30,
                "delta_v2_v1": 20,
                "weighted_v0": 2.0,
                "weighted_v1": 5.0,
                "weighted_v2": 7.0
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
        "overall_v1": 56.5,
        "overall_v2": 74.0,
        "v1_vs_v0_abs": 19.5,
        "v1_vs_v0_pct": 52.7,
        "v2_vs_v1_abs": 17.5,
        "v2_vs_v1_pct": 30.97
    }
