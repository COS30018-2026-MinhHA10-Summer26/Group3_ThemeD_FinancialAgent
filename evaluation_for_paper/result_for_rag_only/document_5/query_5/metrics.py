"""
RAG vs Pipeline Metrics -- document_5 / query_5
Query: What were the main risks Tesla identified in its 2022 annual report?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the main risks Tesla identified in its 2022 annual report?"

RAG_RESPONSE = "\nThe main risks identified by Tesla in its 2022 annual report include:\n\n1. **Government Investigations and Legal Proceedings**: Tesla faces potential liabilities, penalties, and sanctions arising from ongoing governmental investigations and legal proceedings. The outcomes of these matters are uncertain and could adversely affect the company.\n\n2. **Environmental Regulations**: Tesla is subject to environmental regulations and has faced fines related to compliance issues, such as those concerning end-of-life battery products and waste segregation practices.\n\n3. **Foreign Currency Risk**: The company operates globally and is exposed to foreign currency risks that can affect its revenue and operating results due to fluctuations in exchange rates.\n\n4. **Supply Chain and Manufacturing Risks**: Tesla's reliance on suppliers for components and raw materials presents risks related to the availability and pricing of these materials, which can impact production and costs.\n\n5. **Market Competition**: The automotive and energy sectors are highly competitive, and Tesla faces competition from established automakers and new entrants, which could affect its market share and profitability.\n\nThese risks are discussed in detail in the \"Risk Factors\" section of the annual report.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_5/query_5
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       80 |       90 |       90 |     +10 |      +0 |
| Business Analysis    |    15% |        0 |       60 |       70 |     +60 |     +10 |
| Risk Assessment      |    15% |       85 |       80 |       85 |      -5 |      +5 |
| Actionable Advice    |    15% |        0 |        0 |       20 |      +0 |     +20 |
| Evidence Usage       |    10% |        0 |       80 |       80 |     +80 |      +0 |
| Completeness         |    10% |       50 |       90 |       90 |     +40 |      +0 |
| Query Satisfaction   |    10% |      100 |      100 |      100 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    47.75 |    70.50 |    75.75 |  +22.75 |   +5.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +22.75 pts  |  +47.64%
  V2 vs V1: +5.25 pts  |  +7.45%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 80,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 20.0,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": 60,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 85,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": -5,
                "delta_v2_v1": 5,
                "weighted_v0": 12.75,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 0,
                "v2_score": 20,
                "delta_v1_v0": 0,
                "delta_v2_v1": 20,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 3.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 80,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 40,
                "delta_v2_v1": 0,
                "weighted_v0": 5.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 10.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 47.75,
        "overall_v1": 70.5,
        "overall_v2": 75.75,
        "v1_vs_v0_abs": 22.75,
        "v1_vs_v0_pct": 47.64,
        "v2_vs_v1_abs": 5.25,
        "v2_vs_v1_pct": 7.45
    }
