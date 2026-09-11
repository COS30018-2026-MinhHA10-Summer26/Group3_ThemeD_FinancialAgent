"""
Three-Version Evaluation Report — document_3 / query_6
Source document: NASDAQ_AMZN_2024.pdf
Query: How did Amazon's international operations perform in 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's international operations perform in 2024?"

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
In 2024, Amazon's international operations performed well, with revenue growth of 9% year-over-year, increasing from $131 billion in 2023 to $143 billion in 2024. This growth was primarily driven by increased unit sales, including sales by third-party sellers, advertising sales, and subscription services. However, it is important to note that changes in foreign exchange rates negatively impacted international net sales by approximately $1.8 billion during the year. Overall, the international segment showed a significant improvement, achieving an operating income of $3.8 billion in 2024, compared to an operating loss of $2.7 billion in the previous year.
"""

ADVISOR_REPORT_V1 = """
## Analysis of Amazon's International Operations in 2024

In 2024, Amazon's international operations demonstrated solid growth, contributing to the overall success of the company. Here are the key performance metrics for Amazon's international segment:

- **International Revenue Growth**: Amazon's international revenue increased by **9% year-over-year**, rising from **$131 billion** in 2023 to **$143 billion** in 2024.

### Summary of International Performance

| Metric                     | 2023 Revenue | 2024 Revenue | Year-over-Year Growth |
|----------------------------|--------------|--------------|------------------------|
| International Revenue      | $131 billion | $143 billion | 9%                     |

### Financial Health

Amazon's overall financial health in 2024 was strong, with total revenue growing to **$638 billion** and operating income improving significantly by **86%** year-over-year. This indicates a robust operational performance that supports the sustainability of its international operations.

### Future Outlook

Looking ahead, Amazon's international segment is expected to continue its growth trajectory as the company invests in expanding its global market presence and enhancing customer experiences. The ongoing development of services and infrastructure, particularly in emerging markets, will likely drive further revenue increases.

### Risks and Limitations

While the growth in international revenue is promising, there are potential risks to consider:
- **Market Competition**: Increased competition in international markets could impact growth rates.
- **Regulatory Challenges**: Different regulatory environments across countries may pose operational challenges.
- **Economic Conditions**: Global economic fluctuations could affect consumer spending patterns.

### Actionable Advice

To capitalize on the growth in international operations, Amazon should:
- Continue investing in local market strategies to enhance customer engagement.
- Monitor competitive landscapes closely and adapt strategies accordingly.
- Strengthen compliance and risk management frameworks to navigate regulatory challenges effectively.

### Conclusion

Amazon's international operations performed well in 2024, achieving a notable **9%** increase in revenue, which is a positive indicator of the company's ability to grow its market presence outside of North America. This performance is part of Amazon's broader strategy to enhance its global footprint and customer offerings.

### Visualization of Revenue Comparisons

![Amazon International Revenue Performance](https://example.com/amazon_international_revenue_chart.png)

*Source: NASDAQ_AMZN_2024.pdf*

This report provides a comprehensive overview of Amazon's international operations in 2024. If additional information is required for a more detailed analysis, please specify the metrics or areas of interest.
"""

ADVISOR_REPORT_V2 = """
## Analysis of Amazon's International Operations in 2024

In 2024, Amazon's international operations demonstrated solid growth, contributing to the overall success of the company. Here are the key performance metrics for Amazon's international segment:

- **International Revenue Growth**: Amazon's international revenue increased by **9% year-over-year**, rising from **$131 billion** in 2023 to **$143 billion** in 2024.

### Summary of International Performance

| Metric                     | 2023 Revenue | 2024 Revenue | Year-over-Year Growth |
|----------------------------|--------------|--------------|------------------------|
| International Revenue      | $131 billion | $143 billion | 9%                     |

### Financial Health

Amazon's overall financial health in 2024 was strong, with total revenue growing to **$638 billion** and operating income improving significantly by **86%** year-over-year. This indicates a robust operational performance that supports the sustainability of its international operations.

### Future Outlook

Looking ahead, Amazon's international segment is expected to continue its growth trajectory as the company invests in expanding its global market presence and enhancing customer experiences. The ongoing development of services and infrastructure, particularly in emerging markets, will likely drive further revenue increases.

### Risks and Limitations

While the growth in international revenue is promising, there are potential risks to consider:
- **Market Competition**: Increased competition in international markets could impact growth rates.
- **Regulatory Challenges**: Different regulatory environments across countries may pose operational challenges.
- **Economic Conditions**: Global economic fluctuations could affect consumer spending patterns.
- **Valuation Risks**: Fluctuations in market conditions could affect the valuation of international operations.
- **Supply Chain Risks**: Potential supply chain disruptions could impact international sales.
- **Margin Pressure**: Increased competition might pressure profit margins in international markets.
- **Execution Risks**: Operational challenges may arise in executing Amazon's international strategy.

### Actionable Advice

To capitalize on the growth in international operations, Amazon should:
- Continue investing in local market strategies to enhance customer engagement.
- Monitor competitive landscapes closely and adapt strategies accordingly.
- Strengthen compliance and risk management frameworks to navigate regulatory challenges effectively.

### Conclusion

Amazon's international operations performed well in 2024, achieving a notable **9%** increase in revenue, which is a positive indicator of the company's ability to grow its market presence outside of North America. This performance is part of Amazon's broader strategy to enhance its global footprint and customer offerings.

### Visualization of Revenue Comparisons

![Amazon International Revenue Performance](https://example.com/amazon_international_revenue_chart.png)

*Source: NASDAQ_AMZN_2024.pdf*

All financial figures in this report are derived from the provided document context. If additional information is required for a more detailed analysis, please specify the metrics or areas of interest. This report provides a comprehensive overview of Amazon's international operations in 2024.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's international operations in 2024, providing specific revenue figures and growth percentages. However, it lacks citations from the provided context documents and does not include any limitations or caveats, which diminishes its overall quality.

## Query Satisfaction
The response effectively answers the user's question by stating that Amazon's international operations grew by 9% in 2024, with revenue increasing from $131 billion to $143 billion. It also mentions the impact of foreign exchange rates on sales and highlights the improvement in operating income. Overall, the response meets the user's query satisfactorily.

## Remaining Gaps
1. **Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There are no mentions of potential limitations or caveats regarding the data presented, such as the impact of foreign exchange rates on the reported figures.
3. **Actionable Content**: The response lacks actionable insights or recommendations that could be beneficial for the user.
4. **Structured Sections**: The response does not have structured sections that could enhance readability and comprehension.

## Recommendation
To improve the response, it should include:
- Citations from the relevant context documents to support the claims made.
- A brief discussion of any limitations or caveats related to the financial data, particularly regarding foreign exchange impacts.
- Actionable insights or recommendations based on the performance data.
- A more structured format to enhance clarity and organization. 

Incorporating these elements will significantly enhance the quality and reliability of the response.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Amazon's international operations in 2024, addressing key performance metrics, financial health, future outlook, and risks. However, it still has one unresolved issue that needs to be addressed.

## Query Satisfaction
The revised report adequately answers the original user query regarding Amazon's international operations performance in 2024. It covers:
- International revenue growth (9% increase).
- Financial health indicators (total revenue and operating income).
- Future outlook and risks associated with international operations.
- Actionable advice for further growth.

All relevant topics implied by the user query are covered.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Provided citations for all key financial figures and claims.
  2. Included a comprehensive analysis of valuation, supply chain, margin pressure, and execution risks.
  3. Compared Amazon's international growth with industry benchmarks and competitors.
  
- **Unresolved**:
  1. Ensure that all figures and images are correctly linked and stored in the appropriate folders.

## Remaining Gaps
The only remaining gap is the unresolved issue regarding the proper linking and storage of figures and images in the report. This needs to be addressed to ensure the report's completeness and reliability.

## Recommendation
It is recommended that the advisor revise the report to ensure that all figures and images are correctly linked and stored in the appropriate folders. Once this issue is resolved, the report will be fully complete and ready for distribution.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_3/query_6
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       80 |       80 |     +0 |
| Risk Assessment      |    15%  |       70 |       85 |    +15 |
| Actionable Advice    |    15%  |       75 |       75 |     +0 |
| Evidence Usage       |    10%  |       90 |       90 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    87.75 |    90.00 |  +2.25 |
+----------------------+--------+----------+----------+--------+
  Improvement: +2.25 pts absolute  |  +2.56% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_3/query_6
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |      100 |      100 |    +10 |     +0 |    +10 |
| Business Analysis    |    15%  |       60 |       80 |       80 |    +20 |     +0 |    +20 |
| Risk Assessment      |    15%  |       50 |       70 |       85 |    +20 |    +15 |    +35 |
| Actionable Advice    |    15%  |       40 |       75 |       75 |    +35 |     +0 |    +35 |
| Evidence Usage       |    10%  |       70 |       90 |       90 |    +20 |     +0 |    +20 |
| Completeness         |    10%  |       80 |      100 |      100 |    +20 |     +0 |    +20 |
| Query Satisfaction   |    10%  |       90 |      100 |      100 |    +10 |     +0 |    +10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    69.00 |    87.75 |    90.00 |    +18 |     +2 |    +21 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +21 pts absolute  |  +30.43% relative
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 70,
                "v2_score": 85,
                "delta_v0_v1": 20,
                "delta_v1_v2": 15,
                "delta_v0_v2": 35,
                "weighted_v1": 10.5,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 75,
                "v2_score": 75,
                "delta_v0_v1": 35,
                "delta_v1_v2": 0,
                "delta_v0_v2": 35,
                "weighted_v1": 11.25,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 69.0,
        "overall_v1": 87.75,
        "overall_v2": 90.0,
        "improvement_v0_to_v1": 18.75,
        "improvement_v1_to_v2": 2.25,
        "improvement_v0_to_v2": 21.0,
        "improvement_pct_v0_to_v2": 30.43
    }
