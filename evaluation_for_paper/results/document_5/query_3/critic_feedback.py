"""Critic Agent Feedback — document_5 / query_3"""
from __future__ import annotations

USER_QUERY = "What were the key financial ratios and margins for Tesla in 2022?"

ADVISOR_REPORT_V1 = """
# Tesla 2022 Financial Ratios and Margins Report

Unfortunately, key financial ratios and margins for Tesla in 2022 were not found in the available documents. The specific financial metrics necessary for calculating these ratios, such as net income, total revenue, total assets, and total liabilities, are not included in the provided context.

To provide a complete analysis, I would need access to Tesla's financial statements or reports that include these details. If you have access to such documents, please share them for further analysis.

### Actionable Insights
- **Recommendation**: Review Tesla's official financial statements or the 10-K filing for 2022 to obtain the necessary metrics for a comprehensive financial analysis.
- **Future Outlook**: Monitoring Tesla's performance in upcoming quarters will provide insights into its financial health and operational efficiency, which can be compared against industry benchmarks once the relevant data is available.

### Missing Financial Metrics
The following specific financial figures are needed to calculate key financial ratios and margins:
- Net Income
- Total Revenue
- Total Assets
- Total Liabilities

If you can provide these figures or direct me to where they can be found, I can assist you further in analyzing Tesla's financial performance for 2022.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks critical financial data and fails to address significant risks associated with Tesla's financial performance in 2022. It does not provide the necessary financial ratios and margins, which are essential for a comprehensive analysis. The recommendations are vague and do not offer actionable insights based on the available data.\n\n## Major Logic Gaps\n- The report states that key financial ratios and margins were not found in the available documents, yet the context documents contain relevant financial data, including revenue, net income, and total assets.\n- The advisor's conclusion that further documents are needed is misleading, as the necessary figures are present in the provided context.\n\n## Unsupported or Weakly Supported Claims\n- The claim that \"key financial ratios and margins for Tesla in 2022 were not found\" is unsupported, as the context documents provide sufficient data to calculate these metrics.\n- The recommendation to review Tesla's official financial statements is redundant since the advisor already has access to the relevant context documents.\n\n## Missing Investor Risks\n- The report fails to address several critical risks that are visible in the context documents, including:\n  - **Competition**: The automotive industry is highly competitive, and Tesla faces increasing pressure from both established automakers and new entrants.\n  - **Valuation**: The report does not discuss the implications of Tesla's market valuation and how it may affect investor sentiment.\n  - **Supply Chain**: Issues related to supply chain disruptions and their impact on production and costs are not mentioned.\n  - **Regulation**: Potential changes in government incentives and regulations affecting electric vehicles are not addressed.\n  - **Execution**: Risks related to the execution of Tesla's growth strategy and operational efficiency are overlooked.\n\n## Figure and Visualization Issues\n- The report mentions the need for visual data representation but does not include any figures or charts, which would enhance understanding. There are references to figures in the context documents that could have been utilized.\n\n## Competitor Counterarguments\n- Competitors may argue that the advisor's report lacks depth in analyzing Tesla's financial health and does not adequately consider the competitive landscape. The absence of a thorough risk assessment could lead to misinterpretations of Tesla's market position.\n\n## Revision Priorities\n1. **Incorporate Key Financial Metrics**: Include specific financial ratios and margins derived from the context documents.\n2. **Address Missing Risks**: Expand the report to include a detailed analysis of competition, valuation, supply chain issues, regulatory risks, and execution challenges.\n3. **Add Visual Data**: Include relevant figures or charts to support the analysis and enhance clarity.\n4. **Clarify Recommendations**: Provide actionable insights based on the available data rather than suggesting a review of external documents.\n\n## Issues to Resolve\n- [ ] [Include key financial ratios and margins derived from context documents.]\n- [ ] [Address missing risks related to competition, valuation, supply chain, regulation, and execution.]\n- [ ] [Add relevant figures or charts to support the analysis.]\n- [ ] [Clarify and strengthen recommendations based on available data.]"
}
