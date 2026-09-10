"""Critic Agent Feedback — document_6 / query_8"""
from __future__ import annotations

USER_QUERY = "What is Tesla's outlook for new vehicle models and production expansion in 2023?"

ADVISOR_REPORT_V1 = """
# Tesla's Outlook for New Vehicle Models and Production Expansion in 2023

The available documents do not provide specific information regarding Tesla's outlook for new vehicle models and production expansion in 2023. Key details such as planned vehicle launches, production targets, or strategic initiatives for the year are not included in the provided context. 

This lack of information presents a limitation in assessing Tesla's future vehicle offerings and production capabilities. 

To gain insights into Tesla's vehicle model plans and production strategies for 2023, I recommend checking the following sources:
- Tesla's official press releases
- Investor relations updates on Tesla's website
- Recent earnings call transcripts
- Industry news articles covering Tesla's developments

These resources are likely to provide the most accurate and up-to-date information regarding Tesla's future vehicle offerings and production capabilities.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks critical information regarding Tesla's outlook for new vehicle models and production expansion in 2023. It fails to address key risks and uncertainties that could impact Tesla's performance, making it insufficient for decision-making by investors or stakeholders.\n\n## Major Logic Gaps\n- The report states that there is no specific information regarding Tesla's outlook for new vehicle models and production expansion, yet it does not provide any context or analysis of why this information is missing or how it affects the overall assessment of Tesla's future.\n- The recommendation to check external sources for information does not provide any actionable insights or analysis based on the available data.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that the available documents do not provide specific information is not substantiated with references to the relevant sections of the context documents that could have been analyzed for insights.\n- The report does not leverage any data from the context documents that could provide a clearer picture of Tesla's production capabilities or strategic initiatives.\n\n## Missing Investor Risks\n- The report fails to address several key risks identified in the context documents, including:\n  - **Competition**: The automotive market is highly competitive, and the report does not discuss how this could impact Tesla's market share or pricing strategies.\n  - **Valuation**: There is no mention of how Tesla's valuation might be affected by market conditions or investor sentiment.\n  - **Supply Chain**: The report does not consider potential supply chain disruptions that could impact production.\n  - **Regulation**: Changes in government incentives or regulations affecting electric vehicles are not discussed.\n  - **Margin Pressure**: The report does not address how pricing strategies or cost increases could affect profit margins.\n\n## Figure and Visualization Issues\n- There are no figures or visualizations included in the report, which limits the ability to present data effectively. The absence of visual aids makes it harder for readers to grasp complex information quickly.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's lack of transparency regarding its production plans and vehicle models could indicate uncertainty or instability in its operations. This could lead to a loss of investor confidence and market share as competitors capitalize on Tesla's weaknesses.\n\n## Revision Priorities\n1. **Incorporate Specific Information**: Include relevant data from the context documents regarding Tesla's production capabilities, planned vehicle launches, and strategic initiatives.\n2. **Address Key Risks**: Discuss the identified risks (competition, valuation, supply chain, regulation, margin pressure) and their potential impact on Tesla's performance.\n3. **Provide Contextual Analysis**: Analyze the implications of missing information and how it affects the overall outlook for Tesla.\n4. **Include Visual Aids**: Consider adding figures or charts to illustrate key points and data trends.\n\n## Issues to Resolve\n- [ ] Provide specific information regarding Tesla's new vehicle models and production expansion plans for 2023.\n- [ ] Address key risks identified in the context documents, including competition, valuation, supply chain, regulation, and margin pressure.\n- [ ] Include contextual analysis of the implications of missing information.\n- [ ] Add visual aids to enhance the clarity and impact of the report."
}
