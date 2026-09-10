"""Critic Agent Feedback — document_7 / query_3"""
from __future__ import annotations

USER_QUERY = "What was Tesla's gross margin on automotive sales in 2024 and how did it compare to 2023?"

ADVISOR_REPORT_V1 = """
# Tesla Automotive Sales Gross Margin Analysis

⚠️ Tesla's gross margin on automotive sales for both 2024 and 2023 was not found in the available documents. This figure cannot be confirmed without the source filing.

To proceed with your analysis, please provide the specific gross margin figures for automotive sales for both years, or any additional documents that may contain this information.

### Financial Health and Outlook
While specific gross margin figures are unavailable, it is essential to consider Tesla's overall financial health and market position. Tesla has shown resilience in the automotive sector, with a growing market share and increasing production capacity. However, potential risks include supply chain disruptions, competition from other electric vehicle manufacturers, and regulatory changes.

### Next Steps
- **Alternative Sources**: Consider checking Tesla's quarterly earnings reports or investor relations website for the latest financial metrics.
- **Further Analysis**: If you obtain the gross margin figures, I can assist in comparing them to industry benchmarks or previous years to assess performance trends.

If you have any additional documents or specific figures, please share them for a more detailed analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report lacks critical financial metrics, specifically the gross margin figures for Tesla's automotive sales in 2024 and 2023. This absence significantly undermines its decision-grade quality for investors. Furthermore, while it discusses Tesla's financial health and risks, it fails to provide actionable advice or a comprehensive analysis of valuation risks, which could be crucial for both investors and competitors.\n\n## Major Logic Gaps\n- The report states that gross margin figures for automotive sales are unavailable, yet it does not provide any alternative sources or methods to obtain this information, leaving a significant gap in the analysis.\n- The discussion on financial health and market position is vague and lacks specific metrics or comparisons to industry benchmarks, which would help contextualize Tesla's performance.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that Tesla has shown resilience in the automotive sector is not backed by specific data or metrics, making it a weak claim.\n- The report mentions potential risks such as supply chain disruptions and competition but does not quantify these risks or provide historical context to support the claims.\n\n## Missing Investor Risks\n- The report fails to address valuation risks, which are critical for investors assessing Tesla's stock price relative to its earnings and growth potential.\n- While it mentions competition and regulatory changes, it does not explore how these factors could impact Tesla's market share or profitability in detail.\n\n## Figure and Visualization Issues\n- The report references figures and charts but does not include any visual representations or links to relevant data, which could enhance understanding and engagement.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of specific gross margin data indicates potential weaknesses in Tesla's pricing strategy or cost management.\n- The absence of a detailed analysis of valuation risks could be seen as a strategic oversight, suggesting that Tesla may not be as insulated from market fluctuations as implied.\n\n## Revision Priorities\n1. **Include Gross Margin Figures**: Obtain and present the gross margin figures for automotive sales in 2024 and 2023 to provide a complete analysis.\n2. **Strengthen Claims with Data**: Support assertions about Tesla's resilience and market position with specific metrics and comparisons to industry benchmarks.\n3. **Address Valuation Risks**: Incorporate a detailed analysis of valuation risks and how they may affect investor sentiment and stock performance.\n4. **Enhance Visuals**: Include relevant figures or charts to support the analysis and improve the report's engagement and clarity.\n\n## Issues to Resolve\n- [ ] [Provide gross margin figures for automotive sales in 2024 and 2023.]\n- [ ] [Support claims about Tesla's resilience with specific data and metrics.]\n- [ ] [Include a detailed analysis of valuation risks.]\n- [ ] [Add visual representations or links to figures discussed in the report.]"
}
