"""
RAG vs Pipeline Metrics -- document_7 / query_2
Query: How did Tesla's vehicle delivery volumes and production change in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's vehicle delivery volumes and production change in 2024?"

RAG_RESPONSE = "\nIn 2024, Tesla's vehicle delivery volumes and production experienced notable changes. The company produced approximately **1,773,000 consumer vehicles** and delivered around **1,789,000 consumer vehicles** during the year. This reflects a focus on increasing production capacity and efficiency, particularly with the introduction of new models like the Cybertruck, which contributed to an increase in deliveries of other models.\n\nHowever, there was a decrease in automotive sales revenue, which fell by **8%** compared to 2023, primarily due to lower average selling prices and a decrease in deliveries of the Model 3 and Model Y. Despite these challenges, Tesla's overall revenues increased slightly to **$97.69 billion**, with significant growth in the energy generation and storage segment, which saw revenues rise by **67%**.\n\nOverall, while Tesla's production and delivery numbers were strong, the company faced challenges with pricing and specific model deliveries that impacted its revenue performance.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_7/query_2
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |      100 |      +0 |     +10 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       60 |       65 |       80 |      +5 |     +15 |
| Actionable Advice    |    15% |       50 |       60 |       60 |     +10 |      +0 |
| Evidence Usage       |    10% |       80 |       90 |       90 |     +10 |      +0 |
| Completeness         |    10% |       75 |       80 |      100 |      +5 |     +20 |
| Query Satisfaction   |    10% |       85 |      100 |      100 |     +15 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    73.50 |    78.75 |    85.50 |   +5.25 |   +6.75 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +5.25 pts  |  +7.14%
  V2 vs V1: +6.75 pts  |  +8.57%
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
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 22.5,
                "weighted_v1": 22.5,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 65,
                "v2_score": 80,
                "delta_v1_v0": 5,
                "delta_v2_v1": 15,
                "weighted_v0": 9.0,
                "weighted_v1": 9.75,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
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
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 75,
                "v1_score": 80,
                "v2_score": 100,
                "delta_v1_v0": 5,
                "delta_v2_v1": 20,
                "weighted_v0": 7.5,
                "weighted_v1": 8.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 85,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 15,
                "delta_v2_v1": 0,
                "weighted_v0": 8.5,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 73.5,
        "overall_v1": 78.75,
        "overall_v2": 85.5,
        "v1_vs_v0_abs": 5.25,
        "v1_vs_v0_pct": 7.14,
        "v2_vs_v1_abs": 6.75,
        "v2_vs_v1_pct": 8.57
    }
