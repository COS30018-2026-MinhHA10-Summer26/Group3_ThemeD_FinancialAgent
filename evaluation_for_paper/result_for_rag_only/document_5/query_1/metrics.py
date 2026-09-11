"""
RAG vs Pipeline Metrics -- document_5 / query_1
Query: What were Tesla's total revenues and net income for fiscal year 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's total revenues and net income for fiscal year 2022?"

RAG_RESPONSE = "\nFor the fiscal year 2022, Tesla's total revenues were $81.46 billion, and the net income attributable to common stockholders was $12.56 billion.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_5/query_1
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |      100 |      100 |      100 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       70 |       75 |     +70 |      +5 |
| Risk Assessment      |    15% |        0 |       70 |       80 |     +70 |     +10 |
| Actionable Advice    |    15% |        0 |       70 |       75 |     +70 |      +5 |
| Evidence Usage       |    10% |        0 |       80 |       85 |     +80 |      +5 |
| Completeness         |    10% |       20 |      100 |      100 |     +80 |      +0 |
| Query Satisfaction   |    10% |      100 |      100 |      100 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    37.00 |    84.50 |    88.00 |   +47.5 |    +3.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +47.5 pts  |  +128.38%
  V2 vs V1: +3.5 pts  |  +4.14%
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
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 70,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
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
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 80,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
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
        "overall_v1": 84.5,
        "overall_v2": 88.0,
        "v1_vs_v0_abs": 47.5,
        "v1_vs_v0_pct": 128.38,
        "v2_vs_v1_abs": 3.5,
        "v2_vs_v1_pct": 4.14
    }
