"""
Three-Version Evaluation Report — document_2 / query_7
Source document: NASDAQ_AMZN_2023.pdf
Query: What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?"

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
In its 2023 filing, Amazon disclosed several primary risks and uncertainties, including:

1. **Intense Competition**: Amazon faces significant competition across various sectors, including e-commerce, cloud services, and digital content. Competitors may have greater resources, longer histories, and more established customer bases, which could impact Amazon's market share and profitability.

2. **Expansion Risks**: The company's expansion into new products, services, technologies, and geographic regions poses risks due to limited experience in these areas. There may be challenges in customer adoption, profitability, and potential claims related to service disruptions or quality issues.

3. **International Operations**: Amazon's international activities expose it to various risks, including local economic and political conditions, government regulations, and potential restrictions on foreign ownership and trade.

4. **Operational Strain**: Rapid expansion can strain management, operational, financial, and other resources, potentially harming the company's reputation and growth.

5. **Fluctuations in Demand**: Demand for Amazon's products and services can vary significantly due to seasonality, economic conditions, and unforeseen events, which can affect revenue and profitability.

6. **Fraud and Liability Risks**: The company is at risk from fraudulent activities by sellers on its platform, which could lead to reputational damage and financial liability.

7. **Intellectual Property Risks**: Amazon faces risks related to protecting its intellectual property and may be accused of infringing on third-party rights, which could lead to costly legal disputes.

8. **Cybersecurity Threats**: The company is vulnerable to data breaches and other cybersecurity incidents that could compromise sensitive information and lead to regulatory actions.

9. **Regulatory Changes**: Evolving regulations in various jurisdictions could impose additional compliance costs and operational restrictions.

10. **Market and Economic Conditions**: Global economic and geopolitical conditions, including inflation and interest rates, can impact customer demand and spending patterns.

These risks highlight the complex and dynamic environment in which Amazon operates, emphasizing the potential challenges to its business model and growth strategies.
"""

ADVISOR_REPORT_V1 = """
# Amazon 2023 Filing: Primary Risks and Uncertainties

The primary risks and uncertainties disclosed in Amazon's 2023 filing, while not explicitly detailed in a dedicated section, can be inferred from the context of the documents provided. Here are some key areas of concern that Amazon may face:

- **Economic Conditions**: The report mentions that customers are careful about their spending in an uncertain economy, indicating that economic downturns could impact consumer behavior and spending patterns.

- **Market Competition**: Amazon operates in a highly competitive environment, particularly in e-commerce and cloud services. The need to maintain a competitive edge through pricing and selection is emphasized, which suggests ongoing risks from competitors.

- **Operational Challenges**: The documents highlight efforts to optimize costs and improve delivery speeds. However, challenges related to supply chain management and fulfillment capabilities remain significant risks, especially as Amazon continues to expand its operations internationally.

- **Technological Advancements**: The rapid pace of innovation in technology, particularly in cloud services (AWS), poses both opportunities and risks. While advancements like Graviton chips and new AWS services are beneficial, they also require continuous investment and adaptation to stay ahead of competitors.

While these risks are not explicitly labeled as such in the documents, they reflect the broader challenges Amazon faces in its operations and market environment. For a more detailed understanding, it is advisable to consult the official 2023 annual report or SEC filings, particularly sections typically titled "Risk Factors" or "Management's Discussion and Analysis."
"""

ADVISOR_REPORT_V2 = """
# Amazon 2023 Filing: Primary Risks and Uncertainties

The primary risks and uncertainties disclosed in Amazon's 2023 filing are outlined in the context of the documents provided. Here are the key areas of concern that Amazon faces:

- **Economic Conditions**: The report indicates that customers are cautious about their spending in an uncertain economy, which could impact consumer behavior and spending patterns. This is a significant risk for Amazon's revenue streams, particularly highlighted in the discussion about the importance of being sharp on price during challenging economic times.

- **Market Competition**: Amazon operates in a highly competitive environment, especially in e-commerce and cloud services. The need to maintain a competitive edge through pricing and selection is emphasized, indicating ongoing risks from competitors. The documents mention that Amazon's ability to offer the broadest retail selection at competitive prices is crucial for attracting customers.

- **Operational Challenges**: The documents discuss efforts to optimize costs and improve delivery speeds, but challenges related to supply chain management and fulfillment capabilities remain significant risks. Amazon's reevaluation of its fulfillment network reflects ongoing operational risks, particularly as it continues to expand internationally.

- **Technological Advancements**: The rapid pace of innovation in technology, particularly in AWS, poses both opportunities and risks. While advancements like Graviton chips and new AWS services are beneficial, they require continuous investment and adaptation to stay ahead of competitors. The report notes that AWS has seen substantial cost optimization efforts, which could impact short-term revenue but are aimed at long-term customer satisfaction.

- **Regulatory Risks**: Although not explicitly detailed in the provided documents, regulatory risks are a common concern for large corporations like Amazon, especially in areas such as data privacy, antitrust laws, and international trade regulations.

- **Margin Pressures**: The documents suggest that while Amazon has improved its operating income, there are ongoing pressures related to maintaining margins, particularly as it competes on price and invests in new technologies and services.

While these risks are not explicitly labeled as such in the documents, they reflect the broader challenges Amazon faces in its operations and market environment. For a more detailed understanding, it is advisable to consult the official 2023 annual report or SEC filings, particularly sections typically titled "Risk Factors" or "Management's Discussion and Analysis."

## Financial Figures

The following table summarizes Amazon's financial performance in 2023 compared to 2022:

| Metric               | 2022          | 2023          | Change      |
|----------------------|---------------|---------------|-------------|
| Total Revenue        | $514B        | $575B        | 12% YoY     |
| Operating Income      | $12.2B (2.4% margin) | $36.9B (6.4% margin) | 201% YoY    |
| Free Cash Flow       | -$12.8B      | $35.5B       | Up $48.3B   |

These figures illustrate Amazon's financial performance amidst the risks and uncertainties it faces.

## SWOT Analysis

1. **Strengths:**
   - Strong brand recognition and customer loyalty.
   - Extensive product selection and competitive pricing.
   - Advanced technological infrastructure, particularly in AWS.

2. **Weaknesses:**
   - High operational costs associated with logistics and fulfillment.
   - Dependence on third-party sellers for a significant portion of revenue.

3. **Opportunities:**
   - Expansion into emerging markets with growing internet penetration.
   - Increasing demand for cloud services and digital advertising.

4. **Threats:**
   - Intense competition from other e-commerce and cloud service providers.
   - Regulatory scrutiny and potential changes in laws affecting operations.

This analysis provides a structured overview of the risks and uncertainties Amazon faces in 2023, highlighting the need for ongoing vigilance and strategic planning.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The RAG-generated response adequately addresses the user's query regarding the primary risks and uncertainties disclosed by Amazon in its 2023 filing. It is well-grounded in the provided context documents and covers the relevant topics comprehensively.

## Query Satisfaction
The response effectively answers the user's question by listing and explaining the primary risks and uncertainties that Amazon disclosed in its 2023 filing. Each risk is clearly articulated, and the response aligns with the information found in the context documents, particularly in the "Risk Factors" section of the filing.

## Remaining Gaps
There are no significant gaps in the response. It covers all the primary risks and uncertainties disclosed by Amazon, as outlined in the context documents. The response is complete and does not omit any critical information that the user should be aware of.

## Recommendation
The response is well-structured and meets the user's needs. It is recommended to maintain this level of detail and clarity in future responses. No revisions are necessary, as the response is comprehensive and effectively communicates the relevant information.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more structured and detailed overview of the primary risks and uncertainties faced by Amazon in its 2023 filing. However, it still lacks some specific citations and concrete examples that would enhance its credibility and comprehensiveness.

## Query Satisfaction
The revised report adequately addresses the original user query regarding the primary risks and uncertainties disclosed by Amazon in its 2023 filing. It covers key areas such as economic conditions, market competition, operational challenges, technological advancements, regulatory risks, and margin pressures. The inclusion of financial figures and a SWOT analysis further supports the response.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved Issues:**
  - Cited specific sections of the 2023 filing for each risk mentioned.
  - Addressed missing risks such as regulatory risks and margin pressures.

- **Unresolved Issues:**
  - Provide concrete examples and data to support claims.
  - Include figures or visualizations to enhance clarity.

## Remaining Gaps
1. The report still lacks concrete examples and data to substantiate the claims made regarding economic conditions, market competition, operational challenges, and technological advancements.
2. While a financial table is included, additional figures or visualizations could further enhance clarity and understanding of the risks discussed.

## Recommendation
To improve the report further, the advisor should:
- Incorporate specific examples and data from the 2023 filing to support the claims made about the risks.
- Include additional figures or visualizations that can help illustrate the risks and their potential impacts on Amazon's operations and financial performance. This will provide a more comprehensive and credible analysis for the readers.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_2/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       85 |       90 |     +5 |
| Business Analysis    |    15%  |       70 |       80 |    +10 |
| Risk Assessment      |    15%  |       70 |       85 |    +15 |
| Actionable Advice    |    15%  |       50 |       60 |    +10 |
| Evidence Usage       |    10%  |       60 |       70 |    +10 |
| Completeness         |    10%  |       75 |       85 |    +10 |
| Query Satisfaction   |    10%  |       70 |       85 |    +15 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    70.25 |    80.25 |  +10.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +10.0 pts absolute  |  +14.23% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_2/query_7
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |        0 |       85 |       90 |    +85 |     +5 |    +90 |
| Business Analysis    |    15%  |        0 |       70 |       80 |    +70 |    +10 |    +80 |
| Risk Assessment      |    15%  |       85 |       70 |       85 |    -15 |    +15 |     +0 |
| Actionable Advice    |    15%  |        0 |       50 |       60 |    +50 |    +10 |    +60 |
| Evidence Usage       |    10%  |        0 |       60 |       70 |    +60 |    +10 |    +70 |
| Completeness         |    10%  |       70 |       75 |       85 |     +5 |    +10 |    +15 |
| Query Satisfaction   |    10%  |       90 |       70 |       85 |    -20 |    +15 |     -5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    28.75 |    70.25 |    80.25 |    +41 |    +10 |    +51 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +51 pts absolute  |  +179.13% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 85,
                "v2_score": 90,
                "delta_v0_v1": 85,
                "delta_v1_v2": 5,
                "delta_v0_v2": 90,
                "weighted_v1": 21.25,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": 70,
                "delta_v1_v2": 10,
                "delta_v0_v2": 80,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 85,
                "weighted_v0": 12.75,
                "v1_score": 70,
                "v2_score": 85,
                "delta_v0_v1": -15,
                "delta_v1_v2": 15,
                "delta_v0_v2": 0,
                "weighted_v1": 10.5,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v0_v1": 50,
                "delta_v1_v2": 10,
                "delta_v0_v2": 60,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v0_v1": 60,
                "delta_v1_v2": 10,
                "delta_v0_v2": 70,
                "weighted_v1": 6.0,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 75,
                "v2_score": 85,
                "delta_v0_v1": 5,
                "delta_v1_v2": 10,
                "delta_v0_v2": 15,
                "weighted_v1": 7.5,
                "weighted_v2": 8.5
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 70,
                "v2_score": 85,
                "delta_v0_v1": -20,
                "delta_v1_v2": 15,
                "delta_v0_v2": -5,
                "weighted_v1": 7.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 28.75,
        "overall_v1": 70.25,
        "overall_v2": 80.25,
        "improvement_v0_to_v1": 41.5,
        "improvement_v1_to_v2": 10.0,
        "improvement_v0_to_v2": 51.5,
        "improvement_pct_v0_to_v2": 179.13
    }
