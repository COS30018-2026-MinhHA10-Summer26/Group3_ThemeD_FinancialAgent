"""Critic Agent Feedback — document_4 / query_1"""
from __future__ import annotations

USER_QUERY = "What were Amazon's key financial results and revenue breakdown for fiscal year 2025?"

ADVISOR_REPORT_V1 = """
# Amazon's Key Financial Results and Revenue Breakdown for Fiscal Year 2025

⚠️ The specific key financial results and revenue breakdown for fiscal year 2025 were not found in the available documents. The documents provided insights into Amazon's strategic initiatives and growth areas, but they do not include detailed financial figures or a revenue breakdown by segment.

For a comprehensive analysis, I recommend checking Amazon's official financial statements or annual reports for fiscal year 2025, which typically include detailed financial results and revenue breakdowns by segment.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report fails to provide the requested key financial results and revenue breakdown for Amazon in fiscal year 2025. Instead, it suggests checking external sources for this information, which undermines its utility as a standalone report.\n\n## Major Logic Gaps\n- The report does not address the specific financial figures or revenue breakdown, which were the primary focus of the user query.\n- It lacks a clear rationale for why the information is missing, which could leave readers confused about the report's reliability.\n\n## Unsupported or Weakly Supported Claims\n- The claim that the documents do not include detailed financial figures or revenue breakdowns is not substantiated with specific references to the relevant documents that do contain this information.\n\n## Missing Investor Risks\n- The report does not discuss any potential risks associated with the lack of financial data, such as the implications for investors or stakeholders who rely on this information for decision-making.\n- There is no mention of competitive risks or market conditions that could affect Amazon's financial performance.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations, which could have enhanced the presentation of the financial data if it were available.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of financial transparency in the report raises concerns about Amazon's financial health and strategic direction.\n- The absence of detailed financial results could be seen as a sign of weakness or instability in Amazon's operations.\n\n## Revision Priorities\n- The advisor should include specific financial results and revenue breakdowns from the provided documents to fulfill the user query.\n- It would be beneficial to provide context around the missing data, explaining why it is not available and suggesting alternative sources for verification.\n- The report should address potential risks associated with the lack of financial data and how it could impact investor decisions.\n\n## Issues to Resolve\n- [ ] Provide specific financial results and revenue breakdowns for fiscal year 2025.\n- [ ] Include references to relevant documents that contain financial data.\n- [ ] Discuss potential risks associated with the lack of financial data.\n- [ ] Enhance the report with figures or visualizations if applicable."
}
