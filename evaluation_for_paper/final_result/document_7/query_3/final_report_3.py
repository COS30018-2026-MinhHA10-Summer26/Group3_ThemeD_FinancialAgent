"""
Three-Version Evaluation Report — document_7 / query_3
Source document: NASDAQ_TSLA_2024.pdf
Query: What was Tesla's gross margin on automotive sales in 2024 and how did it compare to 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What was Tesla's gross margin on automotive sales in 2024 and how did it compare to 2023?"

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
Tesla's gross margin on automotive sales in 2024 was **18.4%**, which represents a decrease from **19.4%** in 2023. This indicates a decline in gross margin year-over-year.
"""

ADVISOR_REPORT_V1 = """
### Tesla's Gross Margin on Automotive Sales in 2024

In 2024, Tesla's gross margin for total automotive sales was **18.4%**. This represents a decrease from **19.4%** in 2023.

### Comparison of Gross Margin (2024 vs. 2023)

| Year | Gross Margin |
|------|--------------|
| 2024 | 18.4%        |
| 2023 | 19.4%        |

### Summary

- **2024 Gross Margin**: 18.4%
- **2023 Gross Margin**: 19.4%
- **Change**: Decrease of 1.0 percentage points

This decline in gross margin was primarily attributed to lower average selling prices on vehicles and the ramp-up costs associated with the Cybertruck, despite some offset from lower average combined costs per unit and increases in regulatory credit and FSD (Supervised) revenue.

### Financial Health and Future Outlook

Tesla's gross margin decline indicates challenges in maintaining profitability amidst pricing pressures and increased production costs. The company may need to focus on cost management and enhancing operational efficiencies to stabilize margins. 

### Risks and Limitations

Potential risks include fluctuating raw material costs, competition in the electric vehicle market, and the impact of economic conditions on consumer demand. Additionally, the ramp-up of new models like the Cybertruck may involve unforeseen expenses.

### Actionable Advice

To improve gross margins, Tesla should consider strategies such as optimizing supply chain management, exploring cost-effective production techniques, and potentially adjusting pricing strategies to enhance competitiveness without sacrificing profitability.

### Source
Data derived from the Tesla 2024 Annual Report (Form 10-K).
"""

ADVISOR_REPORT_V2 = """
### Tesla's Gross Margin on Automotive Sales in 2024

In 2024, Tesla's gross margin for total automotive sales was **18.4%**, a decrease from **19.4%** in 2023.

### Comparison of Gross Margin (2024 vs. 2023)

| Year | Gross Margin |
|------|--------------|
| 2024 | 18.4%        |
| 2023 | 19.4%        |

### Summary

- **2024 Gross Margin**: 18.4%
- **2023 Gross Margin**: 19.4%
- **Change**: Decrease of 1.0 percentage points

This decline in gross margin was primarily attributed to lower average selling prices on vehicles and the ramp-up costs associated with the Cybertruck. The decrease was partially offset by lower average combined costs per unit and increases in regulatory credit and FSD (Supervised) revenue.

### Financial Health and Future Outlook

Tesla's gross margin decline indicates challenges in maintaining profitability amidst pricing pressures and increased production costs. The company may need to focus on cost management and enhancing operational efficiencies to stabilize margins.

### Risks and Limitations

Potential risks include fluctuating raw material costs, competition in the electric vehicle market, and the impact of economic conditions on consumer demand. Additionally, the ramp-up of new models like the Cybertruck may involve unforeseen expenses. The risk of valuation is also significant, as fluctuations in gross margin could affect investor sentiment and market perception.

### Actionable Advice

To improve gross margins, Tesla should consider strategies such as optimizing supply chain management, exploring cost-effective production techniques, and potentially adjusting pricing strategies to enhance competitiveness without sacrificing profitability. These strategies should be directly linked to the challenges identified in the report.

### Visual Representation

![Tesla's Gross Margin Trends (2023-2024)](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_05b4a0535dea_tesla-s-gross-margin-trends-2023-2024.png)

*Figure: Trend of Tesla's gross margin on automotive sales from 2023 to 2024.*

*Source: Data derived from the Tesla 2024 Annual Report (Form 10-K).*
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's gross margin on automotive sales for 2024 and its comparison to 2023. However, it lacks grounding in the provided context documents and misses essential structural elements.

## Query Satisfaction
The response directly addresses the user's question by providing the gross margin figures for 2024 (18.4%) and 2023 (19.4%), indicating a decline in gross margin year-over-year. Therefore, it satisfies the query in terms of content.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is crucial for validating the information provided.
2. **Missing Limitations or Caveats**: There are no disclaimers or notes about the potential variability in financial data or external factors that could affect the gross margin.
3. **Absence of Actionable Content**: The response does not provide any recommendations or insights based on the gross margin figures, which could enhance its usefulness to the user.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the figures provided.
- Add limitations or caveats regarding the financial data to inform the user of potential uncertainties.
- Consider providing actionable insights or implications of the gross margin changes to enhance the response's value.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) adequately addresses the user query regarding Tesla's gross margin on automotive sales for 2024 and its comparison to 2023. However, one critical issue remains unresolved.

## Query Satisfaction
The report successfully provides the requested information:
- It states Tesla's gross margin for 2024 (18.4%) and compares it to 2023 (19.4%).
- It includes a summary table and discusses the factors contributing to the margin decline, fulfilling the user's request.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  1. Provided specific data to quantify the impact of lower average selling prices and Cybertruck ramp-up costs on gross margin.
  2. Clarified the contribution of regulatory credit and FSD revenue increases to the gross margin.
  3. Included visual representations of gross margin trends.
  4. Discussed the sustainability of revenue sources like regulatory credits and FSD in the context of competitive pressures.

- **Unresolved Issue**:
  - The report still needs to address the missing risk of valuation and its implications for investors.

## Remaining Gaps
- The report does not adequately discuss how fluctuations in gross margin could affect Tesla's valuation and investor sentiment. This is a critical aspect that needs to be included to enhance the report's comprehensiveness.

## Recommendation
To finalize the report, the advisor should:
- Include a detailed analysis of the risk of valuation, explaining how changes in gross margin may impact investor perceptions and the overall market valuation of Tesla. This addition will ensure that all identified issues are resolved and provide a more robust analysis for the users.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_7/query_3
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       75 |       85 |    +10 |
| Evidence Usage       |    10%  |       90 |       90 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    86.25 |    90.00 |  +3.75 |
+----------------------+--------+----------+----------+--------+
  Improvement: +3.75 pts absolute  |  +4.35% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_7/query_3
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |      100 |      100 |    +10 |     +0 |    +10 |
| Business Analysis    |    15%  |        0 |       70 |       75 |    +70 |     +5 |    +75 |
| Risk Assessment      |    15%  |        0 |       70 |       80 |    +70 |    +10 |    +80 |
| Actionable Advice    |    15%  |        0 |       75 |       85 |    +75 |    +10 |    +85 |
| Evidence Usage       |    10%  |        0 |       90 |       90 |    +90 |     +0 |    +90 |
| Completeness         |    10%  |       20 |      100 |      100 |    +80 |     +0 |    +80 |
| Query Satisfaction   |    10%  |      100 |      100 |      100 |     +0 |     +0 |     +0 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    34.50 |    86.25 |    90.00 |    +51 |     +3 |    +55 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +55 pts absolute  |  +160.87% relative
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
                "v1_score": 75,
                "v2_score": 85,
                "delta_v0_v1": 75,
                "delta_v1_v2": 10,
                "delta_v0_v2": 85,
                "weighted_v1": 11.25,
                "weighted_v2": 12.75
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 90,
                "delta_v1_v2": 0,
                "delta_v0_v2": 90,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
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
        "overall_v0": 34.5,
        "overall_v1": 86.25,
        "overall_v2": 90.0,
        "improvement_v0_to_v1": 51.75,
        "improvement_v1_to_v2": 3.75,
        "improvement_v0_to_v2": 55.5,
        "improvement_pct_v0_to_v2": 160.87
    }
