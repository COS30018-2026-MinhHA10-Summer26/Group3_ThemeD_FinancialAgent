"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_18.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Overview
Based on the provided financial statements and data, we can analyze Tesla's financial health and future outlook. The analysis includes a comparison of key financial metrics from 2022 and 2021, as well as a risk assessment.

## Key Financial Metrics Comparison

### Comparison Table: Tesla 2022 vs Tesla 2021

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
|----------------------------|------------|------------|--------------|------------|
| Finance lease liabilities   | $1,054.00  | $1,492.00  | -$438.00     | -29.36%    |
| Operating lease liabilities  | $2,649.00  | $2,039.00  | +$610.00     | +29.92%    |
| Total lease liabilities      | $3,703.00  | $3,531.00  | +$172.00     | +4.87%     |

### Observations
- **Finance Lease Liabilities**: Decreased significantly by 29.36%, indicating a reduction in obligations related to finance leases.
- **Operating Lease Liabilities**: Increased by 29.92%, suggesting that Tesla is expanding its operational footprint, possibly by leasing more assets.
- **Total Lease Liabilities**: A slight increase of 4.87% indicates overall growth in leasing activities, but the reduction in finance lease liabilities is noteworthy.

## Risk Assessment
The Altman Z-Score, which is typically used to assess the likelihood of bankruptcy, cannot be computed due to insufficient data. However, the total liabilities amounting to $2.06 billion indicates a manageable level of debt relative to Tesla's market position and growth trajectory.

## Future Outlook
1. **Growth Potential**: The increase in operating lease liabilities suggests that Tesla is investing in its operational capacity, which could lead to increased production and sales in the future.
2. **Debt Management**: The reduction in finance lease liabilities is a positive sign, indicating improved debt management and potentially lower interest expenses.
3. **Market Position**: Tesla continues to hold a strong position in the electric vehicle market, which is expected to grow as demand for sustainable transportation increases.

## Conclusion
Tesla's financial health appears stable, with a strategic focus on expanding its operational capabilities while managing its debt effectively. The company's future outlook remains positive, driven by growth in the electric vehicle market and ongoing investments in infrastructure.

### Chart of Key Financial Metrics
![Key Financial Metrics Comparison](https://example.com/path/to/chart.png)  
*Source: Tesla Financial Statements 2022* 

(Note: The chart link is a placeholder; please replace it with the actual chart link generated from the figure generation tool if needed.) 

For a more detailed analysis, additional financial metrics such as revenue, net income, and cash flow would be beneficial.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a basic overview of Tesla's financial health and future outlook, but it lacks depth in risk assessment and fails to address several critical areas that could impact investor decisions. The analysis is not sufficiently supported by evidence, and there are significant gaps in the discussion of risks.\n\n## Major Logic Gaps\n- The report states that total liabilities amount to $2.06 billion, which appears to be a miscalculation or misrepresentation of the actual total liabilities of $36,440 million. This discrepancy undermines the credibility of the financial analysis.\n- The conclusion suggests that Tesla's financial health is stable without adequately addressing the implications of increasing operating lease liabilities and the potential risks associated with them.\n\n## Unsupported or Weakly Supported Claims\n- The claim that the reduction in finance lease liabilities indicates improved debt management is not substantiated with context or data. It would be beneficial to provide a comparison of interest expenses or cash flow implications.\n- The report lacks a detailed analysis of revenue, net income, and cash flow, which are critical for a comprehensive understanding of Tesla's financial health.\n\n## Missing Investor Risks\n- The report does not address significant risks such as competition in the electric vehicle market, supply chain vulnerabilities, regulatory changes, and valuation concerns. These are critical factors that investors would consider before making decisions.\n- The absence of a discussion on margin pressure and execution risks further weakens the risk assessment.\n\n## Figure and Visualization Issues\n- The chart link provided is a placeholder and does not lead to a valid source. It is essential to replace it with a proper Supabase-hosted link to ensure accessibility and credibility.\n- The image is not stored under the expected advisor_figure folder, which could lead to issues with retrieval and presentation.\n\n## Competitor Counterarguments\n- Competitors may argue that Tesla's increasing operating lease liabilities could indicate overextension or reliance on leasing rather than ownership, which could be a strategic blind spot.\n- The lack of discussion on competitive pressures and market dynamics may leave the report vulnerable to critiques regarding its comprehensiveness and foresight.\n\n## Revision Priorities\n1. Correct the misrepresentation of total liabilities and ensure all financial figures are accurate and clearly sourced.\n2. Expand the risk assessment section to include competition, supply chain vulnerabilities, regulatory risks, and valuation concerns.\n3. Provide a more detailed analysis of revenue, net income, and cash flow to support claims about financial health.\n4. Replace the placeholder chart link with a valid Supabase-hosted link and ensure proper storage in the advisor_figure folder.\n\n## Issues to Resolve\n- [ ] Correct the total liabilities figure to accurately reflect $36,440 million.\n- [ ] Expand the risk assessment to include competition, supply chain, regulation, and valuation risks.\n- [ ] Provide a detailed analysis of revenue, net income, and cash flow.\n- [ ] Replace the placeholder chart link with a valid Supabase-hosted link.\n- [ ] Ensure the chart is stored in the expected advisor_figure folder."
}
