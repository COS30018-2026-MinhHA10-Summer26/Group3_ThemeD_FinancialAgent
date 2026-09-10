"""Critic Agent Feedback — document_6 / query_6"""
from __future__ import annotations

USER_QUERY = "What were the key balance sheet metrics for Tesla at the end of 2023?"

ADVISOR_REPORT_V1 = """
# Tesla 2023 Balance Sheet Metrics Report

Unfortunately, the key balance sheet metrics for Tesla at the end of 2023 were not found in the available documents. The specific figures for the following metrics are missing:

- Total Assets
- Total Liabilities
- Shareholders' Equity
- Current Assets
- Current Liabilities

To obtain this information, I recommend checking Tesla's official financial statements or their 10-K filing for the fiscal year ended December 31, 2023. You may also consider reviewing the SEC's EDGAR database for the most recent filings. If you have access to those documents or any additional resources, please provide them for further analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report fails to provide critical balance sheet metrics for Tesla at the end of 2023, which are essential for investors and stakeholders to assess the company's financial health. The advisor's recommendation to check external sources does not fulfill the request for a comprehensive analysis.\n\n## Major Logic Gaps\n- The report does not present any actual data or figures, which is a significant oversight when discussing balance sheet metrics.\n- The recommendation to check external sources does not address the immediate need for the requested information.\n\n## Unsupported or Weakly Supported Claims\n- The claim that the key balance sheet metrics were not found in the available documents is not substantiated with specific references to the documents that were reviewed.\n- The advisor does not provide any context or rationale for why the metrics are missing or how they could be obtained.\n\n## Missing Investor Risks\n- The report lacks any discussion of potential risks associated with the absence of this financial information, such as implications for investor confidence or market perception.\n- There is no mention of how the missing data could affect Tesla's stock performance or investor decisions.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations, which is a missed opportunity to present data in a more digestible format.\n\n## Competitor Counterarguments\n- Competitors may argue that the lack of transparency regarding financial metrics could indicate underlying issues within Tesla's financial management or operational performance.\n- The absence of key financial data could be leveraged by competitors to question Tesla's market position and stability.\n\n## Revision Priorities\n- Include actual balance sheet metrics for Tesla at the end of 2023, such as total assets, total liabilities, and shareholders' equity.\n- Provide context or references to the documents reviewed to substantiate claims about missing data.\n- Discuss potential risks associated with the absence of this information and its implications for investors.\n- Consider adding visualizations or figures to enhance the presentation of data.\n\n## Issues to Resolve\n- [ ] Include actual balance sheet metrics for Tesla at the end of 2023.\n- [ ] Provide context or references to the documents reviewed.\n- [ ] Discuss potential risks associated with the absence of this information.\n- [ ] Add visualizations or figures to enhance data presentation."
}
