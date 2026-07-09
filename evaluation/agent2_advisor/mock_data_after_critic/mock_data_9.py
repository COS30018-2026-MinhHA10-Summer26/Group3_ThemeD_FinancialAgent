"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_9.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Overview of Financial Performance

Tesla has demonstrated significant growth in its financial performance for the year ended December 31, 2022, compared to 2021. The key highlights from the financial statements include:

- **Total Revenues**: Increased by **51%** to **$81.46 billion** in 2022 from **$53.82 billion** in 2021.
- **Cash and Cash Equivalents**: As of December 31, 2022, Tesla held **$16.25 billion** in cash and cash equivalents, indicating strong liquidity.
- **Total Liabilities**: Total liabilities stood at **$2.06 billion**, which is manageable given the revenue and cash position.

### Comparison of Key Financial Metrics

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022          | Tesla 2021          | Change (Abs)         | Change (%)         |
|----------------------------|---------------------|---------------------|----------------------|--------------------|
| Cash and Cash Equivalents  | $16,250,000,000.00  | N/A                 | N/A                  | N/A                |
| Short-term Investments      | $5,930,000,000.00   | N/A                 | N/A                  | N/A                |
| Total Revenues             | $81,462,000,000.00  | $53,823,000,000.00  | +$27,639,000,000.00  | +51.35%            |
| Total Liabilities           | $2,060,000,000.00   | N/A                 | N/A                  | N/A                |

### Financial Health Assessment

1. **Liquidity**: Tesla's cash and cash equivalents of **$16.25 billion** provide a strong liquidity position, enabling the company to fund operations and investments without immediate reliance on external financing.

2. **Revenue Growth**: The substantial increase in total revenues indicates robust demand for Tesla's products, particularly in automotive sales, which grew significantly due to increased deliveries and production capacity.

3. **Cost Management**: While revenues increased, the cost of revenues also rose, leading to a slight decrease in gross margins. The gross margin for total automotive decreased from **29.3%** to **28.5%**. This indicates that while Tesla is growing, it faces challenges in managing costs effectively, particularly with rising raw material and logistics costs.

4. **Debt Management**: With total liabilities at **$2.06 billion**, Tesla appears to be in a good position regarding debt management, especially given its revenue and cash reserves.

5. **Future Outlook**: Tesla's ongoing investments in production capacity and technology, including new Gigafactories, suggest a commitment to growth. The company expects capital expenditures between **$6 billion to $8 billion** in 2023, indicating confidence in future revenue generation.

## Conclusion

Tesla's financial health appears strong, characterized by significant revenue growth, robust liquidity, and manageable debt levels. However, the company must focus on improving cost management to maintain healthy profit margins. The outlook remains positive, supported by ongoing investments in production and technology.

### Additional Recommendations

- **Cost Control Measures**: Implement strategies to manage rising costs, particularly in raw materials and logistics, to protect profit margins.
- **Diversification of Revenue Streams**: Continue to explore and expand into new markets and product lines, such as energy generation and storage, to mitigate risks associated with automotive sales.
- **Monitoring Foreign Currency Risks**: Given Tesla's global operations, it should consider strategies to hedge against foreign currency fluctuations that could impact financial results.

### Chart of Key Financial Metrics

![Key Financial Metrics](https://example.com/path/to/your/chart.png) 

*Note: The chart link is a placeholder. Please replace it with the actual link generated from your data visualization tool.* 

This report provides a comprehensive overview of Tesla's financial health and strategic outlook based on the provided financial statements. For further analysis or specific inquiries, additional data may be required.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook. However, it contains several critical gaps in logic, unsupported claims, and missing risk assessments that need to be addressed to enhance its credibility and decision-grade quality.\n\n## Major Logic Gaps\n1. **Inconsistent Liabilities Reporting**: The report states total liabilities as **$2.06 billion**, which contradicts the provided financial statements that indicate total liabilities of **$36.44 billion**. This discrepancy raises questions about the accuracy of the financial analysis.\n2. **Lack of Contextual Analysis**: While the report mentions revenue growth and liquidity, it fails to contextualize these figures against industry benchmarks or historical performance, which is essential for a thorough financial assessment.\n\n## Unsupported or Weakly Supported Claims\n1. **Cash and Cash Equivalents**: The claim that Tesla has **$16.25 billion** in cash and cash equivalents is not adequately supported by the context documents, which may lead to questions about its accuracy.\n2. **Debt Management**: The assertion that total liabilities are manageable is not substantiated with comparative metrics or analysis of industry standards, making it a weak claim.\n\n## Missing Investor Risks\n1. **Valuation Risks**: The report does not address potential valuation risks, especially given Tesla's high market capitalization relative to its earnings, which could be a concern for investors.\n2. **Regulatory Risks**: The impact of changing regulations, particularly in the automotive and energy sectors, is not discussed, which could significantly affect Tesla's operations and profitability.\n\n## Figure and Visualization Issues\n1. **Image URL Issues**: The chart of key financial metrics is linked to a placeholder URL that does not appear to be a valid Supabase-hosted link. This could lead to accessibility issues for readers.\n2. **Missing Metadata**: The report lacks proper metadata for the visualizations, which is essential for understanding the context and source of the data presented.\n\n## Competitor Counterarguments\n1. **Competition**: The report does not address the competitive landscape, particularly how Tesla's market position may be threatened by emerging electric vehicle manufacturers or traditional automakers entering the EV space.\n2. **Cost Management**: Competitors may argue that Tesla's rising costs and decreasing gross margins indicate inefficiencies that could be exploited.\n\n## Revision Priorities\n1. Correct the total liabilities figure to align with the financial statements.\n2. Provide contextual analysis for revenue growth and liquidity against industry benchmarks.\n3. Address missing risks related to valuation and regulation.\n4. Update the chart link to a valid Supabase-hosted URL and include necessary metadata.\n\n## Issues to Resolve\n- [ ] Correct total liabilities figure from **$2.06 billion** to **$36.44 billion**.\n- [ ] Provide contextual analysis for revenue growth and liquidity.\n- [ ] Include discussion on valuation risks.\n- [ ] Address regulatory risks in the report.\n- [ ] Update the chart link to a valid Supabase-hosted URL.\n- [ ] Add necessary metadata for visualizations."
}
