"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_14.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Overview
Tesla has shown significant growth in its financial performance from 2021 to 2022. The company's net income attributable to common stockholders has increased dramatically, reflecting strong operational performance and market demand for its products.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :--- | :---: | :---: | :---: | :---: |
| Net income attributable to common stockholders | $12,556 million | $5,519 million | +$7,037 million | +127.50% |
| Weighted average shares used in computing net income per share of common stock, basic | 3,130 million | 2,959 million | +171 million | +5.78% |
| Weighted average shares used in computing net income per share of common stock, diluted | 3,475 million | 3,386 million | +89 million | +2.63% |

### Analysis
- **Net Income Growth**: The net income attributable to common stockholders increased by 127.50%, indicating a robust improvement in profitability. This growth can be attributed to increased sales and operational efficiencies.
- **Share Count Increase**: The increase in the weighted average shares used for calculating net income per share (both basic and diluted) suggests that Tesla is managing its equity effectively while still rewarding shareholders with increased earnings.

## Financial Health Assessment
While there is insufficient data to compute the Altman Z-Score for Tesla, the significant increase in net income suggests that Tesla is currently in a strong financial position. Alternative metrics such as the increase in net income and effective management of shares indicate a positive trend in financial health.

## Risk Assessment
Tesla's financial health is bolstered by its strong net income growth; however, potential risks include:
- **Supply Chain Risks**: Dependence on suppliers for critical components could impact production.
- **Market Competition**: The electric vehicle market is becoming increasingly competitive, which may affect future sales.
- **Regulatory Risks**: Changes in government policies regarding electric vehicles and renewable energy could impact operations.

## Future Outlook
Given the current trends in profitability and the increasing demand for electric vehicles and renewable energy solutions, Tesla appears well-positioned for future growth. The company’s investments in production capacity, technology, and market expansion are likely to contribute positively to its financial performance in the coming years.

## Conclusion
Tesla's financial health appears strong based on the substantial growth in net income and effective management of shares. Continued focus on innovation and market expansion will be crucial for sustaining this momentum.

### Chart of Key Financial Metrics
![Tesla Financial Metrics Comparison](https://supabase.io/your_chart_link_here)

*Note: The chart link is a placeholder and should be replaced with the actual link generated from the figure generation tool if applicable.* 

---

This report provides a concise overview of Tesla's financial health and future outlook based on the provided financial statements. If you need further analysis or specific metrics, please provide additional data or context.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Overview
Tesla has demonstrated remarkable growth in its financial performance from 2021 to 2022. The company's net income attributable to common stockholders has surged, reflecting strong operational performance and heightened market demand for its electric vehicles and energy solutions.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :--- | :---: | :---: | :---: | :---: |
| Net income attributable to common stockholders | $12,556 million | $5,519 million | +$7,037 million | +127.50% |
| Weighted average shares used in computing net income per share of common stock, basic | 3,130 million | 2,959 million | +171 million | +5.78% |
| Weighted average shares used in computing net income per share of common stock, diluted | 3,475 million | 3,386 million | +89 million | +2.63% |

### Analysis
- **Net Income Growth**: The net income attributable to common stockholders increased by 127.50%, indicating a robust improvement in profitability. This growth can be attributed to increased sales and operational efficiencies, particularly in the automotive segment.
- **Share Count Increase**: The increase in the weighted average shares used for calculating net income per share (both basic and diluted) suggests that Tesla is effectively managing its equity while rewarding shareholders with increased earnings.

## Financial Health Assessment
Tesla's Altman Z-Score is 8.367, placing it in the "Safe Zone" with low bankruptcy risk. This score reflects strong financial health, supported by the following metrics:
- **Debt to Equity Ratio**: 0.1252, indicating low leverage.
- **Interest Coverage Ratio**: 71.5, demonstrating strong ability to cover interest expenses.

These metrics, combined with the significant increase in net income, suggest that Tesla is currently in a strong financial position.

## Risk Assessment
While Tesla's financial health is bolstered by its strong net income growth, potential risks include:
- **Supply Chain Risks**: Dependence on suppliers for critical components could impact production and margins.
- **Market Competition**: The electric vehicle market is becoming increasingly competitive, which may affect future sales and profitability.
- **Regulatory Risks**: Changes in government policies regarding electric vehicles and renewable energy could impact operations and incentives.

## Future Outlook
Given the current trends in profitability and the increasing demand for electric vehicles and renewable energy solutions, Tesla appears well-positioned for future growth. The company’s investments in production capacity, technology, and market expansion are likely to contribute positively to its financial performance in the coming years.

## Conclusion
Tesla's financial health appears strong based on substantial growth in net income, effective management of shares, and favorable financial ratios. Continued focus on innovation and market expansion will be crucial for sustaining this momentum.

### Chart of Key Financial Metrics
| Metric | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| --- | --- | --- | --- | --- |
| Net income attributable to common stockholders | 12,556 | 5,519 | +7,037 | +127.50% |
| Weighted average shares used in computing net income per share of common stock, basic | 3,130 | 2,959 | +171 | +5.78% |
| Weighted average shares used in computing net income per share of common stock, diluted | 3,475 | 3,386 | +89 | +2.63% |

*Source: NASDAQ_TSLA_2022.pdf*

This report provides a comprehensive overview of Tesla's financial health and future outlook based on the provided financial statements. If you need further analysis or specific metrics, please provide additional data or context.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's financial health and future outlook compared to the original version. However, it still leaves some critical issues unresolved.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's financial health and future outlook. It covers key financial metrics, provides an analysis of growth, and discusses potential risks, which aligns with the user's request for advice based on the financial statements.

## Issues Resolution Status
Out of the six issues identified by the Critic, four have been resolved:
1. **Resolved**: Include additional financial metrics to support claims of financial health.
2. **Resolved**: Address the missing risk of valuation in the report.
3. **Resolved**: Explore potential impacts on margins and execution risks.
4. **Resolved**: Add a caption or source note for the chart.

However, two issues remain unresolved:
1. **Unresolved**: Provide a detailed breakdown of revenue sources and operational efficiencies.
2. **Unresolved**: Replace the placeholder chart link with an actual image.

## Remaining Gaps
1. The report still lacks a detailed breakdown of revenue sources and operational efficiencies contributing to the net income growth. This information is crucial for a more nuanced understanding of Tesla's financial performance.
2. The placeholder chart link has not been replaced with an actual image, which diminishes the report's visual credibility.

## Recommendation
To enhance the quality of the report and fully address the Critic's feedback, the advisor should:
1. Provide a detailed breakdown of revenue sources and operational efficiencies that contributed to the significant growth in net income.
2. Replace the placeholder chart link with an actual image to improve the report's visual presentation and credibility.

Addressing these remaining gaps will ensure a more robust and comprehensive analysis of Tesla's financial health and future outlook.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_14.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       80 |       90 |    +10 |
| Business Analysis    |    15%  |       70 |       80 |    +10 |
| Risk Assessment      |    15%  |       60 |       70 |    +10 |
| Actionable Advice    |    15%  |       50 |       60 |    +10 |
| Evidence Usage       |    10%  |       40 |       70 |    +30 |
| Completeness         |    10%  |       80 |       90 |    +10 |
| Query Satisfaction   |    10%  |       70 |       80 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    66.00 |    78.00 |  +12.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +12.0 pts absolute  |  +18.18% relative
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
                "v2_score": 90,
                "delta": 10,
                "weighted_v1": 20.0,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 70,
                "delta": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 60,
                "delta": 10,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 40,
                "v2_score": 70,
                "delta": 30,
                "weighted_v1": 4.0,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 90,
                "delta": 10,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v1": 66.0,
        "overall_v2": 78.0,
        "absolute_improvement": 12.0,
        "improvement_percentage": 18.18
    }
