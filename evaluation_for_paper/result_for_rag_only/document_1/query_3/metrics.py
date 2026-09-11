"""
RAG vs Pipeline Metrics -- document_1 / query_3
Query: What were the major cost drivers that impacted Amazon's operating income in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the major cost drivers that impacted Amazon's operating income in 2022?"

RAG_RESPONSE = "\nIn 2022, Amazon's operating income was significantly impacted by several major cost drivers:\n\n1. **Increased Fulfillment and Shipping Costs**: There was a notable rise in costs associated with fulfilling orders and shipping products, which included investments in the fulfillment network and increased transportation costs. These costs were exacerbated by rising wage rates and incentives for employees.\n\n2. **Technology and Content Costs**: Amazon saw a substantial increase in technology and content expenses, which included payroll for employees involved in research and development, as well as costs related to maintaining and enhancing their technology infrastructure.\n\n3. **General Operating Expenses**: There was growth in various operating expenses, including general and administrative costs, which were driven by increased payroll and professional fees.\n\n4. **Inflation and Economic Conditions**: Macroeconomic factors such as inflation, rising interest rates, and global supply chain constraints contributed to increased operating costs across the North America and International segments.\n\n5. **Impairments**: In 2022, Amazon recorded approximately $1.1 billion in impairments of property and equipment, which also negatively affected operating income.\n\nOverall, these factors combined to create a challenging operating environment, leading to a significant decline in operating income compared to the previous year.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_3
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       85 |       70 |       70 |     -15 |      +0 |
| Business Analysis    |    15% |       70 |       75 |       75 |      +5 |      +0 |
| Risk Assessment      |    15% |       60 |       70 |       70 |     +10 |      +0 |
| Actionable Advice    |    15% |       50 |       80 |       80 |     +30 |      +0 |
| Evidence Usage       |    10% |       40 |       60 |       60 |     +20 |      +0 |
| Completeness         |    10% |       75 |       90 |       90 |     +15 |      +0 |
| Query Satisfaction   |    10% |       90 |       85 |       85 |      -5 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    68.75 |    74.75 |    74.75 |    +6.0 |    +0.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +6.0 pts  |  +8.73%
  V2 vs V1: +0.0 pts  |  +0.00%
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
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": -15,
                "delta_v2_v1": 0,
                "weighted_v0": 21.25,
                "weighted_v1": 17.5,
                "weighted_v2": 17.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 75,
                "v2_score": 75,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 11.25,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
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
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 30,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 4.0,
                "weighted_v1": 6.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 75,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 15,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 85,
                "v2_score": 85,
                "delta_v1_v0": -5,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 8.5,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 68.75,
        "overall_v1": 74.75,
        "overall_v2": 74.75,
        "v1_vs_v0_abs": 6.0,
        "v1_vs_v0_pct": 8.73,
        "v2_vs_v1_abs": 0.0,
        "v2_vs_v1_pct": 0.0
    }
