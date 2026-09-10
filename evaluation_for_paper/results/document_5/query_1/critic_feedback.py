"""Critic Agent Feedback — document_5 / query_1"""
from __future__ import annotations

USER_QUERY = "What were Tesla's total revenues and net income for fiscal year 2022?"

ADVISOR_REPORT_V1 = """
# Tesla Financial Overview for Fiscal Year 2022

For the fiscal year 2022, Tesla reported the following financial figures derived from the NASDAQ TSLA 2022 Annual Report:

- **Total Revenues**: $81.46 billion
- **Net Income**: $12.56 billion

These figures represent significant growth compared to the previous year, with total revenues increasing by $27.64 billion and net income increasing by $7.04 billion.

## Financial Health
Tesla's strong revenue growth and net income indicate a robust financial position. The company continues to ramp up production and expand its operations, which is essential for sustaining this growth trajectory.

## Future Outlook
Looking ahead, Tesla aims to enhance its production capacity and delivery capabilities while focusing on improving battery technologies and expanding its product offerings. This strategic direction positions Tesla well to capitalize on the growing demand for electric vehicles and sustainable energy solutions.

## Risks and Limitations
Despite the positive outlook, Tesla faces several risks, including supply chain disruptions, fluctuating raw material costs, and increasing competition in the electric vehicle market. These factors could impact future profitability and operational efficiency.

## Actionable Advice
Investors should monitor Tesla's production metrics and market conditions closely. Additionally, keeping an eye on the company's ability to manage costs and maintain its competitive edge will be crucial for assessing its long-term viability.

## Visualization of Financial Figures
To enhance clarity, the following table summarizes Tesla's financial performance for 2022:

| Metric            | Amount (in billions) |
|-------------------|----------------------|
| Total Revenues    | $81.46               |
| Net Income        | $12.56               |

![Tesla Financial Overview](https://example.com/tesla_financial_overview.png) <!-- Placeholder for actual image link -->

*Source: NASDAQ TSLA 2022 Annual Report* 

If additional information is required, such as detailed financial ratios or segment performance, please let me know.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a clear summary of Tesla's financial performance for fiscal year 2022, including total revenues and net income. However, it lacks depth in risk analysis and does not adequately address certain critical areas that could impact investor decisions. The report is not fully decision-grade due to missing context on risks and potential challenges.\n\n## Major Logic Gaps\n- The report states that Tesla's financial health is \"robust\" based solely on revenue and net income figures without providing a comparative analysis or context regarding industry benchmarks or historical performance.\n- The future outlook section is optimistic but lacks specific metrics or timelines for the projected enhancements in production capacity and delivery capabilities.\n\n## Unsupported or Weakly Supported Claims\n- The claim that Tesla's revenue growth is \"essential for sustaining this growth trajectory\" is vague and lacks supporting evidence or analysis of how this growth will be maintained in the face of competition and market dynamics.\n- The report mentions \"monitoring production metrics and market conditions\" as actionable advice but does not specify which metrics or conditions are most critical for investors to watch.\n\n## Missing Investor Risks\n- The report does not address the risks associated with valuation, which is a significant concern for investors, especially given the high market expectations for Tesla.\n- Regulatory risks are also absent from the report, despite being a visible concern in the context documents. This omission could mislead investors regarding potential compliance costs or changes in legislation affecting Tesla's operations.\n\n## Figure and Visualization Issues\n- The image link provided for the financial overview does not appear to be a valid Supabase-hosted link, which could lead to accessibility issues for readers.\n- The image is not stored under the expected advisor_figure folder, which raises concerns about the organization and reliability of the visual content.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's growth is unsustainable due to increasing competition in the electric vehicle market, which is not sufficiently addressed in the report.\n- The lack of discussion on regulatory challenges could be leveraged by competitors to highlight potential vulnerabilities in Tesla's business model.\n\n## Revision Priorities\n1. Provide a more detailed analysis of Tesla's financial health, including comparisons with industry benchmarks.\n2. Expand the risk section to include valuation and regulatory risks, along with a discussion of how these could impact future performance.\n3. Improve the actionable advice by specifying key metrics and market conditions that investors should monitor.\n4. Ensure that the image link is valid and stored correctly to enhance the report's professionalism and accessibility.\n\n## Issues to Resolve\n- [ ] [Add comparative analysis of Tesla's financial health against industry benchmarks.]\n- [ ] [Include valuation and regulatory risks in the risk section.]\n- [ ] [Specify key metrics and market conditions in the actionable advice section.]\n- [ ] [Correct the image link to ensure it is a valid Supabase-hosted link.]\n- [ ] [Store the image under the expected advisor_figure folder for better organization.]"
}
