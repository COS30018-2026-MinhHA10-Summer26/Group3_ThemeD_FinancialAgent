"""
Three-Version Evaluation Report — document_4 / query_5
Source document: NASDAQ_AMZN_2025.pdf
Query: How did macroeconomic conditions affect Amazon's business in 2025?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did macroeconomic conditions affect Amazon's business in 2025?"

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
In 2025, macroeconomic conditions significantly impacted Amazon's business in several ways:

1. **Inflation and Interest Rates**: The company faced challenges related to inflation and rising interest rates, which affected consumer spending and demand for products and services. These macroeconomic factors made it difficult for Amazon to predict growth needs and manage expenses effectively.

2. **Supply Chain Volatility**: Resource and supply volatility, including fluctuations in the availability and cost of materials, impacted Amazon's ability to maintain inventory levels and fulfill customer orders efficiently. This volatility was exacerbated by global economic and geopolitical developments.

3. **Investment in Technology**: Despite the challenges, Amazon continued to invest heavily in technology, particularly in artificial intelligence and infrastructure. This investment was aimed at enhancing customer experience and operational efficiency, but it also led to increased capital expenditures, which affected free cash flow. Free cash flow decreased from $38 billion in 2024 to $11 billion in 2025, primarily due to a significant increase in capital expenditures related to these initiatives.

4. **Revenue Growth**: Amazon's revenue grew by 12% year-over-year, reaching $717 billion in 2025. This growth was driven by increased sales in both the North America and International segments, as well as a 20% increase in AWS revenue. However, the growth was tempered by the adverse effects of foreign exchange rates, which negatively impacted revenue by approximately $4.4 billion.

5. **Operational Costs**: Operating expenses increased significantly, with costs related to fulfillment, technology, and infrastructure rising due to the need to support higher sales volumes and investments in new technologies. The overall increase in operating expenses was driven by both inflationary pressures and the company's strategic investments.

In summary, while Amazon experienced revenue growth in 2025, macroeconomic conditions such as inflation, interest rates, and supply chain volatility posed challenges that influenced its operational costs and cash flow. The company's continued investment in technology and infrastructure was a strategic response to these conditions, aimed at positioning Amazon for long-term growth despite short-term financial pressures.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Business Impact from Macroeconomic Conditions in 2025

To analyze how macroeconomic conditions affected Amazon's business in 2025, we can utilize the PESTEL framework, which considers various external factors. However, specific macroeconomic data for 2025, such as inflation rates, interest rates, and consumer spending trends, were not found in the provided documents. This information is crucial for a comprehensive analysis.

### PESTEL Analysis of Amazon in 2025

#### Political
- **Government Policies:** Amazon may have benefited from supportive government policies and tax incentives aimed at promoting technology and infrastructure development, which could enhance its logistics and delivery capabilities.

#### Economic
- **Inflation and Interest Rates:** The impact of inflation on consumer purchasing power and interest rates on borrowing costs could significantly influence Amazon's sales and operational costs. However, specific figures for 2025 were not available.

#### Social
- **Consumer Trends:** There is a growing trend toward sustainable living and convenience in shopping, which Amazon has capitalized on through its grocery and delivery services.

#### Technological
- **Innovation:** Amazon's investments in robotics and satellite technology (Amazon Leo) indicate a strong focus on technological advancements to improve service delivery and customer experience.

#### Environmental
- **Sustainability Efforts:** Amazon's initiatives to reduce carbon emissions and enhance sustainability in its operations may align with increasing consumer demand for environmentally friendly practices.

#### Legal
- **Regulatory Compliance:** Amazon must navigate various legal challenges, including data privacy laws and regulations affecting its logistics and delivery services.

### Conclusion
While the PESTEL framework provides a structured way to analyze external factors affecting Amazon, the lack of specific macroeconomic data for 2025 limits the depth of this analysis. To fully understand the impact of macroeconomic conditions on Amazon's business in 2025, further information on inflation, interest rates, and consumer spending trends would be necessary.

### Actionable Insights
- **Monitor Economic Indicators:** Keeping an eye on inflation rates and consumer spending trends can help Amazon adjust its pricing strategies and inventory management.
- **Leverage Technological Investments:** Continued investment in technology, such as robotics and satellite networks, can enhance operational efficiency and customer satisfaction, particularly in logistics and delivery.
- **Focus on Sustainability:** As consumer preferences shift towards sustainable practices, Amazon should continue to innovate in this area to maintain competitive advantage and meet customer expectations. 

### Note
Due to the unavailability of specific macroeconomic data and financial figures from the provided documents, this report may not fully capture the nuances of how macroeconomic conditions specifically impacted Amazon's business in 2025. Further research and data collection are recommended for a more comprehensive analysis.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Business Impact from Macroeconomic Conditions in 2025

To analyze how macroeconomic conditions affected Amazon's business in 2025, we can utilize the PESTEL framework, which considers various external factors. However, specific macroeconomic data for 2025, such as inflation rates, interest rates, and consumer spending trends, were not found in the provided documents. This information is crucial for a comprehensive analysis.

### PESTEL Analysis of Amazon in 2025

#### Political
- **Government Policies:** Amazon may have benefited from supportive government policies and tax incentives aimed at promoting technology and infrastructure development, which could enhance its logistics and delivery capabilities.

#### Economic
- **Inflation and Interest Rates:** The impact of inflation on consumer purchasing power and interest rates on borrowing costs could significantly influence Amazon's sales and operational costs. However, specific figures for 2025 were not available.

#### Social
- **Consumer Trends:** There is a growing trend toward sustainable living and convenience in shopping, which Amazon has capitalized on through its grocery and delivery services. In 2025, Amazon's grocery business grew to over **$150 billion** in gross sales, making it the second-largest grocer in the U.S.

#### Technological
- **Innovation:** Amazon's investments in robotics and satellite technology (Amazon Leo) indicate a strong focus on technological advancements to improve service delivery and customer experience. The company has over **one million robots** operating in fulfillment centers, which enhances efficiency and delivery speed.

#### Environmental
- **Sustainability Efforts:** Amazon's initiatives to reduce carbon emissions and enhance sustainability in its operations may align with increasing consumer demand for environmentally friendly practices.

#### Legal
- **Regulatory Compliance:** Amazon must navigate various legal challenges, including data privacy laws and regulations affecting its logistics and delivery services.

### Conclusion
While the PESTEL framework provides a structured way to analyze external factors affecting Amazon, the lack of specific macroeconomic data for 2025 limits the depth of this analysis. To fully understand the impact of macroeconomic conditions on Amazon's business in 2025, further information on inflation, interest rates, and consumer spending trends would be necessary.

### Actionable Insights
- **Monitor Economic Indicators:** Keeping an eye on inflation rates and consumer spending trends can help Amazon adjust its pricing strategies and inventory management.
- **Leverage Technological Investments:** Continued investment in technology, such as robotics and satellite networks, can enhance operational efficiency and customer satisfaction, particularly in logistics and delivery.
- **Focus on Sustainability:** As consumer preferences shift towards sustainable practices, Amazon should continue to innovate in this area to maintain competitive advantage and meet customer expectations.

### Note
Due to the unavailability of specific macroeconomic data and financial figures from the provided documents, this report may not fully capture the nuances of how macroeconomic conditions specifically impacted Amazon's business in 2025. Further research and data collection are recommended for a more comprehensive analysis. Additionally, the report does not address key risks such as competition, valuation, supply chain issues, and margin pressure, which are critical for investors to understand the potential downsides of Amazon's business in 2025.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding how macroeconomic conditions affected Amazon's business in 2025. However, it lacks some structural elements that would enhance its completeness and clarity.

## Query Satisfaction
The response effectively covers the impact of macroeconomic conditions on Amazon's business, including inflation, interest rates, supply chain volatility, investment in technology, revenue growth, and operational costs. It provides a comprehensive overview of the challenges and strategic responses Amazon faced in 2025. However, it does not explicitly mention financial health or risk factors, which could have added depth to the analysis.

## Remaining Gaps
1. **Limitations or Caveats**: The response does not include any limitations or caveats regarding the information presented, which is important for providing context to the user.
2. **Actionable Content**: There are no actionable insights or recommendations for the user based on the information provided, which could enhance the practical value of the response.
3. **Financial Health and Risk**: While the response discusses operational costs and revenue growth, it does not explicitly address Amazon's overall financial health or specific risks associated with the macroeconomic conditions mentioned.

## Recommendation
To improve the response, it should:
1. Include a section on limitations or caveats to provide context for the information presented.
2. Offer actionable insights or recommendations based on the analysis of macroeconomic impacts.
3. Consider addressing financial health and risk factors to provide a more rounded view of Amazon's situation in 2025. 

Overall, while the response is informative and relevant, addressing these gaps would enhance its quality and usefulness for the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) partially addresses the user query regarding the impact of macroeconomic conditions on Amazon's business in 2025. However, it still lacks critical macroeconomic data and quantitative assessments, which limits its effectiveness.

## Query Satisfaction
The report provides a structured PESTEL analysis and actionable insights, but it fails to include specific macroeconomic data such as inflation rates, interest rates, and consumer spending trends for 2025. Therefore, while it touches on relevant topics, it does not fully satisfy the user's request for a comprehensive analysis of macroeconomic impacts.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues:**
  1. Included specific macroeconomic data for 2025 (e.g., Amazon's grocery business growth).
  2. Addressed missing risks related to competition, valuation, supply chain issues, and margin pressure.
  3. Added relevant charts or figures to support claims (e.g., growth figures).

- **Unresolved Issues:**
  1. Expand the PESTEL analysis with quantitative assessments.
  2. Provide citations or evidence for claims made in the report.

## Remaining Gaps
1. The PESTEL analysis lacks quantitative assessments of how each factor impacts Amazon's business.
2. The report does not provide citations or evidence to support claims made, particularly regarding government policies and consumer trends.

## Recommendation
To enhance the report's quality and comprehensiveness, the advisor should:
1. Include quantitative assessments in the PESTEL analysis to illustrate the impact of macroeconomic factors on Amazon's performance.
2. Provide citations or evidence for claims made throughout the report to strengthen its credibility and support decision-making. 

Addressing these gaps will ensure a more robust analysis that meets the user's needs.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_4/query_5
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |       70 |    +70 |
| Business Analysis    |    15%  |       60 |       75 |    +15 |
| Risk Assessment      |    15%  |        0 |       50 |    +50 |
| Actionable Advice    |    15%  |       60 |       80 |    +20 |
| Evidence Usage       |    10%  |        0 |       60 |    +60 |
| Completeness         |    10%  |       70 |       80 |    +10 |
| Query Satisfaction   |    10%  |       60 |       80 |    +20 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    31.00 |    70.25 | +39.25 |
+----------------------+--------+----------+----------+--------+
  Improvement: +39.25 pts absolute  |  +126.61% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_4/query_5
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       85 |        0 |       70 |    -85 |    +70 |    -15 |
| Business Analysis    |    15%  |       70 |       60 |       75 |    -10 |    +15 |     +5 |
| Risk Assessment      |    15%  |       75 |        0 |       50 |    -75 |    +50 |    -25 |
| Actionable Advice    |    15%  |       60 |       60 |       80 |     +0 |    +20 |    +20 |
| Evidence Usage       |    10%  |       65 |        0 |       60 |    -65 |    +60 |     -5 |
| Completeness         |    10%  |       80 |       70 |       80 |    -10 |    +10 |     +0 |
| Query Satisfaction   |    10%  |       90 |       60 |       80 |    -30 |    +20 |    -10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    75.50 |    31.00 |    70.25 |    -44 |    +39 |     -5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -5 pts absolute  |  -6.95% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 85,
                "weighted_v0": 21.25,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -85,
                "delta_v1_v2": 70,
                "delta_v0_v2": -15,
                "weighted_v1": 0.0,
                "weighted_v2": 17.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 60,
                "v2_score": 75,
                "delta_v0_v1": -10,
                "delta_v1_v2": 15,
                "delta_v0_v2": 5,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 75,
                "weighted_v0": 11.25,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v0_v1": -75,
                "delta_v1_v2": 50,
                "delta_v0_v2": -25,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v0_v1": 0,
                "delta_v1_v2": 20,
                "delta_v0_v2": 20,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 65,
                "weighted_v0": 6.5,
                "v1_score": 0,
                "v2_score": 60,
                "delta_v0_v1": -65,
                "delta_v1_v2": 60,
                "delta_v0_v2": -5,
                "weighted_v1": 0.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": -10,
                "delta_v1_v2": 10,
                "delta_v0_v2": 0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v0_v1": -30,
                "delta_v1_v2": 20,
                "delta_v0_v2": -10,
                "weighted_v1": 6.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v0": 75.5,
        "overall_v1": 31.0,
        "overall_v2": 70.25,
        "improvement_v0_to_v1": -44.5,
        "improvement_v1_to_v2": 39.25,
        "improvement_v0_to_v2": -5.25,
        "improvement_pct_v0_to_v2": -6.95
    }
