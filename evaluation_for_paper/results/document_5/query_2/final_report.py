"""
Full Pipeline Evaluation Report — document_5 / query_2
Source document: NASDAQ_TSLA_2022.pdf
Query: How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?
"""
from __future__ import annotations
import json

USER_QUERY = "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?"

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

ADVISOR_REPORT_V1 = """
# Tesla Vehicle Deliveries in 2022 vs. 2021

⚠️ The specific number of vehicles delivered by Tesla in 2022 and 2021 was not found in the available documents. This figure cannot be confirmed without the source filing.

To provide a comprehensive analysis, I recommend checking Tesla's official annual report or investor relations website for the specific delivery numbers for both years. If you have access to additional documents or data, please share them, and I can assist further.
"""

ADVISOR_REPORT_V2 = """
# Tesla Vehicle Deliveries in 2022 vs. 2021

⚠️ The specific number of vehicles delivered by Tesla in 2022 and 2021 was not found in the available documents. This figure cannot be confirmed without the source filing.

To provide a comprehensive analysis, I recommend checking Tesla's official annual report or investor relations website for the specific delivery numbers for both years. If you have access to additional documents or data, please share them, and I can assist further.

## Key Risks Impacting Tesla's Market Position

1. **Competition**: The automotive industry is highly competitive, with numerous players vying for market share in the electric vehicle segment. Tesla must continuously innovate and improve its offerings to maintain its competitive edge.

2. **Valuation**: Changes in consumer demand for electric vehicles and overall market conditions can significantly impact Tesla's valuation. Investors should monitor these factors closely.

3. **Supply Chain**: Tesla's reliance on global suppliers exposes it to potential disruptions. Issues such as semiconductor shortages and other supply chain challenges could affect production and delivery timelines.

4. **Regulation**: Regulatory changes affecting electric vehicles, including emissions standards and incentives, could pose risks to Tesla's operations and market strategy.

5. **Margin Pressure**: Rising costs, including inflation and increased material prices, could impact Tesla's profit margins. The company must manage these costs effectively to sustain profitability.

## Conclusion

The absence of specific delivery numbers for 2022 and 2021 limits the analysis of Tesla's performance. It is crucial to obtain these figures to evaluate the company's growth trajectory and market position accurately. Additionally, understanding the risks outlined above will provide a clearer picture of the challenges Tesla faces in the evolving automotive landscape.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) does not adequately answer the original user query regarding Tesla's vehicle deliveries in 2022 and how they compare to 2021. While it addresses some key risks and provides a structured analysis, it fails to include the specific delivery numbers that were essential to the user's request.

## Query Satisfaction
The report does not satisfy the query as it explicitly states that the specific number of vehicles delivered by Tesla in 2022 and 2021 was not found in the available documents. This omission is critical since the user specifically asked for these figures.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved Issues**:
  1. Addressed competition, valuation, supply chain, regulation, and margin pressure risks.
  2. Provided contextual analysis of delivery numbers and risks on Tesla's market position.
  3. Incorporated a structured approach to the report.

- **Unresolved Issue**:
  1. The report still lacks relevant figures or charts to support the analysis.

## Remaining Gaps
1. Include relevant figures or charts to support the analysis of Tesla's vehicle deliveries and market position.

## Recommendation
The advisor should revise the report to include the specific vehicle delivery numbers for 2022 and 2021, as well as relevant visual data representations. This will enhance the report's credibility and provide a comprehensive analysis that meets the user's original query.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_2
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |       50 |    +50 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       50 |       70 |    +20 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     5.00 |    25.00 |  +20.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +20.0 pts absolute  |  +400.0% relative
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
                "v2_score": 50,
                "delta": 50,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
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
                "v1_score": 50,
                "v2_score": 70,
                "delta": 20,
                "weighted_v1": 5.0,
                "weighted_v2": 7.0
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
        "overall_v1": 5.0,
        "overall_v2": 25.0,
        "absolute_improvement": 20.0,
        "improvement_percentage": 400.0
    }
