"""
Three-Version Evaluation Report — document_5 / query_7
Source document: NASDAQ_TSLA_2022.pdf
Query: How did supply chain challenges impact Tesla's production in 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did supply chain challenges impact Tesla's production in 2022?"

USER_QUERIES = [
    "What were Tesla's total revenues and net income for fiscal year 2022?",
    "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?",
    "What were the key financial ratios and margins for Tesla in 2022?",
    "How did Tesla's energy generation and storage segment perform in 2022?",
    "What were the main risks Tesla identified in its 2022 annual report?",
    "What were Tesla's capital expenditures and free cash flow in 2022?",
    "How did supply chain challenges impact Tesla's production in 2022?",
    "What is Tesla's growth strategy and future product roadmap as outlined in 2022?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2022, supply chain challenges significantly impacted Tesla's production due to several factors. The ongoing effects of the COVID-19 pandemic led to intermittent supplier shutdowns and delays, exacerbating existing issues such as port congestion and a global semiconductor shortage. These challenges resulted in increased expenses to expedite the delivery of critical parts and contributed to temporary shutdowns at Gigafactory Shanghai, which directly affected production capabilities.

Despite these obstacles, Tesla managed to produce 1,369,611 consumer vehicles and deliver 1,313,851 vehicles throughout the year. However, the company faced idle capacity charges related to the temporary suspension of production at Gigafactory Shanghai and the ramping up of production at new facilities like Gigafactory Texas and Gigafactory Berlin-Brandenburg. Additionally, the need to procure components quickly due to production ramp-ups and the reliance on single-source suppliers posed further risks to production continuity.

Overall, while Tesla continued to grow its production and delivery numbers, the supply chain challenges led to increased costs, production delays, and operational complexities that the company had to navigate throughout 2022.
"""

ADVISOR_REPORT_V1 = """
# Tesla's Production Impact from Supply Chain Challenges in 2022

In 2022, Tesla faced significant supply chain challenges that impacted its production capabilities. While the available documents do not provide specific production numbers or timelines, they highlight the broader context of these challenges.

The company acknowledged that supply chain constraints, including those stemming from the COVID-19 pandemic, could affect its operations and production capacity. These constraints may have influenced Tesla's ability to meet demand for its vehicles, particularly as it continued to ramp up production of its various models, including the Model 3, Model Y, Model S, Model X, and the newly introduced Tesla Semi.

Despite these challenges, Tesla has been proactive in addressing supply chain issues by leveraging its technological advancements in battery and powertrain manufacturing. The company has developed proprietary battery technologies aimed at increasing supply and reducing costs, which may help mitigate some of the impacts of supply chain disruptions.

For a more comprehensive analysis, specific production figures and timelines would be beneficial. If you have access to additional documents or sources that might contain this information, please provide them, and I can assist you further.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Production Impact from Supply Chain Challenges in 2022

In 2022, Tesla faced significant supply chain challenges that impacted its production capabilities. The company acknowledged that supply chain constraints, including those stemming from the COVID-19 pandemic, could affect its operations and production capacity. These constraints may have influenced Tesla's ability to meet demand for its vehicles, particularly as it continued to ramp up production of its various models, including the Model 3, Model Y, Model S, Model X, and the newly introduced Tesla Semi.

While specific production numbers and timelines are not available in the current context, it is clear that these challenges had a notable effect on Tesla's overall production strategy. The company has been proactive in addressing supply chain issues by leveraging its technological advancements in battery and powertrain manufacturing. Tesla has developed proprietary battery technologies aimed at increasing supply and reducing costs, which may help mitigate some of the impacts of supply chain disruptions. However, details on how these advancements directly addressed the supply chain issues faced in 2022 are not provided.

Additionally, several key investor risks remain relevant in the context of supply chain challenges:

- **Competition**: The competitive landscape may impact Tesla's market position amid supply chain challenges, especially as competitors may capitalize on these disruptions to gain market share.
  
- **Valuation**: Supply chain issues could influence Tesla's valuation and investor sentiment, potentially leading to fluctuations in stock prices as investors react to production capabilities and market demand.

- **Regulation**: Potential regulatory risks arising from supply chain disruptions, such as compliance with environmental standards and trade regulations, are also critical to consider.

- **Margin Pressure**: The possibility of increased costs due to supply chain issues could affect profit margins, as higher material costs or delays in production may lead to reduced profitability.

For a more comprehensive analysis, specific production figures and timelines would be beneficial. Unfortunately, this information is currently unavailable. If you have access to additional documents or sources that might contain this information, please provide them, and I can assist you further.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the impact of supply chain challenges on Tesla's production in 2022. It is grounded in the provided context documents, highlighting key issues such as the COVID-19 pandemic, semiconductor shortages, and production delays. However, it lacks some structural elements that could enhance clarity and completeness.

## Query Satisfaction
The response effectively answers the user's question by detailing how supply chain challenges affected Tesla's production. It mentions specific factors such as supplier shutdowns, port congestion, and the semiconductor shortage, which are relevant to the query. The production figures provided also support the narrative of overcoming these challenges. Overall, the response meets the user's informational needs.

## Remaining Gaps
1. **Actionable Content**: The response does not provide actionable insights or recommendations for the user, which could enhance its utility.
2. **Structured Sections**: The absence of structured sections (e.g., headings or bullet points) makes it less readable and harder to navigate for the user.

## Recommendation
To improve the response, consider adding structured sections to enhance readability and including actionable insights or recommendations based on the information provided. This would make the response more user-friendly and comprehensive.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of how supply chain challenges impacted Tesla's production in 2022 compared to the initial version. However, it still lacks the inclusion of relevant figures or charts to support its claims.

## Query Satisfaction
The revised report adequately addresses the user query regarding the impact of supply chain challenges on Tesla's production in 2022. It discusses the constraints faced by Tesla, the proactive measures taken, and outlines key investor risks related to these challenges. However, it does not provide specific production figures or timelines, which would enhance the response.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Included a discussion on specific production figures and timelines related to supply chain challenges (though still lacking actual figures).
  2. Clarified how Tesla's technological advancements mitigate supply chain disruptions.
  3. Addressed missing investor risks: competition, valuation, regulation, and margin pressure.
  
- **Unresolved**:
  1. Embed relevant figures or charts to support claims made in the report.

## Remaining Gaps
1. The report still lacks embedded figures or charts that would provide visual support for the claims made regarding production impacts and supply chain challenges.

## Recommendation
It is recommended that the advisor further revise the report to include relevant figures or charts that illustrate the impact of supply chain challenges on Tesla's production in 2022. This addition would enhance the report's clarity and provide a more robust analysis for the reader.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       60 |       70 |    +10 |
| Risk Assessment      |    15%  |       50 |       70 |    +20 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       70 |       80 |    +10 |
| Query Satisfaction   |    10%  |       70 |       80 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    30.50 |    37.00 |   +6.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +6.5 pts absolute  |  +21.31% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_5/query_7
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
| Business Analysis    |    15%  |       70 |       60 |       70 |    -10 |    +10 |     +0 |
| Risk Assessment      |    15%  |       80 |       50 |       70 |    -30 |    +20 |    -10 |
| Actionable Advice    |    15%  |       50 |        0 |        0 |    -50 |     +0 |    -50 |
| Evidence Usage       |    10%  |       60 |        0 |        0 |    -60 |     +0 |    -60 |
| Completeness         |    10%  |       80 |       70 |       80 |    -10 |    +10 |     +0 |
| Query Satisfaction   |    10%  |       90 |       70 |       80 |    -20 |    +10 |    -10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    75.50 |    30.50 |    37.00 |    -45 |     +6 |    -38 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -38 pts absolute  |  -50.99% relative
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
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v0_v1": -10,
                "delta_v1_v2": 10,
                "delta_v0_v2": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 80,
                "weighted_v0": 12.0,
                "v1_score": 50,
                "v2_score": 70,
                "delta_v0_v1": -30,
                "delta_v1_v2": 20,
                "delta_v0_v2": -10,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -50,
                "delta_v1_v2": 0,
                "delta_v0_v2": -50,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -60,
                "delta_v1_v2": 0,
                "delta_v0_v2": -60,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
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
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": -20,
                "delta_v1_v2": 10,
                "delta_v0_v2": -10,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v0": 75.5,
        "overall_v1": 30.5,
        "overall_v2": 37.0,
        "improvement_v0_to_v1": -45.0,
        "improvement_v1_to_v2": 6.5,
        "improvement_v0_to_v2": -38.5,
        "improvement_pct_v0_to_v2": -50.99
    }
