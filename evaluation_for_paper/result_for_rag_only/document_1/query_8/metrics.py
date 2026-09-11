"""
RAG vs Pipeline Metrics -- document_1 / query_8
Query: What is Amazon's outlook and strategic priorities discussed in the 2022 annual report?
"""
from __future__ import annotations
import json

USER_QUERY = "What is Amazon's outlook and strategic priorities discussed in the 2022 annual report?"

RAG_RESPONSE = "\nIn Amazon's 2022 Annual Report, the outlook and strategic priorities highlighted by CEO Andy Jassy reflect a focus on long-term growth and innovation despite facing macroeconomic challenges. Key points include:\n\n1. **Optimism for Future Growth**: Jassy expresses confidence in Amazon's ability to emerge stronger from current economic difficulties, emphasizing the company's commitment to long-term investments that enhance customer experience and operational efficiency.\n\n2. **Investment in Core Businesses**: Amazon plans to continue investing in its major business segments, particularly in improving fulfillment capabilities and reducing costs. This includes optimizing its fulfillment network to enhance delivery speed and efficiency.\n\n3. **Adaptation and Streamlining**: The company has made strategic adjustments, including closing underperforming businesses and roles, to focus resources on initiatives with the highest potential for long-term returns. This includes reevaluating certain programs and prioritizing investments that align with customer needs.\n\n4. **Expansion into New Markets**: Amazon aims to expand its presence in international markets and large retail segments, such as grocery, which represents a significant growth opportunity. The company is also exploring new business areas, including healthcare and satellite internet services.\n\n5. **Technological Innovation**: There is a strong emphasis on leveraging technology and machine learning to enhance customer experiences and operational efficiencies. Investments in AWS and advancements in areas like generative AI and machine learning are prioritized to maintain competitive advantages.\n\n6. **Customer-Centric Approach**: Amazon's strategy remains centered on customer obsession, focusing on selection, price, and convenience to drive sales and enhance customer loyalty.\n\nOverall, Amazon's strategic priorities for 2022 and beyond involve a balanced approach of cost management, innovation, and expansion into new markets while maintaining a strong focus on customer satisfaction.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_1/query_8
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       10 |       90 |       90 |     +80 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       80 |     +10 |      +0 |
| Risk Assessment      |    15% |        0 |       70 |       80 |     +70 |     +10 |
| Actionable Advice    |    15% |        0 |       60 |       65 |     +60 |      +5 |
| Evidence Usage       |    10% |        0 |       80 |       80 |     +80 |      +0 |
| Completeness         |    10% |       60 |       90 |       90 |     +30 |      +0 |
| Query Satisfaction   |    10% |       80 |       90 |      100 |     +10 |     +10 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    27.00 |    80.00 |    83.25 |   +53.0 |   +3.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +53.0 pts  |  +196.30%
  V2 vs V1: +3.25 pts  |  +4.06%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 80,
                "delta_v2_v1": 0,
                "weighted_v0": 2.5,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
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
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 60,
                "v2_score": 65,
                "delta_v1_v0": 60,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.75
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
                "v0_score": 60,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 30,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 90,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 8.0,
                "weighted_v1": 9.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 27.0,
        "overall_v1": 80.0,
        "overall_v2": 83.25,
        "v1_vs_v0_abs": 53.0,
        "v1_vs_v0_pct": 196.3,
        "v2_vs_v1_abs": 3.25,
        "v2_vs_v1_pct": 4.06
    }
