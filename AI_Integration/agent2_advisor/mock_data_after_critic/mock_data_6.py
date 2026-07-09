"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_6.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla's Financial Health and Future Outlook

## Financial Health Assessment

Based on the Altman Z-Score analysis, Tesla's financial health is in a **Safe Zone** with a score of **44.454**, indicating a low risk of bankruptcy. Here are the key components of the score:

- **Working Capital to Assets**: 14.12%
- **Retained Earnings to Assets**: 5.26%
- **EBIT to Assets**: 6.58%
- **Market Capitalization to Liabilities**: 72.73
- **Sales to Assets**: 35.73%

Additionally, the ratio of total liabilities to market capitalization is **1.38%**, which further supports the conclusion of a strong financial position.

## Key Financial Metrics Comparison

The following chart compares Tesla's key financial metrics for the years 2022 and 2021:

![Key Financial Metrics Comparison (2022 vs 2021)](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_a14245f034ef_key-financial-metrics-comparison-2022-vs-2021.png)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*

*Source: NASDAQ TSLA 2022 Annual Report*

### Financial Metrics Table

| Metric                | Tesla 2022         | Tesla 2021         | Change (Abs)       | Change (%)       |
|-----------------------|--------------------|--------------------|---------------------|------------------|
| Capital Expenditures   | $7,160,000,000.00  | $6,480,000,000.00  | +$680,000,000.00    | +10.49%          |
| Cash and Equivalents   | $22,190,000,000.00 | $17,770,000,000.00 | +$4,420,000,000.00  | +24.87%          |
| Net Income             | $12,560,000,000.00 | $5,492,000,000.00  | +$7,068,000,000.00  | +128.70%         |
| Total Revenue          | $81,460,000,000.00 | $58,600,000,000.00 | +$22,860,000,000.00 | +39.01%          |

## Future Outlook

Tesla's significant growth in revenue and net income in 2022, alongside an increase in cash reserves, positions the company well for future investments and expansions. The increase in capital expenditures indicates a commitment to scaling operations and enhancing production capabilities.

### Strategic Recommendations:
1. **Investment in R&D**: Continue to invest in research and development, particularly in battery technology and autonomous driving features, to maintain competitive advantages.
2. **Market Expansion**: Explore opportunities in emerging markets where electric vehicle adoption is growing, leveraging government incentives where available.
3. **Cost Management**: Monitor and manage operational costs to sustain profitability, especially as production scales up.
4. **Regulatory Compliance**: Stay ahead of evolving regulations in different markets to avoid potential legal challenges that could impact operations.

## Risks and Limitations

While Tesla's financial health appears strong, several risks could impact its future outlook:

- **Regulatory Challenges**: Changes in government incentives and regulations regarding electric vehicles could affect demand and operational costs.
- **Market Volatility**: The stock price has historically been volatile, influenced by external factors and public perception.
- **Supply Chain Issues**: Ongoing supply chain disruptions could impact production capabilities and costs.
- **Competition**: The electric vehicle market is becoming increasingly competitive, with new entrants and established automakers ramping up their EV offerings.

## Conclusion

Tesla's financial health is robust, with strong revenue growth and low bankruptcy risk. By focusing on strategic investments and maintaining compliance with regulations, Tesla can continue to thrive in the competitive electric vehicle market. However, it must remain vigilant regarding potential risks that could impact its operations and market position.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report on Tesla's financial health and future outlook provides a generally positive assessment but lacks sufficient evidence for some claims and does not adequately address certain risks. The report is not fully decision-grade due to unsupported figures and missing context on competitive pressures.\n\n## Major Logic Gaps\n- The Altman Z-Score is presented as a definitive measure of financial health, but the report does not explain how this score is calculated or its limitations. This could mislead investors who may not be familiar with the metric.\n- The report states that Tesla's financial health is in a \"Safe Zone\" without discussing what this means in practical terms or how it compares to industry standards.\n\n## Unsupported or Weakly Supported Claims\n- Several financial figures, including net income and total revenue, are flagged as possibly unsupported. The report does not provide sufficient context or citations to validate these numbers.\n- The claim that the ratio of total liabilities to market capitalization is \"1.38%\" is presented without context on how this compares to industry norms or what it implies for financial stability.\n\n## Missing Investor Risks\n- The report mentions risks such as regulatory challenges and supply chain issues but does not explore the potential impact of these risks on Tesla's financial performance or stock price.\n- There is no discussion of margin pressure, which is critical given the competitive landscape and rising costs in the EV market.\n\n## Figure and Visualization Issues\n- The figure comparing key financial metrics is included but lacks a detailed explanation of its significance. The report should clarify what the changes in metrics imply for Tesla's future performance.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's reliance on government incentives and regulatory credits makes its financial health less stable than presented. This point is not adequately addressed in the report.\n- The increasing competition in the EV market is mentioned, but the report does not quantify how this could affect Tesla's market share or pricing power.\n\n## Revision Priorities\n1. Provide detailed explanations of financial metrics and their implications.\n2. Validate all financial figures with appropriate citations or context.\n3. Expand on the risks section to include potential impacts of identified risks.\n4. Enhance the figure's explanation to clarify its relevance to the overall analysis.\n\n## Issues to Resolve\n- [ ] Provide context and explanation for the Altman Z-Score and its implications.\n- [ ] Validate all flagged financial figures with appropriate citations.\n- [ ] Discuss the potential impacts of regulatory challenges and supply chain issues on financial performance.\n- [ ] Include a discussion on margin pressure and its relevance to Tesla's competitive position.\n- [ ] Clarify the significance of the financial metrics comparison figure."
}
