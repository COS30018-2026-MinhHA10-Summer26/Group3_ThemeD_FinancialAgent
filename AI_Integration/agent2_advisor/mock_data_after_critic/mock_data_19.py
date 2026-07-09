"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_19.py.
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

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a generally positive assessment of Tesla's financial health and future outlook, highlighting significant growth in income and profitability. However, it lacks depth in risk assessment and fails to address critical areas that could impact investor decisions and competitive positioning.\n\n## Major Logic Gaps\n1. **Lack of Context for Growth Metrics**: While the report highlights impressive growth percentages, it does not provide context regarding industry benchmarks or historical performance, making it difficult to assess whether this growth is sustainable or exceptional.\n2. **Overreliance on Altman Z-Score**: The report heavily leans on the Altman Z-Score without discussing its limitations or how it compares to industry peers, which could mislead investors about the company's financial stability.\n\n## Unsupported or Weakly Supported Claims\n1. **Income Growth Claims**: The report states that income before taxes and net income increased significantly, but it does not provide a source or detailed breakdown of how these figures were calculated, raising questions about their accuracy.\n2. **Tax Provision Management**: The assertion that Tesla is effectively managing its tax liabilities lacks supporting evidence or examples of specific strategies employed.\n\n## Missing Investor Risks\n1. **Valuation Risks**: The report does not address potential overvaluation concerns, especially given Tesla's high market capitalization relative to its earnings.\n2. **Supply Chain Risks**: The report fails to discuss the implications of single-source supplier dependencies highlighted in the context documents, which could pose significant risks to production and profitability.\n3. **Competition**: While competition is mentioned, the report does not analyze how Tesla's market position compares to emerging competitors in the EV space, which is crucial for understanding future growth prospects.\n\n## Figure and Visualization Issues\n- The report includes a comparison table of key financial metrics, but it lacks visual aids such as graphs or charts that could enhance understanding and engagement. Additionally, the table is repeated without any added value, which could be seen as redundant.\n\n## Competitor Counterarguments\n1. **Market Saturation**: Competitors may argue that Tesla's growth is unsustainable due to increasing competition in the EV market, which the report does not adequately address.\n2. **Technological Risks**: Competitors could highlight potential technological setbacks or failures in Tesla's ambitious projects (like FSD and Optimus) that could hinder growth, which are not discussed in the report.\n\n## Revision Priorities\n1. **Provide Context for Financial Metrics**: Include industry benchmarks and historical performance comparisons to give a clearer picture of Tesla's growth.\n2. **Expand Risk Assessment**: Address missing risks related to valuation and supply chain dependencies, and provide a more comprehensive analysis of competitive pressures.\n3. **Enhance Visual Representation**: Improve the visual presentation of financial data with graphs or charts to make the information more digestible and engaging.\n\n## Issues to Resolve\n- [ ] Provide context for income growth metrics, including industry benchmarks.\n- [ ] Clarify the source and calculation of income before taxes and net income figures.\n- [ ] Discuss the limitations of the Altman Z-Score and compare it to industry peers.\n- [ ] Address potential valuation risks and overvaluation concerns.\n- [ ] Include a detailed analysis of supply chain risks related to single-source dependencies.\n- [ ] Analyze competitive pressures and how Tesla's market position compares to rivals.\n- [ ] Improve visual representation of financial metrics with graphs or charts."
}
