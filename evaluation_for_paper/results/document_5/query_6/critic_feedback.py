"""Critic Agent Feedback — document_5 / query_6"""
from __future__ import annotations

USER_QUERY = "What were Tesla's capital expenditures and free cash flow in 2022?"

ADVISOR_REPORT_V1 = """
# Tesla's Capital Expenditures and Free Cash Flow Analysis for 2022

To analyze Tesla's capital expenditures and free cash flow for the year 2022, we can extract the relevant figures from the provided documents.

### Capital Expenditures in 2022
According to Document 4, Tesla's capital expenditures for 2022 amounted to **$7.16 billion**.

### Free Cash Flow Calculation
Free cash flow (FCF) can be calculated using the formula:

\[ \text{Free Cash Flow} = \text{Cash Flow from Operations} - \text{Capital Expenditures} \]

From Document 4, we know:
- Cash Flow from Operations in 2022: **$14.72 billion**
- Capital Expenditures in 2022: **$7.16 billion**

Now, we can calculate the free cash flow:

\[
\text{Free Cash Flow} = 14.72 \, \text{billion} - 7.16 \, \text{billion} = 7.56 \, \text{billion}
\]

### Summary
- **Capital Expenditures in 2022:** $7.16 billion
- **Free Cash Flow in 2022:** $7.56 billion

### Financial Health and Future Outlook
Tesla's ability to generate a significant amount of free cash flow in 2022 indicates strong operational performance and effective capital management. The increase in cash flow from operations by **$3.23 billion** compared to the previous year suggests that Tesla is successfully scaling its operations and managing costs effectively.

However, it is important to note that Tesla's capital expenditures are expected to remain high as the company continues to invest in new manufacturing facilities and product development. The company has indicated that capital expenditures could range between **$6.00 to $8.00 billion** in 2023, which reflects ongoing investments in growth and innovation.

### Risks and Limitations
While Tesla's financial performance appears robust, there are inherent risks associated with its capital expenditures. For example, Document 5 mentions potential supply chain disruptions and rising material costs, which could impact future cash flows. Additionally, the company's reliance on government incentives for electric vehicle adoption may pose risks if such incentives are reduced or eliminated, as noted in Document 3.

### Additional Information Required
For a more comprehensive analysis, it would be beneficial to have access to Tesla's projected financial statements for 2023 and beyond, as well as updates on their strategic initiatives and market conditions. Specific information on upcoming projects and their expected financial impact would also enhance the analysis.

### Visual Aids
To enhance clarity, a table summarizing the financial metrics can be included:

| Metric                        | Amount (in billion) |
|-------------------------------|---------------------|
| Capital Expenditures 2022     | $7.16               |
| Cash Flow from Operations 2022 | $14.72              |
| Free Cash Flow 2022           | $7.56               |

*Source: NASDAQ_TSLA_2022.pdf*

This analysis shows that Tesla is well-positioned in terms of cash generation, but ongoing monitoring of market conditions and strategic execution will be crucial for sustaining its growth trajectory.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe report provides a clear analysis of Tesla's capital expenditures and free cash flow for 2022, but it contains several unsupported claims, missing risks, and lacks depth in certain areas. It requires revisions to enhance its credibility and comprehensiveness.\n\n## Major Logic Gaps\n- The calculation of free cash flow is presented without sufficient context regarding the reliability of the cash flow from operations figure. The report should clarify how this figure was derived and whether it is subject to any adjustments or estimates.\n- The report states that Tesla's capital expenditures are expected to remain high, but it does not adequately explain how this will impact future cash flows or profitability.\n\n## Unsupported or Weakly Supported Claims\n- The free cash flow figure of **$7.56 billion** is flagged as potentially unsupported. The report should provide a clear citation or context for this calculation to ensure it is credible.\n- The assertion that Tesla's financial performance appears robust is subjective and lacks quantitative backing. The report should include comparative metrics or benchmarks to substantiate this claim.\n\n## Missing Investor Risks\n- The report fails to address several critical risks, including:\n  - **Valuation Risks:** There is no discussion on how Tesla's current valuation may be impacted by market conditions or investor sentiment.\n  - **Regulatory Risks:** The report mentions government incentives but does not explore the potential risks associated with changes in regulations that could affect Tesla's operations.\n  - **Margin Pressure:** The report does not discuss potential margin pressures due to rising costs or competition, which could affect profitability.\n\n## Figure and Visualization Issues\n- The report mentions a table summarizing financial metrics but does not include an embedded image link or a properly formatted table in Markdown. This omission detracts from the report's clarity and accessibility.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's reliance on government incentives for electric vehicle adoption is a significant risk, especially if these incentives are reduced or eliminated. The report should address this concern more thoroughly.\n- The lack of discussion on competitive pressures in the electric vehicle market could be seen as a strategic blind spot. Competitors may leverage this to highlight their own advantages or strategies.\n\n## Revision Priorities\n1. Provide clear citations for all financial figures, especially the free cash flow calculation.\n2. Expand the discussion on risks, particularly regarding valuation, regulation, and margin pressures.\n3. Include a properly formatted table or figure to summarize financial metrics.\n4. Strengthen the analysis of Tesla's competitive position and potential market challenges.\n\n## Issues to Resolve\n- [ ] Clarify the source and reliability of the cash flow from operations figure.\n- [ ] Provide context or benchmarks to support claims of robust financial performance.\n- [ ] Address missing risks related to valuation, regulation, and margin pressure.\n- [ ] Embed a properly formatted table or figure summarizing financial metrics.\n- [ ] Discuss competitive pressures and how they may impact Tesla's market position."
}
