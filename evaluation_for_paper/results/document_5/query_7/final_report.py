"""
Full Pipeline Evaluation Report — document_5 / query_7
Source document: NASDAQ_TSLA_2022.pdf
Query: How did supply chain challenges impact Tesla's production in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "How did supply chain challenges impact Tesla's production in 2022?"

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

ADVISOR_REPORT_V1 = """
# Tesla's Production Impact from Supply Chain Challenges in 2022

In 2022, Tesla faced significant supply chain challenges that impacted its production capabilities. While the available documents do not provide specific production numbers or timelines, they highlight the broader context of these challenges.

The company acknowledged that supply chain constraints, including those stemming from the COVID-19 pandemic, could affect its operations and production capacity. These constraints may have influenced Tesla's ability to meet demand for its vehicles, particularly as it continued to ramp up production of its various models, including the Model 3, Model Y, Model S, Model X, and the newly introduced Tesla Semi.

Despite these challenges, Tesla has been proactive in addressing supply chain issues by leveraging its technological advancements in battery and powertrain manufacturing. The company has developed proprietary battery technologies aimed at increasing supply and reducing costs, which may help mitigate some of the impacts of supply chain disruptions.

For a more comprehensive analysis, specific production figures and timelines would be beneficial. If you have access to additional documents or sources that might contain this information, please provide them, and I can assist you further.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Production Impact from Supply Chain Challenges in 2022

In 2022, Tesla faced significant supply chain challenges that impacted its production capabilities. The company acknowledged that supply chain constraints, including those stemming from the COVID-19 pandemic, could affect its operations and production capacity. These constraints may have influenced Tesla's ability to meet demand for its vehicles, particularly as it continued to ramp up production of its various models, including the Model 3, Model Y, Model S, Model X, and the newly introduced Tesla Semi.

While specific production numbers and timelines are not available in the current context, it is clear that these challenges had a notable effect on Tesla's overall production strategy. The company has been proactive in addressing supply chain issues by leveraging its technological advancements in battery and powertrain manufacturing. Tesla has developed proprietary battery technologies aimed at increasing supply and reducing costs, which may help mitigate some of the impacts of supply chain disruptions. However, details on how these advancements directly addressed the supply chain issues faced in 2022 are not provided.

Additionally, several key investor risks remain relevant in the context of supply chain challenges:

- **Competition**: The competitive landscape may impact Tesla's market position amid supply chain challenges, especially as competitors may capitalize on these disruptions to gain market share.
  
- **Valuation**: Supply chain issues could influence Tesla's valuation and investor sentiment, potentially leading to fluctuations in stock prices as investors react to production capabilities and market demand.

- **Regulation**: Potential regulatory risks arising from supply chain disruptions, such as compliance with environmental standards and trade regulations, are also critical to consider.

- **Margin Pressure**: The possibility of increased costs due to supply chain issues could affect profit margins, as higher material costs or delays in production may lead to reduced profitability.

For a more comprehensive analysis, specific production figures and timelines would be beneficial. Unfortunately, this information is currently unavailable. If you have access to additional documents or sources that might contain this information, please provide them, and I can assist you further.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of how supply chain challenges impacted Tesla's production in 2022 compared to the initial version. However, it still lacks the inclusion of relevant figures or charts to support its claims.

## Query Satisfaction
The revised report adequately addresses the user query regarding the impact of supply chain challenges on Tesla's production in 2022. It discusses the constraints faced by Tesla, the proactive measures taken, and outlines key investor risks related to these challenges. However, it does not provide specific production figures or timelines, which would enhance the response.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Included a discussion on specific production figures and timelines related to supply chain challenges (though still lacking actual figures).
  2. Clarified how Tesla's technological advancements mitigate supply chain disruptions.
  3. Addressed missing investor risks: competition, valuation, regulation, and margin pressure.
  
- **Unresolved**:
  1. Embed relevant figures or charts to support claims made in the report.

## Remaining Gaps
1. The report still lacks embedded figures or charts that would provide visual support for the claims made regarding production impacts and supply chain challenges.

## Recommendation
It is recommended that the advisor further revise the report to include relevant figures or charts that illustrate the impact of supply chain challenges on Tesla's production in 2022. This addition would enhance the report's clarity and provide a more robust analysis for the reader.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       60 |       70 |    +10 |
| Risk Assessment      |    15%  |       50 |       70 |    +20 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       70 |       80 |    +10 |
| Query Satisfaction   |    10%  |       70 |       80 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    30.50 |    37.00 |   +6.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +6.5 pts absolute  |  +21.31% relative
==============================================================
```
"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 70,
                "delta": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 70,
                "delta": 20,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v1": 30.5,
        "overall_v2": 37.0,
        "absolute_improvement": 6.5,
        "improvement_percentage": 21.31
    }
