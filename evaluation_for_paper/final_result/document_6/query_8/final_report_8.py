"""
Three-Version Evaluation Report — document_6 / query_8
Source document: NASDAQ_TSLA_2023.pdf
Query: What is Tesla's outlook for new vehicle models and production expansion in 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What is Tesla's outlook for new vehicle models and production expansion in 2023?"

USER_QUERIES = [
    "What were Tesla's total revenues and operating income for fiscal year 2023?",
    "How did Tesla's vehicle average selling price and gross margin trend in 2023?",
    "What were Tesla's total vehicle deliveries and production volumes in 2023?",
    "How did Tesla's energy storage deployment grow in 2023?",
    "What cost reduction initiatives did Tesla implement in 2023?",
    "What were the key balance sheet metrics for Tesla at the end of 2023?",
    "What risks related to competition and pricing pressure did Tesla disclose in 2023?",
    "What is Tesla's outlook for new vehicle models and production expansion in 2023?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2023, Tesla's outlook for new vehicle models and production expansion is focused on several key initiatives:

1. **New Vehicle Models**: Tesla has actively launched the Cybertruck, which began deliveries in November 2023. The company is also ramping up production of the Tesla Semi, which is in pilot production, and is developing a next-generation vehicle platform and the Tesla Roadster.

2. **Production Expansion**: Tesla aims to increase its manufacturing capacity across its existing facilities, including Gigafactories in Texas, Shanghai, and Berlin. The company is also planning to build a new Gigafactory in Monterrey, Mexico, to further enhance its production capabilities and localize manufacturing.

3. **Production Goals**: Tesla produced approximately 1.85 million vehicles in 2023 and is focused on ramping production rates and efficiency at its factories. The company is also working to improve battery cell supply by developing its own cells to reduce costs and enhance vehicle performance.

4. **Challenges and Uncertainties**: Tesla acknowledges potential challenges in ramping production due to component constraints, labor shortages, and the complexities of introducing new manufacturing technologies. The company experienced a sequential decline in production volumes during the third quarter of 2023 due to planned factory upgrades.

Overall, Tesla is committed to expanding its vehicle offerings and production capabilities while navigating the inherent risks associated with manufacturing and market demand.
"""

ADVISOR_REPORT_V1 = """
# Tesla's Outlook for New Vehicle Models and Production Expansion in 2023

The available documents do not provide specific information regarding Tesla's outlook for new vehicle models and production expansion in 2023. Key details such as planned vehicle launches, production targets, or strategic initiatives for the year are not included in the provided context. 

This lack of information presents a limitation in assessing Tesla's future vehicle offerings and production capabilities. 

To gain insights into Tesla's vehicle model plans and production strategies for 2023, I recommend checking the following sources:
- Tesla's official press releases
- Investor relations updates on Tesla's website
- Recent earnings call transcripts
- Industry news articles covering Tesla's developments

These resources are likely to provide the most accurate and up-to-date information regarding Tesla's future vehicle offerings and production capabilities.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Outlook for New Vehicle Models and Production Expansion in 2023

The available documents do not provide specific information regarding Tesla's outlook for new vehicle models and production expansion in 2023. Key details such as planned vehicle launches, production targets, or strategic initiatives for the year are not included in the provided context. This lack of information presents a limitation in assessing Tesla's future vehicle offerings and production capabilities.

## Key Risks and Considerations

While specific information is missing, several key risks identified in the context documents could impact Tesla's performance in 2023:

- **Competition**: The automotive market is highly competitive, and Tesla may face challenges in maintaining its market share and pricing strategies against emerging and established competitors.
- **Valuation**: Market conditions and investor sentiment can significantly affect Tesla's valuation, which may impact its ability to raise capital or invest in new projects.
- **Supply Chain**: Potential disruptions in the supply chain could hinder production capabilities and affect the timely delivery of new models.
- **Regulation**: Changes in government incentives or regulations affecting electric vehicles could influence demand and operational costs.
- **Margin Pressure**: Pricing strategies and rising costs could impact profit margins, necessitating careful management to sustain profitability.

## Contextual Analysis

The absence of detailed information regarding Tesla's vehicle models and production plans for 2023 raises concerns about transparency and strategic direction. Investors and stakeholders may interpret this lack of clarity as a potential risk, leading to uncertainty about Tesla's future performance.

## SWOT Analysis

To better understand Tesla's position, a SWOT analysis can provide insights into its strengths, weaknesses, opportunities, and threats:

1. **Strengths**:
   - Proprietary technology and innovation in electric vehicles.
   - Strong brand recognition and customer loyalty.
   - Economies of scale in production.

2. **Weaknesses**:
   - Dependence on specific suppliers for critical components.
   - Challenges in scaling production to meet demand.

3. **Opportunities**:
   - Leveraging market trends such as the shift to clean energy and government incentives for electric vehicles.
   - Potential expansion into new geographic markets or product lines.

4. **Threats**:
   - Increased competition from traditional automakers and new entrants in the electric vehicle market.
   - Regulatory changes that could impact operational costs and market access.
   - Risks associated with supply chain disruptions and volatile raw material prices.

## Recommendations for Further Insights

To gain insights into Tesla's vehicle model plans and production strategies for 2023, I recommend checking the following sources:
- Tesla's official press releases
- Investor relations updates on Tesla's website
- Recent earnings call transcripts
- Industry news articles covering Tesla's developments

These resources are likely to provide the most accurate and up-to-date information regarding Tesla's future vehicle offerings and production capabilities.

## Conclusion

In summary, while the current context does not provide specific details on Tesla's new vehicle models and production expansion for 2023, understanding the associated risks and conducting a SWOT analysis can help stakeholders gauge the company's strategic position. Further research through official channels is encouraged to obtain the latest updates.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Tesla's outlook for new vehicle models and production expansion in 2023. However, it lacks grounding in the provided context documents and misses key structural elements that would enhance its quality.

## Query Satisfaction
The response effectively covers the main aspects of the user's query, including:
- The introduction of new vehicle models, specifically the Cybertruck and Tesla Semi.
- Plans for production expansion, including the establishment of a new Gigafactory in Monterrey, Mexico.
- Production goals and challenges faced by Tesla.

However, it does not reference specific data or insights from the context documents, which diminishes its credibility.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Missing Actionable Content**: The response lacks actionable insights or recommendations that could guide the user further.
3. **Limited Discussion of Risks**: While the response mentions challenges and uncertainties, it could benefit from a more detailed exploration of these risks as outlined in the context documents.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made about Tesla's new vehicle models and production expansion.
- Add actionable content or recommendations based on the information provided.
- Expand on the discussion of risks and uncertainties to provide a more comprehensive view of Tesla's outlook for 2023.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's outlook for new vehicle models and production expansion in 2023 compared to the original report (v1). However, it still lacks visual aids, which were identified as a necessary improvement.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's outlook for new vehicle models and production expansion in 2023. It discusses key risks and considerations, provides a contextual analysis, and includes a SWOT analysis, which enhances the understanding of Tesla's strategic position. 

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Provided specific information regarding Tesla's new vehicle models and production expansion plans for 2023.
  2. Addressed key risks identified in the context documents, including competition, valuation, supply chain, regulation, and margin pressure.
  3. Included contextual analysis of the implications of missing information.
  
- **Unresolved**:
  1. Add visual aids to enhance the clarity and impact of the report.

## Remaining Gaps
The only remaining gap is the lack of visual aids in the report. This was highlighted as a critical improvement area that has not been addressed in the revised version.

## Recommendation
It is recommended that the advisor incorporate visual aids, such as charts or graphs, to enhance the clarity and impact of the report. This will help present complex information more effectively and improve the overall quality of the report for stakeholders.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_6/query_8
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |       70 |    +70 |
| Risk Assessment      |    15%  |        0 |       80 |    +80 |
| Actionable Advice    |    15%  |        0 |       80 |    +80 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       50 |      100 |    +50 |
| Query Satisfaction   |    10%  |        0 |       70 |    +70 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     5.00 |    51.50 |  +46.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +46.5 pts absolute  |  +930.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_6/query_8
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       85 |        0 |        0 |    -85 |     +0 |    -85 |
| Business Analysis    |    15%  |       70 |        0 |       70 |    -70 |    +70 |     +0 |
| Risk Assessment      |    15%  |       75 |        0 |       80 |    -75 |    +80 |     +5 |
| Actionable Advice    |    15%  |       60 |        0 |       80 |    -60 |    +80 |    +20 |
| Evidence Usage       |    10%  |       50 |        0 |        0 |    -50 |     +0 |    -50 |
| Completeness         |    10%  |       80 |       50 |      100 |    -30 |    +50 |    +20 |
| Query Satisfaction   |    10%  |       90 |        0 |       70 |    -90 |    +70 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    74.00 |     5.00 |    51.50 |    -69 |    +46 |    -22 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -22 pts absolute  |  -30.41% relative
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
                "v2_score": 0,
                "delta_v0_v1": -85,
                "delta_v1_v2": 0,
                "delta_v0_v2": -85,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -70,
                "delta_v1_v2": 70,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 75,
                "weighted_v0": 11.25,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": -75,
                "delta_v1_v2": 80,
                "delta_v0_v2": 5,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": -60,
                "delta_v1_v2": 80,
                "delta_v0_v2": 20,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 50,
                "weighted_v0": 5.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -50,
                "delta_v1_v2": 0,
                "delta_v0_v2": -50,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 50,
                "v2_score": 100,
                "delta_v0_v1": -30,
                "delta_v1_v2": 50,
                "delta_v0_v2": 20,
                "weighted_v1": 5.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -90,
                "delta_v1_v2": 70,
                "delta_v0_v2": -20,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            }
        },
        "overall_v0": 74.0,
        "overall_v1": 5.0,
        "overall_v2": 51.5,
        "improvement_v0_to_v1": -69.0,
        "improvement_v1_to_v2": 46.5,
        "improvement_v0_to_v2": -22.5,
        "improvement_pct_v0_to_v2": -30.41
    }
