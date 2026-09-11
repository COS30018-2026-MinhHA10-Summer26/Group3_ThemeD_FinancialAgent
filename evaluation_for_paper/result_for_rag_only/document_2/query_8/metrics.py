"""
RAG vs Pipeline Metrics -- document_2 / query_8
Query: What generative AI and technology investments did Amazon highlight in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What generative AI and technology investments did Amazon highlight in 2023?"

RAG_RESPONSE = "\nIn 2023, Amazon highlighted several significant investments in generative AI and technology:\n\n1. **AWS Trainium2 Chips**: Amazon announced the launch of AWS Trainium2 chips, which are designed to deliver up to four times faster machine learning training specifically for generative AI applications, along with three times more memory capacity than its predecessor, Trainium1.\n\n2. **Amazon SageMaker Enhancements**: The company added numerous features to Amazon SageMaker, making it easier for developers to build new Foundation Models (FMs). This service is aimed at facilitating the development and deployment of AI applications.\n\n3. **Amazon Bedrock**: This new service allows companies to leverage existing Foundation Models to build generative AI applications. Bedrock has seen significant traction, with tens of thousands of active customers shortly after its launch.\n\n4. **Amazon Q**: Amazon introduced Amazon Q, described as a highly capable coding assistant, which is part of its broader generative AI offerings.\n\n5. **Investment in AI Chips**: Amazon is pushing the envelope on price-performance for AI chips, having developed custom AI training chips (Trainium) and inference chips (Inferentia) to enhance its capabilities in generative AI.\n\nThese initiatives reflect Amazon's commitment to advancing its generative AI capabilities and providing robust tools for developers and businesses to create AI-driven applications.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_2/query_8
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       30 |      100 |      100 |     +70 |      +0 |
| Business Analysis    |    15% |        0 |       80 |       85 |     +80 |      +5 |
| Risk Assessment      |    15% |       20 |       70 |       80 |     +50 |     +10 |
| Actionable Advice    |    15% |        0 |       60 |       65 |     +60 |      +5 |
| Evidence Usage       |    10% |       50 |       80 |       85 |     +30 |      +5 |
| Completeness         |    10% |        0 |      100 |      100 |    +100 |      +0 |
| Query Satisfaction   |    10% |      100 |      100 |      100 |      +0 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    25.50 |    84.50 |    88.00 |   +59.0 |    +3.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +59.0 pts  |  +231.37%
  V2 vs V1: +3.5 pts  |  +4.14%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 30,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 70,
                "delta_v2_v1": 0,
                "weighted_v0": 7.5,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 80,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 20,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 50,
                "delta_v2_v1": 10,
                "weighted_v0": 3.0,
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
                "v0_score": 50,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v1_v0": 30,
                "delta_v2_v1": 5,
                "weighted_v0": 5.0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 100,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 10.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 25.5,
        "overall_v1": 84.5,
        "overall_v2": 88.0,
        "v1_vs_v0_abs": 59.0,
        "v1_vs_v0_pct": 231.37,
        "v2_vs_v1_abs": 3.5,
        "v2_vs_v1_pct": 4.14
    }
