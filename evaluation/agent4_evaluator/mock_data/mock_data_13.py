"""
Mock inputs for testing the Evaluator Agent.

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
The revised advisor report (v2) provides a comprehensive overview of Tesla's financial health and future outlook. However, it still contains several unresolved issues that need to be addressed for it to be considered fully satisfactory.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, insights, risk assessments, and future growth prospects, fulfilling the user's request for advice based on the financial statements.

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
1. **Context for Financial Metrics**: The report lacks comparisons to industry benchmarks or competitors, which would strengthen the claims about Tesla's growth.
2. **Verification of Financial Figures**: The report does not adequately support the financial figures presented with appropriate citations.
3. **Image Link Issues**: The image link provided does not point to a supported format, which could lead to accessibility issues.
4. **Descriptive Captions**: The figure lacks descriptive captions or source notes, which are essential for understanding the context of the data presented.

## Recommendation
It is recommended that the advisor address the unresolved issues by:
1. Including context for financial metrics and comparisons to industry standards.
2. Verifying and supporting all financial figures with appropriate citations.
3. Updating the image link to a supported format and ensuring proper storage.
4. Adding descriptive captions or source notes for figures.

Addressing these gaps will enhance the quality and reliability of the report, making it more useful for decision-making.
"""
