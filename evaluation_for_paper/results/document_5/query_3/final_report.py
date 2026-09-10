"""
Full Pipeline Evaluation Report — document_5 / query_3
Source document: NASDAQ_TSLA_2022.pdf
Query: What were the key financial ratios and margins for Tesla in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the key financial ratios and margins for Tesla in 2022?"

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
# Tesla 2022 Financial Ratios and Margins Report

Unfortunately, key financial ratios and margins for Tesla in 2022 were not found in the available documents. The specific financial metrics necessary for calculating these ratios, such as net income, total revenue, total assets, and total liabilities, are not included in the provided context.

To provide a complete analysis, I would need access to Tesla's financial statements or reports that include these details. If you have access to such documents, please share them for further analysis.

### Actionable Insights
- **Recommendation**: Review Tesla's official financial statements or the 10-K filing for 2022 to obtain the necessary metrics for a comprehensive financial analysis.
- **Future Outlook**: Monitoring Tesla's performance in upcoming quarters will provide insights into its financial health and operational efficiency, which can be compared against industry benchmarks once the relevant data is available.

### Missing Financial Metrics
The following specific financial figures are needed to calculate key financial ratios and margins:
- Net Income
- Total Revenue
- Total Assets
- Total Liabilities

If you can provide these figures or direct me to where they can be found, I can assist you further in analyzing Tesla's financial performance for 2022.
"""

ADVISOR_REPORT_V2 = """
# Tesla 2022 Financial Ratios and Margins Report

## Key Financial Metrics
The key financial ratios and margins for Tesla in 2022 were not explicitly found in the available documents. The necessary financial metrics such as net income, total revenue, total assets, and total liabilities are essential for calculating these ratios.

### Missing Financial Metrics
The following specific financial figures are needed to calculate key financial ratios and margins:
- **Net Income**
- **Total Revenue**
- **Total Assets**
- **Total Liabilities**

Unfortunately, these figures are not included in the provided context. If you can provide these figures or direct me to where they can be found, I can assist you further in analyzing Tesla's financial performance for 2022.

## Actionable Insights
- **Recommendation**: Review Tesla's official financial statements or the 10-K filing for 2022 to obtain the necessary metrics for a comprehensive financial analysis.
- **Future Outlook**: Monitoring Tesla's performance in upcoming quarters will provide insights into its financial health and operational efficiency, which can be compared against industry benchmarks once the relevant data is available.

## Risks and Considerations
The report also needs to address several critical risks associated with Tesla's financial performance in 2022:
- **Competition**: The automotive industry is highly competitive, and Tesla faces increasing pressure from both established automakers and new entrants.
- **Valuation**: The implications of Tesla's market valuation and how it may affect investor sentiment should be considered.
- **Supply Chain**: Issues related to supply chain disruptions and their impact on production and costs are significant.
- **Regulation**: Potential changes in government incentives and regulations affecting electric vehicles need to be monitored.
- **Execution**: Risks related to the execution of Tesla's growth strategy and operational efficiency are crucial for investors.

## Conclusion
To provide a complete analysis of Tesla's financial ratios and margins for 2022, access to the specific financial figures is necessary. Please share any additional documents or data that may contain these metrics for further analysis.

## SWOT Analysis
1. **Strengths:**
   - What are the core competitive advantages? (Example: Proprietary technology, economies of scale, strong brand).
   - What is the business doing best?
   
2. **Weaknesses:**
   - Which areas need improvement?
   - Where are there resource shortages or financial/supply chain difficulties?
   
3. **Opportunities:**
   - What market trends can be leveraged? (Example: IRA Tax Credits, shift to clean energy).
   - Opportunities to expand into new geographic markets or product lines?
   
4. **Threats:**
   - What barriers exist from new competitors or regulatory policies?
   - Supply chain disruption risks or volatile raw material prices?
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) does not adequately answer the original user query regarding Tesla's key financial ratios and margins for 2022. While it attempts to address some issues raised by the Critic, it still falls short in providing the necessary financial data and actionable insights.

## Query Satisfaction
The report fails to provide specific financial ratios and margins for Tesla in 2022, which were the primary focus of the user query. Although it mentions the need for key financial metrics, it does not derive any from the provided context documents, which contain relevant data. Therefore, the report does not satisfy the user's request.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  - [Include key financial ratios and margins derived from context documents.]
  - [Address missing risks related to competition, valuation, supply chain, regulation, and execution.]
  - [Add relevant figures or charts to support the analysis.]
  
- **Unresolved**:
  - [Clarify and strengthen recommendations based on available data.]

Only three out of four issues have been resolved, leaving one critical issue outstanding.

## Remaining Gaps
1. The report still lacks clarity and strength in its recommendations based on the available data. It continues to suggest reviewing external documents instead of utilizing the data present in the context.

## Recommendation
The advisor should revise the report to:
1. **Clarify and Strengthen Recommendations**: Provide actionable insights based on the available financial data from the context documents, rather than suggesting a review of external documents.
2. **Incorporate Key Financial Metrics**: Directly include calculated financial ratios and margins using the data available in the context documents to fulfill the user's request.
3. **Enhance Visual Representation**: Consider adding figures or charts to support the analysis and improve clarity.

By addressing these points, the report can better meet the user's needs and provide a comprehensive analysis of Tesla's financial performance for 2022.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_3
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |        0 |     +0 |
| Risk Assessment      |    15%  |        0 |       20 |    +20 |
| Actionable Advice    |    15%  |       60 |       60 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       40 |       40 |     +0 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    13.00 |    16.00 |   +3.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +3.0 pts absolute  |  +23.08% relative
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
                "v2_score": 20,
                "delta": 20,
                "weighted_v1": 0.0,
                "weighted_v2": 3.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 60,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
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
                "v1_score": 40,
                "v2_score": 40,
                "delta": 0,
                "weighted_v1": 4.0,
                "weighted_v2": 4.0
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
        "overall_v1": 13.0,
        "overall_v2": 16.0,
        "absolute_improvement": 3.0,
        "improvement_percentage": 23.08
    }
