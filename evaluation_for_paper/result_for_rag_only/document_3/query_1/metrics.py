"""
RAG vs Pipeline Metrics -- document_3 / query_1
Query: What were Amazon's total net sales and earnings per share for fiscal year 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's total net sales and earnings per share for fiscal year 2024?"

RAG_RESPONSE = "\nFor fiscal year 2024, Amazon's total net sales were $638 billion, and the earnings per share (EPS) were $5.66.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_1
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |      100 |      100 |      100 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       30 |       60 |     +30 |     +30 |
| Risk Assessment      |    15% |        0 |       20 |       70 |     +20 |     +50 |
| Actionable Advice    |    15% |        0 |       35 |       80 |     +35 |     +45 |
| Evidence Usage       |    10% |        0 |        0 |       80 |      +0 |     +80 |
| Completeness         |    10% |       20 |       40 |       85 |     +20 |     +45 |
| Query Satisfaction   |    10% |      100 |      100 |      100 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    37.00 |    51.75 |    83.00 |  +14.75 |  +31.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +14.75 pts  |  +39.86%
  V2 vs V1: +31.25 pts  |  +60.39%
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
                "v2_score": 60,
                "delta_v1_v0": 30,
                "delta_v2_v1": 30,
                "weighted_v0": 0.0,
                "weighted_v1": 4.5,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 20,
                "v2_score": 70,
                "delta_v1_v0": 20,
                "delta_v2_v1": 50,
                "weighted_v0": 0.0,
                "weighted_v1": 3.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 35,
                "v2_score": 80,
                "delta_v1_v0": 35,
                "delta_v2_v1": 45,
                "weighted_v0": 0.0,
                "weighted_v1": 5.25,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 80,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 20,
                "v1_score": 40,
                "v2_score": 85,
                "delta_v1_v0": 20,
                "delta_v2_v1": 45,
                "weighted_v0": 2.0,
                "weighted_v1": 4.0,
                "weighted_v2": 8.5
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
        "overall_v1": 51.75,
        "overall_v2": 83.0,
        "v1_vs_v0_abs": 14.75,
        "v1_vs_v0_pct": 39.86,
        "v2_vs_v1_abs": 31.25,
        "v2_vs_v1_pct": 60.39
    }
