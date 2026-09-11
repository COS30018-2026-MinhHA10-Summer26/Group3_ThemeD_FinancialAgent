"""
RAG vs Pipeline Metrics -- document_5 / query_4
Query: How did Tesla's energy generation and storage segment perform in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's energy generation and storage segment perform in 2022?"

RAG_RESPONSE = "\nIn 2022, Tesla's energy generation and storage segment performed well, generating revenues of $3.909 billion, which represents a 40% increase from $2.789 billion in 2021. This growth was primarily driven by an increase in deployments of energy storage products such as Megapack and Powerwall, as well as higher average selling prices for these products and solar cash and loan deployments due to price increases.\n\nAdditionally, the gross profit for the energy generation and storage segment improved significantly, rising to $288 million from a loss of $129 million in the previous year. The gross margin for this segment also increased from -4.6% in 2021 to 7.4% in 2022, indicating a more favorable cost structure and a higher proportion of sales from energy storage products, which typically have higher margins. \n\nOverall, the segment showed strong growth and improved profitability in 2022.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_5/query_4
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       95 |       95 |       95 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       75 |       75 |      +5 |      +0 |
| Risk Assessment      |    15% |       50 |       70 |       80 |     +20 |     +10 |
| Actionable Advice    |    15% |       40 |       50 |       80 |     +10 |     +30 |
| Evidence Usage       |    10% |       60 |       70 |       70 |     +10 |      +0 |
| Completeness         |    10% |       80 |       80 |       90 |      +0 |     +10 |
| Query Satisfaction   |    10% |       90 |       90 |       90 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    70.75 |    77.00 |    84.00 |   +6.25 |    +7.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +6.25 pts  |  +8.83%
  V2 vs V1: +7.0 pts  |  +9.09%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 95,
                "v1_score": 95,
                "v2_score": 95,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 23.75,
                "weighted_v1": 23.75,
                "weighted_v2": 23.75
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 75,
                "v2_score": 75,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 11.25,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 10,
                "weighted_v0": 7.5,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 50,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 30,
                "weighted_v0": 6.0,
                "weighted_v1": 7.5,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 7.0,
                "weighted_v2": 7.0
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
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 70.75,
        "overall_v1": 77.0,
        "overall_v2": 84.0,
        "v1_vs_v0_abs": 6.25,
        "v1_vs_v0_pct": 8.83,
        "v2_vs_v1_abs": 7.0,
        "v2_vs_v1_pct": 9.09
    }
