"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_7.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla's Financial Health and Future Outlook

## Financial Health Assessment

Based on the analysis of Tesla's financial metrics for 2022, the company demonstrates a strong financial position with a favorable outlook. Here are the key findings:

### Altman Z-Score Analysis
- **Z-Score**: 12.88
- **Zone**: Safe Zone (Low Bankruptcy Risk)

The Altman Z-Score indicates that Tesla is in a safe zone with a low risk of bankruptcy. This score is derived from the following ratios:
- **Working Capital to Assets**: 32.63%
- **Retained Earnings to Assets**: 17.65%
- **EBIT to Assets**: 18.47%
- **Market Capitalization to Liabilities**: 17.39
- **Sales to Assets**: 119.79%

### Key Financial Metrics Comparison (2022 vs 2021)

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|-------------|-------------|--------------|-------------|
| Capital Expenditures       | $7,160M     | $6,480M     | +$680M       | +10.49%     |
| Cash and Cash Equivalents  | $22,190M    | $17,741M    | +$4,449M     | +25.08%     |
| Net Income                 | $12,560M    | $5,252M     | +$7,308M     | +139.15%    |
| Revenue                    | $81,460M    | $54,896M    | +$26,564M    | +48.39%     |

### Key Observations
- **Revenue Growth**: Tesla's revenue increased significantly by 48.39%, reflecting strong demand for its electric vehicles and energy products.
- **Net Income Surge**: The net income rose by 139.15%, indicating improved profitability and operational efficiency.
- **Cash Reserves**: The cash and cash equivalents increased by 25.08%, providing a solid liquidity position to fund future growth initiatives.
- **Capital Expenditures**: Increased capital expenditures by 10.49% suggest ongoing investments in production capacity and technology development.

## Future Outlook

Tesla's future outlook appears promising, driven by several factors:
1. **Production Capacity Expansion**: The company is ramping up production capabilities at its Gigafactories, which will support increased vehicle deliveries and energy product deployments.
2. **Technological Advancements**: Continued focus on battery technology and AI-driven features (like Full Self-Driving) is expected to enhance product offerings and competitiveness.
3. **Market Demand**: The ongoing shift towards electrification in the automotive sector and increasing environmental awareness will likely sustain demand for Tesla's products.
4. **Global Expansion**: New factories in strategic locations will help mitigate supply chain issues and improve delivery efficiency.

However, Tesla must navigate challenges such as inflationary pressures, rising interest rates, and potential supply chain disruptions. The cyclical nature of the automotive industry also poses risks that could affect sales volatility.

![Key Financial Metrics Comparison: Tesla 2022 vs 2021](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_35749045fc9f)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*  
*Source: Data sourced from Tesla's 2022 financial statements.*

## Actionable Recommendations
- **Invest in Technology**: Continue investing in battery technology and AI features to maintain a competitive edge.
- **Expand Production**: Focus on ramping up production at new Gigafactories to meet growing demand.
- **Monitor Economic Factors**: Keep a close eye on inflation and interest rates, adjusting pricing strategies as necessary to maintain sales momentum.
- **Enhance Supply Chain Resilience**: Develop strategies to mitigate supply chain disruptions, including diversifying suppliers and increasing local sourcing.

## Conclusion

Tesla's financial health is robust, with strong revenue growth, improved profitability, and a solid cash position. The company's strategic investments and focus on innovation position it well for future growth, despite the inherent risks in the automotive sector.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook. However, it contains several unsupported claims, missing risks, and issues with figures that need to be addressed to enhance its credibility and decision-grade quality.\n\n## Major Logic Gaps\n- The report claims a \"safe zone\" based on the Altman Z-Score without providing context on how this score compares to industry benchmarks or historical performance. This lack of comparative analysis weakens the assertion of low bankruptcy risk.\n- The report does not sufficiently address the cyclical nature of the automotive industry and how it may impact Tesla's future performance, particularly in a potential economic downturn.\n\n## Unsupported or Weakly Supported Claims\n- The report states that Tesla's revenue growth reflects \"strong demand\" for its products but does not provide evidence or context to support this assertion. It would be beneficial to include market analysis or sales data to substantiate this claim.\n- The Altman Z-Score is presented without a clear explanation of its components or how they were calculated, which may leave readers questioning the validity of the score.\n\n## Missing Investor Risks\n- The report fails to address regulatory risks, which are critical given the evolving landscape of automotive regulations and environmental policies. This omission could mislead investors about potential challenges Tesla may face.\n- Competition is not mentioned as a risk, despite the increasing number of players in the electric vehicle market. This oversight could lead to an underestimation of market pressures on Tesla.\n\n## Figure and Visualization Issues\n- The figure included in the report does not point to a supported image extension, which may hinder accessibility and understanding. Additionally, there is no clear source or citation for the data presented in the figure, which could raise questions about its reliability.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's reliance on a few key suppliers for raw materials poses a significant risk, especially in light of potential supply chain disruptions. This point is not adequately addressed in the report.\n- The report's optimistic outlook on production capacity expansion may be challenged by competitors who have established more diversified supply chains or who are investing heavily in their own production capabilities.\n\n## Revision Priorities\n1. Provide context for the Altman Z-Score, including industry comparisons and historical performance.\n2. Include evidence or market analysis to support claims of strong demand for Tesla's products.\n3. Address regulatory risks and competition as significant factors that could impact Tesla's future performance.\n4. Fix the figure's image URL and ensure it points to a supported format, along with proper citations for the data presented.\n\n## Issues to Resolve\n- [ ] Provide context for the Altman Z-Score and its components.\n- [ ] Include evidence to support claims of strong demand for Tesla's products.\n- [ ] Address regulatory risks in the report.\n- [ ] Discuss competition as a potential risk factor.\n- [ ] Fix the figure's image URL and ensure proper citation for the data."
}
