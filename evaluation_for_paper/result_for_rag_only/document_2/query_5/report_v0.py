"""
RAG-only Evaluation Report — document_2 / query_5
Source document: NASDAQ_AMZN_2023.pdf
Query: What were the key balance sheet highlights for Amazon at the end of 2023?
"""
from __future__ import annotations

USER_QUERY = "What were the key balance sheet highlights for Amazon at the end of 2023?"

RAG_RESPONSE = """
At the end of 2023, Amazon's key balance sheet highlights included:

1. **Total Assets**: Amazon's total assets increased from $462.7 billion in 2022 to $527.9 billion in 2023.

2. **Cash and Cash Equivalents**: The company reported cash and cash equivalents of $73.4 billion, up from $53.9 billion in the previous year.

3. **Marketable Securities**: Marketable securities decreased slightly from $16.1 billion in 2022 to $13.4 billion in 2023.

4. **Inventories**: Inventories were reported at $33.3 billion, a slight decrease from $34.4 billion in 2022.

5. **Accounts Receivable**: Accounts receivable increased from $42.4 billion in 2022 to $52.3 billion in 2023.

6. **Total Liabilities**: Total liabilities rose from $316.6 billion in 2022 to $326.5 billion in 2023.

7. **Long-term Debt**: Long-term debt decreased from $67.2 billion in 2022 to $58.3 billion in 2023.

8. **Stockholders' Equity**: Stockholders' equity increased significantly from $146.0 billion in 2022 to $201.9 billion in 2023.

These figures reflect Amazon's strong financial position and growth in various areas, particularly in cash and accounts receivable.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's key balance sheet highlights at the end of 2023. However, it lacks citations for the data presented and does not include any limitations or actionable content, which diminishes its overall quality.

## Query Satisfaction
The response effectively covers the key aspects of Amazon's balance sheet, including total assets, cash and cash equivalents, marketable securities, inventories, accounts receivable, total liabilities, long-term debt, and stockholders' equity. Each of these points is relevant to the user's inquiry about the financial highlights at the end of 2023.

## Remaining Gaps
1. **Source Citations**: The response does not provide citations for the financial figures mentioned, which is crucial for verifying the accuracy of the information.
2. **Limitations or Caveats**: There are no disclaimers or notes regarding the potential variability of the figures or the context in which they should be interpreted.
3. **Actionable Content**: The response lacks any actionable insights or recommendations based on the financial highlights, which could enhance its utility for the user.

## Recommendation
To improve the response, it is recommended to:
1. Include citations for the financial data to enhance credibility and allow users to verify the information.
2. Add any relevant limitations or caveats regarding the financial figures to provide context.
3. Consider including actionable insights or implications of the financial highlights to make the response more valuable to the user.
"""
