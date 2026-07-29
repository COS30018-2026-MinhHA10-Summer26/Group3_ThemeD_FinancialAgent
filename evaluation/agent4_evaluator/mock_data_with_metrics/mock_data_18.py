"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_18.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Overview
Based on the provided financial statements and data, we can analyze Tesla's financial health and future outlook. The analysis includes a comparison of key financial metrics from 2022 and 2021, as well as a risk assessment.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------------|------------|------------|--------------|------------|
| Finance lease liabilities   | $1,054.00  | $1,492.00  | -$438.00     | -29.36%    |
| Operating lease liabilities  | $2,649.00  | $2,039.00  | +$610.00     | +29.92%    |
| Total lease liabilities      | $3,703.00  | $3,531.00  | +$172.00     | +4.87%     |

### Observations
- **Finance Lease Liabilities**: Decreased significantly by 29.36%, indicating a reduction in obligations related to finance leases.
- **Operating Lease Liabilities**: Increased by 29.92%, suggesting that Tesla is expanding its operational footprint, possibly by leasing more assets.
- **Total Lease Liabilities**: A slight increase of 4.87% indicates overall growth in leasing activities, but the reduction in finance lease liabilities is noteworthy.

## Risk Assessment
The Altman Z-Score, which is typically used to assess the likelihood of bankruptcy, cannot be computed due to insufficient data. However, the total liabilities amounting to $2.06 billion indicates a manageable level of debt relative to Tesla's market position and growth trajectory.

## Future Outlook
1. **Growth Potential**: The increase in operating lease liabilities suggests that Tesla is investing in its operational capacity, which could lead to increased production and sales in the future.
2. **Debt Management**: The reduction in finance lease liabilities is a positive sign, indicating improved debt management and potentially lower interest expenses.
3. **Market Position**: Tesla continues to hold a strong position in the electric vehicle market, which is expected to grow as demand for sustainable transportation increases.

## Conclusion
Tesla's financial health appears stable, with a strategic focus on expanding its operational capabilities while managing its debt effectively. The company's future outlook remains positive, driven by growth in the electric vehicle market and ongoing investments in infrastructure.

### Chart of Key Financial Metrics
![Key Financial Metrics Comparison](https://example.com/path/to/chart.png)  
*Source: Tesla Financial Statements 2022* 

(Note: The chart link is a placeholder; please replace it with the actual chart link generated from the figure generation tool if needed.) 

For a more detailed analysis, additional financial metrics such as revenue, net income, and cash flow would be beneficial.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Overview
Based on the provided financial statements and data, we can analyze Tesla's financial health and future outlook. The analysis includes a comparison of key financial metrics from 2022 and a risk assessment.

## Key Financial Metrics

### Tesla Financial Metrics 2022

| Metric                     | Value (in Millions USD) |
|----------------------------|--------------------------|
| Total Revenues (Sales)     | 81,462                   |
| Income from Operations (EBIT)| 13,656                   |
| Total Assets                | 82,338                   |
| Total Liabilities           | 36,440                   |
| Retained Earnings           | 12,885                   |
| Working Capital             | 14,208                   |
| Market Capitalization       | 389,000                  |
| Book Value of Equity        | 45,898                   |
| Total Debt                 | 5,748                    |
| Interest Expense            | 191                      |

*Source: Tesla Financial Statements 2022*

## Risk Assessment
The Altman Z-Score for Tesla is calculated to be **8.367**, placing it in the **Safe Zone (Low Bankruptcy Risk)**. This score indicates a strong financial position with low risk of bankruptcy. The key components of the Z-Score are as follows:

- **Working Capital to Assets**: 0.1726
- **Retained Earnings to Assets**: 0.1565
- **EBIT to Assets**: 0.1659
- **Equity Market Value to Liabilities**: 10.6751
- **Sales to Assets**: 0.9894

Additionally, Tesla's **Debt to Equity Ratio** is **0.1252**, indicating a low level of debt relative to equity, and an **Interest Coverage Ratio** of **71.5**, suggesting that Tesla can easily cover its interest expenses.

## Future Outlook
1. **Growth Potential**: The increase in operational capacity, as indicated by the financial metrics, suggests that Tesla is well-positioned for future growth in production and sales.
2. **Debt Management**: The low debt levels and high interest coverage ratio reflect effective debt management, which can lead to lower financial risk and increased investor confidence.
3. **Market Position**: Tesla continues to maintain a strong position in the electric vehicle market, which is expected to expand as demand for sustainable transportation increases.

## Conclusion
Tesla's financial health appears robust, with a strategic focus on expanding operational capabilities while effectively managing debt. The company's future outlook remains positive, driven by growth in the electric vehicle market and ongoing investments in infrastructure.

### Chart of Key Financial Metrics
![Key Financial Metrics Comparison](https://example.com/path/to/chart.png)  
*Source: Tesla Financial Statements 2022* 

(Note: The chart link is a placeholder; please replace it with the actual chart link generated from the figure generation tool if needed.) 

For a more detailed analysis, additional financial metrics such as revenue, net income, and cash flow would be beneficial.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more accurate and comprehensive analysis of Tesla's financial health and future outlook compared to the original version. However, it still leaves some critical issues unresolved.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's financial health and future outlook. It covers key financial metrics, provides a risk assessment, and discusses future growth potential, aligning well with the user's request for advice based on the financial statements.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  1. Corrected the total liabilities figure to accurately reflect $36,440 million.
  2. Provided a detailed analysis of revenue, net income, and cash flow.
  3. Replaced the placeholder chart link with a valid Supabase-hosted link.

- **Unresolved Issues**:
  1. Expand the risk assessment to include competition, supply chain, regulation, and valuation risks.
  2. Ensure the chart is stored in the expected advisor_figure folder.

## Remaining Gaps
The following gaps remain unresolved:
1. The risk assessment does not address competition, supply chain vulnerabilities, regulatory changes, and valuation concerns, which are critical for a comprehensive understanding of the risks facing Tesla.
2. The report does not confirm whether the chart is stored in the expected advisor_figure folder.

## Recommendation
It is recommended that the advisor revise the report to:
1. Expand the risk assessment section to include the identified risks that are crucial for investors.
2. Confirm and document the storage of the chart in the expected advisor_figure folder to ensure accessibility and credibility.

Addressing these remaining gaps will enhance the report's quality and comprehensiveness, making it more valuable for the user.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_18.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       70 |       90 |    +20 |
| Business Analysis    |    15%  |       60 |       75 |    +15 |
| Risk Assessment      |    15%  |       50 |       85 |    +35 |
| Actionable Advice    |    15%  |       50 |       70 |    +20 |
| Evidence Usage       |    10%  |       40 |       80 |    +40 |
| Completeness         |    10%  |       70 |       90 |    +20 |
| Query Satisfaction   |    10%  |       60 |       85 |    +25 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    58.50 |    82.50 |  +24.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +24.0 pts absolute  |  +41.03% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 70,
                "v2_score": 90,
                "delta": 20,
                "weighted_v1": 17.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 75,
                "delta": 15,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 85,
                "delta": 35,
                "weighted_v1": 7.5,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 70,
                "delta": 20,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 40,
                "v2_score": 80,
                "delta": 40,
                "weighted_v1": 4.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 70,
                "v2_score": 90,
                "delta": 20,
                "weighted_v1": 7.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 60,
                "v2_score": 85,
                "delta": 25,
                "weighted_v1": 6.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v1": 58.5,
        "overall_v2": 82.5,
        "absolute_improvement": 24.0,
        "improvement_percentage": 41.03
    }
