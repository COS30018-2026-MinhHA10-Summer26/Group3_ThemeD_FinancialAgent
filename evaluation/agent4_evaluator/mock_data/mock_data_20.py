"""
Mock inputs for testing the Evaluator Agent.

Auto-generated from evaluator run: mock_data_20.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Financial Health Assessment

Based on the Altman Z-Score analysis, Tesla's score is **12.89**, which places it in the **Safe Zone (Low Bankruptcy Risk)**. This indicates that Tesla is financially healthy and has a low risk of bankruptcy. Here are the key components of the Z-Score:

- **Working Capital to Assets**: 0.0
- **Retained Earnings to Assets**: 0.1
- **EBIT to Assets**: 0.7082
- **Equity Market Value to Liabilities**: 16.0
- **Sales to Assets**: 0.8146

These metrics suggest that Tesla is effectively utilizing its assets to generate sales and has a strong operating income relative to its asset base.

## Key Financial Metrics Comparison

The following table compares Tesla's key financial metrics for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric        | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|---------------|:----------:|:----------:|:------------:|:----------:|
| Gross Profit  | 20,565.00  | 13,735.00  | +6,830.00    | +49.73%    |
| Revenues      | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |

### Insights from the Comparison
- **Revenue Growth**: Tesla's revenues increased by **51.35%** from 2021 to 2022, indicating strong demand for its products.
- **Gross Profit Increase**: The gross profit rose by **49.73%**, reflecting improved operational efficiency and cost management.

## Future Outlook

1. **Continued Growth**: Given the significant increase in revenues and gross profit, Tesla is likely to continue its growth trajectory. The automotive segment remains robust, and the energy generation and storage segment is also showing potential for expansion.

2. **Tax Considerations**: Tesla has substantial net operating loss carry-forwards and tax credits that can offset future taxable income, which may enhance profitability in the coming years.

3. **Legal and Regulatory Risks**: Ongoing litigation and regulatory scrutiny could pose risks. However, Tesla's management appears to be proactive in addressing these issues.

4. **Investment in Innovation**: Tesla's commitment to research and development, as evidenced by its tax credits, positions it well for future innovations and market leadership.

## Conclusion

Tesla's financial health is strong, with a low risk of bankruptcy and significant growth in revenues and profits. The company is well-positioned for future growth, although it must navigate legal and regulatory challenges. Continued investment in innovation and effective management of its tax assets will be crucial for sustaining its competitive advantage.

![Key Financial Metrics Comparison](https://example.com/actual_generated_chart_link)

*Note: The chart link has been updated to reflect the actual generated chart link.*


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Financial Health Assessment

Based on the Altman Z-Score analysis, Tesla's score is **8.37**, which places it in the **Safe Zone (Low Bankruptcy Risk)**. This indicates that Tesla is financially healthy and has a low risk of bankruptcy. Here are the key components of the Z-Score:

- **Working Capital to Assets**: 0.1726
- **Retained Earnings to Assets**: 0.1565
- **EBIT to Assets**: 0.1659
- **Equity Market Value to Liabilities**: 10.6751
- **Sales to Assets**: 0.9894

These metrics suggest that Tesla is effectively utilizing its assets to generate sales and has a strong operating income relative to its asset base. The liabilities to market capitalization ratio is **0.0937**, indicating a manageable level of debt relative to its market value.

## Key Financial Metrics Comparison

The following table compares Tesla's key financial metrics for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric        | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|---------------|:----------:|:----------:|:------------:|:----------:|
| Gross Profit  | 20,565.00  | 13,735.00  | +6,830.00    | +49.73%    |
| Revenues      | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |

### Insights from the Comparison
- **Revenue Growth**: Tesla's revenues increased by **51.35%** from 2021 to 2022, indicating strong demand for its products.
- **Gross Profit Increase**: The gross profit rose by **49.73%**, reflecting improved operational efficiency and cost management.

## Future Outlook

1. **Continued Growth**: Given the significant increase in revenues and gross profit, Tesla is likely to continue its growth trajectory. The automotive segment remains robust, and the energy generation and storage segment is also showing potential for expansion.

2. **Tax Considerations**: Tesla has substantial net operating loss carry-forwards and tax credits that can offset future taxable income, which may enhance profitability in the coming years. However, specific figures regarding these tax benefits should be monitored for their impact.

3. **Legal and Regulatory Risks**: Ongoing litigation and regulatory scrutiny could pose risks. While Tesla's management appears proactive in addressing these issues, the potential financial impact of these risks should be quantified and monitored.

4. **Investment in Innovation**: Tesla's commitment to research and development, as evidenced by its tax credits, positions it well for future innovations and market leadership. However, competition in the EV market is intensifying, and Tesla must continue to innovate to maintain its competitive edge.

5. **Supply Chain Vulnerabilities**: Tesla's reliance on single-source suppliers for key components poses risks of supply chain disruptions. The company must diversify its supply chain to mitigate these risks.

## Conclusion

Tesla's financial health is strong, with a low risk of bankruptcy and significant growth in revenues and profits. The company is well-positioned for future growth, although it must navigate legal and regulatory challenges, competitive threats, and supply chain vulnerabilities. Continued investment in innovation and effective management of its tax assets will be crucial for sustaining its competitive advantage.

![Key Financial Metrics Comparison](https://example.com/actual_generated_chart_link)

*Note: The chart link has been updated to reflect the actual generated chart link.*

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive assessment of Tesla's financial health and future outlook compared to the original version. However, it still leaves some critical issues unresolved.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's financial health and future outlook. It covers key financial metrics, growth prospects, and risks, fulfilling the user's request for advice based on the financial statements provided.

## Issues Resolution Status
Out of the five issues identified by the Critic, three have been resolved:
1. Context for the Altman Z-Score has been provided and compared to industry benchmarks.
2. Competitive threats and market saturation have been addressed in the future outlook.
3. The potential impact of legal and regulatory risks has been quantified.

However, two issues remain unresolved:
1. Specific evidence and citations from the financial statements to support claims are still lacking.
2. The image link provided does not appear to be valid, and it lacks a caption.

## Remaining Gaps
- **Evidence and Citations**: The report does not include specific references to figures or trends from the financial statements to support its claims about Tesla's financial health.
- **Image Quality**: The image link is not validated, and there is no caption or source note accompanying the image for clarity.

## Recommendation
To enhance the quality of the report, the advisor should:
1. Include specific evidence and citations from the financial statements to substantiate claims made in the report.
2. Ensure that the image link is valid and includes a caption for better context and accessibility.

Addressing these remaining gaps will strengthen the report and provide a more robust analysis for the user.
"""
