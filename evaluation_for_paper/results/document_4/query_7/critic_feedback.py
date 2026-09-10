"""Critic Agent Feedback — document_4 / query_7"""
from __future__ import annotations

USER_QUERY = "How did Amazon's Prime membership and subscription services perform in 2025?"

ADVISOR_REPORT_V1 = """
# Amazon's Prime Membership and Subscription Services Performance in 2025

The available documents do not provide specific financial figures or metrics directly related to Amazon's Prime membership and subscription services performance in 2025. However, there are some relevant insights regarding Amazon's overall business strategies and developments that may impact these services:

1. **Grocery Business Growth**: Amazon's grocery business has grown significantly, reaching over $150 billion in gross sales in 2025. This growth includes the integration of perishables into their Same-Day Delivery network, which has resonated well with customers. This expansion could potentially enhance the value proposition of Prime membership, especially for customers interested in grocery delivery.

2. **Same-Day Delivery Initiatives**: Amazon has introduced Same-Day Fulfillment Centers and is expanding its delivery capabilities, which may improve the overall customer experience for Prime members. The introduction of ultra-fast delivery services, such as Amazon Now, has reportedly increased shopping frequency among Prime members.

3. **Customer Engagement**: The documents indicate that Prime members have tripled their shopping frequency after using the Amazon Now service, suggesting that enhancements in delivery speed and service offerings are positively influencing customer engagement.

Unfortunately, specific metrics such as Prime membership revenue, subscription services revenue, growth rate of Prime membership, and the total number of Prime members in 2025 are not available in the provided documents.

Given the absence of detailed data, I recommend consulting additional sources or documents that may contain the needed information, such as Amazon's official financial statements or investor presentations for 2025. If you have access to such documents, please share them for a more comprehensive analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report lacks specific financial metrics and detailed insights into Amazon's Prime membership and subscription services performance in 2025. While it highlights relevant business strategies and developments, it fails to provide a comprehensive analysis that would be valuable for investors or stakeholders.\n\n## Major Logic Gaps\n- The report does not connect the growth in the grocery business and same-day delivery initiatives directly to Prime membership performance, leaving a gap in understanding how these factors specifically impact subscription services.\n- There is an assumption that increased shopping frequency among Prime members will lead to higher revenue without providing supporting data or projections.\n\n## Unsupported or Weakly Supported Claims\n- The claim that the grocery business growth could enhance the value proposition of Prime membership is not substantiated with data on how many new members were attracted or retained due to these initiatives.\n- The assertion that Prime members tripled their shopping frequency lacks context regarding the overall impact on revenue or membership growth.\n\n## Missing Investor Risks\n- The report does not address potential risks related to competition in the grocery and delivery sectors, which could impact Prime membership growth.\n- There is no mention of regulatory risks that could affect Amazon's delivery services or grocery business.\n- The report fails to discuss the potential for margin pressure due to increased operational costs associated with expanding delivery capabilities.\n\n## Figure and Visualization Issues\n- The report mentions significant figures (e.g., $150 billion in grocery sales) but does not provide any visual representation or context for these numbers, making it harder for readers to grasp their significance.\n\n## Competitor Counterarguments\n- Competitors could argue that Amazon's growth in grocery and delivery does not guarantee sustained growth in Prime memberships, especially if they can offer similar services at competitive prices.\n- There is a risk that competitors may innovate faster in delivery services, potentially eroding Amazon's market share.\n\n## Revision Priorities\n- Include specific financial metrics related to Prime membership and subscription services.\n- Provide a clearer connection between business initiatives and their impact on Prime membership performance.\n- Address potential risks and competitive pressures that could affect future growth.\n- Consider adding visual aids to support key figures and claims.\n\n## Issues to Resolve\n- [ ] Include specific financial metrics related to Prime membership performance.\n- [ ] Strengthen connections between business initiatives and Prime membership impact.\n- [ ] Address potential risks and competitive pressures.\n- [ ] Add visual aids to support key figures."
}
