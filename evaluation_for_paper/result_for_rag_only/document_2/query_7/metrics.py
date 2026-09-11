"""
RAG vs Pipeline Metrics -- document_2 / query_7
Query: What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?"

RAG_RESPONSE = "\nIn its 2023 filing, Amazon disclosed several primary risks and uncertainties, including:\n\n1. **Intense Competition**: Amazon faces significant competition across various sectors, including e-commerce, cloud services, and digital content. Competitors may have greater resources, longer histories, and more established customer bases, which could impact Amazon's market share and profitability.\n\n2. **Expansion Risks**: The company's expansion into new products, services, technologies, and geographic regions poses risks due to limited experience in these areas. There may be challenges in customer adoption, profitability, and potential claims related to service disruptions or quality issues.\n\n3. **International Operations**: Amazon's international activities expose it to various risks, including local economic and political conditions, government regulations, and potential restrictions on foreign ownership and trade.\n\n4. **Operational Strain**: Rapid expansion can strain management, operational, financial, and other resources, potentially harming the company's reputation and growth.\n\n5. **Fluctuations in Demand**: Demand for Amazon's products and services can vary significantly due to seasonality, economic conditions, and unforeseen events, which can affect revenue and profitability.\n\n6. **Fraud and Liability Risks**: The company is at risk from fraudulent activities by sellers on its platform, which could lead to reputational damage and financial liability.\n\n7. **Intellectual Property Risks**: Amazon faces risks related to protecting its intellectual property and may be accused of infringing on third-party rights, which could lead to costly legal disputes.\n\n8. **Cybersecurity Threats**: The company is vulnerable to data breaches and other cybersecurity incidents that could compromise sensitive information and lead to regulatory actions.\n\n9. **Regulatory Changes**: Evolving regulations in various jurisdictions could impose additional compliance costs and operational restrictions.\n\n10. **Market and Economic Conditions**: Global economic and geopolitical conditions, including inflation and interest rates, can impact customer demand and spending patterns.\n\nThese risks highlight the complex and dynamic environment in which Amazon operates, emphasizing the potential challenges to its business model and growth strategies.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_2/query_7
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |        0 |       85 |       90 |     +85 |      +5 |
| Business Analysis    |    15% |        0 |       70 |       80 |     +70 |     +10 |
| Risk Assessment      |    15% |       90 |       70 |       85 |     -20 |     +15 |
| Actionable Advice    |    15% |        0 |       50 |       60 |     +50 |     +10 |
| Evidence Usage       |    10% |        0 |       60 |       70 |     +60 |     +10 |
| Completeness         |    10% |       70 |       75 |       85 |      +5 |     +10 |
| Query Satisfaction   |    10% |      100 |       70 |       85 |     -30 |     +15 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    30.50 |    70.25 |    80.25 |  +39.75 |   +10.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +39.75 pts  |  +130.33%
  V2 vs V1: +10.0 pts  |  +14.23%
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
                "v1_score": 85,
                "v2_score": 90,
                "delta_v1_v0": 85,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 21.25,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 70,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 90,
                "v1_score": 70,
                "v2_score": 85,
                "delta_v1_v0": -20,
                "delta_v2_v1": 15,
                "weighted_v0": 13.5,
                "weighted_v1": 10.5,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 50,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": 60,
                "delta_v2_v1": 10,
                "weighted_v0": 0.0,
                "weighted_v1": 6.0,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 75,
                "v2_score": 85,
                "delta_v1_v0": 5,
                "delta_v2_v1": 10,
                "weighted_v0": 7.0,
                "weighted_v1": 7.5,
                "weighted_v2": 8.5
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "v1_score": 70,
                "v2_score": 85,
                "delta_v1_v0": -30,
                "delta_v2_v1": 15,
                "weighted_v0": 10.0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 30.5,
        "overall_v1": 70.25,
        "overall_v2": 80.25,
        "v1_vs_v0_abs": 39.75,
        "v1_vs_v0_pct": 130.33,
        "v2_vs_v1_abs": 10.0,
        "v2_vs_v1_pct": 14.23
    }
