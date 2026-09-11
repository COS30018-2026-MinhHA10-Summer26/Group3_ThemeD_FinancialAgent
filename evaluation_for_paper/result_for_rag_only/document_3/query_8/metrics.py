"""
RAG vs Pipeline Metrics -- document_3 / query_8
Query: What AI and cloud strategy shifts did Amazon announce or execute in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "What AI and cloud strategy shifts did Amazon announce or execute in 2024?"

RAG_RESPONSE = "\nIn 2024, Amazon announced and executed several significant shifts in its AI and cloud strategy:\n\n1. **Launch of New AI Services**: AWS introduced a range of new infrastructure and AI services aimed at enhancing customer experiences. This included the release of custom AI silicon (Trainium2), a new set of frontier foundation models under the Amazon Nova initiative, and substantial expansions in the capabilities of its Generative AI services, specifically Amazon SageMaker and Amazon Bedrock.\n\n2. **Investment in AI Development**: Amazon is aggressively investing in AI, with over 1,000 Generative AI applications being developed across the company. This investment is aimed at transforming customer experiences in various sectors, including shopping, coding, personal assistants, streaming video and music, advertising, healthcare, and more.\n\n3. **Custom AI Chips**: The introduction of the Trainium2 chips is a key part of Amazon's strategy to improve price-performance for AI workloads, particularly for training and inference tasks. These chips are designed to reduce the costs associated with AI processing.\n\n4. **Focus on Cost Efficiency**: Amazon is working to make AI more accessible by reducing the costs associated with AI inference, which is expected to become a significant part of future AI spending. This includes advancements in model distillation, prompt caching, and improvements in computing infrastructure.\n\n5. **Expansion of AWS Capabilities**: AWS is rapidly developing foundational building blocks for AI development, which includes flexible model-building and inference services. This strategic focus is intended to position AWS as a leader in the AI cloud services market.\n\nOverall, Amazon's 2024 strategy reflects a deep commitment to integrating AI into its offerings and enhancing its cloud capabilities to meet growing demand in this area.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_3/query_8
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |        0 |      100 |      100 |    +100 |      +0 |
| Business Analysis    |    15% |       70 |       80 |       80 |     +10 |      +0 |
| Risk Assessment      |    15% |        0 |       70 |       80 |     +70 |     +10 |
| Actionable Advice    |    15% |        0 |       75 |       80 |     +75 |      +5 |
| Evidence Usage       |    10% |        0 |       90 |       90 |     +90 |      +0 |
| Completeness         |    10% |       50 |      100 |      100 |     +50 |      +0 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    24.50 |    87.75 |    90.00 |  +63.25 |   +2.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +63.25 pts  |  +258.16%
  V2 vs V1: +2.25 pts  |  +2.56%
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 100,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
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
                "v1_score": 75,
                "v2_score": 80,
                "delta_v1_v0": 75,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 11.25,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 90,
                "delta_v2_v1": 0,
                "weighted_v0": 0.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 50,
                "delta_v2_v1": 0,
                "weighted_v0": 5.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
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
        "overall_v0": 24.5,
        "overall_v1": 87.75,
        "overall_v2": 90.0,
        "v1_vs_v0_abs": 63.25,
        "v1_vs_v0_pct": 258.16,
        "v2_vs_v1_abs": 2.25,
        "v2_vs_v1_pct": 2.56
    }
