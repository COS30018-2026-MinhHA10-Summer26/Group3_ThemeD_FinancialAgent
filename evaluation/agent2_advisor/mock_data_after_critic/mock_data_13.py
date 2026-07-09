"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_13.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Overview
Tesla, Inc. has shown significant growth in its financial performance from 2021 to 2022. The company's revenue streams from automotive sales, energy generation, and services have all increased substantially, indicating a robust demand for its products and services.

## Key Financial Metrics Comparison

The following table summarizes the key financial metrics for Tesla in 2022 compared to 2021:

| Metric                               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|--------------------------------------|:----------:|:----------:|:------------:|:----------:|
| Automotive regulatory credits         | 1,776.00   | 1,465.00   | +311.00      | +21.23%    |
| Automotive sales                     | 67,210.00  | 44,125.00  | +23,085.00   | +52.32%    |
| Energy generation and storage sales   | 3,376.00   | 2,279.00   | +1,097.00    | +48.14%    |
| Services and other                   | 6,091.00   | 3,802.00   | +2,289.00    | +60.21%    |
| **Total revenues**                   | **81,462.00** | **53,823.00** | **+27,639.00** | **+51.35%** |

### Insights
1. **Automotive Sales Growth**: The automotive sales revenue increased by 52.32%, which is a strong indicator of Tesla's market position and consumer demand. This growth can be attributed to the expanding product lineup and increased production capacity.

2. **Energy Generation and Storage**: The energy segment also saw a significant increase of 48.14%, reflecting Tesla's commitment to diversifying its revenue streams beyond automotive sales.

3. **Services and Other Revenue**: This segment grew by 60.21%, indicating that Tesla is successfully monetizing its after-sales services and related offerings, which can enhance customer loyalty and recurring revenue.

4. **Total Revenue Increase**: Overall, total revenues increased by 51.35%, showcasing Tesla's strong operational performance and market expansion.

## Financial Health Assessment
While the Altman Z-Score could not be computed due to insufficient data, the substantial revenue growth and diversification of income sources suggest that Tesla is in a healthy financial position. Specifically, additional information on liabilities, working capital, and other financial metrics would be necessary for a comprehensive risk assessment.

### Additional Data Needed for Altman Z-Score
To compute the Altman Z-Score, the following financial metrics are required:
- Working Capital
- Total Assets
- Retained Earnings
- EBIT (Earnings Before Interest and Taxes)
- Market Capitalization
- Total Liabilities

## Future Outlook
Tesla's growth trajectory appears promising, driven by:
- **Increased Production Capacity**: Continued investments in manufacturing facilities and technology.
- **Expansion into New Markets**: Ongoing efforts to penetrate international markets and diversify product offerings.
- **Innovation in Energy Solutions**: A focus on renewable energy products and services, aligning with global sustainability trends.

### Recommendations
- **Monitor Market Trends**: Keep an eye on consumer preferences and regulatory changes that may impact sales.
- **Enhance Operational Efficiency**: Focus on reducing costs and improving margins through better supply chain management.
- **Invest in R&D**: Continue to innovate in both automotive and energy sectors to maintain competitive advantage.

## Conclusion
Tesla's financial performance in 2022 demonstrates strong growth and resilience. With strategic investments and a focus on innovation, the company is well-positioned for future success. Further analysis of liabilities and other financial metrics will provide a more detailed understanding of its financial health.

![Key Financial Metrics Comparison](https://supabase.io/your_image_link_here)

*Source: Tesla 2022 Financial Statements (NASDAQ_TSLA_2022.pdf)*

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook. However, it contains several unsupported claims, missing risk assessments, and issues with figures that need to be addressed for it to be considered decision-grade.\n\n## Major Logic Gaps\n1. **Lack of Context for Financial Metrics**: The report presents financial metrics without sufficient context or explanation of their significance. For example, while revenue growth is highlighted, there is no discussion of how this compares to industry averages or competitors.\n2. **Insufficient Risk Analysis**: The report mentions risks but does not adequately address competitive risks, which are crucial for understanding Tesla's market position.\n\n## Unsupported or Weakly Supported Claims\n1. **Revenue Growth Claims**: The report states significant revenue growth but does not provide sources or context for the numbers presented. The flagged numbers are potentially unsupported and should be verified against the provided financial statements.\n2. **Altman Z-Score Calculation**: The report mentions the inability to compute the Altman Z-Score due to insufficient data but does not explain why the available data is inadequate or how it could be supplemented.\n\n## Missing Investor Risks\n1. **Competitive Risks**: The report fails to address competition, which is a critical factor in Tesla's market dynamics. This oversight could mislead investors about the sustainability of Tesla's growth.\n2. **Supply Chain Risks**: While supply chain issues are mentioned, the report does not elaborate on how these could impact future operations or financial performance.\n\n## Figure and Visualization Issues\n1. **Image Storage and Format**: The image link provided does not point to a supported image extension and is not stored in the expected advisor figure folder. This could lead to accessibility issues for readers.\n2. **Lack of Descriptive Captions**: The figure lacks a descriptive caption or source note, which is essential for understanding the context of the data presented.\n\n## Competitor Counterarguments\n1. **Market Positioning**: Competitors may argue that Tesla's growth is not sustainable due to increasing competition in the EV market, which the report does not address.\n2. **Regulatory Risks**: Competitors could highlight that Tesla's reliance on regulatory credits for revenue could be a vulnerability if regulations change.\n\n## Revision Priorities\n1. **Provide Context for Financial Metrics**: Include comparisons to industry benchmarks and competitors to strengthen claims about growth.\n2. **Enhance Risk Analysis**: Address competitive risks and provide a more detailed discussion of supply chain vulnerabilities.\n3. **Verify Financial Data**: Ensure all financial figures are supported by the context documents and clearly labeled as estimates or derived calculations where applicable.\n4. **Fix Figure Issues**: Update the image link to a supported format and ensure it is stored correctly, along with adding captions.\n\n## Issues to Resolve\n- [ ] Provide context for financial metrics and comparisons to industry standards.\n- [ ] Address competitive risks in the analysis.\n- [ ] Elaborate on supply chain vulnerabilities and their potential impact.\n- [ ] Verify and support all financial figures with appropriate citations.\n- [ ] Update the image link to a supported format and ensure proper storage.\n- [ ] Add descriptive captions or source notes for figures."
}
