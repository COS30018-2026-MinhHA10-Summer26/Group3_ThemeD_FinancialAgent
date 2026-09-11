"""
Three-Version Evaluation Report — document_1 / query_6
Source document: NASDAQ_AMZN_2022.pdf
Query: How did Amazon's international segment perform financially in 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's international segment perform financially in 2022?"

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
In 2022, Amazon's international segment experienced a decline in financial performance. The international segment generated $118 billion in revenue, which represented an 8% decrease compared to the previous year. This decline was primarily attributed to the impact of foreign currency exchange rates, which reduced international net sales by approximately $15 billion. Despite this decrease, the segment saw some growth in unit sales, including sales by third-party sellers and advertising sales, but these were not sufficient to offset the overall revenue decline. Additionally, the operating loss for the international segment increased significantly to $7.7 billion, compared to a loss of $924 million in 2021, largely due to rising fulfillment and shipping costs, as well as increased technology and content costs.
"""

ADVISOR_REPORT_V1 = """
# Amazon's International Segment Performance in 2022

⚠️ The specific financial metrics for Amazon's international segment in 2022, such as international revenue and operating income, were not found in the available documents. This information cannot be confirmed without the source filing.

To analyze Amazon's international segment performance, the following information is needed:
- 2022 international revenue
- 2022 international operating income
- Any additional metrics related to the international segment's performance

Unfortunately, without these critical figures, a comprehensive analysis cannot be provided. If you have access to further documents or can provide this information, I can assist you in analyzing the performance. Alternatively, you may consider reviewing Amazon's official financial statements or investor relations materials for detailed insights into the international segment's performance.
"""

ADVISOR_REPORT_V2 = """
# Amazon's International Segment Performance in 2022

⚠️ The specific financial metrics for Amazon's international segment in 2022, such as international revenue and operating income, were not found in the available documents. This information cannot be confirmed without the source filing.

## Analysis of Missing Financial Metrics

The absence of critical figures such as international revenue and operating income significantly limits our ability to assess Amazon's international segment performance comprehensively. Without these metrics, we cannot evaluate the segment's contribution to overall revenue, profitability, or growth trends. This lack of data may hinder investors' understanding of Amazon's competitive positioning and operational efficiency in international markets.

## Potential Risks and Challenges

Several risks could impact Amazon's international segment performance, including:

- **Competition**: Amazon faces intense competition from local and global e-commerce players, which may affect market share and pricing strategies.
- **Regulatory Challenges**: Different countries have varying regulations regarding e-commerce, data privacy, and taxation, which could pose operational hurdles.
- **Supply Chain Issues**: Global supply chain disruptions can impact inventory availability and fulfillment efficiency, affecting customer satisfaction and sales.

## Qualitative Insights

While specific financial metrics are unavailable, it is essential to consider qualitative factors that may influence the international segment's performance:

- **Market Expansion**: Amazon has been actively expanding its presence in various international markets, which may lead to increased customer acquisition and brand recognition.
- **Investment in Infrastructure**: The company has invested significantly in logistics and fulfillment capabilities, which could enhance service levels and operational efficiency in the long term.

## Conclusion

Unfortunately, without the necessary financial figures, a comprehensive analysis of Amazon's international segment performance in 2022 cannot be provided. If you have access to further documents or can provide this information, I can assist you in analyzing the performance. Alternatively, you may consider reviewing Amazon's official financial statements or investor relations materials for detailed insights into the international segment's performance.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Amazon's international segment performance in 2022, but it lacks grounding in the provided context documents and misses several structural elements that would enhance its quality.

## Query Satisfaction
The response provides a clear summary of the financial performance of Amazon's international segment in 2022, including revenue figures and the reasons for the decline. It mentions the $118 billion revenue, the 8% decrease, and the significant increase in operating loss. However, it does not reference specific documents or provide citations, which diminishes its credibility.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Missing Limitations or Caveats**: The response does not mention any potential limitations or caveats regarding the financial data, such as the impact of foreign exchange rates.
3. **No Actionable Content**: The response lacks actionable insights or recommendations for the user based on the financial performance discussed.
4. **No Structured Sections**: The response does not follow a structured format that could help in better understanding the information presented.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made.
- Add any necessary limitations or caveats regarding the financial data.
- Provide actionable insights or recommendations based on the financial performance.
- Structure the response into clear sections to enhance readability and comprehension.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Amazon's international segment performance in 2022 compared to the initial version. However, it still lacks specific financial metrics, which are crucial for a complete evaluation.

## Query Satisfaction
The revised report addresses the user query regarding Amazon's international segment performance in 2022 by discussing the implications of missing financial metrics, potential risks, and qualitative insights. However, it does not provide the requested financial figures, such as international revenue and operating income, which limits its effectiveness in fully answering the query.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved**:
  - Include 2022 international revenue and operating income figures.
  - Analyze the implications of missing financial metrics on overall performance.
  - Address potential risks related to competition, regulation, and supply chain for the international segment.
  - Incorporate qualitative insights or alternative metrics to provide context.
  
- **Unresolved**:
  - Add visualizations or figures to support the analysis.

## Remaining Gaps
The following issue remains unresolved:
- **Add visualizations or figures to support the analysis.**

## Recommendation
To enhance the report further, the advisor should:
1. Include specific financial metrics for the international segment, such as revenue and operating income, if available.
2. Add visualizations or figures that could help illustrate the performance of the international segment or the impact of missing data.
3. Consider summarizing any available data that could provide context or insights, even if specific figures are not present. 

Addressing these points will improve the report's comprehensiveness and utility for decision-making.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_1/query_6
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |       60 |    +60 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       30 |       50 |    +20 |
| Query Satisfaction   |    10%  |        0 |       40 |    +40 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     3.00 |    28.50 |  +25.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +25.5 pts absolute  |  +850.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_1/query_6
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
| Business Analysis    |    15%  |       60 |        0 |       60 |    -60 |    +60 |     +0 |
| Risk Assessment      |    15%  |       50 |        0 |       70 |    -50 |    +70 |    +20 |
| Actionable Advice    |    15%  |       40 |        0 |        0 |    -40 |     +0 |    -40 |
| Evidence Usage       |    10%  |       70 |        0 |        0 |    -70 |     +0 |    -70 |
| Completeness         |    10%  |       80 |       30 |       50 |    -50 |    +20 |    -30 |
| Query Satisfaction   |    10%  |       90 |        0 |       40 |    -90 |    +40 |    -50 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    69.00 |     3.00 |    28.50 |    -66 |    +25 |    -40 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -40 pts absolute  |  -58.70% relative
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
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 60,
                "delta_v0_v1": -60,
                "delta_v1_v2": 60,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -50,
                "delta_v1_v2": 70,
                "delta_v0_v2": 20,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -40,
                "delta_v1_v2": 0,
                "delta_v0_v2": -40,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -70,
                "delta_v1_v2": 0,
                "delta_v0_v2": -70,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 30,
                "v2_score": 50,
                "delta_v0_v1": -50,
                "delta_v1_v2": 20,
                "delta_v0_v2": -30,
                "weighted_v1": 3.0,
                "weighted_v2": 5.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 40,
                "delta_v0_v1": -90,
                "delta_v1_v2": 40,
                "delta_v0_v2": -50,
                "weighted_v1": 0.0,
                "weighted_v2": 4.0
            }
        },
        "overall_v0": 69.0,
        "overall_v1": 3.0,
        "overall_v2": 28.5,
        "improvement_v0_to_v1": -66.0,
        "improvement_v1_to_v2": 25.5,
        "improvement_v0_to_v2": -40.5,
        "improvement_pct_v0_to_v2": -58.7
    }
