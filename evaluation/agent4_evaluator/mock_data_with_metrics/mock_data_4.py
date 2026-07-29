"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_4.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla Financial Health and Future Outlook

Based on the available context and analysis, here is an overview of Tesla's financial health and future outlook.

## Financial Health Assessment

### Risk Assessment
Tesla's Altman Z-Score is **2.477**, indicating a **Gray Zone (Moderate Bankruptcy Risk)**. This score suggests that while Tesla is in a relatively stable financial position, there are moderate risks associated with its financial health. Key metrics contributing to this score include:

- **Working Capital to Assets**: 0.02
- **Retained Earnings to Assets**: 0.04
- **EBIT to Assets**: 0.06
- **Equity Market Value to Liabilities**: 2.0
- **Sales to Assets**: 1.0

Additionally, Tesla's liabilities represent **50%** of its market capitalization, which indicates a significant level of debt relative to its equity.

## Key Financial Metrics Comparison

Here is a comparison of key financial metrics for Tesla in 2022 versus 2021:

| Metric               | Tesla 2022         | Tesla 2021         | Change (Abs)         | Change (%)         |
|----------------------|--------------------|--------------------|-----------------------|---------------------|
| Equity                | $20,000,000,000.00 | $20,000,000,000.00 | +$0.00                | +0.00%              |
| Net Income            | $3,000,000,000.00  | $2,500,000,000.00  | +$500,000,000.00      | +20.00%             |
| Revenue               | $50,000,000,000.00 | $40,000,000,000.00 | +$10,000,000,000.00   | +25.00%             |
| Total Assets          | $50,000,000,000.00 | $45,000,000,000.00 | +$5,000,000,000.00    | +11.11%             |
| Total Liabilities     | $30,000,000,000.00 | $25,000,000,000.00 | +$5,000,000,000.00    | +20.00%             |

### Analysis
- **Revenue Growth**: Tesla's revenue increased by **25%** from 2021 to 2022, reflecting strong demand for its electric vehicles and energy products.
- **Net Income Growth**: The net income rose by **20%**, indicating improved profitability alongside revenue growth.
- **Asset Growth**: Total assets increased by **11.11%**, which is a positive sign of expanding operations and investments.
- **Liabilities Increase**: While total liabilities also increased by **20%**, the growth in assets and equity suggests that Tesla is managing its debt effectively.

## Future Outlook
Tesla's future outlook appears positive, driven by:
- Continued demand for electric vehicles and energy solutions.
- Strong financial metrics indicating moderate bankruptcy risk.
- Ongoing investments in production capacity and technology.

However, Tesla must navigate challenges such as competition, supply chain issues, and regulatory environments. Maintaining operational efficiency and managing costs will be crucial for sustaining growth.

### Conclusion
Overall, Tesla is in a stable financial position with a promising outlook, but it must remain vigilant against industry challenges. The company's ability to innovate and adapt will be key to its continued success in the competitive automotive and energy markets.

### Chart of Key Financial Metrics
![Comparison of Key Financial Metrics for Tesla (2022 vs 2021)](https://example.com/path/to/your/chart.png)


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla Financial Health and Future Outlook

Based on the available context and analysis, here is an overview of Tesla's financial health and future outlook.

## Financial Health Assessment

### Risk Assessment
Tesla's Altman Z-Score is **8.367**, indicating a **Safe Zone (Low Bankruptcy Risk)**. This score suggests that Tesla is in a strong financial position with minimal risk of bankruptcy. Key metrics contributing to this score include:

- **Working Capital to Assets**: 0.1726
- **Retained Earnings to Assets**: 0.1565
- **EBIT to Assets**: 0.1659
- **Equity Market Value to Liabilities**: 10.6751
- **Sales to Assets**: 0.9894

Additionally, Tesla's liabilities represent approximately **9.37%** of its market capitalization, indicating a manageable level of debt relative to its equity.

## Key Financial Metrics Comparison

Here is a comparison of key financial metrics for Tesla in 2022 versus 2021:

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric               | Tesla 2022         | Tesla 2021         | Change (Abs)         | Change (%)         |
|----------------------|--------------------|--------------------|-----------------------|---------------------|
| Equity                | $45,898,000,000.00 | $20,000,000,000.00 | +$25,898,000,000.00   | +129.49%            |
| Net Income            | $12,100,000,000.00 | $2,500,000,000.00  | +$9,600,000,000.00    | +384.00%            |
| Revenue               | $81,462,000,000.00 | $50,000,000,000.00 | +$31,462,000,000.00   | +62.92%             |
| Total Assets          | $82,338,000,000.00 | $50,000,000,000.00 | +$32,338,000,000.00   | +64.68%             |
| Total Liabilities     | $36,440,000,000.00 | $30,000,000,000.00 | +$6,440,000,000.00    | +21.47%             |

### Analysis
- **Revenue Growth**: Tesla's revenue increased by **62.92%** from 2021 to 2022, reflecting strong demand for its electric vehicles and energy products.
- **Net Income Growth**: The net income rose by **384.00%**, indicating significant improvement in profitability alongside revenue growth.
- **Asset Growth**: Total assets increased by **64.68%**, which is a positive sign of expanding operations and investments.
- **Liabilities Increase**: While total liabilities also increased by **21.47%**, the growth in assets and equity suggests that Tesla is managing its debt effectively.

## Future Outlook
Tesla's future outlook appears positive, driven by:
- Continued demand for electric vehicles and energy solutions.
- Strong financial metrics indicating low bankruptcy risk.
- Ongoing investments in production capacity and technology.

However, Tesla must navigate challenges such as competition, supply chain issues, and regulatory environments. Additionally, margin pressure could arise due to increased competition in the EV market. Maintaining operational efficiency and managing costs will be crucial for sustaining growth.

### Conclusion
Overall, Tesla is in a stable financial position with a promising outlook, but it must remain vigilant against industry challenges. The company's ability to innovate and adapt will be key to its continued success in the competitive automotive and energy markets.

### Chart of Key Financial Metrics
![Comparison of Key Financial Metrics for Tesla (2022 vs 2021)](https://example.com/path/to/your/chart.png)  
*Source: Financial data derived from Tesla's consolidated financial statements.*

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Tesla's financial health and future outlook. However, it still has unresolved issues that need to be addressed to ensure the report's reliability and completeness.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, risk assessments, and provides a future outlook, fulfilling the user's request for advice based on the financial statements.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  - [Add citations and evidence for all financial claims and metrics.]
  - [Address missing risks, particularly margin pressure and regulatory challenges.]
  
- **Unresolved Issues**:
  - [Clarify the methodology behind the Altman Z-Score and its implications.]
  - [Ensure all figures are consistent with the provided context documents.]
  - [Update the chart to use a Supabase-hosted link and include a caption or source note.]

## Remaining Gaps
The following issues remain unresolved:
1. Clarification of the methodology behind the Altman Z-Score and its implications.
2. Consistency of all figures with the provided context documents.
3. Update of the chart to use a Supabase-hosted link and inclusion of a caption or source note.

## Recommendation
It is recommended that the advisor address the unresolved issues to enhance the report's credibility and completeness. Specifically, the methodology for the Altman Z-Score should be explained, all figures should be verified against the context documents, and the chart should be updated to ensure accessibility and proper citation.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_4.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       70 |       90 |    +20 |
| Business Analysis    |    15%  |       60 |       75 |    +15 |
| Risk Assessment      |    15%  |       60 |       85 |    +25 |
| Actionable Advice    |    15%  |       50 |       70 |    +20 |
| Evidence Usage       |    10%  |       50 |       70 |    +20 |
| Completeness         |    10%  |       80 |       90 |    +10 |
| Query Satisfaction   |    10%  |       70 |       85 |    +15 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    63.00 |    81.50 |  +18.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +18.5 pts absolute  |  +29.37% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 70,
                "v2_score": 90,
                "delta": 20,
                "weighted_v1": 17.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 75,
                "delta": 15,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 85,
                "delta": 25,
                "weighted_v1": 9.0,
                "weighted_v2": 12.75
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 50,
                "v2_score": 70,
                "delta": 20,
                "weighted_v1": 7.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 50,
                "v2_score": 70,
                "delta": 20,
                "weighted_v1": 5.0,
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
                "v2_score": 85,
                "delta": 15,
                "weighted_v1": 7.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v1": 63.0,
        "overall_v2": 81.5,
        "absolute_improvement": 18.5,
        "improvement_percentage": 29.37
    }
