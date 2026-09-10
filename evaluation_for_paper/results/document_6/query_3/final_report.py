"""
Full Pipeline Evaluation Report — document_6 / query_3
Source document: NASDAQ_TSLA_2023.pdf
Query: What were Tesla's total vehicle deliveries and production volumes in 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What were Tesla's total vehicle deliveries and production volumes in 2023?"

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

ADVISOR_REPORT_V1 = """
# Tesla 2023 Vehicle Deliveries and Production Volumes Report

Unfortunately, the total vehicle deliveries and production volumes for Tesla in 2023 were not found in the available documents. This information is crucial for a comprehensive understanding of Tesla's performance in that year.

To obtain these figures, I recommend checking the following sources:
- Tesla's official website, particularly their Investor Relations section, where they often publish quarterly and annual reports.
- The SEC filings, specifically the Form 10-K for the fiscal year ended December 31, 2023, which may contain detailed operational metrics.
- Financial news outlets that cover Tesla, as they may report on these figures following their release.

If you have access to additional documents or specific reports, please share them, and I can assist further in extracting the required information.
"""

ADVISOR_REPORT_V2 = """
# Tesla 2023 Vehicle Deliveries and Production Volumes Report

Unfortunately, the total vehicle deliveries and production volumes for Tesla in 2023 were not found in the available documents. This information is crucial for a comprehensive understanding of Tesla's performance in that year.

## Reviewed Documents
The following documents were reviewed to extract the requested information:
- **NASDAQ_TSLA_2023.pdf**: This document includes Tesla's Form 10-K for the fiscal year ended December 31, 2023, but it does not contain specific figures for total vehicle deliveries and production volumes (referenced on Page 1 and Page 2).

## Implications of Missing Data
The absence of data on vehicle deliveries and production volumes can have several implications:
- **Investor Confidence**: Lack of transparency regarding operational metrics may lead to decreased investor confidence.
- **Stock Price Volatility**: Uncertainty about production capabilities can contribute to stock price fluctuations.
- **Operational Challenges**: Without this data, stakeholders may question Tesla's ability to meet market demand and manage supply chain issues effectively.

## Recommendations for Data Retrieval
To obtain these figures, I recommend checking the following sources:
- **Tesla's Official Website**: Visit the Investor Relations section, where they often publish quarterly and annual reports that may include the desired metrics.
- **SEC Filings**: Review the Form 10-K for the fiscal year ended December 31, 2023, as it may contain detailed operational metrics.
- **Financial News Outlets**: Look for reports from reputable financial news sources that cover Tesla, as they may report on these figures following their release.

If you have access to additional documents or specific reports, please share them, and I can assist further in extracting the required information.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) does not adequately address the original user query regarding Tesla's total vehicle deliveries and production volumes in 2023. While it provides some context and implications of the missing data, it fails to deliver the requested figures or a comprehensive analysis.

## Query Satisfaction
The report does not satisfy the user query as it explicitly states that the total vehicle deliveries and production volumes for Tesla in 2023 were not found in the available documents. Although it mentions the reviewed documents, it does not provide the specific data requested.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved**:
  - Include total vehicle deliveries and production volumes for 2023.
  - Strengthen recommendations with specific guidance on where to find the data.
  
- **Unresolved**:
  - Specify which documents were reviewed and why they were insufficient.
  - Address potential risks associated with the lack of data.
  - Incorporate relevant figures or visualizations to support claims.

## Remaining Gaps
1. The report does not specify which documents were reviewed and why they were deemed insufficient for providing the requested data.
2. It fails to address potential risks associated with the absence of delivery and production data, such as impacts on investor confidence and stock price volatility.
3. There are no relevant figures or visualizations included to support the claims made in the report.

## Recommendation
To improve the report, the advisor should:
1. Include specific figures for total vehicle deliveries and production volumes for 2023, sourced from the relevant documents.
2. Provide a detailed analysis of how these figures impact Tesla's financial health and market position.
3. Address potential risks associated with the lack of this data and how it could affect investor sentiment.
4. Incorporate visual aids or figures to support claims and enhance the report's clarity and engagement.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_6/query_3
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |        0 |     +0 |
| Risk Assessment      |    15%  |        0 |        0 |     +0 |
| Actionable Advice    |    15%  |        0 |       70 |    +70 |
| Evidence Usage       |    10%  |        0 |       50 |    +50 |
| Completeness         |    10%  |        0 |       70 |    +70 |
| Query Satisfaction   |    10%  |        0 |       50 |    +50 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     0.00 |    27.50 |  +27.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +27.5 pts absolute  |  +0.0% relative
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
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
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
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 50,
                "delta": 50,
                "weighted_v1": 0.0,
                "weighted_v2": 5.0
            }
        },
        "overall_v1": 0.0,
        "overall_v2": 27.5,
        "absolute_improvement": 27.5,
        "improvement_percentage": 0.0
    }
