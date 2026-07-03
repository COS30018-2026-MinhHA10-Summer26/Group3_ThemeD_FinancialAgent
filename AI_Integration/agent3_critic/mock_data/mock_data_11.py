"""
Mock inputs for testing the Critic Agent.

Auto-generated from advisor run: mock_data_11.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT = """
# Tesla, Inc. Financial Health and Future Outlook

## Overview
Based on the consolidated financial statements for Tesla, Inc. for the year ended December 31, 2022, the company has shown significant growth in key financial metrics compared to the previous year. However, there are also indications of high bankruptcy risk as assessed by the Altman Z-Score.

## Key Financial Metrics Comparison

### Financial Performance
The following table summarizes the key financial metrics for Tesla in 2022 compared to 2021:

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| Equity                | 44,704.00  | 30,189.00  | +14,515.00   | +48.08%    |
| Net Income            | 12,556.00  | 5,519.00   | +7,037.00    | +127.50%   |
| Revenues             | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |
| Total Assets         | 82,338.00  | 62,131.00  | +20,207.00   | +32.52%    |
| Total Liabilities    | 36,440.00  | 30,548.00  | +5,892.00    | +19.29%    |

### Chart of Key Financial Metrics
![Key Financial Metrics Comparison: Tesla 2022 vs 2021](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_198cdedc8d79_key-financial-metrics-comparison-tesla-2022-vs-2021.png)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*  
*Source: Data sourced from Tesla's consolidated financial statements.*

## Risk Assessment
The Altman Z-Score for Tesla is **1.755**, placing it in the **Distress Zone (High Bankruptcy Risk)**. The components of the Z-Score are as follows:

- **Working Capital to Assets**: 0.0002
- **Retained Earnings to Assets**: 0.1565
- **EBIT to Assets**: 0.1659
- **Equity Market Value to Liabilities**: 0.0 (not applicable)
- **Sales to Assets**: 0.9894

### Explanation of the Altman Z-Score Calculation
The Altman Z-Score is a formula used to predict the likelihood of bankruptcy for a company. It combines five financial ratios, weighted by coefficients derived from a study of publicly traded manufacturing firms. The Z-Score is calculated as follows:

\[ Z = 1.2 \times \text{(Working Capital / Total Assets)} + 1.4 \times \text{(Retained Earnings / Total Assets)} + 1.2 \times \text{(EBIT / Total Assets)} + 0.6 \times \text{(Market Value of Equity / Total Liabilities)} + 0.999 \times \text{(Sales / Total Assets)} \]

A Z-Score below 1.8 indicates a high risk of bankruptcy, while a score above 3 suggests a low risk.

### Interpretation
- **Distress Zone**: This indicates that Tesla is at a high risk of bankruptcy. While the company has shown strong revenue growth and improved profitability, the increasing liabilities relative to assets could pose a significant risk if not managed properly.

## Limitations of the Analysis
While the Altman Z-Score provides valuable insights into Tesla's financial health, it has limitations:
- **Industry Specificity**: The Z-Score was developed based on manufacturing firms and may not fully capture the unique aspects of Tesla's business model, which includes technology and energy sectors.
- **Market Conditions**: The score does not account for external market conditions that could impact Tesla's performance, such as economic downturns or changes in consumer preferences.
- **Non-Financial Factors**: Factors such as management quality, brand strength, and competitive landscape are not considered in the Z-Score but can significantly influence a company's long-term viability.

## Future Outlook
1. **Growth Potential**: Tesla's significant increase in revenues and net income suggests strong demand for its products, particularly in the automotive sector. The company should continue to capitalize on this momentum by expanding its product offerings and market reach.

2. **Cost Management**: With rising liabilities, Tesla must focus on managing its costs effectively to maintain profitability. This includes optimizing production processes and controlling operational expenses.

3. **Investment in Innovation**: Continued investment in research and development will be crucial for Tesla to stay competitive in the rapidly evolving automotive and energy sectors.

4. **Monitoring Financial Health**: Regular monitoring of financial metrics and risk assessments will be essential for Tesla to navigate potential challenges and sustain its growth trajectory.

## Conclusion
Tesla's financial health appears robust with significant growth in key metrics; however, the high bankruptcy risk indicated by the Altman Z-Score necessitates careful financial management and strategic planning to ensure long-term sustainability and success.
"""
