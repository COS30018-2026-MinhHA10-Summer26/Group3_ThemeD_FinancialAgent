"""
RAG vs Pipeline Metrics -- document_1 / query_2
Query: How did Amazon's AWS segment perform in 2022 compared to prior years?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's AWS segment perform in 2022 compared to prior years?"

RAG_RESPONSE = "\nIn 2022, Amazon's AWS segment experienced a year-over-year revenue growth of 29%, reaching an annualized revenue run rate of $85 billion. This growth was notable despite facing short-term headwinds due to macroeconomic conditions, which led many companies to be more cautious in their spending. The AWS segment's performance in 2022 continued to reflect strong demand, although it was slower compared to the 37% growth rate seen in 2021. Overall, AWS maintained its trajectory of growth, driven by increased customer usage and a robust pipeline of new customers, despite the challenges presented by the economic environment.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_2
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       75 |      +0 |      +5 |
| Risk Assessment      |    15% |       60 |       60 |       80 |      +0 |     +20 |
| Actionable Advice    |    15% |       50 |       70 |       75 |     +20 |      +5 |
| Evidence Usage       |    10% |       40 |       50 |       60 |     +10 |     +10 |
| Completeness         |    10% |       70 |       80 |       85 |     +10 |      +5 |
| Query Satisfaction   |    10% |       80 |       80 |       85 |      +0 |      +5 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    68.50 |    73.50 |    80.00 |    +5.0 |    +6.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +5.0 pts  |  +7.30%
  V2 vs V1: +6.5 pts  |  +8.84%
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
                "v0_score": 60,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 20,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 20,
                "delta_v2_v1": 5,
                "weighted_v0": 7.5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 4.0,
                "weighted_v1": 5.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 10,
                "delta_v2_v1": 5,
                "weighted_v0": 7.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 0,
                "delta_v2_v1": 5,
                "weighted_v0": 8.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 68.5,
        "overall_v1": 73.5,
        "overall_v2": 80.0,
        "v1_vs_v0_abs": 5.0,
        "v1_vs_v0_pct": 7.3,
        "v2_vs_v1_abs": 6.5,
        "v2_vs_v1_pct": 8.84
    }
