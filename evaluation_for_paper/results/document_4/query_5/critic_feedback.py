"""Critic Agent Feedback — document_4 / query_5"""
from __future__ import annotations

USER_QUERY = "How did macroeconomic conditions affect Amazon's business in 2025?"

ADVISOR_REPORT_V1 = """
# Amazon's Business Impact from Macroeconomic Conditions in 2025

To analyze how macroeconomic conditions affected Amazon's business in 2025, we can utilize the PESTEL framework, which considers various external factors. However, specific macroeconomic data for 2025, such as inflation rates, interest rates, and consumer spending trends, were not found in the provided documents. This information is crucial for a comprehensive analysis.

### PESTEL Analysis of Amazon in 2025

#### Political
- **Government Policies:** Amazon may have benefited from supportive government policies and tax incentives aimed at promoting technology and infrastructure development, which could enhance its logistics and delivery capabilities.

#### Economic
- **Inflation and Interest Rates:** The impact of inflation on consumer purchasing power and interest rates on borrowing costs could significantly influence Amazon's sales and operational costs. However, specific figures for 2025 were not available.

#### Social
- **Consumer Trends:** There is a growing trend toward sustainable living and convenience in shopping, which Amazon has capitalized on through its grocery and delivery services.

#### Technological
- **Innovation:** Amazon's investments in robotics and satellite technology (Amazon Leo) indicate a strong focus on technological advancements to improve service delivery and customer experience.

#### Environmental
- **Sustainability Efforts:** Amazon's initiatives to reduce carbon emissions and enhance sustainability in its operations may align with increasing consumer demand for environmentally friendly practices.

#### Legal
- **Regulatory Compliance:** Amazon must navigate various legal challenges, including data privacy laws and regulations affecting its logistics and delivery services.

### Conclusion
While the PESTEL framework provides a structured way to analyze external factors affecting Amazon, the lack of specific macroeconomic data for 2025 limits the depth of this analysis. To fully understand the impact of macroeconomic conditions on Amazon's business in 2025, further information on inflation, interest rates, and consumer spending trends would be necessary.

### Actionable Insights
- **Monitor Economic Indicators:** Keeping an eye on inflation rates and consumer spending trends can help Amazon adjust its pricing strategies and inventory management.
- **Leverage Technological Investments:** Continued investment in technology, such as robotics and satellite networks, can enhance operational efficiency and customer satisfaction, particularly in logistics and delivery.
- **Focus on Sustainability:** As consumer preferences shift towards sustainable practices, Amazon should continue to innovate in this area to maintain competitive advantage and meet customer expectations. 

### Note
Due to the unavailability of specific macroeconomic data and financial figures from the provided documents, this report may not fully capture the nuances of how macroeconomic conditions specifically impacted Amazon's business in 2025. Further research and data collection are recommended for a more comprehensive analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report lacks critical macroeconomic data and fails to address significant risks that could impact Amazon's business in 2025. While it provides some actionable insights, the absence of specific financial metrics and risk assessments makes it less robust for decision-making.\n\n## Major Logic Gaps\n- The report does not provide specific macroeconomic data such as inflation rates, interest rates, or consumer spending trends for 2025, which are essential for a comprehensive analysis.\n- The PESTEL analysis is superficial and does not delve into how each factor quantitatively affects Amazon's performance.\n\n## Unsupported or Weakly Supported Claims\n- The report claims that Amazon may have benefited from government policies and tax incentives but does not provide evidence or specific examples to support this assertion.\n- The discussion on inflation and interest rates lacks specific figures or context, making it difficult to assess their impact on Amazon's operations.\n\n## Missing Investor Risks\n- The report does not address key risks such as competition, valuation, supply chain issues, and margin pressure, which are critical for investors to understand the potential downsides of Amazon's business in 2025.\n- While regulatory compliance is mentioned, the implications of potential legal challenges are not explored in depth.\n\n## Figure and Visualization Issues\n- The report references a chart or figure but does not include any visual representation or Markdown image link, which could enhance understanding and engagement.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of specific macroeconomic data and risk assessments indicates a lack of preparedness for potential market challenges.\n- The absence of detailed analysis on competitive pressures could be seen as a strategic blind spot, especially in a rapidly evolving e-commerce landscape.\n\n## Revision Priorities\n1. **Include Specific Macroeconomic Data**: Add relevant inflation rates, interest rates, and consumer spending trends for 2025 to strengthen the analysis.\n2. **Expand on Risks**: Address missing risks such as competition, valuation, supply chain issues, and margin pressure to provide a more balanced view.\n3. **Enhance PESTEL Analysis**: Provide quantitative assessments of how each PESTEL factor impacts Amazon's business.\n4. **Add Visuals**: Include relevant charts or figures to support claims and enhance the report's engagement.\n5. **Cite Evidence**: Support claims with specific examples or data from the provided documents.\n\n## Issues to Resolve\n- [ ] Include specific macroeconomic data for 2025 (inflation rates, interest rates, consumer spending).\n- [ ] Address missing risks: competition, valuation, supply chain issues, margin pressure.\n- [ ] Expand the PESTEL analysis with quantitative assessments.\n- [ ] Add relevant charts or figures to support claims.\n- [ ] Provide citations or evidence for claims made in the report."
}
