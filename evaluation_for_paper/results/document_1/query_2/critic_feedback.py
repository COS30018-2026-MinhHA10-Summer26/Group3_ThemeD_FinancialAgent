"""Critic Agent Feedback — document_1 / query_2"""
from __future__ import annotations

USER_QUERY = "How did Amazon's AWS segment perform in 2022 compared to prior years?"

ADVISOR_REPORT_V1 = """
# Amazon AWS Segment Performance Analysis for 2022

To analyze Amazon's AWS segment performance in 2022 compared to prior years, we have the following information:

- AWS had an annualized revenue run rate of **$85 billion** in 2022.
- AWS revenue grew **29% year-over-year** in 2022 on a **$62 billion** revenue base.

Unfortunately, the specific revenue figures for AWS in 2021 and 2020 are not available in the provided documents. Therefore, a direct year-over-year comparison with those years cannot be made.

### Summary of AWS Performance in 2022:
- **2022 Revenue Base**: $62 billion
- **2022 Year-over-Year Growth**: 29%
- **Annualized Revenue Run Rate**: $85 billion

### Revenue Performance Comparison Table

| Year | Revenue       |
|------|---------------|
| 2020 | Unavailable   |
| 2021 | Unavailable   |
| 2022 | $62 billion   |

### Financial Health and Future Outlook:
Despite the growth in 2022, AWS is facing short-term headwinds as companies are being more cautious in spending due to challenging macroeconomic conditions. This has led to a focus on customer relationships and optimizing AWS spend rather than aggressive cost-cutting.

### Risks and Limitations:
- The current macroeconomic environment may impact AWS's growth trajectory.
- Companies may be hesitant to invest heavily in cloud services during uncertain times, which could affect AWS's revenue growth in the near term.

### Actionable Insights:
- AWS should continue to focus on customer-centric strategies to maintain and grow its market share.
- Emphasizing the unique elasticity of cloud services can help in retaining customers who may be looking to optimize costs.

If you have access to additional documents or data that include AWS revenue figures for 2021 and 2020, please share them, and I can assist you further in providing a more comprehensive analysis.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a concise overview of Amazon's AWS segment performance in 2022, highlighting key metrics such as revenue growth and annualized revenue run rate. However, it lacks comprehensive year-over-year comparisons and fails to address several critical risks that could impact AWS's future performance. The report is not fully decision-grade due to these gaps.\n\n## Major Logic Gaps\n- The report states that AWS had a revenue base of $62 billion in 2022 but does not provide figures for 2021 and 2020, making it impossible to assess growth trends accurately.\n- The report mentions \"short-term headwinds\" but does not elaborate on what specific factors are causing these headwinds or how they might affect AWS's performance.\n\n## Unsupported or Weakly Supported Claims\n- The claim of a 29% year-over-year growth is presented without context or comparison to previous years, which weakens its impact.\n- The annualized revenue run rate of $85 billion is mentioned but lacks supporting evidence or context regarding how this figure was derived.\n\n## Missing Investor Risks\n- The report does not address several visible risks from the context documents, including:\n  - **Competition**: The report fails to mention the competitive landscape AWS operates in, which is crucial for understanding market dynamics.\n  - **Valuation**: There is no discussion on how AWS's valuation might be affected by market conditions or investor sentiment.\n  - **Supply Chain**: The report does not consider potential supply chain issues that could impact AWS's service delivery.\n  - **Regulation**: There is no mention of regulatory risks that could affect AWS's operations.\n  - **Margin Pressure**: The report does not discuss potential margin pressures due to rising costs or competitive pricing.\n  - **Execution Risks**: The report lacks insights into operational challenges that could hinder AWS's growth.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations to support the claims made, which could enhance understanding and retention of the information presented.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of detailed year-over-year comparisons undermines the credibility of the growth claims.\n- The absence of a discussion on competitive pressures could be seen as a strategic blind spot, suggesting that AWS may not be adequately prepared for market challenges.\n\n## Revision Priorities\n1. Include historical revenue figures for AWS in 2021 and 2020 to allow for a comprehensive year-over-year comparison.\n2. Elaborate on the specific short-term headwinds affecting AWS and how they might impact future growth.\n3. Address the missing risks related to competition, valuation, supply chain, regulation, margin pressure, and execution.\n4. Consider adding figures or visualizations to support key claims and enhance the report's clarity.\n\n## Issues to Resolve\n- [ ] Provide AWS revenue figures for 2021 and 2020 for comparison.\n- [ ] Elaborate on specific short-term headwinds affecting AWS.\n- [ ] Address missing risks: competition, valuation, supply chain, regulation, margin pressure, execution.\n- [ ] Include figures or visualizations to support claims made in the report."
}
