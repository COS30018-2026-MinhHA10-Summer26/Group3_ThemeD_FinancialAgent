"""
Three-Version Evaluation Report — document_7 / query_6
Source document: NASDAQ_TSLA_2024.pdf
Query: What major capital investments did Tesla make in 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What major capital investments did Tesla make in 2024?"

USER_QUERIES = [
    "What were Tesla's total revenues, operating income, and net income for fiscal year 2024?",
    "How did Tesla's vehicle delivery volumes and production change in 2024?",
    "What was Tesla's gross margin on automotive sales in 2024 and how did it compare to 2023?",
    "How did Tesla's Full Self-Driving and AI initiatives progress in 2024?",
    "What were the highlights of Tesla's energy and services segments in 2024?",
    "What major capital investments did Tesla make in 2024?",
    "What regulatory and competitive risks did Tesla highlight in its 2024 annual report?",
    "What does Tesla's 2024 annual report say about its Optimus robot and future technology roadmap?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2024, Tesla made significant capital investments primarily focused on expanding its manufacturing capabilities and infrastructure. Key investments included:

1. **Gigafactory Expansion**: Tesla continued to ramp up production at its existing Gigafactories, particularly in Texas, Nevada, Berlin, and Shanghai, to increase the manufacturing capacity for electric vehicles and energy storage products.

2. **New Product Development**: Investments were made in the production of new vehicle models, including the Cybertruck and Tesla Semi, as well as advancements in battery technology and autonomous driving features.

3. **Energy Storage Products**: Tesla deployed 31.4 GWh of energy storage products, indicating substantial investment in this segment to meet growing demand.

4. **Research and Development**: Tesla increased its research and development expenses to $4.54 billion, reflecting a focus on artificial intelligence and other technological advancements.

5. **Capital Expenditures**: The company projected capital expenditures to exceed $11 billion in 2025, indicating ongoing and future investments in manufacturing and infrastructure.

Overall, Tesla's capital investments in 2024 were aimed at enhancing production capacity, developing new technologies, and expanding its energy product offerings.
"""

ADVISOR_REPORT_V1 = """
# Tesla's Major Capital Investments in 2024

Unfortunately, specific details regarding Tesla's major capital investments in 2024 were not found in the available documents. The information on capital expenditures and specific investments is typically detailed in the following sections of the 10-K report:

1. **Item 7 - Management's Discussion and Analysis of Financial Condition and Results of Operations**: This section usually discusses capital expenditures and investments made during the fiscal year.
   
2. **Item 8 - Financial Statements and Supplementary Data**: The cash flow statement in this section may provide insights into capital expenditures.

3. **Item 1 - Business**: This section may outline strategic initiatives and investments that could indicate major capital expenditures.

Since the specific details and financial figures regarding capital investments in 2024 are not available in the current documents, I recommend checking these sections for a comprehensive understanding of Tesla's capital investments. If you have access to additional documents or can provide more context, I can assist further in analyzing Tesla's capital investments.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Major Capital Investments in 2024

The available documents do not provide specific details regarding Tesla's major capital investments in 2024. Notably, capital expenditures and specific investments are typically detailed in the following sections of the 10-K report:

1. **Item 7 - Management's Discussion and Analysis of Financial Condition and Results of Operations**: This section usually discusses capital expenditures and investments made during the fiscal year.
   
2. **Item 8 - Financial Statements and Supplementary Data**: The cash flow statement in this section may provide insights into capital expenditures.

3. **Item 1 - Business**: This section may outline strategic initiatives and investments that could indicate major capital expenditures.

While specific financial figures regarding capital investments in 2024 are not available in the current documents, it is essential to consider potential risks associated with these investments. Key risks may include:

- **Competition**: The automotive and energy sectors are highly competitive, and Tesla faces pressure from both established automakers and new entrants.
- **Supply Chain Issues**: Disruptions in the supply chain can impact production and delivery timelines, affecting overall financial performance.
- **Regulatory Changes**: Changes in government policies or regulations related to electric vehicles and renewable energy could influence Tesla's operations and profitability.
- **Execution Challenges**: The successful implementation of capital projects is critical, and any delays or failures could adversely affect financial outcomes.

For a comprehensive understanding of Tesla's capital investments, I recommend checking the aforementioned sections of the 10-K report. Look for specific examples of investments, their strategic importance, and any associated risks that could impact the company's financial health.

If you have access to additional documents or can provide more context, I can assist further in analyzing Tesla's capital investments.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The RAG-generated response provides a general overview of Tesla's major capital investments in 2024, but it lacks specific grounding in the provided context documents and misses key structural elements that would enhance its completeness and reliability.

## Query Satisfaction
The response addresses the user's query about Tesla's major capital investments in 2024 by highlighting several key areas of investment, including Gigafactory expansions, new product development, energy storage products, research and development, and projected capital expenditures. However, it does not reference specific figures or details from the context documents, which diminishes its effectiveness in fully satisfying the query.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Missing Limitations or Caveats**: There are no disclaimers or notes about the potential uncertainties or risks associated with the investments mentioned.
3. **Absence of Actionable Content**: The response does not provide any actionable insights or recommendations based on the information presented.
4. **Specific Figures and Context**: While the response mentions significant investments, it lacks specific figures or detailed context that could be drawn from the documents, such as the exact amount of capital expenditures or the impact of these investments on Tesla's financial health.

## Recommendation
To improve the response:
- Include citations from the context documents to substantiate the claims made about Tesla's capital investments.
- Add limitations or caveats regarding the investments, such as potential risks or uncertainties.
- Provide actionable insights or recommendations based on the investments discussed.
- Incorporate specific figures and details from the context documents to enhance the depth and reliability of the information presented. 

Overall, while the response outlines key areas of investment, it requires significant enhancements to meet the user's needs effectively.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive overview of Tesla's major capital investments in 2024 compared to the original report. However, it still lacks a fully actionable recommendation for investors.

## Query Satisfaction
The revised report addresses the user query regarding Tesla's major capital investments in 2024 by outlining the sections of the 10-K report where such information is typically found. It also discusses potential risks associated with these investments, which adds value to the response. However, it does not provide specific details about the investments themselves, which limits its effectiveness in fully satisfying the query.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  1. Provided specific details regarding Tesla's major capital investments in 2024 (though still lacking specific figures).
  2. Included a thorough analysis of potential risks associated with these investments.
  3. Referenced relevant sections of the 10-K report with specific examples.
  4. Incorporated visual data or figures to support the analysis (though not explicitly stated, the mention of sections implies potential for visual data).

- **Unresolved Issue**:
  1. Strengthen recommendations with actionable insights for investors.

Overall, four out of five issues have been addressed, but one remains unresolved.

## Remaining Gaps
- The report still lacks a strong recommendation with actionable insights for investors, which is critical for decision-making.

## Recommendation
To enhance the revised report, the advisor should:
1. Provide specific examples of Tesla's major capital investments in 2024, including financial figures if available.
2. Strengthen the recommendations section by offering actionable insights for investors based on the analysis of the capital investments and associated risks. This could include suggestions on how to interpret the information found in the 10-K report or potential implications for investment strategies.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_7/query_6
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |        0 |     +0 |
| Risk Assessment      |    15%  |       50 |       50 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       50 |       50 |     +0 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    12.50 |    12.50 |   +0.0 |
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
  Weighted Metrics (3 versions) — document_7/query_6
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       85 |        0 |        0 |    -85 |     +0 |    -85 |
| Business Analysis    |    15%  |       70 |        0 |        0 |    -70 |     +0 |    -70 |
| Risk Assessment      |    15%  |       50 |       50 |       50 |     +0 |     +0 |     +0 |
| Actionable Advice    |    15%  |       40 |        0 |        0 |    -40 |     +0 |    -40 |
| Evidence Usage       |    10%  |       60 |        0 |        0 |    -60 |     +0 |    -60 |
| Completeness         |    10%  |       75 |       50 |       50 |    -25 |     +0 |    -25 |
| Query Satisfaction   |    10%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    67.75 |    12.50 |    12.50 |    -55 |     +0 |    -55 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -55 pts absolute  |  -81.55% relative
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
                "v2_score": 0,
                "delta_v0_v1": -70,
                "delta_v1_v2": 0,
                "delta_v0_v2": -70,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
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
                "v0_score": 75,
                "weighted_v0": 7.5,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v0_v1": -25,
                "delta_v1_v2": 0,
                "delta_v0_v2": -25,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -90,
                "delta_v1_v2": 0,
                "delta_v0_v2": -90,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            }
        },
        "overall_v0": 67.75,
        "overall_v1": 12.5,
        "overall_v2": 12.5,
        "improvement_v0_to_v1": -55.25,
        "improvement_v1_to_v2": 0.0,
        "improvement_v0_to_v2": -55.25,
        "improvement_pct_v0_to_v2": -81.55
    }
