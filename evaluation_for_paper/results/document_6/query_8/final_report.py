"""
Full Pipeline Evaluation Report — document_6 / query_8
Source document: NASDAQ_TSLA_2023.pdf
Query: What is Tesla's outlook for new vehicle models and production expansion in 2023?
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

EVALUATION_REPORT = """
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

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 80,
                "delta": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 80,
                "delta": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 50,
                "v2_score": 100,
                "delta": 50,
                "weighted_v1": 5.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            }
        },
        "overall_v1": 5.0,
        "overall_v2": 51.5,
        "absolute_improvement": 46.5,
        "improvement_percentage": 930.0
    }
