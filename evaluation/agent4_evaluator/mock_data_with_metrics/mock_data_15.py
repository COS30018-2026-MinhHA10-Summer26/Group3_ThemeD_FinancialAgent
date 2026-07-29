"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_15.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Financial Health Overview

Tesla's financial health can be assessed through various metrics, including cash reserves, sales performance, and overall asset management. Based on the latest financial statements, here are some key observations:

1. **Cash and Cash Equivalents**: As of December 31, 2022, Tesla reported cash and cash equivalents of $16.25 billion, a decrease of approximately 7.53% from $17.58 billion in 2021. This decline may indicate a need for careful cash management, especially in light of ongoing investments and operational costs.

2. **Sales and Revenue**: The sales figures were not explicitly provided in the financial statements, making it difficult to assess revenue generation accurately. The lack of data suggests potential stagnation or lack of growth, which could be a concern for future profitability and operational expansion.

3. **Total Assets and Liabilities**: Unfortunately, the total assets and liabilities data were not provided in the financial statements, making it difficult to assess the overall leverage and financial stability of the company.

## Risks and Limitations

- **Market Dependency**: Tesla's performance is heavily reliant on the automotive market and the demand for electric vehicles (EVs). Any downturn in consumer interest or economic conditions could adversely affect sales.
  
- **Supply Chain Issues**: The company faces risks related to supply chain disruptions, particularly with single-source suppliers. This could impact production timelines and costs.

- **Regulatory Changes**: Changes in government incentives for EVs and renewable energy could significantly impact Tesla's financial performance. The recent Inflation Reduction Act (IRA) may provide some benefits, but ongoing evaluation is necessary.

## Future Outlook

Tesla's future outlook appears cautiously optimistic, provided it can navigate the aforementioned risks effectively. The company's commitment to innovation and expansion into new markets, such as energy storage and solar products, may offer additional revenue streams. However, maintaining strong cash reserves and managing operational costs will be crucial for sustaining growth.

## Key Financial Metrics Comparison

Below is a comparison of key financial metrics between Tesla for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------------|:----------:|:----------:|:------------:|:----------:|
| Cash and cash equivalents   | 16,253.00  | 17,576.00  | -1,323.00    | -7.53%     |
| Sales                      | N/A        | N/A        | N/A          | N/A        |
| Total Assets               | N/A        | N/A        | N/A          | N/A        |
| Total Liabilities          | N/A        | N/A        | N/A          | N/A        |

*Note: Sales, Total Assets, and Total Liabilities data were not provided in the financial statements.*

## Conclusion

In summary, while Tesla shows a solid cash position, the decline in cash reserves and the lack of sales figures raise concerns about its financial health. The company must focus on improving revenue generation and managing risks associated with market dependency and supply chain issues to ensure a sustainable future. Further analysis and data would be beneficial for a more comprehensive assessment.

### Actionable Recommendations
- **Enhance Revenue Streams**: Explore new markets and product lines to diversify revenue sources.
- **Strengthen Cash Management**: Implement tighter controls on cash flow and operational expenses to mitigate the decline in cash reserves.
- **Monitor Supply Chain**: Develop alternative supplier relationships to reduce dependency on single-source suppliers and enhance resilience against disruptions.
- **Stay Informed on Regulations**: Continuously evaluate the impact of government policies and incentives on the business model and adjust strategies accordingly.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Financial Health Overview

Tesla's financial health can be assessed through various metrics, including cash reserves, sales performance, and overall asset management. Based on the latest financial statements, here are some key observations:

1. **Cash and Cash Equivalents**: As of December 31, 2022, Tesla reported cash and cash equivalents of $16.25 billion, a decrease of approximately 7.53% from $17.58 billion in 2021. This decline may indicate a need for careful cash management, especially in light of ongoing investments and operational costs.

2. **Sales and Revenue**: Tesla reported total revenues of $81.46 billion in 2022. This significant revenue figure provides context for the cash position and indicates strong sales performance despite the decline in cash reserves.

3. **Total Assets and Liabilities**: Tesla's total assets were reported at $82.34 billion, while total liabilities stood at $36.44 billion. This results in a healthy debt-to-equity ratio of approximately 0.125, indicating low leverage and a strong balance sheet.

4. **Working Capital**: The working capital of $14.21 billion suggests that Tesla has sufficient short-term assets to cover its short-term liabilities, which is a positive indicator of liquidity.

5. **Risk Assessment**: The Altman Z-Score for Tesla is 8.367, placing it in the "Safe Zone" with low bankruptcy risk. This score reflects strong financial stability, supported by a solid EBIT-to-assets ratio of 0.1659 and a high equity market value to liabilities ratio of 10.6751.

## Risks and Limitations

- **Market Dependency**: Tesla's performance is heavily reliant on the automotive market and the demand for electric vehicles (EVs). Any downturn in consumer interest or economic conditions could adversely affect sales.
  
- **Supply Chain Issues**: The company faces risks related to supply chain disruptions, particularly with single-source suppliers. This could impact production timelines and costs.

- **Regulatory Changes**: Changes in government incentives for EVs and renewable energy could significantly impact Tesla's financial performance. The recent Inflation Reduction Act (IRA) may provide some benefits, but ongoing evaluation is necessary.

- **Competitive Landscape**: The report does not address competition, which is a critical risk factor for Tesla, especially in the rapidly evolving EV market.

- **Margin Pressure**: Potential margin pressures due to rising costs or pricing strategies could impact profitability.

## Future Outlook

Tesla's future outlook appears cautiously optimistic, provided it can navigate the aforementioned risks effectively. The company's commitment to innovation and expansion into new markets, such as energy storage and solar products, may offer additional revenue streams. However, maintaining strong cash reserves and managing operational costs will be crucial for sustaining growth.

## Key Financial Metrics Comparison

Below is a comparison of key financial metrics between Tesla for the years 2022 and 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------------|:----------:|:----------:|:------------:|:----------:|
| Cash and cash equivalents   | 16,253.00  | 17,576.00  | -1,323.00    | -7.53%     |
| Total Revenues             | 81,462.00  | N/A        | N/A          | N/A        |

*Note: Total Revenues for 2021 were not provided in the financial statements.*

## Conclusion

In summary, while Tesla shows a solid cash position, the decline in cash reserves is a concern. However, the reported total revenues of $81.46 billion indicate strong sales performance. The company must focus on improving revenue generation and managing risks associated with market dependency and supply chain issues to ensure a sustainable future. Further analysis and data would be beneficial for a more comprehensive assessment.

### Actionable Recommendations
- **Enhance Revenue Streams**: Explore new markets and product lines to diversify revenue sources.
- **Strengthen Cash Management**: Implement tighter controls on cash flow and operational expenses to mitigate the decline in cash reserves.
- **Monitor Supply Chain**: Develop alternative supplier relationships to reduce dependency on single-source suppliers and enhance resilience against disruptions.
- **Stay Informed on Regulations**: Continuously evaluate the impact of government policies and incentives on the business model and adjust strategies accordingly.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's financial health and future outlook compared to the original report (v1). However, it still has one unresolved issue that needs to be addressed.

## Query Satisfaction
The revised report adequately answers the user query regarding Tesla's financial health and future outlook. It covers key financial metrics, risks, and actionable recommendations, fulfilling the user's request for advice based on the financial statements provided.

## Issues Resolution Status
Out of the five issues identified by the Critic, four have been successfully resolved in the revised report:
1. Total assets and liabilities are now included in the financial health assessment.
2. The relationship between cash reserves and total revenues has been clarified.
3. Competitive risks in the automotive market have been addressed.
4. Potential margin pressures affecting profitability have been discussed.

However, one issue remains unresolved:
- **Embed relevant figures or charts to support the analysis.**

## Remaining Gaps
- The report still lacks embedded figures or charts that could enhance the analysis and improve clarity for the reader.

## Recommendation
It is recommended that the advisor revise the report to include relevant figures or charts that support the analysis. This addition will enhance the overall quality and effectiveness of the report, ensuring it meets the expectations set by the Critic's feedback.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_15.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       50 |       85 |    +35 |
| Business Analysis    |    15%  |       40 |       60 |    +20 |
| Risk Assessment      |    15%  |       50 |       70 |    +20 |
| Actionable Advice    |    15%  |       60 |       75 |    +15 |
| Evidence Usage       |    10%  |       30 |       60 |    +30 |
| Completeness         |    10%  |       70 |       85 |    +15 |
| Query Satisfaction   |    10%  |       60 |       80 |    +20 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    51.00 |    74.50 |  +23.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +23.5 pts absolute  |  +46.08% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 50,
                "v2_score": 85,
                "delta": 35,
                "weighted_v1": 12.5,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 40,
                "v2_score": 60,
                "delta": 20,
                "weighted_v1": 6.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 70,
                "delta": 20,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 75,
                "delta": 15,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 30,
                "v2_score": 60,
                "delta": 30,
                "weighted_v1": 3.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 70,
                "v2_score": 85,
                "delta": 15,
                "weighted_v1": 7.0,
                "weighted_v2": 8.5
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 60,
                "v2_score": 80,
                "delta": 20,
                "weighted_v1": 6.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v1": 51.0,
        "overall_v2": 74.5,
        "absolute_improvement": 23.5,
        "improvement_percentage": 46.08
    }
