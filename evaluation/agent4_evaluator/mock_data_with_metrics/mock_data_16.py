"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_16.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Financial Health Analysis

Based on the financial statements for Tesla as of December 31, 2022, the company exhibits a mixed financial health profile. Here are the key insights:

1. **Altman Z-Score**: Tesla's Altman Z-Score is **5.509**, placing it in the **Safe Zone (Low Bankruptcy Risk)**. This indicates that Tesla is not at immediate risk of bankruptcy, which is a positive sign for investors.

   - **Working Capital to Assets**: 17.36%
   - **Retained Earnings to Assets**: -7.60%
   - **EBIT to Assets**: -0.30%
   - **Market Capitalization to Liabilities**: 7.04
   - **Sales to Assets**: 119.26%

2. **Liabilities to Market Capitalization**: The ratio is **0.142**, suggesting that Tesla's liabilities are manageable relative to its market capitalization.

3. **Sales Growth**: Tesla reported sales of **$81.38 billion** in 2022, a **16.26% increase** from **$70 billion** in 2021. This growth indicates strong demand for Tesla's products.

4. **Retained Earnings**: Tesla's retained earnings decreased to **-$5.19 billion**, a decline of **29.70%** from the previous year. This suggests that Tesla is reinvesting heavily in growth, but it also indicates a need for improved profitability.

5. **EBIT**: The company reported an EBIT of **-$204 million**, a significant decline from **$1 billion** in 2021, reflecting challenges in operational efficiency or increased costs.

## Comparison of Key Financial Metrics

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| EBIT                 | -204.00    | 1,000.00   | -1,204.00    | -120.40%   |
| Retained Earnings     | -5,188.00  | -4,000.00  | -1,188.00    | +29.70%    |
| Sales                | 81,380.00  | 70,000.00  | +11,380.00   | +16.26%    |
| Total Assets         | 68,236.00  | 58,000.00  | +10,236.00   | +17.65%    |
| Total Liabilities    | 27,688.00  | 25,000.00  | +2,688.00    | +10.75%    |

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| EBIT                 | -204.00    | 1,000.00   | -1,204.00    | -120.40%   |
| Retained Earnings     | -5,188.00  | -4,000.00  | -1,188.00    | +29.70%    |
| Sales                | 81,380.00  | 70,000.00  | +11,380.00   | +16.26%    |
| Total Assets         | 68,236.00  | 58,000.00  | +10,236.00   | +17.65%    |
| Total Liabilities    | 27,688.00  | 25,000.00  | +2,688.00    | +10.75%    |

## Future Outlook

Tesla's future outlook appears cautiously optimistic, driven by strong sales growth and a solid market position. However, the company must address its declining EBIT and increasing retained losses to ensure sustainable growth. Key factors to consider include:

- **Operational Efficiency**: Improving operational efficiency to enhance profitability will be crucial. The significant drop in EBIT indicates that cost management needs to be prioritized.
  
- **Market Demand**: Continued demand for electric vehicles and energy products will support revenue growth. Tesla's expansion into new markets and product lines can further bolster sales.

- **Investment in Growth**: While reinvesting in growth is essential, Tesla must balance this with the need to improve its bottom line to restore positive retained earnings.

## Actionable Advice

1. **Focus on Cost Management**: Implement strategies to reduce operational costs and improve margins.
2. **Enhance Product Offerings**: Continue innovating and expanding product lines to capture a larger market share.
3. **Monitor Financial Ratios**: Keep a close eye on financial ratios to ensure that liabilities remain manageable relative to market capitalization.

## Conclusion

Tesla's financial health shows resilience with strong sales growth and a low bankruptcy risk. However, the company faces challenges in profitability that need to be addressed to secure its future growth trajectory.

---

### Sources
- Financial data sourced from Tesla's financial statements for the years ended December 31, 2022 and 2021.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Financial Health Analysis

Based on the financial statements for Tesla as of December 31, 2022, the company exhibits a mixed financial health profile. Here are the key insights:

1. **Altman Z-Score**: Tesla's Altman Z-Score is **7.504**, placing it in the **Safe Zone (Low Bankruptcy Risk)**. This indicates that Tesla is not at immediate risk of bankruptcy, which is a positive sign for investors.

   - **Working Capital to Assets**: 17.26%
   - **Retained Earnings to Assets**: -6.31%
   - **EBIT to Assets**: -0.25%
   - **Market Capitalization to Liabilities**: 10.68
   - **Sales to Assets**: 98.94%

2. **Liabilities to Market Capitalization**: The ratio is **0.0937**, suggesting that Tesla's liabilities are manageable relative to its market capitalization.

3. **Sales Growth**: Tesla reported sales of **$81.38 billion** in 2022, a **16.26% increase** from **$70 billion** in 2021. This growth indicates strong demand for Tesla's products.

4. **Retained Earnings**: Tesla's retained earnings decreased to **-$5.19 billion**, a decline of **29.95%** from the previous year. This suggests that Tesla is reinvesting heavily in growth, but it also indicates a need for improved profitability.

5. **EBIT**: The company reported an EBIT of **-$204 million**, a significant decline from **$1 billion** in 2021, reflecting challenges in operational efficiency or increased costs.

## Comparison of Key Financial Metrics

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| EBIT                 | -204.00    | 1,000.00   | -1,204.00    | -120.40%   |
| Retained Earnings     | -5,198.00  | -4,000.00  | -1,198.00    | +29.95%    |
| Sales                | 81,380.00  | 70,000.00  | +11,380.00   | +16.26%    |
| Total Assets         | 82,338.00  | 68,336.00  | +14,002.00   | +20.49%    |
| Total Liabilities    | 36,440.00  | 25,000.00  | +11,440.00   | +45.76%    |

## Future Outlook

Tesla's future outlook appears cautiously optimistic, driven by strong sales growth and a solid market position. However, the company must address its declining EBIT and increasing retained losses to ensure sustainable growth. Key factors to consider include:

- **Operational Efficiency**: Improving operational efficiency to enhance profitability will be crucial. The significant drop in EBIT indicates that cost management needs to be prioritized.
  
- **Market Demand**: Continued demand for electric vehicles and energy products will support revenue growth. Tesla's expansion into new markets and product lines can further bolster sales.

- **Investment in Growth**: While reinvesting in growth is essential, Tesla must balance this with the need to improve its bottom line to restore positive retained earnings.

## Actionable Advice

1. **Focus on Cost Management**: Implement strategies to reduce operational costs and improve margins.
2. **Enhance Product Offerings**: Continue innovating and expanding product lines to capture a larger market share.
3. **Monitor Financial Ratios**: Keep a close eye on financial ratios to ensure that liabilities remain manageable relative to market capitalization.

## Conclusion

Tesla's financial health shows resilience with strong sales growth and a low bankruptcy risk. However, the company faces challenges in profitability that need to be addressed to secure its future growth trajectory.

---

### Sources
- Financial data sourced from Tesla's financial statements for the years ended December 31, 2022, and 2021.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Tesla's financial health and future outlook, but it fails to fully address all issues identified by the Critic. While some improvements have been made, significant gaps remain.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, provides an analysis of sales growth, and offers actionable advice. However, it does not fully address the risks associated with Tesla's operations, which were implied in the user query.

## Issues Resolution Status
Out of the five issues identified by the Critic, only two have been resolved in the revised report:
1. **Resolved**: Include context for the Altman Z-Score and sales growth figures.
2. **Resolved**: Add visual aids to enhance understanding of financial metrics.

The following issues remain unresolved:
1. **Unresolved**: Clarify EBIT reporting and ensure consistency in figures.
2. **Unresolved**: Correct retained earnings analysis and provide context for percentage changes.
3. **Unresolved**: Address missing risks related to supply chain, regulation, and execution.

## Remaining Gaps
1. The EBIT reporting remains inconsistent, as the report states an EBIT of **-$204 million** but does not clarify the context or implications of this figure.
2. The retained earnings analysis lacks clarity and does not provide a proper context for the percentage change reported.
3. The report fails to address significant risks related to supply chain dependencies, regulatory changes, and execution challenges that could impact Tesla's future performance.

## Recommendation
It is recommended that the advisor revises the report to:
1. Clarify and ensure consistency in the EBIT reporting.
2. Correct the retained earnings analysis and provide a clear context for the percentage changes.
3. Include a thorough discussion of the risks associated with supply chain, regulatory changes, and execution challenges.
4. Consider adding more visual aids to enhance the clarity and impact of the financial metrics presented. 

Addressing these gaps will strengthen the report and make it more decision-grade for users.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_16.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       85 |       80 |     -5 |
| Business Analysis    |    15%  |       70 |       70 |     +0 |
| Risk Assessment      |    15%  |       75 |       75 |     +0 |
| Actionable Advice    |    15%  |       80 |       80 |     +0 |
| Evidence Usage       |    10%  |       90 |       90 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |       90 |       90 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    83.00 |    81.75 |  -1.25 |
+----------------------+--------+----------+----------+--------+
  Improvement: -1.25 pts absolute  |  -1.51% relative
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
                "v2_score": 80,
                "delta": -5,
                "weighted_v1": 21.25,
                "weighted_v2": 20.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 70,
                "delta": 0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 75,
                "v2_score": 75,
                "delta": 0,
                "weighted_v1": 11.25,
                "weighted_v2": 11.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 80,
                "v2_score": 80,
                "delta": 0,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 100,
                "v2_score": 100,
                "delta": 0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v1": 83.0,
        "overall_v2": 81.75,
        "absolute_improvement": -1.25,
        "improvement_percentage": -1.51
    }
