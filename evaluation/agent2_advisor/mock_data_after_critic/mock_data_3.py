"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_3.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

Based on the analysis of the provided context documents, Tesla's financial health and future outlook can be summarized as follows:

### Financial Health Analysis

1. **Risks and Challenges**:
   - **Macroeconomic Factors**: Tesla faces risks from global economic conditions, particularly those stemming from the COVID-19 pandemic. Supply chain disruptions, labor shortages, and rising interest rates could adversely affect production and consumer demand.
   - **Production and Supply Chain**: The company has experienced delays in launching and ramping production for new products. Challenges with suppliers, particularly in securing components like semiconductors and battery cells, could hinder growth.
   - **Competition**: The automotive market is becoming increasingly competitive, with numerous established and new players entering the electric vehicle (EV) space. This competition could impact Tesla's market share and pricing strategies.
   - **Regulatory and Operational Risks**: Tesla must navigate various regulatory environments across different countries, which can complicate operations and increase costs.

2. **Growth Potential**:
   - Tesla's focus on expanding production capabilities, particularly with new factories like Gigafactory Berlin and Gigafactory Texas, positions it well for future growth. However, successful execution of these plans is critical.
   - The demand for electric vehicles is on the rise, and Tesla's established brand and innovative technology give it a competitive edge. Continued investment in R&D and manufacturing efficiency will be essential.

3. **Financial Metrics**:
   - Tesla's Altman Z-Score is **19.726**, indicating a **Safe Zone (Low Bankruptcy Risk)**. This suggests that the company is in a strong financial position with low risk of bankruptcy.
   - Key financial metrics for Tesla in 2022 compared to 2021 are as follows:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :-------------------- | :--------: | :--------: | :----------: | :--------: |
| EBIT                  | 800,000.00 | 700,000.00 | +100,000.00  | +14.29%   |
| Market Capitalization  | 80,000,000.00 | 70,000,000.00 | +10,000,000.00 | +14.29%   |
| Retained Earnings      | 2,000,000.00 | 1,500,000.00 | +500,000.00  | +33.33%   |
| Sales                 | 12,000,000.00 | 10,000,000.00 | +2,000,000.00 | +20.00%   |
| Total Assets          | 5,000,000.00 | 4,500,000.00 | +500,000.00  | +11.11%   |
| Total Liabilities     | 3,000,000.00 | 2,500,000.00 | +500,000.00  | +20.00%   |

### Future Outlook

Tesla's future outlook remains cautiously optimistic. The company is well-positioned to capitalize on the growing demand for electric vehicles, but it must address the outlined risks to sustain its growth trajectory. Key factors to monitor include:

- **Production Efficiency**: The ability to ramp up production without significant delays or cost overruns.
- **Market Demand**: Continued consumer interest in electric vehicles and Tesla's ability to meet that demand.
- **Competitive Landscape**: How Tesla adapts to increasing competition and maintains its market leadership.

### Conclusion

Tesla's financial health is influenced by various internal and external factors. While the company has significant growth potential, it must navigate challenges related to production, competition, and market dynamics. The Altman Z-Score indicates a low risk of bankruptcy, and the comparison of key financial metrics shows positive growth trends. Continued monitoring of these factors will be essential for assessing Tesla's long-term viability and success in the electric vehicle market. 

For further analysis, please provide any additional financial statements or metrics you may have, and I can assist in generating more detailed insights.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a comprehensive overview of Tesla's financial health and future outlook. However, it contains several unsupported claims, lacks depth in certain risk assessments, and presents potentially misleading financial metrics. The report requires revisions to enhance its credibility and decision-grade quality.\n\n## Major Logic Gaps\n- The report claims that Tesla's Altman Z-Score is in the \"Safe Zone,\" but it does not explain how this score was calculated or provide context for its significance. This lack of clarity may mislead investors about the company's financial stability.\n- The comparison table includes financial metrics that appear to be inflated or inaccurately represented, such as EBIT and market capitalization figures, which do not align with the provided context documents.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that Tesla's Altman Z-Score indicates a low risk of bankruptcy is not substantiated with a clear explanation of the score's calculation or its implications.\n- The report states that Tesla's demand for electric vehicles is on the rise but does not provide specific data or trends to support this claim, making it less convincing.\n\n## Missing Investor Risks\n- The report fails to address margin pressure, which is a critical risk given the rising costs of raw materials and potential supply chain disruptions. This oversight could lead investors to underestimate the financial pressures Tesla may face.\n- While competition is mentioned, the report does not quantify the impact of new entrants in the EV market or provide a comparative analysis of Tesla's market position relative to its competitors.\n\n## Figure and Visualization Issues\n- The comparison table contains potentially misleading figures that do not match the context documents. For example, the EBIT and market capitalization figures appear to be significantly higher than those reported in the financial statements. This discrepancy needs to be clarified or corrected.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's reliance on a limited number of suppliers for key components poses a significant risk, especially in light of recent supply chain disruptions. The report should address this vulnerability more thoroughly.\n- The report does not consider the potential for competitors to innovate and capture market share, which could undermine Tesla's growth prospects. A more detailed analysis of competitive threats is necessary.\n\n## Revision Priorities\n1. Clarify the calculation and significance of the Altman Z-Score.\n2. Correct the financial metrics in the comparison table to align with the context documents.\n3. Provide specific data or trends to support claims about rising demand for electric vehicles.\n4. Address the missing risk of margin pressure and its implications for Tesla's financial health.\n5. Include a more detailed analysis of the competitive landscape and potential threats to Tesla's market position.\n\n## Issues to Resolve\n- [ ] Clarify the calculation and significance of the Altman Z-Score.\n- [ ] Correct the financial metrics in the comparison table to align with context documents.\n- [ ] Provide specific data or trends to support claims about rising demand for electric vehicles.\n- [ ] Address the missing risk of margin pressure and its implications for Tesla's financial health.\n- [ ] Include a more detailed analysis of the competitive landscape and potential threats to Tesla's market position."
}
