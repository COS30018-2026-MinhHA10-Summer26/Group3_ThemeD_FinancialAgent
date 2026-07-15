"""
Mock inputs for testing the Evaluator Agent.

Auto-generated from evaluator run: mock_data_5.py.
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

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

Based on the analysis of Tesla's financial health and future outlook, here are the key insights derived from the provided documents:

## Financial Health Assessment

Tesla's financial health can be evaluated through various factors, including its operational risks, market conditions, and regulatory environment. Here are some critical points:

1. **Operational Risks**: Tesla faces significant operational risks, including potential disruptions from union activities, product recalls, and warranty claims. These factors could lead to increased costs and impact profitability. For instance, past recalls have affected consumer trust and could lead to increased warranty claims.

2. **Debt Management**: As of December 31, 2022, Tesla had approximately $5.748 billion in outstanding debt. The company must manage its debt levels carefully, as covenant restrictions could limit operational flexibility and access to additional financing.

3. **Market Volatility**: The trading price of Tesla's stock has been highly volatile, influenced by various external factors, including market conditions and public perception. This volatility can affect investor confidence and the company's market capitalization.

4. **Regulatory Challenges**: Tesla's operations are subject to evolving laws and regulations, particularly concerning environmental standards and direct-to-consumer sales models. Changes in these regulations could impact sales and operational costs.

5. **Currency Fluctuations**: Operating in multiple currencies exposes Tesla to foreign exchange risks, which can affect revenue and costs. The strength of the U.S. dollar against other currencies can significantly impact financial results.

### Bankruptcy Risk Assessment

Using the Altman Z-Score, Tesla's financial stability is assessed as follows:

- **Z-Score**: 8.367 (Safe Zone - Low Bankruptcy Risk)
- **Liabilities to Market Cap Ratio**: 0.0937

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
| EBIT               | $13,656.00        | $3,000.00         | +$10,656.00         | +355.20%          |
| Sales              | $81,462.00        | $50,000.00        | +$31,462.00         | +62.92%           |
| Total Assets       | $82,338.00        | $50,000.00        | +$32,338.00         | +64.68%           |
| Total Liabilities  | $36,440.00        | $20,000.00        | +$16,440.00         | +82.20%           |

## Conclusion

Tesla's financial health is influenced by various operational and market factors. While the company has significant growth potential, it must navigate challenges related to debt management, regulatory compliance, and market volatility. Continuous innovation and strategic planning will be essential for sustaining its competitive advantage in the electric vehicle market.

For a more detailed analysis, specific financial metrics would be beneficial to assess Tesla's risk of bankruptcy and overall financial stability accurately. Additionally, it is crucial to consider competition and execution risks as Tesla continues to expand its market presence.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more accurate assessment of Tesla's financial health and future outlook compared to the original version. However, it still lacks actionable advice and does not fully address all issues identified by the Critic.

## Query Satisfaction
The revised report adequately covers the financial health and future outlook of Tesla, but it fails to provide actionable advice, which was a key component of the user query. Therefore, while it addresses the main topics, it does not fully satisfy the user's request for advice.

## Issues Resolution Status
Out of the seven issues identified by the Critic:
- **Resolved Issues**:
  1. Provide actionable advice based on the financial analysis.
  2. Expand on operational risks with specific examples.
  3. Include a discussion on competition as a risk factor.
  4. Discuss execution risks related to growth plans and product development.

- **Unresolved Issues**:
  1. Correct the outstanding debt figure to match the financial statements.
  2. Elaborate on supply chain risks related to single-source dependencies.
  3. Consider adding figures or visualizations to enhance the report.

## Remaining Gaps
The following gaps remain unresolved:
1. The outstanding debt figure is still incorrect; it should match the financial statements indicating total debt of $5,748 million.
2. Supply chain risks related to single-source dependencies have not been elaborated upon.
3. The report lacks figures or visualizations that could enhance understanding of Tesla's financial metrics and trends.

## Recommendation
It is recommended that the advisor revise the report to:
1. Correct the outstanding debt figure to accurately reflect the financial statements.
2. Provide a detailed discussion on supply chain risks, particularly focusing on single-source dependencies.
3. Include relevant figures or visualizations to support the financial analysis and improve clarity for the reader. 

Addressing these points will enhance the report's completeness and better meet the user's request for advice on Tesla's financial health and future outlook.
"""
