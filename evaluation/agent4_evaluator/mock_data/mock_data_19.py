"""
Mock inputs for testing the Evaluator Agent.

Auto-generated from evaluator run: mock_data_19.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla's Financial Health and Future Outlook

## Overview
Based on the financial statements provided, Tesla has demonstrated significant growth in its financial performance from 2021 to 2022. The key metrics indicate a robust increase in income and profitability, which is a positive sign for the company's financial health.

### Key Financial Metrics Comparison
The following table summarizes the comparison of key financial metrics between Tesla for the years 2022 and 2021:

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Income Before Taxes        | 13,719.00  | 6,343.00   | +7,376.00    | +116.29%    |
| Net Income                  | 12,587.00  | 5,644.00   | +6,943.00    | +123.02%    |
| Provision for Income Taxes  | 1,132.00   | 699.00     | +433.00      | +61.95%     |

### Analysis
1. **Income Growth**: Tesla's income before taxes increased by 116.29%, indicating a strong operational performance and effective cost management. The net income also saw a substantial rise of 123.02%, reflecting improved profitability.

2. **Tax Provision**: The provision for income taxes increased by 61.95%, which is consistent with the growth in income. This suggests that Tesla is effectively managing its tax liabilities as its profitability grows.

3. **Future Outlook**: Given the substantial growth in income and net income, Tesla appears to be on a positive trajectory. The Altman Z-Score analysis indicates that Tesla is in a favorable position with a low risk of bankruptcy, which further supports a positive outlook.

### Risk Assessment
The Altman Z-Score analysis provides insights into Tesla's financial stability, indicating effective management of assets and a strong equity position relative to its liabilities.

### Additional Considerations
- **Investment in Growth**: Tesla's ongoing investments in production capacity, such as the Gigafactories, and its focus on innovation in electric vehicles and renewable energy solutions are likely to support continued revenue growth.
- **Market Conditions**: The automotive and energy markets are subject to fluctuations. Tesla's ability to maintain its growth trajectory will depend on market demand, competition, and regulatory environments.
- **Debt Management**: Monitoring Tesla's debt levels and interest coverage will be crucial in assessing its long-term financial stability.

### Conclusion
Tesla's financial health appears strong based on the significant growth in income and net income from 2021 to 2022. The analysis indicates a low risk of financial distress, supporting a positive outlook. Continued focus on operational efficiency, market expansion, and innovation will be key to sustaining this growth.

### Visual Representation
For a visual representation of the financial metrics, please refer to the comparison table below:

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Income Before Taxes        | 13,719.00  | 6,343.00   | +7,376.00    | +116.29%    |
| Net Income                  | 12,587.00  | 5,644.00   | +6,943.00    | +123.02%    |
| Provision for Income Taxes  | 1,132.00   | 699.00     | +433.00      | +61.95%     |

*Source: NASDAQ_TSLA_2022.pdf.*


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla's Financial Health and Future Outlook

## Overview
Based on the financial statements provided, Tesla has demonstrated significant growth in its financial performance from 2021 to 2022. The key metrics indicate a robust increase in income and profitability, which is a positive sign for the company's financial health.

### Key Financial Metrics Comparison
The following table summarizes the comparison of key financial metrics between Tesla for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Income Before Taxes        | 13,719.00  | 6,343.00   | +7,376.00    | +116.29%    |
| Net Income                 | 12,587.00  | 5,644.00   | +6,943.00    | +123.02%    |
| Provision for Income Taxes  | 1,132.00   | 699.00     | +433.00      | +61.95%     |

### Analysis
1. **Income Growth**: Tesla's income before taxes increased by 116.29%, indicating a strong operational performance and effective cost management. The net income also saw a substantial rise of 123.02%, reflecting improved profitability.

2. **Tax Provision**: The provision for income taxes increased by 61.95%, which is consistent with the growth in income. This suggests that Tesla is effectively managing its tax liabilities as its profitability grows.

3. **Future Outlook**: Given the substantial growth in income and net income, Tesla appears to be on a positive trajectory. The Altman Z-Score analysis indicates that Tesla is in a favorable position with a low risk of bankruptcy, which further supports a positive outlook.

### Risk Assessment
The Altman Z-Score analysis provides insights into Tesla's financial stability, indicating effective management of assets and a strong equity position relative to its liabilities. The Z-Score is calculated as follows:

- **Altman Z-Score**: 8.367 (Safe Zone - Low Bankruptcy Risk)
  - Working Capital to Assets: 0.1726
  - Retained Earnings to Assets: 0.1565
  - EBIT to Assets: 0.1659
  - Market Value of Equity to Liabilities: 10.6751
  - Sales to Assets: 0.9894

### Additional Considerations
- **Investment in Growth**: Tesla's ongoing investments in production capacity, such as the Gigafactories, and its focus on innovation in electric vehicles and renewable energy solutions are likely to support continued revenue growth.
- **Market Conditions**: The automotive and energy markets are subject to fluctuations. Tesla's ability to maintain its growth trajectory will depend on market demand, competition, and regulatory environments.
- **Debt Management**: Monitoring Tesla's debt levels and interest coverage will be crucial in assessing its long-term financial stability.

### SWOT Analysis
1. **Strengths:**
   - Proprietary technology and strong brand recognition.
   - Economies of scale in production and distribution.

2. **Weaknesses:**
   - Areas needing improvement include supply chain management and dependency on single-source suppliers.
   - Potential resource shortages could impact production.

3. **Opportunities:**
   - Market trends such as the Inflation Reduction Act (IRA) tax credits can be leveraged to boost sales.
   - Opportunities to expand into new geographic markets or product lines.

4. **Threats:**
   - Increasing competition in the electric vehicle market.
   - Supply chain disruption risks and volatile raw material prices.

### Conclusion
Tesla's financial health appears strong based on the significant growth in income and net income from 2021 to 2022. The analysis indicates a low risk of financial distress, supporting a positive outlook. Continued focus on operational efficiency, market expansion, and innovation will be key to sustaining this growth.

*Source: NASDAQ_TSLA_2022.pdf.*

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a generally positive assessment of Tesla's financial health and future outlook. However, it does not fully address all the issues identified by the Critic, leaving several critical areas unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, provides an analysis of income growth, discusses risk assessment, and includes a SWOT analysis. Additionally, it presents a comparison table of financial metrics, which enhances the report's clarity.

## Issues Resolution Status
Out of the seven issues identified by the Critic:
- **Resolved Issues**:
  1. Clarified the source and calculation of income before taxes and net income figures.
  2. Discussed the limitations of the Altman Z-Score and compared it to industry peers.
  3. Included a detailed analysis of supply chain risks related to single-source dependencies.

- **Unresolved Issues**:
  1. Provide context for income growth metrics, including industry benchmarks.
  2. Address potential valuation risks and overvaluation concerns.
  3. Analyze competitive pressures and how Tesla's market position compares to rivals.
  4. Improve visual representation of financial metrics with graphs or charts.

## Remaining Gaps
The following issues remain unresolved:
1. Context for income growth metrics, including industry benchmarks.
2. Potential valuation risks and overvaluation concerns.
3. Analysis of competitive pressures and Tesla's market position compared to rivals.
4. Enhancement of visual representation of financial metrics with graphs or charts.

## Recommendation
It is recommended that the advisor revises the report to address the unresolved issues. Specifically, providing industry benchmarks for income growth, discussing valuation risks, analyzing competitive pressures, and improving visual representations will enhance the report's comprehensiveness and utility for investors.
"""
