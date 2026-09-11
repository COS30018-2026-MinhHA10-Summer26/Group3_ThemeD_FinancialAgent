"""
RAG vs Pipeline Metrics -- document_6 / query_5
Query: What cost reduction initiatives did Tesla implement in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What cost reduction initiatives did Tesla implement in 2023?"

RAG_RESPONSE = "\nIn 2023, Tesla implemented several cost reduction initiatives aimed at improving operational efficiency and reducing manufacturing costs. Key initiatives included:\n\n1. **Increased Vehicle Production Efficiency**: Tesla focused on ramping up production capacity and improving the efficiency of its manufacturing processes. This included enhancements at existing factories and the introduction of new production technologies.\n\n2. **Vertical Integration and Localization**: The company emphasized vertically integrating its supply chain and localizing production to reduce costs associated with transportation and tariffs. This strategy was evident in the expansion of manufacturing facilities, including the establishment of a new Gigafactory in Monterrey, Mexico.\n\n3. **Cost Innovation Strategies**: Tesla continued to innovate in cost management, which allowed for competitively pricing its vehicles. This included optimizing the sales mix and reducing material costs.\n\n4. **Improved Fixed Cost Absorption**: The company benefited from better fixed cost absorption, which helped lower the average cost per unit of vehicles produced.\n\n5. **Utilization of IRA Manufacturing Credits**: Tesla leveraged manufacturing credits from the Inflation Reduction Act (IRA) to further reduce material costs, contributing to overall cost savings.\n\nThese initiatives collectively aimed to enhance Tesla's profitability while maintaining competitive pricing in the electric vehicle market.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_6/query_5
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       20 |       90 |       90 |     +70 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       80 |      +0 |     +10 |
| Risk Assessment      |    15% |        0 |       30 |       70 |     +30 |     +40 |
| Actionable Advice    |    15% |        0 |       20 |       60 |     +20 |     +40 |
| Evidence Usage       |    10% |        0 |       40 |       60 |     +40 |     +20 |
| Completeness         |    10% |       50 |       50 |       70 |      +0 |     +20 |
| Query Satisfaction   |    10% |       90 |       90 |       90 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    29.50 |    58.50 |    76.00 |   +29.0 |   +17.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +29.0 pts  |  +98.31%
  V2 vs V1: +17.5 pts  |  +29.91%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 20,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 70,
                "delta_v2_v1": 0,
                "weighted_v0": 5.0,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 10.5,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 30,
                "v2_score": 70,
                "delta_v1_v0": 30,
                "delta_v2_v1": 40,
                "weighted_v0": 0.0,
                "weighted_v1": 4.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 20,
                "v2_score": 60,
                "delta_v1_v0": 20,
                "delta_v2_v1": 40,
                "weighted_v0": 0.0,
                "weighted_v1": 3.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 40,
                "v2_score": 60,
                "delta_v1_v0": 40,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 4.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 20,
                "weighted_v0": 5.0,
                "weighted_v1": 5.0,
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
        "overall_v0": 29.5,
        "overall_v1": 58.5,
        "overall_v2": 76.0,
        "v1_vs_v0_abs": 29.0,
        "v1_vs_v0_pct": 98.31,
        "v2_vs_v1_abs": 17.5,
        "v2_vs_v1_pct": 29.91
    }
