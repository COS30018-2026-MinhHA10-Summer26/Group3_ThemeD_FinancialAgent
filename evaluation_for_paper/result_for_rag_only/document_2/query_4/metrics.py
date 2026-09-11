"""
RAG vs Pipeline Metrics -- document_2 / query_4
Query: How did Amazon's advertising revenue segment grow in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's advertising revenue segment grow in 2023?"

RAG_RESPONSE = "\nIn 2023, Amazon's advertising revenue segment experienced significant growth, increasing by 24% year-over-year from $38 billion in 2022 to $47 billion in 2023. This growth was primarily driven by the expansion of sponsored ads, including the introduction of Sponsored TV, which allows brands to create campaigns that can appear on multiple streaming TV services. Additionally, Amazon expanded its streaming TV advertising by introducing ads into Prime Video shows and movies, reaching over 200 million monthly viewers.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_2/query_4
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       75 |      +0 |      +5 |
| Risk Assessment      |    15% |       50 |       60 |       80 |     +10 |     +20 |
| Actionable Advice    |    15% |       40 |       80 |       80 |     +40 |      +0 |
| Evidence Usage       |    10% |       60 |       70 |       90 |     +10 |     +20 |
| Completeness         |    10% |       70 |       90 |       90 |     +20 |      +0 |
| Query Satisfaction   |    10% |       80 |       90 |       90 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    67.50 |    81.50 |    87.25 |   +14.0 |   +5.75 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +14.0 pts  |  +20.74%
  V2 vs V1: +5.75 pts  |  +7.06%
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
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 0,
                "delta_v2_v1": 5,
                "weighted_v0": 10.5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 20,
                "weighted_v0": 7.5,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 40,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 20,
                "weighted_v0": 6.0,
                "weighted_v1": 7.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 67.5,
        "overall_v1": 81.5,
        "overall_v2": 87.25,
        "v1_vs_v0_abs": 14.0,
        "v1_vs_v0_pct": 20.74,
        "v2_vs_v1_abs": 5.75,
        "v2_vs_v1_pct": 7.06
    }
