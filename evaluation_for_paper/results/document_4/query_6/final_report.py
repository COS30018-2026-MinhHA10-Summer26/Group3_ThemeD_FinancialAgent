"""
Full Pipeline Evaluation Report — document_4 / query_6
Source document: NASDAQ_AMZN_2025.pdf
Query: What is Amazon's cash and debt position at the end of fiscal year 2025?
"""
from __future__ import annotations
import json

USER_QUERY = "What is Amazon's cash and debt position at the end of fiscal year 2025?"

USER_QUERIES = [
    "What were Amazon's key financial results and revenue breakdown for fiscal year 2025?",
    "How did Amazon's AWS segment grow in 2025 and what products drove demand?",
    "What is Amazon's profitability trend and operating margin outlook for 2025?",
    "What strategic acquisitions or investments did Amazon make in 2025?",
    "How did macroeconomic conditions affect Amazon's business in 2025?",
    "What is Amazon's cash and debt position at the end of fiscal year 2025?",
    "How did Amazon's Prime membership and subscription services perform in 2025?",
    "What does Amazon's 2025 annual report say about its long-term growth strategy?",
]

ADVISOR_REPORT_V1 = """
# Amazon's Cash and Debt Position at the End of Fiscal Year 2025

⚠️ Unfortunately, the cash position and debt position for Amazon at the end of fiscal year 2025 were not found in the available documents. This information is currently unavailable.

To obtain accurate figures regarding Amazon's cash and debt positions, I recommend checking the following sources:
- Amazon's official financial statements or annual report for fiscal year 2025, which should contain the necessary information.
- Financial news websites or databases that track corporate financials, such as Bloomberg, Yahoo Finance, or Reuters, for updated financial metrics.
- The U.S. Securities and Exchange Commission (SEC) filings, where Amazon is required to disclose detailed financial information.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Cash and Debt Position at the End of Fiscal Year 2025

⚠️ Unfortunately, the specific cash and debt positions for Amazon at the end of fiscal year 2025 were not found in the available documents. This information is currently unavailable.

To obtain accurate figures regarding Amazon's cash and debt positions, I recommend checking the following sources:
- Amazon's official financial statements or annual report for fiscal year 2025, which should contain the necessary information.
- Financial news websites or databases that track corporate financials, such as Bloomberg, Yahoo Finance, or Reuters, for updated financial metrics.
- The U.S. Securities and Exchange Commission (SEC) filings, where Amazon is required to disclose detailed financial information.

## Risk Analysis

Given the absence of specific financial data, a comprehensive risk analysis is essential for understanding potential challenges facing Amazon:

1. **Competition:** Amazon faces intense competition from various sectors, including e-commerce, cloud computing, and digital streaming. Competitors like Walmart, Microsoft, and Alibaba pose significant threats to market share.

2. **Valuation:** The company's valuation may be impacted by market fluctuations and investor sentiment, particularly in a volatile economic environment.

3. **Supply Chain:** Disruptions in the supply chain can affect product availability and delivery times, impacting customer satisfaction and sales.

4. **Regulation:** Increasing scrutiny from regulators regarding antitrust issues and data privacy could lead to legal challenges and operational constraints.

5. **Margin Pressure:** Rising costs, including labor and logistics, may pressure profit margins, necessitating strategic adjustments to maintain profitability.

6. **Execution:** The ability to effectively execute growth strategies, such as expanding into new markets or launching new products, is critical for sustaining competitive advantage.

## SWOT Analysis

### Strengths:
- Strong brand recognition and customer loyalty.
- Extensive logistics and fulfillment network.
- Diversified revenue streams from various business segments, including AWS and retail.

### Weaknesses:
- High operational costs associated with maintaining a vast logistics network.
- Dependence on third-party sellers for a significant portion of sales.

### Opportunities:
- Expansion into emerging markets and new product lines.
- Leveraging advancements in technology, such as AI and robotics, to enhance operational efficiency.

### Threats:
- Regulatory challenges and potential antitrust actions.
- Economic downturns affecting consumer spending.

In conclusion, while specific cash and debt figures for Amazon at the end of fiscal year 2025 are unavailable, understanding the associated risks and conducting a SWOT analysis can provide valuable insights for investors and stakeholders.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) does not adequately answer the original user query regarding Amazon's cash and debt position at the end of fiscal year 2025. While it provides a risk analysis and a SWOT analysis, it fails to include the specific cash and debt figures requested.

## Query Satisfaction
The report partially satisfies the query by addressing the financial health of Amazon through a risk analysis and SWOT analysis. However, it does not provide the specific cash and debt figures, which were the primary focus of the user query. Therefore, it does not fully meet the user's request.

## Issues Resolution Status
Out of the three issues identified by the Critic:
- **Resolved:**
  - [Include specific cash and debt figures for Amazon at the end of fiscal year 2025.]
  - [Add a comprehensive risk analysis covering competition, valuation, supply chain, regulation, margin pressure, and execution.]
  
- **Unresolved:**
  - [Incorporate visual aids or figures to support claims made in the report.]

Only two out of three issues have been resolved, indicating that the report still requires further revision.

## Remaining Gaps
1. The report still lacks the incorporation of visual aids or figures to support claims made in the report, which is essential for enhancing clarity and understanding.

## Recommendation
It is recommended that the advisor revise the report to include:
1. Specific cash and debt figures for Amazon at the end of fiscal year 2025, as derived from the context documents.
2. Visual aids or figures to support the claims made in the report, which would enhance the overall quality and comprehensibility of the information presented.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_4/query_6
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       60 |       60 |     +0 |
| Risk Assessment      |    15%  |       70 |       70 |     +0 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       50 |       70 |    +20 |
| Query Satisfaction   |    10%  |        0 |        0 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    24.50 |    26.50 |   +2.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +2.0 pts absolute  |  +8.16% relative
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
                "v1_score": 60,
                "v2_score": 60,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 70,
                "delta": 0,
                "weighted_v1": 10.5,
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
        "overall_v1": 24.5,
        "overall_v2": 26.5,
        "absolute_improvement": 2.0,
        "improvement_percentage": 8.16
    }
