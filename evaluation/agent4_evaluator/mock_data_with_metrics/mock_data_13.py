"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_13.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

## Overview
Tesla, Inc. has shown significant growth in its financial performance from 2021 to 2022. The company's revenue streams from automotive sales, energy generation, and services have all increased substantially, indicating a robust demand for its products and services.

## Key Financial Metrics Comparison

The following table summarizes the key financial metrics for Tesla in 2022 compared to 2021:

| Metric                               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|--------------------------------------|:----------:|:----------:|:------------:|:----------:|
| Automotive regulatory credits         | 1,776.00   | 1,465.00   | +311.00      | +21.23%    |
| Automotive sales                     | 67,210.00  | 44,125.00  | +23,085.00   | +52.32%    |
| Energy generation and storage sales   | 3,376.00   | 2,279.00   | +1,097.00    | +48.14%    |
| Services and other                   | 6,091.00   | 3,802.00   | +2,289.00    | +60.21%    |
| **Total revenues**                   | **81,462.00** | **53,823.00** | **+27,639.00** | **+51.35%** |

### Insights
1. **Automotive Sales Growth**: The automotive sales revenue increased by 52.32%, which is a strong indicator of Tesla's market position and consumer demand. This growth can be attributed to the expanding product lineup and increased production capacity.

2. **Energy Generation and Storage**: The energy segment also saw a significant increase of 48.14%, reflecting Tesla's commitment to diversifying its revenue streams beyond automotive sales.

3. **Services and Other Revenue**: This segment grew by 60.21%, indicating that Tesla is successfully monetizing its after-sales services and related offerings, which can enhance customer loyalty and recurring revenue.

4. **Total Revenue Increase**: Overall, total revenues increased by 51.35%, showcasing Tesla's strong operational performance and market expansion.

## Financial Health Assessment
While the Altman Z-Score could not be computed due to insufficient data, the substantial revenue growth and diversification of income sources suggest that Tesla is in a healthy financial position. Specifically, additional information on liabilities, working capital, and other financial metrics would be necessary for a comprehensive risk assessment.

### Additional Data Needed for Altman Z-Score
To compute the Altman Z-Score, the following financial metrics are required:
- Working Capital
- Total Assets
- Retained Earnings
- EBIT (Earnings Before Interest and Taxes)
- Market Capitalization
- Total Liabilities

## Future Outlook
Tesla's growth trajectory appears promising, driven by:
- **Increased Production Capacity**: Continued investments in manufacturing facilities and technology.
- **Expansion into New Markets**: Ongoing efforts to penetrate international markets and diversify product offerings.
- **Innovation in Energy Solutions**: A focus on renewable energy products and services, aligning with global sustainability trends.

### Recommendations
- **Monitor Market Trends**: Keep an eye on consumer preferences and regulatory changes that may impact sales.
- **Enhance Operational Efficiency**: Focus on reducing costs and improving margins through better supply chain management.
- **Invest in R&D**: Continue to innovate in both automotive and energy sectors to maintain competitive advantage.

## Conclusion
Tesla's financial performance in 2022 demonstrates strong growth and resilience. With strategic investments and a focus on innovation, the company is well-positioned for future success. Further analysis of liabilities and other financial metrics will provide a more detailed understanding of its financial health.

![Key Financial Metrics Comparison](https://supabase.io/your_image_link_here)

*Source: Tesla 2022 Financial Statements (NASDAQ_TSLA_2022.pdf)*


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

## Overview
Tesla, Inc. has demonstrated remarkable growth in its financial performance from 2021 to 2022. The company's revenue streams from automotive sales, energy generation, and services have all increased significantly, indicating robust demand for its products and services. This report provides a detailed analysis of Tesla's financial health, including key metrics, risk assessments, and future outlook.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                               | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|--------------------------------------|:----------:|:----------:|:------------:|:----------:|
| Automotive regulatory credits         | 1,776.00   | 1,465.00   | +311.00      | +21.23%    |
| Automotive sales                     | 67,210.00  | 44,125.00  | +23,085.00   | +52.32%    |
| Energy generation and storage sales   | 3,376.00   | 2,279.00   | +1,097.00    | +48.14%    |
| Services and other                   | 6,091.00   | 3,802.00   | +2,289.00    | +60.21%    |
| **Total revenues**                   | **81,462.00** | **53,823.00** | **+27,639.00** | **+51.35%** |

### Insights
1. **Automotive Sales Growth**: The automotive sales revenue increased by 52.32%, indicating a strong market position and consumer demand. This growth can be attributed to the expanding product lineup and increased production capacity.

2. **Energy Generation and Storage**: The energy segment also saw a significant increase of 48.14%, reflecting Tesla's commitment to diversifying its revenue streams beyond automotive sales.

3. **Services and Other Revenue**: This segment grew by 60.21%, indicating successful monetization of after-sales services and related offerings, enhancing customer loyalty and recurring revenue.

4. **Total Revenue Increase**: Overall, total revenues increased by 51.35%, showcasing Tesla's strong operational performance and market expansion.

## Financial Health Assessment
The Altman Z-Score could not be computed due to insufficient data. However, the substantial revenue growth and diversification of income sources suggest that Tesla is in a healthy financial position. Here are some key financial metrics:

- **Working Capital**: $14,208 million
- **Total Assets**: $82,338 million
- **Retained Earnings**: $12,885 million
- **EBIT (Earnings Before Interest and Taxes)**: $13,656 million
- **Market Capitalization**: $389,000 million
- **Total Liabilities**: $36,440 million

### Risk Assessment
- **Liabilities to Market Capitalization Ratio**: 0.0937, indicating that Tesla's liabilities are manageable relative to its market value.
- **Supply Chain Risks**: Tesla faces risks related to single-source supplier dependencies for key components, which could disrupt operations.

## Future Outlook
Tesla's growth trajectory appears promising, driven by:
- **Increased Production Capacity**: Continued investments in manufacturing facilities and technology.
- **Expansion into New Markets**: Ongoing efforts to penetrate international markets and diversify product offerings.
- **Innovation in Energy Solutions**: A focus on renewable energy products and services, aligning with global sustainability trends.

### Recommendations
- **Monitor Market Trends**: Keep an eye on consumer preferences and regulatory changes that may impact sales.
- **Enhance Operational Efficiency**: Focus on reducing costs and improving margins through better supply chain management.
- **Invest in R&D**: Continue to innovate in both automotive and energy sectors to maintain competitive advantage.

## Conclusion
Tesla's financial performance in 2022 demonstrates strong growth and resilience. With strategic investments and a focus on innovation, the company is well-positioned for future success. Further analysis of liabilities and other financial metrics will provide a more detailed understanding of its financial health.

![Key Financial Metrics Comparison](https://supabase.io/your_image_link_here)

*Source: Tesla 2022 Financial Statements (NASDAQ_TSLA_2022.pdf)*

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Tesla's financial health and future outlook. However, it does not fully address all the issues identified by the Critic, leaving several gaps that need to be resolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, insights, risk assessments, and recommendations, fulfilling the user's request for advice based on the financial statements.

## Issues Resolution Status
Out of the six issues identified by the Critic:
- **Resolved Issues**:
  1. Address competitive risks in the analysis.
  2. Elaborate on supply chain vulnerabilities and their potential impact.

- **Unresolved Issues**:
  1. Provide context for financial metrics and comparisons to industry standards.
  2. Verify and support all financial figures with appropriate citations.
  3. Update the image link to a supported format and ensure proper storage.
  4. Add descriptive captions or source notes for figures.

## Remaining Gaps
The following issues remain unresolved:
1. **Context for Financial Metrics**: The report lacks comparisons to industry benchmarks or competitors, which would strengthen the claims about growth.
2. **Verification of Financial Figures**: The report does not provide appropriate citations or sources for the financial figures presented.
3. **Image Link Issues**: The image link provided does not point to a supported format, and there is no confirmation of proper storage.
4. **Descriptive Captions**: The figure lacks descriptive captions or source notes, which are essential for understanding the context of the data.

## Recommendation
To enhance the quality and reliability of the report, the advisor should:
1. Include context for financial metrics by comparing them to industry standards or competitors.
2. Ensure all financial figures are verified and supported with appropriate citations.
3. Update the image link to a supported format and confirm its proper storage.
4. Add descriptive captions or source notes for figures to provide clarity and context.

Addressing these remaining gaps will ensure the report meets the necessary standards for decision-making and provides a complete analysis of Tesla's financial health and future outlook.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_13.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       75 |       90 |    +15 |
| Business Analysis    |    15%  |       60 |       70 |    +10 |
| Risk Assessment      |    15%  |       50 |       75 |    +25 |
| Actionable Advice    |    15%  |       70 |       80 |    +10 |
| Evidence Usage       |    10%  |       60 |       80 |    +20 |
| Completeness         |    10%  |       80 |       90 |    +10 |
| Query Satisfaction   |    10%  |       70 |       85 |    +15 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    66.75 |    81.75 |  +15.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +15.0 pts absolute  |  +22.47% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 75,
                "v2_score": 90,
                "delta": 15,
                "weighted_v1": 18.75,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 70,
                "delta": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 75,
                "delta": 25,
                "weighted_v1": 7.5,
                "weighted_v2": 11.25
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
                "v1_score": 60,
                "v2_score": 80,
                "delta": 20,
                "weighted_v1": 6.0,
                "weighted_v2": 8.0
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
                "v2_score": 85,
                "delta": 15,
                "weighted_v1": 7.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v1": 66.75,
        "overall_v2": 81.75,
        "absolute_improvement": 15.0,
        "improvement_percentage": 22.47
    }
