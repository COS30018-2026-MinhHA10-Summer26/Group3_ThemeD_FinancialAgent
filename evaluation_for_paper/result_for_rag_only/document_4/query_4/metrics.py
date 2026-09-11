"""
RAG vs Pipeline Metrics -- document_4 / query_4
Query: What strategic acquisitions or investments did Amazon make in 2025?
"""
from __future__ import annotations
import json

USER_QUERY = "What strategic acquisitions or investments did Amazon make in 2025?"

RAG_RESPONSE = "\nIn 2025, Amazon made several strategic acquisitions and investments, including:\n\n1. **Investment in Robotics**: Amazon has been heavily investing in robotics initiatives, building on its previous acquisition of Kiva in 2012. The company now operates over one million robots in its fulfillment centers, aiming to enhance delivery speed and reduce costs.\n\n2. **Expansion of Rural Delivery Network**: Amazon committed over $4 billion to expand its rural delivery network, focusing on underserved communities.\n\n3. **Amazon Leo**: Amazon has developed a low Earth orbit satellite network, Amazon Leo, with over 200 satellites launched. This network aims to provide high-speed internet access to underserved areas and is expected to begin commercial service in mid-2026. Notably, Delta Airlines has committed to using Amazon Leo for Wi-Fi on 500 planes starting in 2028.\n\n4. **Investments in AI**: Amazon has significantly increased its investments in artificial intelligence, particularly through AWS, which has seen a rapid increase in AI-related revenue. The company is also developing its own AI chips, such as Trainium, to enhance its offerings.\n\n5. **Acquisitions**: In 2025, Amazon completed acquisition activity for immaterial aggregate cash consideration, net of cash acquired, although specific details on these acquisitions were not provided in the documents.\n\nOverall, Amazon's strategic focus in 2025 was on enhancing its technological capabilities, expanding its service offerings, and improving customer access, particularly in rural areas and through advanced technologies like AI and satellite internet.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_4/query_4
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       70 |       85 |       85 |     +15 |      +0 |
| Business Analysis    |    15% |       60 |       70 |       70 |     +10 |      +0 |
| Risk Assessment      |    15% |       50 |       75 |       80 |     +25 |      +5 |
| Actionable Advice    |    15% |       40 |       70 |       75 |     +30 |      +5 |
| Evidence Usage       |    10% |       30 |       60 |       65 |     +30 |      +5 |
| Completeness         |    10% |       80 |       90 |       90 |     +10 |      +0 |
| Query Satisfaction   |    10% |       90 |       60 |       60 |     -30 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    60.00 |    74.50 |    76.50 |   +14.5 |    +2.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +14.5 pts  |  +24.17%
  V2 vs V1: +2.0 pts  |  +2.68%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 70,
                "v1_score": 85,
                "v2_score": 85,
                "delta_v1_v0": 15,
                "delta_v2_v1": 0,
                "weighted_v0": 17.5,
                "weighted_v1": 21.25,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 75,
                "v2_score": 80,
                "delta_v1_v0": 25,
                "delta_v2_v1": 5,
                "weighted_v0": 7.5,
                "weighted_v1": 11.25,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 30,
                "delta_v2_v1": 5,
                "weighted_v0": 6.0,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 30,
                "v1_score": 60,
                "v2_score": 65,
                "delta_v1_v0": 30,
                "delta_v2_v1": 5,
                "weighted_v0": 3.0,
                "weighted_v1": 6.0,
                "weighted_v2": 6.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v1_v0": -30,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 6.0,
                "weighted_v2": 6.0
            }
        },
        "overall_v0": 60.0,
        "overall_v1": 74.5,
        "overall_v2": 76.5,
        "v1_vs_v0_abs": 14.5,
        "v1_vs_v0_pct": 24.17,
        "v2_vs_v1_abs": 2.0,
        "v2_vs_v1_pct": 2.68
    }
