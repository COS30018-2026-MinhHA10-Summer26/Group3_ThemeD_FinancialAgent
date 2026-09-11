"""
RAG vs Pipeline Metrics -- document_4 / query_7
Query: How did Amazon's Prime membership and subscription services perform in 2025?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's Prime membership and subscription services perform in 2025?"

RAG_RESPONSE = "\nIn 2025, Amazon's Prime membership and subscription services performed strongly, contributing to the overall growth of the company. The total net sales for Amazon increased by 12% year-over-year, reaching approximately $716.9 billion. Within this growth, subscription services, including Amazon Prime, played a significant role, as they were part of the increased unit sales and advertising sales reported in both the North America and International segments.\n\nSpecifically, the North America segment saw net sales rise to $426.3 billion, while the International segment's sales increased to $161.9 billion. The growth in these segments was attributed to factors such as improved customer experience, including fast shipping offers, which are integral to the Prime membership.\n\nAdditionally, the AWS segment, which also contributes to subscription services through its offerings, reported a 20% increase in sales, reaching $128.7 billion. This indicates that Amazon's subscription services, including Prime, are not only maintaining their relevance but are also expanding in their impact on overall revenue.\n\nOverall, Amazon's Prime membership and subscription services were a key driver of growth in 2025, reflecting strong customer engagement and increased usage.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_4/query_7
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       80 |     +10 |      +0 |
| Risk Assessment      |    15% |       50 |       60 |       60 |     +10 |      +0 |
| Actionable Advice    |    15% |       40 |       50 |       50 |     +10 |      +0 |
| Evidence Usage       |    10% |       60 |       70 |       80 |     +10 |     +10 |
| Completeness         |    10% |       80 |       80 |       80 |      +0 |      +0 |
| Query Satisfaction   |    10% |       90 |       90 |       90 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    69.50 |    77.50 |    78.50 |    +8.0 |    +1.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +8.0 pts  |  +11.51%
  V2 vs V1: +1.0 pts  |  +1.29%
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
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 12.0,
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
                "v2_score": 50,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 6.0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 69.5,
        "overall_v1": 77.5,
        "overall_v2": 78.5,
        "v1_vs_v0_abs": 8.0,
        "v1_vs_v0_pct": 11.51,
        "v2_vs_v1_abs": 1.0,
        "v2_vs_v1_pct": 1.29
    }
