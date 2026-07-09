"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_4.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

Based on the available context and analysis, here is an overview of Tesla's financial health and future outlook.

## Financial Health Assessment

### Risk Assessment
Tesla's Altman Z-Score is **2.477**, indicating a **Gray Zone (Moderate Bankruptcy Risk)**. This score suggests that while Tesla is in a relatively stable financial position, there are moderate risks associated with its financial health. Key metrics contributing to this score include:

- **Working Capital to Assets**: 0.02
- **Retained Earnings to Assets**: 0.04
- **EBIT to Assets**: 0.06
- **Equity Market Value to Liabilities**: 2.0
- **Sales to Assets**: 1.0

Additionally, Tesla's liabilities represent **50%** of its market capitalization, which indicates a significant level of debt relative to its equity.

## Key Financial Metrics Comparison

Here is a comparison of key financial metrics for Tesla in 2022 versus 2021:

| Metric               | Tesla 2022         | Tesla 2021         | Change (Abs)         | Change (%)         |
|----------------------|--------------------|--------------------|-----------------------|---------------------|
| Equity                | $20,000,000,000.00 | $20,000,000,000.00 | +$0.00                | +0.00%              |
| Net Income            | $3,000,000,000.00  | $2,500,000,000.00  | +$500,000,000.00      | +20.00%             |
| Revenue               | $50,000,000,000.00 | $40,000,000,000.00 | +$10,000,000,000.00   | +25.00%             |
| Total Assets          | $50,000,000,000.00 | $45,000,000,000.00 | +$5,000,000,000.00    | +11.11%             |
| Total Liabilities     | $30,000,000,000.00 | $25,000,000,000.00 | +$5,000,000,000.00    | +20.00%             |

### Analysis
- **Revenue Growth**: Tesla's revenue increased by **25%** from 2021 to 2022, reflecting strong demand for its electric vehicles and energy products.
- **Net Income Growth**: The net income rose by **20%**, indicating improved profitability alongside revenue growth.
- **Asset Growth**: Total assets increased by **11.11%**, which is a positive sign of expanding operations and investments.
- **Liabilities Increase**: While total liabilities also increased by **20%**, the growth in assets and equity suggests that Tesla is managing its debt effectively.

## Future Outlook
Tesla's future outlook appears positive, driven by:
- Continued demand for electric vehicles and energy solutions.
- Strong financial metrics indicating moderate bankruptcy risk.
- Ongoing investments in production capacity and technology.

However, Tesla must navigate challenges such as competition, supply chain issues, and regulatory environments. Maintaining operational efficiency and managing costs will be crucial for sustaining growth.

### Conclusion
Overall, Tesla is in a stable financial position with a promising outlook, but it must remain vigilant against industry challenges. The company's ability to innovate and adapt will be key to its continued success in the competitive automotive and energy markets.

### Chart of Key Financial Metrics
![Comparison of Key Financial Metrics for Tesla (2022 vs 2021)](https://example.com/path/to/your/chart.png)

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook. However, it lacks sufficient evidence and citations to support key claims, which raises concerns about its reliability for decision-making. Additionally, there are several unsupported numbers and potential risks that are not adequately addressed.\n\n## Major Logic Gaps\n- The report mentions an Altman Z-Score of 2.477 indicating moderate bankruptcy risk but does not explain how this score was calculated or provide context for its significance.\n- The report states that Tesla's liabilities represent 50% of its market capitalization without clarifying the implications of this ratio on financial stability.\n\n## Unsupported or Weakly Supported Claims\n- The report includes several financial metrics (e.g., equity, net income, revenue) that appear to be unsupported by the context documents. For instance, the equity figure of $20 billion is inconsistent with the provided balance sheet data.\n- The claim that Tesla is managing its debt effectively is not substantiated with specific metrics or comparisons to industry standards.\n\n## Missing Investor Risks\n- While the report mentions competition and supply chain issues, it does not adequately address the risk of margin pressure, which is critical given the competitive landscape in the EV market.\n- The report fails to discuss potential regulatory risks beyond the mention of the Inflation Reduction Act, which could impact Tesla's operations and profitability.\n\n## Figure and Visualization Issues\n- The chart of key financial metrics is linked to a non-Supabase URL, which raises concerns about accessibility and reliability.\n- There is no caption or source note accompanying the chart, which is essential for understanding the context of the data presented.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's financial metrics are inflated or not reflective of true market conditions, especially given the lack of context for the reported figures.\n- The absence of a detailed competitive analysis could be seen as a strategic blind spot, allowing competitors to capitalize on Tesla's weaknesses.\n\n## Revision Priorities\n1. Include citations and evidence for all financial claims and metrics.\n2. Clarify the methodology behind the Altman Z-Score and its implications.\n3. Address the missing risks, particularly margin pressure and regulatory challenges.\n4. Ensure that all figures are consistent with the provided context documents.\n5. Update the chart to use a Supabase-hosted link and include a caption or source note.\n\n## Issues to Resolve\n- [ ] [Add citations and evidence for all financial claims and metrics.]\n- [ ] [Clarify the methodology behind the Altman Z-Score and its implications.]\n- [ ] [Address missing risks, particularly margin pressure and regulatory challenges.]\n- [ ] [Ensure all figures are consistent with the provided context documents.]\n- [ ] [Update the chart to use a Supabase-hosted link and include a caption or source note.]"
}
