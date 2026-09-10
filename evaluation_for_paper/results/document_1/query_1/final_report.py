"""
Full Pipeline Evaluation Report — document_1 / query_1
Source document: NASDAQ_AMZN_2022.pdf
Query: What were Amazon's total net sales and net income for fiscal year 2022?
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

EVALUATION_REPORT = """
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

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 100,
                "v2_score": 0,
                "delta": -100,
                "weighted_v1": 25.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 50,
                "delta": 50,
                "weighted_v1": 0.0,
                "weighted_v2": 5.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 100,
                "v2_score": 100,
                "delta": 0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v1": 35.0,
        "overall_v2": 15.0,
        "absolute_improvement": -20.0,
        "improvement_percentage": -57.14
    }
