"""
RAG vs Pipeline Metrics -- document_7 / query_4
Query: How did Tesla's Full Self-Driving and AI initiatives progress in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's Full Self-Driving and AI initiatives progress in 2024?"

RAG_RESPONSE = "\nIn 2024, Tesla's Full Self-Driving (FSD) and AI initiatives made significant progress. The company continued to enhance its FSD (Supervised) capabilities, which included the deployment of advanced driver-assist systems that relieve drivers of many tedious aspects of road travel. Tesla's FSD Computer, which runs neural networks in its vehicles, was further developed to improve real-world performance through continuous training with field data.\n\nA notable milestone was the anticipation of launching the Robotaxi business in 2025, which aims to operate fully autonomous vehicles. This initiative is expected to open access to a new customer base and reflects Tesla's commitment to advancing its AI capabilities. The company also emphasized the importance of its AI learnings from self-driving technology in other areas, such as robotics, exemplified by the development of Optimus, a robotic humanoid.\n\nFinancially, Tesla recognized $596 million in revenue from FSD (Supervised) features in 2024, indicating a growing monetization of its AI technologies. Overall, Tesla's focus on improving and deploying its FSD capabilities, alongside its broader AI initiatives, positions the company for continued innovation and market leadership in autonomous driving technology.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_7/query_4
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       85 |      100 |      100 |     +15 |      +0 |
| Business Analysis    |    15% |       70 |       60 |       70 |     -10 |     +10 |
| Risk Assessment      |    15% |       60 |       70 |       80 |     +10 |     +10 |
| Actionable Advice    |    15% |       50 |       65 |       80 |     +15 |     +15 |
| Evidence Usage       |    10% |       40 |       50 |       60 |     +10 |     +10 |
| Completeness         |    10% |       75 |       75 |       85 |      +0 |     +10 |
| Query Satisfaction   |    10% |       90 |       90 |      100 |      +0 |     +10 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    68.75 |    75.75 |    84.00 |    +7.0 |   +8.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +7.0 pts  |  +10.18%
  V2 vs V1: +8.25 pts  |  +10.89%
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
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": -10,
                "delta_v2_v1": 10,
                "weighted_v0": 10.5,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 9.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 65,
                "v2_score": 80,
                "delta_v1_v0": 15,
                "delta_v2_v1": 15,
                "weighted_v0": 7.5,
                "weighted_v1": 9.75,
                "weighted_v2": 12.0
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
                "v0_score": 75,
                "v1_score": 75,
                "v2_score": 85,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 7.5,
                "weighted_v1": 7.5,
                "weighted_v2": 8.5
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
        "overall_v1": 75.75,
        "overall_v2": 84.0,
        "v1_vs_v0_abs": 7.0,
        "v1_vs_v0_pct": 10.18,
        "v2_vs_v1_abs": 8.25,
        "v2_vs_v1_pct": 10.89
    }
