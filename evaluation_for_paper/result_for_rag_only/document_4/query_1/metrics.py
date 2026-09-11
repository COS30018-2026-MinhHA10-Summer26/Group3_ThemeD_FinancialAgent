"""
RAG vs Pipeline Metrics -- document_4 / query_1
Query: What were Amazon's key financial results and revenue breakdown for fiscal year 2025?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's key financial results and revenue breakdown for fiscal year 2025?"

RAG_RESPONSE = "\nIn fiscal year 2025, Amazon reported key financial results as follows:\n\n- **Total Revenue**: $717 billion, which represents a 12% increase from $638 billion in 2024.\n- **Revenue Breakdown**:\n  - **North America**: $426 billion (up 10% from $387 billion)\n  - **International**: $162 billion (up 13% from $143 billion)\n  - **Amazon Web Services (AWS)**: $129 billion (up 20% from $108 billion)\n\n- **Operating Income**: $80 billion, an increase of 17% from $69 billion in 2024.\n- **Free Cash Flow**: Decreased to $11 billion from $38 billion in 2024, primarily due to a significant increase in capital expenditures related to investments in artificial intelligence and other initiatives.\n\nThese results indicate a strong performance across all segments, particularly in AWS, which continues to show robust growth.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_4/query_1
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |       50 |       50 |       60 |      +0 |     +10 |
| Risk Assessment      |    15% |       40 |       40 |       70 |      +0 |     +30 |
| Actionable Advice    |    15% |       30 |       50 |       70 |     +20 |     +20 |
| Evidence Usage       |    10% |       20 |       50 |       50 |     +30 |      +0 |
| Completeness         |    10% |       70 |       70 |       70 |      +0 |      +0 |
| Query Satisfaction   |    10% |       90 |       90 |       90 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    58.50 |    67.00 |    76.00 |    +8.5 |    +9.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +8.5 pts  |  +14.53%
  V2 vs V1: +9.0 pts  |  +13.43%
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
                "v0_score": 50,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 7.5,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 40,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 30,
                "weighted_v0": 6.0,
                "weighted_v1": 6.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 30,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 20,
                "delta_v2_v1": 20,
                "weighted_v0": 4.5,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 20,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v1_v0": 30,
                "delta_v2_v1": 0,
                "weighted_v0": 2.0,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 7.0,
                "weighted_v2": 7.0
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
        "overall_v0": 58.5,
        "overall_v1": 67.0,
        "overall_v2": 76.0,
        "v1_vs_v0_abs": 8.5,
        "v1_vs_v0_pct": 14.53,
        "v2_vs_v1_abs": 9.0,
        "v2_vs_v1_pct": 13.43
    }
