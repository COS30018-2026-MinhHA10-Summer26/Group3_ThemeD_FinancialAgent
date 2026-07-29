"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

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
The revised advisor report (v2) provides a generally positive assessment of Tesla's financial health and future outlook. However, it does not fully address all the issues identified by the Critic, leaving some gaps that need to be resolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, growth prospects, and risks associated with the company. All expected topics from the user query are present in the response.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  1. Provided context for the Altman Z-Score and compared it to industry benchmarks.
  2. Addressed competitive threats and market saturation in the future outlook.
  3. Quantified the potential impact of legal and regulatory risks.

- **Unresolved Issues**:
  1. Include specific evidence and citations from financial statements to support claims.
  2. Ensure the image link is valid and includes a caption.

## Remaining Gaps
The following issues remain unresolved:
1. Specific evidence and citations from the financial statements are still lacking to support claims made in the report.
2. The image link provided does not appear to be validated, and there is no caption accompanying the image for clarity.

## Recommendation
It is recommended that the advisor address the unresolved issues by:
1. Including specific figures or references from the financial statements to substantiate claims made in the report.
2. Validating the image link and adding a caption to provide context for the visual content. 

Addressing these gaps will enhance the report's credibility and provide a more comprehensive analysis for the user.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_20.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       90 |       85 |     -5 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       60 |       70 |    +10 |
| Evidence Usage       |    10%  |       60 |       65 |     +5 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       85 |       90 |     +5 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    76.00 |    79.50 |   +3.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +3.5 pts absolute  |  +4.61% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 90,
                "v2_score": 85,
                "delta": -5,
                "weighted_v1": 22.5,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 75,
                "delta": 5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 70,
                "delta": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 60,
                "v2_score": 65,
                "delta": 5,
                "weighted_v1": 6.0,
                "weighted_v2": 6.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 85,
                "v2_score": 90,
                "delta": 5,
                "weighted_v1": 8.5,
                "weighted_v2": 9.0
            }
        },
        "overall_v1": 76.0,
        "overall_v2": 79.5,
        "absolute_improvement": 3.5,
        "improvement_percentage": 4.61
    }
