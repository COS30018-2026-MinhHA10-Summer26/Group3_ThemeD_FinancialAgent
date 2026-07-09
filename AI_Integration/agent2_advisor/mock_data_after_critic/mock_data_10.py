"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_10.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla, Inc. Financial Health and Future Outlook

## Overview
Based on the financial statements for the year ended December 31, 2022, Tesla has shown significant growth in several key financial metrics compared to the previous year. This report analyzes Tesla's financial health, focusing on liquidity, capital resources, and overall performance.

## Key Financial Metrics Comparison

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Cash and cash equivalents   | 16,253     | 17,576     | -1,323       | -7.53%      |
| Short-term investments      | 5,932      | 131        | +5,801       | +4428.24%   |
| Stockholders' equity       | 44,704     | 30,189     | +14,515      | +48.08%     |
| Total assets               | 82,338     | 62,131     | +20,207      | +32.52%     |
| Total liabilities           | 36,440     | 30,548     | +5,892       | +19.29%     |

### Source Note
Data sourced from Tesla's 2022 financial statements.

## Financial Health Analysis

### Liquidity
- **Cash and Cash Equivalents**: Decreased by 7.53%, indicating a reduction in liquid assets. However, the company still maintains a substantial cash reserve of $16.25 billion.
- **Short-term Investments**: Increased dramatically by over 4428%, reflecting a strategic shift towards more liquid investments, which can provide flexibility in funding operations and growth.

### Capital Resources
- **Stockholders' Equity**: Increased by 48.08%, suggesting strong retained earnings and overall financial health. This increase indicates that Tesla is effectively reinvesting profits back into the business.
- **Total Assets**: Grew by 32.52%, showcasing the company's expansion and investment in growth initiatives, including manufacturing facilities and technology development.
- **Total Liabilities**: Increased by 19.29%, which is manageable given the growth in assets and equity. The rise in liabilities may be associated with financing for expansion projects.

### Risk Assessment
The Altman Z-Score could not be computed due to insufficient data. However, the overall financial metrics suggest that Tesla is in a solid position, with a healthy balance between assets and liabilities. 

### Alternative Risk Considerations
While the Altman Z-Score is not available, Tesla's financial health can be qualitatively assessed through its liquidity ratios, debt levels, and cash flow management. The company has maintained a positive operating cash flow, which supports its ongoing operations and growth initiatives.

## Future Outlook
Tesla's future outlook appears positive, driven by:
- Continued investment in manufacturing capabilities and technology.
- Strong operating cash flow, which supports ongoing operations and expansion.
- A proactive approach to managing capital expenditures, allowing for flexibility in response to market conditions.

### Recommendations
1. **Monitor Cash Flow**: Given the decrease in cash and cash equivalents, it is essential to closely monitor cash flow to ensure liquidity is maintained.
2. **Evaluate Debt Levels**: While the increase in liabilities is manageable, Tesla should continue to evaluate its debt levels to ensure they do not hinder future growth.
3. **Focus on Growth Initiatives**: Continue investing in R&D and manufacturing to maintain competitive advantages in the electric vehicle market.

In conclusion, Tesla's financial health is robust, with significant growth in equity and assets, positioning the company well for future opportunities.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook. However, it contains several logic gaps, unsupported claims, and missing risk considerations that need to be addressed to enhance its credibility and decision-grade quality.\n\n## Major Logic Gaps\n- The report claims that Tesla's financial health is \"robust\" based on growth metrics, yet it does not adequately address the implications of the decrease in cash and cash equivalents. This could mislead investors about the company's liquidity position.\n- The assertion that the increase in total liabilities is \"manageable\" lacks a comparative analysis with industry standards or historical data, which is essential for context.\n\n## Unsupported or Weakly Supported Claims\n- The report states that \"the overall financial metrics suggest that Tesla is in a solid position,\" but this conclusion is not backed by a thorough analysis of cash flow or profitability ratios.\n- The claim regarding the positive operating cash flow is made without providing specific figures or trends, which weakens the argument.\n\n## Missing Investor Risks\n- The report fails to address significant risks related to competition, valuation, supply chain dependencies, and regulatory changes. These are critical factors that could impact Tesla's future performance and should be included in a comprehensive risk assessment.\n- The absence of a discussion on margin pressure, especially in the context of rising material costs and competition, is a notable oversight.\n\n## Figure and Visualization Issues\n- While the report includes a table comparing key financial metrics, it lacks visual aids that could enhance understanding, such as graphs or charts that illustrate trends over time. This could make the data more accessible and impactful for investors.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's reliance on single-source suppliers for key components poses a significant risk, especially in a volatile market. This point is not addressed in the report, leaving a gap in the analysis.\n- The report does not consider the competitive landscape, particularly how emerging EV manufacturers might affect Tesla's market share and pricing power.\n\n## Revision Priorities\n1. Provide a more nuanced analysis of liquidity, particularly regarding the implications of decreased cash reserves.\n2. Include a detailed risk assessment that covers competition, valuation, supply chain, and regulatory risks.\n3. Support claims with specific data points and trends, particularly regarding cash flow and profitability.\n4. Enhance visual representation of financial data to improve clarity and engagement.\n\n## Issues to Resolve\n- [ ] Address the implications of decreased cash and cash equivalents on liquidity.\n- [ ] Provide comparative analysis for total liabilities to support claims of manageability.\n- [ ] Include specific figures or trends to substantiate claims about positive operating cash flow.\n- [ ] Discuss risks related to competition, valuation, supply chain dependencies, and regulatory changes.\n- [ ] Consider the impact of margin pressure on Tesla's financial outlook.\n- [ ] Add visual aids (graphs/charts) to enhance the presentation of financial metrics."
}
