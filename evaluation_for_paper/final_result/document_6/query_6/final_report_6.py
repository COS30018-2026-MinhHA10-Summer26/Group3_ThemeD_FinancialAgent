"""
Three-Version Evaluation Report — document_6 / query_6
Source document: NASDAQ_TSLA_2023.pdf
Query: What were the key balance sheet metrics for Tesla at the end of 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were the key balance sheet metrics for Tesla at the end of 2023?"

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
At the end of 2023, Tesla's key balance sheet metrics were as follows:

- **Total Assets**: $106.62 billion
- **Total Liabilities**: $43.01 billion
- **Total Stockholders' Equity**: $62.63 billion
- **Cash and Cash Equivalents**: $16.40 billion
- **Short-term Investments**: $12.70 billion
- **Accounts Receivable**: $12.70 billion
- **Inventory**: $13.63 billion
- **Accrued Liabilities**: $9.08 billion
- **Debt and Finance Leases**: $4.68 billion

These figures reflect Tesla's financial position as of December 31, 2023, as detailed in their consolidated balance sheets and financial statements.
"""

ADVISOR_REPORT_V1 = """
# Tesla 2023 Balance Sheet Metrics Report

Unfortunately, the key balance sheet metrics for Tesla at the end of 2023 were not found in the available documents. The specific figures for the following metrics are missing:

- Total Assets
- Total Liabilities
- Shareholders' Equity
- Current Assets
- Current Liabilities

To obtain this information, I recommend checking Tesla's official financial statements or their 10-K filing for the fiscal year ended December 31, 2023. You may also consider reviewing the SEC's EDGAR database for the most recent filings. If you have access to those documents or any additional resources, please provide them for further analysis.
"""

ADVISOR_REPORT_V2 = """
# Tesla 2023 Balance Sheet Metrics Report

Unfortunately, the key balance sheet metrics for Tesla at the end of 2023 were not found in the available documents. The specific figures for the following metrics are missing:

- Total Assets
- Total Liabilities
- Shareholders' Equity
- Current Assets
- Current Liabilities

The absence of this information poses potential risks for investors, as it limits the ability to assess Tesla's financial health and stability. Without these metrics, stakeholders may question the company's operational performance and market position, which could affect investor confidence and stock performance.

To obtain this information, I recommend checking Tesla's official financial statements or their 10-K filing for the fiscal year ended December 31, 2023. You may also consider reviewing the SEC's EDGAR database for the most recent filings. If you have access to those documents or any additional resources, please provide them for further analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The RAG-generated response adequately answers the user query regarding Tesla's key balance sheet metrics at the end of 2023. However, it lacks source citations and other structural elements that would enhance its completeness and reliability.

## Query Satisfaction
The response successfully provides the key balance sheet metrics for Tesla as of December 31, 2023, including total assets, liabilities, stockholders' equity, cash and cash equivalents, short-term investments, accounts receivable, inventory, accrued liabilities, and debt. This directly addresses the user's query.

## Remaining Gaps
1. **Source Citations**: The response does not include citations to the specific documents or sections from which the financial metrics were derived. This is important for verifying the accuracy of the information.
2. **Limitations or Caveats**: There are no limitations or caveats mentioned regarding the financial data, which could inform the user about potential uncertainties or changes in the figures.
3. **Actionable Content**: The response lacks actionable content that could guide the user on what to do with this information or how it might impact their understanding of Tesla's financial health.

## Recommendation
To improve the response, it is recommended to:
1. Include citations to the specific sections of the provided context documents that support the financial metrics listed.
2. Add any relevant limitations or caveats regarding the financial data to provide a more comprehensive view.
3. Consider including actionable insights or implications of the financial metrics for the user, enhancing the practical value of the information provided.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) does not adequately address the user query regarding Tesla's key balance sheet metrics at the end of 2023. While it acknowledges the absence of specific metrics, it fails to provide the requested financial data or sufficient context.

## Query Satisfaction
The report partially satisfies the query by acknowledging the absence of key balance sheet metrics such as total assets, total liabilities, shareholders' equity, current assets, and current liabilities. However, it does not provide any actual figures or metrics, which are essential for a complete response to the user's request.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  - Include actual balance sheet metrics for Tesla at the end of 2023.
  - Discuss potential risks associated with the absence of this information.
  - Add visualizations or figures to enhance data presentation.
  
- **Unresolved**:
  - Provide context or references to the documents reviewed.

The report has resolved 3 out of 4 issues, leaving one unresolved.

## Remaining Gaps
1. **Provide context or references to the documents reviewed**: The report does not reference specific documents or provide context for the missing metrics, which is crucial for substantiating the claims made.

## Recommendation
The advisor should revise the report to include:
- Actual balance sheet metrics for Tesla at the end of 2023, if available.
- Context or references to the documents reviewed to substantiate the claims about missing data.
- Consider adding visualizations or figures to present the data more effectively, if applicable. 

Addressing these gaps will enhance the report's quality and better meet the user's needs.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_6/query_6
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |        0 |     +0 |
| Risk Assessment      |    15%  |        0 |        0 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       50 |       50 |     +0 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     5.00 |     5.00 |   +0.0 |
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
  Weighted Metrics (3 versions) — document_6/query_6
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |      100 |        0 |        0 |   -100 |     +0 |   -100 |
| Business Analysis    |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Risk Assessment      |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Completeness         |    10%  |        1 |       50 |       50 |    +49 |     +0 |    +49 |
| Query Satisfaction   |    10%  |      100 |        0 |        0 |   -100 |     +0 |   -100 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    35.10 |     5.00 |     5.00 |    -30 |     +0 |    -30 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -30 pts absolute  |  -85.75% relative
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
                "v2_score": 0,
                "delta_v0_v1": -100,
                "delta_v1_v2": 0,
                "delta_v0_v2": -100,
                "weighted_v1": 0.0,
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
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 1,
                "weighted_v0": 0.1,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v0_v1": 49,
                "delta_v1_v2": 0,
                "delta_v0_v2": 49,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "weighted_v0": 10.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -100,
                "delta_v1_v2": 0,
                "delta_v0_v2": -100,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            }
        },
        "overall_v0": 35.1,
        "overall_v1": 5.0,
        "overall_v2": 5.0,
        "improvement_v0_to_v1": -30.1,
        "improvement_v1_to_v2": 0.0,
        "improvement_v0_to_v2": -30.1,
        "improvement_pct_v0_to_v2": -85.75
    }
