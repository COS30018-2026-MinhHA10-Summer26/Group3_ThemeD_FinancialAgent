"""
RAG vs Pipeline Metrics -- document_2 / query_2
Query: How did AWS revenue growth trend in 2023 and what drove it?
"""
from __future__ import annotations
import json

USER_QUERY = "How did AWS revenue growth trend in 2023 and what drove it?"

RAG_RESPONSE = "\nIn 2023, AWS (Amazon Web Services) revenue grew by 13% year-over-year, increasing from $80 billion to $91 billion. This growth was primarily driven by increased customer usage, although it was partially offset by pricing changes associated with long-term customer contracts. The overall revenue growth trend for AWS was influenced by substantial cost optimization efforts among customers, who were looking to save money in an uncertain economic environment. AWS helped customers leverage more efficient cloud capabilities, such as Graviton chips and intelligent storage solutions, which initially diminished short-term revenue but were beneficial for customers in the long run. By the end of 2023, AWS saw a resurgence in new deals and customer renewals at larger commitments, indicating a positive outlook for future growth.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_2/query_2
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       85 |     +10 |      +5 |
| Risk Assessment      |    15% |       60 |       70 |       80 |     +10 |     +10 |
| Actionable Advice    |    15% |       50 |       75 |       80 |     +25 |      +5 |
| Evidence Usage       |    10% |       40 |       80 |       85 |     +40 |      +5 |
| Completeness         |    10% |       80 |      100 |      100 |     +20 |      +0 |
| Query Satisfaction   |    10% |       85 |       90 |       90 |      +5 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    70.00 |    83.25 |    86.75 |  +13.25 |    +3.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +13.25 pts  |  +18.93%
  V2 vs V1: +3.5 pts  |  +4.20%
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
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 10,
                "delta_v2_v1": 5,
                "weighted_v0": 10.5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "risk_assessment": {
                "label": "Risk Assessment",
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
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 75,
                "v2_score": 80,
                "delta_v1_v0": 25,
                "delta_v2_v1": 5,
                "weighted_v0": 7.5,
                "weighted_v1": 11.25,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 40,
                "delta_v2_v1": 5,
                "weighted_v0": 4.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
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
                "v0_score": 85,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 8.5,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 70.0,
        "overall_v1": 83.25,
        "overall_v2": 86.75,
        "v1_vs_v0_abs": 13.25,
        "v1_vs_v0_pct": 18.93,
        "v2_vs_v1_abs": 3.5,
        "v2_vs_v1_pct": 4.2
    }
