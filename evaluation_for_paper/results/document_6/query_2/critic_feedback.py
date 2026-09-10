"""Critic Agent Feedback — document_6 / query_2"""
from __future__ import annotations

USER_QUERY = "How did Tesla's vehicle average selling price and gross margin trend in 2023?"

ADVISOR_REPORT_V1 = """
# Tesla's Vehicle Average Selling Price and Gross Margin Trend in 2023

Unfortunately, Tesla's vehicle average selling price and gross margin for 2023 were not found in the available documents. This information is crucial for analyzing the trends, and without it, we cannot provide a definitive answer regarding the performance in these areas.

## Financial Health and Future Outlook

While specific figures for the average selling price and gross margin are missing, Tesla's overall financial health can be inferred from its market capitalization, which was reported at **$722.52 billion** as of June 30, 2023. This substantial market value suggests strong investor confidence and a robust business model.

### Risks and Limitations

1. **Market Competition**: Tesla faces increasing competition from both established automakers and new entrants in the electric vehicle market, which could impact pricing strategies and margins.
2. **Supply Chain Issues**: Ongoing supply chain disruptions could affect production costs and timelines, potentially impacting gross margins.
3. **Regulatory Changes**: Changes in government policies regarding electric vehicles and emissions could influence market dynamics and operational costs.

## Actionable Insights

- **Monitor Competitor Pricing**: Keeping an eye on competitor pricing strategies will be essential for Tesla to maintain its market position.
- **Focus on Cost Management**: Enhancing operational efficiency and managing production costs can help protect gross margins.
- **Invest in Innovation**: Continued investment in technology and innovation will be crucial for maintaining a competitive edge in the rapidly evolving EV market.

## Conclusion

To analyze the trends in Tesla's vehicle average selling price and gross margin for 2023 accurately, we recommend obtaining the relevant financial data or documents that include these metrics. If you have access to additional sources or specific reports, please share them for a more comprehensive analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks critical data regarding Tesla's vehicle average selling price and gross margin for 2023, which are essential for a comprehensive analysis. While it provides some insights into Tesla's financial health and risks, the absence of specific metrics undermines the report's decision-grade quality.\n\n## Major Logic Gaps\n- The report states that the average selling price and gross margin data were not found, yet it attempts to analyze financial health based solely on market capitalization. This is a logical inconsistency as the core metrics requested are missing.\n- The conclusion suggests obtaining additional data without acknowledging the implications of the missing information on the overall analysis.\n\n## Unsupported or Weakly Supported Claims\n- The claim regarding Tesla's market capitalization of **$722.52 billion** is presented without context or source verification, making it potentially unsupported.\n- The report mentions risks such as market competition and supply chain issues but does not provide specific examples or data to substantiate these claims.\n\n## Missing Investor Risks\n- While the report identifies general risks, it fails to address specific risks related to the missing data on average selling price and gross margin, which are crucial for understanding potential impacts on profitability.\n- The report does not discuss how fluctuations in average selling price could affect demand or market share, which is a significant oversight.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations, despite discussing trends. This absence limits the ability to convey complex information effectively and makes the report less engaging.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of specific financial metrics indicates a weakness in Tesla's pricing strategy or market positioning.\n- The report's focus on general risks without detailed analysis may lead competitors to perceive Tesla as vulnerable to market fluctuations and competitive pressures.\n\n## Revision Priorities\n1. **Include Specific Data**: Obtain and present Tesla's average selling price and gross margin for 2023 to support the analysis.\n2. **Cite Sources**: Ensure all claims, especially regarding financial metrics, are backed by credible sources.\n3. **Enhance Risk Analysis**: Provide a more detailed examination of how missing data impacts investor perception and potential risks.\n4. **Add Visuals**: Incorporate relevant figures or charts to illustrate trends and support the narrative.\n\n## Issues to Resolve\n- [ ] Include Tesla's average selling price and gross margin for 2023.\n- [ ] Verify and cite the source for the market capitalization figure.\n- [ ] Expand on the analysis of risks related to pricing and margins.\n- [ ] Add visual representations of data trends where applicable."
}
