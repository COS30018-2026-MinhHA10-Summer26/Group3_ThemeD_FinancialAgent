"""
RAG vs Pipeline Metrics -- document_7 / query_5
Query: What were the highlights of Tesla's energy and services segments in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the highlights of Tesla's energy and services segments in 2024?"

RAG_RESPONSE = "\nIn 2024, Tesla's energy and services segments experienced significant growth and developments:\n\n1. **Energy Generation and Storage Revenue**: The energy generation and storage segment saw a substantial increase in revenue, rising by $4.05 billion, or 67%, compared to the previous year. This growth was primarily driven by a 16.7 GWh increase in deployments of Megapack and Powerwall products.\n\n2. **Total Energy Storage Deployment**: Tesla deployed 31.4 GWh of energy storage products in 2024, indicating a strong focus on ramping production and increasing market penetration for these products.\n\n3. **Cost Reductions and Margin Improvements**: The gross margin for the energy generation and storage segment improved significantly, increasing from 18.9% to 26.2%. This improvement was attributed to cost reductions, including benefits from manufacturing credits, and a higher proportion of the storage business operating at a higher gross margin.\n\n4. **Focus on Product Development**: Tesla continued to enhance its energy storage offerings, including the introduction of Powerwall 3, and ramped up production capabilities at its Megafactories in Shanghai and Lathrop, California.\n\n5. **Services Revenue Growth**: The services and other revenue segment also saw an increase of $2.22 billion, or 27%, driven by higher sales of used vehicles, non-warranty maintenance services, collision revenue, paid Supercharging, and insurance services.\n\nOverall, Tesla's energy and services segments in 2024 highlighted a commitment to expanding its energy storage capabilities and improving operational efficiencies, contributing to significant revenue growth and enhanced profitability.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_7/query_5
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       50 |       60 |       70 |     +10 |     +10 |
| Actionable Advice    |    15% |       40 |       50 |       50 |     +10 |      +0 |
| Evidence Usage       |    10% |       60 |       80 |       80 |     +20 |      +0 |
| Completeness         |    10% |       80 |       90 |       90 |     +10 |      +0 |
| Query Satisfaction   |    10% |       90 |       90 |       90 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    69.50 |    78.00 |    79.50 |    +8.5 |    +1.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +8.5 pts  |  +12.23%
  V2 vs V1: +1.5 pts  |  +1.92%
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 22.5,
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
                "v0_score": 50,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 7.5,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
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
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 69.5,
        "overall_v1": 78.0,
        "overall_v2": 79.5,
        "v1_vs_v0_abs": 8.5,
        "v1_vs_v0_pct": 12.23,
        "v2_vs_v1_abs": 1.5,
        "v2_vs_v1_pct": 1.92
    }
