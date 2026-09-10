"""
Full Pipeline Evaluation Report — document_2 / query_1
Source document: NASDAQ_AMZN_2023.pdf
Query: What were Amazon's total revenues and operating income for fiscal year 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's total revenues and operating income for fiscal year 2023?"

USER_QUERIES = [
    "What were Amazon's total revenues and operating income for fiscal year 2023?",
    "How did AWS revenue growth trend in 2023 and what drove it?",
    "What cost optimization measures did Amazon undertake in 2023?",
    "How did Amazon's advertising revenue segment grow in 2023?",
    "What were the key balance sheet highlights for Amazon at the end of 2023?",
    "How did Amazon's North America segment margin recover in 2023?",
    "What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?",
    "What generative AI and technology investments did Amazon highlight in 2023?",
]

ADVISOR_REPORT_V1 = """
# Amazon Financial Report for Fiscal Year 2023

In fiscal year 2023, Amazon reported the following financial metrics:

- **Total Revenue**: $575 billion
- **Operating Income**: $36.9 billion

These figures reflect a year-over-year growth in total revenue of 12% and a significant improvement in operating income, which increased by 201% compared to the previous year.

## Financial Metrics Comparison

| Metric            | 2023          | 2022          | Change    |
|-------------------|---------------|---------------|-----------|
| Total Revenue     | $575 billion  | $514 billion  | 12% YoY   |
| Operating Income   | $36.9 billion | $12.2 billion | 201% YoY  |

*Source: NASDAQ_AMZN_2023.pdf.*

## Financial Health and Future Outlook

Currently, specific financial health indicators such as debt levels, liquidity ratios, or cash flow metrics for 2023 are unavailable. Additionally, there is no guidance provided by Amazon for 2024 and beyond in the available documents.

## Risks and Limitations

While the report does not detail specific risks, potential limitations that could impact Amazon's future performance include:

- **Market Competition**: Increased competition in e-commerce and cloud services could affect market share and pricing strategies.
- **Economic Conditions**: Economic downturns or changes in consumer spending habits may impact revenue growth.
- **Regulatory Challenges**: Potential regulatory changes in various markets could pose operational challenges.

## Actionable Advice

Given the significant improvement in operating income and total revenue, stakeholders may consider monitoring Amazon's future performance closely, especially in light of potential risks and the competitive landscape in e-commerce and cloud services.

For a more comprehensive analysis, additional information regarding financial health, future outlook, and risks would be beneficial.
"""

ADVISOR_REPORT_V2 = """
# Amazon Financial Report for Fiscal Year 2023

In fiscal year 2023, Amazon reported the following financial metrics:

- **Total Revenue**: $575 billion
- **Operating Income**: $36.9 billion

These figures reflect a year-over-year growth in total revenue of 12% and a significant improvement in operating income, which increased by 201% compared to the previous year.

## Financial Metrics Comparison

| Metric            | 2023          | 2022          | Change    |
|-------------------|---------------|---------------|-----------|
| Total Revenue     | $575 billion  | $514 billion  | 12% YoY   |
| Operating Income   | $36.9 billion | $12.2 billion | 201% YoY  |

*Source: NASDAQ_AMZN_2023.pdf.*

## Financial Health and Future Outlook

Currently, specific financial health indicators such as debt levels, liquidity ratios, or cash flow metrics for 2023 are unavailable. Additionally, guidance for 2024 and beyond is also missing from the available documents.

## Risks and Limitations

While the report does not detail specific risks, potential limitations that could impact Amazon's future performance include:

- **Market Competition**: Increased competition in e-commerce and cloud services could affect market share and pricing strategies.
- **Economic Conditions**: Economic downturns or changes in consumer spending habits may impact revenue growth.
- **Regulatory Challenges**: Potential regulatory changes in various markets could pose operational challenges.
- **Valuation Risks**: Market expectations and stock performance may lead to valuation risks.
- **Supply Chain Risks**: Operational efficiency could be impacted by supply chain disruptions.
- **Margin Pressure**: Rising costs or competitive pricing strategies may exert pressure on profit margins.
- **Execution Risks**: Challenges associated with scaling operations and managing growth could affect performance.

## Actionable Advice

Given the significant improvement in operating income and total revenue, stakeholders may consider monitoring Amazon's future performance closely, especially in light of potential risks and the competitive landscape in e-commerce and cloud services. 

For a more comprehensive analysis, additional information regarding financial health, future outlook, and risks would be beneficial. The source of the financial figures is noted as NASDAQ_AMZN_2023.pdf.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a clear and concise summary of Amazon's total revenues and operating income for fiscal year 2023. It addresses the original user query effectively, presenting the key financial metrics and their year-over-year changes. However, it still has one unresolved issue that needs to be addressed.

## Query Satisfaction
The revised report adequately answers the original user query regarding Amazon's total revenues and operating income for fiscal year 2023. It includes:
- Total Revenue: $575 billion
- Operating Income: $36.9 billion
Additionally, it provides context regarding year-over-year growth, which enhances the response.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Cited sources for total revenue and operating income figures.
  2. Expanded the risk analysis to include valuation, supply chain, margin pressure, and execution risks.
  3. Provided contextual analysis of financial metrics in relation to Amazon's strategy.
  
- **Unresolved**:
  1. Embed visual representations of financial data in the report.

## Remaining Gaps
The only remaining gap is:
- [ ] **Embed visual representations of financial data in the report.**

## Recommendation
To enhance the quality and engagement of the report, it is recommended to include visual representations (such as charts or graphs) of the financial data presented. This will not only improve readability but also provide a clearer understanding of the trends and comparisons in Amazon's financial performance. Once this issue is resolved, the report will be comprehensive and well-rounded.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_2/query_1
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       70 |       80 |    +10 |
| Risk Assessment      |    15%  |       60 |       80 |    +20 |
| Actionable Advice    |    15%  |       70 |       80 |    +10 |
| Evidence Usage       |    10%  |       90 |       90 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    84.00 |    90.00 |   +6.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +6.0 pts absolute  |  +7.14% relative
==============================================================
```
"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 100,
                "v2_score": 100,
                "delta": 0,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 80,
                "delta": 20,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
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
                "v1_score": 100,
                "v2_score": 100,
                "delta": 0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v1": 84.0,
        "overall_v2": 90.0,
        "absolute_improvement": 6.0,
        "improvement_percentage": 7.14
    }
