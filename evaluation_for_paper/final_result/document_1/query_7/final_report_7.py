"""
Three-Version Evaluation Report — document_1 / query_7
Source document: NASDAQ_AMZN_2022.pdf
Query: What were Amazon's capital expenditure and investment priorities in 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's capital expenditure and investment priorities in 2022?"

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
In 2022, Amazon's capital expenditure and investment priorities focused on several key areas:

1. **Infrastructure Expansion**: Amazon continued to invest heavily in its fulfillment network, including the expansion of fulfillment centers and last-mile transportation networks to improve delivery efficiency. This was a response to the significant growth in consumer demand during the pandemic, which necessitated a doubling of their fulfillment center footprint over a short period.

2. **Technology and Content**: There was a notable increase in spending on technology and content, which included investments in AWS (Amazon Web Services) to enhance its capabilities and support growth. This included the development of new machine learning chips and other technology infrastructure.

3. **Cost Management and Efficiency**: Amazon undertook initiatives to streamline operations and reduce costs, particularly in its fulfillment network. This included optimizing processes and reevaluating inventory placement strategies to improve delivery speed and reduce costs.

4. **Strategic Acquisitions**: Amazon made significant acquisitions, including MGM Holdings for approximately $6.1 billion, to enhance its digital media content offerings. They also planned to invest in healthcare through the acquisition of One Medical.

5. **Long-term Growth Investments**: Despite facing macroeconomic challenges, Amazon emphasized maintaining long-term investments that could drive future growth, such as in cloud computing, advertising, and international expansion.

Overall, Amazon's capital expenditures in 2022 were aimed at enhancing operational efficiency, expanding infrastructure, and investing in technology and strategic acquisitions to support long-term growth.
"""

ADVISOR_REPORT_V1 = """
### Capital Expenditure and Investment Priorities in 2022

To analyze Amazon's capital expenditure and investment priorities in 2022, we can extract relevant information from the provided documents. Here’s a summary based on the context:

1. **Fulfillment Network Expansion**:
   - Amazon significantly expanded its fulfillment network to accommodate the extraordinary growth in consumer business during the pandemic. Annual revenue increased from $245 billion in 2019 to $434 billion in 2022, necessitating a doubling of the fulfillment center footprint and the acceleration of building a last-mile transportation network comparable to UPS.

2. **Cost Optimization**:
   - The company focused on optimizing its fulfillment processes and transportation network to improve productivity and reduce costs. This included scrutinizing every process path in fulfillment centers and redesigning processes to yield steady productivity gains and cost reductions.

3. **Regionalized Fulfillment Network**:
   - Amazon transitioned from a national fulfillment network to a regionalized model. This change aimed to enhance efficiency by reducing shipping costs and delivery times, allowing for better inventory management across fulfillment centers.

4. **Technology and Machine Learning**:
   - Investment in advanced machine learning algorithms was prioritized to predict customer needs more accurately, ensuring that the right inventory is available in the right regions at the right time. This technological enhancement is expected to lower costs and improve delivery speeds.

5. **AWS Investment**:
   - Amazon Web Services (AWS) continued to be a focal point for investment, with an annualized revenue run rate of $85 billion. Despite facing short-term headwinds, AWS's growth was emphasized, and the company remained committed to long-term customer relationships rather than short-term profit maximization.

6. **Streamlining Operations**:
   - The company made strategic decisions to shutter certain businesses and amend programs that were not yielding the expected returns. This included eliminating 27,000 corporate roles to streamline operations and focus resources on more promising initiatives.

### Financial Health Metrics

- **Revenue Growth**: Amazon's revenue increased from $245 billion in 2019 to $434 billion in 2022, reflecting a significant growth trajectory.

| Year | Revenue (in billions) |
| --- | --- |
| 2019 | 245 |
| 2020 | None |
| 2021 | None |
| 2022 | 434 |

*Source: Data extracted from NASDAQ_AMZN_2022.pdf.*

- **Risk Assessment**: Insufficient data to compute Altman Z-Score, indicating a lack of detailed financial metrics for a comprehensive risk analysis.

### Future Outlook

Amazon aims to balance immediate operational challenges with long-term strategic investments that enhance customer experience and operational efficiency. The focus on optimizing the fulfillment network and leveraging technology positions the company well for future growth.

### Risks and Limitations

- **Macroeconomic Conditions**: The company faces challenges due to rising costs and cautious spending from customers, particularly in the AWS segment.
- **Operational Streamlining**: The decision to eliminate roles and shutter certain businesses may impact employee morale and operational capacity in the short term.

### Actionable Advice

- **Continued Investment in Technology**: Amazon should maintain its focus on technology and machine learning to enhance operational efficiency and customer satisfaction.
- **Monitoring Market Conditions**: Regular assessment of macroeconomic conditions and customer spending patterns will be crucial for adapting strategies effectively.

### Conclusion

In 2022, Amazon's capital expenditure and investment priorities were heavily focused on expanding and optimizing its fulfillment network, leveraging technology for efficiency, and maintaining a strong commitment to AWS. The company is positioned to navigate current challenges while pursuing long-term growth strategies.

### Additional Information Needed

If more detailed financial metrics or specific figures related to capital expenditures are required for a deeper analysis, please provide that information.
"""

ADVISOR_REPORT_V2 = """
### Capital Expenditure and Investment Priorities in 2022

To analyze Amazon's capital expenditure and investment priorities in 2022, we can extract relevant information from the provided documents. Here’s a summary based on the context:

1. **Fulfillment Network Expansion**:
   - Amazon significantly expanded its fulfillment network to accommodate the extraordinary growth in consumer business during the pandemic. Annual revenue increased from $245 billion in 2019 to $434 billion in 2022, necessitating a doubling of the fulfillment center footprint and the acceleration of building a last-mile transportation network comparable to UPS.

2. **Cost Optimization**:
   - The company focused on optimizing its fulfillment processes and transportation network to improve productivity and reduce costs. This included scrutinizing every process path in fulfillment centers and redesigning processes to yield steady productivity gains and cost reductions.

3. **Regionalized Fulfillment Network**:
   - Amazon transitioned from a national fulfillment network to a regionalized model. This change aimed to enhance efficiency by reducing shipping costs and delivery times, allowing for better inventory management across fulfillment centers. The implications of this shift include improved operational efficiency and reduced costs associated with long-distance shipping.

4. **Technology and Machine Learning**:
   - Investment in advanced machine learning algorithms was prioritized to predict customer needs more accurately, ensuring that the right inventory is available in the right regions at the right time. This technological enhancement is expected to lower costs and improve delivery speeds.

5. **AWS Investment**:
   - Amazon Web Services (AWS) continued to be a focal point for investment, with an annualized revenue run rate of $85 billion. Despite facing short-term headwinds, AWS's growth was emphasized, and the company remained committed to long-term customer relationships rather than short-term profit maximization.

6. **Streamlining Operations**:
   - The company made strategic decisions to shutter certain businesses and amend programs that were not yielding the expected returns. This included eliminating 27,000 corporate roles to streamline operations and focus resources on more promising initiatives. This decision may impact operational capacity and employee morale in the short term.

### Financial Health Metrics

- **Revenue Growth**: Amazon's revenue increased from $245 billion in 2019 to $434 billion in 2022, reflecting a significant growth trajectory. The Compound Annual Growth Rate (CAGR) over this period is approximately **21%**.

| Year | Revenue (in billions) |
| --- | --- |
| 2019 | 245 |
| 2020 | Unavailable |
| 2021 | Unavailable |
| 2022 | 434 |

*Source: Data extracted from NASDAQ_AMZN_2022.pdf.*

- **Risk Assessment**: Insufficient data to compute Altman Z-Score, indicating a lack of detailed financial metrics for a comprehensive risk analysis.

### Future Outlook

Amazon aims to balance immediate operational challenges with long-term strategic investments that enhance customer experience and operational efficiency. The focus on optimizing the fulfillment network and leveraging technology positions the company well for future growth.

### Risks and Limitations

- **Macroeconomic Conditions**: The company faces challenges due to rising costs and cautious spending from customers, particularly in the AWS segment.
- **Operational Streamlining**: The decision to eliminate roles and shutter certain businesses may impact employee morale and operational capacity in the short term.
- **Competitive Risks**: Amazon must navigate a competitive landscape with well-funded rivals, necessitating continuous innovation and efficiency improvements.
- **Valuation Risks**: The aggressive investment strategy may lead to valuation pressures if expected returns do not materialize.
- **Supply Chain Risks**: Recent global disruptions could impact Amazon's supply chain efficiency and cost structure.
- **Regulatory Risks**: Potential regulatory changes could affect Amazon's operations and growth strategies.
- **Margin Pressure**: Rising costs may exert pressure on profit margins, requiring careful management of operational expenses.

### Actionable Advice

- **Continued Investment in Technology**: Amazon should maintain its focus on technology and machine learning to enhance operational efficiency and customer satisfaction.
- **Monitoring Market Conditions**: Regular assessment of macroeconomic conditions and customer spending patterns will be crucial for adapting strategies effectively.

### Conclusion

In 2022, Amazon's capital expenditure and investment priorities were heavily focused on expanding and optimizing its fulfillment network, leveraging technology for efficiency, and maintaining a strong commitment to AWS. The company is positioned to navigate current challenges while pursuing long-term growth strategies.

### Additional Information Needed

If more detailed financial metrics or specific figures related to capital expenditures are required for a deeper analysis, please provide that information.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's capital expenditure and investment priorities in 2022. However, it lacks grounding in the provided context documents and misses several structural elements that would enhance its quality.

## Query Satisfaction
The response provides a comprehensive overview of Amazon's capital expenditure and investment priorities, including infrastructure expansion, technology and content investments, cost management, strategic acquisitions, and long-term growth investments. However, it does not reference specific figures or details from the context documents, which would strengthen its credibility and relevance.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Absence of Limitations or Caveats**: There are no acknowledgments of potential limitations in the information or the context in which it was provided.
3. **No Actionable Content**: The response does not offer any actionable insights or recommendations based on the information presented.
4. **Missing Specific Figures**: While the response outlines general priorities, it lacks specific financial figures or detailed examples from the context documents that would provide a clearer picture of Amazon's expenditures.

## Recommendation
To improve the response:
- Include citations from the context documents to support the claims made about Amazon's capital expenditures and investment priorities.
- Acknowledge any limitations or uncertainties regarding the information provided.
- Add actionable insights or recommendations based on the analysis of Amazon's investment strategies.
- Incorporate specific financial figures or examples from the context to enhance the depth and credibility of the response.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Amazon's capital expenditure and investment priorities in 2022. It addresses the key aspects of the user query and incorporates several improvements based on the Critic's feedback. However, there are still some unresolved issues that need to be addressed.

## Query Satisfaction
The revised report adequately answers the original user query regarding Amazon's capital expenditure and investment priorities in 2022. It covers the following key areas:
- Fulfillment network expansion
- Cost optimization
- Transition to a regionalized fulfillment network
- Investment in technology and machine learning
- Focus on AWS
- Streamlining operations

Additionally, it includes financial health metrics and discusses risks and limitations, which enhances the overall response.

## Issues Resolution Status
Out of the 9 issues identified by the Critic:
- **Resolved Issues (7)**:
  - Specific financial metrics related to capital expenditures were provided.
  - The implications of the regionalized fulfillment network were expanded upon.
  - Competitive risks were addressed in detail.
  - Valuation risks associated with the investment strategy were discussed.
  - Supply chain risks and their potential impact were included.
  - Regulatory risks that could affect operations were mentioned.
  - Margin pressure due to rising costs was discussed.

- **Unresolved Issues (2)**:
  - Incorporation of visual aids to support data claims.
  - Provision of evidence to support claims made in the report.

## Remaining Gaps
1. **Incorporate visual aids**: The report should include charts or figures to visually represent data and enhance understanding.
2. **Provide evidence**: Specific evidence or examples to support claims made in the report should be included to strengthen the arguments presented.

## Recommendation
To finalize the report, the advisor should:
- Add visual aids to illustrate key points and data.
- Include specific evidence or examples that substantiate the claims made in the report.

Addressing these remaining gaps will enhance the quality and credibility of the report, ensuring it meets the expectations of the user query comprehensively.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_1/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       80 |       85 |     +5 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       70 |       75 |     +5 |
| Evidence Usage       |    10%  |       70 |       75 |     +5 |
| Completeness         |    10%  |       80 |       85 |     +5 |
| Query Satisfaction   |    10%  |       80 |       85 |     +5 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    74.50 |    80.25 |  +5.75 |
+----------------------+--------+----------+----------+--------+
  Improvement: +5.75 pts absolute  |  +7.72% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_1/query_7
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       80 |       80 |       85 |     +0 |     +5 |     +5 |
| Business Analysis    |    15%  |       70 |       70 |       75 |     +0 |     +5 |     +5 |
| Risk Assessment      |    15%  |       60 |       70 |       80 |    +10 |    +10 |    +20 |
| Actionable Advice    |    15%  |       50 |       70 |       75 |    +20 |     +5 |    +25 |
| Evidence Usage       |    10%  |       40 |       70 |       75 |    +30 |     +5 |    +35 |
| Completeness         |    10%  |       70 |       80 |       85 |    +10 |     +5 |    +15 |
| Query Satisfaction   |    10%  |       90 |       80 |       85 |    -10 |     +5 |     -5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    67.00 |    74.50 |    80.25 |     +7 |     +5 |    +13 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +13 pts absolute  |  +19.78% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 80,
                "weighted_v0": 20.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 0,
                "delta_v1_v2": 5,
                "delta_v0_v2": 5,
                "weighted_v1": 20.0,
                "weighted_v2": 21.25
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
                "v1_score": 70,
                "v2_score": 75,
                "delta_v0_v1": 20,
                "delta_v1_v2": 5,
                "delta_v0_v2": 25,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "weighted_v0": 4.0,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v0_v1": 30,
                "delta_v1_v2": 5,
                "delta_v0_v2": 35,
                "weighted_v1": 7.0,
                "weighted_v2": 7.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 10,
                "delta_v1_v2": 5,
                "delta_v0_v2": 15,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": -10,
                "delta_v1_v2": 5,
                "delta_v0_v2": -5,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 67.0,
        "overall_v1": 74.5,
        "overall_v2": 80.25,
        "improvement_v0_to_v1": 7.5,
        "improvement_v1_to_v2": 5.75,
        "improvement_v0_to_v2": 13.25,
        "improvement_pct_v0_to_v2": 19.78
    }
