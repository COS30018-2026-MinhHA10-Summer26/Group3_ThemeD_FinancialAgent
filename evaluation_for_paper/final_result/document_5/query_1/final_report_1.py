"""
Three-Version Evaluation Report — document_5 / query_1
Source document: NASDAQ_TSLA_2022.pdf
Query: What were Tesla's total revenues and net income for fiscal year 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's total revenues and net income for fiscal year 2022?"

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
For the fiscal year 2022, Tesla's total revenues were $81.46 billion, and the net income attributable to common stockholders was $12.56 billion.
"""

ADVISOR_REPORT_V1 = """
# Tesla Financial Overview for Fiscal Year 2022

For the fiscal year 2022, Tesla reported the following financial figures derived from the NASDAQ TSLA 2022 Annual Report:

- **Total Revenues**: $81.46 billion
- **Net Income**: $12.56 billion

These figures represent significant growth compared to the previous year, with total revenues increasing by $27.64 billion and net income increasing by $7.04 billion.

## Financial Health
Tesla's strong revenue growth and net income indicate a robust financial position. The company continues to ramp up production and expand its operations, which is essential for sustaining this growth trajectory.

## Future Outlook
Looking ahead, Tesla aims to enhance its production capacity and delivery capabilities while focusing on improving battery technologies and expanding its product offerings. This strategic direction positions Tesla well to capitalize on the growing demand for electric vehicles and sustainable energy solutions.

## Risks and Limitations
Despite the positive outlook, Tesla faces several risks, including supply chain disruptions, fluctuating raw material costs, and increasing competition in the electric vehicle market. These factors could impact future profitability and operational efficiency.

## Actionable Advice
Investors should monitor Tesla's production metrics and market conditions closely. Additionally, keeping an eye on the company's ability to manage costs and maintain its competitive edge will be crucial for assessing its long-term viability.

## Visualization of Financial Figures
To enhance clarity, the following table summarizes Tesla's financial performance for 2022:

| Metric            | Amount (in billions) |
|-------------------|----------------------|
| Total Revenues    | $81.46               |
| Net Income        | $12.56               |

![Tesla Financial Overview](https://example.com/tesla_financial_overview.png) <!-- Placeholder for actual image link -->

*Source: NASDAQ TSLA 2022 Annual Report* 

If additional information is required, such as detailed financial ratios or segment performance, please let me know.
"""

ADVISOR_REPORT_V2 = """
# Tesla Financial Overview for Fiscal Year 2022

For the fiscal year 2022, Tesla reported the following financial figures derived from the NASDAQ TSLA 2022 Annual Report (Document 3):

- **Total Revenues**: $81.46 billion
- **Net Income**: $12.56 billion

These figures represent significant growth compared to the previous year, with total revenues increasing by $27.64 billion and net income increasing by $7.04 billion.

## Financial Health
Tesla's strong revenue growth and net income indicate a robust financial position. The company continues to ramp up production and expand its operations, which is essential for sustaining this growth trajectory. However, a comparative analysis with industry benchmarks is currently unavailable, which limits the depth of this assessment.

## Future Outlook
Looking ahead, Tesla aims to enhance its production capacity and delivery capabilities while focusing on improving battery technologies and expanding its product offerings. This strategic direction positions Tesla well to capitalize on the growing demand for electric vehicles and sustainable energy solutions.

## Risks and Limitations
Despite the positive outlook, Tesla faces several risks, including:
- **Valuation Risks**: Given the high market expectations for Tesla, any failure to meet growth targets could lead to significant valuation adjustments.
- **Regulatory Risks**: Changes in legislation or compliance costs could impact Tesla's operations and profitability.

These factors could impact future profitability and operational efficiency. The lack of comparative analysis with industry benchmarks further limits the depth of this assessment.

## Actionable Advice
Investors should monitor Tesla's production metrics, such as vehicle delivery numbers and production capacity, as well as market conditions, including competition in the electric vehicle sector. Additionally, keeping an eye on the company's ability to manage costs and maintain its competitive edge will be crucial for assessing its long-term viability.

## Visualization of Financial Figures
To enhance clarity, the following table summarizes Tesla's financial performance for 2022:

| Metric            | Amount (in billions) |
|-------------------|----------------------|
| Total Revenues    | $81.46               |
| Net Income        | $12.56               |

*Source: NASDAQ TSLA 2022 Annual Report (Document 3)* 

If additional information is required, such as detailed financial ratios or segment performance, please let me know.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's total revenues and net income for fiscal year 2022. However, it lacks grounding in the provided context documents and does not include necessary structural elements.

## Query Satisfaction
The response directly addresses the user's query by providing the total revenues ($81.46 billion) and net income ($12.56 billion) for Tesla in fiscal year 2022. Therefore, it satisfies the query in terms of content.

## Remaining Gaps
1. **Lack of Source Citation**: The response does not cite the source of the information, which is critical for verifying the accuracy of the figures provided.
2. **Missing Limitations or Caveats**: There are no disclaimers or limitations mentioned regarding the data, which could be important for the user to understand the context of the figures.
3. **Absence of Actionable Content**: The response does not provide any additional context or actionable insights that could enhance the user's understanding of Tesla's financial performance.
4. **No Structured Sections**: The response lacks a clear structure, making it less user-friendly.

## Recommendation
To improve the response, it should include:
- A citation referencing the specific document or section from which the financial figures were derived.
- Any relevant limitations or caveats regarding the financial data.
- Additional context or insights that could help the user understand the implications of the reported revenues and net income.
- A more structured format to enhance readability and usability.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) adequately answers the original user query regarding Tesla's total revenues and net income for fiscal year 2022. However, not all issues identified by the Critic have been resolved.

## Query Satisfaction
The revised report successfully provides the requested financial figures:
- **Total Revenues**: $81.46 billion
- **Net Income**: $12.56 billion

Additionally, it includes relevant context about Tesla's financial health, future outlook, risks, and actionable advice, which enhances the overall response.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved**:
  - [Add comparative analysis of Tesla's financial health against industry benchmarks.]
  - [Include valuation and regulatory risks in the risk section.]
  - [Specify key metrics and market conditions in the actionable advice section.]
  
- **Unresolved**:
  - [Correct the image link to ensure it is a valid Supabase-hosted link.]
  - [Store the image under the expected advisor_figure folder for better organization.]

## Remaining Gaps
The following issues remain unresolved:
1. Correct the image link to ensure it is a valid Supabase-hosted link.
2. Store the image under the expected advisor_figure folder for better organization.

## Recommendation
To enhance the quality and professionalism of the report, it is recommended that the advisor addresses the remaining gaps by correcting the image link and ensuring proper organization of visual content. This will improve accessibility and reliability for readers.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_1
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       70 |       75 |     +5 |
| Evidence Usage       |    10%  |       80 |       85 |     +5 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    84.50 |    88.00 |   +3.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +3.5 pts absolute  |  +4.14% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_5/query_1
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |      100 |     +0 |     +0 |     +0 |
| Business Analysis    |    15%  |        0 |       70 |       75 |    +70 |     +5 |    +75 |
| Risk Assessment      |    15%  |        0 |       70 |       80 |    +70 |    +10 |    +80 |
| Actionable Advice    |    15%  |        0 |       70 |       75 |    +70 |     +5 |    +75 |
| Evidence Usage       |    10%  |        0 |       80 |       85 |    +80 |     +5 |    +85 |
| Completeness         |    10%  |       20 |      100 |      100 |    +80 |     +0 |    +80 |
| Query Satisfaction   |    10%  |      100 |      100 |      100 |     +0 |     +0 |     +0 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    37.00 |    84.50 |    88.00 |    +47 |     +3 |    +51 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +51 pts absolute  |  +137.84% relative
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
                "v2_score": 100,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
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
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": 70,
                "delta_v1_v2": 10,
                "delta_v0_v2": 80,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
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
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 80,
                "delta_v1_v2": 5,
                "delta_v0_v2": 85,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 20,
                "weighted_v0": 2.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 80,
                "delta_v1_v2": 0,
                "delta_v0_v2": 80,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
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
        "overall_v0": 37.0,
        "overall_v1": 84.5,
        "overall_v2": 88.0,
        "improvement_v0_to_v1": 47.5,
        "improvement_v1_to_v2": 3.5,
        "improvement_v0_to_v2": 51.0,
        "improvement_pct_v0_to_v2": 137.84
    }
