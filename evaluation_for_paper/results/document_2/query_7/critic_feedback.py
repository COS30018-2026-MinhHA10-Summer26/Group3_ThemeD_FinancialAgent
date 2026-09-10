"""Critic Agent Feedback — document_2 / query_7"""
from __future__ import annotations

USER_QUERY = "What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?"

ADVISOR_REPORT_V1 = """
# Amazon 2023 Filing: Primary Risks and Uncertainties

The primary risks and uncertainties disclosed in Amazon's 2023 filing, while not explicitly detailed in a dedicated section, can be inferred from the context of the documents provided. Here are some key areas of concern that Amazon may face:

- **Economic Conditions**: The report mentions that customers are careful about their spending in an uncertain economy, indicating that economic downturns could impact consumer behavior and spending patterns.

- **Market Competition**: Amazon operates in a highly competitive environment, particularly in e-commerce and cloud services. The need to maintain a competitive edge through pricing and selection is emphasized, which suggests ongoing risks from competitors.

- **Operational Challenges**: The documents highlight efforts to optimize costs and improve delivery speeds. However, challenges related to supply chain management and fulfillment capabilities remain significant risks, especially as Amazon continues to expand its operations internationally.

- **Technological Advancements**: The rapid pace of innovation in technology, particularly in cloud services (AWS), poses both opportunities and risks. While advancements like Graviton chips and new AWS services are beneficial, they also require continuous investment and adaptation to stay ahead of competitors.

While these risks are not explicitly labeled as such in the documents, they reflect the broader challenges Amazon faces in its operations and market environment. For a more detailed understanding, it is advisable to consult the official 2023 annual report or SEC filings, particularly sections typically titled "Risk Factors" or "Management's Discussion and Analysis."
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report provides a general overview of the risks and uncertainties faced by Amazon in 2023, but lacks specificity and depth in addressing key risk factors. It does not adequately reference the detailed risk factors outlined in the official filings, which could leave investors and competitors wanting more clarity.\n\n## Major Logic Gaps\n- The report does not explicitly cite the specific sections of the 2023 filing where these risks are discussed, which could lead to confusion about the source of the information.\n- The inference of risks from context without direct citations may weaken the credibility of the claims made in the report.\n\n## Unsupported or Weakly Supported Claims\n- The claims regarding economic conditions and market competition are broad and lack specific examples or data from the filing to support them.\n- The mention of operational challenges and technological advancements is vague and does not provide concrete evidence or references to specific initiatives or outcomes.\n\n## Missing Investor Risks\n- The report fails to address several significant risks that are explicitly mentioned in the 2023 filing, such as regulatory risks, margin pressure, and valuation concerns. These omissions could mislead investors about the comprehensive nature of the risks involved.\n\n## Figure and Visualization Issues\n- There are no figures or visualizations included in the report, which could enhance understanding and provide a clearer picture of the risks discussed.\n\n## Competitor Counterarguments\n- Competitors may argue that the report does not sufficiently address the competitive landscape and the specific strategies Amazon is employing to mitigate these risks. This could be seen as a strategic blind spot.\n\n## Revision Priorities\n- Include specific references to the relevant sections of the 2023 filing to substantiate claims made in the report.\n- Provide concrete examples and data to support claims regarding economic conditions, market competition, operational challenges, and technological advancements.\n- Address the missing risks explicitly mentioned in the filing, such as regulatory risks and margin pressures.\n- Consider including figures or visualizations to enhance clarity and understanding of the risks discussed.\n\n## Issues to Resolve\n- [ ] Cite specific sections of the 2023 filing for each risk mentioned.\n- [ ] Provide concrete examples and data to support claims.\n- [ ] Address missing risks such as regulatory risks and margin pressures.\n- [ ] Include figures or visualizations to enhance clarity."
}
