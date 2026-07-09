"""
Mock inputs for testing the Advisor Agent revision process.

Auto-generated from advisor revision run: mock_data_18.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

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
