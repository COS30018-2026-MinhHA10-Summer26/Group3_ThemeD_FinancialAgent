"""
RAG vs Pipeline Metrics -- document_6 / query_2
Query: How did Tesla's vehicle average selling price and gross margin trend in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's vehicle average selling price and gross margin trend in 2023?"

RAG_RESPONSE = "\nIn 2023, Tesla's average selling price for vehicles decreased due to overall price reductions and a shift in sales mix, which negatively impacted gross margins. Specifically, the gross margin for total automotive sales fell from 28.5% in 2022 to 19.4% in 2023. This decline was attributed to a lower average selling price, despite some cost reductions and benefits from IRA manufacturing credits. Overall, while Tesla's revenues increased, the gross margin trends indicate challenges in maintaining profitability amidst pricing pressures.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_6/query_2
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       90 |       90 |     +20 |      +0 |
| Risk Assessment      |    15% |       60 |       70 |       90 |     +10 |     +20 |
| Actionable Advice    |    15% |       50 |       60 |       60 |     +10 |      +0 |
| Evidence Usage       |    10% |       70 |       90 |       90 |     +20 |      +0 |
| Completeness         |    10% |       80 |       80 |       80 |      +0 |      +0 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    73.50 |    82.50 |    85.50 |    +9.0 |    +3.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +9.0 pts  |  +12.24%
  V2 vs V1: +3.0 pts  |  +3.64%
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
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 13.5,
                "weighted_v2": 13.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 20,
                "weighted_v0": 9.0,
                "weighted_v1": 10.5,
                "weighted_v2": 13.5
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
                "v0_score": 70,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
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
        "overall_v0": 73.5,
        "overall_v1": 82.5,
        "overall_v2": 85.5,
        "v1_vs_v0_abs": 9.0,
        "v1_vs_v0_pct": 12.24,
        "v2_vs_v1_abs": 3.0,
        "v2_vs_v1_pct": 3.64
    }
