"""
Three-Version Evaluation Report — document_3 / query_2
Source document: NASDAQ_AMZN_2024.pdf
Query: How did AWS perform in 2024 and what was its contribution to operating profit?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
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

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2024, AWS (Amazon Web Services) performed strongly, with revenue increasing by 19% year-over-year, rising from $91 billion in 2023 to $108 billion in 2024. This growth was attributed to increased customer usage and the launch of new services, despite some pricing changes due to long-term customer contracts.

AWS made a significant contribution to Amazon's overall operating profit, with its operating income reaching $39.8 billion in 2024, compared to $24.6 billion in 2023. This increase in operating income was primarily driven by higher sales, reduced payroll and related expenses, and a decrease in depreciation and amortization expenses. Overall, Amazon's consolidated operating income for 2024 was $68.6 billion, indicating that AWS was a major contributor to the company's profitability.
"""

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

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding AWS's performance in 2024 and its contribution to operating profit. However, it lacks citations from the provided context documents and does not include any limitations or caveats, which diminishes its overall quality.

## Query Satisfaction
The response effectively addresses the user's query by providing specific figures for AWS's revenue growth (19% increase from $91 billion to $108 billion) and operating income (from $24.6 billion to $39.8 billion). It also contextualizes AWS's contribution to Amazon's overall operating profit, which was $68.6 billion in 2024. Therefore, the response satisfies the query.

## Remaining Gaps
1. **Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There are no mentions of any limitations or potential uncertainties regarding the figures or claims made.
3. **Actionable Content**: The response lacks actionable insights or recommendations that could be beneficial for the user.
4. **Structured Sections**: The response does not have a clear structure or sections, which could enhance readability and comprehension.

## Recommendation
To improve the response, it should include:
- Citations from the relevant context documents to support the claims made.
- A section discussing any limitations or uncertainties related to the financial data provided.
- Actionable insights or recommendations based on the performance data.
- A more structured format to enhance clarity and organization.
"""

PIPELINE_EVALUATION_REPORT = """
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

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_3/query_2
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |       90 |       90 |     +0 |     +0 |     +0 |
| Business Analysis    |    15%  |       60 |       70 |       70 |    +10 |     +0 |    +10 |
| Risk Assessment      |    15%  |       50 |       50 |       50 |     +0 |     +0 |     +0 |
| Actionable Advice    |    15%  |       40 |       60 |       60 |    +20 |     +0 |    +20 |
| Evidence Usage       |    10%  |       70 |       80 |       80 |    +10 |     +0 |    +10 |
| Completeness         |    10%  |       80 |       90 |       90 |    +10 |     +0 |    +10 |
| Query Satisfaction   |    10%  |       90 |       85 |       85 |     -5 |     +0 |     -5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    69.00 |    75.00 |    75.00 |     +6 |     +0 |     +6 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +6 pts absolute  |  +8.70% relative
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
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
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
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
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
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 85,
                "v2_score": 85,
                "delta_v0_v1": -5,
                "delta_v1_v2": 0,
                "delta_v0_v2": -5,
                "weighted_v1": 8.5,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 69.0,
        "overall_v1": 75.0,
        "overall_v2": 75.0,
        "improvement_v0_to_v1": 6.0,
        "improvement_v1_to_v2": 0.0,
        "improvement_v0_to_v2": 6.0,
        "improvement_pct_v0_to_v2": 8.7
    }
