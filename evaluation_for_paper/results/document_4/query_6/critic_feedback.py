"""Critic Agent Feedback — document_4 / query_6"""
from __future__ import annotations

USER_QUERY = "What is Amazon's cash and debt position at the end of fiscal year 2025?"

ADVISOR_REPORT_V1 = """
# Amazon's Cash and Debt Position at the End of Fiscal Year 2025

⚠️ Unfortunately, the cash position and debt position for Amazon at the end of fiscal year 2025 were not found in the available documents. This information is currently unavailable.

To obtain accurate figures regarding Amazon's cash and debt positions, I recommend checking the following sources:
- Amazon's official financial statements or annual report for fiscal year 2025, which should contain the necessary information.
- Financial news websites or databases that track corporate financials, such as Bloomberg, Yahoo Finance, or Reuters, for updated financial metrics.
- The U.S. Securities and Exchange Commission (SEC) filings, where Amazon is required to disclose detailed financial information.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report fails to provide the requested cash and debt position for Amazon at the end of fiscal year 2025. It lacks critical financial data and does not address significant risks associated with the company's financial health, making it inadequate for decision-making purposes.\n\n## Major Logic Gaps\n- The report claims that the cash and debt positions are unavailable but does not utilize the provided context documents that contain this information.\n- There is no analysis or interpretation of the financial data that could have been extracted from the context documents.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that the cash and debt positions are unavailable is unsupported, as the context documents contain relevant financial information.\n- The report does not provide any figures or estimates, which could have been derived from the context documents.\n\n## Missing Investor Risks\n- The report does not address any risks related to competition, valuation, supply chain, regulation, margin pressure, or execution, which are critical for investors to consider.\n- The absence of a risk analysis leaves investors without a comprehensive understanding of potential challenges facing Amazon.\n\n## Figure and Visualization Issues\n- The report mentions figures or charts but does not include any visual representations or links to relevant data, which could enhance understanding and support claims made in the report.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of financial data and risk analysis indicates a lack of transparency or preparedness on Amazon's part.\n- The absence of a detailed financial overview could be seen as a weakness, potentially leading investors to consider alternative investments.\n\n## Revision Priorities\n1. Include specific cash and debt figures for Amazon at the end of fiscal year 2025, derived from the context documents.\n2. Provide a thorough risk analysis that addresses competition, valuation, supply chain, regulation, margin pressure, and execution risks.\n3. Incorporate visual aids or figures to support claims and enhance the report's clarity and impact.\n\n## Issues to Resolve\n- [ ] [Include specific cash and debt figures for Amazon at the end of fiscal year 2025.]\n- [ ] [Add a comprehensive risk analysis covering competition, valuation, supply chain, regulation, margin pressure, and execution.]\n- [ ] [Incorporate visual aids or figures to support claims made in the report.]"
}
