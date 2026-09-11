"""
RAG vs Pipeline Metrics -- document_3 / query_5
Query: What were Amazon's major capital allocation decisions in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's major capital allocation decisions in 2024?"

RAG_RESPONSE = "\nIn 2024, Amazon made several significant capital allocation decisions, primarily focused on expanding its technology infrastructure and enhancing customer experiences. Key decisions included:\n\n1. **Investment in Technology and Infrastructure**: Amazon significantly increased its capital expenditures, spending approximately $77.7 billion in 2024 compared to $48.1 billion in 2023. This investment was primarily directed towards enhancing its technology infrastructure, particularly for Amazon Web Services (AWS), and expanding its fulfillment network to support growth in both retail and cloud services.\n\n2. **Acquisitions**: Amazon engaged in acquisition activities totaling $780 million in 2024, aimed at acquiring technologies and know-how to better serve customers and expand its customer base. This included ongoing investments in convertible notes from Anthropic, PBC, with a total planned investment of $4.0 billion by the end of 2025.\n\n3. **Focus on Artificial Intelligence**: Amazon aggressively invested in AI technologies, launching new services and infrastructure, including custom AI silicon and expanding its AWS offerings. This strategic focus on AI was seen as a critical area for future growth and customer experience enhancement.\n\n4. **Expansion of Fulfillment Capabilities**: The company continued to invest in its fulfillment network, including the introduction of same-day delivery options and enhancements to its logistics capabilities, particularly in rural areas.\n\n5. **Stock Repurchase Program**: Although there were no stock repurchases in 2023 or 2024, Amazon retained $6.1 billion under its existing stock repurchase program, indicating a potential future commitment to returning capital to shareholders.\n\nOverall, Amazon's capital allocation decisions in 2024 reflected a strong emphasis on long-term growth through technology investments, strategic acquisitions, and enhancing customer service capabilities.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_5
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |       75 |       80 |       80 |      +5 |      +0 |
| Risk Assessment      |    15% |       60 |       70 |       80 |     +10 |     +10 |
| Actionable Advice    |    15% |       50 |       60 |       70 |     +10 |     +10 |
| Evidence Usage       |    10% |       70 |       70 |       70 |      +0 |      +0 |
| Completeness         |    10% |       80 |      100 |      100 |     +20 |      +0 |
| Query Satisfaction   |    10% |       85 |       90 |       90 |      +5 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    73.75 |    82.50 |    85.50 |   +8.75 |    +3.0 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +8.75 pts  |  +11.86%
  V2 vs V1: +3.0 pts  |  +3.64%
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 22.5,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 75,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 11.25,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
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
                "v1_score": 60,
                "v2_score": 70,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 7.5,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
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
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 8.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 85,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 5,
                "delta_v2_v1": 0,
                "weighted_v0": 8.5,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 73.75,
        "overall_v1": 82.5,
        "overall_v2": 85.5,
        "v1_vs_v0_abs": 8.75,
        "v1_vs_v0_pct": 11.86,
        "v2_vs_v1_abs": 3.0,
        "v2_vs_v1_pct": 3.64
    }
