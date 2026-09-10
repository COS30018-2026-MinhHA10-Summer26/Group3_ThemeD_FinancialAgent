"""Critic Agent Feedback — document_6 / query_3"""
from __future__ import annotations

USER_QUERY = "What were Tesla's total vehicle deliveries and production volumes in 2023?"

ADVISOR_REPORT_V1 = """
# Tesla 2023 Vehicle Deliveries and Production Volumes Report

Unfortunately, the total vehicle deliveries and production volumes for Tesla in 2023 were not found in the available documents. This information is crucial for a comprehensive understanding of Tesla's performance in that year.

To obtain these figures, I recommend checking the following sources:
- Tesla's official website, particularly their Investor Relations section, where they often publish quarterly and annual reports.
- The SEC filings, specifically the Form 10-K for the fiscal year ended December 31, 2023, which may contain detailed operational metrics.
- Financial news outlets that cover Tesla, as they may report on these figures following their release.

If you have access to additional documents or specific reports, please share them, and I can assist further in extracting the required information.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report fails to provide the requested information regarding Tesla's total vehicle deliveries and production volumes for 2023. It lacks critical data that would be essential for investors and stakeholders to assess Tesla's performance. The recommendations for obtaining this information are vague and do not address the immediate need for clarity.\n\n## Major Logic Gaps\n- The report states that the total vehicle deliveries and production volumes were not found in the available documents but does not specify which documents were reviewed or why they were insufficient.\n- The advisor does not provide any context or rationale for why the absence of this data is acceptable or how it impacts the overall assessment of Tesla's performance.\n\n## Unsupported or Weakly Supported Claims\n- The claim that the information is crucial for understanding Tesla's performance is valid, but the report does not substantiate this with any evidence or examples of how this data would influence investor decisions.\n- The recommendation to check Tesla's official website or SEC filings lacks specificity and does not guide the reader on how to find the relevant information effectively.\n\n## Missing Investor Risks\n- The report does not address any potential risks associated with the lack of delivery and production data, such as impacts on investor confidence, stock price volatility, or operational challenges.\n- Key risk areas such as competition, supply chain issues, regulatory changes, and margin pressures are not mentioned, despite being visible in the context documents.\n\n## Figure and Visualization Issues\n- The report mentions the need for data but does not include any figures, charts, or visualizations that could help illustrate Tesla's performance metrics or trends over time.\n- There is a lack of visual aids that could enhance understanding and engagement with the report.\n\n## Competitor Counterarguments\n- Competitors could argue that the absence of this critical data indicates a lack of transparency or operational issues within Tesla.\n- The report does not preemptively address potential competitor claims regarding Tesla's market position or performance, leaving it vulnerable to criticism.\n\n## Revision Priorities\n1. Include specific figures for total vehicle deliveries and production volumes for 2023, sourced from the relevant documents.\n2. Provide a detailed analysis of how these figures impact Tesla's financial health and market position.\n3. Address potential risks associated with the lack of this data and how it could affect investor sentiment.\n4. Incorporate visual aids or figures to support claims and enhance the report's clarity and engagement.\n5. Strengthen the recommendations by providing direct links or specific sections of the documents where the data can be found.\n\n## Issues to Resolve\n- [ ] Include total vehicle deliveries and production volumes for 2023.\n- [ ] Specify which documents were reviewed and why they were insufficient.\n- [ ] Address potential risks associated with the lack of data.\n- [ ] Incorporate relevant figures or visualizations to support claims.\n- [ ] Strengthen recommendations with specific guidance on where to find the data."
}
