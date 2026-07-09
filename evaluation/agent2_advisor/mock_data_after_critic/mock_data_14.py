"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_14.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Overview
Tesla has shown significant growth in its financial performance from 2021 to 2022. The company's net income attributable to common stockholders has increased dramatically, reflecting strong operational performance and market demand for its products.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :--- | :---: | :---: | :---: | :---: |
| Net income attributable to common stockholders | $12,556 million | $5,519 million | +$7,037 million | +127.50% |
| Weighted average shares used in computing net income per share of common stock, basic | 3,130 million | 2,959 million | +171 million | +5.78% |
| Weighted average shares used in computing net income per share of common stock, diluted | 3,475 million | 3,386 million | +89 million | +2.63% |

### Analysis
- **Net Income Growth**: The net income attributable to common stockholders increased by 127.50%, indicating a robust improvement in profitability. This growth can be attributed to increased sales and operational efficiencies.
- **Share Count Increase**: The increase in the weighted average shares used for calculating net income per share (both basic and diluted) suggests that Tesla is managing its equity effectively while still rewarding shareholders with increased earnings.

## Financial Health Assessment
While there is insufficient data to compute the Altman Z-Score for Tesla, the significant increase in net income suggests that Tesla is currently in a strong financial position. Alternative metrics such as the increase in net income and effective management of shares indicate a positive trend in financial health.

## Risk Assessment
Tesla's financial health is bolstered by its strong net income growth; however, potential risks include:
- **Supply Chain Risks**: Dependence on suppliers for critical components could impact production.
- **Market Competition**: The electric vehicle market is becoming increasingly competitive, which may affect future sales.
- **Regulatory Risks**: Changes in government policies regarding electric vehicles and renewable energy could impact operations.

## Future Outlook
Given the current trends in profitability and the increasing demand for electric vehicles and renewable energy solutions, Tesla appears well-positioned for future growth. The company’s investments in production capacity, technology, and market expansion are likely to contribute positively to its financial performance in the coming years.

## Conclusion
Tesla's financial health appears strong based on the substantial growth in net income and effective management of shares. Continued focus on innovation and market expansion will be crucial for sustaining this momentum.

### Chart of Key Financial Metrics
![Tesla Financial Metrics Comparison](https://supabase.io/your_chart_link_here)

*Note: The chart link is a placeholder and should be replaced with the actual link generated from the figure generation tool if applicable.* 

---

This report provides a concise overview of Tesla's financial health and future outlook based on the provided financial statements. If you need further analysis or specific metrics, please provide additional data or context.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report on Tesla's financial health and future outlook provides a solid overview but contains several critical gaps in logic, unsupported claims, and missing risk assessments. These issues need to be addressed to enhance the report's credibility and decision-grade quality.\n\n## Major Logic Gaps\n- The report claims significant growth in net income but does not provide a comprehensive analysis of the factors contributing to this growth. It lacks a detailed breakdown of revenue sources and operational efficiencies.\n- The assessment of Tesla's financial health is overly simplistic, relying solely on net income growth without considering other financial metrics or ratios that could provide a more nuanced view.\n\n## Unsupported or Weakly Supported Claims\n- The report states that Tesla is in a \"strong financial position\" based on net income growth but does not provide sufficient context or comparative metrics (e.g., profit margins, return on equity) to substantiate this claim.\n- The assertion that Tesla is managing its equity effectively is not backed by any specific data or analysis regarding equity financing or share dilution impacts.\n\n## Missing Investor Risks\n- The report fails to address the risk of valuation, which is crucial for investors considering Tesla's high market capitalization relative to its earnings.\n- While supply chain and regulatory risks are mentioned, the report does not explore potential impacts on margins or execution risks, which are critical in the rapidly evolving EV market.\n\n## Figure and Visualization Issues\n- The chart link provided is a placeholder and does not lead to an actual image, which undermines the report's visual credibility.\n- There is no caption or source note for the chart, making it difficult for readers to understand the context or significance of the data presented.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's growth is unsustainable given the increasing competition in the EV market, which the report does not adequately address.\n- The report does not consider potential technological advancements by competitors that could impact Tesla's market share and profitability.\n\n## Revision Priorities\n1. Provide a more detailed analysis of revenue sources and operational efficiencies contributing to net income growth.\n2. Include additional financial metrics and ratios to support claims of strong financial health.\n3. Address the missing risk of valuation and explore potential impacts on margins and execution risks.\n4. Replace the placeholder chart link with an actual image and include a caption or source note for clarity.\n\n## Issues to Resolve\n- [ ] Provide a detailed breakdown of revenue sources and operational efficiencies.\n- [ ] Include additional financial metrics to support claims of financial health.\n- [ ] Address the missing risk of valuation in the report.\n- [ ] Explore potential impacts on margins and execution risks.\n- [ ] Replace the placeholder chart link with an actual image.\n- [ ] Add a caption or source note for the chart."
}
