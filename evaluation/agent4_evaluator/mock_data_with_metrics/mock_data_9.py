"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_9.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Overview of Financial Performance

Tesla has demonstrated significant growth in its financial performance for the year ended December 31, 2022, compared to 2021. The key highlights from the financial statements include:

- **Total Revenues**: Increased by **51%** to **$81.46 billion** in 2022 from **$53.82 billion** in 2021.
- **Cash and Cash Equivalents**: As of December 31, 2022, Tesla held **$16.25 billion** in cash and cash equivalents, indicating strong liquidity.
- **Total Liabilities**: Total liabilities stood at **$2.06 billion**, which is manageable given the revenue and cash position.

### Comparison of Key Financial Metrics

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022          | Tesla 2021          | Change (Abs)         | Change (%)         |
|----------------------------|---------------------|---------------------|----------------------|--------------------|
| Cash and Cash Equivalents  | $16,250,000,000.00  | N/A                 | N/A                  | N/A                |
| Short-term Investments      | $5,930,000,000.00   | N/A                 | N/A                  | N/A                |
| Total Revenues             | $81,462,000,000.00  | $53,823,000,000.00  | +$27,639,000,000.00  | +51.35%            |
| Total Liabilities           | $2,060,000,000.00   | N/A                 | N/A                  | N/A                |

### Financial Health Assessment

1. **Liquidity**: Tesla's cash and cash equivalents of **$16.25 billion** provide a strong liquidity position, enabling the company to fund operations and investments without immediate reliance on external financing.

2. **Revenue Growth**: The substantial increase in total revenues indicates robust demand for Tesla's products, particularly in automotive sales, which grew significantly due to increased deliveries and production capacity.

3. **Cost Management**: While revenues increased, the cost of revenues also rose, leading to a slight decrease in gross margins. The gross margin for total automotive decreased from **29.3%** to **28.5%**. This indicates that while Tesla is growing, it faces challenges in managing costs effectively, particularly with rising raw material and logistics costs.

4. **Debt Management**: With total liabilities at **$2.06 billion**, Tesla appears to be in a good position regarding debt management, especially given its revenue and cash reserves.

5. **Future Outlook**: Tesla's ongoing investments in production capacity and technology, including new Gigafactories, suggest a commitment to growth. The company expects capital expenditures between **$6 billion to $8 billion** in 2023, indicating confidence in future revenue generation.

## Conclusion

Tesla's financial health appears strong, characterized by significant revenue growth, robust liquidity, and manageable debt levels. However, the company must focus on improving cost management to maintain healthy profit margins. The outlook remains positive, supported by ongoing investments in production and technology.

### Additional Recommendations

- **Cost Control Measures**: Implement strategies to manage rising costs, particularly in raw materials and logistics, to protect profit margins.
- **Diversification of Revenue Streams**: Continue to explore and expand into new markets and product lines, such as energy generation and storage, to mitigate risks associated with automotive sales.
- **Monitoring Foreign Currency Risks**: Given Tesla's global operations, it should consider strategies to hedge against foreign currency fluctuations that could impact financial results.

### Chart of Key Financial Metrics

![Key Financial Metrics](https://example.com/path/to/your/chart.png) 

*Note: The chart link is a placeholder. Please replace it with the actual link generated from your data visualization tool.* 

This report provides a comprehensive overview of Tesla's financial health and strategic outlook based on the provided financial statements. For further analysis or specific inquiries, additional data may be required.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Overview of Financial Performance

Tesla has demonstrated significant growth in its financial performance for the year ended December 31, 2022, compared to 2021. The key highlights from the financial statements include:

- **Total Revenues**: Increased by **51%** to **$81.46 billion** in 2022 from **$53.82 billion** in 2021.
- **Cash and Cash Equivalents**: As of December 31, 2022, Tesla held **$16.25 billion** in cash and cash equivalents, indicating strong liquidity.
- **Total Liabilities**: Total liabilities stood at **$36.44 billion**, which is manageable given the revenue and cash position.

### Comparison of Key Financial Metrics

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022          | Tesla 2021          | Change (Abs)         | Change (%)         |
|----------------------------|---------------------|---------------------|----------------------|--------------------|
| Cash and Cash Equivalents  | $16,250,000,000.00  | N/A                 | N/A                  | N/A                |
| Total Revenues             | $81,462,000,000.00  | $53,823,000,000.00  | +$27,639,000,000.00  | +51.35%            |
| Total Liabilities           | $36,440,000,000.00  | N/A                 | N/A                  | N/A                |

### Financial Health Assessment

1. **Liquidity**: Tesla's cash and cash equivalents of **$16.25 billion** provide a strong liquidity position, enabling the company to fund operations and investments without immediate reliance on external financing.

2. **Revenue Growth**: The substantial increase in total revenues indicates robust demand for Tesla's products, particularly in automotive sales, which grew significantly due to increased deliveries and production capacity.

3. **Cost Management**: While revenues increased, the cost of revenues also rose, leading to a slight decrease in gross margins. The gross margin for total automotive decreased from **29.3%** to **28.5%**. This indicates that while Tesla is growing, it faces challenges in managing costs effectively, particularly with rising raw material and logistics costs.

4. **Debt Management**: With total liabilities at **$36.44 billion**, Tesla appears to be in a good position regarding debt management, especially given its revenue and cash reserves. The liabilities-to-market-cap ratio is approximately **0.0937**, indicating a manageable level of debt relative to its market capitalization.

5. **Future Outlook**: Tesla's ongoing investments in production capacity and technology, including new Gigafactories, suggest a commitment to growth. The company expects capital expenditures between **$6 billion to $8 billion** in 2023, indicating confidence in future revenue generation.

### Risk Assessment

- **Altman Z-Score**: Tesla's Altman Z-Score is **8.367**, placing it in the "Safe Zone" with a low bankruptcy risk. This score reflects strong working capital, retained earnings, and EBIT relative to total assets.
  
### Conclusion

Tesla's financial health appears strong, characterized by significant revenue growth, robust liquidity, and manageable debt levels. However, the company must focus on improving cost management to maintain healthy profit margins. The outlook remains positive, supported by ongoing investments in production and technology.

### Additional Recommendations

- **Cost Control Measures**: Implement strategies to manage rising costs, particularly in raw materials and logistics, to protect profit margins.
- **Diversification of Revenue Streams**: Continue to explore and expand into new markets and product lines, such as energy generation and storage, to mitigate risks associated with automotive sales.
- **Monitoring Foreign Currency Risks**: Given Tesla's global operations, it should consider strategies to hedge against foreign currency fluctuations that could impact financial results.

### Chart of Key Financial Metrics

![Key Financial Metrics](https://example.com/path/to/your/chart.png) 

*Note: The chart link is a placeholder. Please replace it with the actual link generated from your data visualization tool.* 

This report provides a comprehensive overview of Tesla's financial health and strategic outlook based on the provided financial statements. For further analysis or specific inquiries, additional data may be required.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more accurate and comprehensive overview of Tesla's financial health and future outlook compared to the original version. However, it still contains unresolved issues that need to be addressed.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, growth indicators, and provides advice, including risk assessments. Additionally, it includes a chart, although the link is a placeholder.

## Issues Resolution Status
Out of the six issues identified by the Critic:
- **Resolved Issues**:
  1. Corrected the total liabilities figure from **$2.06 billion** to **$36.44 billion**.
  2. Provided contextual analysis for revenue growth and liquidity.
  3. Addressed regulatory risks in the report.

- **Unresolved Issues**:
  1. Include discussion on valuation risks.
  2. Update the chart link to a valid Supabase-hosted URL.
  3. Add necessary metadata for visualizations.

## Remaining Gaps
The following issues remain unresolved:
1. **Valuation Risks**: The report does not discuss potential valuation risks, which is crucial for investors.
2. **Chart Link**: The chart link remains a placeholder and needs to be updated to a valid Supabase-hosted URL.
3. **Metadata for Visualizations**: The report lacks necessary metadata for the visualizations, which is essential for understanding the context and source of the data presented.

## Recommendation
It is recommended that the advisor address the unresolved issues by:
1. Including a discussion on valuation risks to provide a more comprehensive risk assessment.
2. Updating the chart link to a valid Supabase-hosted URL to ensure accessibility.
3. Adding necessary metadata for the visualizations to enhance clarity and context.

Addressing these gaps will improve the report's credibility and decision-grade quality, ensuring it meets the expectations set by the user query and the Critic's feedback.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_9.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       80 |       70 |    -10 |
| Business Analysis    |    15%  |       60 |       60 |     +0 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |       70 |       70 |     +0 |
| Evidence Usage       |    10%  |       50 |       50 |     +0 |
| Completeness         |    10%  |       80 |       80 |     +0 |
| Query Satisfaction   |    10%  |       80 |       80 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    60.50 |    68.50 |   +8.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +8.0 pts absolute  |  +13.22% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 80,
                "v2_score": 70,
                "delta": -10,
                "weighted_v1": 20.0,
                "weighted_v2": 17.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 60,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 70,
                "delta": 0,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 50,
                "v2_score": 50,
                "delta": 0,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 80,
                "delta": 0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 80,
                "delta": 0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v1": 60.5,
        "overall_v2": 68.5,
        "absolute_improvement": 8.0,
        "improvement_percentage": 13.22
    }
