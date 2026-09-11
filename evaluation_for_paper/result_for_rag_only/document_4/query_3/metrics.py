"""
RAG vs Pipeline Metrics -- document_4 / query_3
Query: What is Amazon's profitability trend and operating margin outlook for 2025?
"""
from __future__ import annotations
import json

USER_QUERY = "What is Amazon's profitability trend and operating margin outlook for 2025?"

RAG_RESPONSE = "\nAmazon's profitability trend shows a positive trajectory, with operating income improving from $69 billion in 2024 to $80 billion in 2025, reflecting a 17% year-over-year increase. This corresponds to an operating margin of 10.8% in 2024, which improved to approximately 11.1% in 2025.\n\nLooking ahead to 2025, Amazon's operating margin outlook appears optimistic, as they anticipate continued growth driven by investments in technology and infrastructure, particularly in artificial intelligence and AWS. The company expects to maintain strong revenue growth, with net sales increasing by 12% from $638 billion in 2024 to $717 billion in 2025. This growth, combined with operational efficiencies and strategic investments, suggests a favorable outlook for profitability in the coming years.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_4/query_3
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       60 |       80 |       80 |     +20 |      +0 |
| Actionable Advice    |    15% |       50 |       70 |       70 |     +20 |      +0 |
| Evidence Usage       |    10% |       40 |       50 |       50 |     +10 |      +0 |
| Completeness         |    10% |       80 |       80 |       90 |      +0 |     +10 |
| Query Satisfaction   |    10% |       90 |       90 |       95 |      +0 |      +5 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    70.50 |    77.50 |    79.00 |    +7.0 |    +1.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +7.0 pts  |  +9.93%
  V2 vs V1: +1.5 pts  |  +1.94%
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
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 4.0,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 80,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 8.0,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 90,
                "v2_score": 95,
                "delta_v1_v0": 0,
                "delta_v2_v1": 5,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.5
            }
        },
        "overall_v0": 70.5,
        "overall_v1": 77.5,
        "overall_v2": 79.0,
        "v1_vs_v0_abs": 7.0,
        "v1_vs_v0_pct": 9.93,
        "v2_vs_v1_abs": 1.5,
        "v2_vs_v1_pct": 1.94
    }
