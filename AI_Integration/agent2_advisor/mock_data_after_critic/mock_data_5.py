"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_5.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

Based on the analysis of Tesla's financial health and future outlook, here are the key insights derived from the provided documents:

## Financial Health Assessment

Tesla's financial health can be evaluated through various factors, including its operational risks, market conditions, and regulatory environment. Here are some critical points:

1. **Operational Risks**: Tesla faces significant operational risks, including potential disruptions from union activities, product recalls, and warranty claims. These factors could lead to increased costs and impact profitability.

2. **Debt Management**: As of December 31, 2022, Tesla had approximately $2.06 billion in outstanding debt. The company must manage its debt levels carefully, as covenant restrictions could limit operational flexibility and access to additional financing.

3. **Market Volatility**: The trading price of Tesla's stock has been highly volatile, influenced by various external factors, including market conditions and public perception. This volatility can affect investor confidence and the company's market capitalization.

4. **Regulatory Challenges**: Tesla's operations are subject to evolving laws and regulations, particularly concerning environmental standards and direct-to-consumer sales models. Changes in these regulations could impact sales and operational costs.

5. **Currency Fluctuations**: Operating in multiple currencies exposes Tesla to foreign exchange risks, which can affect revenue and costs. The strength of the U.S. dollar against other currencies can significantly impact financial results.

### Bankruptcy Risk Assessment

Using the Altman Z-Score, Tesla's financial stability is assessed as follows:

- **Z-Score**: 25.277 (Safe Zone - Low Bankruptcy Risk)
- **Liabilities to Market Cap Ratio**: 0.025

This indicates that Tesla is in a strong financial position with a low risk of bankruptcy.

## Future Outlook

Tesla's future outlook remains cautiously optimistic, driven by its commitment to innovation and expansion in the electric vehicle market. However, several factors will influence its trajectory:

- **Product Development**: Continued investment in research and development is crucial for maintaining a competitive edge in the rapidly evolving automotive industry.

- **Market Demand**: The demand for electric vehicles is expected to grow, supported by government incentives and increasing consumer awareness of sustainability. However, any reduction in these incentives could negatively impact sales.

- **Global Expansion**: Tesla's expansion into international markets presents opportunities for growth but also introduces complexities related to regulatory compliance and market entry strategies.

## Key Financial Metrics Comparison

Here is a comparison of key financial metrics for Tesla in 2022 versus 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric             | Tesla 2022         | Tesla 2021         | Change (Abs)         | Change (%)         |
| :----------------- | :----------------: | :----------------: | :------------------: | :----------------: |
| EBIT               | $3,000,000,000.00  | $2,000,000,000.00  | +$1,000,000,000.00   | +50.00%           |
| Sales              | $50,000,000,000.00 | $40,000,000,000.00 | +$10,000,000,000.00  | +25.00%           |
| Total Assets       | $50,000,000,000.00 | $45,000,000,000.00 | +$5,000,000,000.00   | +11.11%           |
| Total Liabilities  | $20,000,000,000.00 | $18,000,000,000.00 | +$2,000,000,000.00   | +11.11%           |

## Conclusion

Tesla's financial health is influenced by various operational and market factors. While the company has significant growth potential, it must navigate challenges related to debt management, regulatory compliance, and market volatility. Continuous innovation and strategic planning will be essential for sustaining its competitive advantage in the electric vehicle market.

For a more detailed analysis, specific financial metrics would be beneficial to assess Tesla's risk of bankruptcy and overall financial stability accurately.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a reasonable overview of Tesla's financial health and future outlook. However, it lacks actionable advice and contains several unsupported claims and missing risk factors that could mislead investors and strategic planners.\n\n## Major Logic Gaps\n1. The report states that Tesla has approximately $2.06 billion in outstanding debt, which contradicts the provided financial statements that indicate total debt of $5,748 million. This discrepancy raises questions about the accuracy of the financial assessment.\n2. The bankruptcy risk assessment using the Altman Z-Score is presented without context or explanation of how this score was derived, leaving it unclear whether the calculation is accurate or relevant.\n\n## Unsupported or Weakly Supported Claims\n1. The claim that Tesla's stock price volatility affects investor confidence is not substantiated with data or examples, making it a weak assertion.\n2. The report mentions \"significant operational risks\" but does not quantify or provide specific examples of how these risks have impacted Tesla in the past or could impact it in the future.\n\n## Missing Investor Risks\n1. The report fails to address competition as a risk factor, which is critical given the increasing number of players in the electric vehicle market.\n2. Supply chain risks are mentioned but not elaborated upon, particularly regarding single-source supplier dependencies that could disrupt production.\n3. Execution risks related to Tesla's ambitious growth plans and product development timelines are not discussed, which could lead to strategic blind spots.\n\n## Figure and Visualization Issues\n- There are no figures or visualizations included in the report, which could enhance understanding and provide a clearer picture of Tesla's financial metrics and trends.\n\n## Competitor Counterarguments\n1. Competitors may argue that Tesla's reliance on government incentives for sales is a significant risk, especially if these incentives are reduced or eliminated.\n2. The lack of discussion on competition could be seen as a strategic oversight, as competitors may leverage Tesla's weaknesses in this area to capture market share.\n\n## Revision Priorities\n1. Correct the debt figure to align with the financial statements and clarify the source of the $2.06 billion figure.\n2. Provide actionable advice based on the financial analysis, including specific recommendations for managing risks and capitalizing on opportunities.\n3. Expand on operational risks with specific examples and potential impacts on Tesla's financial health.\n4. Include a discussion on competition and execution risks to provide a more comprehensive risk assessment.\n\n## Issues to Resolve\n- [ ] Correct the outstanding debt figure to match the financial statements.\n- [ ] Provide actionable advice based on the financial analysis.\n- [ ] Expand on operational risks with specific examples.\n- [ ] Include a discussion on competition as a risk factor.\n- [ ] Elaborate on supply chain risks related to single-source dependencies.\n- [ ] Discuss execution risks related to growth plans and product development.\n- [ ] Consider adding figures or visualizations to enhance the report."
}
