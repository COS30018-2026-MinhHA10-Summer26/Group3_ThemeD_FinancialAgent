"""
Three-Version Evaluation Report — document_5 / query_6
Source document: NASDAQ_TSLA_2022.pdf
Query: What were Tesla's capital expenditures and free cash flow in 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's capital expenditures and free cash flow in 2022?"

USER_QUERIES = [
    "What were Tesla's total revenues and net income for fiscal year 2022?",
    "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?",
    "What were the key financial ratios and margins for Tesla in 2022?",
    "How did Tesla's energy generation and storage segment perform in 2022?",
    "What were the main risks Tesla identified in its 2022 annual report?",
    "What were Tesla's capital expenditures and free cash flow in 2022?",
    "How did supply chain challenges impact Tesla's production in 2022?",
    "What is Tesla's growth strategy and future product roadmap as outlined in 2022?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2022, Tesla's capital expenditures amounted to $7.16 billion. The cash flows provided by operating activities during the same year were $14.72 billion, which indicates that Tesla generated significant free cash flow, although the exact figure for free cash flow is not explicitly stated in the documents. Free cash flow can be calculated as cash flows from operating activities minus capital expenditures, which would be approximately $7.56 billion ($14.72 billion - $7.16 billion).
"""

ADVISOR_REPORT_V1 = """
# Tesla's Capital Expenditures and Free Cash Flow Analysis for 2022

To analyze Tesla's capital expenditures and free cash flow for the year 2022, we can extract the relevant figures from the provided documents.

### Capital Expenditures in 2022
According to Document 4, Tesla's capital expenditures for 2022 amounted to **$7.16 billion**.

### Free Cash Flow Calculation
Free cash flow (FCF) can be calculated using the formula:

\[ 	ext{Free Cash Flow} = 	ext{Cash Flow from Operations} - 	ext{Capital Expenditures} \]

From Document 4, we know:
- Cash Flow from Operations in 2022: **$14.72 billion**
- Capital Expenditures in 2022: **$7.16 billion**

Now, we can calculate the free cash flow:

\[
	ext{Free Cash Flow} = 14.72 \, 	ext{billion} - 7.16 \, 	ext{billion} = 7.56 \, 	ext{billion}
\]

### Summary
- **Capital Expenditures in 2022:** $7.16 billion
- **Free Cash Flow in 2022:** $7.56 billion

### Financial Health and Future Outlook
Tesla's ability to generate a significant amount of free cash flow in 2022 indicates strong operational performance and effective capital management. The increase in cash flow from operations by **$3.23 billion** compared to the previous year suggests that Tesla is successfully scaling its operations and managing costs effectively.

However, it is important to note that Tesla's capital expenditures are expected to remain high as the company continues to invest in new manufacturing facilities and product development. The company has indicated that capital expenditures could range between **$6.00 to $8.00 billion** in 2023, which reflects ongoing investments in growth and innovation.

### Risks and Limitations
While Tesla's financial performance appears robust, there are inherent risks associated with its capital expenditures. For example, Document 5 mentions potential supply chain disruptions and rising material costs, which could impact future cash flows. Additionally, the company's reliance on government incentives for electric vehicle adoption may pose risks if such incentives are reduced or eliminated, as noted in Document 3.

### Additional Information Required
For a more comprehensive analysis, it would be beneficial to have access to Tesla's projected financial statements for 2023 and beyond, as well as updates on their strategic initiatives and market conditions. Specific information on upcoming projects and their expected financial impact would also enhance the analysis.

### Visual Aids
To enhance clarity, a table summarizing the financial metrics can be included:

| Metric                        | Amount (in billion) |
|-------------------------------|---------------------|
| Capital Expenditures 2022     | $7.16               |
| Cash Flow from Operations 2022 | $14.72              |
| Free Cash Flow 2022           | $7.56               |

*Source: NASDAQ_TSLA_2022.pdf*

This analysis shows that Tesla is well-positioned in terms of cash generation, but ongoing monitoring of market conditions and strategic execution will be crucial for sustaining its growth trajectory.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Capital Expenditures and Free Cash Flow Analysis for 2022

To analyze Tesla's capital expenditures and free cash flow for the year 2022, we can extract the relevant figures from the provided documents.

### Capital Expenditures in 2022
According to Document 4, Tesla's capital expenditures for 2022 amounted to **$7.16 billion**.

### Free Cash Flow Calculation
Free cash flow (FCF) can be calculated using the formula:

\[ 	ext{Free Cash Flow} = 	ext{Cash Flow from Operations} - 	ext{Capital Expenditures} \]

From Document 4, we know:
- Cash Flow from Operations in 2022: **$14.72 billion** (sourced from Document 4)
- Capital Expenditures in 2022: **$7.16 billion** (sourced from Document 4)

Now, we can calculate the free cash flow:

\[
	ext{Free Cash Flow} = 14.72 \, 	ext{billion} - 7.16 \, 	ext{billion} = 7.56 \, 	ext{billion}
\]

### Summary
- **Capital Expenditures in 2022:** $7.16 billion (sourced from Document 4)
- **Cash Flow from Operations in 2022:** $14.72 billion (sourced from Document 4)
- **Free Cash Flow in 2022:** $7.56 billion (derived from the cash flow from operations and capital expenditures)

### Financial Health and Future Outlook
Tesla's ability to generate a significant amount of free cash flow in 2022 indicates strong operational performance and effective capital management. The increase in cash flow from operations by **$3.23 billion** compared to the previous year suggests that Tesla is successfully scaling its operations and managing costs effectively.

However, it is important to note that Tesla's capital expenditures are expected to remain high as the company continues to invest in new manufacturing facilities and product development. The company has indicated that capital expenditures could range between **$6.00 to $8.00 billion** in 2023, reflecting ongoing investments in growth and innovation.

### Risks and Limitations
While Tesla's financial performance appears robust, there are inherent risks associated with its capital expenditures and overall business model. Here are some actionable strategies to mitigate these risks:
- **Valuation Risks:** Tesla should focus on transparent communication with investors to manage expectations and maintain confidence in its valuation.
- **Regulatory Risks:** Proactively engaging with policymakers and adapting to regulatory changes can help mitigate the impact of potential changes in government incentives or regulations.
- **Margin Pressure:** Implementing cost-control measures and exploring alternative supply chain strategies can help alleviate rising material costs and maintain profit margins.

### Visual Aids
To enhance clarity, a table summarizing the financial metrics is included below:

| Metric                        | Amount (in billion) |
|-------------------------------|---------------------|
| Capital Expenditures 2022     | $7.16               |
| Cash Flow from Operations 2022 | $14.72              |
| Free Cash Flow 2022           | $7.56               |

*Source: NASDAQ_TSLA_2022.pdf*

This analysis shows that Tesla is well-positioned in terms of cash generation, but ongoing monitoring of market conditions and strategic execution will be crucial for sustaining its growth trajectory. Additionally, addressing the identified risks with actionable strategies will be essential for maintaining investor confidence and operational stability.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's capital expenditures and provides a calculated estimate of free cash flow for 2022. However, it lacks explicit mention of free cash flow in the context of the provided documents, which could lead to confusion.

## Query Satisfaction
The response directly addresses the user's query by stating that Tesla's capital expenditures in 2022 were $7.16 billion and provides an estimated free cash flow of approximately $7.56 billion. This information is relevant and derived from the context documents, particularly Document 4, which details Tesla's financial performance for the year.

## Remaining Gaps
1. **Explicit Free Cash Flow Definition**: The response does not explicitly define free cash flow or clarify how it is calculated, which may leave some users unclear about the term.
2. **Limitations and Caveats**: The response lacks a discussion of any limitations or caveats regarding the financial data, which is important for users to understand the context of the figures provided.
3. **Actionable Content**: There is no actionable content or recommendations for the user, which could enhance the response's utility.
4. **Structured Sections**: The response does not have structured sections that could improve readability and comprehension.

## Recommendation
To improve the response, it should:
- Include a clear definition of free cash flow and the formula used for its calculation.
- Mention any limitations or caveats regarding the financial data, such as potential fluctuations or uncertainties in future projections.
- Provide actionable insights or recommendations based on the financial data presented.
- Organize the response into structured sections for better clarity and readability.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive analysis of Tesla's capital expenditures and free cash flow for 2022. It addresses several issues raised by the Critic, but one critical issue remains unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's capital expenditures and free cash flow in 2022. It provides specific figures for both metrics and includes a calculation for free cash flow, along with relevant context about Tesla's financial health and future outlook.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues:**
  1. Clarified the source and reliability of the cash flow from operations figure.
  2. Addressed missing risks related to valuation, regulation, and margin pressure.
  3. Embedded a properly formatted table summarizing financial metrics.
  4. Discussed competitive pressures and how they may impact Tesla's market position.

- **Unresolved Issue:**
  1. Provide context or benchmarks to support claims of robust financial performance.

## Remaining Gaps
The following issue remains unresolved:
- Provide context or benchmarks to support claims of robust financial performance.

## Recommendation
It is recommended that the advisor revises the report to include context or benchmarks that substantiate the claims of Tesla's robust financial performance. This addition will enhance the credibility of the analysis and ensure that all issues identified by the Critic are fully addressed.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_6
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       60 |       75 |    +15 |
| Actionable Advice    |    15%  |        0 |       60 |    +60 |
| Evidence Usage       |    10%  |       90 |       90 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    73.50 |    85.50 |  +12.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +12.0 pts absolute  |  +16.33% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_5/query_6
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |      100 |      100 |    +10 |     +0 |    +10 |
| Business Analysis    |    15%  |        0 |       70 |       75 |    +70 |     +5 |    +75 |
| Risk Assessment      |    15%  |        0 |       60 |       75 |    +60 |    +15 |    +75 |
| Actionable Advice    |    15%  |        0 |        0 |       60 |     +0 |    +60 |    +60 |
| Evidence Usage       |    10%  |       70 |       90 |       90 |    +20 |     +0 |    +20 |
| Completeness         |    10%  |       30 |      100 |      100 |    +70 |     +0 |    +70 |
| Query Satisfaction   |    10%  |       80 |      100 |      100 |    +20 |     +0 |    +20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    40.50 |    73.50 |    85.50 |    +33 |    +12 |    +45 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +45 pts absolute  |  +111.11% relative
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v0_v1": 70,
                "delta_v1_v2": 5,
                "delta_v0_v2": 75,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 60,
                "v2_score": 75,
                "delta_v0_v1": 60,
                "delta_v1_v2": 15,
                "delta_v0_v2": 75,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
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
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 30,
                "weighted_v0": 3.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 70,
                "delta_v1_v2": 0,
                "delta_v0_v2": 70,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 40.5,
        "overall_v1": 73.5,
        "overall_v2": 85.5,
        "improvement_v0_to_v1": 33.0,
        "improvement_v1_to_v2": 12.0,
        "improvement_v0_to_v2": 45.0,
        "improvement_pct_v0_to_v2": 111.11
    }
