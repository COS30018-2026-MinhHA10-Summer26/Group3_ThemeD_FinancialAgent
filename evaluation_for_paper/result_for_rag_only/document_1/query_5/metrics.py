"""
RAG vs Pipeline Metrics -- document_1 / query_5
Query: What key risks does Amazon identify in its 2022 annual report?
"""
from __future__ import annotations
import json

USER_QUERY = "What key risks does Amazon identify in its 2022 annual report?"

RAG_RESPONSE = "\nIn its 2022 annual report, Amazon identifies several key risks, including:\n\n1. **Intense Competition**: Amazon faces significant competition across various sectors, including e-commerce, cloud services, and digital content. Competitors may have greater resources, brand recognition, and customer loyalty, which can impact Amazon's market share and profitability.\n\n2. **Expansion Risks**: The company’s expansion into new products, services, technologies, and geographic regions carries risks due to limited experience in these areas. There is uncertainty regarding customer adoption and potential claims related to service disruptions or quality issues.\n\n3. **International Operations**: Amazon's international activities expose it to various risks, including local economic and political conditions, government regulations, and compliance with differing legal systems. These factors can affect profitability and operational success in foreign markets.\n\n4. **Operational Strain**: Rapid expansion can strain management, operational, financial, and other resources. Failure to manage this growth effectively could harm Amazon's reputation and limit its growth potential.\n\n5. **Fluctuations in Demand**: Demand for Amazon's products and services can fluctuate significantly due to seasonality, economic conditions, and unforeseen events, which can impact revenue and operational efficiency.\n\n6. **Fraud and Liability Risks**: Amazon is at risk of fraudulent activities by sellers on its platform, which could lead to legal liabilities and damage to its reputation.\n\n7. **Intellectual Property Risks**: The company faces risks related to protecting its intellectual property and may be accused of infringing on the rights of others, which could result in costly legal disputes.\n\n8. **Data Security and System Interruptions**: Amazon collects and processes large amounts of sensitive data, making it vulnerable to data breaches and security incidents that could harm its operations and reputation.\n\n9. **Regulatory Changes**: Evolving government regulations, particularly concerning data privacy, taxation, and competition, could impose additional costs or operational constraints.\n\nThese risks, among others, could materially affect Amazon's business, financial condition, and stock price.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_5
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |        0 |        0 |        0 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       60 |       70 |     +60 |     +10 |
| Risk Assessment      |    15% |       90 |       70 |       90 |     -20 |     +20 |
| Actionable Advice    |    15% |        0 |        0 |        0 |      +0 |      +0 |
| Evidence Usage       |    10% |        0 |        0 |        0 |      +0 |      +0 |
| Completeness         |    10% |       70 |       80 |       90 |     +10 |     +10 |
| Query Satisfaction   |    10% |      100 |       80 |       90 |     -20 |     +10 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    30.50 |    35.50 |    42.00 |    +5.0 |    +6.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +5.0 pts  |  +16.39%
  V2 vs V1: +6.5 pts  |  +18.31%
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
                "v1_score": 0,
                "v2_score": 0,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
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
                "v0_score": 90,
                "v1_score": 70,
                "v2_score": 90,
                "delta_v1_v0": -20,
                "delta_v2_v1": 20,
                "weighted_v0": 13.5,
                "weighted_v1": 10.5,
                "weighted_v2": 13.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 90,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 7.0,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "v1_score": 80,
                "v2_score": 90,
                "delta_v1_v0": -20,
                "delta_v2_v1": 10,
                "weighted_v0": 10.0,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 30.5,
        "overall_v1": 35.5,
        "overall_v2": 42.0,
        "v1_vs_v0_abs": 5.0,
        "v1_vs_v0_pct": 16.39,
        "v2_vs_v1_abs": 6.5,
        "v2_vs_v1_pct": 18.31
    }
