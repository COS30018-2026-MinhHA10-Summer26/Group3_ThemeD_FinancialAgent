"""
RAG vs Pipeline Metrics -- document_1 / query_6
Query: How did Amazon's international segment perform financially in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's international segment perform financially in 2022?"

RAG_RESPONSE = "\nIn 2022, Amazon's international segment experienced a decline in financial performance. The international segment generated $118 billion in revenue, which represented an 8% decrease compared to the previous year. This decline was primarily attributed to the impact of foreign currency exchange rates, which reduced international net sales by approximately $15 billion. Despite this decrease, the segment saw some growth in unit sales, including sales by third-party sellers and advertising sales, but these were not sufficient to offset the overall revenue decline. Additionally, the operating loss for the international segment increased significantly to $7.7 billion, compared to a loss of $924 million in 2021, largely due to rising fulfillment and shipping costs, as well as increased technology and content costs.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_6
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       95 |       95 |      +5 |      +0 |
| Business Analysis    |    15% |       60 |       60 |       70 |      +0 |     +10 |
| Risk Assessment      |    15% |       50 |       50 |       75 |      +0 |     +25 |
| Actionable Advice    |    15% |       40 |       50 |       60 |     +10 |     +10 |
| Evidence Usage       |    10% |       70 |       70 |       80 |      +0 |     +10 |
| Completeness         |    10% |       80 |       80 |       80 |      +0 |      +0 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    69.00 |    72.75 |    80.50 |   +3.75 |   +7.75 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +3.75 pts  |  +5.43%
  V2 vs V1: +7.75 pts  |  +10.65%
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
                "v1_score": 95,
                "v2_score": 95,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 22.5,
                "weighted_v1": 23.75,
                "weighted_v2": 23.75
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 50,
                "v2_score": 75,
                "delta_v1_v0": 0,
                "delta_v2_v1": 25,
                "weighted_v0": 7.5,
                "weighted_v1": 7.5,
                "weighted_v2": 11.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 6.0,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 7.0,
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 69.0,
        "overall_v1": 72.75,
        "overall_v2": 80.5,
        "v1_vs_v0_abs": 3.75,
        "v1_vs_v0_pct": 5.43,
        "v2_vs_v1_abs": 7.75,
        "v2_vs_v1_pct": 10.65
    }
