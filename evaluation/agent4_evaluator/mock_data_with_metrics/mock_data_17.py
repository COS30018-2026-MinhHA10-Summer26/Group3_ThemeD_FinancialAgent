"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_17.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Overview

Tesla's financial health as of December 31, 2022, shows significant improvement compared to the previous year. Key metrics indicate a strong liquidity position, reduced debt levels, and increased profitability. Below is a detailed analysis of Tesla's financial metrics, risk assessment, and future outlook.

## Key Financial Metrics Comparison

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Cash and Cash Equivalents  | 22,209     | 17,708     | +4,501       | +25.42%     |
| Inventory                  | 12,839     | 5,757      | +7,082       | +123.02%    |
| Net Income                 | 1,211      | 557        | +654         | +117.41%    |
| Total Assets               | 33,589     | 30,700     | +2,889       | +9.41%      |
| Total Debt                 | 2,061      | 5,380      | -3,319       | -61.69%     |
| Total Liabilities           | 20,661     | 19,300     | +1,361       | +7.05%      |

*Source: Data sourced from Tesla's financial statements.*

## Financial Health Analysis

### Liquidity and Cash Position
Tesla's cash and cash equivalents increased by 25.42% to $22.21 billion, indicating a strong liquidity position that can support operational needs and future investments.

### Inventory Management
The inventory has significantly increased by 123.02%, which may reflect higher production levels or potential challenges in sales. This warrants monitoring to ensure that inventory levels do not lead to excess stock or obsolescence.

### Profitability
Net income rose by 117.41% to $1.21 billion, showcasing improved operational efficiency and profitability. This positive trend is crucial for sustaining growth and investor confidence.

### Debt Reduction
Total debt decreased by 61.69% to $2.06 billion, which enhances Tesla's financial stability and reduces interest obligations. The liabilities to market capitalization ratio stands at 0.2583, indicating a manageable debt level relative to the company's market value.

## Risk Assessment

Using the Altman Z-Score, Tesla's score is 5.425, placing it in the "Safe Zone" with low bankruptcy risk. The components of the score are as follows:

- **Working Capital to Assets**: 0.448
- **Retained Earnings to Assets**: -0.0298
- **EBIT to Assets**: 0.0595
- **Equity Market Value to Liabilities**: 3.872
- **Sales to Assets**: 2.4115

These metrics indicate that Tesla is well-positioned to manage its financial obligations and sustain operations.

## Future Outlook

Tesla's strong cash position, reduced debt, and increasing profitability suggest a positive outlook for the company. However, the significant rise in inventory should be addressed to ensure it does not hinder cash flow or operational efficiency. Continued focus on production efficiency and market demand will be essential for maintaining growth.

### Actionable Advice
1. **Monitor Inventory Levels**: Implement strategies to manage inventory effectively to avoid excess stock.
2. **Leverage Cash Reserves**: Utilize cash reserves for strategic investments in technology and expansion to drive future growth.
3. **Debt Management**: Continue to focus on reducing debt levels to enhance financial flexibility.

## Conclusion

Tesla's financial health is robust, with strong liquidity, reduced debt, and improved profitability. By addressing inventory management and leveraging its cash reserves, Tesla can continue to thrive in the competitive automotive and energy markets.

![Comparison of Key Financial Metrics (2022 vs 2021)](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_fa39cbc2d176_comparison-of-key-financial-metrics-2022-vs-2021.png)

*Figure: Bar chart comparing key financial metrics for Tesla in 2022 and 2021.*

*Source: Data sourced from Tesla's financial statements.*


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Overview

Tesla's financial health as of December 31, 2022, shows significant improvement compared to the previous year. Key metrics indicate a strong liquidity position, reduced debt levels, and increased profitability. Below is a detailed analysis of Tesla's financial metrics, risk assessment, and future outlook.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Cash and Cash Equivalents  | 22,209     | 17,708     | +4,501       | +25.42%     |
| Inventory                  | 12,839     | 5,757      | +7,082       | +123.02%    |
| Net Income                 | 1,211      | 557        | +654         | +117.41%    |
| Total Assets               | 82,338     | 82,338     | +0           | +0.00%      |
| Total Debt                 | 5,748      | 5,748      | +0           | +0.00%      |
| Total Liabilities           | 36,440     | 36,440     | +0           | +0.00%      |

*Source: Data sourced from Tesla's financial statements.*

## Financial Health Analysis

### Liquidity and Cash Position
Tesla's cash and cash equivalents increased by 25.42% to $22.21 billion, indicating a strong liquidity position that can support operational needs and future investments. The working capital ratio is 0.1726, which suggests that while Tesla has a solid cash position, it should continue to monitor its current liabilities to ensure operational stability.

### Inventory Management
The inventory has significantly increased by 123.02%, which may reflect higher production levels or potential challenges in sales. This warrants monitoring to ensure that inventory levels do not lead to excess stock or obsolescence, which could impact cash flow and operational efficiency.

### Profitability
Net income rose by 117.41% to $1.21 billion, showcasing improved operational efficiency and profitability. This positive trend is crucial for sustaining growth and investor confidence.

### Debt Management
Total debt remained stable at $5.748 billion, which enhances Tesla's financial stability and reduces interest obligations. The liabilities to market capitalization ratio stands at 0.0937, indicating a manageable debt level relative to the company's market value.

## Risk Assessment

Using the Altman Z-Score, Tesla's score is 8.367, placing it in the "Safe Zone" with low bankruptcy risk. The components of the score are as follows:

- **Working Capital to Assets**: 0.1726
- **Retained Earnings to Assets**: 0.1565
- **EBIT to Assets**: 0.1659
- **Equity Market Value to Liabilities**: 10.6751
- **Sales to Assets**: 0.9894

These metrics indicate that Tesla is well-positioned to manage its financial obligations and sustain operations. However, it is essential to consider industry benchmarks for a more comprehensive view.

## Future Outlook

Tesla's strong cash position, stable debt levels, and increasing profitability suggest a positive outlook for the company. However, the significant rise in inventory should be addressed to ensure it does not hinder cash flow or operational efficiency. Continued focus on production efficiency and market demand will be essential for maintaining growth.

### Actionable Advice
1. **Monitor Inventory Levels**: Implement strategies to manage inventory effectively to avoid excess stock.
2. **Leverage Cash Reserves**: Utilize cash reserves for strategic investments in technology and expansion to drive future growth.
3. **Debt Management**: Continue to focus on maintaining stable debt levels to enhance financial flexibility.

## Conclusion

Tesla's financial health is robust, with strong liquidity, stable debt, and improved profitability. By addressing inventory management and leveraging its cash reserves, Tesla can continue to thrive in the competitive automotive and energy markets.

![Comparison of Key Financial Metrics (2022 vs 2021)](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_fa39cbc2d176_comparison-of-key-financial-metrics-2022-vs-2021.png)

*Figure: Bar chart comparing key financial metrics for Tesla in 2022 and 2021.*

*Source: Data sourced from Tesla's financial statements.*

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's financial health and future outlook compared to the original report (v1). However, it still fails to address several critical issues identified by the Critic, which limits its overall effectiveness.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's financial health and future outlook. It covers key financial metrics, provides an analysis of liquidity, profitability, and debt management, and includes actionable advice. Additionally, it incorporates a risk assessment, which was missing in the original report. However, the report does not fully meet the expectations due to unresolved issues related to competition, supply chain vulnerabilities, and regulatory risks.

## Issues Resolution Status
Out of the six issues identified by the Critic:
- **Resolved Issues**:
  1. Provided a detailed analysis of liquidity ratios and their implications.
  2. Clarified the significance of the Altman Z-Score with industry comparisons.
  3. Enhanced the figure's context with comparisons to industry standards or competitors.

- **Unresolved Issues**:
  1. Address competition as a critical risk factor.
  2. Discuss supply chain vulnerabilities and their potential impact.
  3. Include regulatory risks related to changing government policies.

The report has resolved 3 out of 6 issues, leaving 3 unresolved.

## Remaining Gaps
1. The report does not address competition as a critical risk factor, which is essential for understanding Tesla's market position.
2. There is no discussion of supply chain vulnerabilities, despite the context documents highlighting single-source supplier dependencies that could disrupt production.
3. Regulatory risks related to changing government policies and incentives are not mentioned, which could impact Tesla's sales and profitability.

## Recommendation
To enhance the quality and completeness of the report, the advisor should:
1. Include a thorough analysis of competitive pressures in the EV market and how they may affect Tesla's future performance.
2. Discuss supply chain vulnerabilities and their potential impact on production and financial health.
3. Address regulatory risks associated with changing government policies and incentives that could influence Tesla's operations and profitability.

By resolving these remaining gaps, the advisor can provide a more robust and comprehensive analysis that meets the user's needs and expectations.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_17.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       85 |       70 |    -15 |
| Business Analysis    |    15%  |       60 |       60 |     +0 |
| Risk Assessment      |    15%  |       80 |       85 |     +5 |
| Actionable Advice    |    15%  |       75 |       75 |     +0 |
| Evidence Usage       |    10%  |       80 |       80 |     +0 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       85 |       85 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    79.00 |    76.00 |   -3.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: -3.0 pts absolute  |  -3.8% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 85,
                "v2_score": 70,
                "delta": -15,
                "weighted_v1": 21.25,
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
                "v1_score": 80,
                "v2_score": 85,
                "delta": 5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 75,
                "v2_score": 75,
                "delta": 0,
                "weighted_v1": 11.25,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 80,
                "delta": 0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
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
                "v2_score": 85,
                "delta": 0,
                "weighted_v1": 8.5,
                "weighted_v2": 8.5
            }
        },
        "overall_v1": 79.0,
        "overall_v2": 76.0,
        "absolute_improvement": -3.0,
        "improvement_percentage": -3.8
    }
