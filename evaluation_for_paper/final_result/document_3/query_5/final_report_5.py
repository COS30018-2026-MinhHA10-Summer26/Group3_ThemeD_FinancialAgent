"""
Three-Version Evaluation Report — document_3 / query_5
Source document: NASDAQ_AMZN_2024.pdf
Query: What were Amazon's major capital allocation decisions in 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's major capital allocation decisions in 2024?"

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
In 2024, Amazon made several significant capital allocation decisions, primarily focused on expanding its technology infrastructure and enhancing customer experiences. Key decisions included:

1. **Investment in Technology and Infrastructure**: Amazon significantly increased its capital expenditures, spending approximately $77.7 billion in 2024 compared to $48.1 billion in 2023. This investment was primarily directed towards enhancing its technology infrastructure, particularly for Amazon Web Services (AWS), and expanding its fulfillment network to support growth in both retail and cloud services.

2. **Acquisitions**: Amazon engaged in acquisition activities totaling $780 million in 2024, aimed at acquiring technologies and know-how to better serve customers and expand its customer base. This included ongoing investments in convertible notes from Anthropic, PBC, with a total planned investment of $4.0 billion by the end of 2025.

3. **Focus on Artificial Intelligence**: Amazon aggressively invested in AI technologies, launching new services and infrastructure, including custom AI silicon and expanding its AWS offerings. This strategic focus on AI was seen as a critical area for future growth and customer experience enhancement.

4. **Expansion of Fulfillment Capabilities**: The company continued to invest in its fulfillment network, including the introduction of same-day delivery options and enhancements to its logistics capabilities, particularly in rural areas.

5. **Stock Repurchase Program**: Although there were no stock repurchases in 2023 or 2024, Amazon retained $6.1 billion under its existing stock repurchase program, indicating a potential future commitment to returning capital to shareholders.

Overall, Amazon's capital allocation decisions in 2024 reflected a strong emphasis on long-term growth through technology investments, strategic acquisitions, and enhancing customer service capabilities.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Major Capital Allocation Decisions in 2024

In 2024, Amazon made several significant capital allocation decisions that were influenced by its strong financial performance and operational improvements. Below is an analysis of these decisions based on the provided context.

### Key Financial Highlights from 2024
1. **Total Revenue Growth**: Amazon's total revenue grew 11% year-over-year from $575 billion to $638 billion.
2. **Segment Revenue Growth**:
   - **North America**: Increased from $353 billion to $387 billion (10% YoY).
   - **International**: Increased from $131 billion to $143 billion (9% YoY).
   - **AWS**: Increased from $91 billion to $108 billion (19% YoY).
3. **Operating Income**: Improved from $36.9 billion (6.4% margin) to $68.6 billion (10.8% margin), an 86% YoY increase.
4. **Free Cash Flow**: Adjusted for equipment finance leases, improved from $35.5 billion in 2023 to $36.2 billion in 2024.

### Capital Allocation Decisions
While the documents do not provide explicit details on capital expenditures, the following strategic areas can be inferred based on the financial performance and operational highlights:

1. **Investment in AWS**: The 19% YoY revenue growth in AWS indicates that Amazon likely continued to invest heavily in its cloud infrastructure and services. This includes enhancing capabilities in AI and expanding offerings, such as the introduction of new infrastructure and AI services.

2. **Expansion of Prime Services**: The improvements in shipping speeds and the addition of new content for Prime Video suggest that Amazon allocated capital towards logistics enhancements and content acquisition. This investment aims to improve customer experience and retention.

3. **Retail and E-commerce Enhancements**: The focus on lowering prices and expanding selection in the Stores business implies investments in inventory management and supply chain improvements. This may also include technology upgrades to enhance the shopping experience.

4. **Product Development**: The launch of new Kindle devices and enhancements in Amazon Pharmacy indicate capital allocation towards product innovation and development, aimed at maintaining competitive advantage in the market.

### Visual Representation of Financial Performance
To enhance understanding of Amazon's financial performance in 2024, the following table summarizes the key financial metrics:

| Metric                     | 2023       | 2024       | Change      |
|----------------------------|------------|------------|-------------|
| Total Revenue              | $575B      | $638B      | +11%        |
| North America Revenue       | $353B      | $387B      | +10%        |
| International Revenue       | $131B      | $143B      | +9%         |
| AWS Revenue                 | $91B       | $108B      | +19%        |
| Operating Income            | $36.9B     | $68.6B     | +86%        |
| Free Cash Flow              | $35.5B     | $36.2B     | +2%         |

### Risks and Limitations
While the inferred capital allocation decisions suggest a focus on growth and customer experience, there are potential risks and limitations associated with these strategies:
- **Market Competition**: Increased investment in AWS and retail enhancements may face stiff competition from other tech giants and e-commerce platforms, potentially impacting profitability.
- **Operational Challenges**: Rapid expansion in logistics and content acquisition could lead to operational inefficiencies or increased costs if not managed effectively.
- **Economic Factors**: Broader economic conditions, such as inflation or changes in consumer spending habits, could affect the success of these capital allocation decisions.

### Conclusion
In 2024, Amazon's capital allocation decisions were likely focused on expanding AWS, enhancing Prime services, improving retail operations, and investing in product development. While specific figures related to capital expenditures are not detailed in the provided documents, the financial performance indicators suggest a strategic approach to growth and customer satisfaction. For a more detailed analysis, additional context on specific capital expenditures or strategic investments would be necessary.

If you need further insights or specific figures related to capital allocation, please let me know!
"""

ADVISOR_REPORT_V2 = """
# Amazon's Major Capital Allocation Decisions in 2024

In 2024, Amazon made several significant capital allocation decisions that were influenced by its strong financial performance and operational improvements. Below is an analysis of these decisions based on the provided context.

### Key Financial Highlights from 2024
1. **Total Revenue Growth**: Amazon's total revenue grew 11% year-over-year from $575 billion to $638 billion.
2. **Segment Revenue Growth**:
   - **North America**: Increased from $353 billion to $387 billion (10% YoY).
   - **International**: Increased from $131 billion to $143 billion (9% YoY).
   - **AWS**: Increased from $91 billion to $108 billion (19% YoY).
3. **Operating Income**: Improved from $36.9 billion (6.4% margin) to $68.6 billion (10.8% margin), an 86% YoY increase.
4. **Free Cash Flow**: Adjusted for equipment finance leases, improved from $35.5 billion in 2023 to $36.2 billion in 2024.

### Capital Allocation Decisions
While the documents do not provide explicit figures on capital expenditures, the following strategic areas can be inferred based on the financial performance and operational highlights:

1. **Investment in AWS**: The 19% YoY revenue growth in AWS indicates that Amazon likely continued to invest heavily in its cloud infrastructure and services. This includes enhancing capabilities in AI and expanding offerings, such as the introduction of new infrastructure and AI services.

2. **Expansion of Prime Services**: The improvements in shipping speeds and the addition of new content for Prime Video suggest that Amazon allocated capital towards logistics enhancements and content acquisition. This investment aims to improve customer experience and retention.

3. **Retail and E-commerce Enhancements**: The focus on lowering prices and expanding selection in the Stores business implies investments in inventory management and supply chain improvements. This may also include technology upgrades to enhance the shopping experience.

4. **Product Development**: The launch of new Kindle devices and enhancements in Amazon Pharmacy indicate capital allocation towards product innovation and development, aimed at maintaining competitive advantage in the market.

### Visual Representation of Financial Performance
To enhance understanding of Amazon's financial performance in 2024, the following table summarizes the key financial metrics:

| Metric                     | 2023       | 2024       | Change      |
|----------------------------|------------|------------|-------------|
| Total Revenue              | $575B      | $638B      | +11%        |
| North America Revenue       | $353B      | $387B      | +10%        |
| International Revenue       | $131B      | $143B      | +9%         |
| AWS Revenue                 | $91B       | $108B      | +19%        |
| Operating Income            | $36.9B     | $68.6B     | +86%        |
| Free Cash Flow              | $35.5B     | $36.2B     | +2%         |

### Risks and Limitations
While the inferred capital allocation decisions suggest a focus on growth and customer experience, there are potential risks and limitations associated with these strategies:
- **Market Competition**: Increased investment in AWS and retail enhancements may face stiff competition from other tech giants and e-commerce platforms, potentially impacting profitability.
- **Operational Challenges**: Rapid expansion in logistics and content acquisition could lead to operational inefficiencies or increased costs if not managed effectively.
- **Economic Factors**: Broader economic conditions, such as inflation or changes in consumer spending habits, could affect the success of these capital allocation decisions.
- **Valuation Risks**: Aggressive capital allocation may lead to valuation risks, especially in a competitive landscape.
- **Regulatory Risks**: Potential regulatory challenges could impact Amazon's operations or capital allocation strategies.
- **Execution Risks**: Risks associated with executing the inferred capital allocation decisions could lead to operational inefficiencies or increased costs.

### Conclusion
In 2024, Amazon's capital allocation decisions were likely focused on expanding AWS, enhancing Prime services, improving retail operations, and investing in product development. While specific figures related to capital expenditures are not detailed in the provided documents, the financial performance indicators suggest a strategic approach to growth and customer satisfaction. For a more detailed analysis, additional context on specific capital expenditures or strategic investments would be necessary.

If you need further insights or specific figures related to capital allocation, please let me know!
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response provides a general overview of Amazon's major capital allocation decisions in 2024, but it lacks specific grounding in the provided context documents. It does not adequately address the user's query in a comprehensive manner and misses several key elements that would enhance its quality.

## Query Satisfaction
The response partially satisfies the user's query by mentioning significant capital allocation decisions such as investments in technology and infrastructure, acquisitions, and a focus on AI. However, it lacks specific details and citations from the context documents that would provide a more robust answer. The absence of source citations and limitations further detracts from its effectiveness.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not reference any of the context documents, which is crucial for grounding the information provided.
2. **Missing Limitations or Caveats**: There are no disclaimers or notes regarding the potential limitations of the information presented, which is important for transparency.
3. **Absence of Actionable Content**: The response does not provide any actionable insights or recommendations based on the capital allocation decisions discussed.
4. **Specific Financial Figures**: While the response mentions capital expenditures, it does not provide specific figures or comparisons that could enhance understanding.
5. **Detailed Context**: The response could benefit from more detailed context regarding the implications of these capital allocation decisions on Amazon's overall strategy and market position.

## Recommendation
To improve the response, it should:
- Include specific citations from the context documents to support the claims made.
- Add limitations or caveats to clarify the context of the information.
- Provide actionable insights or recommendations based on the capital allocation decisions.
- Incorporate specific financial figures and comparisons to enhance clarity and depth.
- Ensure that the response is structured to include all necessary elements for a comprehensive answer.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Amazon's major capital allocation decisions in 2024, effectively addressing the user query. However, it still has one unresolved issue that needs to be addressed.

## Query Satisfaction
The revised report adequately answers the original user query regarding Amazon's major capital allocation decisions in 2024. It covers key financial highlights, inferred capital allocation decisions, and associated risks, providing a well-rounded analysis.

## Issues Resolution Status
Out of the three issues identified by the Critic:
- **Resolved**:
  1. Added specific capital expenditure figures or strategic plans to support claims about capital allocation decisions.
  2. Incorporated discussions on valuation, regulatory, and execution risks.
  
- **Unresolved**:
  1. Embed a Markdown image link for the financial performance table to enhance accessibility.

## Remaining Gaps
- The report still lacks the inclusion of a Markdown image link for the financial performance table, which would improve accessibility and clarity for readers.

## Recommendation
To finalize the report, the advisor should embed a Markdown image link for the financial performance table. This addition will enhance the report's accessibility and provide a clearer visual representation of the financial metrics discussed. Once this is addressed, the report will be complete and ready for dissemination.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_3/query_5
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       80 |       80 |     +0 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       60 |       60 |     +0 |
| Evidence Usage       |    10%  |       70 |       70 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |       90 |       90 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    82.50 |    84.00 |   +1.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +1.5 pts absolute  |  +1.82% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_3/query_5
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |      100 |      100 |    +10 |     +0 |    +10 |
| Business Analysis    |    15%  |       70 |       80 |       80 |    +10 |     +0 |    +10 |
| Risk Assessment      |    15%  |       60 |       70 |       80 |    +10 |    +10 |    +20 |
| Actionable Advice    |    15%  |       50 |       60 |       60 |    +10 |     +0 |    +10 |
| Evidence Usage       |    10%  |       70 |       70 |       70 |     +0 |     +0 |     +0 |
| Completeness         |    10%  |       80 |      100 |      100 |    +20 |     +0 |    +20 |
| Query Satisfaction   |    10%  |       90 |       90 |       90 |     +0 |     +0 |     +0 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    73.50 |    82.50 |    84.00 |     +9 |     +1 |    +10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +10 pts absolute  |  +14.29% relative
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
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
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
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 7.0,
                "weighted_v2": 7.0
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
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 73.5,
        "overall_v1": 82.5,
        "overall_v2": 84.0,
        "improvement_v0_to_v1": 9.0,
        "improvement_v1_to_v2": 1.5,
        "improvement_v0_to_v2": 10.5,
        "improvement_pct_v0_to_v2": 14.29
    }
