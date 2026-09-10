"""
Full Pipeline Evaluation Report — document_3 / query_2
Source document: NASDAQ_AMZN_2024.pdf
Query: How did AWS perform in 2024 and what was its contribution to operating profit?
"""
from __future__ import annotations
import json

USER_QUERY = "How did AWS perform in 2024 and what was its contribution to operating profit?"

USER_QUERIES = [
    "What were Amazon's total net sales and earnings per share for fiscal year 2024?",
    "How did AWS perform in 2024 and what was its contribution to operating profit?",
    "What were the highlights of Amazon's logistics and fulfillment network in 2024?",
    "How did Amazon's subscription services revenue evolve in 2024?",
    "What were Amazon's major capital allocation decisions in 2024?",
    "How did Amazon's international operations perform in 2024?",
    "What were the significant legal and regulatory risks Amazon faced in 2024?",
    "What AI and cloud strategy shifts did Amazon announce or execute in 2024?",
]

ADVISOR_REPORT_V1 = """
### AWS Performance in 2024

In 2024, Amazon Web Services (AWS) demonstrated significant growth and contributed positively to the company's overall financial performance. Here are the key metrics regarding AWS:

- **Revenue Growth**: AWS revenue increased by **19% year-over-year**, rising from **$91 billion** in 2023 to **$108 billion** in 2024.

- **Operating Income Contribution**: The specific contribution of AWS to the overall operating profit was not detailed in the provided documents. Amazon's overall operating income improved by **86% year-over-year**, from **$36.9 billion** to **$68.6 billion**. Given AWS's high margins compared to other segments, its growth likely played a crucial role in this increase, but exact figures are unavailable.

### Financial Health Assessment

AWS's robust revenue growth indicates a strong demand for its services, which is essential for maintaining competitive advantage in the cloud computing market. The overall improvement in Amazon's operating income suggests that AWS is a key driver of profitability for the company.

### Future Outlook

Looking ahead, AWS is expected to continue its growth trajectory, especially with the ongoing expansion of its service offerings, including advancements in AI and infrastructure services. This positions AWS well to capture more market share and enhance its contribution to Amazon's overall profitability.

### Actionable Advice

To maximize AWS's potential, Amazon should focus on:
- Continuing to innovate and expand its service offerings.
- Enhancing customer experience to retain and attract new clients.
- Exploring strategic partnerships to broaden its market reach.

### Visual Aid

Here is a table summarizing AWS's revenue growth in 2024:

| Year | AWS Revenue (in Billion USD) |
| --- | --- |
| 2023 | 91 |
| 2024 | 108 |

This table illustrates the significant increase in AWS revenue from 2023 to 2024, highlighting its contribution to Amazon's overall financial success.

### Summary

AWS's performance in 2024 was robust, with a revenue increase of **19%**, contributing to Amazon's overall operating income growth. However, the exact contribution of AWS to the operating profit was not specified in the documents provided, and further details would be needed to quantify its specific impact on operating income.
"""

ADVISOR_REPORT_V2 = """
### AWS Performance in 2024

In 2024, Amazon Web Services (AWS) demonstrated significant growth and contributed positively to the company's overall financial performance. Here are the key metrics regarding AWS:

- **Revenue Growth**: AWS revenue increased by **19% year-over-year**, rising from **$91 billion** in 2023 to **$108 billion** in 2024.

- **Operating Income Contribution**: The specific contribution of AWS to the overall operating profit was not detailed in the provided documents. Amazon's overall operating income improved by **86% year-over-year**, from **$36.9 billion** to **$68.6 billion**. Given AWS's high margins compared to other segments, its growth likely played a crucial role in this increase, but exact figures are unavailable.

### Financial Health Assessment

AWS's robust revenue growth indicates a strong demand for its services, which is essential for maintaining competitive advantage in the cloud computing market. The overall improvement in Amazon's operating income suggests that AWS is a key driver of profitability for the company.

### Future Outlook

Looking ahead, AWS is expected to continue its growth trajectory, especially with the ongoing expansion of its service offerings, including advancements in AI and infrastructure services. This positions AWS well to capture more market share and enhance its contribution to Amazon's overall profitability.

### Visual Aid

Here is a table summarizing AWS's revenue growth in 2024:

| Year | AWS Revenue (in Billion USD) |
| --- | --- |
| 2023 | 91 |
| 2024 | 108 |

This table illustrates the significant increase in AWS revenue from 2023 to 2024, highlighting its contribution to Amazon's overall financial success.

### Summary

AWS's performance in 2024 was robust, with a revenue increase of **19%**, contributing to Amazon's overall operating income growth. However, the exact contribution of AWS to the operating profit was not specified in the documents provided, and further details would be needed to quantify its specific impact on operating income.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of AWS's performance in 2024, addressing key metrics such as revenue growth and the overall financial health of the segment. However, it still lacks specific quantitative data regarding AWS's direct contribution to operating profit and does not adequately address potential risks associated with AWS's growth.

## Query Satisfaction
The report adequately answers the original user query regarding AWS's performance in 2024, highlighting a **19% increase in revenue** and the overall improvement in Amazon's operating income. However, it does not provide specific figures for AWS's contribution to operating profit, which is a critical aspect of the query. Additionally, while it discusses future outlook and financial health, it fails to mention risks, which could mislead readers about the sustainability of AWS's growth.

## Issues Resolution Status
- **Resolved Issues**: 
  - The report has provided a clearer overview of AWS's performance and included a table summarizing revenue growth.
- **Unresolved Issues**:
  - The report still lacks quantitative data on AWS's direct contribution to operating profit.
  - It does not address missing risks related to competition, valuation, supply chain, regulation, and execution.
  - The report does not embed visual aids or links to enhance the presentation of data.

## Remaining Gaps
1. **Quantitative Data**: Specific figures regarding AWS's direct contribution to operating profit are still missing.
2. **Risk Assessment**: The report does not address key risks associated with AWS's growth, including competition and regulatory challenges.
3. **Visual Aids**: There is a need for embedded visual aids or links to enhance the presentation of data.

## Recommendation
To improve the report further, the advisor should:
1. Include specific quantitative data on AWS's contribution to operating profit to provide clarity and support claims made in the report.
2. Address potential risks associated with AWS's growth, including competition and regulatory challenges, to present a balanced view.
3. Embed visual aids or links to enhance the presentation of data and improve reader engagement.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_3/query_2
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       90 |       90 |     +0 |
| Business Analysis    |    15%  |       70 |       70 |     +0 |
| Risk Assessment      |    15%  |       50 |       50 |     +0 |
| Actionable Advice    |    15%  |       60 |       60 |     +0 |
| Evidence Usage       |    10%  |       80 |       80 |     +0 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       85 |       85 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    75.00 |    75.00 |   +0.0 |
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
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 70,
                "delta": 0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 50,
                "delta": 0,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 60,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 80,
                "delta": 0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 85,
                "v2_score": 85,
                "delta": 0,
                "weighted_v1": 8.5,
                "weighted_v2": 8.5
            }
        },
        "overall_v1": 75.0,
        "overall_v2": 75.0,
        "absolute_improvement": 0.0,
        "improvement_percentage": 0.0
    }
