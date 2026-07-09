"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_16.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Financial Health Analysis

Based on the financial statements for Tesla as of December 31, 2022, the company exhibits a mixed financial health profile. Here are the key insights:

1. **Altman Z-Score**: Tesla's Altman Z-Score is **5.509**, placing it in the **Safe Zone (Low Bankruptcy Risk)**. This indicates that Tesla is not at immediate risk of bankruptcy, which is a positive sign for investors.

   - **Working Capital to Assets**: 17.36%
   - **Retained Earnings to Assets**: -7.60%
   - **EBIT to Assets**: -0.30%
   - **Market Capitalization to Liabilities**: 7.04
   - **Sales to Assets**: 119.26%

2. **Liabilities to Market Capitalization**: The ratio is **0.142**, suggesting that Tesla's liabilities are manageable relative to its market capitalization.

3. **Sales Growth**: Tesla reported sales of **$81.38 billion** in 2022, a **16.26% increase** from **$70 billion** in 2021. This growth indicates strong demand for Tesla's products.

4. **Retained Earnings**: Tesla's retained earnings decreased to **-$5.19 billion**, a decline of **29.70%** from the previous year. This suggests that Tesla is reinvesting heavily in growth, but it also indicates a need for improved profitability.

5. **EBIT**: The company reported an EBIT of **-$204 million**, a significant decline from **$1 billion** in 2021, reflecting challenges in operational efficiency or increased costs.

## Comparison of Key Financial Metrics

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| EBIT                 | -204.00    | 1,000.00   | -1,204.00    | -120.40%   |
| Retained Earnings     | -5,188.00  | -4,000.00  | -1,188.00    | +29.70%    |
| Sales                | 81,380.00  | 70,000.00  | +11,380.00   | +16.26%    |
| Total Assets         | 68,236.00  | 58,000.00  | +10,236.00   | +17.65%    |
| Total Liabilities    | 27,688.00  | 25,000.00  | +2,688.00    | +10.75%    |

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| EBIT                 | -204.00    | 1,000.00   | -1,204.00    | -120.40%   |
| Retained Earnings     | -5,188.00  | -4,000.00  | -1,188.00    | +29.70%    |
| Sales                | 81,380.00  | 70,000.00  | +11,380.00   | +16.26%    |
| Total Assets         | 68,236.00  | 58,000.00  | +10,236.00   | +17.65%    |
| Total Liabilities    | 27,688.00  | 25,000.00  | +2,688.00    | +10.75%    |

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
- Financial data sourced from Tesla's financial statements for the years ended December 31, 2022 and 2021.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook, but it contains several critical gaps in logic, unsupported claims, and missing risks that need to be addressed for it to be considered decision-grade.\n\n## Major Logic Gaps\n1. **Inconsistent EBIT Reporting**: The report states that Tesla's EBIT is **-$204 million**, yet it also mentions a significant decline from **$1 billion** in 2021. This discrepancy raises questions about the accuracy of the figures presented.\n2. **Retained Earnings Confusion**: The report mentions retained earnings as **-$5.19 billion** but also states a decline of **29.70%** from the previous year without providing the correct context or calculation basis for this percentage.\n\n## Unsupported or Weakly Supported Claims\n1. **Altman Z-Score Interpretation**: While the report claims a Z-Score of **5.509** indicates a low bankruptcy risk, it does not provide context on how this score compares to industry benchmarks or historical performance, which is essential for a robust analysis.\n2. **Sales Growth Analysis**: The report highlights a **16.26% increase** in sales but fails to discuss the implications of this growth in relation to market trends or competitive positioning.\n\n## Missing Investor Risks\n1. **Supply Chain Risks**: The report does not address the single-source supplier dependencies mentioned in the context documents, which pose significant risks to Tesla's operations.\n2. **Regulatory Risks**: The impact of changing regulations, particularly in the EV market, is not discussed, despite being a visible risk in the context documents.\n3. **Execution Risks**: The report lacks an analysis of potential execution risks related to Tesla's ambitious growth plans and operational challenges.\n\n## Figure and Visualization Issues\n- There are no figures or visualizations included in the report, which could enhance understanding and provide a clearer picture of Tesla's financial metrics. Including charts or graphs could help visualize trends and comparisons.\n\n## Competitor Counterarguments\n1. **Market Competition**: The report does not address the competitive landscape, which is crucial for understanding Tesla's market position. Competitors may leverage this gap to argue that Tesla's growth is not guaranteed.\n2. **Cost Management**: Competitors could point out Tesla's declining EBIT as a sign of operational inefficiency, questioning the company's ability to maintain profitability amidst rising costs.\n\n## Revision Priorities\n1. Clarify and correct the EBIT and retained earnings figures to ensure accuracy.\n2. Provide context for the Altman Z-Score and sales growth figures, including industry comparisons.\n3. Address the missing risks related to supply chain, regulation, and execution.\n4. Consider adding visual aids to enhance the report's clarity and impact.\n\n## Issues to Resolve\n- [ ] Clarify EBIT reporting and ensure consistency in figures.\n- [ ] Correct retained earnings analysis and provide context for percentage changes.\n- [ ] Include context for the Altman Z-Score and sales growth figures.\n- [ ] Address missing risks related to supply chain, regulation, and execution.\n- [ ] Add visual aids to enhance understanding of financial metrics."
}
