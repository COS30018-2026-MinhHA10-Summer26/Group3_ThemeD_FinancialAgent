"""
RAG vs Pipeline Metrics -- document_3 / query_3
Query: What were the highlights of Amazon's logistics and fulfillment network in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the highlights of Amazon's logistics and fulfillment network in 2024?"

RAG_RESPONSE = "\nIn 2024, Amazon's logistics and fulfillment network achieved several significant highlights:\n\n1. **Record Shipping Speeds**: Amazon continued to ship at record speeds for Prime members, marking the second consecutive year of such performance. This was attributed to enhancements in their fulfillment network, including regionalization redesign and new placement algorithms.\n\n2. **Expansion of Same-Day and Overnight Delivery**: The company expanded its same-day and overnight delivery services to dozens of smaller cities and towns across the U.S., aiming to improve service for rural customers. This initiative is expected to enable Amazon to deliver over a billion packages annually to customers in 13,000 zip codes.\n\n3. **Innovative Fulfillment Centers**: The introduction of innovative same-day fulfillment centers contributed to the improvement in delivery speeds. These centers are part of Amazon's strategy to enhance customer experience by ensuring faster access to products.\n\n4. **Regionalization of Fulfillment Network**: Amazon's fulfillment network underwent a regionalization redesign, which helped optimize delivery times and efficiency, allowing for faster shipping options.\n\n5. **Investment in Technology and Infrastructure**: Amazon invested heavily in technology and infrastructure to support its logistics capabilities, including enhancements to its fulfillment centers and the introduction of new technologies aimed at improving operational efficiency.\n\n6. **Prime Air Drones**: Amazon continued to develop its Prime Air drone delivery service, which aims to deliver items to customers within an hour, further enhancing the speed of delivery.\n\nThese highlights reflect Amazon's ongoing commitment to improving its logistics and fulfillment capabilities, ensuring that customers receive their orders as quickly and efficiently as possible.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_3
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |        0 |       60 |       80 |     +60 |     +20 |
| Business Analysis    |    15% |       60 |       60 |       70 |      +0 |     +10 |
| Risk Assessment      |    15% |        0 |       50 |       70 |     +50 |     +20 |
| Actionable Advice    |    15% |        0 |       30 |       50 |     +30 |     +20 |
| Evidence Usage       |    10% |        0 |       40 |       60 |     +40 |     +20 |
| Completeness         |    10% |       50 |       50 |       80 |      +0 |     +30 |
| Query Satisfaction   |    10% |       80 |       80 |       80 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    22.00 |    53.00 |    70.50 |   +31.0 |   +17.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +31.0 pts  |  +140.91%
  V2 vs V1: +17.5 pts  |  +33.02%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 0,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v1_v0": 60,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 15.0,
                "weighted_v2": 20.0
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
                "v0_score": 0,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v1_v0": 50,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 30,
                "v2_score": 50,
                "delta_v1_v0": 30,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 4.5,
                "weighted_v2": 7.5
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
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 30,
                "weighted_v0": 5.0,
                "weighted_v1": 5.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v0": 22.0,
        "overall_v1": 53.0,
        "overall_v2": 70.5,
        "v1_vs_v0_abs": 31.0,
        "v1_vs_v0_pct": 140.91,
        "v2_vs_v1_abs": 17.5,
        "v2_vs_v1_pct": 33.02
    }
