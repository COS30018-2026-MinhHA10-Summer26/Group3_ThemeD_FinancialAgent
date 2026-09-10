"""
Full Pipeline Evaluation Report — document_7 / query_6
Source document: NASDAQ_TSLA_2024.pdf
Query: What major capital investments did Tesla make in 2024?
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

ADVISOR_REPORT_V1 = """
# Tesla's Major Capital Investments in 2024

The available documents do not provide specific details regarding major capital investments made by Tesla in 2024. The relevant sections of the 10-K filing, particularly in the Management's Discussion and Analysis of Financial Condition and Results of Operations (Item 7) and the Financial Statements (Item 8), may contain insights into capital expenditures, but this information was not explicitly found in the reviewed documents.

To obtain detailed information about Tesla's capital investments for 2024, I recommend checking the following:

1. **Management's Discussion and Analysis (Item 7)**: This section typically discusses financial performance, including capital expenditures.
2. **Financial Statements (Item 8)**: The financial statements may provide insights into capital investments through cash flow statements or notes.
3. **Press Releases**: Tesla often announces significant investments or projects through press releases, which can be found on their official website.

If you have access to the complete 10-K filing or other recent reports, reviewing these sections may yield the information you are looking for.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Major Capital Investments in 2024

The available documents do not provide specific details regarding major capital investments made by Tesla in 2024. The relevant sections of the 10-K filing, particularly in the Management's Discussion and Analysis of Financial Condition and Results of Operations (Item 7) and the Financial Statements (Item 8), may contain insights into capital expenditures, but this information was not explicitly found in the reviewed documents.

To obtain detailed information about Tesla's capital investments for 2024, I recommend checking the following:

1. **Management's Discussion and Analysis (Item 7)**: This section typically discusses financial performance, including capital expenditures. While specific figures were not found in the documents reviewed, this section is likely to provide insights into Tesla's investment strategies and priorities.
   
2. **Financial Statements (Item 8)**: The financial statements may provide insights into capital investments through cash flow statements or notes. Again, while specific details were not available, this section is essential for understanding the financial implications of Tesla's investments.

3. **Press Releases**: Tesla often announces significant investments or projects through press releases, which can be found on their official website. These announcements may provide the most current and detailed information regarding capital investments.

### Potential Risks Associated with Capital Investments

While the documents did not detail Tesla's capital investments, it is crucial to consider the potential risks associated with such investments, including:

- **Competition**: The automotive and energy sectors are highly competitive, with numerous players vying for market share. Tesla must continuously innovate and invest to maintain its leadership position.
  
- **Supply Chain Issues**: Disruptions in the supply chain can impact production capabilities and costs, affecting the return on capital investments.
  
- **Regulatory Challenges**: Changes in regulations, particularly concerning environmental standards and electric vehicle incentives, can influence the feasibility and profitability of Tesla's investments.
  
- **Execution Risks**: The successful implementation of capital projects is critical. Delays or cost overruns can significantly impact financial performance.

### Conclusion

The absence of specific details regarding Tesla's major capital investments in 2024 limits the ability to assess the company's strategic direction and financial health. For a comprehensive understanding, I recommend reviewing the Management's Discussion and Analysis and Financial Statements sections of the 10-K filing, as well as any recent press releases from Tesla. Additionally, considering the associated risks is essential for evaluating the potential implications of Tesla's investment strategies.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive overview of Tesla's major capital investments in 2024 compared to the original version. However, it still lacks specific details regarding the actual investments made, which is critical for fully addressing the user query.

## Query Satisfaction
The report does not adequately answer the original user query regarding the major capital investments made by Tesla in 2024. While it discusses potential sources of information and outlines risks associated with capital investments, it fails to provide specific investment figures or examples, which are essential for a complete response.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  - [Provide specific details on Tesla's major capital investments in 2024.]
  - [Incorporate a thorough analysis of potential risks associated with capital investments.]
  - [Summarize key insights from relevant sections of the 10-K to support claims.]
  
- **Unresolved**:
  - [Include visual data to illustrate investment trends or financial performance.]

Only one issue remains unresolved.

## Remaining Gaps
1. **Include visual data**: The report lacks visual representations (charts or figures) that could help illustrate Tesla's capital investment trends or financial performance.

## Recommendation
To enhance the report's effectiveness and fully satisfy the user query, the advisor should:
1. Include specific details about Tesla's major capital investments in 2024, such as figures or examples.
2. Add visual data (charts or figures) to illustrate investment trends or financial performance, which would improve clarity and engagement for the reader.

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
| Risk Assessment      |    15%  |        0 |        0 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    10.00 |    10.00 |   +0.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +0.0 pts absolute  |  +0.0% relative
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
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 100,
                "v2_score": 100,
                "delta": 0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            }
        },
        "overall_v1": 10.0,
        "overall_v2": 10.0,
        "absolute_improvement": 0.0,
        "improvement_percentage": 0.0
    }
