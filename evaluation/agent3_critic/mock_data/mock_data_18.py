"""
Mock inputs for testing the Critic Agent.

Auto-generated from advisor run: mock_data_18.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT = """
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
