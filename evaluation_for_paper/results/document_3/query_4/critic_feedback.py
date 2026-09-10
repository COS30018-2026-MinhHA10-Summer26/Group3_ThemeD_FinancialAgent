"""Critic Agent Feedback — document_3 / query_4"""
from __future__ import annotations

USER_QUERY = "How did Amazon's subscription services revenue evolve in 2024?"

ADVISOR_REPORT_V1 = """
# Amazon's Subscription Services Revenue Evolution in 2024

⚠️ Subscription services revenue for 2024 was not found in the available documents. This figure cannot be confirmed without the source filing.

To analyze the evolution of Amazon's subscription services revenue in 2024, the specific revenue figure for that segment is needed. Unfortunately, the documents provided do not include this information.

However, it is noteworthy that Amazon's overall revenue grew 11% year-over-year, reaching $638 billion in 2024. This growth was driven by various segments, including North America, International, and AWS, which saw significant increases. The expansion of Prime Video and other subscription offerings suggests that subscription services may have also experienced growth, aligning with the overall positive trend in revenue.

In addition, the continued investment in enhancing customer experiences—such as the introduction of new original shows on Prime Video and improvements in delivery services—indicates a strategic focus on retaining and expanding the subscriber base. This could imply a favorable outlook for subscription services moving forward.

While we cannot provide the exact figures for subscription services, the overall revenue growth and strategic initiatives suggest a potentially positive trajectory for this segment. If you have access to additional documents or data that include the specific revenue figures for Amazon's subscription services, please provide them for a more comprehensive analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report lacks critical data on Amazon's subscription services revenue for 2024, which is essential for a comprehensive analysis. While it provides some context regarding overall revenue growth, it fails to address specific risks and assumptions related to subscription services, making it less decision-grade for investors.\n\n## Major Logic Gaps\n- The report states that subscription services likely experienced growth but does not provide any quantitative data or estimates to support this claim.\n- It mentions strategic initiatives but does not connect these initiatives to measurable outcomes or expected impacts on subscription revenue.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that subscription services may have experienced growth is speculative and lacks supporting evidence or data.\n- The report does not cite any specific figures or trends related to subscription services, making it difficult to assess the validity of the claims.\n\n## Missing Investor Risks\n- The report does not address key risks such as competition, regulatory challenges, and potential margin pressures that could impact subscription services.\n- There is no discussion of the implications of rising costs or changes in consumer behavior on subscription revenue.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations to support its claims, which would enhance understanding and provide context.\n\n## Competitor Counterarguments\n- Competitors may argue that without specific revenue figures, the report lacks credibility and fails to provide a clear picture of Amazon's performance in the subscription segment.\n- The absence of risk analysis may lead competitors to view Amazon as vulnerable to market changes that could affect subscription growth.\n\n## Revision Priorities\n- Include specific revenue figures for subscription services if available, or provide estimates based on historical data or market trends.\n- Address missing risks and provide a more comprehensive analysis of the competitive landscape and potential challenges.\n- Incorporate figures or visualizations to enhance the report's clarity and impact.\n\n## Issues to Resolve\n- [ ] Include specific revenue figures for subscription services for 2024.\n- [ ] Provide estimates or historical data to support claims of growth in subscription services.\n- [ ] Address missing risks related to competition, regulation, and margin pressures.\n- [ ] Incorporate figures or visualizations to support the analysis."
}
