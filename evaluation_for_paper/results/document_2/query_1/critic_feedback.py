"""Critic Agent Feedback — document_2 / query_1"""
from __future__ import annotations

USER_QUERY = "What were Amazon's total revenues and operating income for fiscal year 2023?"

ADVISOR_REPORT_V1 = """
# Amazon Financial Report for Fiscal Year 2023

In fiscal year 2023, Amazon reported the following financial metrics:

- **Total Revenue**: $575 billion
- **Operating Income**: $36.9 billion

These figures reflect a year-over-year growth in total revenue of 12% and a significant improvement in operating income, which increased by 201% compared to the previous year.

## Financial Metrics Comparison

| Metric            | 2023          | 2022          | Change    |
|-------------------|---------------|---------------|-----------|
| Total Revenue     | $575 billion  | $514 billion  | 12% YoY   |
| Operating Income   | $36.9 billion | $12.2 billion | 201% YoY  |

*Source: NASDAQ_AMZN_2023.pdf.*

## Financial Health and Future Outlook

Currently, specific financial health indicators such as debt levels, liquidity ratios, or cash flow metrics for 2023 are unavailable. Additionally, there is no guidance provided by Amazon for 2024 and beyond in the available documents.

## Risks and Limitations

While the report does not detail specific risks, potential limitations that could impact Amazon's future performance include:

- **Market Competition**: Increased competition in e-commerce and cloud services could affect market share and pricing strategies.
- **Economic Conditions**: Economic downturns or changes in consumer spending habits may impact revenue growth.
- **Regulatory Challenges**: Potential regulatory changes in various markets could pose operational challenges.

## Actionable Advice

Given the significant improvement in operating income and total revenue, stakeholders may consider monitoring Amazon's future performance closely, especially in light of potential risks and the competitive landscape in e-commerce and cloud services.

For a more comprehensive analysis, additional information regarding financial health, future outlook, and risks would be beneficial.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides key financial metrics for Amazon's fiscal year 2023, including total revenue and operating income. However, it lacks sufficient detail on financial health indicators, future outlook, and specific risks, which are critical for a comprehensive understanding of the company's performance and potential challenges.\n\n## Major Logic Gaps\n- The report states significant improvements in operating income and total revenue but does not provide context or analysis on how these figures were achieved or their sustainability.\n- There is a lack of discussion on the implications of the reported financial metrics on Amazon's long-term strategy or market position.\n\n## Unsupported or Weakly Supported Claims\n- The total revenue of $575 billion and operating income of $36.9 billion are presented without sufficient evidence or citations from the context documents, raising concerns about their reliability.\n- The report mentions a year-over-year growth of 12% and a 201% increase in operating income but does not explain the factors contributing to these changes.\n\n## Missing Investor Risks\n- The report identifies some risks, such as market competition and regulatory challenges, but fails to address other critical risks visible in the context documents, including:\n  - Valuation risks related to market expectations and stock performance.\n  - Supply chain risks that could impact operational efficiency.\n  - Margin pressure due to rising costs or competitive pricing strategies.\n  - Execution risks associated with scaling operations and managing growth.\n\n## Figure and Visualization Issues\n- The report references a financial metrics comparison table but does not include a visual representation or embed a Markdown image link, which could enhance clarity and engagement for readers.\n\n## Competitor Counterarguments\n- Competitors may argue that the report underestimates the impact of increasing competition in e-commerce and cloud services, which could erode market share and profitability.\n- The lack of detailed risk analysis may lead competitors to perceive Amazon as vulnerable to market fluctuations and regulatory scrutiny.\n\n## Revision Priorities\n1. **Cite Sources**: Include citations for all financial figures to enhance credibility.\n2. **Expand Risk Analysis**: Provide a more comprehensive risk assessment that includes valuation, supply chain, margin pressure, and execution risks.\n3. **Enhance Visuals**: Incorporate visual representations of financial data to improve readability and engagement.\n4. **Contextual Analysis**: Add context to the financial metrics, explaining how they relate to Amazon's overall strategy and market conditions.\n\n## Issues to Resolve\n- [ ] [Cite sources for total revenue and operating income figures.]\n- [ ] [Expand the risk analysis to include valuation, supply chain, margin pressure, and execution risks.]\n- [ ] [Embed visual representations of financial data in the report.]\n- [ ] [Provide contextual analysis of financial metrics in relation to Amazon's strategy.]"
}
