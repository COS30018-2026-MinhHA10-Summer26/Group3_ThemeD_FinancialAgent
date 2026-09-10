"""Critic Agent Feedback — document_6 / query_1"""
from __future__ import annotations

USER_QUERY = "What were Tesla's total revenues and operating income for fiscal year 2023?"

ADVISOR_REPORT_V1 = """
# Tesla 2023 Financial Overview

## Total Revenues and Operating Income
Unfortunately, Tesla's total revenues and operating income for fiscal year 2023 are not available in the provided documents. This information cannot be confirmed without access to the relevant financial statements. If you have access to Tesla's financial statements or can provide additional context, please share them so I can assist you further in retrieving the specific figures you are looking for.

## Financial Health
As the specific financial figures for 2023 are unavailable, a comprehensive assessment of Tesla's financial health cannot be conducted. However, it is essential to monitor key metrics such as revenue growth, profit margins, and cash flow in future reports.

## Future Outlook
Without the latest financial data, it is challenging to provide a detailed future outlook. Generally, Tesla's growth trajectory has been influenced by factors such as market demand for electric vehicles, production capacity, and competition. Keeping an eye on these elements will be crucial for understanding Tesla's potential performance in the coming years.

## Risks and Limitations
1. **Market Competition**: The electric vehicle market is becoming increasingly competitive, with traditional automakers and new entrants vying for market share.
2. **Supply Chain Issues**: Disruptions in the supply chain can impact production and delivery timelines.
3. **Regulatory Changes**: Changes in government policies regarding electric vehicles and renewable energy can affect Tesla's operations and profitability.

## Actionable Advice
- **Stay Informed**: Keep track of Tesla's quarterly earnings reports and other financial disclosures to gain insights into its performance.
- **Diversification**: Consider diversifying investments to mitigate risks associated with Tesla's stock volatility.
- **Monitor Industry Trends**: Pay attention to trends in the electric vehicle market and technological advancements that could impact Tesla's business model.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks critical financial data regarding Tesla's total revenues and operating income for fiscal year 2023, which is essential for making informed investment decisions. The absence of this information significantly undermines the report's utility for investors.\n\n## Major Logic Gaps\n- The report states that total revenues and operating income are unavailable, yet it does not provide any context or alternative sources for this information. This creates a gap in the analysis and leaves investors without a clear understanding of Tesla's financial performance.\n- The report fails to address how the lack of financial data impacts the overall assessment of Tesla's financial health and future outlook.\n\n## Unsupported or Weakly Supported Claims\n- The claim that a comprehensive assessment of Tesla's financial health cannot be conducted without specific figures is valid, but it lacks depth. The report should suggest alternative metrics or indicators that could provide insights into Tesla's financial health in the absence of revenue and income data.\n\n## Missing Investor Risks\n- While the report mentions market competition, supply chain issues, and regulatory changes, it does not address the risk of valuation, which is critical given the current market dynamics and Tesla's stock performance.\n- The report should also consider the potential impact of macroeconomic factors, such as inflation and interest rates, on Tesla's business.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations to support its claims, which could enhance understanding and provide a clearer picture of Tesla's financial situation.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's inability to provide financial data raises concerns about transparency and reliability, which could affect investor confidence.\n- Additionally, competitors may highlight their own financial performance metrics to position themselves as more stable or reliable investments compared to Tesla.\n\n## Revision Priorities\n- Include specific financial figures for total revenues and operating income for 2023, if available, or provide alternative sources for this information.\n- Expand on the analysis of Tesla's financial health by suggesting other metrics or indicators that could be monitored in the absence of revenue data.\n- Address the missing risk of valuation and consider macroeconomic factors that could impact Tesla's performance.\n- Incorporate figures or visualizations to support claims and enhance the report's clarity.\n\n## Issues to Resolve\n- [ ] Provide total revenues and operating income for 2023 or alternative sources for this information.\n- [ ] Suggest alternative metrics for assessing Tesla's financial health.\n- [ ] Include the risk of valuation in the report.\n- [ ] Consider macroeconomic factors affecting Tesla's performance.\n- [ ] Incorporate figures or visualizations to support claims."
}
