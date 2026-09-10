"""Critic Agent Feedback — document_1 / query_6"""
from __future__ import annotations

USER_QUERY = "How did Amazon's international segment perform financially in 2022?"

ADVISOR_REPORT_V1 = """
# Amazon's International Segment Performance in 2022

⚠️ The specific financial metrics for Amazon's international segment in 2022, such as international revenue and operating income, were not found in the available documents. This information cannot be confirmed without the source filing.

To analyze Amazon's international segment performance, the following information is needed:
- 2022 international revenue
- 2022 international operating income
- Any additional metrics related to the international segment's performance

Unfortunately, without these critical figures, a comprehensive analysis cannot be provided. If you have access to further documents or can provide this information, I can assist you in analyzing the performance. Alternatively, you may consider reviewing Amazon's official financial statements or investor relations materials for detailed insights into the international segment's performance.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks critical financial metrics and insights regarding Amazon's international segment performance in 2022. It fails to provide essential data such as international revenue and operating income, which are necessary for a comprehensive analysis. The absence of these figures makes the report insufficient for decision-making purposes.\n\n## Major Logic Gaps\n- The report states that specific financial metrics for the international segment were not found, yet it does not attempt to summarize or analyze the available data that could provide context or insights.\n- There is no attempt to discuss the implications of the missing data or how it affects the overall understanding of Amazon's international performance.\n\n## Unsupported or Weakly Supported Claims\n- The claim that a comprehensive analysis cannot be provided without specific figures is valid; however, the report does not explore any alternative metrics or qualitative insights that could still be relevant.\n- The report does not reference any specific figures from the context documents that could have been used to provide a partial analysis.\n\n## Missing Investor Risks\n- The report does not address any potential risks associated with the international segment, such as competition, regulatory challenges, or supply chain issues, which are critical for investors to consider.\n- There is no mention of how macroeconomic factors may have impacted the international segment's performance, which is essential for understanding the broader context.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations, which could have helped illustrate the performance of the international segment or the impact of missing data.\n\n## Competitor Counterarguments\n- Competitors may argue that the lack of detailed financial metrics indicates a weakness in Amazon's international strategy or execution.\n- The absence of risk analysis could lead competitors to perceive Amazon as vulnerable to market fluctuations or regulatory challenges in international markets.\n\n## Revision Priorities\n- Include specific financial metrics for the international segment, such as revenue and operating income, to provide a complete picture.\n- Discuss potential risks and challenges that could affect the international segment's performance.\n- Consider including qualitative insights or alternative metrics that could provide context in the absence of specific figures.\n\n## Issues to Resolve\n- [ ] Include 2022 international revenue and operating income figures.\n- [ ] Analyze the implications of missing financial metrics on overall performance.\n- [ ] Address potential risks related to competition, regulation, and supply chain for the international segment.\n- [ ] Incorporate qualitative insights or alternative metrics to provide context.\n- [ ] Add visualizations or figures to support the analysis."
}
