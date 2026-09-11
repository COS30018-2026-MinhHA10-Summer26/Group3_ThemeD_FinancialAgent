"""
RAG vs Pipeline Metrics -- document_3 / query_7
Query: What were the significant legal and regulatory risks Amazon faced in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the significant legal and regulatory risks Amazon faced in 2024?"

RAG_RESPONSE = "\nIn 2024, Amazon faced several significant legal and regulatory risks, including:\n\n1. **Government Regulation and Compliance**: Amazon is subject to evolving regulations across various sectors, including e-commerce, digital content, data protection, and artificial intelligence. Changes in these regulations could increase compliance costs and limit operational flexibility. The company is regularly under review by regulatory authorities, which could lead to investigations and potential penalties.\n\n2. **Antitrust Investigations**: Amazon is involved in multiple investigations related to competition and consumer protection laws. These include claims of price fixing, monopolization, and other anticompetitive practices. The outcomes of these investigations could result in significant fines, operational changes, or restrictions on business practices.\n\n3. **Tax Controversies**: The company is engaged in various tax disputes in multiple jurisdictions, including claims from foreign tax authorities that could result in substantial tax liabilities. For instance, the Indian tax authority has asserted that taxes apply to cloud services fees, which could lead to significant payments if the matter is resolved unfavorably.\n\n4. **Intellectual Property Claims**: Amazon is facing lawsuits alleging infringement of patents related to its products and services. These claims could result in substantial damages or require changes to its business practices.\n\n5. **Data Privacy and Security Risks**: The company is under scrutiny for its data handling practices, particularly concerning compliance with privacy laws like the EU General Data Protection Regulation. Any breaches or failures to comply could lead to fines and reputational damage.\n\n6. **Product Liability**: Amazon is exposed to product liability claims for items sold through its platform, including those from third-party sellers. This could result in financial liabilities and impact customer trust.\n\nThese risks highlight the complex legal landscape in which Amazon operates, necessitating ongoing vigilance and adaptation to regulatory changes.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_7
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       20 |       45 |       85 |     +25 |     +40 |
| Business Analysis    |    15% |       35 |       35 |       70 |      +0 |     +35 |
| Risk Assessment      |    15% |       85 |       90 |       90 |      +5 |      +0 |
| Actionable Advice    |    15% |       20 |       40 |       80 |     +20 |     +40 |
| Evidence Usage       |    10% |       30 |       50 |       75 |     +20 |     +25 |
| Completeness         |    10% |       70 |       70 |       90 |      +0 |     +20 |
| Query Satisfaction   |    10% |       90 |       90 |       95 |      +0 |      +5 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    45.00 |    57.00 |    83.25 |   +12.0 |  +26.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +12.0 pts  |  +26.67%
  V2 vs V1: +26.25 pts  |  +46.05%
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
                "v1_score": 45,
                "v2_score": 85,
                "delta_v1_v0": 25,
                "delta_v2_v1": 40,
                "weighted_v0": 5.0,
                "weighted_v1": 11.25,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 35,
                "v1_score": 35,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 35,
                "weighted_v0": 5.25,
                "weighted_v1": 5.25,
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
                "v0_score": 20,
                "v1_score": 40,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 40,
                "weighted_v0": 3.0,
                "weighted_v1": 6.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 30,
                "v1_score": 50,
                "v2_score": 75,
                "delta_v1_v0": 20,
                "delta_v2_v1": 25,
                "weighted_v0": 3.0,
                "weighted_v1": 5.0,
                "weighted_v2": 7.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 20,
                "weighted_v0": 7.0,
                "weighted_v1": 7.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 90,
                "v2_score": 95,
                "delta_v1_v0": 0,
                "delta_v2_v1": 5,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.5
            }
        },
        "overall_v0": 45.0,
        "overall_v1": 57.0,
        "overall_v2": 83.25,
        "v1_vs_v0_abs": 12.0,
        "v1_vs_v0_pct": 26.67,
        "v2_vs_v1_abs": 26.25,
        "v2_vs_v1_pct": 46.05
    }
