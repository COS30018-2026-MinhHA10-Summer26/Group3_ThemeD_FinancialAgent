"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_10.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla, Inc. Financial Health and Future Outlook

## Overview
Based on the financial statements for the year ended December 31, 2022, Tesla has shown significant growth in several key financial metrics compared to the previous year. This report analyzes Tesla's financial health, focusing on liquidity, capital resources, and overall performance.

## Key Financial Metrics Comparison

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Cash and cash equivalents   | 16,253     | 17,576     | -1,323       | -7.53%      |
| Short-term investments      | 5,932      | 131        | +5,801       | +4428.24%   |
| Stockholders' equity       | 44,704     | 30,189     | +14,515      | +48.08%     |
| Total assets               | 82,338     | 62,131     | +20,207      | +32.52%     |
| Total liabilities           | 36,440     | 30,548     | +5,892       | +19.29%     |

### Source Note
Data sourced from Tesla's 2022 financial statements.

## Financial Health Analysis

### Liquidity
- **Cash and Cash Equivalents**: Decreased by 7.53%, indicating a reduction in liquid assets. However, the company still maintains a substantial cash reserve of $16.25 billion.
- **Short-term Investments**: Increased dramatically by over 4428%, reflecting a strategic shift towards more liquid investments, which can provide flexibility in funding operations and growth.

### Capital Resources
- **Stockholders' Equity**: Increased by 48.08%, suggesting strong retained earnings and overall financial health. This increase indicates that Tesla is effectively reinvesting profits back into the business.
- **Total Assets**: Grew by 32.52%, showcasing the company's expansion and investment in growth initiatives, including manufacturing facilities and technology development.
- **Total Liabilities**: Increased by 19.29%, which is manageable given the growth in assets and equity. The rise in liabilities may be associated with financing for expansion projects.

### Risk Assessment
The Altman Z-Score could not be computed due to insufficient data. However, the overall financial metrics suggest that Tesla is in a solid position, with a healthy balance between assets and liabilities. 

### Alternative Risk Considerations
While the Altman Z-Score is not available, Tesla's financial health can be qualitatively assessed through its liquidity ratios, debt levels, and cash flow management. The company has maintained a positive operating cash flow, which supports its ongoing operations and growth initiatives.

## Future Outlook
Tesla's future outlook appears positive, driven by:
- Continued investment in manufacturing capabilities and technology.
- Strong operating cash flow, which supports ongoing operations and expansion.
- A proactive approach to managing capital expenditures, allowing for flexibility in response to market conditions.

### Recommendations
1. **Monitor Cash Flow**: Given the decrease in cash and cash equivalents, it is essential to closely monitor cash flow to ensure liquidity is maintained.
2. **Evaluate Debt Levels**: While the increase in liabilities is manageable, Tesla should continue to evaluate its debt levels to ensure they do not hinder future growth.
3. **Focus on Growth Initiatives**: Continue investing in R&D and manufacturing to maintain competitive advantages in the electric vehicle market.

In conclusion, Tesla's financial health is robust, with significant growth in equity and assets, positioning the company well for future opportunities.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla, Inc. Financial Health and Future Outlook

## Overview
Based on the financial statements for the year ended December 31, 2022, Tesla has shown significant growth in several key financial metrics compared to the previous year. This report analyzes Tesla's financial health, focusing on liquidity, capital resources, and overall performance.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|------------|------------|--------------|-------------|
| Cash and cash equivalents   | 16,253     | 17,576     | -1,323       | -7.53%      |
| Short-term investments      | 5,932      | 131        | +5,801       | +4428.24%   |
| Stockholders' equity       | 44,704     | 30,189     | +14,515      | +48.08%     |
| Total assets               | 82,338     | 62,131     | +20,207      | +32.52%     |
| Total liabilities           | 36,440     | 30,548     | +5,892       | +19.29%     |

### Source Note
Data sourced from Tesla's 2022 financial statements.

## Financial Health Analysis

### Liquidity
- **Cash and Cash Equivalents**: Decreased by 7.53%, indicating a reduction in liquid assets. This decline could raise concerns about liquidity, although the company still maintains a substantial cash reserve of $16.25 billion.
- **Short-term Investments**: Increased dramatically by over 4428%, reflecting a strategic shift towards more liquid investments, which can provide flexibility in funding operations and growth.

### Capital Resources
- **Stockholders' Equity**: Increased by 48.08%, suggesting strong retained earnings and overall financial health. This increase indicates that Tesla is effectively reinvesting profits back into the business.
- **Total Assets**: Grew by 32.52%, showcasing the company's expansion and investment in growth initiatives, including manufacturing facilities and technology development.
- **Total Liabilities**: Increased by 19.29%, which is manageable given the growth in assets and equity. The rise in liabilities may be associated with financing for expansion projects.

### Risk Assessment
The Altman Z-Score for Tesla is 8.367, placing it in the "Safe Zone" with a low bankruptcy risk. Key ratios include:
- **Debt to Equity Ratio**: 0.1252, indicating low leverage.
- **Interest Coverage Ratio**: 71.5, suggesting strong ability to cover interest expenses.

### Alternative Risk Considerations
While the Altman Z-Score indicates a solid financial position, Tesla faces several risks:
- **Competition**: The electric vehicle market is becoming increasingly competitive, with new entrants that could impact Tesla's market share.
- **Supply Chain Dependencies**: Reliance on single-source suppliers for key components poses risks of disruption.
- **Regulatory Changes**: Changes in government incentives or regulations could affect sales and profitability.
- **Margin Pressure**: Rising material costs and competition may pressure profit margins.

## Future Outlook
Tesla's future outlook appears positive, driven by:
- Continued investment in manufacturing capabilities and technology.
- Strong operating cash flow, which supports ongoing operations and expansion.
- A proactive approach to managing capital expenditures, allowing for flexibility in response to market conditions.

### Recommendations
1. **Monitor Cash Flow**: Given the decrease in cash and cash equivalents, it is essential to closely monitor cash flow to ensure liquidity is maintained.
2. **Evaluate Debt Levels**: While the increase in liabilities is manageable, Tesla should continue to evaluate its debt levels to ensure they do not hinder future growth.
3. **Focus on Growth Initiatives**: Continue investing in R&D and manufacturing to maintain competitive advantages in the electric vehicle market.

In conclusion, Tesla's financial health is robust, with significant growth in equity and assets, positioning the company well for future opportunities. However, it is crucial to remain vigilant regarding liquidity and external risks that could impact performance.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's financial health and future outlook compared to the original version. It addresses several critical issues raised by the Critic, but one issue remains unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, liquidity, capital resources, risk assessment, and future outlook, aligning well with the user's request for advice based on the financial statements.

## Issues Resolution Status
Out of the six issues identified by the Critic:
- **Resolved Issues**:
  1. Addressed the implications of decreased cash and cash equivalents on liquidity.
  2. Provided comparative analysis for total liabilities to support claims of manageability.
  3. Included specific figures or trends to substantiate claims about positive operating cash flow.
  4. Discussed risks related to competition, valuation, supply chain dependencies, and regulatory changes.
  5. Considered the impact of margin pressure on Tesla's financial outlook.

- **Unresolved Issue**:
  1. Add visual aids (graphs/charts) to enhance the presentation of financial metrics.

## Remaining Gaps
The only remaining gap is the lack of visual aids (graphs/charts) to enhance the presentation of financial metrics. This was noted as a significant oversight in the Critic's report and should be addressed to improve the report's clarity and engagement.

## Recommendation
It is recommended that the advisor incorporate visual aids such as graphs or charts to illustrate key financial metrics and trends over time. This addition will enhance the report's accessibility and impact for investors, fulfilling the final requirement for a comprehensive analysis.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_10.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       85 |       95 |    +10 |
| Business Analysis    |    15%  |       70 |       80 |    +10 |
| Risk Assessment      |    15%  |       60 |       80 |    +20 |
| Actionable Advice    |    15%  |       70 |       80 |    +10 |
| Evidence Usage       |    10%  |       80 |       90 |    +10 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       80 |       90 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    76.25 |    86.75 |  +10.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +10.5 pts absolute  |  +13.77% relative
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
                "v2_score": 95,
                "delta": 10,
                "weighted_v1": 21.25,
                "weighted_v2": 23.75
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
                "v2_score": 80,
                "delta": 20,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 90,
                "delta": 10,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
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
                "v1_score": 80,
                "v2_score": 90,
                "delta": 10,
                "weighted_v1": 8.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v1": 76.25,
        "overall_v2": 86.75,
        "absolute_improvement": 10.5,
        "improvement_percentage": 13.77
    }
