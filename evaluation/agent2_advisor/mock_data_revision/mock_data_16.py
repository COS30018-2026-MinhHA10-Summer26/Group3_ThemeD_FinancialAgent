"""
Mock inputs for testing the Advisor Agent revision process.

Auto-generated from advisor revision run: mock_data_16.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

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
