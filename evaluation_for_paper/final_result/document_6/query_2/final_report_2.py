"""
Three-Version Evaluation Report — document_6 / query_2
Source document: NASDAQ_TSLA_2023.pdf
Query: How did Tesla's vehicle average selling price and gross margin trend in 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's vehicle average selling price and gross margin trend in 2023?"

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
In 2023, Tesla's average selling price for vehicles decreased due to overall price reductions and a shift in sales mix, which negatively impacted gross margins. Specifically, the gross margin for total automotive sales fell from 28.5% in 2022 to 19.4% in 2023. This decline was attributed to a lower average selling price, despite some cost reductions and benefits from IRA manufacturing credits. Overall, while Tesla's revenues increased, the gross margin trends indicate challenges in maintaining profitability amidst pricing pressures.
"""

ADVISOR_REPORT_V1 = """
# Tesla's Vehicle Average Selling Price and Gross Margin Trend in 2023

Unfortunately, Tesla's vehicle average selling price and gross margin for 2023 were not found in the available documents. This information is crucial for analyzing the trends, and without it, we cannot provide a definitive answer regarding the performance in these areas.

## Financial Health and Future Outlook

While specific figures for the average selling price and gross margin are missing, Tesla's overall financial health can be inferred from its market capitalization, which was reported at **$722.52 billion** as of June 30, 2023. This substantial market value suggests strong investor confidence and a robust business model.

### Risks and Limitations

1. **Market Competition**: Tesla faces increasing competition from both established automakers and new entrants in the electric vehicle market, which could impact pricing strategies and margins.
2. **Supply Chain Issues**: Ongoing supply chain disruptions could affect production costs and timelines, potentially impacting gross margins.
3. **Regulatory Changes**: Changes in government policies regarding electric vehicles and emissions could influence market dynamics and operational costs.

## Actionable Insights

- **Monitor Competitor Pricing**: Keeping an eye on competitor pricing strategies will be essential for Tesla to maintain its market position.
- **Focus on Cost Management**: Enhancing operational efficiency and managing production costs can help protect gross margins.
- **Invest in Innovation**: Continued investment in technology and innovation will be crucial for maintaining a competitive edge in the rapidly evolving EV market.

## Conclusion

To analyze the trends in Tesla's vehicle average selling price and gross margin for 2023 accurately, we recommend obtaining the relevant financial data or documents that include these metrics. If you have access to additional sources or specific reports, please share them for a more comprehensive analysis.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Vehicle Average Selling Price and Gross Margin Trend in 2023

Unfortunately, Tesla's vehicle average selling price and gross margin for 2023 were not found in the available documents. This information is crucial for analyzing the trends, and without it, we cannot provide a definitive answer regarding the performance in these areas.

## Financial Health and Future Outlook

While specific figures for the average selling price and gross margin are missing, Tesla's overall financial health can be inferred from its market capitalization, which was reported at **$722.52 billion** as of June 30, 2023. This substantial market value suggests strong investor confidence and a robust business model.

### Market Capitalization

| Metric                  | Value            |
|-------------------------|------------------|
| Market Capitalization    | $722.52 billion   |

*Source: NASDAQ_TSLA_2023.pdf (Page 3)*

### Risks and Limitations

1. **Market Competition**: Tesla faces increasing competition from both established automakers and new entrants in the electric vehicle market, which could impact pricing strategies and margins.
2. **Supply Chain Issues**: Ongoing supply chain disruptions could affect production costs and timelines, potentially impacting gross margins.
3. **Regulatory Changes**: Changes in government policies regarding electric vehicles and emissions could influence market dynamics and operational costs.

## Actionable Insights

- **Monitor Competitor Pricing**: Keeping an eye on competitor pricing strategies will be essential for Tesla to maintain its market position.
- **Focus on Cost Management**: Enhancing operational efficiency and managing production costs can help protect gross margins.
- **Invest in Innovation**: Continued investment in technology and innovation will be crucial for maintaining a competitive edge in the rapidly evolving EV market.

## Conclusion

To analyze the trends in Tesla's vehicle average selling price and gross margin for 2023 accurately, we recommend referencing the **Management's Discussion and Analysis of Financial Condition and Results of Operations** section in the annual report (Item 7) for detailed financial metrics. If you have access to additional sources or specific reports, please share them for a more comprehensive analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Tesla's vehicle average selling price and gross margin trends in 2023. However, it lacks grounding in the provided context documents and is missing several structural elements that would enhance its quality.

## Query Satisfaction
The response provides a clear answer to the user's question about the trends in Tesla's vehicle average selling price and gross margin for 2023. It mentions the decrease in average selling price and the corresponding decline in gross margin, which aligns with the user's inquiry.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not reference any specific documents or data points from the provided context, which diminishes its credibility.
2. **Missing Limitations or Caveats**: There are no disclaimers or notes regarding the potential variability in financial data or external factors affecting the results.
3. **Absence of Actionable Content**: The response does not provide any recommendations or next steps for the user, which could enhance its usefulness.
4. **No Structured Sections**: The response lacks a clear structure, such as headings or bullet points, which would make it easier to read and understand.

## Recommendation
To improve the response, it should:
- Include specific citations from the context documents to support the claims made about the average selling price and gross margin.
- Add limitations or caveats regarding the financial data presented.
- Provide actionable insights or recommendations for the user.
- Structure the response with clear sections or bullet points for better readability. 

Incorporating these elements will enhance the quality and reliability of the response, making it more informative for the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) does not adequately address the original user query regarding Tesla's vehicle average selling price and gross margin trend in 2023. While it provides some context and insights, it still lacks the critical data requested.

## Query Satisfaction
The report fails to answer the user query directly, as it states that the average selling price and gross margin for 2023 were not found in the available documents. Although it discusses Tesla's financial health and market capitalization, it does not provide the specific metrics requested, which undermines its effectiveness in addressing the query.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Included Tesla's market capitalization figure with a source citation.
  2. Expanded on the analysis of risks related to pricing and margins.
  3. Addressed the need for actionable insights.

- **Unresolved**:
  1. The report still does not include visual representations of data trends where applicable.

## Remaining Gaps
- The report lacks visual aids or figures to illustrate trends, which would enhance understanding and engagement.

## Recommendation
To improve the report, the advisor should:
1. Include visual representations of Tesla's average selling price and gross margin trends for 2023, if available.
2. Ensure that the report directly addresses the user query with the necessary data to provide a comprehensive analysis.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_6/query_2
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       60 |       60 |     +0 |
| Risk Assessment      |    15%  |       70 |       70 |     +0 |
| Actionable Advice    |    15%  |       60 |       60 |     +0 |
| Evidence Usage       |    10%  |        0 |       10 |    +10 |
| Completeness         |    10%  |       80 |       80 |     +0 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    36.50 |    37.50 |   +1.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +1.0 pts absolute  |  +2.74% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_6/query_2
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
| Business Analysis    |    15%  |       70 |       60 |       60 |    -10 |     +0 |    -10 |
| Risk Assessment      |    15%  |       60 |       70 |       70 |    +10 |     +0 |    +10 |
| Actionable Advice    |    15%  |       50 |       60 |       60 |    +10 |     +0 |    +10 |
| Evidence Usage       |    10%  |       40 |        0 |       10 |    -40 |    +10 |    -30 |
| Completeness         |    10%  |       70 |       80 |       80 |    +10 |     +0 |    +10 |
| Query Satisfaction   |    10%  |       80 |        0 |        0 |    -80 |     +0 |    -80 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    68.50 |    36.50 |    37.50 |    -32 |     +1 |    -31 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -31 pts absolute  |  -45.26% relative
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
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": -10,
                "delta_v1_v2": 0,
                "delta_v0_v2": -10,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "weighted_v0": 4.0,
                "v1_score": 0,
                "v2_score": 10,
                "delta_v0_v1": -40,
                "delta_v1_v2": 10,
                "delta_v0_v2": -30,
                "weighted_v1": 0.0,
                "weighted_v2": 1.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -80,
                "delta_v1_v2": 0,
                "delta_v0_v2": -80,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            }
        },
        "overall_v0": 68.5,
        "overall_v1": 36.5,
        "overall_v2": 37.5,
        "improvement_v0_to_v1": -32.0,
        "improvement_v1_to_v2": 1.0,
        "improvement_v0_to_v2": -31.0,
        "improvement_pct_v0_to_v2": -45.26
    }
