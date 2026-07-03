"""
Mock data for testing the Advisor Agent's revision process.
Provides a V1 report containing gaps, context documents, and Critic's feedback.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

# Draft Advisor Report V1 with missing elements and logic gaps
MOCK_ADVISOR_REPORT_V1 = """
# Tesla, Inc. Financial Health and Future Outlook

## Key Financial Metrics (2022)

The following table summarizes Tesla's key financial metrics as of December 31, 2022:

| Metric                           | Value       |
|----------------------------------|-------------|
| Total Revenues (Sales)          | $81,462M    |
| Income from Operations (EBIT)    | $13,656M    |
| Total Assets                     | $82,338M    |
| Total Liabilities                | $36,440M    |
| Retained Earnings                 | $12,885M    |
| Working Capital                   | $14,208M    |
| Market Capitalization             | $389,000M   |
| Total Debt                       | $5,748M     |
| Interest Expense                  | $191M       |

*Source: NASDAQ_TSLA_2022.pdf (Part II, Item 8) - Consolidated Balance Sheets & Operations*

## Financial Health Assessment

### 1. Risk Assessment
- **Altman Z-Score**: 8.367 (Safe Zone - Low Bankruptcy Risk)
  - This score indicates that Tesla is in a strong financial position with a low risk of bankruptcy.
  
- **Debt to Equity Ratio**: 0.1252
  - This low ratio suggests that Tesla is not heavily reliant on debt to finance its operations, which is a positive indicator of financial stability.

- **Interest Coverage Ratio**: 71.5
  - This high ratio indicates that Tesla generates significantly more earnings than it needs to cover its interest expenses, demonstrating strong operational efficiency.

### 2. Working Capital
- **Working Capital**: $14,208M
  - This positive working capital indicates that Tesla has sufficient short-term assets to cover its short-term liabilities.

## Future Outlook

Tesla's future outlook appears promising due to its battery technology, global factories, and tax incentives.

### Risks and Limitations
- **Supply Chain**: Dependency on single-source suppliers for key components.
- **Competition**: EV market is competitive.

### Actionable Advice
1. **Diversify Supply Chain**: Seek other suppliers.
2. **Invest in R&D**: Continue improving battery tech.
"""

# Feedback matching the critic's audit results
MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "The report does not include a visual chart comparing key financial metrics as requested by the user.",
        "The debt-to-equity ratio of 0.1252 lacks comparison with automotive industry averages.",
        "The Altman Z-Score of 8.367 is presented without explanation of its zones or context.",
        "The future outlook section is extremely brief and lacks detail on margin pressures or market competition."
    ],
    "revision_instructions": (
        "1. Call figure_generation_tool with figure_type='bar_chart' comparing key metrics: Revenues, EBIT, Assets, and Debt.\\n"
        "2. Add comparison for the debt-to-equity ratio against the automotive industry average (~1.0 - 1.5).\\n"
        "3. Provide brief context explaining the Altman Z-score calculation and how it indicates low bankruptcy risk.\\n"
        "4. Expand the future outlook to discuss margin pressures from competition and rising raw material costs."
    )
}
