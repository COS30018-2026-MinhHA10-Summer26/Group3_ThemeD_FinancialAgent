"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_12.py.
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

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a generally positive overview of Tesla's financial health and future outlook. However, it lacks depth in risk assessment and fails to address several critical areas that could impact investor decisions and competitive positioning. \n\n## Major Logic Gaps\n1. **Inconsistent Revenue Figures**: The report states that total revenues increased to $81.5 billion in 2022, but the table shows $81,462 million. This inconsistency could confuse readers and undermine credibility.\n2. **Lack of Comprehensive Risk Analysis**: The report mentions a risk assessment but does not compute the Altman Z-Score due to insufficient data. This raises questions about the thoroughness of the risk evaluation.\n\n## Unsupported or Weakly Supported Claims\n1. **Net Income and Cash Flow Figures**: The report claims a net income of $12.6 billion and cash flow from operations of $14.7 billion, but these figures are not clearly supported by the context documents. They should be explicitly referenced or calculated from the provided data.\n2. **Assumption of Continued Demand**: The assertion that demand for electric vehicles will continue to drive revenue growth is not substantiated with market data or trends, making it a weak claim.\n\n## Missing Investor Risks\n1. **Competition**: The report does not address the competitive landscape, which is crucial for understanding Tesla's market position and potential threats.\n2. **Valuation Risks**: There is no discussion on Tesla's valuation, which is essential for investors considering the stock's price relative to its earnings and growth potential.\n3. **Supply Chain Risks**: While the context documents mention single-source supplier dependencies, the report fails to address how these could impact Tesla's operations and financial health.\n4. **Regulatory Risks**: The report does not discuss potential regulatory changes that could affect Tesla's operations or profitability, particularly in the context of the Inflation Reduction Act.\n5. **Execution Risks**: The report lacks an analysis of execution risks related to Tesla's ambitious growth plans and technological advancements.\n\n## Figure and Visualization Issues\n- The figure comparing key financial metrics is well-presented, but the report should ensure that all figures are consistent and accurately reflect the data discussed in the text.\n\n## Competitor Counterarguments\n1. **Market Saturation**: Competitors may argue that the electric vehicle market is becoming saturated, which could limit Tesla's growth potential.\n2. **Technological Advancements by Rivals**: Other automakers are rapidly advancing in EV technology, which could erode Tesla's competitive advantage.\n3. **Cost Management Challenges**: While the report claims effective cost management, competitors may highlight potential challenges in maintaining this as production scales.\n\n## Revision Priorities\n1. **Clarify Revenue Figures**: Ensure consistency in reported revenue figures throughout the report.\n2. **Enhance Risk Assessment**: Include a comprehensive analysis of competition, valuation, supply chain, regulatory, and execution risks.\n3. **Support Claims with Data**: Provide clear references or calculations for net income and cash flow figures.\n4. **Substantiate Demand Assumptions**: Include market data or trends to support claims about continued demand for EVs.\n\n## Issues to Resolve\n- [ ] Clarify and ensure consistency in revenue figures throughout the report.\n- [ ] Include a comprehensive risk assessment addressing competition, valuation, supply chain, regulatory, and execution risks.\n- [ ] Provide clear references or calculations for net income and cash flow figures.\n- [ ] Substantiate claims about continued demand for electric vehicles with market data or trends."
}
