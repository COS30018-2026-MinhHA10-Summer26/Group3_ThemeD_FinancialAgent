"""
RAG vs Pipeline Metrics -- document_1 / query_7
Query: What were Amazon's capital expenditure and investment priorities in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's capital expenditure and investment priorities in 2022?"

RAG_RESPONSE = "\nIn 2022, Amazon's capital expenditure and investment priorities focused on several key areas:\n\n1. **Infrastructure Expansion**: Amazon continued to invest heavily in its fulfillment network, including the expansion of fulfillment centers and last-mile transportation networks to improve delivery efficiency. This was a response to the significant growth in consumer demand during the pandemic, which necessitated a doubling of their fulfillment center footprint over a short period.\n\n2. **Technology and Content**: There was a notable increase in spending on technology and content, which included investments in AWS (Amazon Web Services) to enhance its capabilities and support growth. This included the development of new machine learning chips and other technology infrastructure.\n\n3. **Cost Management and Efficiency**: Amazon undertook initiatives to streamline operations and reduce costs, particularly in its fulfillment network. This included optimizing processes and reevaluating inventory placement strategies to improve delivery speed and reduce costs.\n\n4. **Strategic Acquisitions**: Amazon made significant acquisitions, including MGM Holdings for approximately $6.1 billion, to enhance its digital media content offerings. They also planned to invest in healthcare through the acquisition of One Medical.\n\n5. **Long-term Growth Investments**: Despite facing macroeconomic challenges, Amazon emphasized maintaining long-term investments that could drive future growth, such as in cloud computing, advertising, and international expansion.\n\nOverall, Amazon's capital expenditures in 2022 were aimed at enhancing operational efficiency, expanding infrastructure, and investing in technology and strategic acquisitions to support long-term growth.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_7
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       80 |       80 |       85 |      +0 |      +5 |
| Business Analysis    |    15% |       70 |       70 |       75 |      +0 |      +5 |
| Risk Assessment      |    15% |       60 |       70 |       80 |     +10 |     +10 |
| Actionable Advice    |    15% |       50 |       70 |       75 |     +20 |      +5 |
| Evidence Usage       |    10% |       40 |       70 |       75 |     +30 |      +5 |
| Completeness         |    10% |       70 |       80 |       85 |     +10 |      +5 |
| Query Satisfaction   |    10% |       90 |       80 |       85 |     -10 |      +5 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    67.00 |    74.50 |    80.25 |    +7.5 |   +5.75 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +7.5 pts  |  +11.19%
  V2 vs V1: +5.75 pts  |  +7.72%
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
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 0,
                "delta_v2_v1": 5,
                "weighted_v0": 20.0,
                "weighted_v1": 20.0,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 0,
                "delta_v2_v1": 5,
                "weighted_v0": 10.5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 9.0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 20,
                "delta_v2_v1": 5,
                "weighted_v0": 7.5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 30,
                "delta_v2_v1": 5,
                "weighted_v0": 4.0,
                "weighted_v1": 7.0,
                "weighted_v2": 7.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 10,
                "delta_v2_v1": 5,
                "weighted_v0": 7.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": -10,
                "delta_v2_v1": 5,
                "weighted_v0": 9.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 67.0,
        "overall_v1": 74.5,
        "overall_v2": 80.25,
        "v1_vs_v0_abs": 7.5,
        "v1_vs_v0_pct": 11.19,
        "v2_vs_v1_abs": 5.75,
        "v2_vs_v1_pct": 7.72
    }
