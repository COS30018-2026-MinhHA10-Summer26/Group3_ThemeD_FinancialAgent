"""Critic Agent Feedback — document_5 / query_5"""
from __future__ import annotations

USER_QUERY = "What were the main risks Tesla identified in its 2022 annual report?"

ADVISOR_REPORT_V1 = """
### Main Risks Identified by Tesla in its 2022 Annual Report

Tesla's 2022 Annual Report highlights several key risks that could impact its operations and financial performance. Here are the main risks identified:

1. **Government Investigations and Legal Proceedings:**
   - Tesla is currently cooperating with various government investigations, which could lead to liability, penalties, and other sanctions. The outcomes of these investigations are uncertain, and there is a risk of incurring significant costs related to compliance and legal defense (Source: Page 26).

2. **Environmental Regulations:**
   - Tesla has faced fines and legal challenges related to environmental regulations, particularly in Germany. The company has been involved in proceedings concerning compliance with market participation notifications and take-back obligations for end-of-life battery products. For instance, a fine was initially set at 12 million euros but was reduced to 600,000 euros following a settlement (Source: Page 29). The potential for further penalties exists if compliance issues are not adequately addressed.

3. **Waste Management Practices:**
   - Investigations into Tesla's waste segregation practices in California could pose risks. Although the company has implemented remedial measures, the outcome of these investigations remains uncertain, and there could be implications for Tesla's operations (Source: Page 29).

4. **Market Competition:**
   - The automotive and energy sectors are highly competitive, with numerous established and emerging players. Tesla faces the threat of new entrants and existing competitors that could impact its market share and pricing strategies.

5. **Supply Chain Disruptions:**
   - Tesla's operations are susceptible to supply chain disruptions, which can affect production and delivery timelines. Volatility in raw material prices can also impact profitability.

6. **Regulatory Changes:**
   - Changes in regulations, particularly those related to emissions and energy policies, could affect Tesla's business model and operational costs.

### Conclusion

Tesla's 2022 Annual Report outlines significant risks primarily related to legal and regulatory challenges, competition, and supply chain vulnerabilities. Addressing these risks will be crucial for maintaining operational stability and achieving long-term growth.

**Note:** The report does not include specific financial figures or metrics beyond those mentioned, and further context may be required for a more comprehensive analysis. Additionally, no actionable advice or recommendations based on the identified risks were included, and no tool-derived calculations or financial analysis could be performed due to insufficient data.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a reasonable summary of the main risks identified by Tesla in its 2022 Annual Report. However, it lacks depth in certain areas, particularly in providing actionable advice and addressing all relevant risks. Additionally, some claims are not fully supported by the context provided, which could lead to misinterpretations.\n\n## Major Logic Gaps\n- The report mentions \"market competition\" but does not elaborate on how Tesla plans to address this competition or what specific strategies it has in place. This leaves a gap in understanding Tesla's competitive positioning.\n- The report states that Tesla faces \"supply chain disruptions\" but does not discuss how these disruptions have historically impacted the company or what mitigation strategies are in place.\n\n## Unsupported or Weakly Supported Claims\n- The claim regarding the potential for further penalties related to environmental regulations is vague and lacks specific examples or data to substantiate the severity of this risk.\n- The mention of \"significant costs related to compliance and legal defense\" is not quantified, making it difficult to assess the potential financial impact on Tesla.\n\n## Missing Investor Risks\n- The report fails to address the risk of valuation, which is a critical aspect for investors. Given the volatility in the automotive and tech sectors, this omission could mislead investors regarding Tesla's financial health.\n- There is no mention of margin pressure, which could arise from rising costs or competitive pricing strategies, potentially affecting profitability.\n\n## Figure and Visualization Issues\n- The report references a chart or figure but does not include any visual representation or link to an image. This omission makes it harder for readers to grasp the data being discussed.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's reliance on government incentives and regulations could be a significant risk, especially if these incentives are reduced or eliminated. This point is not addressed in the report.\n- The report does not consider the potential for new entrants in the EV market, which could further dilute Tesla's market share and pricing power.\n\n## Revision Priorities\n1. Include specific strategies Tesla is employing to address competition and supply chain risks.\n2. Quantify the potential costs associated with legal compliance and environmental penalties.\n3. Add a discussion on valuation risks and margin pressures.\n4. Incorporate visual aids or figures to support claims made in the report.\n5. Address the implications of government incentives on Tesla's business model.\n\n## Issues to Resolve\n- [ ] Provide specific strategies for addressing competition and supply chain risks.\n- [ ] Quantify potential costs related to legal compliance and environmental penalties.\n- [ ] Discuss valuation risks and margin pressures.\n- [ ] Include visual aids or figures to support claims.\n- [ ] Address the implications of government incentives on Tesla's business model."
}
