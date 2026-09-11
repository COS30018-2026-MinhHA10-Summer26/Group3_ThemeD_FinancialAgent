"""
RAG vs Pipeline Metrics -- document_7 / query_7
Query: What regulatory and competitive risks did Tesla highlight in its 2024 annual report?
"""
from __future__ import annotations
import json

USER_QUERY = "What regulatory and competitive risks did Tesla highlight in its 2024 annual report?"

RAG_RESPONSE = "\nIn its 2024 annual report, Tesla highlighted several regulatory and competitive risks:\n\n1. **Regulatory Risks**:\n   - Tesla's operations are subject to numerous governmental regulations that vary by jurisdiction, which can impact the sale and operation of its vehicles and energy products. This includes compliance with vehicle safety standards, emissions regulations, and other environmental laws.\n   - The company noted the evolving nature of laws regarding self-driving vehicles, which could restrict the design and functionality of its Autopilot and Full Self-Driving (FSD) features. This regulatory patchwork increases complexity and may delay or limit the rollout of new technologies.\n   - Changes in government incentives, such as tax credits and rebates for electric vehicles and renewable energy products, could adversely affect demand for Tesla's products. The expiration or reduction of such incentives could make Tesla's offerings less competitive.\n\n2. **Competitive Risks**:\n   - The automotive market is highly competitive, with many established and new manufacturers entering the electric vehicle space. This competition could lead to reduced market share and pricing pressures for Tesla.\n   - Tesla faces competition not only from traditional automakers but also from new entrants in the electric vehicle market, which could impact its sales and profitability.\n   - The energy generation and storage market is also competitive, with various companies offering similar products, which could affect Tesla's market position and pricing strategies.\n\nThese risks, if realized, could materially impact Tesla's business, financial condition, and operating results.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_7/query_7
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |        0 |       70 |       70 |     +70 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       85 |       90 |       90 |      +5 |      +0 |
| Actionable Advice    |    15% |        0 |       40 |       60 |     +40 |     +20 |
| Evidence Usage       |    10% |        0 |       50 |       50 |     +50 |      +0 |
| Completeness         |    10% |       70 |       70 |       70 |      +0 |      +0 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    39.25 |    69.50 |    72.50 |  +30.25 |    +3.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +30.25 pts  |  +77.07%
  V2 vs V1: +3.0 pts  |  +4.32%
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
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 70,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 17.5,
                "weighted_v2": 17.5
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
                "v0_score": 85,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 12.75,
                "weighted_v1": 13.5,
                "weighted_v2": 13.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 40,
                "v2_score": 60,
                "delta_v1_v0": 40,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 6.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v1_v0": 50,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 7.0,
                "weighted_v2": 7.0
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
        "overall_v0": 39.25,
        "overall_v1": 69.5,
        "overall_v2": 72.5,
        "v1_vs_v0_abs": 30.25,
        "v1_vs_v0_pct": 77.07,
        "v2_vs_v1_abs": 3.0,
        "v2_vs_v1_pct": 4.32
    }
