"""
Three-Version Evaluation Report — document_1 / query_1
Source document: NASDAQ_AMZN_2022.pdf
Query: What were Amazon's total net sales and net income for fiscal year 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were Amazon's total net sales and net income for fiscal year 2022?"

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
For the fiscal year 2022, Amazon's total net sales were $513.98 billion, and the net income was a loss of $2.72 billion.
"""

ADVISOR_REPORT_V1 = """
# Amazon Financial Metrics for Fiscal Year 2022

For fiscal year 2022, Amazon reported total net sales of **$514 billion** and a net income of **$11.3 billion**. 

These figures reflect Amazon's performance amidst various macroeconomic challenges and operational adjustments throughout the year.

For further details, you can refer to the official annual report available in the provided documents.
"""

ADVISOR_REPORT_V2 = """
# Amazon Financial Metrics for Fiscal Year 2022

For fiscal year 2022, Amazon reported total net sales of **$434 billion** and a net income of **$11.3 billion**. These figures reflect Amazon's performance amidst various macroeconomic challenges and operational adjustments throughout the year. The total net sales and net income figures are sourced from the provided document context.

For further details, you can refer to the official annual report available in the provided documents.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user's query regarding Amazon's total net sales and net income for fiscal year 2022. However, it lacks proper grounding in the provided context documents and does not include necessary citations or structural elements.

## Query Satisfaction
The response directly addresses the user's question by providing the total net sales of $513.98 billion and a net income loss of $2.72 billion for fiscal year 2022. Therefore, it satisfies the query in terms of content.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents from which the financial figures were derived. This is crucial for verifying the accuracy of the information provided.
2. **Missing Limitations or Caveats**: The response does not mention any limitations or caveats regarding the financial data, which could be important for the user to understand the context of the figures.
3. **Absence of Actionable Content**: There is no actionable content or recommendations provided in the response, which could enhance its usefulness.
4. **No Structured Sections**: The response lacks a structured format that could help in presenting the information more clearly.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the financial figures provided.
- Add any necessary limitations or caveats regarding the financial data.
- Consider including actionable content or recommendations based on the financial results.
- Structure the response into clear sections for better readability and comprehension.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) partially addresses the user query regarding Amazon's total net sales and net income for fiscal year 2022. However, it fails to fully resolve the issues identified by the Critic, leaving several critical gaps in the analysis.

## Query Satisfaction
The report provides the requested figures: total net sales of **$434 billion** and net income of **$11.3 billion**. However, it lacks context regarding the implications of these figures, such as comparisons to previous years or the factors influencing these results. Additionally, it does not discuss the financial health, future outlook, or risks associated with these figures, which are essential for a comprehensive understanding.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**: 
  - Validation of the total net sales figure with proper citations.
- **Unresolved**: 
  - Discussion of key risks such as competition, valuation, supply chain, regulation, margin pressure, and execution.
  - Addition of visual aids to represent financial data clearly.
  - Discussion of the future outlook and strategies for addressing identified risks.

## Remaining Gaps
1. **Key Risks**: The report does not include a discussion of significant risks that could impact Amazon's financial performance.
2. **Visual Aids**: There are no charts or graphs to visually represent the financial data, which would enhance understanding.
3. **Future Outlook**: The report lacks insights into how Amazon plans to navigate identified risks and its strategies for future growth.

## Recommendation
The advisor should revise the report to include:
1. A comprehensive analysis of key risks associated with Amazon's operations and market environment.
2. Visual aids such as charts or graphs to support the financial data presented.
3. A discussion on the future outlook, including strategies for addressing the identified risks and sustaining growth.

Addressing these gaps will enhance the report's quality and provide a more complete picture of Amazon's financial health for fiscal year 2022.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_1/query_1
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |        0 |   -100 |
| Business Analysis    |    15%  |        0 |        0 |     +0 |
| Risk Assessment      |    15%  |        0 |        0 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |       50 |    +50 |
| Completeness         |    10%  |        0 |        0 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    35.00 |    15.00 |  -20.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: -20.0 pts absolute  |  -57.14% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_1/query_1
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |        0 |     +0 |   -100 |   -100 |
| Business Analysis    |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Risk Assessment      |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |       50 |     +0 |    +50 |    +50 |
| Completeness         |    10%  |        1 |        0 |        0 |     -1 |     +0 |     -1 |
| Query Satisfaction   |    10%  |      100 |      100 |      100 |     +0 |     +0 |     +0 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    35.10 |    35.00 |    15.00 |     +0 |    -20 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -20 pts absolute  |  -57.26% relative
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
                "v1_score": 100,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": -100,
                "delta_v0_v2": -100,
                "weighted_v1": 25.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v0_v1": 0,
                "delta_v1_v2": 50,
                "delta_v0_v2": 50,
                "weighted_v1": 0.0,
                "weighted_v2": 5.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 1,
                "weighted_v0": 0.1,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -1,
                "delta_v1_v2": 0,
                "delta_v0_v2": -1,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "weighted_v0": 10.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 35.1,
        "overall_v1": 35.0,
        "overall_v2": 15.0,
        "improvement_v0_to_v1": -0.1,
        "improvement_v1_to_v2": -20.0,
        "improvement_v0_to_v2": -20.1,
        "improvement_pct_v0_to_v2": -57.26
    }
