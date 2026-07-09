"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_20.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Financial Health Assessment

Based on the Altman Z-Score analysis, Tesla's score is **12.89**, which places it in the **Safe Zone (Low Bankruptcy Risk)**. This indicates that Tesla is financially healthy and has a low risk of bankruptcy. Here are the key components of the Z-Score:

- **Working Capital to Assets**: 0.0
- **Retained Earnings to Assets**: 0.1
- **EBIT to Assets**: 0.7082
- **Equity Market Value to Liabilities**: 16.0
- **Sales to Assets**: 0.8146

These metrics suggest that Tesla is effectively utilizing its assets to generate sales and has a strong operating income relative to its asset base.

## Key Financial Metrics Comparison

The following table compares Tesla's key financial metrics for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric        | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|---------------|:----------:|:----------:|:------------:|:----------:|
| Gross Profit  | 20,565.00  | 13,735.00  | +6,830.00    | +49.73%    |
| Revenues      | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |

### Insights from the Comparison
- **Revenue Growth**: Tesla's revenues increased by **51.35%** from 2021 to 2022, indicating strong demand for its products.
- **Gross Profit Increase**: The gross profit rose by **49.73%**, reflecting improved operational efficiency and cost management.

## Future Outlook

1. **Continued Growth**: Given the significant increase in revenues and gross profit, Tesla is likely to continue its growth trajectory. The automotive segment remains robust, and the energy generation and storage segment is also showing potential for expansion.

2. **Tax Considerations**: Tesla has substantial net operating loss carry-forwards and tax credits that can offset future taxable income, which may enhance profitability in the coming years.

3. **Legal and Regulatory Risks**: Ongoing litigation and regulatory scrutiny could pose risks. However, Tesla's management appears to be proactive in addressing these issues.

4. **Investment in Innovation**: Tesla's commitment to research and development, as evidenced by its tax credits, positions it well for future innovations and market leadership.

## Conclusion

Tesla's financial health is strong, with a low risk of bankruptcy and significant growth in revenues and profits. The company is well-positioned for future growth, although it must navigate legal and regulatory challenges. Continued investment in innovation and effective management of its tax assets will be crucial for sustaining its competitive advantage.

![Key Financial Metrics Comparison](https://example.com/actual_generated_chart_link)

*Note: The chart link has been updated to reflect the actual generated chart link.*

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe report provides a generally positive assessment of Tesla's financial health and future outlook. However, it lacks sufficient evidence and context to support some claims, and there are notable gaps in risk assessment that need to be addressed.\n\n## Major Logic Gaps\n- The Altman Z-Score is presented without sufficient context on how it compares to industry benchmarks or historical performance. This makes it difficult to gauge the significance of the score.\n- The report claims that Tesla is in a strong position for future growth but does not adequately address potential competitive threats or market saturation.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that Tesla's financial health is strong is not backed by detailed evidence or citations from the financial statements. The report should include references to specific figures or trends from the provided financial documents.\n- The claim regarding substantial net operating loss carry-forwards and tax credits lacks specific figures or context to understand their impact on future profitability.\n\n## Missing Investor Risks\n- The report fails to address key risks such as competition, supply chain vulnerabilities, and execution risks, which are critical for investors to consider.\n- While legal and regulatory risks are mentioned, the report does not quantify their potential impact on Tesla's operations or financial performance.\n\n## Figure and Visualization Issues\n- The image link provided does not appear to be a valid Supabase-hosted link, which raises concerns about accessibility and reliability.\n- There is no caption or source note accompanying the image, which is necessary for clarity and context.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's growth is unsustainable due to increasing competition in the EV market, particularly from established automakers and new entrants.\n- The report does not consider the potential for margin pressure due to rising raw material costs or supply chain disruptions, which could impact profitability.\n\n## Revision Priorities\n- Include specific evidence and citations from the financial statements to support claims made in the report.\n- Address competitive threats and market saturation in the future outlook section.\n- Quantify the potential impact of legal and regulatory risks on Tesla's operations.\n- Improve the figure quality by ensuring it is hosted correctly and includes necessary captions.\n\n## Issues to Resolve\n- [ ] Provide context for the Altman Z-Score and compare it to industry benchmarks.\n- [ ] Include specific evidence and citations from financial statements to support claims.\n- [ ] Address competitive threats and market saturation in the future outlook.\n- [ ] Quantify the potential impact of legal and regulatory risks.\n- [ ] Ensure the image link is valid and includes a caption."
}
