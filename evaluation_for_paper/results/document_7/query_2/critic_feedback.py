"""Critic Agent Feedback — document_7 / query_2"""
from __future__ import annotations

USER_QUERY = "How did Tesla's vehicle delivery volumes and production change in 2024?"

ADVISOR_REPORT_V1 = """
# Tesla's Vehicle Delivery Volumes and Production Changes in 2024

Unfortunately, the available documents do not provide specific figures regarding Tesla's vehicle delivery volumes and production changes for 2024. This information is crucial for understanding how Tesla's performance evolved during the year.

### Implications of Missing Data
The absence of delivery and production figures limits our ability to assess Tesla's operational efficiency, market demand, and overall growth trajectory in 2024. Without this data, stakeholders may find it challenging to make informed decisions regarding investments or strategic planning related to Tesla.

### Next Steps
To obtain the relevant data, you may consider the following options:
1. **Check Tesla's Official Website**: Tesla often publishes quarterly and annual reports on their investor relations page, which may contain the necessary figures.
2. **Review Financial News Sources**: Financial news websites and platforms like Bloomberg, Reuters, or CNBC may report on Tesla's performance and provide insights into their delivery and production numbers.
3. **Consult SEC Filings**: The U.S. Securities and Exchange Commission (SEC) website allows you to search for Tesla's filings, which may include detailed financial information.

If you have access to specific documents or reports that might contain this data, please share them for further analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report lacks critical data regarding Tesla's vehicle delivery volumes and production changes for 2024, which are essential for stakeholders to make informed decisions. The absence of this information significantly undermines the report's value and credibility.\n\n## Major Logic Gaps\n- The report states that the necessary figures are not available, yet it does not explore the implications of this absence on Tesla's operational performance or market position.\n- The report suggests checking external sources for data but fails to provide a clear rationale for why the report itself cannot include this information.\n\n## Unsupported or Weakly Supported Claims\n- The claim that stakeholders may find it challenging to make informed decisions due to missing data is valid but lacks supporting evidence or examples of how this could impact investment or strategic planning.\n- The recommendations to check Tesla's official website or financial news sources are generic and do not provide specific guidance on what to look for or how to interpret that data.\n\n## Missing Investor Risks\n- The report does not address several key risks that are visible in the context documents, including:\n  - **Competition**: The automotive market is becoming increasingly competitive, and the report fails to discuss how this could affect Tesla's market share.\n  - **Valuation**: There is no mention of how changes in production and delivery volumes could impact Tesla's valuation.\n  - **Supply Chain**: The report does not consider potential supply chain disruptions that could affect production.\n  - **Regulation**: The impact of changing regulations on Tesla's operations is not discussed.\n  - **Margin Pressure**: The report does not address how lower vehicle prices and production costs could affect profit margins.\n\n## Figure and Visualization Issues\n- The report mentions the need for figures but does not include any visualizations or links to relevant charts, which could enhance understanding and provide context for the data discussed.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of specific delivery and production data indicates a lack of transparency or operational challenges within Tesla.\n- The absence of a discussion on competitive pressures may lead investors to question Tesla's market strategy and resilience against emerging competitors.\n\n## Revision Priorities\n1. **Include Specific Data**: Incorporate Tesla's actual vehicle delivery volumes and production figures for 2024 to provide a complete picture.\n2. **Analyze Implications**: Discuss the implications of missing data on operational efficiency, market demand, and growth trajectory.\n3. **Address Risks**: Include a comprehensive analysis of risks related to competition, valuation, supply chain, regulation, and margin pressure.\n4. **Visualize Data**: Add relevant figures or charts to support claims and enhance the report's clarity and engagement.\n\n## Issues to Resolve\n- [ ] Include specific figures for Tesla's vehicle delivery volumes and production changes in 2024.\n- [ ] Analyze the implications of missing data on operational performance and market position.\n- [ ] Address key investor risks, including competition, valuation, supply chain, regulation, and margin pressure.\n- [ ] Add relevant figures or visualizations to support claims made in the report."
}
