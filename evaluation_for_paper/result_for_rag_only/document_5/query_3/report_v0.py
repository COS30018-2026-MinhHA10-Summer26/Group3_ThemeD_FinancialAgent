"""
RAG-only Evaluation Report: document_5 / query_3
Source document: NASDAQ_TSLA_2022.pdf
Query: What were the key financial ratios and margins for Tesla in 2022?
"""
from __future__ import annotations

USER_QUERY = "What were the key financial ratios and margins for Tesla in 2022?"

RAG_RESPONSE = """
In 2022, Tesla's key financial ratios and margins were as follows:

1. **Gross Margin**:
   - Total automotive gross margin decreased from 29.3% in 2021 to **28.5%** in 2022.
   - Gross margin for the total automotive and services segment decreased from 26.9% in 2021 to **26.5%** in 2022.

2. **Selling, General and Administrative (SG&A) Expenses**:
   - SG&A expenses were **$3,946 million**, which represented **5%** of total revenues, down from **8%** in 2021.

3. **Net Income**:
   - Tesla reported a net income of **$12,556 million** for 2022.

4. **Revenue**:
   - Total revenues for Tesla in 2022 were **$81,462 million**, an increase from **$53,823 million** in 2021.

These figures indicate a solid financial performance for Tesla in 2022, despite a slight decrease in gross margins.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's key financial ratios and margins for 2022, but it lacks proper grounding in the provided context documents and misses essential structural elements.

## Query Satisfaction
The response provides relevant financial metrics, including gross margin, SG&A expenses, net income, and total revenues for Tesla in 2022. However, it does not reference the source documents from which these figures were derived, which is crucial for validating the information presented.

## Remaining Gaps
1. **Source Citations**: The response does not include citations to the specific documents from which the financial data was obtained. This is important for credibility and verification.
2. **Limitations or Caveats**: There are no mentions of any limitations or caveats regarding the financial data, which could provide context for the figures presented.
3. **Actionable Content**: The response lacks actionable insights or recommendations based on the financial data, which could enhance its usefulness to the user.

## Recommendation
To improve the response:
- Include citations to the relevant documents that provide the financial data.
- Add any limitations or caveats related to the financial figures to give the user a clearer understanding of the context.
- Consider providing actionable insights or implications based on the financial performance metrics shared. 

Overall, while the response contains valuable information, enhancing its grounding and completeness will significantly improve its quality and reliability.
"""
