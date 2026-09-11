"""
Three-Version Evaluation Report — document_1 / query_2
Source document: NASDAQ_AMZN_2022.pdf
Query: How did Amazon's AWS segment perform in 2022 compared to prior years?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's AWS segment perform in 2022 compared to prior years?"

USER_QUERIES = [
    "What were Amazon's total net sales and net income for fiscal year 2022?",
    "How did Amazon's AWS segment perform in 2022 compared to prior years?",
    "What were the major cost drivers that impacted Amazon's operating income in 2022?",
    "What is Amazon's free cash flow position and how did it change in 2022?",
    "What key risks does Amazon identify in its 2022 annual report?",
    "How did Amazon's international segment perform financially in 2022?",
    "What were Amazon's capital expenditure and investment priorities in 2022?",
    "What is Amazon's outlook and strategic priorities discussed in the 2022 annual report?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2022, Amazon's AWS segment experienced a year-over-year revenue growth of 29%, reaching an annualized revenue run rate of $85 billion. This growth was notable despite facing short-term headwinds due to macroeconomic conditions, which led many companies to be more cautious in their spending. The AWS segment's performance in 2022 continued to reflect strong demand, although it was slower compared to the 37% growth rate seen in 2021. Overall, AWS maintained its trajectory of growth, driven by increased customer usage and a robust pipeline of new customers, despite the challenges presented by the economic environment.
"""

ADVISOR_REPORT_V1 = """
# Amazon AWS Segment Performance Analysis for 2022

To analyze Amazon's AWS segment performance in 2022 compared to prior years, we have the following information:

- AWS had an annualized revenue run rate of **$85 billion** in 2022.
- AWS revenue grew **29% year-over-year** in 2022 on a **$62 billion** revenue base.

Unfortunately, the specific revenue figures for AWS in 2021 and 2020 are not available in the provided documents. Therefore, a direct year-over-year comparison with those years cannot be made.

### Summary of AWS Performance in 2022:
- **2022 Revenue Base**: $62 billion
- **2022 Year-over-Year Growth**: 29%
- **Annualized Revenue Run Rate**: $85 billion

### Revenue Performance Comparison Table

| Year | Revenue       |
|------|---------------|
| 2020 | Unavailable   |
| 2021 | Unavailable   |
| 2022 | $62 billion   |

### Financial Health and Future Outlook:
Despite the growth in 2022, AWS is facing short-term headwinds as companies are being more cautious in spending due to challenging macroeconomic conditions. This has led to a focus on customer relationships and optimizing AWS spend rather than aggressive cost-cutting.

### Risks and Limitations:
- The current macroeconomic environment may impact AWS's growth trajectory.
- Companies may be hesitant to invest heavily in cloud services during uncertain times, which could affect AWS's revenue growth in the near term.

### Actionable Insights:
- AWS should continue to focus on customer-centric strategies to maintain and grow its market share.
- Emphasizing the unique elasticity of cloud services can help in retaining customers who may be looking to optimize costs.

If you have access to additional documents or data that include AWS revenue figures for 2021 and 2020, please share them, and I can assist you further in providing a more comprehensive analysis.
"""

ADVISOR_REPORT_V2 = """
# Amazon AWS Segment Performance Analysis for 2022

To analyze Amazon's AWS segment performance in 2022 compared to prior years, we have the following information:

- AWS had an annualized revenue run rate of **$85 billion** in 2022.
- AWS revenue grew **29% year-over-year** in 2022 on a **$62 billion** revenue base.

Unfortunately, the specific revenue figures for AWS in 2021 and 2020 are not available in the provided documents. Therefore, a direct year-over-year comparison with those years cannot be made. However, the 29% growth in 2022 is significant, especially considering the challenging macroeconomic conditions that have led many companies to be more cautious in their spending.

### Summary of AWS Performance in 2022:
- **2022 Revenue Base**: $62 billion
- **2022 Year-over-Year Growth**: 29%
- **Annualized Revenue Run Rate**: $85 billion

### Revenue Performance Comparison Table

| Year | Revenue       |
|------|---------------|
| 2020 | Unavailable   |
| 2021 | Unavailable   |
| 2022 | $62 billion   |

### Contextual Analysis of Growth:
The **29% growth** in AWS's revenue for 2022 indicates a robust performance, especially in a year where many businesses faced economic headwinds. This growth suggests that AWS has continued to gain traction in the cloud market, despite the overall cautious spending environment. However, without the revenue figures from 2021 and 2020, it is challenging to assess whether this growth rate is consistent with historical trends or represents a slowdown compared to previous years.

### Financial Health and Future Outlook:
Despite the growth in 2022, AWS is facing short-term headwinds as companies are being more cautious in spending due to challenging macroeconomic conditions. This has led to a focus on customer relationships and optimizing AWS spend rather than aggressive cost-cutting.

### Risks and Limitations:
- The current macroeconomic environment may impact AWS's growth trajectory.
- Companies may be hesitant to invest heavily in cloud services during uncertain times, which could affect AWS's revenue growth in the near term.
- **Competition**: AWS operates in a highly competitive landscape with numerous well-funded rivals.
- **Valuation**: Market conditions and investor sentiment could influence AWS's valuation.
- **Supply Chain**: Potential supply chain issues may impact service delivery.
- **Regulation**: Regulatory risks could affect AWS's operations.
- **Margin Pressure**: Rising costs and competitive pricing may exert pressure on margins.
- **Execution Risks**: Operational challenges could hinder AWS's growth.

### Actionable Insights:
- AWS should continue to focus on customer-centric strategies to maintain and grow its market share.
- Emphasizing the unique elasticity of cloud services can help in retaining customers who may be looking to optimize costs.

If you have access to additional documents or data that include AWS revenue figures for 2021 and 2020, please share them, and I can assist you further in providing a more comprehensive analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the performance of Amazon's AWS segment in 2022, highlighting the year-over-year revenue growth and contextualizing it within the broader economic challenges. However, it lacks citations from the provided context documents and does not include limitations or caveats, which diminishes its completeness and reliability.

## Query Satisfaction
The response effectively answers the user's question about AWS's performance in 2022 by stating that it achieved a 29% growth rate and reached an annualized revenue run rate of $85 billion. It also compares this performance to the previous year's growth rate of 37%, providing a clear picture of the segment's trajectory. However, it does not delve into specific financial health indicators or future outlooks beyond the immediate context of growth.

## Remaining Gaps
1. **Source Citations**: The response does not reference any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There is no mention of potential limitations or caveats regarding the growth figures or the economic conditions affecting AWS.
3. **Actionable Content**: The response lacks actionable insights or recommendations for the user, which could enhance its utility.
4. **Structured Sections**: The response does not follow a structured format that could improve readability and comprehension.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made.
- Add limitations or caveats regarding the growth figures and economic conditions.
- Consider providing actionable insights or recommendations based on the AWS performance data.
- Structure the response into clear sections to enhance clarity and user engagement.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a clearer analysis of Amazon's AWS segment performance in 2022 compared to prior years. It addresses several issues raised in the Critic's report but still leaves one critical issue unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding AWS's performance in 2022. It includes key metrics such as revenue growth and annualized revenue run rate, and it contextualizes the growth within the macroeconomic environment. However, it still lacks historical revenue figures for 2021 and 2020, which limits the ability to fully assess growth trends.

## Issues Resolution Status
The following issues identified by the Critic have been resolved:
- Provided a contextual analysis of growth.
- Elaborated on specific short-term headwinds affecting AWS.
- Addressed missing risks related to competition, valuation, supply chain, regulation, margin pressure, and execution.

The following issue remains unresolved:
- **Include figures or visualizations to support claims made in the report.**

## Remaining Gaps
- The report does not include any figures or visualizations to support the claims made, which could enhance understanding and retention of the information presented.

## Recommendation
To improve the report further, the advisor should:
1. Include relevant figures or visualizations to support key claims and enhance clarity.
2. If possible, provide AWS revenue figures for 2021 and 2020 to allow for a comprehensive year-over-year comparison. 

Addressing these points will strengthen the report's overall quality and decision-making utility.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_1/query_2
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       90 |       90 |     +0 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       60 |       80 |    +20 |
| Actionable Advice    |    15%  |       70 |       75 |     +5 |
| Evidence Usage       |    10%  |       50 |       60 |    +10 |
| Completeness         |    10%  |       80 |       85 |     +5 |
| Query Satisfaction   |    10%  |       80 |       85 |     +5 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    73.50 |    80.00 |   +6.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +6.5 pts absolute  |  +8.84% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_1/query_2
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |       90 |       90 |     +0 |     +0 |     +0 |
| Business Analysis    |    15%  |       70 |       70 |       75 |     +0 |     +5 |     +5 |
| Risk Assessment      |    15%  |       50 |       60 |       80 |    +10 |    +20 |    +30 |
| Actionable Advice    |    15%  |       30 |       70 |       75 |    +40 |     +5 |    +45 |
| Evidence Usage       |    10%  |       40 |       50 |       60 |    +10 |    +10 |    +20 |
| Completeness         |    10%  |       60 |       80 |       85 |    +20 |     +5 |    +25 |
| Query Satisfaction   |    10%  |       80 |       80 |       85 |     +0 |     +5 |     +5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    63.00 |    73.50 |    80.00 |    +10 |     +6 |    +17 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +17 pts absolute  |  +26.98% relative
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
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v0_v1": 0,
                "delta_v1_v2": 5,
                "delta_v0_v2": 5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v0_v1": 10,
                "delta_v1_v2": 20,
                "delta_v0_v2": 30,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 30,
                "weighted_v0": 4.5,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v0_v1": 40,
                "delta_v1_v2": 5,
                "delta_v0_v2": 45,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "weighted_v0": 4.0,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v0_v1": 10,
                "delta_v1_v2": 10,
                "delta_v0_v2": 20,
                "weighted_v1": 5.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 20,
                "delta_v1_v2": 5,
                "delta_v0_v2": 25,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 0,
                "delta_v1_v2": 5,
                "delta_v0_v2": 5,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 63.0,
        "overall_v1": 73.5,
        "overall_v2": 80.0,
        "improvement_v0_to_v1": 10.5,
        "improvement_v1_to_v2": 6.5,
        "improvement_v0_to_v2": 17.0,
        "improvement_pct_v0_to_v2": 26.98
    }
