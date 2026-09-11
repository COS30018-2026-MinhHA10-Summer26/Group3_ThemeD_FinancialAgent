"""
RAG vs Pipeline Metrics -- document_1 / query_4
Query: What is Amazon's free cash flow position and how did it change in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What is Amazon's free cash flow position and how did it change in 2022?"

RAG_RESPONSE = "\nAmazon's free cash flow position in 2022 was negative, amounting to **$(11,569) million**. This represents a decline from the previous year, where the free cash flow was **$(9,069) million** in 2021. The change in free cash flow from 2021 to 2022 indicates a worsening position, primarily driven by increased capital expenditures, which rose from **$55,396 million** in 2021 to **$58,321 million** in 2022. Despite a slight increase in cash provided by operating activities, the higher investments led to a larger negative free cash flow in 2022.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_4
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       50 |       60 |     +50 |     +10 |
| Risk Assessment      |    15% |        0 |       60 |       65 |     +60 |      +5 |
| Actionable Advice    |    15% |        0 |       70 |       75 |     +70 |      +5 |
| Evidence Usage       |    10% |       70 |       80 |       80 |     +10 |      +0 |
| Completeness         |    10% |       50 |       70 |       85 |     +20 |     +15 |
| Query Satisfaction   |    10% |      100 |      100 |      100 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    44.50 |    74.50 |    79.00 |   +30.0 |    +4.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +30.0 pts  |  +67.42%
  V2 vs V1: +4.5 pts  |  +6.04%
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
                "v0_score": 0,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 50,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 60,
                "v2_score": 65,
                "delta_v1_v0": 60,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.75
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
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 70,
                "v2_score": 85,
                "delta_v1_v0": 20,
                "delta_v2_v1": 15,
                "weighted_v0": 5.0,
                "weighted_v1": 7.0,
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
        "overall_v0": 44.5,
        "overall_v1": 74.5,
        "overall_v2": 79.0,
        "v1_vs_v0_abs": 30.0,
        "v1_vs_v0_pct": 67.42,
        "v2_vs_v1_abs": 4.5,
        "v2_vs_v1_pct": 6.04
    }
