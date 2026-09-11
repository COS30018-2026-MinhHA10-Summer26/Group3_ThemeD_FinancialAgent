"""
RAG vs Pipeline Metrics -- document_6 / query_8
Query: What is Tesla's outlook for new vehicle models and production expansion in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What is Tesla's outlook for new vehicle models and production expansion in 2023?"

RAG_RESPONSE = "\nIn 2023, Tesla's outlook for new vehicle models and production expansion is focused on several key initiatives:\n\n1. **New Vehicle Models**: Tesla has actively launched the Cybertruck, which began deliveries in November 2023. The company is also ramping up production of the Tesla Semi, which is in pilot production, and is developing a next-generation vehicle platform and the Tesla Roadster.\n\n2. **Production Expansion**: Tesla aims to increase its manufacturing capacity across its existing facilities, including Gigafactories in Texas, Shanghai, and Berlin. The company is also planning to build a new Gigafactory in Monterrey, Mexico, to further enhance its production capabilities and localize manufacturing.\n\n3. **Production Goals**: Tesla produced approximately 1.85 million vehicles in 2023 and is focused on ramping production rates and efficiency at its factories. The company is also working to improve battery cell supply by developing its own cells to reduce costs and enhance vehicle performance.\n\n4. **Challenges and Uncertainties**: Tesla acknowledges potential challenges in ramping production due to component constraints, labor shortages, and the complexities of introducing new manufacturing technologies. The company experienced a sequential decline in production volumes during the third quarter of 2023 due to planned factory upgrades.\n\nOverall, Tesla is committed to expanding its vehicle offerings and production capabilities while navigating the inherent risks associated with manufacturing and market demand.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_6/query_8
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       85 |      100 |      100 |     +15 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       75 |       80 |       80 |      +5 |      +0 |
| Actionable Advice    |    15% |       60 |       80 |       80 |     +20 |      +0 |
| Evidence Usage       |    10% |       50 |       75 |       75 |     +25 |      +0 |
| Completeness         |    10% |       80 |       80 |      100 |      +0 |     +20 |
| Query Satisfaction   |    10% |       90 |       60 |       70 |     -30 |     +10 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    74.00 |    81.00 |    84.00 |    +7.0 |    +3.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +7.0 pts  |  +9.46%
  V2 vs V1: +3.0 pts  |  +3.70%
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
                "v0_score": 75,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 11.25,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
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
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 75,
                "v2_score": 75,
                "delta_v1_v0": 25,
                "delta_v2_v1": 0,
                "weighted_v0": 5.0,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 80,
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 20,
                "weighted_v0": 8.0,
                "weighted_v1": 8.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": -30,
                "delta_v2_v1": 10,
                "weighted_v0": 9.0,
                "weighted_v1": 6.0,
                "weighted_v2": 7.0
            }
        },
        "overall_v0": 74.0,
        "overall_v1": 81.0,
        "overall_v2": 84.0,
        "v1_vs_v0_abs": 7.0,
        "v1_vs_v0_pct": 9.46,
        "v2_vs_v1_abs": 3.0,
        "v2_vs_v1_pct": 3.7
    }
