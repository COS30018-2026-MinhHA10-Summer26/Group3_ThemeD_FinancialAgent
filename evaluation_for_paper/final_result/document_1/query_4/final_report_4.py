"""
Three-Version Evaluation Report — document_1 / query_4
Source document: NASDAQ_AMZN_2022.pdf
Query: What is Amazon's free cash flow position and how did it change in 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What is Amazon's free cash flow position and how did it change in 2022?"

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
Amazon's free cash flow position in 2022 was negative, amounting to **$(11,569) million**. This represents a decline from the previous year, where the free cash flow was **$(9,069) million** in 2021. The change in free cash flow from 2021 to 2022 indicates a worsening position, primarily driven by increased capital expenditures, which rose from **$55,396 million** in 2021 to **$58,321 million** in 2022. Despite a slight increase in cash provided by operating activities, the higher investments led to a larger negative free cash flow in 2022.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Free Cash Flow Position in 2022

⚠️ Free cash flow for 2022 and the previous year was not found in the available documents. This figure cannot be confirmed without the source filing.

To accurately analyze Amazon's free cash flow position and how it changed in 2022, the specific values for free cash flow in both 2022 and the prior year are needed. Unfortunately, this information is missing from the current context. Please provide those figures or any additional context that may contain this information.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Free Cash Flow Position in 2022

⚠️ Free cash flow for 2022 and the previous year was not found in the available documents. This figure cannot be confirmed without the source filing.

To accurately analyze Amazon's free cash flow position and how it changed in 2022, the specific values for free cash flow in both 2022 and the prior year are needed. Unfortunately, this information is missing from the current context. Please provide those figures or any additional context that may contain this information.

## Implications of Missing Financial Data

The absence of free cash flow figures significantly limits our ability to assess Amazon's financial health and strategic direction. Free cash flow is a critical metric that indicates the cash a company generates after accounting for capital expenditures, which is essential for funding operations, paying dividends, and pursuing growth opportunities.

### Risks Impacting Amazon's Financial Position

Several visible risk factors could impact Amazon's overall financial health:

- **Competition**: Amazon operates in a highly competitive environment, facing challenges from both established players and new entrants across various sectors, including retail and cloud services.
  
- **Valuation Risks**: Market conditions can significantly affect Amazon's valuation, especially in a volatile economic climate where investor sentiment may shift rapidly.
  
- **Supply Chain Risks**: The ongoing economic challenges could lead to supply chain disruptions, impacting Amazon's ability to deliver products efficiently and cost-effectively.
  
- **Regulatory Risks**: Potential regulatory challenges, particularly concerning antitrust issues and data privacy, could pose significant hurdles for Amazon's operations.
  
- **Margin Pressure**: Rising costs, particularly in fulfillment and logistics, could squeeze profit margins, affecting overall profitability.
  
- **Execution Risks**: The successful execution of strategic initiatives, such as optimizing fulfillment networks and enhancing customer experiences, is crucial for maintaining competitive advantage.

## Conclusion

In summary, the lack of specific free cash flow figures for 2022 and the previous year hampers a comprehensive analysis of Amazon's financial position. Additionally, the identified risks highlight the complexities and challenges Amazon faces in navigating its business environment. Further context or data regarding free cash flow would be essential for a more informed evaluation.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's free cash flow position and its changes in 2022. However, it lacks grounding in the provided context documents and misses important structural elements.

## Query Satisfaction
The response provides a clear answer to the user's question about Amazon's free cash flow position in 2022, stating that it was negative at $(11,569) million and that it declined from $(9,069) million in 2021. It also mentions the reasons for this decline, specifically increased capital expenditures. However, it does not reference any specific context documents to support these claims, which diminishes its reliability.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for verifying the information provided.
2. **Absence of Limitations or Caveats**: There are no disclaimers or notes about the potential variability in financial data or external factors that could affect the interpretation of free cash flow.
3. **No Actionable Content**: The response does not provide any recommendations or next steps for the user, which could enhance its usefulness.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to substantiate the claims made about free cash flow.
- Add any necessary limitations or caveats regarding the financial data to provide a more nuanced understanding.
- Consider including actionable content or recommendations for the user based on the financial position discussed. 

Overall, while the response answers the query, it needs to be better grounded in the provided context and structured to enhance clarity and reliability.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) partially addresses the original user query regarding Amazon's free cash flow position and its changes in 2022. However, it still lacks specific financial data, which is critical for a comprehensive analysis.

## Query Satisfaction
The report provides a general discussion about Amazon's free cash flow and the implications of missing data. It also outlines various risks impacting Amazon's financial position. However, it does not include the specific free cash flow figures for 2022 and the previous year, which were essential to fully satisfy the user's query.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Discuss competition, valuation, supply chain, regulation, margin pressure, and execution risks.
  2. Provide contextual analysis or estimates regarding the implications of missing financial data.
  3. Include specific free cash flow figures for 2022 and the previous year.
  
- **Unresolved**:
  1. Embed relevant figures or charts to support the analysis.

## Remaining Gaps
1. The report still lacks relevant figures or charts that could enhance the analysis and provide visual support for the discussion.

## Recommendation
To improve the report, the advisor should:
1. Include specific free cash flow figures for 2022 and the previous year.
2. Embed relevant figures or charts to support the analysis and enhance clarity.
3. Ensure that the report is comprehensive enough to provide a complete picture of Amazon's financial health and strategic direction.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_1/query_4
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       50 |       50 |     +0 |
| Risk Assessment      |    15%  |       60 |       60 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       70 |       70 |     +0 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    23.50 |    23.50 |   +0.0 |
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
  Weighted Metrics (3 versions) — document_1/query_4
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
| Business Analysis    |    15%  |       20 |       50 |       50 |    +30 |     +0 |    +30 |
| Risk Assessment      |    15%  |       10 |       60 |       60 |    +50 |     +0 |    +50 |
| Actionable Advice    |    15%  |       10 |        0 |        0 |    -10 |     +0 |    -10 |
| Evidence Usage       |    10%  |       50 |        0 |        0 |    -50 |     +0 |    -50 |
| Completeness         |    10%  |       70 |       70 |       70 |     +0 |     +0 |     +0 |
| Query Satisfaction   |    10%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    49.50 |    23.50 |    23.50 |    -26 |     +0 |    -26 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -26 pts absolute  |  -52.53% relative
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
                "v0_score": 20,
                "weighted_v0": 3.0,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v0_v1": 30,
                "delta_v1_v2": 0,
                "delta_v0_v2": 30,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 10,
                "weighted_v0": 1.5,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": 50,
                "delta_v1_v2": 0,
                "delta_v0_v2": 50,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 10,
                "weighted_v0": 1.5,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -10,
                "delta_v1_v2": 0,
                "delta_v0_v2": -10,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
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
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 7.0,
                "weighted_v2": 7.0
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
        "overall_v0": 49.5,
        "overall_v1": 23.5,
        "overall_v2": 23.5,
        "improvement_v0_to_v1": -26.0,
        "improvement_v1_to_v2": 0.0,
        "improvement_v0_to_v2": -26.0,
        "improvement_pct_v0_to_v2": -52.53
    }
