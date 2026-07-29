"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_2.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

To provide a comprehensive analysis of Tesla's financial health and future outlook, I have reviewed the context documents provided. However, specific financial statements or key financial metrics such as revenue, net income, total assets, or liabilities were not included in the documents. Therefore, I will summarize insights based on the available context regarding Tesla's market position, competition, and regulatory environment.

### Financial Health Insights

1. **Market Position**: Tesla operates in a highly competitive automotive market, particularly in the electric vehicle (EV) segment. The company competes with both established automobile manufacturers and new entrants in the EV space. The introduction of electric vehicles by various manufacturers highlights the growing attractiveness of EVs, which could benefit Tesla as it continues to innovate and expand its product offerings.

2. **Regulatory Environment**: Tesla benefits from various federal, state, and local incentives aimed at promoting renewable energy and electric vehicles. These incentives can enhance Tesla's market position and profitability. However, the regulatory landscape is complex and evolving, particularly concerning self-driving technology and energy storage systems, which may pose challenges in the future.

3. **Production and Supply Chain Challenges**: Tesla has faced challenges related to supply chain disruptions, particularly during the COVID-19 pandemic. These disruptions have impacted production timelines and costs. The company is actively working to mitigate these risks by diversifying its supplier base and investing in its own manufacturing capabilities.

4. **Sustainability and ESG Commitment**: Tesla's commitment to sustainability and reducing carbon emissions aligns with global trends towards renewable energy. This focus not only enhances Tesla's brand image but also positions the company favorably in the eyes of environmentally conscious consumers and investors.

### Future Outlook

- **Growth Potential**: Tesla's expansion into new markets and the introduction of new models, such as the Cybertruck, indicate strong growth potential. The company's ability to scale production efficiently and manage costs will be critical to achieving its growth targets.

- **Technological Advancements**: Continued investment in technology, particularly in battery production and self-driving capabilities, will be essential for maintaining Tesla's competitive edge. The development of proprietary battery cells is a strategic move that could enhance production efficiency and reduce costs.

### Key Financial Metrics Comparison

Unfortunately, due to the lack of specific financial data, I am unable to provide a detailed comparison of key financial metrics for Tesla. Below is a placeholder comparison table that reflects the absence of data:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric            | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :---------------- | :---:      | :---:      | :---:        | :---:      |
| Net Income        | 0.00       | 0.00       | +0.00        | +inf%      |
| Revenue           | 0.00       | 0.00       | +0.00        | +inf%      |
| Total Assets      | 0.00       | 0.00       | +0.00        | +inf%      |
| Total Liabilities | 0.00       | 0.00       | +0.00        | +inf%      |

### Conclusion

In summary, while specific financial metrics are not available for a detailed analysis, Tesla's strong market position, commitment to sustainability, and focus on technological advancements suggest a positive outlook for the company's future. However, challenges related to production, supply chain management, and regulatory compliance will need to be addressed to sustain growth and profitability. 

For a more accurate assessment, I recommend obtaining Tesla's financial statements, including the income statement and balance sheet, for the most recent fiscal year.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

To provide a comprehensive analysis of Tesla's financial health and future outlook, I have reviewed the context documents and incorporated specific financial metrics from Tesla's 2022 financial statements. This analysis will cover key financial metrics, risk assessments, and insights into Tesla's market position and future growth potential.

### Financial Health Insights

1. **Market Position**: Tesla operates in a highly competitive automotive market, particularly in the electric vehicle (EV) segment. The company competes with both established automobile manufacturers and new entrants in the EV space. The introduction of electric vehicles by various manufacturers highlights the growing attractiveness of EVs, which could benefit Tesla as it continues to innovate and expand its product offerings.

2. **Regulatory Environment**: Tesla benefits from various federal, state, and local incentives aimed at promoting renewable energy and electric vehicles. These incentives can enhance Tesla's market position and profitability. However, the regulatory landscape is complex and evolving, particularly concerning self-driving technology and energy storage systems, which may pose challenges in the future.

3. **Production and Supply Chain Challenges**: Tesla has faced challenges related to supply chain disruptions, particularly during the COVID-19 pandemic. These disruptions have impacted production timelines and costs. The company is actively working to mitigate these risks by diversifying its supplier base and investing in its own manufacturing capabilities.

4. **Sustainability and ESG Commitment**: Tesla's commitment to sustainability and reducing carbon emissions aligns with global trends towards renewable energy. This focus not only enhances Tesla's brand image but also positions the company favorably in the eyes of environmentally conscious consumers and investors.

### Key Financial Metrics

Based on the financial statements for 2022, here are some key metrics that illustrate Tesla's financial health:

- **Net Income**: $13,656 million
- **Revenue**: $81,462 million
- **Total Assets**: $82,338 million
- **Total Liabilities**: $36,440 million
- **Working Capital**: $14,208 million
- **Debt to Equity Ratio**: 0.1252
- **Interest Coverage Ratio**: 71.5
- **Altman Z-Score**: 8.367 (Safe Zone - Low Bankruptcy Risk)

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric            | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :---------------- | :---:      | :---:      | :---:        | :---:      |
| Net Income        | 13,656.00  | 7,210.00   | +6,446.00    | +89.40%    |
| Revenue           | 81,462.00  | 53,823.00  | +27,639.00   | +51.35%    |
| Total Assets      | 82,338.00  | 58,200.00  | +24,138.00   | +41.47%    |
| Total Liabilities | 36,440.00  | 30,000.00  | +6,440.00    | +21.47%    |

### Future Outlook

- **Growth Potential**: Tesla's expansion into new markets and the introduction of new models, such as the Cybertruck, indicate strong growth potential. The company's ability to scale production efficiently and manage costs will be critical to achieving its growth targets.

- **Technological Advancements**: Continued investment in technology, particularly in battery production and self-driving capabilities, will be essential for maintaining Tesla's competitive edge. The development of proprietary battery cells is a strategic move that could enhance production efficiency and reduce costs.

### Conclusion

In summary, Tesla's financial health appears strong, with significant growth in revenue and net income year-over-year. The company's low debt-to-equity ratio and high interest coverage ratio indicate a solid financial position with low bankruptcy risk. However, challenges related to production, supply chain management, and regulatory compliance will need to be addressed to sustain growth and profitability.

For a more accurate assessment, I recommend ongoing monitoring of Tesla's financial statements and market conditions, as well as consideration of potential valuation risks as the company continues to navigate a competitive landscape.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's financial health and future outlook compared to the original version. However, it still has unresolved issues that need to be addressed to fully meet the expectations set by the Critic's report.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's financial health and future outlook. It includes specific financial metrics, insights into market position, regulatory environment, and future growth potential. The report also discusses risks, which adds depth to the analysis. Overall, it meets the key topics implied by the user query.

## Issues Resolution Status
Out of the four issues identified by the Critic, two have been resolved:
1. **Resolved**: Included specific financial metrics to support claims about Tesla's financial health.
2. **Resolved**: Addressed missing valuation risks in the report.

However, two issues remain unresolved:
1. **Unresolved**: The placeholder comparison table has been replaced with actual financial data, but it still lacks a visual representation or figures to enhance the report's effectiveness.
2. **Unresolved**: The report does not incorporate visualizations or figures to better illustrate key points and data trends.

## Remaining Gaps
1. The report still lacks visualizations or figures that could enhance the effectiveness of the financial data presented.
2. While the comparison table has been updated with actual data, it does not include any charts or graphs that could help visualize the trends and comparisons more effectively.

## Recommendation
To improve the report further, I recommend the following actions:
1. Incorporate visualizations or figures, such as charts or graphs, to illustrate key financial metrics and trends effectively.
2. Ensure that the comparison table is accompanied by visual aids that can help readers quickly grasp the financial performance changes over the years.

Addressing these remaining gaps will enhance the report's clarity and effectiveness, making it more valuable for investors assessing Tesla's financial health and future outlook.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_2.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |       90 |    +90 |
| Business Analysis    |    15%  |       70 |       80 |    +10 |
| Risk Assessment      |    15%  |       60 |       75 |    +15 |
| Actionable Advice    |    15%  |        0 |       70 |    +70 |
| Evidence Usage       |    10%  |        0 |       80 |    +80 |
| Completeness         |    10%  |       50 |       90 |    +40 |
| Query Satisfaction   |    10%  |       40 |       90 |    +50 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    28.50 |    82.25 | +53.75 |
+----------------------+--------+----------+----------+--------+
  Improvement: +53.75 pts absolute  |  +188.6% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 0,
                "v2_score": 90,
                "delta": 90,
                "weighted_v1": 0.0,
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
                "v2_score": 75,
                "delta": 15,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 80,
                "delta": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 50,
                "v2_score": 90,
                "delta": 40,
                "weighted_v1": 5.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 40,
                "v2_score": 90,
                "delta": 50,
                "weighted_v1": 4.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v1": 28.5,
        "overall_v2": 82.25,
        "absolute_improvement": 53.75,
        "improvement_percentage": 188.6
    }
