"""Critic Agent Feedback — document_4 / query_3"""
from __future__ import annotations

USER_QUERY = "What is Amazon's profitability trend and operating margin outlook for 2025?"

ADVISOR_REPORT_V1 = """
# Amazon's Profitability Trend and Operating Margin Outlook for 2025

⚠️ Profitability trend and operating margin outlook for 2025 were not found in the available documents. This figure cannot be confirmed without the source filing.

To provide a comprehensive analysis, I would need specific financial metrics such as revenue, net income, and operating margin figures for Amazon for 2025. If you have access to additional documents or data sources that contain this information, please share them.

### Analysis of Current Context

The documents provide insights into Amazon's strategic initiatives and growth areas, including investments in robotics, rural delivery, and broadband connectivity. However, they do not include specific financial metrics that would allow for a detailed profitability trend analysis or operating margin outlook for 2025.

### Future Outlook

Amazon's ongoing investments in various sectors could positively impact its profitability in the long term. For instance, the expansion of its grocery business and advancements in delivery logistics may enhance revenue streams. However, without concrete financial figures, it is challenging to quantify the expected operating margin for 2025.

### Recommendations

To gain a clearer understanding of Amazon's profitability trend and operating margin outlook for 2025, I recommend obtaining the following financial metrics:
- Revenue projections for 2025
- Expected net income for 2025
- Operating margin figures for 2025

If you can provide additional documents or data sources that contain this information, I would be happy to assist further.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks critical financial metrics necessary for assessing Amazon's profitability trend and operating margin outlook for 2025. While it provides some strategic insights, it fails to address key risks and does not include specific financial data that would allow for a comprehensive analysis.\n\n## Major Logic Gaps\n- The report states that profitability trend and operating margin outlook for 2025 were not found in the available documents, yet it does not provide any alternative sources or suggestions for obtaining this information.\n- The analysis of current context mentions strategic initiatives but does not connect these initiatives to potential financial outcomes or profitability metrics.\n\n## Unsupported or Weakly Supported Claims\n- The report claims that Amazon's ongoing investments could positively impact profitability but does not provide any quantitative evidence or projections to support this assertion.\n- Recommendations for obtaining financial metrics are vague and do not specify how these metrics could be sourced or calculated.\n\n## Missing Investor Risks\n- The report does not address significant risks such as competition, valuation, supply chain issues, or regulatory challenges, which are crucial for investors to consider.\n- While it mentions margin pressure and execution risks, it does not elaborate on how these could impact profitability.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations, which could have helped illustrate the financial trends or strategic initiatives discussed.\n\n## Competitor Counterarguments\n- Competitors may argue that the lack of specific financial metrics indicates a lack of transparency or reliability in Amazon's financial outlook.\n- The absence of a detailed risk analysis could be seen as a strategic blind spot, making the company vulnerable to competitive pressures.\n\n## Revision Priorities\n1. Include specific financial metrics for 2025, such as revenue projections, expected net income, and operating margin figures.\n2. Provide a detailed analysis of risks, including competition, valuation, supply chain, and regulatory challenges.\n3. Incorporate figures or visualizations to support claims and enhance the report's clarity and impact.\n4. Strengthen the connection between strategic initiatives and their potential financial outcomes.\n\n## Issues to Resolve\n- [ ] [Include specific financial metrics for 2025: revenue, net income, operating margin.]\n- [ ] [Address missing risks: competition, valuation, supply chain, regulation.]\n- [ ] [Incorporate figures or visualizations to support claims.]\n- [ ] [Strengthen the connection between strategic initiatives and financial outcomes.]"
}
