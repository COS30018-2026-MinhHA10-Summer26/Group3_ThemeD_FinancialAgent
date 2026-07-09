"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_15.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Financial Health Overview

Tesla's financial health can be assessed through various metrics, including cash reserves, sales performance, and overall asset management. Based on the latest financial statements, here are some key observations:

1. **Cash and Cash Equivalents**: As of December 31, 2022, Tesla reported cash and cash equivalents of $16.25 billion, a decrease of approximately 7.53% from $17.58 billion in 2021. This decline may indicate a need for careful cash management, especially in light of ongoing investments and operational costs.

2. **Sales and Revenue**: The sales figures were not explicitly provided in the financial statements, making it difficult to assess revenue generation accurately. The lack of data suggests potential stagnation or lack of growth, which could be a concern for future profitability and operational expansion.

3. **Total Assets and Liabilities**: Unfortunately, the total assets and liabilities data were not provided in the financial statements, making it difficult to assess the overall leverage and financial stability of the company.

## Risks and Limitations

- **Market Dependency**: Tesla's performance is heavily reliant on the automotive market and the demand for electric vehicles (EVs). Any downturn in consumer interest or economic conditions could adversely affect sales.
  
- **Supply Chain Issues**: The company faces risks related to supply chain disruptions, particularly with single-source suppliers. This could impact production timelines and costs.

- **Regulatory Changes**: Changes in government incentives for EVs and renewable energy could significantly impact Tesla's financial performance. The recent Inflation Reduction Act (IRA) may provide some benefits, but ongoing evaluation is necessary.

## Future Outlook

Tesla's future outlook appears cautiously optimistic, provided it can navigate the aforementioned risks effectively. The company's commitment to innovation and expansion into new markets, such as energy storage and solar products, may offer additional revenue streams. However, maintaining strong cash reserves and managing operational costs will be crucial for sustaining growth.

## Key Financial Metrics Comparison

Below is a comparison of key financial metrics between Tesla for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------------|:----------:|:----------:|:------------:|:----------:|
| Cash and cash equivalents   | 16,253.00  | 17,576.00  | -1,323.00    | -7.53%     |
| Sales                      | N/A        | N/A        | N/A          | N/A        |
| Total Assets               | N/A        | N/A        | N/A          | N/A        |
| Total Liabilities          | N/A        | N/A        | N/A          | N/A        |

*Note: Sales, Total Assets, and Total Liabilities data were not provided in the financial statements.*

## Conclusion

In summary, while Tesla shows a solid cash position, the decline in cash reserves and the lack of sales figures raise concerns about its financial health. The company must focus on improving revenue generation and managing risks associated with market dependency and supply chain issues to ensure a sustainable future. Further analysis and data would be beneficial for a more comprehensive assessment.

### Actionable Recommendations
- **Enhance Revenue Streams**: Explore new markets and product lines to diversify revenue sources.
- **Strengthen Cash Management**: Implement tighter controls on cash flow and operational expenses to mitigate the decline in cash reserves.
- **Monitor Supply Chain**: Develop alternative supplier relationships to reduce dependency on single-source suppliers and enhance resilience against disruptions.
- **Stay Informed on Regulations**: Continuously evaluate the impact of government policies and incentives on the business model and adjust strategies accordingly.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report on Tesla's financial health and future outlook presents some relevant information but suffers from significant gaps in data and analysis. The lack of critical financial metrics and unsupported claims raises concerns about its reliability for decision-making.\n\n## Major Logic Gaps\n1. **Missing Financial Data**: The report claims to assess financial health but fails to provide key figures such as total assets and liabilities, which are essential for understanding leverage and stability.\n2. **Inconsistent Revenue Analysis**: The report mentions a decline in cash reserves but does not correlate this with the reported total revenues of $81,462 million, which could provide context for the cash position.\n\n## Unsupported or Weakly Supported Claims\n1. **Cash Management Concerns**: The assertion that the decline in cash reserves indicates a need for careful cash management is not substantiated with comparative analysis or context regarding operational costs.\n2. **Sales Figures**: The report states that sales figures were not provided, yet it fails to mention that total revenues were reported as $81,462 million, which contradicts the claim of a lack of data.\n\n## Missing Investor Risks\n1. **Competitive Landscape**: The report does not address competition, which is a critical risk factor for Tesla, especially in the rapidly evolving EV market.\n2. **Margin Pressure**: There is no discussion of potential margin pressures due to rising costs or pricing strategies, which could impact profitability.\n\n## Figure and Visualization Issues\n- The report references a comparison table but does not include any visual representation or embedded figures, which could enhance understanding and engagement.\n\n## Competitor Counterarguments\n1. **Market Dependency**: Competitors may argue that Tesla's reliance on the automotive market is a significant vulnerability, especially as new entrants emerge.\n2. **Supply Chain Risks**: While the report mentions supply chain issues, it does not explore how competitors might be better positioned to mitigate these risks.\n\n## Revision Priorities\n1. **Include Key Financial Metrics**: Ensure that total assets, liabilities, and revenue figures are clearly presented and analyzed.\n2. **Strengthen Risk Analysis**: Incorporate a discussion on competition and margin pressures to provide a more comprehensive risk assessment.\n3. **Enhance Visuals**: Add relevant figures or charts to support the analysis and improve clarity.\n\n## Issues to Resolve\n- [ ] Include total assets and liabilities in the financial health assessment.\n- [ ] Clarify the relationship between cash reserves and total revenues.\n- [ ] Address competitive risks in the automotive market.\n- [ ] Discuss potential margin pressures affecting profitability.\n- [ ] Embed relevant figures or charts to support the analysis."
}
