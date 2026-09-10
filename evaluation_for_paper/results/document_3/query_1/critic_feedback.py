"""Critic Agent Feedback — document_3 / query_1"""
from __future__ import annotations

USER_QUERY = "What were Amazon's total net sales and earnings per share for fiscal year 2024?"

ADVISOR_REPORT_V1 = """
# Amazon Fiscal Year 2024 Financial Metrics Report

⚠️ Total net sales and earnings per share for fiscal year 2024 were not found in the available documents. These figures cannot be confirmed without the source filing.

The documents indicate that Amazon's total revenue for 2024 was $638 billion, reflecting an 11% year-over-year growth. However, specific figures for total net sales and earnings per share are not provided.

To obtain accurate financial metrics, I recommend checking Amazon's official financial statements or their annual report for the fiscal year 2024. You can find this information on Amazon's [Investor Relations website](https://ir.aboutamazon.com/) or through their SEC filings.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report lacks critical financial metrics, specifically total net sales and earnings per share for fiscal year 2024, which are essential for investors and stakeholders. The absence of these figures significantly undermines the report's decision-grade quality. Additionally, it fails to address key risks that could impact Amazon's financial performance.\n\n## Major Logic Gaps\n- The report states that total net sales and earnings per share were not found, yet it claims total revenue of $638 billion without providing a clear source or context for this figure.\n- The recommendation to check Amazon's official financial statements is vague and does not guide the reader on how to find the specific information needed.\n\n## Unsupported or Weakly Supported Claims\n- The claim of total revenue being $638 billion is presented without sufficient evidence or citation from the context documents, making it potentially unsupported.\n- The report does not provide any figures for earnings per share, which is a critical metric for assessing company performance.\n\n## Missing Investor Risks\n- The report fails to address significant risks such as competition, valuation, supply chain issues, regulatory challenges, margin pressure, and execution risks, all of which are visible in the context documents but not discussed in the report.\n- The absence of a risk assessment leaves investors without a comprehensive understanding of potential challenges facing Amazon.\n\n## Figure and Visualization Issues\n- The report mentions figures but does not include any visual representations or charts to support the data discussed. This lack of visual aids can make it harder for readers to grasp the financial metrics effectively.\n\n## Competitor Counterarguments\n- Competitors may leverage the report's omission of critical financial metrics and risk factors to question Amazon's transparency and reliability.\n- The lack of discussion on competitive risks could be seen as a strategic blind spot, allowing competitors to capitalize on Amazon's vulnerabilities.\n\n## Revision Priorities\n1. Include total net sales and earnings per share for fiscal year 2024 with proper citations from the context documents.\n2. Address missing risks that could impact Amazon's financial health, including competition and regulatory challenges.\n3. Provide visual representations of key financial metrics to enhance clarity and engagement.\n4. Clarify the source of the $638 billion revenue figure to ensure it is supported by the context documents.\n\n## Issues to Resolve\n- [ ] [Include total net sales and earnings per share for fiscal year 2024 with citations.]\n- [ ] [Address missing risks such as competition, valuation, and regulation.]\n- [ ] [Add visual representations of key financial metrics.]\n- [ ] [Clarify the source of the $638 billion revenue figure.]"
}
