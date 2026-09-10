"""Critic Agent Feedback — document_7 / query_3"""
from __future__ import annotations

USER_QUERY = "What was Tesla's gross margin on automotive sales in 2024 and how did it compare to 2023?"

ADVISOR_REPORT_V1 = """
### Tesla's Gross Margin on Automotive Sales in 2024

In 2024, Tesla's gross margin for total automotive sales was **18.4%**. This represents a decrease from **19.4%** in 2023.

### Comparison of Gross Margin (2024 vs. 2023)

| Year | Gross Margin |
|------|--------------|
| 2024 | 18.4%        |
| 2023 | 19.4%        |

### Summary

- **2024 Gross Margin**: 18.4%
- **2023 Gross Margin**: 19.4%
- **Change**: Decrease of 1.0 percentage points

This decline in gross margin was primarily attributed to lower average selling prices on vehicles and the ramp-up costs associated with the Cybertruck, despite some offset from lower average combined costs per unit and increases in regulatory credit and FSD (Supervised) revenue.

### Financial Health and Future Outlook

Tesla's gross margin decline indicates challenges in maintaining profitability amidst pricing pressures and increased production costs. The company may need to focus on cost management and enhancing operational efficiencies to stabilize margins. 

### Risks and Limitations

Potential risks include fluctuating raw material costs, competition in the electric vehicle market, and the impact of economic conditions on consumer demand. Additionally, the ramp-up of new models like the Cybertruck may involve unforeseen expenses.

### Actionable Advice

To improve gross margins, Tesla should consider strategies such as optimizing supply chain management, exploring cost-effective production techniques, and potentially adjusting pricing strategies to enhance competitiveness without sacrificing profitability.

### Source
Data derived from the Tesla 2024 Annual Report (Form 10-K).
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a clear overview of Tesla's gross margin on automotive sales for 2024 and its comparison to 2023. However, it lacks sufficient context and evidence to support some claims, particularly regarding risks and strategic recommendations. The report needs revisions to enhance its credibility and comprehensiveness.\n\n## Major Logic Gaps\n- The report states that the decline in gross margin was \"primarily attributed\" to lower average selling prices and ramp-up costs for the Cybertruck, but it does not provide specific data or context to quantify these impacts. This weakens the argument and leaves the reader questioning the extent of these factors.\n- The actionable advice section suggests strategies for improving gross margins but does not connect these strategies to the specific challenges identified in the report. This disconnect makes the recommendations feel generic rather than tailored to Tesla's current situation.\n\n## Unsupported or Weakly Supported Claims\n- The claim that the gross margin decline was \"primarily attributed\" to certain factors lacks quantitative backing. The report should include specific figures or percentages to illustrate how much each factor contributed to the margin decline.\n- The mention of \"increases in regulatory credit and FSD (Supervised) revenue\" as offsets to margin decline is vague. The report should specify how much these increases were and their direct impact on gross margin.\n\n## Missing Investor Risks\n- The report fails to address the risk of valuation, which is critical for investors. Given the fluctuations in gross margin and the competitive landscape, understanding how Tesla's valuation might be affected is essential.\n- While the report mentions competition and supply chain risks, it does not elaborate on how these factors could impact Tesla's market position or financial health in the long term.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations to support the data presented. Including charts or graphs could enhance understanding and provide a visual representation of the trends in gross margin over the years.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's reliance on regulatory credits and FSD revenue is a sign of vulnerability, as these sources may not be sustainable in the long term. The report should address this potential criticism by discussing the sustainability of these revenue streams.\n- The report does not consider potential competitive responses to Tesla's pricing strategies, which could further pressure margins. Competitors might capitalize on Tesla's margin decline to gain market share.\n\n## Revision Priorities\n1. Provide quantitative data to support claims about the factors affecting gross margin.\n2. Include a detailed analysis of the risks associated with valuation and how they may impact investor sentiment.\n3. Incorporate visual aids to enhance the presentation of data and trends.\n4. Strengthen the connection between identified challenges and the recommended strategies for improvement.\n\n## Issues to Resolve\n- [ ] Provide specific data or percentages to quantify the impact of lower average selling prices and Cybertruck ramp-up costs on gross margin.\n- [ ] Clarify the contribution of regulatory credit and FSD revenue increases to the gross margin.\n- [ ] Address the missing risk of valuation and its implications for investors.\n- [ ] Include visual representations of gross margin trends to support the analysis.\n- [ ] Discuss the sustainability of revenue sources like regulatory credits and FSD in the context of competitive pressures."
}
