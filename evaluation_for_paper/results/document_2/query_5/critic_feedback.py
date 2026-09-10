"""Critic Agent Feedback — document_2 / query_5"""
from __future__ import annotations

USER_QUERY = "What were the key balance sheet highlights for Amazon at the end of 2023?"

ADVISOR_REPORT_V1 = """
# Amazon 2023 Balance Sheet Highlights

At the end of 2023, specific balance sheet figures such as total assets, total liabilities, equity, cash and cash equivalents, and long-term debt are not available in the provided documents. Therefore, we cannot provide the requested balance sheet highlights. 

However, we can highlight some key financial metrics that reflect Amazon's performance:

- **Total Revenue**: Amazon's total revenue grew 12% year-over-year from $514 billion in 2022 to **$575 billion** in 2023.
- **Operating Income**: The operating income saw a significant increase of 201% year-over-year, rising from **$12.2 billion** (with an operating margin of 2.4%) in 2022 to **$36.9 billion** (with an operating margin of 6.4%) in 2023.
- **Free Cash Flow (FCF)**: Amazon's trailing twelve-month FCF adjusted for equipment finance leases improved dramatically from **-$12.8 billion** in 2022 to **$35.5 billion** in 2023, marking an increase of **$48.3 billion**.

### Summary
While we cannot provide specific balance sheet highlights due to the absence of detailed balance sheet data, the substantial growth in revenue, operating income, and free cash flow indicates a strong financial position for Amazon at the end of 2023. For a complete analysis, access to the detailed balance sheet figures would be necessary. If you have access to Amazon's financial statements or balance sheet data for 2023, please provide that information for further analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report on Amazon's 2023 balance sheet highlights lacks critical balance sheet data and fails to address significant risks, making it insufficient for informed decision-making by investors or stakeholders.\n\n## Major Logic Gaps\n- The report states that specific balance sheet figures are not available, yet it does not provide any alternative insights or estimates that could help fill this gap.\n- The conclusion suggests a strong financial position based solely on revenue and cash flow metrics without acknowledging the absence of balance sheet data, which is essential for a complete financial analysis.\n\n## Unsupported or Weakly Supported Claims\n- The report claims significant improvements in free cash flow and operating income but does not provide context or sources for these figures, raising concerns about their reliability.\n- The assertion that Amazon has a strong financial position is made without supporting balance sheet data, which is critical for assessing overall financial health.\n\n## Missing Investor Risks\n- The report does not address any potential risks or downsides, particularly regarding competition, valuation, supply chain issues, or regulatory challenges, which are crucial for investors to consider.\n- There is no mention of execution risks related to Amazon's growth strategies or operational challenges, which could impact future performance.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations to support the claims made, which would enhance understanding and provide a clearer picture of Amazon's financial health.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of balance sheet data indicates potential weaknesses in liquidity or solvency that are not being disclosed.\n- The absence of risk discussion could be leveraged by competitors to highlight their own strengths in risk management and financial transparency.\n\n## Revision Priorities\n1. **Include Balance Sheet Data**: If available, provide key balance sheet figures such as total assets, liabilities, and equity.\n2. **Address Risks**: Incorporate a section discussing potential risks and challenges facing Amazon, including competition and regulatory issues.\n3. **Support Claims with Sources**: Ensure all financial metrics are backed by clear citations from the provided documents.\n4. **Add Visuals**: Consider including charts or graphs that summarize key financial metrics for better clarity and impact.\n\n## Issues to Resolve\n- [ ] [Include specific balance sheet figures if available.]\n- [ ] [Address potential risks and downsides in the report.]\n- [ ] [Cite sources for all financial metrics presented.]\n- [ ] [Incorporate visual aids to enhance understanding of financial data.]"
}
