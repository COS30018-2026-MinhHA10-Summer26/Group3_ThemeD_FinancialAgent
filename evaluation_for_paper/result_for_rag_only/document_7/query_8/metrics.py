"""
RAG vs Pipeline Metrics -- document_7 / query_8
Query: What does Tesla's 2024 annual report say about its Optimus robot and future technology roadmap?
"""
from __future__ import annotations
import json

USER_QUERY = "What does Tesla's 2024 annual report say about its Optimus robot and future technology roadmap?"

RAG_RESPONSE = "\nTesla's 2024 annual report highlights significant developments regarding its Optimus robot and the company's future technology roadmap. The report indicates that Tesla is actively applying its artificial intelligence advancements from self-driving technology to robotics, particularly through the development of the Optimus robot, a humanoid robot that is controlled by the same AI system used in Tesla's vehicles. \n\nFurthermore, Tesla plans to launch its Robotaxi business in 2025, which will feature fully autonomous vehicles, thereby expanding its technological capabilities and market reach. The report emphasizes the company's commitment to leveraging AI and robotics to enhance its product offerings and operational efficiencies, aligning with its mission to accelerate the world's transition to sustainable energy. \n\nOverall, Tesla's future technology roadmap includes a focus on AI, robotics, and the integration of these technologies into its existing and upcoming products, such as the Cybercab and the Optimus robot.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_7/query_8
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       30 |       70 |      100 |     +40 |     +30 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       30 |       50 |       80 |     +20 |     +30 |
| Actionable Advice    |    15% |        0 |       20 |       70 |     +20 |     +50 |
| Evidence Usage       |    10% |        0 |       35 |       55 |     +35 |     +20 |
| Completeness         |    10% |       50 |       60 |       80 |     +10 |     +20 |
| Query Satisfaction   |    10% |       80 |       90 |       90 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    35.50 |    57.00 |    80.50 |   +21.5 |   +23.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +21.5 pts  |  +60.56%
  V2 vs V1: +23.5 pts  |  +41.23%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 30,
                "v1_score": 70,
                "v2_score": 100,
                "delta_v1_v0": 40,
                "delta_v2_v1": 30,
                "weighted_v0": 7.5,
                "weighted_v1": 17.5,
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
                "v0_score": 30,
                "v1_score": 50,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 30,
                "weighted_v0": 4.5,
                "weighted_v1": 7.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 20,
                "v2_score": 70,
                "delta_v1_v0": 20,
                "delta_v2_v1": 50,
                "weighted_v0": 0.0,
                "weighted_v1": 3.0,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 35,
                "v2_score": 55,
                "delta_v1_v0": 35,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 3.5,
                "weighted_v2": 5.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 20,
                "weighted_v0": 5.0,
                "weighted_v1": 6.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 35.5,
        "overall_v1": 57.0,
        "overall_v2": 80.5,
        "v1_vs_v0_abs": 21.5,
        "v1_vs_v0_pct": 60.56,
        "v2_vs_v1_abs": 23.5,
        "v2_vs_v1_pct": 41.23
    }
