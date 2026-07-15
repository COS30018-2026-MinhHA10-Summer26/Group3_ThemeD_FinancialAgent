"""
Mock inputs for testing the Evaluator Agent.

Auto-generated from evaluator run: mock_data_8.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Overview
Tesla has shown significant growth in its financial performance from 2021 to 2022, with substantial increases in revenues and gross profit. However, the company faces various risks and uncertainties that could impact its future performance.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                          | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|---------------------------------|:----------:|:----------:|:------------:|:-----------:|
| Automotive leasing              |  2,476.00  |  1,642.00  |   +834.00    |  +50.79%    |
| Automotive regulatory credits    |  1,776.00  |  1,465.00  |   +311.00    |  +21.23%    |
| Automotive sales                | 67,210.00  | 44,125.00  | +23,085.00   |  +52.32%    |
| Cost of revenues                | 60,609.00  | 40,217.00  | +20,392.00   |  +50.70%    |
| Gross margin                    |    25.60   |    25.30   |     +0.30    |  +1.19%     |
| Gross profit                    | 20,853.00  | 13,606.00  | +7,247.00    |  +53.26%    |
| Services and other              |  6,091.00  |  3,802.00  | +2,289.00    |  +60.21%    |
| Total automotive revenues        | 71,462.00  | 47,232.00  | +24,230.00   |  +51.30%    |
| Total revenues                  | 81,462.00  | 53,823.00  | +27,639.00   |  +51.35%    |

*Source: NASDAQ_TSLA_2022.pdf*

## Financial Health Analysis
1. **Revenue Growth**: Tesla's total revenues increased by 51.35% from 2021 to 2022, driven primarily by a significant rise in automotive sales and services. The automotive sales revenue alone rose by 52.32%, indicating strong demand for Tesla vehicles.

2. **Cost Management**: While the cost of revenues also increased significantly, the gross profit margin remained relatively stable, showing that Tesla is managing its costs effectively despite rising material and operational expenses.

3. **Diversification**: The growth in services and other revenue (up 60.21%) suggests that Tesla is successfully diversifying its income streams beyond just vehicle sales, which is crucial for long-term sustainability.

## Risks and Limitations
- **Market Volatility**: Tesla operates in a cyclical industry sensitive to economic fluctuations, regulatory changes, and supply chain disruptions. The recent inflationary pressures and rising interest rates could affect vehicle affordability and demand.
  
- **Production Challenges**: The ramp-up of production at new facilities (e.g., Gigafactory Berlin and Texas) poses operational risks. Any delays or inefficiencies could impact revenue growth.

- **Technological Uncertainties**: Tesla's ambitious plans for new technologies, including battery production, are subject to execution risks and market acceptance.

## Future Outlook
Tesla's strong revenue growth and improving operational efficiency position it well for future expansion. However, the company must navigate the aforementioned risks carefully. Continued investment in R&D and operational improvements will be essential to maintain its competitive edge and meet growing demand.

## Conclusion
Tesla's financial health appears robust, with significant growth in revenues and profits. However, the company must remain vigilant about market conditions and operational challenges to sustain its momentum. 

For a detailed risk assessment, further financial metrics would be required to compute the Altman Z-Score, which could provide additional insights into Tesla's bankruptcy risk. Currently, there is insufficient data to compute the Altman Z-Score.

---

This report provides a comprehensive analysis of Tesla's financial health and future outlook, including a comparison of key financial metrics. If you have any further questions or need additional information, please let me know!


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Overview
Tesla has demonstrated remarkable growth in its financial performance from 2021 to 2022, with substantial increases in revenues and gross profit. However, the company faces various risks and uncertainties that could impact its future performance.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                          | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|---------------------------------|:----------:|:----------:|:------------:|:-----------:|
| Automotive leasing              |  2,476.00  |  1,642.00  |   +834.00    |  +50.79%    |
| Automotive regulatory credits    |  1,776.00  |  1,465.00  |   +311.00    |  +21.23%    |
| Automotive sales                | 67,210.00  | 44,125.00  | +23,085.00   |  +52.32%    |
| Cost of revenues                | 60,609.00  | 40,217.00  | +20,392.00   |  +50.70%    |
| Gross margin                    |    25.60   |    25.30   |     +0.30    |  +1.19%     |
| Gross profit                    | 20,853.00  | 13,606.00  | +7,247.00    |  +53.26%    |
| Services and other              |  6,091.00  |  3,802.00  | +2,289.00    |  +60.21%    |
| Total automotive revenues        | 71,462.00  | 47,232.00  | +24,230.00   |  +51.30%    |
| Total revenues                  | 81,462.00  | 53,823.00  | +27,639.00   |  +51.35%    |

*Source: NASDAQ_TSLA_2022.pdf*

## Financial Health Analysis
1. **Revenue Growth**: Tesla's total revenues increased by 51.35% from 2021 to 2022, driven primarily by a significant rise in automotive sales and services. The automotive sales revenue alone rose by 52.32%, indicating strong demand for Tesla vehicles, supported by favorable market conditions and incentives.

2. **Cost Management**: While the cost of revenues also increased significantly, the gross profit margin remained relatively stable at 25.60%. This stability suggests effective cost management strategies, such as optimizing production processes and leveraging economies of scale.

3. **Diversification**: The growth in services and other revenue (up 60.21%) indicates that Tesla is successfully diversifying its income streams beyond just vehicle sales, which is crucial for long-term sustainability.

4. **Risk Assessment**: Tesla's Altman Z-Score is 8.367, placing it in the "Safe Zone" with low bankruptcy risk. The debt-to-equity ratio stands at 0.1252, indicating a conservative approach to leveraging, while the interest coverage ratio of 71.5 suggests strong ability to meet interest obligations.

## Risks and Limitations
- **Market Volatility**: Tesla operates in a cyclical industry sensitive to economic fluctuations, regulatory changes, and supply chain disruptions. The recent inflationary pressures and rising interest rates could affect vehicle affordability and demand.

- **Production Challenges**: The ramp-up of production at new facilities (e.g., Gigafactory Berlin and Texas) poses operational risks. Any delays or inefficiencies could impact revenue growth.

- **Technological Uncertainties**: Tesla's ambitious plans for new technologies, including battery production, are subject to execution risks and market acceptance.

- **Competitive Risks**: The rapidly evolving EV market is attracting new competitors, which could impact Tesla's market share and pricing power. Additionally, reliance on regulatory credits for revenue may pose vulnerabilities as regulations evolve.

- **Valuation Risks**: Tesla's high market capitalization relative to traditional automotive companies raises concerns about valuation, especially in a market correction scenario.

## Future Outlook
Tesla's strong revenue growth and improving operational efficiency position it well for future expansion. However, the company must navigate the aforementioned risks carefully. Continued investment in R&D and operational improvements will be essential to maintain its competitive edge and meet growing demand.

## Conclusion
Tesla's financial health appears robust, with significant growth in revenues and profits. However, the company must remain vigilant about market conditions and operational challenges to sustain its momentum. A thorough understanding of competitive dynamics and external economic factors will be crucial for Tesla's long-term success.

For a detailed risk assessment, the Altman Z-Score indicates a low bankruptcy risk, but ongoing monitoring of market conditions and competitive pressures is essential. 

---

This report provides a comprehensive analysis of Tesla's financial health and future outlook, including a comparison of key financial metrics. If you have any further questions or need additional information, please let me know!

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive analysis of Tesla's financial health and future outlook, addressing many of the issues raised in the Critic's report. However, one critical issue remains unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, discusses risks, and provides insights into the company's performance and strategies. The inclusion of the Altman Z-Score adds depth to the financial analysis.

## Issues Resolution Status
Out of the five issues identified by the Critic, four have been successfully resolved:
1. Evidence or market data supporting claims of strong demand for Tesla vehicles has been provided.
2. The report elaborates on how Tesla maintains stable gross profit margins amidst rising costs.
3. A discussion on competitive risks and their potential impact on Tesla's market position has been included.
4. Valuation risks associated with Tesla's high market capitalization have been addressed.

However, one issue remains unresolved:
- **Add contextual insights to the comparison table and consider including visual aids for better clarity.**

## Remaining Gaps
- The report still lacks contextual insights in the comparison table, which would help readers understand the significance of the changes in metrics. Additionally, the absence of visual aids or graphs to illustrate trends over time limits the report's effectiveness in conveying financial trajectories.

## Recommendation
To enhance the report further, it is recommended that the advisor:
1. Add contextual insights to the comparison table to explain the significance of the changes in metrics.
2. Consider including visual aids or graphs to illustrate financial trends over time, which would improve clarity and understanding for the reader.

Addressing these remaining gaps will ensure a more robust and informative analysis of Tesla's financial health and future outlook.
"""
