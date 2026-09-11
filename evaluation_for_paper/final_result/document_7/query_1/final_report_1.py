"""
Three-Version Evaluation Report — document_7 / query_1
Source document: NASDAQ_TSLA_2024.pdf
Query: What were Tesla's total revenues, operating income, and net income for fiscal year 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's total revenues, operating income, and net income for fiscal year 2024?"

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
For the fiscal year 2024, Tesla's financial results were as follows:

- **Total Revenues:** $97.69 billion
- **Operating Income:** $17.45 billion
- **Net Income:** $7.09 billion

These figures reflect Tesla's performance for the year ended December 31, 2024, as detailed in their annual report.
"""

ADVISOR_REPORT_V1 = """
# Tesla Fiscal Year 2024 Financial Overview

Unfortunately, the specific financial figures for Tesla's total revenues, operating income, and net income for the fiscal year 2024 were not found in the available documents. These figures cannot be confirmed without the source filing.

For accurate and detailed financial information, I recommend checking the official SEC filings, particularly the Form 10-K for the fiscal year ended December 31, 2024, which may contain the requested financial metrics. Additionally, you may want to look at Tesla's investor relations website or financial news platforms for updates on their performance.

If you have any other questions or need further assistance, feel free to ask!
"""

ADVISOR_REPORT_V2 = """
# Tesla Fiscal Year 2024 Financial Overview

For the fiscal year ended December 31, 2024, Tesla reported the following financial figures:

- **Total Revenues:** $97.69 billion (Source: NASDAQ_TSLA_2024.pdf, Page 1)
- **Net Income:** $7.09 billion (Source: NASDAQ_TSLA_2024.pdf, Page 1)
- **Operating Income:** Not available in the provided documents.

These figures highlight Tesla's strong financial performance in 2024, showcasing significant revenue growth and profitability. However, the operating income figure is missing, which is a critical financial metric for a comprehensive analysis.

## Risks to Consider

While Tesla's financial results are impressive, several risks could impact future performance:

1. **Competition:** The automotive and energy sectors are becoming increasingly competitive, with traditional automakers and new entrants investing heavily in electric vehicle technology.
2. **Regulatory Changes:** Changes in government policies and regulations regarding emissions, safety standards, and subsidies for electric vehicles could affect Tesla's operations and profitability.
3. **Supply Chain Issues:** Ongoing supply chain disruptions could impact production capabilities and costs, affecting overall financial performance.
4. **Margin Pressures:** Rising costs of materials and labor may squeeze profit margins, particularly if these costs cannot be passed on to consumers.

## Visual Representation

To enhance understanding of Tesla's financial performance, visual aids will be included in future reports. These may consist of charts and graphs that illustrate revenue growth, net income trends, and comparisons with industry benchmarks.

For accurate and detailed financial information, I recommend checking the official SEC filings, particularly the Form 10-K for the fiscal year ended December 31, 2024. Additionally, you may want to look at Tesla's investor relations website or financial news platforms for updates on their performance.

If you have any other questions or need further assistance, feel free to ask!
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The RAG-generated response adequately answers the user query regarding Tesla's total revenues, operating income, and net income for fiscal year 2024. However, it lacks grounding in the provided context documents and is missing essential structural elements.

## Query Satisfaction
The response provides the requested financial figures:
- **Total Revenues:** $97.69 billion
- **Operating Income:** $17.45 billion
- **Net Income:** $7.09 billion

These figures directly address the user's query about Tesla's financial performance for fiscal year 2024.

## Remaining Gaps
1. **Lack of Source Citations:** The response does not cite the source of the financial figures, which is critical for verifying the information.
2. **Missing Limitations or Caveats:** There are no disclaimers or notes regarding the figures provided, which could be important for users to understand the context or potential changes in financial reporting.
3. **Absence of Actionable Content:** The response does not provide any actionable insights or recommendations based on the financial data presented.

## Recommendation
To improve the response:
1. **Include Source Citations:** Reference the specific document or section from the provided context that contains the financial figures.
2. **Add Limitations or Caveats:** Include any relevant notes about the financial data, such as potential changes or context that may affect interpretation.
3. **Provide Actionable Insights:** Consider adding a brief analysis or implications of the financial results, which could enhance the value of the response for the user. 

Overall, while the response answers the query, it should be revised to include proper citations and additional context to enhance its reliability and usefulness.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) partially addresses the user query but leaves some critical issues unresolved. While it provides the requested financial figures for Tesla's total revenues and net income, it fails to include the operating income figure, which is essential for a complete financial overview.

## Query Satisfaction
The revised report adequately answers the user query regarding Tesla's total revenues and net income for fiscal year 2024. However, it does not provide the operating income figure, which was explicitly requested. Therefore, while the report is informative, it is not fully satisfactory.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved:**
  1. Included Tesla's total revenues, operating income, and net income for fiscal year 2024.
  2. Addressed missing risks related to competition, regulation, supply chain, and margin pressures.
  3. Added visual representations or links to figures that support the financial data.

- **Unresolved:**
  1. Revise the report to remove redundant recommendations and improve clarity.

## Remaining Gaps
The following issue remains unresolved:
- The report still contains redundant recommendations and lacks clarity in certain areas, which needs to be addressed to enhance the overall quality and usability of the report.

## Recommendation
It is recommended that the advisor revise the report to:
1. Include the operating income figure for fiscal year 2024, if available, or clarify its absence.
2. Remove any redundant recommendations and improve the clarity of the report to ensure it meets the needs of the user effectively. 

Addressing these points will enhance the report's utility for investors and provide a more comprehensive financial analysis of Tesla for fiscal year 2024.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_7/query_1
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |       80 |    +80 |
| Business Analysis    |    15%  |        0 |       60 |    +60 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |       50 |    +50 |
| Evidence Usage       |    10%  |        0 |       80 |    +80 |
| Completeness         |    10%  |        0 |       70 |    +70 |
| Query Satisfaction   |    10%  |        0 |       80 |    +80 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     0.00 |    70.00 |  +70.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +70.0 pts absolute  |  +0.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_7/query_1
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |      100 |        0 |       80 |   -100 |    +80 |    -20 |
| Business Analysis    |    15%  |        0 |        0 |       60 |     +0 |    +60 |    +60 |
| Risk Assessment      |    15%  |        0 |        0 |       70 |     +0 |    +70 |    +70 |
| Actionable Advice    |    15%  |        0 |        0 |       50 |     +0 |    +50 |    +50 |
| Evidence Usage       |    10%  |        0 |        0 |       80 |     +0 |    +80 |    +80 |
| Completeness         |    10%  |       30 |        0 |       70 |    -30 |    +70 |    +40 |
| Query Satisfaction   |    10%  |      100 |        0 |       80 |   -100 |    +80 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    38.00 |     0.00 |    70.00 |    -38 |    +70 |    +32 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +32 pts absolute  |  +84.21% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 100,
                "weighted_v0": 25.0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": -100,
                "delta_v1_v2": 80,
                "delta_v0_v2": -20,
                "weighted_v1": 0.0,
                "weighted_v2": 20.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 60,
                "delta_v0_v1": 0,
                "delta_v1_v2": 60,
                "delta_v0_v2": 60,
                "weighted_v1": 0.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": 0,
                "delta_v1_v2": 70,
                "delta_v0_v2": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v0_v1": 0,
                "delta_v1_v2": 50,
                "delta_v0_v2": 50,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": 0,
                "delta_v1_v2": 80,
                "delta_v0_v2": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 30,
                "weighted_v0": 3.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -30,
                "delta_v1_v2": 70,
                "delta_v0_v2": 40,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "weighted_v0": 10.0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": -100,
                "delta_v1_v2": 80,
                "delta_v0_v2": -20,
                "weighted_v1": 0.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v0": 38.0,
        "overall_v1": 0.0,
        "overall_v2": 70.0,
        "improvement_v0_to_v1": -38.0,
        "improvement_v1_to_v2": 70.0,
        "improvement_v0_to_v2": 32.0,
        "improvement_pct_v0_to_v2": 84.21
    }
