"""
RAG vs Pipeline Metrics -- document_4 / query_2
Query: How did Amazon's AWS segment grow in 2025 and what products drove demand?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's AWS segment grow in 2025 and what products drove demand?"

RAG_RESPONSE = "\nIn 2025, Amazon's AWS segment experienced significant growth, with revenue increasing by 20% year-over-year, rising from $108 billion to $129 billion. This growth was primarily driven by increased customer usage and demand for AWS services, particularly in the areas of artificial intelligence (AI) and machine learning.\n\nKey products that drove demand included:\n1. **Amazon SageMaker** - A service for building, training, and deploying machine learning models.\n2. **Amazon Bedrock** - An AI service that allows customers to build and scale generative AI applications.\n3. **Custom AI silicon (Trainium and Graviton)** - AWS's proprietary chips that offer better price-performance for AI workloads, with Trainium2 and Trainium3 being particularly popular among customers.\n\nAdditionally, AWS's operating income also improved, reaching $45.6 billion, reflecting the segment's robust performance amidst ongoing investments in technology infrastructure to support growth.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_4/query_2
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |      100 |      100 |     +10 |      +0 |
| Business Analysis    |    15% |       70 |       70 |       70 |      +0 |      +0 |
| Risk Assessment      |    15% |       50 |       50 |       55 |      +0 |      +5 |
| Actionable Advice    |    15% |       40 |       50 |       60 |     +10 |     +10 |
| Evidence Usage       |    10% |       60 |       60 |       60 |      +0 |      +0 |
| Completeness         |    10% |       80 |       80 |       80 |      +0 |      +0 |
| Query Satisfaction   |    10% |       90 |       90 |       90 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    69.50 |    73.50 |    75.75 |    +4.0 |   +2.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +4.0 pts  |  +5.76%
  V2 vs V1: +2.25 pts  |  +3.06%
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
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 10.5,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "v1_score": 50,
                "v2_score": 55,
                "delta_v1_v0": 0,
                "delta_v2_v1": 5,
                "weighted_v0": 7.5,
                "weighted_v1": 7.5,
                "weighted_v2": 8.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 10,
                "delta_v2_v1": 10,
                "weighted_v0": 6.0,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 6.0,
                "weighted_v1": 6.0,
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
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 69.5,
        "overall_v1": 73.5,
        "overall_v2": 75.75,
        "v1_vs_v0_abs": 4.0,
        "v1_vs_v0_pct": 5.76,
        "v2_vs_v1_abs": 2.25,
        "v2_vs_v1_pct": 3.06
    }
