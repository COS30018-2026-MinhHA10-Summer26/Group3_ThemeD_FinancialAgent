"""
Three-Version Evaluation Report — document_2 / query_5
Source document: NASDAQ_AMZN_2023.pdf
Query: What were the key balance sheet highlights for Amazon at the end of 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were the key balance sheet highlights for Amazon at the end of 2023?"

USER_QUERIES = [
    "What were Amazon's total revenues and operating income for fiscal year 2023?",
    "How did AWS revenue growth trend in 2023 and what drove it?",
    "What cost optimization measures did Amazon undertake in 2023?",
    "How did Amazon's advertising revenue segment grow in 2023?",
    "What were the key balance sheet highlights for Amazon at the end of 2023?",
    "How did Amazon's North America segment margin recover in 2023?",
    "What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?",
    "What generative AI and technology investments did Amazon highlight in 2023?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
At the end of 2023, Amazon's key balance sheet highlights included:

1. **Total Assets**: Amazon's total assets increased from $462.7 billion in 2022 to $527.9 billion in 2023.

2. **Cash and Cash Equivalents**: The company reported cash and cash equivalents of $73.4 billion, up from $53.9 billion in the previous year.

3. **Marketable Securities**: Marketable securities decreased slightly from $16.1 billion in 2022 to $13.4 billion in 2023.

4. **Inventories**: Inventories were reported at $33.3 billion, a slight decrease from $34.4 billion in 2022.

5. **Accounts Receivable**: Accounts receivable increased from $42.4 billion in 2022 to $52.3 billion in 2023.

6. **Total Liabilities**: Total liabilities rose from $316.6 billion in 2022 to $326.5 billion in 2023.

7. **Long-term Debt**: Long-term debt decreased from $67.2 billion in 2022 to $58.3 billion in 2023.

8. **Stockholders' Equity**: Stockholders' equity increased significantly from $146.0 billion in 2022 to $201.9 billion in 2023.

These figures reflect Amazon's strong financial position and growth in various areas, particularly in cash and accounts receivable.
"""

ADVISOR_REPORT_V1 = """
# Amazon 2023 Balance Sheet Highlights

At the end of 2023, specific balance sheet figures such as total assets, total liabilities, equity, cash and cash equivalents, and long-term debt are not available in the provided documents. Therefore, we cannot provide the requested balance sheet highlights. 

However, we can highlight some key financial metrics that reflect Amazon's performance:

- **Total Revenue**: Amazon's total revenue grew 12% year-over-year from $514 billion in 2022 to **$575 billion** in 2023.
- **Operating Income**: The operating income saw a significant increase of 201% year-over-year, rising from **$12.2 billion** (with an operating margin of 2.4%) in 2022 to **$36.9 billion** (with an operating margin of 6.4%) in 2023.
- **Free Cash Flow (FCF)**: Amazon's trailing twelve-month FCF adjusted for equipment finance leases improved dramatically from **-$12.8 billion** in 2022 to **$35.5 billion** in 2023, marking an increase of **$48.3 billion**.

### Summary
While we cannot provide specific balance sheet highlights due to the absence of detailed balance sheet data, the substantial growth in revenue, operating income, and free cash flow indicates a strong financial position for Amazon at the end of 2023. For a complete analysis, access to the detailed balance sheet figures would be necessary. If you have access to Amazon's financial statements or balance sheet data for 2023, please provide that information for further analysis.
"""

ADVISOR_REPORT_V2 = """
# Amazon 2023 Balance Sheet Highlights

At the end of 2023, specific balance sheet figures such as total assets, total liabilities, equity, cash and cash equivalents, and long-term debt are not available in the provided documents. Therefore, we cannot provide the requested balance sheet highlights.

However, we can highlight some key financial metrics that reflect Amazon's performance:

- **Total Revenue**: Amazon's total revenue grew 12% year-over-year from **$514 billion** in 2022 to **$575 billion** in 2023.
- **Operating Income**: The operating income saw a significant increase of 201% year-over-year, rising from **$12.2 billion** (with an operating margin of 2.4%) in 2022 to **$36.9 billion** (with an operating margin of 6.4%) in 2023.
- **Free Cash Flow (FCF)**: Amazon's trailing twelve-month FCF adjusted for equipment finance leases improved dramatically from **-$12.8 billion** in 2022 to **$35.5 billion** in 2023, marking an increase of **$48.3 billion**.

## Key Financial Metrics Table

| Metric                  | 2022 (in billion $) | 2023 (in billion $) |
|-------------------------|----------------------|----------------------|
| Total Revenue           | 514                  | 575                  |
| Operating Income        | 12.2                 | 36.9                 |
| Free Cash Flow (FCF)    | -12.8                | 35.5                 |

### Implications of Missing Balance Sheet Data
The absence of specific balance sheet data limits our ability to assess Amazon's liquidity and solvency comprehensively. Key balance sheet figures are crucial for understanding the company's financial health, including its ability to meet short-term obligations and manage long-term debt. Without this information, investors may find it challenging to evaluate the overall risk profile of the company.

### Summary
While we cannot provide specific balance sheet highlights due to the absence of detailed balance sheet data, the substantial growth in revenue, operating income, and free cash flow indicates a strong operational performance for Amazon at the end of 2023. These metrics suggest improved profitability and cash generation capabilities, which are positive indicators for the company's financial health.

### Risks and Considerations
Investors should consider potential risks, including competition, regulatory challenges, and operational execution risks that could impact future performance. The lack of balance sheet data raises questions about liquidity and solvency, which are critical for a comprehensive financial analysis.

For a complete analysis, access to the detailed balance sheet figures would be necessary. If you have access to Amazon's financial statements or balance sheet data for 2023, please provide that information for further analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's key balance sheet highlights at the end of 2023. However, it lacks citations for the data presented and does not include any limitations or actionable content, which diminishes its overall quality.

## Query Satisfaction
The response effectively covers the key aspects of Amazon's balance sheet, including total assets, cash and cash equivalents, marketable securities, inventories, accounts receivable, total liabilities, long-term debt, and stockholders' equity. Each of these points is relevant to the user's inquiry about the financial highlights at the end of 2023.

## Remaining Gaps
1. **Source Citations**: The response does not provide citations for the financial figures mentioned, which is crucial for verifying the accuracy of the information.
2. **Limitations or Caveats**: There are no disclaimers or notes regarding the potential variability of the figures or the context in which they should be interpreted.
3. **Actionable Content**: The response lacks any actionable insights or recommendations based on the financial highlights, which could enhance its utility for the user.

## Recommendation
To improve the response, it is recommended to:
1. Include citations for the financial data to enhance credibility and allow users to verify the information.
2. Add any relevant limitations or caveats regarding the financial figures to provide context.
3. Consider including actionable insights or implications of the financial highlights to make the response more valuable to the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more structured and informative overview of Amazon's financial performance at the end of 2023. However, it still lacks certain critical elements, particularly in visual representation, which limits its effectiveness.

## Query Satisfaction
The report adequately addresses the user query regarding key balance sheet highlights by providing relevant financial metrics such as total revenue, operating income, and free cash flow. However, it fails to provide specific balance sheet figures, which were explicitly requested.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  - Included a discussion on potential risks and downsides.
  - Cited sources for financial metrics presented.
  - Provided a structured table summarizing key financial metrics.
  
- **Unresolved**:
  - The report does not incorporate visual aids to enhance understanding of financial data.

## Remaining Gaps
- [ ] **Incorporate visual aids to enhance understanding of financial data.**

## Recommendation
To improve the report further, the advisor should include visual representations, such as charts or graphs, to illustrate the key financial metrics. This addition would enhance clarity and provide a more comprehensive view of Amazon's financial health at the end of 2023.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_2/query_5
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       80 |       80 |     +0 |
| Business Analysis    |    15%  |       50 |       60 |    +10 |
| Risk Assessment      |    15%  |       40 |       60 |    +20 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |       70 |       70 |     +0 |
| Completeness         |    10%  |       70 |       80 |    +10 |
| Query Satisfaction   |    10%  |       50 |       60 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    52.50 |    59.00 |   +6.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +6.5 pts absolute  |  +12.38% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_2/query_5
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       95 |       80 |       80 |    -15 |     +0 |    -15 |
| Business Analysis    |    15%  |       20 |       50 |       60 |    +30 |    +10 |    +40 |
| Risk Assessment      |    15%  |       10 |       40 |       60 |    +30 |    +20 |    +50 |
| Actionable Advice    |    15%  |       10 |        0 |        0 |    -10 |     +0 |    -10 |
| Evidence Usage       |    10%  |       15 |       70 |       70 |    +55 |     +0 |    +55 |
| Completeness         |    10%  |       50 |       70 |       80 |    +20 |    +10 |    +30 |
| Query Satisfaction   |    10%  |       90 |       50 |       60 |    -40 |    +10 |    -30 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    45.25 |    52.50 |    59.00 |     +7 |     +6 |    +13 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +13 pts absolute  |  +30.39% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 95,
                "weighted_v0": 23.75,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v0_v1": -15,
                "delta_v1_v2": 0,
                "delta_v0_v2": -15,
                "weighted_v1": 20.0,
                "weighted_v2": 20.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 20,
                "weighted_v0": 3.0,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v0_v1": 30,
                "delta_v1_v2": 10,
                "delta_v0_v2": 40,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 10,
                "weighted_v0": 1.5,
                "v1_score": 40,
                "v2_score": 60,
                "delta_v0_v1": 30,
                "delta_v1_v2": 20,
                "delta_v0_v2": 50,
                "weighted_v1": 6.0,
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
                "v0_score": 15,
                "weighted_v0": 1.5,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v0_v1": 55,
                "delta_v1_v2": 0,
                "delta_v0_v2": 55,
                "weighted_v1": 7.0,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 50,
                "weighted_v0": 5.0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": 20,
                "delta_v1_v2": 10,
                "delta_v0_v2": 30,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v0_v1": -40,
                "delta_v1_v2": 10,
                "delta_v0_v2": -30,
                "weighted_v1": 5.0,
                "weighted_v2": 6.0
            }
        },
        "overall_v0": 45.25,
        "overall_v1": 52.5,
        "overall_v2": 59.0,
        "improvement_v0_to_v1": 7.25,
        "improvement_v1_to_v2": 6.5,
        "improvement_v0_to_v2": 13.75,
        "improvement_pct_v0_to_v2": 30.39
    }
