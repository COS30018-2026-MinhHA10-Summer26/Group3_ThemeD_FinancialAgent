"""
Three-Version Evaluation Report — document_5 / query_2
Source document: NASDAQ_TSLA_2022.pdf
Query: How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?"

USER_QUERIES = [
    "What were Tesla's total revenues and net income for fiscal year 2022?",
    "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?",
    "What were the key financial ratios and margins for Tesla in 2022?",
    "How did Tesla's energy generation and storage segment perform in 2022?",
    "What were the main risks Tesla identified in its 2022 annual report?",
    "What were Tesla's capital expenditures and free cash flow in 2022?",
    "How did supply chain challenges impact Tesla's production in 2022?",
    "What is Tesla's growth strategy and future product roadmap as outlined in 2022?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2022, Tesla delivered a total of 1,313,851 vehicles. This represented an increase of 385,000 vehicles compared to 2021, when Tesla delivered 928,000 vehicles.
"""

ADVISOR_REPORT_V1 = """
# Tesla Vehicle Deliveries in 2022 vs. 2021

⚠️ The specific number of vehicles delivered by Tesla in 2022 and 2021 was not found in the available documents. This figure cannot be confirmed without the source filing.

To provide a comprehensive analysis, I recommend checking Tesla's official annual report or investor relations website for the specific delivery numbers for both years. If you have access to additional documents or data, please share them, and I can assist further.
"""

ADVISOR_REPORT_V2 = """
# Tesla Vehicle Deliveries in 2022 vs. 2021

⚠️ The specific number of vehicles delivered by Tesla in 2022 and 2021 was not found in the available documents. This figure cannot be confirmed without the source filing.

To provide a comprehensive analysis, I recommend checking Tesla's official annual report or investor relations website for the specific delivery numbers for both years. If you have access to additional documents or data, please share them, and I can assist further.

## Key Risks Impacting Tesla's Market Position

1. **Competition**: The automotive industry is highly competitive, with numerous players vying for market share in the electric vehicle segment. Tesla must continuously innovate and improve its offerings to maintain its competitive edge.

2. **Valuation**: Changes in consumer demand for electric vehicles and overall market conditions can significantly impact Tesla's valuation. Investors should monitor these factors closely.

3. **Supply Chain**: Tesla's reliance on global suppliers exposes it to potential disruptions. Issues such as semiconductor shortages and other supply chain challenges could affect production and delivery timelines.

4. **Regulation**: Regulatory changes affecting electric vehicles, including emissions standards and incentives, could pose risks to Tesla's operations and market strategy.

5. **Margin Pressure**: Rising costs, including inflation and increased material prices, could impact Tesla's profit margins. The company must manage these costs effectively to sustain profitability.

## Conclusion

The absence of specific delivery numbers for 2022 and 2021 limits the analysis of Tesla's performance. It is crucial to obtain these figures to evaluate the company's growth trajectory and market position accurately. Additionally, understanding the risks outlined above will provide a clearer picture of the challenges Tesla faces in the evolving automotive landscape.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's vehicle deliveries in 2022 and provides a comparison to 2021. However, it lacks proper grounding in the provided context documents and does not include necessary structural elements.

## Query Satisfaction
The response directly addresses the user's question by stating that Tesla delivered 1,313,851 vehicles in 2022, which is an increase of 385,000 vehicles compared to the 928,000 vehicles delivered in 2021. This satisfies the user's request for both the delivery numbers and the year-over-year comparison.

## Remaining Gaps
1. **Lack of Source Citation**: The response does not cite any of the context documents, which is essential for verifying the accuracy of the information provided.
2. **Missing Limitations or Caveats**: There are no disclaimers or notes regarding the data, which could be important for understanding the context of the figures.
3. **No Actionable Content**: The response does not provide any additional insights or recommendations based on the data presented.
4. **Structural Elements**: The response lacks structured sections that could enhance clarity and readability.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the figures provided.
- Add any necessary limitations or caveats regarding the data.
- Consider providing additional insights or implications of the delivery numbers.
- Structure the response into clear sections for better readability.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) does not adequately answer the original user query regarding Tesla's vehicle deliveries in 2022 and how they compare to 2021. While it addresses some key risks and provides a structured analysis, it fails to include the specific delivery numbers that were essential to the user's request.

## Query Satisfaction
The report does not satisfy the query as it explicitly states that the specific number of vehicles delivered by Tesla in 2022 and 2021 was not found in the available documents. This omission is critical since the user specifically asked for these figures.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved Issues**:
  1. Addressed competition, valuation, supply chain, regulation, and margin pressure risks.
  2. Provided contextual analysis of delivery numbers and risks on Tesla's market position.
  3. Incorporated a structured approach to the report.

- **Unresolved Issue**:
  1. The report still lacks relevant figures or charts to support the analysis.

## Remaining Gaps
1. Include relevant figures or charts to support the analysis of Tesla's vehicle deliveries and market position.

## Recommendation
The advisor should revise the report to include the specific vehicle delivery numbers for 2022 and 2021, as well as relevant visual data representations. This will enhance the report's credibility and provide a comprehensive analysis that meets the user's original query.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_2
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |       50 |    +50 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       50 |       70 |    +20 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     5.00 |    25.00 |  +20.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +20.0 pts absolute  |  +400.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_5/query_2
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |      100 |        0 |        0 |   -100 |     +0 |   -100 |
| Business Analysis    |    15%  |        0 |        0 |       50 |     +0 |    +50 |    +50 |
| Risk Assessment      |    15%  |        0 |        0 |       70 |     +0 |    +70 |    +70 |
| Actionable Advice    |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Completeness         |    10%  |        0 |       50 |       70 |    +50 |    +20 |    +70 |
| Query Satisfaction   |    10%  |      100 |        0 |        0 |   -100 |     +0 |   -100 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    35.00 |     5.00 |    25.00 |    -30 |    +20 |    -10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -10 pts absolute  |  -28.57% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 100,
                "weighted_v0": 25.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -100,
                "delta_v1_v2": 0,
                "delta_v0_v2": -100,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v0_v1": 0,
                "delta_v1_v2": 50,
                "delta_v0_v2": 50,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": 0,
                "delta_v1_v2": 70,
                "delta_v0_v2": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v0_v1": 50,
                "delta_v1_v2": 20,
                "delta_v0_v2": 70,
                "weighted_v1": 5.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "weighted_v0": 10.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -100,
                "delta_v1_v2": 0,
                "delta_v0_v2": -100,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            }
        },
        "overall_v0": 35.0,
        "overall_v1": 5.0,
        "overall_v2": 25.0,
        "improvement_v0_to_v1": -30.0,
        "improvement_v1_to_v2": 20.0,
        "improvement_v0_to_v2": -10.0,
        "improvement_pct_v0_to_v2": -28.57
    }
