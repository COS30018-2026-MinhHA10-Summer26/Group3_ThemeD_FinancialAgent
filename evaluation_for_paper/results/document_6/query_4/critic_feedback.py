"""Critic Agent Feedback — document_6 / query_4"""
from __future__ import annotations

USER_QUERY = "How did Tesla's energy storage deployment grow in 2023?"

ADVISOR_REPORT_V1 = """
# Tesla's Energy Storage Deployment Growth in 2023

Tesla's energy storage deployment figures for 2023 were not explicitly found in the available documents. The annual report typically includes insights into operational performance, including segments like energy storage, but specific deployment figures are currently unavailable.

To gather more information on Tesla's energy storage growth in 2023, consider the following avenues:

1. **Official Annual Report**: Review Tesla's complete 10-K filing for the fiscal year ended December 31, 2023, which may contain detailed discussions on energy storage performance and growth metrics.

2. **Press Releases**: Check Tesla's official website for press releases that may highlight milestones or achievements in their energy storage segment throughout 2023.

3. **Investor Relations**: Explore the Investor Relations section of Tesla's website, where they often provide updates, presentations, and earnings call transcripts that may discuss energy storage developments.

4. **Industry Reports**: Look for third-party industry analysis or reports that cover Tesla's energy storage market performance, as these may provide insights and comparative data.

If you have access to additional documents or data, please provide them for further analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report lacks specific deployment figures for Tesla's energy storage in 2023, which is critical for assessing growth. It suggests alternative sources for information but does not provide a comprehensive analysis or insights based on available data.\n\n## Major Logic Gaps\n- The report states that deployment figures are unavailable but does not explore the implications of this lack of data on Tesla's market position or future growth.\n- It fails to connect the importance of energy storage growth to Tesla's overall strategy and financial health.\n\n## Unsupported or Weakly Supported Claims\n- The report does not provide any evidence or context to support the claim that the annual report typically includes insights into operational performance.\n- It suggests checking press releases and investor relations but does not indicate how these sources have historically provided relevant data.\n\n## Missing Investor Risks\n- The report does not address potential risks associated with the lack of deployment data, such as market share loss or competitive disadvantages.\n- It overlooks risks related to supply chain issues, regulatory changes, and competition in the energy storage market.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations to support its claims or provide context for the discussion.\n\n## Competitor Counterarguments\n- The report does not consider how competitors might leverage Tesla's lack of specific deployment data to their advantage.\n- It fails to analyze how Tesla's energy storage growth compares to that of its competitors, which is essential for a comprehensive market analysis.\n\n## Revision Priorities\n- Include specific deployment figures for Tesla's energy storage in 2023 if available.\n- Analyze the implications of the lack of data on Tesla's market position and strategy.\n- Provide evidence or context for claims made regarding the annual report and other sources.\n- Address potential investor risks related to energy storage growth.\n- Incorporate figures or visualizations to enhance the report's clarity and impact.\n\n## Issues to Resolve\n- [ ] Include specific deployment figures for Tesla's energy storage in 2023.\n- [ ] Analyze implications of lack of data on Tesla's market position.\n- [ ] Provide evidence for claims regarding annual report insights.\n- [ ] Address potential investor risks related to energy storage growth.\n- [ ] Incorporate figures or visualizations to support claims."
}
