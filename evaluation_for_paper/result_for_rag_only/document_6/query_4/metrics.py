"""
RAG vs Pipeline Metrics -- document_6 / query_4
Query: How did Tesla's energy storage deployment grow in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's energy storage deployment grow in 2023?"

RAG_RESPONSE = "\nIn 2023, Tesla's energy storage deployment experienced significant growth, with the company deploying 14.72 GWh of energy storage products. This marked a notable increase compared to previous years, reflecting Tesla's focus on ramping production of energy storage products and improving installation capabilities for its Solar Roof. Additionally, the energy generation and storage segment's revenue increased by 54% year-over-year, primarily driven by the rise in Megapack deployments. Overall, Tesla's efforts to enhance its energy storage offerings contributed to this growth in 2023.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_6/query_4
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       90 |     +10 |     +10 |
| Risk Assessment      |    15% |       50 |       50 |       70 |      +0 |     +20 |
| Actionable Advice    |    15% |       40 |       60 |       70 |     +20 |     +10 |
| Evidence Usage       |    10% |       60 |       80 |       80 |     +20 |      +0 |
| Completeness         |    10% |       20 |       70 |       80 |     +50 |     +10 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    63.50 |    76.00 |    83.00 |   +12.5 |    +7.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +12.5 pts  |  +19.69%
  V2 vs V1: +7.0 pts  |  +9.21%
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
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 10.5,
                "weighted_v1": 12.0,
                "weighted_v2": 13.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 20,
                "weighted_v0": 7.5,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": 20,
                "delta_v2_v1": 10,
                "weighted_v0": 6.0,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 20,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 50,
                "delta_v2_v1": 10,
                "weighted_v0": 2.0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 63.5,
        "overall_v1": 76.0,
        "overall_v2": 83.0,
        "v1_vs_v0_abs": 12.5,
        "v1_vs_v0_pct": 19.69,
        "v2_vs_v1_abs": 7.0,
        "v2_vs_v1_pct": 9.21
    }
