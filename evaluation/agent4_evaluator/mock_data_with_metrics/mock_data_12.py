"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_12.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Financial Health Analysis

Based on the consolidated financial statements for Tesla, Inc. for the year ended December 31, 2022, the following key observations can be made regarding the company's financial health:

1. **Revenue Growth**: Tesla's total revenues increased significantly from $53.8 billion in 2021 to $81.5 billion in 2022, representing a growth of approximately 51.35%. This growth is primarily driven by increased automotive sales, which rose from $44.1 billion to $67.2 billion.

2. **Net Income Surge**: The net income for Tesla also saw a remarkable increase from $5.5 billion in 2021 to $12.6 billion in 2022, marking a 127.50% increase. This indicates improved profitability and operational efficiency.

3. **Gross Profit Improvement**: The gross profit increased from $13.6 billion in 2021 to $20.9 billion in 2022, reflecting a gross margin improvement as Tesla continues to scale its operations.

4. **Operating Expenses**: Operating expenses remained relatively stable, increasing slightly from $7.1 billion in 2021 to $7.2 billion in 2022. This indicates that Tesla is managing its costs effectively while expanding its revenue base.

5. **Cash Flow from Operations**: Tesla generated $14.7 billion in cash from operating activities in 2022, up from $11.5 billion in 2021, which is a positive indicator of cash generation capability.

### Risk Assessment

The Altman Z-Score, which is typically used to assess the likelihood of bankruptcy, could not be computed due to insufficient data. However, the significant increase in net income and cash flow from operations suggests that Tesla is in a strong position financially.

## Key Financial Metrics Comparison

The following table summarizes the key financial metrics for Tesla in 2022 compared to 2021:

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| Gross Profit          | 20,853.00  | 13,606.00  | +7,247.00    | +53.26%    |
| Net Income            | 12,556.00  | 5,519.00   | +7,037.00    | +127.50%   |
| Operating Expenses     | 7,197.00   | 7,083.00   | +114.00      | +1.61%     |
| Revenues             | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |

![Key Financial Metrics Comparison: Tesla 2022 vs 2021](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_f3454e3333b8.png)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*

*Source: Data sourced from Tesla's consolidated financial statements.*

## Future Outlook

Given the strong financial performance in 2022, Tesla appears well-positioned for future growth. The following factors may influence its outlook:

- **Market Demand**: Continued demand for electric vehicles (EVs) and energy solutions is expected to drive revenue growth.
- **Operational Efficiency**: Tesla's ability to manage costs while scaling operations will be crucial in maintaining profitability.
- **Innovation and Expansion**: Ongoing investments in technology and expansion into new markets could further enhance revenue streams.

### Recommendations

1. **Focus on Cost Management**: Continue to monitor and manage operating expenses to ensure profitability as revenues grow.
2. **Invest in R&D**: Allocate resources towards research and development to maintain a competitive edge in technology and innovation.
3. **Expand Market Presence**: Explore opportunities for expansion into new geographic markets and product lines to diversify revenue streams.

In conclusion, Tesla's financial health appears robust, with significant growth in revenues and net income, alongside effective cost management. The company is likely to continue its upward trajectory if it maintains its operational efficiencies and capitalizes on market opportunities.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Financial Health Analysis

Based on the consolidated financial statements for Tesla, Inc. for the year ended December 31, 2022, the following key observations can be made regarding the company's financial health:

1. **Revenue Growth**: Tesla's total revenues increased significantly from $53.8 billion in 2021 to $81.5 billion in 2022, representing a growth of approximately 51.35%. This growth is primarily driven by increased automotive sales, which rose from $44.1 billion to $67.2 billion.

2. **Net Income Surge**: The net income for Tesla also saw a remarkable increase from $5.5 billion in 2021 to $12.6 billion in 2022, marking a 127.50% increase. This indicates improved profitability and operational efficiency.

3. **Gross Profit Improvement**: The gross profit increased from $13.6 billion in 2021 to $20.9 billion in 2022, reflecting a gross margin improvement as Tesla continues to scale its operations.

4. **Operating Expenses**: Operating expenses remained relatively stable, increasing slightly from $7.1 billion in 2021 to $7.2 billion in 2022. This indicates that Tesla is managing its costs effectively while expanding its revenue base.

5. **Cash Flow from Operations**: Tesla generated $14.7 billion in cash from operating activities in 2022, up from $11.5 billion in 2021, which is a positive indicator of cash generation capability.

### Risk Assessment

The Altman Z-Score, which is typically used to assess the likelihood of bankruptcy, has been calculated as follows:

- **Altman Z-Score**: 8.367 (Safe Zone - Low Bankruptcy Risk)
- **Debt to Equity Ratio**: 0.1252
- **Interest Coverage Ratio**: 71.5

These figures indicate that Tesla is in a strong financial position with low bankruptcy risk, manageable debt levels, and excellent ability to cover interest expenses.

## Key Financial Metrics Comparison

The following table summarizes the key financial metrics for Tesla in 2022 compared to 2021:

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| Gross Profit          | 20,853.00  | 13,606.00  | +7,247.00    | +53.26%    |
| Net Income            | 12,556.00  | 5,519.00   | +7,037.00    | +127.50%   |
| Operating Expenses     | 7,197.00   | 7,083.00   | +114.00      | +1.61%     |
| Revenues             | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |

![Key Financial Metrics Comparison: Tesla 2022 vs 2021](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_f3454e3333b8.png)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*

*Source: Data sourced from Tesla's consolidated financial statements.*

## Future Outlook

Given the strong financial performance in 2022, Tesla appears well-positioned for future growth. The following factors may influence its outlook:

- **Market Demand**: Continued demand for electric vehicles (EVs) and energy solutions is expected to drive revenue growth. The global shift towards sustainable energy and electric mobility supports this trend.
- **Operational Efficiency**: Tesla's ability to manage costs while scaling operations will be crucial in maintaining profitability. The company has demonstrated effective cost management, which will be vital as production increases.
- **Innovation and Expansion**: Ongoing investments in technology and expansion into new markets could further enhance revenue streams. Tesla's commitment to R&D and new product development, such as the Optimus robot, positions it well for future opportunities.

### Recommendations

1. **Focus on Cost Management**: Continue to monitor and manage operating expenses to ensure profitability as revenues grow.
2. **Invest in R&D**: Allocate resources towards research and development to maintain a competitive edge in technology and innovation.
3. **Expand Market Presence**: Explore opportunities for expansion into new geographic markets and product lines to diversify revenue streams.

In conclusion, Tesla's financial health appears robust, with significant growth in revenues and net income, alongside effective cost management. The company is likely to continue its upward trajectory if it maintains its operational efficiencies and capitalizes on market opportunities. However, it should remain vigilant regarding competitive pressures, supply chain risks, and regulatory changes that could impact its operations.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's financial health and future outlook compared to the original version. However, it still contains an unresolved issue regarding the consistency of revenue figures.

## Query Satisfaction
The revised report adequately addresses the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, provides a risk assessment, and includes actionable recommendations. All expected topics from the user query are present in the response.

## Issues Resolution Status
Out of the four issues identified by the Critic, three have been resolved in the revised report:
1. A comprehensive risk assessment has been included.
2. Clear references for net income and cash flow figures have been provided.
3. Claims about continued demand for electric vehicles have been substantiated with market data.

However, one issue remains unresolved:
- **Clarify and ensure consistency in revenue figures throughout the report.** The report states total revenues increased to $81.5 billion in 2022, but the table shows $81,462 million, which could confuse readers.

## Remaining Gaps
- The revenue figures presented in the text and the table are inconsistent. The report should clarify this discrepancy to maintain credibility and avoid confusion.

## Recommendation
The advisor should revise the report to ensure consistency in the revenue figures presented. This is crucial for maintaining the report's credibility and ensuring that readers can trust the information provided. Once this issue is addressed, the report will be complete and ready for final approval.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_12.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       85 |       95 |    +10 |
| Business Analysis    |    15%  |       70 |       80 |    +10 |
| Risk Assessment      |    15%  |       50 |       80 |    +30 |
| Actionable Advice    |    15%  |       70 |       80 |    +10 |
| Evidence Usage       |    10%  |       70 |       80 |    +10 |
| Completeness         |    10%  |       80 |       90 |    +10 |
| Query Satisfaction   |    10%  |       75 |       85 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    72.25 |    85.25 |  +13.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +13.0 pts absolute  |  +17.99% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 85,
                "v2_score": 95,
                "delta": 10,
                "weighted_v1": 21.25,
                "weighted_v2": 23.75
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 80,
                "delta": 30,
                "weighted_v1": 7.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 90,
                "delta": 10,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 75,
                "v2_score": 85,
                "delta": 10,
                "weighted_v1": 7.5,
                "weighted_v2": 8.5
            }
        },
        "overall_v1": 72.25,
        "overall_v2": 85.25,
        "absolute_improvement": 13.0,
        "improvement_percentage": 17.99
    }
