"""
Mock inputs for testing the Evaluator Agent.

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
The revised advisor report (v2) provides a more comprehensive overview of Tesla's financial health and future outlook compared to the original version. However, it still has unresolved issues that need to be addressed before it can be considered fully satisfactory.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's financial health and future outlook. It covers key financial metrics, risk assessments, and provides a positive outlook for the company. The inclusion of a chart also adds value to the analysis. Overall, the report meets the expectations set by the user query.

## Issues Resolution Status
Out of the five issues identified by the Critic, two have been resolved:
- **Resolved**: Add citations and evidence for all financial claims and metrics.
- **Resolved**: Address missing risks, particularly margin pressure and regulatory challenges.

The following issues remain unresolved:
- **Unresolved**: Clarify the methodology behind the Altman Z-Score and its implications.
- **Unresolved**: Ensure all figures are consistent with the provided context documents.
- **Unresolved**: Update the chart to use a Supabase-hosted link and include a caption or source note.

## Remaining Gaps
1. The methodology behind the Altman Z-Score and its implications is not clarified.
2. There is a need to ensure that all financial figures presented are consistent with the provided context documents.
3. The chart link needs to be updated to a Supabase-hosted link, and a caption or source note should be included for clarity.

## Recommendation
It is recommended that the advisor address the remaining unresolved issues to enhance the reliability and completeness of the report. Specifically, the advisor should:
1. Provide a clear explanation of how the Altman Z-Score was calculated and its significance.
2. Verify that all financial figures align with the data from the context documents.
3. Update the chart link and include a caption or source note to improve accessibility and context for the data presented. 

Addressing these points will strengthen the report and ensure it meets the quality standards expected in financial analysis.
"""
