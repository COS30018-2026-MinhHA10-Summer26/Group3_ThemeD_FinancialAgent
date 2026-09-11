"""
RAG vs Pipeline Metrics -- document_2 / query_3
Query: What cost optimization measures did Amazon undertake in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What cost optimization measures did Amazon undertake in 2023?"

RAG_RESPONSE = "\nIn 2023, Amazon implemented several cost optimization measures that contributed to significant improvements in its financial performance. Key measures included:\n\n1. **Reduction in Cost to Serve**: Amazon successfully reduced its cost to serve on a per unit basis globally for the first time since 2018, with a notable decrease of more than $0.45 per unit in the U.S. This reduction was achieved through regionalization efforts that trimmed transportation distances, allowing for lower operational costs.\n\n2. **Operational Efficiency**: The company challenged existing beliefs about its fulfillment network and reevaluated various components to identify further cost-saving opportunities. This included focusing on inbound fulfillment architecture and inventory placement, which are expected to yield additional savings in the future.\n\n3. **Investment in Technology**: Amazon continued to invest in technology and infrastructure, which helped improve operational efficiencies. For instance, the use of AWS capabilities like Graviton chips and intelligent storage solutions contributed to cost savings for both Amazon and its customers.\n\n4. **Improved Delivery Speeds**: By optimizing its logistics and fulfillment processes, Amazon was able to enhance delivery speeds, which not only improved customer satisfaction but also contributed to operational efficiencies.\n\n5. **Increased Revenue from Advertising and Other Services**: The company saw strong growth in its advertising segment, which grew 24% year-over-year, indicating a successful strategy to leverage its platform for additional revenue streams.\n\nThese measures collectively contributed to a dramatic improvement in Amazon's operating income, which increased by 201% year-over-year, and a significant turnaround in free cash flow, which improved from -$12.8 billion in 2022 to $35.5 billion in 2023.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_2/query_3
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       85 |     +10 |      +5 |
| Risk Assessment      |    15% |       50 |       70 |       80 |     +20 |     +10 |
| Actionable Advice    |    15% |       60 |       75 |       80 |     +15 |      +5 |
| Evidence Usage       |    10% |       70 |       70 |       80 |      +0 |     +10 |
| Completeness         |    10% |       80 |       85 |       90 |      +5 |      +5 |
| Query Satisfaction   |    10% |       90 |       90 |       90 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    73.50 |    80.75 |    85.25 |   +7.25 |    +4.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +7.25 pts  |  +9.86%
  V2 vs V1: +4.5 pts  |  +5.57%
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
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 22.5,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 10,
                "delta_v2_v1": 5,
                "weighted_v0": 10.5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 10,
                "weighted_v0": 7.5,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 60,
                "v1_score": 75,
                "v2_score": 80,
                "delta_v1_v0": 15,
                "delta_v2_v1": 5,
                "weighted_v0": 9.0,
                "weighted_v1": 11.25,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 7.0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 85,
                "v2_score": 90,
                "delta_v1_v0": 5,
                "delta_v2_v1": 5,
                "weighted_v0": 8.0,
                "weighted_v1": 8.5,
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
        "overall_v0": 73.5,
        "overall_v1": 80.75,
        "overall_v2": 85.25,
        "v1_vs_v0_abs": 7.25,
        "v1_vs_v0_pct": 9.86,
        "v2_vs_v1_abs": 4.5,
        "v2_vs_v1_pct": 5.57
    }
