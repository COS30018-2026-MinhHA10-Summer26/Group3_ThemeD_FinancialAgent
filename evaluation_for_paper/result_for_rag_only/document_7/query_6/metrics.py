"""
RAG vs Pipeline Metrics -- document_7 / query_6
Query: What major capital investments did Tesla make in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "What major capital investments did Tesla make in 2024?"

RAG_RESPONSE = "\nIn 2024, Tesla made significant capital investments primarily focused on expanding its manufacturing capabilities and infrastructure. Key investments included:\n\n1. **Gigafactory Expansion**: Tesla continued to ramp up production at its existing Gigafactories, particularly in Texas, Nevada, Berlin, and Shanghai, to increase the manufacturing capacity for electric vehicles and energy storage products.\n\n2. **New Product Development**: Investments were made in the production of new vehicle models, including the Cybertruck and Tesla Semi, as well as advancements in battery technology and autonomous driving features.\n\n3. **Energy Storage Products**: Tesla deployed 31.4 GWh of energy storage products, indicating substantial investment in this segment to meet growing demand.\n\n4. **Research and Development**: Tesla increased its research and development expenses to $4.54 billion, reflecting a focus on artificial intelligence and other technological advancements.\n\n5. **Capital Expenditures**: The company projected capital expenditures to exceed $11 billion in 2025, indicating ongoing and future investments in manufacturing and infrastructure.\n\nOverall, Tesla's capital investments in 2024 were aimed at enhancing production capacity, developing new technologies, and expanding its energy product offerings.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_7/query_6
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       85 |      100 |      100 |     +15 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       85 |     +10 |      +5 |
| Risk Assessment      |    15% |       60 |       60 |       80 |      +0 |     +20 |
| Actionable Advice    |    15% |       50 |       50 |       70 |      +0 |     +20 |
| Evidence Usage       |    10% |       40 |       55 |       70 |     +15 |     +15 |
| Completeness         |    10% |       75 |       50 |       50 |     -25 |      +0 |
| Query Satisfaction   |    10% |       90 |       90 |      100 |      +0 |     +10 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    68.75 |    73.00 |    82.25 |   +4.25 |   +9.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +4.25 pts  |  +6.18%
  V2 vs V1: +9.25 pts  |  +12.67%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 85,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 15,
                "delta_v2_v1": 0,
                "weighted_v0": 21.25,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 10,
                "delta_v2_v1": 5,
                "weighted_v0": 10.5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
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
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 20,
                "weighted_v0": 7.5,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "v1_score": 55,
                "v2_score": 70,
                "delta_v1_v0": 15,
                "delta_v2_v1": 15,
                "weighted_v0": 4.0,
                "weighted_v1": 5.5,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 75,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v1_v0": -25,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 90,
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 68.75,
        "overall_v1": 73.0,
        "overall_v2": 82.25,
        "v1_vs_v0_abs": 4.25,
        "v1_vs_v0_pct": 6.18,
        "v2_vs_v1_abs": 9.25,
        "v2_vs_v1_pct": 12.67
    }
