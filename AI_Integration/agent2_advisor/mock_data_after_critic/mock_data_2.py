"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_2.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

To provide a comprehensive analysis of Tesla's financial health and future outlook, I have reviewed the context documents provided. However, specific financial statements or key financial metrics such as revenue, net income, total assets, or liabilities were not included in the documents. Therefore, I will summarize insights based on the available context regarding Tesla's market position, competition, and regulatory environment.

### Financial Health Insights

1. **Market Position**: Tesla operates in a highly competitive automotive market, particularly in the electric vehicle (EV) segment. The company competes with both established automobile manufacturers and new entrants in the EV space. The introduction of electric vehicles by various manufacturers highlights the growing attractiveness of EVs, which could benefit Tesla as it continues to innovate and expand its product offerings.

2. **Regulatory Environment**: Tesla benefits from various federal, state, and local incentives aimed at promoting renewable energy and electric vehicles. These incentives can enhance Tesla's market position and profitability. However, the regulatory landscape is complex and evolving, particularly concerning self-driving technology and energy storage systems, which may pose challenges in the future.

3. **Production and Supply Chain Challenges**: Tesla has faced challenges related to supply chain disruptions, particularly during the COVID-19 pandemic. These disruptions have impacted production timelines and costs. The company is actively working to mitigate these risks by diversifying its supplier base and investing in its own manufacturing capabilities.

4. **Sustainability and ESG Commitment**: Tesla's commitment to sustainability and reducing carbon emissions aligns with global trends towards renewable energy. This focus not only enhances Tesla's brand image but also positions the company favorably in the eyes of environmentally conscious consumers and investors.

### Future Outlook

- **Growth Potential**: Tesla's expansion into new markets and the introduction of new models, such as the Cybertruck, indicate strong growth potential. The company's ability to scale production efficiently and manage costs will be critical to achieving its growth targets.

- **Technological Advancements**: Continued investment in technology, particularly in battery production and self-driving capabilities, will be essential for maintaining Tesla's competitive edge. The development of proprietary battery cells is a strategic move that could enhance production efficiency and reduce costs.

### Key Financial Metrics Comparison

Unfortunately, due to the lack of specific financial data, I am unable to provide a detailed comparison of key financial metrics for Tesla. Below is a placeholder comparison table that reflects the absence of data:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric            | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :---------------- | :---:      | :---:      | :---:        | :---:      |
| Net Income        | 0.00       | 0.00       | +0.00        | +inf%      |
| Revenue           | 0.00       | 0.00       | +0.00        | +inf%      |
| Total Assets      | 0.00       | 0.00       | +0.00        | +inf%      |
| Total Liabilities | 0.00       | 0.00       | +0.00        | +inf%      |

### Conclusion

In summary, while specific financial metrics are not available for a detailed analysis, Tesla's strong market position, commitment to sustainability, and focus on technological advancements suggest a positive outlook for the company's future. However, challenges related to production, supply chain management, and regulatory compliance will need to be addressed to sustain growth and profitability. 

For a more accurate assessment, I recommend obtaining Tesla's financial statements, including the income statement and balance sheet, for the most recent fiscal year.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a general overview of Tesla's financial health and future outlook but lacks specific financial data and detailed analysis. This absence of key metrics undermines its decision-grade quality for investors and leaves significant gaps for competitors to exploit.\n\n## Major Logic Gaps\n- The report claims to summarize insights based on available context but fails to incorporate specific financial metrics that are crucial for a comprehensive analysis. This creates a disconnect between the stated intent and the actual content.\n- The placeholder comparison table with all zeros is misleading and does not provide any useful information, which detracts from the report's credibility.\n\n## Unsupported or Weakly Supported Claims\n- The report mentions Tesla's strong market position and growth potential without providing quantitative evidence or specific examples to support these claims.\n- The assertion that Tesla's commitment to sustainability enhances its brand image lacks supporting data or context from the financial statements.\n\n## Missing Investor Risks\n- The report does not address valuation risks, which are critical for investors assessing Tesla's stock price relative to its financial performance and market conditions.\n- While supply chain challenges are mentioned, the report does not quantify the potential financial impact of these risks on Tesla's operations or profitability.\n\n## Figure and Visualization Issues\n- The report references a comparison table but does not include any actual figures or visualizations, which diminishes the report's effectiveness in conveying financial insights.\n- The absence of embedded images or charts makes it difficult for readers to visualize the data and trends discussed.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's market position is not as strong as suggested, given the increasing competition in the EV market from established automakers and new entrants.\n- The report's lack of detailed financial metrics could be used by competitors to question Tesla's financial stability and growth prospects.\n\n## Revision Priorities\n1. Include specific financial metrics from the provided context documents to support claims about Tesla's financial health.\n2. Address missing risks, particularly valuation risks, to provide a more balanced view for investors.\n3. Replace the placeholder comparison table with actual data to enhance credibility and usefulness.\n4. Incorporate visualizations or figures to better illustrate key points and data trends.\n\n## Issues to Resolve\n- [ ] Include specific financial metrics to support claims about Tesla's financial health.\n- [ ] Address missing valuation risks in the report.\n- [ ] Replace the placeholder comparison table with actual financial data.\n- [ ] Incorporate visualizations or figures to enhance the report's effectiveness."
}
