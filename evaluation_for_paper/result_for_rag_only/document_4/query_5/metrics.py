"""
RAG vs Pipeline Metrics -- document_4 / query_5
Query: How did macroeconomic conditions affect Amazon's business in 2025?
"""
from __future__ import annotations
import json

USER_QUERY = "How did macroeconomic conditions affect Amazon's business in 2025?"

RAG_RESPONSE = "\nIn 2025, macroeconomic conditions significantly impacted Amazon's business in several ways:\n\n1. **Inflation and Interest Rates**: The company faced challenges related to inflation and rising interest rates, which affected consumer spending and demand for products and services. These macroeconomic factors made it difficult for Amazon to predict growth needs and manage expenses effectively.\n\n2. **Supply Chain Volatility**: Resource and supply volatility, including fluctuations in the availability and cost of materials, impacted Amazon's ability to maintain inventory levels and fulfill customer orders efficiently. This volatility was exacerbated by global economic and geopolitical developments.\n\n3. **Investment in Technology**: Despite the challenges, Amazon continued to invest heavily in technology, particularly in artificial intelligence and infrastructure. This investment was aimed at enhancing customer experience and operational efficiency, but it also led to increased capital expenditures, which affected free cash flow. Free cash flow decreased from $38 billion in 2024 to $11 billion in 2025, primarily due to a significant increase in capital expenditures related to these initiatives.\n\n4. **Revenue Growth**: Amazon's revenue grew by 12% year-over-year, reaching $717 billion in 2025. This growth was driven by increased sales in both the North America and International segments, as well as a 20% increase in AWS revenue. However, the growth was tempered by the adverse effects of foreign exchange rates, which negatively impacted revenue by approximately $4.4 billion.\n\n5. **Operational Costs**: Operating expenses increased significantly, with costs related to fulfillment, technology, and infrastructure rising due to the need to support higher sales volumes and investments in new technologies. The overall increase in operating expenses was driven by both inflationary pressures and the company's strategic investments.\n\nIn summary, while Amazon experienced revenue growth in 2025, macroeconomic conditions such as inflation, interest rates, and supply chain volatility posed challenges that influenced its operational costs and cash flow. The company's continued investment in technology and infrastructure was a strategic response to these conditions, aimed at positioning Amazon for long-term growth despite short-term financial pressures.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_4/query_5
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       85 |       90 |       90 |      +5 |      +0 |
| Business Analysis    |    15% |       70 |       75 |       75 |      +5 |      +0 |
| Risk Assessment      |    15% |       75 |       90 |       90 |     +15 |      +0 |
| Actionable Advice    |    15% |       60 |       80 |       80 |     +20 |      +0 |
| Evidence Usage       |    10% |       50 |       50 |       60 |      +0 |     +10 |
| Completeness         |    10% |       80 |       80 |       80 |      +0 |      +0 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    74.00 |    82.25 |    83.25 |   +8.25 |    +1.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +8.25 pts  |  +11.15%
  V2 vs V1: +1.0 pts  |  +1.22%
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
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 21.25,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
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
                "v0_score": 75,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 15,
                "delta_v2_v1": 0,
                "weighted_v0": 11.25,
                "weighted_v1": 13.5,
                "weighted_v2": 13.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 5.0,
                "weighted_v1": 5.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
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
        "overall_v0": 74.0,
        "overall_v1": 82.25,
        "overall_v2": 83.25,
        "v1_vs_v0_abs": 8.25,
        "v1_vs_v0_pct": 11.15,
        "v2_vs_v1_abs": 1.0,
        "v2_vs_v1_pct": 1.22
    }
