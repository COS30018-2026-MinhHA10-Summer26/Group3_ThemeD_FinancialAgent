"""
Three-Version Evaluation Report — document_6 / query_4
Source document: NASDAQ_TSLA_2023.pdf
Query: How did Tesla's energy storage deployment grow in 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's energy storage deployment grow in 2023?"

USER_QUERIES = [
    "What were Tesla's total revenues and operating income for fiscal year 2023?",
    "How did Tesla's vehicle average selling price and gross margin trend in 2023?",
    "What were Tesla's total vehicle deliveries and production volumes in 2023?",
    "How did Tesla's energy storage deployment grow in 2023?",
    "What cost reduction initiatives did Tesla implement in 2023?",
    "What were the key balance sheet metrics for Tesla at the end of 2023?",
    "What risks related to competition and pricing pressure did Tesla disclose in 2023?",
    "What is Tesla's outlook for new vehicle models and production expansion in 2023?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2023, Tesla's energy storage deployment experienced significant growth, with the company deploying 14.72 GWh of energy storage products. This marked a notable increase compared to previous years, reflecting Tesla's focus on ramping production of energy storage products and improving installation capabilities for its Solar Roof. Additionally, the energy generation and storage segment's revenue increased by 54% year-over-year, primarily driven by the rise in Megapack deployments. Overall, Tesla's efforts to enhance its energy storage offerings contributed to this growth in 2023.
"""

ADVISOR_REPORT_V1 = """
# Tesla's Energy Storage Deployment Growth in 2023

Tesla's energy storage deployment figures for 2023 were not explicitly found in the available documents. The annual report typically includes insights into operational performance, including segments like energy storage, but specific deployment figures are currently unavailable.

To gather more information on Tesla's energy storage growth in 2023, consider the following avenues:

1. **Official Annual Report**: Review Tesla's complete 10-K filing for the fiscal year ended December 31, 2023, which may contain detailed discussions on energy storage performance and growth metrics.

2. **Press Releases**: Check Tesla's official website for press releases that may highlight milestones or achievements in their energy storage segment throughout 2023.

3. **Investor Relations**: Explore the Investor Relations section of Tesla's website, where they often provide updates, presentations, and earnings call transcripts that may discuss energy storage developments.

4. **Industry Reports**: Look for third-party industry analysis or reports that cover Tesla's energy storage market performance, as these may provide insights and comparative data.

If you have access to additional documents or data, please provide them for further analysis.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Energy Storage Deployment Growth in 2023

Tesla's energy storage deployment figures for 2023 were not explicitly found in the available documents. The annual report typically includes insights into operational performance, including segments like energy storage, but specific deployment figures are currently unavailable. Relevant sections that may contain insights into energy storage performance include **Item 7: Management's Discussion and Analysis of Financial Condition and Results of Operations** and **Item 8: Financial Statements and Supplementary Data**.

## Implications of Lack of Data

The absence of specific deployment figures raises concerns regarding Tesla's market position and future growth in the energy storage sector. Without concrete data, it is challenging to assess how Tesla is performing relative to its competitors and whether it is maintaining or expanding its market share. This lack of transparency may lead to investor uncertainty and could impact Tesla's stock performance.

## Importance of Energy Storage Growth

Energy storage is a critical component of Tesla's overall strategy, as it complements its electric vehicle business and supports the transition to renewable energy. Growth in this segment is essential for enhancing Tesla's revenue streams and solidifying its position as a leader in sustainable energy solutions.

## Potential Investor Risks

The lack of deployment data could pose several risks for investors, including:

- **Market Share Loss**: Competitors may capitalize on Tesla's lack of specific data to position themselves more favorably in the market.
- **Supply Chain Issues**: Any delays or challenges in scaling energy storage production could hinder Tesla's growth.
- **Regulatory Changes**: Changes in government policies regarding energy storage could impact Tesla's operations and profitability.
- **Competitive Disadvantages**: Competitors may leverage Tesla's lack of transparency to gain an advantage in marketing and sales.

## Recommendations for Further Information

To gather more information on Tesla's energy storage growth in 2023, consider the following avenues:

1. **Official Annual Report**: Review Tesla's complete 10-K filing for the fiscal year ended December 31, 2023, which may contain detailed discussions on energy storage performance and growth metrics.
   
2. **Press Releases**: Check Tesla's official website for press releases that may highlight milestones or achievements in their energy storage segment throughout 2023.

3. **Investor Relations**: Explore the Investor Relations section of Tesla's website, where they often provide updates, presentations, and earnings call transcripts that may discuss energy storage developments.

4. **Industry Reports**: Look for third-party industry analysis or reports that cover Tesla's energy storage market performance, as these may provide insights and comparative data.

If you have access to additional documents or data, please provide them for further analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Tesla's energy storage deployment growth in 2023, but it lacks grounding in the provided context documents and misses essential structural elements.

## Query Satisfaction
The response answers the user's question by stating that Tesla deployed 14.72 GWh of energy storage products in 2023 and highlights a 54% increase in revenue for the energy generation and storage segment. However, it does not provide specific citations from the context documents to support these claims, which diminishes its reliability.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not reference any of the context documents, which is crucial for validating the information presented.
2. **Missing Actionable Content**: The response does not include any actionable insights or recommendations for the user, which could enhance its utility.
3. **Absence of Structured Sections**: The response lacks a clear structure, such as headings or bullet points, which would improve readability and comprehension.

## Recommendation
To improve the response:
- Include specific citations from the context documents to support the claims made about Tesla's energy storage deployment and revenue growth.
- Add actionable insights or recommendations based on the information provided.
- Structure the response with clear headings or bullet points to enhance clarity and readability.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's energy storage deployment growth in 2023 compared to the original version. However, it still lacks specific deployment figures, which are crucial for a complete assessment.

## Query Satisfaction
The report adequately addresses the user query regarding Tesla's energy storage deployment growth in 2023 by discussing the implications of the lack of specific data, the importance of energy storage growth, and potential investor risks. It also suggests avenues for further information. However, it does not provide the specific deployment figures requested, which limits its effectiveness.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved**:
  - Included an analysis of the implications of the lack of data on Tesla's market position.
  - Discussed the importance of energy storage growth to Tesla's overall strategy.
  - Provided potential investor risks related to the lack of deployment data.
  - Suggested recommendations for further information sources.

- **Unresolved**:
  - The report does not incorporate figures or visualizations to support claims.

## Remaining Gaps
1. **Incorporate figures or visualizations to support claims**: The report should include relevant figures or visualizations that illustrate Tesla's energy storage deployment growth or comparisons with competitors.

## Recommendation
To enhance the report's quality and fully satisfy the user query, it is recommended that the advisor:
- Include specific deployment figures for Tesla's energy storage in 2023, if available.
- Incorporate relevant figures or visualizations to support the claims made in the report. This will provide a clearer context and strengthen the analysis.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_6/query_4
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       50 |       70 |    +20 |
| Risk Assessment      |    15%  |       50 |       70 |    +20 |
| Actionable Advice    |    15%  |       60 |       70 |    +10 |
| Evidence Usage       |    10%  |        0 |       10 |    +10 |
| Completeness         |    10%  |       70 |       80 |    +10 |
| Query Satisfaction   |    10%  |       50 |       70 |    +20 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    36.00 |    47.50 |  +11.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +11.5 pts absolute  |  +31.94% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_6/query_4
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
| Business Analysis    |    15%  |       70 |       50 |       70 |    -20 |    +20 |     +0 |
| Risk Assessment      |    15%  |       50 |       50 |       70 |     +0 |    +20 |    +20 |
| Actionable Advice    |    15%  |       40 |       60 |       70 |    +20 |    +10 |    +30 |
| Evidence Usage       |    10%  |       60 |        0 |       10 |    -60 |    +10 |    -50 |
| Completeness         |    10%  |       80 |       70 |       80 |    -10 |    +10 |     +0 |
| Query Satisfaction   |    10%  |       90 |       50 |       70 |    -40 |    +20 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    69.50 |    36.00 |    47.50 |    -33 |    +11 |    -22 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -22 pts absolute  |  -31.65% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 90,
                "weighted_v0": 22.5,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -90,
                "delta_v1_v2": 0,
                "delta_v0_v2": -90,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v0_v1": -20,
                "delta_v1_v2": 20,
                "delta_v0_v2": 0,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v0_v1": 0,
                "delta_v1_v2": 20,
                "delta_v0_v2": 20,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v0_v1": 20,
                "delta_v1_v2": 10,
                "delta_v0_v2": 30,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 10,
                "delta_v0_v1": -60,
                "delta_v1_v2": 10,
                "delta_v0_v2": -50,
                "weighted_v1": 0.0,
                "weighted_v2": 1.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": -10,
                "delta_v1_v2": 10,
                "delta_v0_v2": 0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v0_v1": -40,
                "delta_v1_v2": 20,
                "delta_v0_v2": -20,
                "weighted_v1": 5.0,
                "weighted_v2": 7.0
            }
        },
        "overall_v0": 69.5,
        "overall_v1": 36.0,
        "overall_v2": 47.5,
        "improvement_v0_to_v1": -33.5,
        "improvement_v1_to_v2": 11.5,
        "improvement_v0_to_v2": -22.0,
        "improvement_pct_v0_to_v2": -31.65
    }
