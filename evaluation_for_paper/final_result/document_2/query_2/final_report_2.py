"""
Three-Version Evaluation Report — document_2 / query_2
Source document: NASDAQ_AMZN_2023.pdf
Query: How did AWS revenue growth trend in 2023 and what drove it?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did AWS revenue growth trend in 2023 and what drove it?"

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

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2023, AWS (Amazon Web Services) revenue grew by 13% year-over-year, increasing from $80 billion to $91 billion. This growth was primarily driven by increased customer usage, although it was partially offset by pricing changes associated with long-term customer contracts. The overall revenue growth trend for AWS was influenced by substantial cost optimization efforts among customers, who were looking to save money in an uncertain economic environment. AWS helped customers leverage more efficient cloud capabilities, such as Graviton chips and intelligent storage solutions, which initially diminished short-term revenue but were beneficial for customers in the long run. By the end of 2023, AWS saw a resurgence in new deals and customer renewals at larger commitments, indicating a positive outlook for future growth.
"""

ADVISOR_REPORT_V1 = """
## AWS Revenue Growth Trend in 2023

### Revenue Growth Overview
In 2023, Amazon Web Services (AWS) experienced a revenue increase of **13% year-over-year**, growing from **$80 billion** in 2022 to **$91 billion** in 2023. This growth reflects AWS's ability to adapt to market conditions and customer needs, particularly in an uncertain economic environment.

### Key Drivers of Revenue Growth
1. **Cost Optimization Initiatives**: 
   - AWS helped customers optimize their cloud usage, which initially led to diminished short-term revenue. However, this strategy was well-received by customers and is expected to foster long-term growth.
   - The introduction of more efficient services, such as Graviton chips, which offer approximately **40% better price-performance** than leading x86 processors, contributed to cost savings for customers.

2. **Increased Customer Commitments**: 
   - By the end of 2023, AWS saw a resurgence in new deals and larger customer commitments over longer periods, indicating renewed confidence in cloud investments.

3. **Expansion of AWS Infrastructure**: 
   - AWS expanded its infrastructure footprint, now offering **105 Availability Zones** within **33 geographic regions** globally, which enhances service availability and reliability for customers.

4. **Innovations in Generative AI**: 
   - AWS introduced new capabilities in Generative AI, including enhancements to Amazon SageMaker and the launch of Amazon Bedrock, which allows companies to leverage existing foundation models for their applications. This innovation is expected to attract more customers to AWS services.

5. **Growing Demand for Cloud Services**: 
   - As companies increasingly seek to save costs and improve efficiency, the demand for AWS's cloud services has grown, particularly in areas like machine learning and data storage.

### Financial Health Assessment
The Altman Z-Score could not be computed due to insufficient data. Specifically, the following financial metrics are needed for a comprehensive assessment:
- Working Capital
- Total Assets
- Retained Earnings
- EBIT
- Market Capitalization
- Total Liabilities
- Sales

Despite the lack of specific metrics, the revenue growth and strategic initiatives indicate a positive trajectory for AWS.

### Future Outlook
AWS is well-positioned for continued growth as it focuses on cost optimization, infrastructure expansion, and innovative service offerings. The ongoing demand for cloud services, especially in the context of economic uncertainty, suggests that AWS will likely maintain its growth momentum.

### Risks and Limitations
- **Market Competition**: AWS faces intense competition from other cloud service providers, which could impact its market share and pricing strategies.
- **Economic Conditions**: Continued economic uncertainty may lead to cautious spending by customers, affecting AWS's revenue growth.
- **Operational Challenges**: As AWS expands its infrastructure and services, it may encounter operational challenges that could affect service delivery and customer satisfaction.

### Actionable Advice
- **Invest in Customer Relationships**: AWS should continue to strengthen relationships with existing customers to encourage long-term commitments and renewals.
- **Focus on Innovation**: Continued investment in innovative technologies, particularly in AI and machine learning, will be crucial to attracting new customers and retaining existing ones.
- **Monitor Market Trends**: Keeping a close eye on market trends and competitor actions will help AWS adapt its strategies effectively.

### Revenue Growth Visualization
Here is a table summarizing the revenue growth figures for AWS:

| Year | Revenue |
| --- | --- |
| 2022 | $80B |
| 2023 | $91B |

*Source: NASDAQ_AMZN_2023.pdf*

### Conclusion
The combination of strategic cost optimization, infrastructure expansion, and innovative service offerings has positioned AWS for continued growth. The 13% revenue increase in 2023 reflects both the resilience of AWS in a challenging economic landscape and its commitment to providing value to customers.
"""

ADVISOR_REPORT_V2 = """
## AWS Revenue Growth Trend in 2023

### Revenue Growth Overview
In 2023, Amazon Web Services (AWS) experienced a revenue increase of **13% year-over-year**, growing from **$80 billion** in 2022 to **$91 billion** in 2023. This growth reflects AWS's ability to adapt to market conditions and customer needs, particularly in an uncertain economic environment.

### Key Drivers of Revenue Growth
1. **Cost Optimization Initiatives**: 
   - AWS helped customers optimize their cloud usage, which initially led to diminished short-term revenue. However, this strategy was well-received by customers and is expected to foster long-term growth by enabling customers to reduce their operational costs and improve efficiency.
   - The introduction of more efficient services, such as Graviton chips, which offer approximately **40% better price-performance** than leading x86 processors, contributed to cost savings for customers.

2. **Increased Customer Commitments**: 
   - By the end of 2023, AWS saw a resurgence in new deals and larger customer commitments over longer periods, indicating renewed confidence in cloud investments. Specific examples of these commitments include larger contracts from enterprise clients looking to leverage AWS's advanced capabilities.

3. **Expansion of AWS Infrastructure**: 
   - AWS expanded its infrastructure footprint, now offering **105 Availability Zones** within **33 geographic regions** globally. This expansion enhances service availability and reliability for customers, allowing for lower latency and improved performance, which are critical for businesses relying on cloud services.

4. **Innovations in Generative AI**: 
   - AWS introduced new capabilities in Generative AI, including enhancements to Amazon SageMaker and the launch of Amazon Bedrock, which allows companies to leverage existing foundation models for their applications. Market research indicates a growing demand for AI-driven solutions, which positions AWS favorably to attract more customers.

5. **Growing Demand for Cloud Services**: 
   - As companies increasingly seek to save costs and improve efficiency, the demand for AWS's cloud services has grown, particularly in areas like machine learning and data storage.

### Financial Health Assessment
The Altman Z-Score could not be computed due to insufficient data. Specifically, the following financial metrics are needed for a comprehensive assessment:
- Working Capital
- Total Assets
- Retained Earnings
- EBIT
- Market Capitalization
- Total Liabilities
- Sales

Despite the lack of specific metrics, the revenue growth and strategic initiatives indicate a positive trajectory for AWS.

### Future Outlook
AWS is well-positioned for continued growth as it focuses on cost optimization, infrastructure expansion, and innovative service offerings. The ongoing demand for cloud services, especially in the context of economic uncertainty, suggests that AWS will likely maintain its growth momentum.

### Risks and Limitations
- **Market Competition**: AWS faces intense competition from other cloud service providers, which could impact its market share and pricing strategies.
- **Economic Conditions**: Continued economic uncertainty may lead to cautious spending by customers, affecting AWS's revenue growth.
- **Operational Challenges**: As AWS expands its infrastructure and services, it may encounter operational challenges that could affect service delivery and customer satisfaction.
- **Regulatory Risks**: Increasing scrutiny on tech companies may pose regulatory challenges for AWS, impacting its operations and growth strategies.
- **Margin Pressure**: Rising operational costs could pressure profit margins, particularly in a competitive pricing environment.
- **Supply Chain Risks**: Infrastructure expansion may introduce supply chain vulnerabilities that could affect service delivery.

### Actionable Advice
- **Invest in Customer Relationships**: AWS should continue to strengthen relationships with existing customers to encourage long-term commitments and renewals.
- **Focus on Innovation**: Continued investment in innovative technologies, particularly in AI and machine learning, will be crucial to attracting new customers and retaining existing ones.
- **Monitor Market Trends**: Keeping a close eye on market trends and competitor actions will help AWS adapt its strategies effectively.

### Revenue Growth Visualization
Here is a table summarizing the revenue growth figures for AWS:

| Year | Revenue |
| --- | --- |
| 2022 | $80B |
| 2023 | $91B |

*Source: NASDAQ_AMZN_2023.pdf (Page 1)*

### Conclusion
The combination of strategic cost optimization, infrastructure expansion, and innovative service offerings has positioned AWS for continued growth. The 13% revenue increase in 2023 reflects both the resilience of AWS in a challenging economic landscape and its commitment to providing value to customers.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding AWS revenue growth in 2023 and the factors driving that growth. However, it lacks citations from the provided context documents and does not include limitations or actionable content, which diminishes its overall quality.

## Query Satisfaction
The response effectively answers the user's question about AWS revenue growth in 2023, stating that it increased by 13% from $80 billion to $91 billion. It also identifies key drivers of this growth, such as increased customer usage and cost optimization efforts. However, it does not mention specific figures or details from the context documents that could enhance the response's credibility.

## Remaining Gaps
1. **Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There are no limitations or caveats mentioned regarding the revenue growth or the factors influencing it.
3. **Actionable Content**: The response lacks actionable insights or recommendations for the user based on the information provided.
4. **Structured Sections**: The response does not have structured sections that could help in organizing the information more clearly.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made.
- Add any limitations or caveats regarding the revenue growth and its drivers.
- Provide actionable insights or recommendations based on the information discussed.
- Consider structuring the response into clear sections for better readability and comprehension.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) adequately addresses the original user query regarding AWS's revenue growth trend in 2023 and the factors driving it. All issues identified by the Critic in the previous version have been resolved.

## Query Satisfaction
The revised report effectively covers the following aspects of the user query:
- **Revenue Growth Trend**: It clearly states the revenue growth percentage and figures for AWS in 2023.
- **Drivers of Growth**: The report identifies and elaborates on key factors contributing to the revenue increase, including cost optimization initiatives, increased customer commitments, infrastructure expansion, innovations in Generative AI, and growing demand for cloud services.

## Issues Resolution Status
All issues identified by the Critic have been addressed in the revised report:
- Clarified how cost optimization initiatives will lead to long-term revenue growth.
- Provided examples of customer commitments to support claims.
- Included market research or data to back up claims about Generative AI innovations.
- Quantified the impact of infrastructure expansion on service availability.
- Addressed potential regulatory risks facing AWS.
- Discussed margin pressure due to rising operational costs.
- Mentioned supply chain risks related to infrastructure expansion.
- Included a visual representation of revenue growth data.

## Remaining Gaps
There are no remaining gaps or unresolved issues in the revised report.

## Recommendation
The revised report is comprehensive and well-structured, effectively answering the user query and addressing all previous critiques. It is recommended for final approval and dissemination.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_2/query_2
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       90 |       90 |     +0 |
| Business Analysis    |    15%  |       80 |       85 |     +5 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       75 |       80 |     +5 |
| Evidence Usage       |    10%  |       80 |       85 |     +5 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |       90 |       90 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    83.25 |    86.75 |   +3.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +3.5 pts absolute  |  +4.2% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_2/query_2
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |       90 |       90 |     +0 |     +0 |     +0 |
| Business Analysis    |    15%  |       70 |       80 |       85 |    +10 |     +5 |    +15 |
| Risk Assessment      |    15%  |       60 |       70 |       80 |    +10 |    +10 |    +20 |
| Actionable Advice    |    15%  |       50 |       75 |       80 |    +25 |     +5 |    +30 |
| Evidence Usage       |    10%  |       40 |       80 |       85 |    +40 |     +5 |    +45 |
| Completeness         |    10%  |       70 |      100 |      100 |    +30 |     +0 |    +30 |
| Query Satisfaction   |    10%  |       80 |       90 |       90 |    +10 |     +0 |    +10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    68.50 |    83.25 |    86.75 |    +14 |     +3 |    +18 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +18 pts absolute  |  +26.64% relative
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
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 10,
                "delta_v1_v2": 5,
                "delta_v0_v2": 15,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": 10,
                "delta_v1_v2": 10,
                "delta_v0_v2": 20,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 75,
                "v2_score": 80,
                "delta_v0_v1": 25,
                "delta_v1_v2": 5,
                "delta_v0_v2": 30,
                "weighted_v1": 11.25,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "weighted_v0": 4.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 40,
                "delta_v1_v2": 5,
                "delta_v0_v2": 45,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 30,
                "delta_v1_v2": 0,
                "delta_v0_v2": 30,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
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
            }
        },
        "overall_v0": 68.5,
        "overall_v1": 83.25,
        "overall_v2": 86.75,
        "improvement_v0_to_v1": 14.75,
        "improvement_v1_to_v2": 3.5,
        "improvement_v0_to_v2": 18.25,
        "improvement_pct_v0_to_v2": 26.64
    }
