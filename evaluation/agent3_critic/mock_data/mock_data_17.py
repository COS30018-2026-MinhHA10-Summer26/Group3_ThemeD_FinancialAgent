"""
Mock inputs for testing the Critic Agent.

Auto-generated from advisor run: mock_data_17.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT = """
# Tesla Financial Health and Future Outlook

## Overview

Tesla's financial health as of December 31, 2022, shows significant improvement compared to the previous year. Key metrics indicate a strong liquidity position, reduced debt levels, and increased profitability. Below is a detailed analysis of Tesla's financial metrics, risk assessment, and future outlook.

## Key Financial Metrics Comparison

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Cash and Cash Equivalents  | 22,209     | 17,708     | +4,501       | +25.42%     |
| Inventory                  | 12,839     | 5,757      | +7,082       | +123.02%    |
| Net Income                 | 1,211      | 557        | +654         | +117.41%    |
| Total Assets               | 33,589     | 30,700     | +2,889       | +9.41%      |
| Total Debt                 | 2,061      | 5,380      | -3,319       | -61.69%     |
| Total Liabilities           | 20,661     | 19,300     | +1,361       | +7.05%      |

*Source: Data sourced from Tesla's financial statements.*

## Financial Health Analysis

### Liquidity and Cash Position
Tesla's cash and cash equivalents increased by 25.42% to $22.21 billion, indicating a strong liquidity position that can support operational needs and future investments.

### Inventory Management
The inventory has significantly increased by 123.02%, which may reflect higher production levels or potential challenges in sales. This warrants monitoring to ensure that inventory levels do not lead to excess stock or obsolescence.

### Profitability
Net income rose by 117.41% to $1.21 billion, showcasing improved operational efficiency and profitability. This positive trend is crucial for sustaining growth and investor confidence.

### Debt Reduction
Total debt decreased by 61.69% to $2.06 billion, which enhances Tesla's financial stability and reduces interest obligations. The liabilities to market capitalization ratio stands at 0.2583, indicating a manageable debt level relative to the company's market value.

## Risk Assessment

Using the Altman Z-Score, Tesla's score is 5.425, placing it in the "Safe Zone" with low bankruptcy risk. The components of the score are as follows:

- **Working Capital to Assets**: 0.448
- **Retained Earnings to Assets**: -0.0298
- **EBIT to Assets**: 0.0595
- **Equity Market Value to Liabilities**: 3.872
- **Sales to Assets**: 2.4115

These metrics indicate that Tesla is well-positioned to manage its financial obligations and sustain operations.

## Future Outlook

Tesla's strong cash position, reduced debt, and increasing profitability suggest a positive outlook for the company. However, the significant rise in inventory should be addressed to ensure it does not hinder cash flow or operational efficiency. Continued focus on production efficiency and market demand will be essential for maintaining growth.

### Actionable Advice
1. **Monitor Inventory Levels**: Implement strategies to manage inventory effectively to avoid excess stock.
2. **Leverage Cash Reserves**: Utilize cash reserves for strategic investments in technology and expansion to drive future growth.
3. **Debt Management**: Continue to focus on reducing debt levels to enhance financial flexibility.

## Conclusion

Tesla's financial health is robust, with strong liquidity, reduced debt, and improved profitability. By addressing inventory management and leveraging its cash reserves, Tesla can continue to thrive in the competitive automotive and energy markets.

![Comparison of Key Financial Metrics (2022 vs 2021)](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_fa39cbc2d176_comparison-of-key-financial-metrics-2022-vs-2021.png)

*Figure: Bar chart comparing key financial metrics for Tesla in 2022 and 2021.*

*Source: Data sourced from Tesla's financial statements.*
"""
