"""Critic Agent Feedback — document_7 / query_4"""
from __future__ import annotations

USER_QUERY = "How did Tesla's Full Self-Driving and AI initiatives progress in 2024?"

ADVISOR_REPORT_V1 = """
# Tesla's Full Self-Driving and AI Initiatives Progress in 2024

The available documents do not provide specific details or milestones regarding Tesla's Full Self-Driving (FSD) and AI initiatives progress in 2024. However, there are some relevant insights that can be inferred:

1. **Ongoing Development**: Tesla continues to develop its Full Self-Driving technology, emphasizing improved safety. This suggests that advancements in FSD are a priority for the company, although specific updates or milestones for 2024 are not detailed in the documents.

2. **Product Integration**: The documents mention Tesla's plans to leverage developments in FSD features, including the introduction of a purpose-built Robotaxi product, the Cybercab. This indicates that Tesla is actively working on integrating FSD capabilities into new vehicle models.

3. **Market Expansion**: Tesla's entry into the consumer pickup truck market with the Cybertruck and the ongoing production of the Tesla Semi also reflect the company's broader strategy to enhance its vehicle lineup, potentially incorporating FSD technology across various models.

### Missing Information
It is important to note that specific information regarding Tesla's FSD and AI initiatives in 2024 is missing from the documents. This includes concrete updates, financial health, future outlook, risks or limitations, and actionable advice related to these initiatives.

For a more comprehensive understanding of Tesla's FSD and AI initiatives in 2024, I recommend checking Tesla's official communications, such as press releases, updates in their quarterly earnings calls, or the upcoming Proxy Statement for the 2025 Annual Meeting of Stockholders. These sources often contain insights into technological advancements and project statuses that may not be fully captured in the annual report.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks specific details and concrete evidence regarding Tesla's Full Self-Driving (FSD) and AI initiatives in 2024. While it identifies some ongoing developments, it fails to address critical risks and competitive factors that could impact investor decisions. The report is not decision-grade as it stands.\n\n## Major Logic Gaps\n- The report states that Tesla is \"continuing to develop\" its FSD technology but does not provide any specific milestones or achievements for 2024. This vague assertion does not support a clear understanding of progress.\n- The mention of the Cybercab as a product leveraging FSD capabilities is noted, but there is no discussion on its expected launch timeline or market readiness, which is crucial for assessing its impact.\n\n## Unsupported or Weakly Supported Claims\n- The report claims that advancements in FSD are a priority for Tesla but does not cite any specific evidence or data to substantiate this claim.\n- The assertion that Tesla is actively working on integrating FSD capabilities into new vehicle models lacks supporting details, such as timelines or expected outcomes.\n\n## Missing Investor Risks\n- **Competition**: The report does not address the competitive landscape for FSD technology, which is critical given the increasing number of players in the autonomous vehicle market.\n- **Supply Chain Risks**: There is no mention of potential supply chain issues that could affect the development and rollout of FSD technology.\n- **Regulatory Risks**: The report fails to discuss the evolving regulatory environment surrounding self-driving vehicles, which could significantly impact Tesla's FSD initiatives.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations that could help illustrate Tesla's progress or strategy regarding FSD and AI initiatives. Including such visuals could enhance understanding and engagement.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's lack of specific milestones and failure to address competitive and regulatory risks indicate a lack of preparedness in the FSD space. This could undermine investor confidence.\n- The absence of detailed comparisons with competitors' advancements in FSD technology could be seen as a strategic blind spot.\n\n## Revision Priorities\n1. Include specific milestones or achievements related to FSD and AI initiatives for 2024.\n2. Address competitive risks and how Tesla plans to maintain its edge in the FSD market.\n3. Discuss supply chain and regulatory risks that could impact FSD development and deployment.\n4. Consider adding figures or visualizations to support claims and enhance clarity.\n\n## Issues to Resolve\n- [ ] Provide specific milestones or achievements for Tesla's FSD initiatives in 2024.\n- [ ] Address competitive risks in the FSD market.\n- [ ] Discuss supply chain risks related to FSD technology development.\n- [ ] Include regulatory risks impacting FSD initiatives.\n- [ ] Add figures or visualizations to support claims made in the report."
}
