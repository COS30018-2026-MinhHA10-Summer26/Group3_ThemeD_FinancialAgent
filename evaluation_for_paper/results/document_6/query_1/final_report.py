"""
Full Pipeline Evaluation Report — document_6 / query_1
Source document: NASDAQ_TSLA_2023.pdf
Query: What were Tesla's total revenues and operating income for fiscal year 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's total revenues and operating income for fiscal year 2023?"

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

ADVISOR_REPORT_V1 = """
# Tesla 2023 Financial Overview

## Total Revenues and Operating Income
Unfortunately, Tesla's total revenues and operating income for fiscal year 2023 are not available in the provided documents. This information cannot be confirmed without access to the relevant financial statements. If you have access to Tesla's financial statements or can provide additional context, please share them so I can assist you further in retrieving the specific figures you are looking for.

## Financial Health
As the specific financial figures for 2023 are unavailable, a comprehensive assessment of Tesla's financial health cannot be conducted. However, it is essential to monitor key metrics such as revenue growth, profit margins, and cash flow in future reports.

## Future Outlook
Without the latest financial data, it is challenging to provide a detailed future outlook. Generally, Tesla's growth trajectory has been influenced by factors such as market demand for electric vehicles, production capacity, and competition. Keeping an eye on these elements will be crucial for understanding Tesla's potential performance in the coming years.

## Risks and Limitations
1. **Market Competition**: The electric vehicle market is becoming increasingly competitive, with traditional automakers and new entrants vying for market share.
2. **Supply Chain Issues**: Disruptions in the supply chain can impact production and delivery timelines.
3. **Regulatory Changes**: Changes in government policies regarding electric vehicles and renewable energy can affect Tesla's operations and profitability.

## Actionable Advice
- **Stay Informed**: Keep track of Tesla's quarterly earnings reports and other financial disclosures to gain insights into its performance.
- **Diversification**: Consider diversifying investments to mitigate risks associated with Tesla's stock volatility.
- **Monitor Industry Trends**: Pay attention to trends in the electric vehicle market and technological advancements that could impact Tesla's business model.
"""

ADVISOR_REPORT_V2 = """
# Tesla 2023 Financial Overview

## Total Revenues and Operating Income
Unfortunately, Tesla's total revenues and operating income for fiscal year 2023 are not available in the provided documents. This information cannot be confirmed without access to the relevant financial statements. For the most accurate figures, I recommend checking Tesla's official financial statements or their SEC filings.

## Financial Health
In the absence of specific financial figures for 2023, a comprehensive assessment of Tesla's financial health cannot be conducted. However, investors can monitor key metrics such as:
- **Gross Margin**: Indicates profitability relative to sales.
- **Cash Flow**: Essential for understanding liquidity and operational efficiency.
- **Debt Levels**: Important for assessing financial stability.

## Future Outlook
Without the latest financial data, it is challenging to provide a detailed future outlook. Generally, Tesla's growth trajectory has been influenced by factors such as:
- **Market Demand**: Increasing interest in electric vehicles.
- **Production Capacity**: Ability to meet consumer demand.
- **Competition**: The presence of both traditional automakers and new entrants in the electric vehicle market.

Keeping an eye on these elements will be crucial for understanding Tesla's potential performance in the coming years.

## Risks and Limitations
1. **Market Competition**: The electric vehicle market is becoming increasingly competitive, with traditional automakers and new entrants vying for market share.
2. **Supply Chain Issues**: Disruptions in the supply chain can impact production and delivery timelines.
3. **Regulatory Changes**: Changes in government policies regarding electric vehicles and renewable energy can affect Tesla's operations and profitability.
4. **Valuation Risk**: Given the current market dynamics, fluctuations in Tesla's stock price may not accurately reflect its underlying value.
5. **Macroeconomic Factors**: Inflation and interest rates can impact consumer purchasing power and overall market conditions.

## Actionable Advice
- **Stay Informed**: Keep track of Tesla's quarterly earnings reports and other financial disclosures to gain insights into its performance.
- **Diversification**: Consider diversifying investments to mitigate risks associated with Tesla's stock volatility.
- **Monitor Industry Trends**: Pay attention to trends in the electric vehicle market and technological advancements that could impact Tesla's business model.

In summary, while the lack of specific financial data for 2023 limits the depth of this analysis, monitoring alternative metrics and understanding the broader market context will be essential for making informed investment decisions regarding Tesla.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Tesla's financial situation for fiscal year 2023, but it still lacks specific financial figures for total revenues and operating income. While several issues identified in the Critic's report have been addressed, one critical issue remains unresolved.

## Query Satisfaction
The report does not adequately answer the original user query regarding Tesla's total revenues and operating income for fiscal year 2023. The advisor states that this information is unavailable and suggests checking Tesla's official financial statements or SEC filings, which does not fulfill the user's request for specific figures.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues:**
  - Provided alternative metrics for assessing Tesla's financial health.
  - Included the risk of valuation in the report.
  - Considered macroeconomic factors affecting Tesla's performance.
  - Suggested monitoring key metrics such as gross margin, cash flow, and debt levels.

- **Unresolved Issue:**
  - **Incorporate figures or visualizations to support claims.**

## Remaining Gaps
1. The report still lacks specific financial figures for total revenues and operating income for 2023 or alternative sources for this information.
2. The report does not include any figures or visualizations to support its claims, which could enhance understanding and provide a clearer picture of Tesla's financial situation.

## Recommendation
The advisor should revise the report to include specific financial figures for Tesla's total revenues and operating income for fiscal year 2023, if available, or provide alternative sources for this information. Additionally, incorporating figures or visualizations to support claims would significantly improve the report's clarity and utility for investors.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_6/query_1
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       60 |       60 |     +0 |
| Risk Assessment      |    15%  |       70 |       70 |     +0 |
| Actionable Advice    |    15%  |       70 |       70 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    40.00 |    40.00 |   +0.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +0.0 pts absolute  |  +0.0% relative
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
                "v2_score": 60,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 70,
                "delta": 0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 70,
                "delta": 0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
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
                "v1_score": 100,
                "v2_score": 100,
                "delta": 0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            }
        },
        "overall_v1": 40.0,
        "overall_v2": 40.0,
        "absolute_improvement": 0.0,
        "improvement_percentage": 0.0
    }
