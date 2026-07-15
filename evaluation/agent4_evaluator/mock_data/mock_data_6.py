"""
Mock inputs for testing the Evaluator Agent.

Auto-generated from evaluator run: mock_data_6.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla's Financial Health and Future Outlook

## Financial Health Assessment

Based on the Altman Z-Score analysis, Tesla's financial health is in a **Safe Zone** with a score of **44.454**, indicating a low risk of bankruptcy. Here are the key components of the score:

- **Working Capital to Assets**: 14.12%
- **Retained Earnings to Assets**: 5.26%
- **EBIT to Assets**: 6.58%
- **Market Capitalization to Liabilities**: 72.73
- **Sales to Assets**: 35.73%

Additionally, the ratio of total liabilities to market capitalization is **1.38%**, which further supports the conclusion of a strong financial position.

## Key Financial Metrics Comparison

The following chart compares Tesla's key financial metrics for the years 2022 and 2021:

![Key Financial Metrics Comparison (2022 vs 2021)](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_a14245f034ef_key-financial-metrics-comparison-2022-vs-2021.png)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*

*Source: NASDAQ TSLA 2022 Annual Report*

### Financial Metrics Table

| Metric                | Tesla 2022         | Tesla 2021         | Change (Abs)       | Change (%)       |
|-----------------------|--------------------|--------------------|---------------------|------------------|
| Capital Expenditures   | $7,160,000,000.00  | $6,480,000,000.00  | +$680,000,000.00    | +10.49%          |
| Cash and Equivalents   | $22,190,000,000.00 | $17,770,000,000.00 | +$4,420,000,000.00  | +24.87%          |
| Net Income             | $12,560,000,000.00 | $5,492,000,000.00  | +$7,068,000,000.00  | +128.70%         |
| Total Revenue          | $81,460,000,000.00 | $58,600,000,000.00 | +$22,860,000,000.00 | +39.01%          |

## Future Outlook

Tesla's significant growth in revenue and net income in 2022, alongside an increase in cash reserves, positions the company well for future investments and expansions. The increase in capital expenditures indicates a commitment to scaling operations and enhancing production capabilities.

### Strategic Recommendations:
1. **Investment in R&D**: Continue to invest in research and development, particularly in battery technology and autonomous driving features, to maintain competitive advantages.
2. **Market Expansion**: Explore opportunities in emerging markets where electric vehicle adoption is growing, leveraging government incentives where available.
3. **Cost Management**: Monitor and manage operational costs to sustain profitability, especially as production scales up.
4. **Regulatory Compliance**: Stay ahead of evolving regulations in different markets to avoid potential legal challenges that could impact operations.

## Risks and Limitations

While Tesla's financial health appears strong, several risks could impact its future outlook:

- **Regulatory Challenges**: Changes in government incentives and regulations regarding electric vehicles could affect demand and operational costs.
- **Market Volatility**: The stock price has historically been volatile, influenced by external factors and public perception.
- **Supply Chain Issues**: Ongoing supply chain disruptions could impact production capabilities and costs.
- **Competition**: The electric vehicle market is becoming increasingly competitive, with new entrants and established automakers ramping up their EV offerings.

## Conclusion

Tesla's financial health is robust, with strong revenue growth and low bankruptcy risk. By focusing on strategic investments and maintaining compliance with regulations, Tesla can continue to thrive in the competitive electric vehicle market. However, it must remain vigilant regarding potential risks that could impact its operations and market position.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla's Financial Health and Future Outlook

## Financial Health Assessment

Based on the Altman Z-Score analysis, Tesla's financial health is in a **Safe Zone** with a score of **8.367**, indicating a low risk of bankruptcy. Here are the key components of the score:

- **Working Capital to Assets**: 17.26%
- **Retained Earnings to Assets**: 15.65%
- **EBIT to Assets**: 16.59%
- **Market Capitalization to Liabilities**: 10.68
- **Sales to Assets**: 98.94%

Additionally, the ratio of total liabilities to market capitalization is **9.37%**, which further supports the conclusion of a strong financial position.

## Key Financial Metrics Comparison

The following table compares Tesla's key financial metrics for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                | Tesla 2022         | Tesla 2021         | Change (Abs)       | Change (%)       |
|-----------------------|--------------------|--------------------|---------------------|------------------|
| Capital Expenditures   | $7,160,000,000.00  | $6,480,000,000.00  | +$680,000,000.00    | +10.49%          |
| Cash and Equivalents   | $22,190,000,000.00 | $17,770,000,000.00 | +$4,420,000,000.00  | +24.87%          |
| Net Income             | $12,560,000,000.00 | $5,492,000,000.00  | +$7,068,000,000.00  | +128.70%         |
| Total Revenue          | $81,460,000,000.00 | $58,600,000,000.00 | +$22,860,000,000.00 | +39.01%          |

*Source: NASDAQ TSLA 2022 Annual Report*

## Future Outlook

Tesla's significant growth in revenue and net income in 2022, alongside an increase in cash reserves, positions the company well for future investments and expansions. The increase in capital expenditures indicates a commitment to scaling operations and enhancing production capabilities.

### Strategic Recommendations:
1. **Investment in R&D**: Continue to invest in research and development, particularly in battery technology and autonomous driving features, to maintain competitive advantages.
2. **Market Expansion**: Explore opportunities in emerging markets where electric vehicle adoption is growing, leveraging government incentives where available.
3. **Cost Management**: Monitor and manage operational costs to sustain profitability, especially as production scales up.
4. **Regulatory Compliance**: Stay ahead of evolving regulations in different markets to avoid potential legal challenges that could impact operations.

## Risks and Limitations

While Tesla's financial health appears strong, several risks could impact its future outlook:

- **Regulatory Challenges**: Changes in government incentives and regulations regarding electric vehicles could affect demand and operational costs.
- **Market Volatility**: The stock price has historically been volatile, influenced by external factors and public perception.
- **Supply Chain Issues**: Ongoing supply chain disruptions could impact production capabilities and costs.
- **Competition**: The electric vehicle market is becoming increasingly competitive, with new entrants and established automakers ramping up their EV offerings.
- **Margin Pressure**: Rising costs in the EV market and increased competition could pressure profit margins.

## Conclusion

Tesla's financial health is robust, with strong revenue growth and low bankruptcy risk. By focusing on strategic investments and maintaining compliance with regulations, Tesla can continue to thrive in the competitive electric vehicle market. However, it must remain vigilant regarding potential risks that could impact its operations and market position.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a generally positive assessment of Tesla's financial health and future outlook. However, it fails to fully address all issues identified by the Critic, particularly regarding the validation of financial figures.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's financial health and future outlook. It covers key financial metrics, strategic recommendations, and risks associated with Tesla's operations. The inclusion of a financial metrics comparison table and a discussion on risks enhances the report's relevance to the user's request.

## Issues Resolution Status
Out of the five issues identified by the Critic, four have been resolved in the revised report:
1. **Resolved**: Provide context and explanation for the Altman Z-Score and its implications.
2. **Resolved**: Discuss the potential impacts of regulatory challenges and supply chain issues on financial performance.
3. **Resolved**: Include a discussion on margin pressure and its relevance to Tesla's competitive position.
4. **Resolved**: Clarify the significance of the financial metrics comparison figure.
5. **Unresolved**: Validate all flagged financial figures with appropriate citations.

## Remaining Gaps
The following issue remains unresolved:
- **Validate all flagged financial figures with appropriate citations.** The report presents several financial figures, but it lacks sufficient context or citations to validate these numbers, which could mislead readers.

## Recommendation
It is recommended that the advisor revises the report to include appropriate citations or context for all financial figures presented. This will enhance the credibility of the report and ensure that it meets the standards expected for decision-grade analysis.
"""
