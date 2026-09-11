"""
Three-Version Evaluation Report — document_3 / query_4
Source document: NASDAQ_AMZN_2024.pdf
Query: How did Amazon's subscription services revenue evolve in 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's subscription services revenue evolve in 2024?"

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
In 2024, Amazon's subscription services revenue, which includes fees associated with Amazon Prime memberships, increased to $44.4 billion, up from $40.2 billion in 2023. This represents a year-over-year growth of approximately 10.5%. The growth in subscription services revenue was driven by increased unit sales, including sales by third-party sellers, advertising sales, and the continued popularity of Amazon Prime.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Subscription Services Revenue Evolution in 2024

⚠️ Subscription services revenue for 2024 was not found in the available documents. This figure cannot be confirmed without the source filing.

To analyze the evolution of Amazon's subscription services revenue in 2024, the specific revenue figure for that segment is needed. Unfortunately, the documents provided do not include this information.

However, it is noteworthy that Amazon's overall revenue grew 11% year-over-year, reaching $638 billion in 2024. This growth was driven by various segments, including North America, International, and AWS, which saw significant increases. The expansion of Prime Video and other subscription offerings suggests that subscription services may have also experienced growth, aligning with the overall positive trend in revenue.

In addition, the continued investment in enhancing customer experiences—such as the introduction of new original shows on Prime Video and improvements in delivery services—indicates a strategic focus on retaining and expanding the subscriber base. This could imply a favorable outlook for subscription services moving forward.

While we cannot provide the exact figures for subscription services, the overall revenue growth and strategic initiatives suggest a potentially positive trajectory for this segment. If you have access to additional documents or data that include the specific revenue figures for Amazon's subscription services, please provide them for a more comprehensive analysis.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Subscription Services Revenue Evolution in 2024

⚠️ Subscription services revenue for 2024 was not found in the available documents. This figure cannot be confirmed without the source filing.

To analyze the evolution of Amazon's subscription services revenue in 2024, the specific revenue figure for that segment is needed. Unfortunately, the documents provided do not include this information.

However, it is noteworthy that Amazon's overall revenue grew 11% year-over-year, reaching $638 billion in 2024. This growth was driven by various segments, including North America, International, and AWS, which saw significant increases. The expansion of Prime Video and other subscription offerings suggests that subscription services may have also experienced growth, aligning with the overall positive trend in revenue.

In addition, the continued investment in enhancing customer experiences—such as the introduction of new original shows on Prime Video and improvements in delivery services—indicates a strategic focus on retaining and expanding the subscriber base. This could imply a favorable outlook for subscription services moving forward.

While we cannot provide the exact figures for subscription services, the overall revenue growth and strategic initiatives suggest a potentially positive trajectory for this segment.

### Risks and Competitive Landscape
It is important to note that several risks could impact the performance of Amazon's subscription services. These include:

- **Competition**: The subscription market is highly competitive, with other streaming services and subscription models vying for consumer attention and spending.
- **Regulatory Challenges**: Changes in regulations affecting digital content and subscription services could pose challenges.
- **Margin Pressures**: Rising costs associated with content production and delivery could impact profitability in the subscription segment.

If you have access to additional documents or data that include the specific revenue figures for Amazon's subscription services, please provide them for a more comprehensive analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the evolution of Amazon's subscription services revenue in 2024. However, it lacks grounding in the provided context documents and misses essential structural elements.

## Query Satisfaction
The response provides a clear answer to the user's question about the revenue evolution of Amazon's subscription services in 2024, stating that it increased to $44.4 billion from $40.2 billion in 2023, representing a growth of approximately 10.5%. This directly satisfies the user's inquiry.

## Remaining Gaps
1. **Grounding in Context**: The response does not reference any of the provided context documents, which contain relevant financial data and insights about Amazon's performance in 2024. For instance, the documents indicate that subscription services revenue is part of the overall sales growth driven by various factors, but the response does not cite these sources.
   
2. **Source Citation**: There is no citation of the source of the revenue figures mentioned in the response, which is critical for validating the information provided.

3. **Limitations or Caveats**: The response lacks any mention of limitations or caveats regarding the revenue figures, which could provide a more nuanced understanding of the data.

4. **Actionable Content**: The response does not include any actionable insights or recommendations based on the revenue growth, which could enhance its usefulness to the user.

5. **Structured Sections**: The response is presented as a single paragraph without structured sections, making it less readable and harder to digest.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to ground the information in verified data.
- Add limitations or caveats regarding the revenue figures to provide a balanced view.
- Consider including actionable insights or implications of the revenue growth for Amazon's future.
- Structure the response into clear sections for better readability and comprehension.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a general overview of Amazon's subscription services revenue evolution in 2024 but fails to include specific revenue figures or quantitative data, which are critical for a comprehensive analysis. While it addresses some of the issues raised by the Critic, it does not fully resolve all identified gaps.

## Query Satisfaction
The report does not adequately answer the original user query regarding the evolution of Amazon's subscription services revenue in 2024. Although it discusses overall revenue growth and strategic initiatives, it lacks the specific data needed to evaluate the subscription services segment directly.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  - Include specific revenue figures for subscription services for 2024.
  - Provide estimates or historical data to support claims of growth in subscription services.
  - Address missing risks related to competition, regulation, and margin pressures.
  
- **Unresolved**:
  - Incorporate figures or visualizations to support the analysis.

## Remaining Gaps
1. **Incorporate figures or visualizations** to support the analysis of subscription services revenue.

## Recommendation
The advisor should revise the report to include relevant figures or visualizations that can substantiate the claims made regarding the growth and performance of Amazon's subscription services in 2024. This will enhance the report's credibility and provide a clearer picture for investors.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_3/query_4
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       70 |       70 |     +0 |
| Risk Assessment      |    15%  |       60 |       60 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       80 |       80 |     +0 |
| Query Satisfaction   |    10%  |       60 |       60 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    33.50 |    33.50 |   +0.0 |
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
  Weighted Metrics (3 versions) — document_3/query_4
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
| Business Analysis    |    15%  |       60 |       70 |       70 |    +10 |     +0 |    +10 |
| Risk Assessment      |    15%  |       50 |       60 |       60 |    +10 |     +0 |    +10 |
| Actionable Advice    |    15%  |       40 |        0 |        0 |    -40 |     +0 |    -40 |
| Evidence Usage       |    10%  |       30 |        0 |        0 |    -30 |     +0 |    -30 |
| Completeness         |    10%  |       70 |       80 |       80 |    +10 |     +0 |    +10 |
| Query Satisfaction   |    10%  |       80 |       60 |       60 |    -20 |     +0 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    63.00 |    33.50 |    33.50 |    -29 |     +0 |    -29 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -29 pts absolute  |  -46.83% relative
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
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
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
                "v0_score": 30,
                "weighted_v0": 3.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -30,
                "delta_v1_v2": 0,
                "delta_v0_v2": -30,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
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
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": -20,
                "delta_v1_v2": 0,
                "delta_v0_v2": -20,
                "weighted_v1": 6.0,
                "weighted_v2": 6.0
            }
        },
        "overall_v0": 63.0,
        "overall_v1": 33.5,
        "overall_v2": 33.5,
        "improvement_v0_to_v1": -29.5,
        "improvement_v1_to_v2": 0.0,
        "improvement_v0_to_v2": -29.5,
        "improvement_pct_v0_to_v2": -46.83
    }
