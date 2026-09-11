"""
Three-Version Evaluation Report — document_4 / query_7
Source document: NASDAQ_AMZN_2025.pdf
Query: How did Amazon's Prime membership and subscription services perform in 2025?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's Prime membership and subscription services perform in 2025?"

USER_QUERIES = [
    "What were Amazon's key financial results and revenue breakdown for fiscal year 2025?",
    "How did Amazon's AWS segment grow in 2025 and what products drove demand?",
    "What is Amazon's profitability trend and operating margin outlook for 2025?",
    "What strategic acquisitions or investments did Amazon make in 2025?",
    "How did macroeconomic conditions affect Amazon's business in 2025?",
    "What is Amazon's cash and debt position at the end of fiscal year 2025?",
    "How did Amazon's Prime membership and subscription services perform in 2025?",
    "What does Amazon's 2025 annual report say about its long-term growth strategy?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2025, Amazon's Prime membership and subscription services performed strongly, contributing to the overall growth of the company. The total net sales for Amazon increased by 12% year-over-year, reaching approximately $716.9 billion. Within this growth, subscription services, including Amazon Prime, played a significant role, as they were part of the increased unit sales and advertising sales reported in both the North America and International segments.

Specifically, the North America segment saw net sales rise to $426.3 billion, while the International segment's sales increased to $161.9 billion. The growth in these segments was attributed to factors such as improved customer experience, including fast shipping offers, which are integral to the Prime membership.

Additionally, the AWS segment, which also contributes to subscription services through its offerings, reported a 20% increase in sales, reaching $128.7 billion. This indicates that Amazon's subscription services, including Prime, are not only maintaining their relevance but are also expanding in their impact on overall revenue.

Overall, Amazon's Prime membership and subscription services were a key driver of growth in 2025, reflecting strong customer engagement and increased usage.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Prime Membership and Subscription Services Performance in 2025

The available documents do not provide specific financial figures or metrics directly related to Amazon's Prime membership and subscription services performance in 2025. However, there are some relevant insights regarding Amazon's overall business strategies and developments that may impact these services:

1. **Grocery Business Growth**: Amazon's grocery business has grown significantly, reaching over $150 billion in gross sales in 2025. This growth includes the integration of perishables into their Same-Day Delivery network, which has resonated well with customers. This expansion could potentially enhance the value proposition of Prime membership, especially for customers interested in grocery delivery.

2. **Same-Day Delivery Initiatives**: Amazon has introduced Same-Day Fulfillment Centers and is expanding its delivery capabilities, which may improve the overall customer experience for Prime members. The introduction of ultra-fast delivery services, such as Amazon Now, has reportedly increased shopping frequency among Prime members.

3. **Customer Engagement**: The documents indicate that Prime members have tripled their shopping frequency after using the Amazon Now service, suggesting that enhancements in delivery speed and service offerings are positively influencing customer engagement.

Unfortunately, specific metrics such as Prime membership revenue, subscription services revenue, growth rate of Prime membership, and the total number of Prime members in 2025 are not available in the provided documents.

Given the absence of detailed data, I recommend consulting additional sources or documents that may contain the needed information, such as Amazon's official financial statements or investor presentations for 2025. If you have access to such documents, please share them for a more comprehensive analysis.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Prime Membership and Subscription Services Performance in 2025

The available documents do not provide specific financial figures or metrics directly related to Amazon's Prime membership and subscription services performance in 2025. However, there are relevant insights regarding Amazon's overall business strategies and developments that may impact these services:

1. **Grocery Business Growth**: Amazon's grocery business has grown significantly, reaching over **$150 billion** in gross sales in 2025. This growth includes the integration of perishables into their Same-Day Delivery network, which has resonated well with customers. This expansion could potentially enhance the value proposition of Prime membership, especially for customers interested in grocery delivery.

   | Metric       | Value          |
   |--------------|----------------|
   | Gross Sales  | $150 billion   |

2. **Same-Day Delivery Initiatives**: Amazon has introduced Same-Day Fulfillment Centers and is expanding its delivery capabilities, which may improve the overall customer experience for Prime members. The introduction of ultra-fast delivery services, such as Amazon Now, has reportedly increased shopping frequency among Prime members, with reports indicating that Prime members have tripled their shopping frequency after using this service.

3. **Customer Engagement**: The enhancements in delivery speed and service offerings are positively influencing customer engagement, which is crucial for maintaining and growing Prime membership.

### Potential Risks and Competitive Pressures
While the growth in grocery sales and delivery capabilities is promising, there are several risks and competitive pressures that could impact Prime membership growth:

- **Competition**: Other retailers may offer similar grocery and delivery services, potentially eroding Amazon's market share in the subscription space. This could lead to a dilution of Prime's unique value proposition.
- **Operational Costs**: Expanding delivery capabilities may lead to increased operational costs, which could pressure profit margins and affect the sustainability of subscription pricing.
- **Regulatory Risks**: Changes in regulations affecting delivery services or grocery operations could pose challenges for Amazon's business model, potentially impacting service availability and costs.

Unfortunately, specific metrics such as Prime membership revenue, subscription services revenue, growth rate of Prime membership, and the total number of Prime members in 2025 are not available in the provided documents. It is important to note that these figures are missing from the context provided.

### Recommendations for Further Information
Given the absence of detailed data, I recommend consulting additional sources or documents that may contain the needed information, such as Amazon's official financial statements or investor presentations for 2025. Additionally, industry reports or market analysis from financial analysts may provide insights into Prime membership performance and trends. If you have access to such documents, please share them for a more comprehensive analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response provides a general overview of Amazon's Prime membership and subscription services performance in 2025, but it lacks specific details and citations from the provided context documents. It does not fully address the user's query regarding the performance metrics of these services.

## Query Satisfaction
The response partially satisfies the query by mentioning that Amazon's Prime membership and subscription services contributed to the overall growth of the company in 2025. However, it lacks specific performance metrics or detailed insights directly related to the Prime membership itself, such as subscriber numbers, revenue generated from subscriptions, or comparisons to previous years. The response does not provide a comprehensive view of the subscription services' performance.

## Remaining Gaps
1. **Lack of Specific Metrics**: The response does not include specific performance metrics for Amazon Prime membership, such as the number of subscribers or revenue generated from subscription services.
2. **No Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
3. **Missing Limitations or Caveats**: There are no acknowledgments of potential limitations or uncertainties regarding the performance data.
4. **Absence of Actionable Content**: The response does not provide any actionable insights or recommendations based on the performance of the subscription services.

## Recommendation
To improve the response:
- Include specific performance metrics related to Amazon's Prime membership and subscription services, such as subscriber growth, revenue figures, and comparisons to previous years.
- Cite relevant context documents to support the claims made in the response.
- Acknowledge any limitations or uncertainties regarding the data presented.
- Provide actionable insights or recommendations based on the performance of the subscription services.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more structured and detailed analysis of Amazon's Prime membership and subscription services performance in 2025 compared to the original version. However, it still lacks some critical elements that would enhance its completeness and usefulness.

## Query Satisfaction
The revised report addresses the user query regarding Amazon's Prime membership and subscription services performance in 2025 by discussing relevant business strategies and developments. It highlights the growth in grocery sales, same-day delivery initiatives, and customer engagement. However, it does not provide specific financial metrics or detailed insights directly related to Prime membership performance, which limits its effectiveness in fully answering the query.

## Issues Resolution Status
The report has resolved 3 out of 4 identified issues:
- **Resolved**: 
  - Included specific financial metrics related to Prime membership performance (e.g., grocery sales).
  - Strengthened connections between business initiatives and Prime membership impact.
  - Addressed potential risks and competitive pressures.
- **Unresolved**: 
  - The report still lacks visual aids to support key figures, which was identified as a necessary improvement.

## Remaining Gaps
1. **Visual Aids**: The report does not include any visual representations (charts or figures) to support the key figures mentioned, such as the $150 billion in grocery sales. This omission makes it harder for readers to grasp the significance of these numbers.

## Recommendation
To enhance the quality and completeness of the report, it is recommended to:
- **Add Visual Aids**: Include charts or figures that illustrate key metrics and trends related to Prime membership and subscription services. This will help convey the information more effectively and provide a clearer understanding of the data presented. 

Overall, while the revised report is an improvement, addressing the remaining gap will make it more comprehensive and valuable for stakeholders.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_4/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |       25 |    +25 |
| Business Analysis    |    15%  |       50 |       70 |    +20 |
| Risk Assessment      |    15%  |        0 |       60 |    +60 |
| Actionable Advice    |    15%  |        0 |       50 |    +50 |
| Evidence Usage       |    10%  |        0 |       10 |    +10 |
| Completeness         |    10%  |        0 |       70 |    +70 |
| Query Satisfaction   |    10%  |        0 |       70 |    +70 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     7.50 |    48.25 | +40.75 |
+----------------------+--------+----------+----------+--------+
  Improvement: +40.75 pts absolute  |  +543.33% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_4/query_7
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |       25 |    -90 |    +25 |    -65 |
| Business Analysis    |    15%  |       70 |       50 |       70 |    -20 |    +20 |     +0 |
| Risk Assessment      |    15%  |       50 |        0 |       60 |    -50 |    +60 |    +10 |
| Actionable Advice    |    15%  |       40 |        0 |       50 |    -40 |    +50 |    +10 |
| Evidence Usage       |    10%  |       60 |        0 |       10 |    -60 |    +10 |    -50 |
| Completeness         |    10%  |       80 |        0 |       70 |    -80 |    +70 |    -10 |
| Query Satisfaction   |    10%  |       85 |        0 |       70 |    -85 |    +70 |    -15 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    69.00 |     7.50 |    48.25 |    -61 |    +40 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -20 pts absolute  |  -30.07% relative
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
                "v2_score": 25,
                "delta_v0_v1": -90,
                "delta_v1_v2": 25,
                "delta_v0_v2": -65,
                "weighted_v1": 0.0,
                "weighted_v2": 6.25
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
                "v1_score": 0,
                "v2_score": 60,
                "delta_v0_v1": -50,
                "delta_v1_v2": 60,
                "delta_v0_v2": 10,
                "weighted_v1": 0.0,
                "weighted_v2": 9.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v0_v1": -40,
                "delta_v1_v2": 50,
                "delta_v0_v2": 10,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
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
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -80,
                "delta_v1_v2": 70,
                "delta_v0_v2": -10,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 85,
                "weighted_v0": 8.5,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -85,
                "delta_v1_v2": 70,
                "delta_v0_v2": -15,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            }
        },
        "overall_v0": 69.0,
        "overall_v1": 7.5,
        "overall_v2": 48.25,
        "improvement_v0_to_v1": -61.5,
        "improvement_v1_to_v2": 40.75,
        "improvement_v0_to_v2": -20.75,
        "improvement_pct_v0_to_v2": -30.07
    }
