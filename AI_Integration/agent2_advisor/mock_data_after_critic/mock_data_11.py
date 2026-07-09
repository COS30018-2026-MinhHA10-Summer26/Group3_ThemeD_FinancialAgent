"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_11.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla, Inc. Financial Health and Future Outlook

## Overview
Based on the consolidated financial statements for Tesla, Inc. for the year ended December 31, 2022, the company has shown significant growth in key financial metrics compared to the previous year. However, there are also indications of high bankruptcy risk as assessed by the Altman Z-Score.

## Key Financial Metrics Comparison

### Financial Performance
The following table summarizes the key financial metrics for Tesla in 2022 compared to 2021:

| Metric               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------|------------|------------|--------------|------------|
| Equity                | 44,704.00  | 30,189.00  | +14,515.00   | +48.08%    |
| Net Income            | 12,556.00  | 5,519.00   | +7,037.00    | +127.50%   |
| Revenues             | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |
| Total Assets         | 82,338.00  | 62,131.00  | +20,207.00   | +32.52%    |
| Total Liabilities    | 36,440.00  | 30,548.00  | +5,892.00    | +19.29%    |

### Chart of Key Financial Metrics
![Key Financial Metrics Comparison: Tesla 2022 vs 2021](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_198cdedc8d79_key-financial-metrics-comparison-tesla-2022-vs-2021.png)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*  
*Source: Data sourced from Tesla's consolidated financial statements.*

## Risk Assessment
The Altman Z-Score for Tesla is **1.755**, placing it in the **Distress Zone (High Bankruptcy Risk)**. The components of the Z-Score are as follows:

- **Working Capital to Assets**: 0.0002
- **Retained Earnings to Assets**: 0.1565
- **EBIT to Assets**: 0.1659
- **Equity Market Value to Liabilities**: 0.0 (not applicable)
- **Sales to Assets**: 0.9894

### Explanation of the Altman Z-Score Calculation
The Altman Z-Score is a formula used to predict the likelihood of bankruptcy for a company. It combines five financial ratios, weighted by coefficients derived from a study of publicly traded manufacturing firms. The Z-Score is calculated as follows:

\[ Z = 1.2 	imes 	ext{(Working Capital / Total Assets)} + 1.4 	imes 	ext{(Retained Earnings / Total Assets)} + 1.2 	imes 	ext{(EBIT / Total Assets)} + 0.6 	imes 	ext{(Market Value of Equity / Total Liabilities)} + 0.999 	imes 	ext{(Sales / Total Assets)} \]

A Z-Score below 1.8 indicates a high risk of bankruptcy, while a score above 3 suggests a low risk.

### Interpretation
- **Distress Zone**: This indicates that Tesla is at a high risk of bankruptcy. While the company has shown strong revenue growth and improved profitability, the increasing liabilities relative to assets could pose a significant risk if not managed properly.

## Limitations of the Analysis
While the Altman Z-Score provides valuable insights into Tesla's financial health, it has limitations:
- **Industry Specificity**: The Z-Score was developed based on manufacturing firms and may not fully capture the unique aspects of Tesla's business model, which includes technology and energy sectors.
- **Market Conditions**: The score does not account for external market conditions that could impact Tesla's performance, such as economic downturns or changes in consumer preferences.
- **Non-Financial Factors**: Factors such as management quality, brand strength, and competitive landscape are not considered in the Z-Score but can significantly influence a company's long-term viability.

## Future Outlook
1. **Growth Potential**: Tesla's significant increase in revenues and net income suggests strong demand for its products, particularly in the automotive sector. The company should continue to capitalize on this momentum by expanding its product offerings and market reach.

2. **Cost Management**: With rising liabilities, Tesla must focus on managing its costs effectively to maintain profitability. This includes optimizing production processes and controlling operational expenses.

3. **Investment in Innovation**: Continued investment in research and development will be crucial for Tesla to stay competitive in the rapidly evolving automotive and energy sectors.

4. **Monitoring Financial Health**: Regular monitoring of financial metrics and risk assessments will be essential for Tesla to navigate potential challenges and sustain its growth trajectory.

## Conclusion
Tesla's financial health appears robust with significant growth in key metrics; however, the high bankruptcy risk indicated by the Altman Z-Score necessitates careful financial management and strategic planning to ensure long-term sustainability and success.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook, but it contains significant gaps in risk assessment and lacks a thorough analysis of competitive pressures. The reliance on the Altman Z-Score without contextualizing its limitations may mislead investors regarding the company's true financial stability.\n\n## Major Logic Gaps\n- The report states that Tesla is in the \"Distress Zone\" based on the Altman Z-Score but does not sufficiently explain how this score relates to the company's operational realities and market position. The implications of being in this zone should be elaborated upon.\n- The conclusion suggests that Tesla's financial health is \"robust\" despite the high bankruptcy risk indicated by the Z-Score. This contradiction needs clarification.\n\n## Unsupported or Weakly Supported Claims\n- The report claims significant growth in key financial metrics but does not provide a comparative analysis of industry benchmarks or competitors, which would help contextualize Tesla's performance.\n- The assertion that Tesla's growth suggests strong demand lacks supporting evidence or data trends that illustrate market demand beyond financial metrics.\n\n## Missing Investor Risks\n- The report fails to address critical risks such as competition, supply chain vulnerabilities, and regulatory changes that could impact Tesla's operations and financial health. These are essential for investors to understand the broader risk landscape.\n- The mention of rising liabilities is noted, but the potential impact of these liabilities on future cash flows and operational flexibility is not discussed.\n\n## Figure and Visualization Issues\n- The figure provided is relevant but lacks a detailed explanation of its significance in the context of Tesla's financial health. More context around the visual data would enhance understanding.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's high bankruptcy risk, as indicated by the Altman Z-Score, reflects underlying weaknesses that could be exploited. The report does not address how Tesla plans to mitigate these risks in comparison to its competitors.\n- The absence of a competitive analysis leaves the report vulnerable to critiques regarding Tesla's market position and strategic advantages.\n\n## Revision Priorities\n1. Clarify the implications of the Altman Z-Score and reconcile it with the overall assessment of financial health.\n2. Provide a comparative analysis of Tesla's financial metrics against industry benchmarks and competitors.\n3. Expand the risk assessment section to include competition, supply chain vulnerabilities, and regulatory risks.\n4. Enhance the explanation of the figure to provide context and significance to the data presented.\n\n## Issues to Resolve\n- [ ] Clarify the implications of the Altman Z-Score and reconcile it with the overall assessment of financial health.\n- [ ] Provide a comparative analysis of Tesla's financial metrics against industry benchmarks and competitors.\n- [ ] Expand the risk assessment section to include competition, supply chain vulnerabilities, and regulatory risks.\n- [ ] Enhance the explanation of the figure to provide context and significance to the data presented."
}
