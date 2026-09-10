"""Critic Agent Feedback — document_6 / query_7"""
from __future__ import annotations

USER_QUERY = "What risks related to competition and pricing pressure did Tesla disclose in 2023?"

ADVISOR_REPORT_V1 = """
# Tesla 2023 Risks Related to Competition and Pricing Pressure

⚠️ The specific risks related to competition and pricing pressure disclosed in Tesla's 2023 Annual Report (Form 10-K), particularly in the "Item 1A. Risk Factors" section, are currently unavailable. 

As such, I cannot provide the detailed disclosures regarding the company's exposure to competitive pressures and pricing strategies. 

To gain a thorough understanding of Tesla's competitive landscape and pricing strategies, I recommend accessing the "Item 1A. Risk Factors" section of Tesla's 2023 Annual Report directly. This section typically contains valuable insights into the risks the company faces in these areas.

If you have access to that specific section or any additional documents, please share them for further analysis. Alternatively, you may consider checking Tesla's official investor relations website or the SEC's EDGAR database for the complete report.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report lacks specific details regarding Tesla's risks related to competition and pricing pressure, which are crucial for investors and stakeholders. The absence of direct references to the relevant sections of the 2023 Annual Report diminishes the report's credibility and usefulness.\n\n## Major Logic Gaps\n- The report states that the risks related to competition and pricing pressure are \"currently unavailable,\" which is misleading. The risks are documented in the 2023 Annual Report, specifically in the \"Item 1A. Risk Factors\" section. This oversight suggests a lack of thoroughness in the analysis.\n- The recommendation to access the report directly without summarizing key points fails to provide actionable insights for the reader.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that the specific risks are unavailable is unsupported, as the context documents clearly outline various risks associated with competition and pricing pressures.\n- The report does not provide any evidence or citations to back up the claim of unavailability, which undermines its reliability.\n\n## Missing Investor Risks\n- The report fails to address several key risks that are visible in the context documents, including:\n  - **Valuation Risks**: The potential impact of fluctuating market conditions on Tesla's valuation.\n  - **Supply Chain Risks**: Issues related to supplier dependencies and potential disruptions.\n  - **Regulatory Risks**: Changes in government policies that could affect Tesla's operations and profitability.\n  - **Margin Pressure**: The effects of pricing strategies on profit margins.\n  - **Execution Risks**: Challenges in scaling production and meeting demand.\n\n## Figure and Visualization Issues\n- There are no figures or visualizations included in the report, which could have enhanced the understanding of the risks discussed. The absence of visual aids limits the report's effectiveness.\n\n## Competitor Counterarguments\n- Competitors could argue that the lack of detailed risk analysis indicates a weakness in Tesla's strategic planning. They may leverage this gap to position themselves as more transparent and risk-aware in their communications.\n\n## Revision Priorities\n- Include a summary of the specific risks related to competition and pricing pressure as outlined in the 2023 Annual Report.\n- Provide citations or references to the relevant sections of the report to support claims made in the critique.\n- Consider adding visual aids or figures to illustrate key points and enhance the report's clarity.\n\n## Issues to Resolve\n- [ ] [Summarize specific risks related to competition and pricing pressure from the 2023 Annual Report.]\n- [ ] [Provide citations or references to the relevant sections of the report.]\n- [ ] [Include visual aids or figures to enhance understanding.]\n- [ ] [Clarify the claim regarding the unavailability of risk information.]"
}
