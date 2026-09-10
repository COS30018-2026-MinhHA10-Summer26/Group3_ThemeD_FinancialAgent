"""Critic Agent Feedback — document_5 / query_8"""
from __future__ import annotations

USER_QUERY = "What is Tesla's growth strategy and future product roadmap as outlined in 2022?"

ADVISOR_REPORT_V1 = """
# Tesla's Growth Strategy and Future Product Roadmap (2022)

## Overview
Tesla, Inc. has outlined a comprehensive growth strategy focused on innovation, sustainability, and technological advancement. The company's future product roadmap emphasizes the development of electric vehicles (EVs), autonomous driving technologies, and energy solutions, all aimed at accelerating the world's transition to sustainable energy.

## Key Components of Tesla's Growth Strategy

### 1. **Innovation in Vehicle Technology**
Tesla continues to invest heavily in the development of sophisticated vehicle control and infotainment software. This includes:
- **Self-Driving Development**: Tesla is advancing its Full Self-Driving (FSD) capabilities, utilizing vision-based technologies and neural networks to enhance vehicle autonomy. The company aims to establish an autonomous ride-hailing network, which could significantly expand its customer base.

### 2. **Expansion of Product Offerings**
Tesla is committed to broadening its product lineup, which includes:
- **Electric Vehicles**: The company is focused on producing a range of EVs that cater to different market segments. The introduction of new models is anticipated to attract a wider audience.
- **Robotics**: In 2022, Tesla previewed "Optimus," a humanoid robot controlled by the same AI system used in its vehicles, indicating a diversification into robotics.

### 3. **Strategic Partnerships and Workforce Development**
Tesla emphasizes the importance of a skilled workforce to support its growth:
- **Internship and Apprenticeship Programs**: The company recruits over 3,000 students annually, fostering talent through partnerships with educational institutions.
- **Tesla START Program**: This initiative trains individuals for technician roles, ensuring a steady pipeline of skilled workers.

### 4. **Government Incentives and Market Adaptation**
Tesla is poised to benefit from legislative measures such as the Inflation Reduction Act, which provides tax credits for electric vehicle purchases. This will likely enhance demand for Tesla's products in the U.S. market.

### 5. **Sustainability and Energy Solutions**
Tesla's mission is deeply rooted in sustainability, and the company is exploring various avenues to promote clean energy:
- **Energy Storage Solutions**: Tesla's focus on battery technology and energy storage systems aligns with its goal to provide comprehensive energy solutions alongside its vehicles.

## Financial Health and Outlook
As of June 30, 2022, Tesla's market capitalization was approximately $580.48 billion. However, specific financial metrics such as working capital, total assets, retained earnings, EBIT, total liabilities, and sales are currently unavailable. This lack of data limits the ability to conduct a thorough financial health assessment and risk analysis. 

### Additional Information Required
To conduct a comprehensive financial health assessment, the following metrics are needed:
- Working capital
- Total assets
- Retained earnings
- EBIT
- Total liabilities
- Sales

## Future Product Roadmap
Tesla's future product roadmap includes:
- **Continued Development of FSD Technologies**: Enhancements in autonomous driving capabilities are expected to be rolled out progressively.
- **Expansion of Manufacturing Facilities**: The growth of Gigafactories in various locations will support increased production capacity.
- **Introduction of New Vehicle Models**: Tesla plans to unveil additional models that cater to diverse consumer needs, further solidifying its market position.

## Conclusion
Tesla's growth strategy is characterized by a commitment to innovation, a focus on sustainability, and the development of a skilled workforce. The company's future product roadmap indicates a robust pipeline of technological advancements and new offerings, positioning Tesla as a leader in the electric vehicle and clean energy markets. However, the absence of specific financial metrics necessitates further investigation to fully understand Tesla's financial health and associated risks. Additional context regarding these financial figures is required for a comprehensive analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "# Critique of Tesla's Growth Strategy and Future Product Roadmap (2022)\n\n## Overall Verdict\nThe advisor report provides a solid overview of Tesla's growth strategy and future product roadmap, highlighting key areas such as innovation, product expansion, workforce development, and sustainability. However, it lacks specific financial metrics and a thorough risk analysis, which are crucial for investors to assess the company's financial health and potential challenges.\n\n## Major Logic Gaps\n- The report mentions Tesla's market capitalization but fails to connect this figure to the company's financial health or operational performance. Without context, this number is less meaningful.\n- The discussion on government incentives is relevant but does not address potential risks associated with changes in legislation or market conditions that could impact these incentives.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that Tesla's autonomous ride-hailing network could significantly expand its customer base lacks supporting evidence or data to quantify this potential impact.\n- The report states that Tesla is committed to broadening its product lineup but does not provide specific timelines or details on upcoming models, making this claim vague.\n\n## Missing Investor Risks\n- The report does not adequately address risks related to supply chain disruptions, competition, or regulatory challenges that could impact Tesla's growth strategy.\n- There is no mention of potential market saturation for electric vehicles or the impact of economic downturns on consumer demand.\n\n## Figure and Visualization Issues\n- The report lacks visual aids or figures that could enhance understanding, such as charts showing production capacity, sales forecasts, or market share comparisons with competitors.\n\n## Competitor Counterarguments\n- The report does not consider the competitive landscape adequately. It should address how Tesla's strategies compare to those of other major players in the EV market, such as Ford, GM, and emerging startups.\n- There is no analysis of how Tesla's pricing strategy might be affected by competitors' actions or market trends.\n\n## Revision Priorities\n1. Include specific financial metrics to provide a clearer picture of Tesla's financial health.\n2. Expand on the risks associated with government incentives and market conditions.\n3. Incorporate competitor analysis to contextualize Tesla's strategies within the broader market.\n4. Add visual aids to support claims and enhance the report's clarity.\n\n## Issues to Resolve\n- [ ] Provide specific financial metrics such as working capital, total assets, and EBIT.\n- [ ] Address potential risks related to supply chain and competition.\n- [ ] Include competitor analysis to strengthen the report's context.\n- [ ] Add visual aids to enhance understanding of Tesla's growth strategy and market position."
}
