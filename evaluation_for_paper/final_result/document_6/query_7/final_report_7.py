"""
Three-Version Evaluation Report — document_6 / query_7
Source document: NASDAQ_TSLA_2023.pdf
Query: What risks related to competition and pricing pressure did Tesla disclose in 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What risks related to competition and pricing pressure did Tesla disclose in 2023?"

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
In 2023, Tesla disclosed several risks related to competition and pricing pressure in its annual report. Key points include:

1. **Increased Competition**: Tesla noted that the automotive market is highly competitive and expected to become even more so as more established and new manufacturers enter the electric vehicle (EV) market. This includes both traditional internal combustion engine vehicles and electric vehicles, which could lead to increased competition for Tesla's offerings.

2. **Pricing Pressure**: The company highlighted that competition could lead to pricing pressure, which may result in lower vehicle unit sales, price reductions, revenue shortfalls, and loss of market share. The introduction of new electric vehicles by competitors could further exacerbate this situation.

3. **Economic Factors**: Tesla acknowledged that the automotive industry is cyclical and sensitive to economic conditions, including inflation and rising interest rates, which could impact the affordability of vehicle financing and leasing arrangements. These economic pressures could lead to decreased consumer demand for Tesla vehicles.

4. **Government Incentives**: Changes in government incentives for electric vehicles could also affect demand and pricing strategies, as these incentives play a significant role in making EVs more attractive to consumers.

Overall, Tesla's disclosures indicate a recognition of the competitive landscape and the potential for pricing pressures that could impact its business performance.
"""

ADVISOR_REPORT_V1 = """
# Tesla 2023 Risks Related to Competition and Pricing Pressure

⚠️ The specific risks related to competition and pricing pressure disclosed in Tesla's 2023 Annual Report (Form 10-K), particularly in the "Item 1A. Risk Factors" section, are currently unavailable. 

As such, I cannot provide the detailed disclosures regarding the company's exposure to competitive pressures and pricing strategies. 

To gain a thorough understanding of Tesla's competitive landscape and pricing strategies, I recommend accessing the "Item 1A. Risk Factors" section of Tesla's 2023 Annual Report directly. This section typically contains valuable insights into the risks the company faces in these areas.

If you have access to that specific section or any additional documents, please share them for further analysis. Alternatively, you may consider checking Tesla's official investor relations website or the SEC's EDGAR database for the complete report.
"""

ADVISOR_REPORT_V2 = """
# Tesla 2023 Risks Related to Competition and Pricing Pressure

Tesla's 2023 Annual Report (Form 10-K) includes a section titled "Item 1A. Risk Factors," which outlines various risks the company faces, particularly those related to competition and pricing pressure. While specific details from this section are not available in the provided context, it is essential to highlight the general types of risks that companies like Tesla typically face in these areas:

- **Valuation Risks**: Fluctuating market conditions can significantly impact Tesla's valuation, affecting investor sentiment and stock performance.
- **Supply Chain Risks**: Dependencies on suppliers and potential disruptions in the supply chain can hinder production capabilities and affect pricing strategies.
- **Regulatory Risks**: Changes in government policies, such as emissions regulations or incentives for electric vehicles, could impact Tesla's operations and profitability.
- **Margin Pressure**: Competitive pricing strategies may lead to reduced profit margins, especially in a rapidly evolving market with increasing competition from other electric vehicle manufacturers.
- **Execution Risks**: Challenges in scaling production to meet demand can result in operational inefficiencies and impact Tesla's market position.

For a comprehensive understanding of Tesla's specific risks related to competition and pricing pressure, I recommend accessing the "Item 1A. Risk Factors" section of Tesla's 2023 Annual Report directly. This section typically contains valuable insights into the risks the company faces in these areas.

You may also consider checking Tesla's official investor relations website or the SEC's EDGAR database for the complete report to ensure you have the most accurate and comprehensive information regarding Tesla's risks.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the risks related to competition and pricing pressure disclosed by Tesla in 2023. However, it lacks proper citations from the provided context documents, which diminishes its credibility and completeness.

## Query Satisfaction
The response effectively covers the key aspects of the user's query by outlining Tesla's disclosures about increased competition, pricing pressure, economic factors, and government incentives. It provides a clear summary of the risks Tesla faces in the competitive automotive market. Therefore, the response satisfies the query in terms of content.

## Remaining Gaps
1. **Source Citations**: The response does not include citations from the context documents, which are essential for grounding the information presented. This absence makes it difficult for the user to verify the claims made in the response.
2. **Actionable Content**: The response lacks actionable content or recommendations that could guide the user on how to interpret or respond to the risks mentioned.

## Recommendation
To improve the response, it is recommended to:
1. Include specific citations from the context documents to support the claims made about Tesla's risks. This will enhance the credibility and reliability of the information provided.
2. Consider adding actionable insights or recommendations based on the disclosed risks, which could help the user understand the implications of these risks on Tesla's business and their own interests.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) partially addresses the user query regarding the risks related to competition and pricing pressure disclosed by Tesla in 2023. However, it does not fully resolve all issues identified by the Critic.

## Query Satisfaction
The revised report provides a general overview of the types of risks Tesla faces related to competition and pricing pressure, which aligns with the user query. However, it lacks specific details and citations from the 2023 Annual Report, which diminishes its effectiveness in answering the query comprehensively.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved:**
  - [Summarize specific risks related to competition and pricing pressure from the 2023 Annual Report.]
  - [Clarify the claim regarding the unavailability of risk information.]
  
- **Unresolved:**
  - [Provide citations or references to the relevant sections of the report.]
  - [Include visual aids or figures to enhance understanding.]

## Remaining Gaps
1. The report does not provide citations or references to the specific sections of the 2023 Annual Report that detail the risks.
2. There are no visual aids or figures included to enhance the understanding of the risks discussed.

## Recommendation
To improve the report, the advisor should:
1. Include specific citations or references to the relevant sections of the 2023 Annual Report that detail the risks related to competition and pricing pressure.
2. Consider adding visual aids or figures to illustrate key points and enhance the report's clarity and effectiveness.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_6/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |       50 |    +50 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |       60 |    +60 |
| Evidence Usage       |    10%  |        0 |       50 |    +50 |
| Completeness         |    10%  |        0 |       70 |    +70 |
| Query Satisfaction   |    10%  |        0 |       80 |    +80 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     0.00 |    47.00 |  +47.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +47.0 pts absolute  |  +0.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_6/query_7
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Business Analysis    |    15%  |       70 |        0 |       50 |    -70 |    +50 |    -20 |
| Risk Assessment      |    15%  |       80 |        0 |       70 |    -80 |    +70 |    -10 |
| Actionable Advice    |    15%  |        0 |        0 |       60 |     +0 |    +60 |    +60 |
| Evidence Usage       |    10%  |        0 |        0 |       50 |     +0 |    +50 |    +50 |
| Completeness         |    10%  |       70 |        0 |       70 |    -70 |    +70 |     +0 |
| Query Satisfaction   |    10%  |       90 |        0 |       80 |    -90 |    +80 |    -10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    38.50 |     0.00 |    47.00 |    -38 |    +47 |     +8 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +8 pts absolute  |  +22.08% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
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
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v0_v1": -70,
                "delta_v1_v2": 50,
                "delta_v0_v2": -20,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 80,
                "weighted_v0": 12.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -80,
                "delta_v1_v2": 70,
                "delta_v0_v2": -10,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
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
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -70,
                "delta_v1_v2": 70,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": -90,
                "delta_v1_v2": 80,
                "delta_v0_v2": -10,
                "weighted_v1": 0.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v0": 38.5,
        "overall_v1": 0.0,
        "overall_v2": 47.0,
        "improvement_v0_to_v1": -38.5,
        "improvement_v1_to_v2": 47.0,
        "improvement_v0_to_v2": 8.5,
        "improvement_pct_v0_to_v2": 22.08
    }
