"""
RAG-only Evaluation Report — document_1 / query_4
Source document: NASDAQ_AMZN_2022.pdf
Query: What is Amazon's free cash flow position and how did it change in 2022?
"""
from __future__ import annotations

USER_QUERY = "What is Amazon's free cash flow position and how did it change in 2022?"

RAG_RESPONSE = """
Amazon's free cash flow position in 2022 was negative, amounting to **$(11,569) million**. This represents a decline from the previous year, where the free cash flow was **$(9,069) million** in 2021. The change in free cash flow from 2021 to 2022 indicates a worsening position, primarily driven by increased capital expenditures, which rose from **$55,396 million** in 2021 to **$58,321 million** in 2022. Despite a slight increase in cash provided by operating activities, the higher investments led to a larger negative free cash flow in 2022.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's free cash flow position and its changes in 2022. However, it lacks grounding in the provided context documents and misses important structural elements.

## Query Satisfaction
The response provides a clear answer to the user's question about Amazon's free cash flow position in 2022, stating that it was negative at $(11,569) million and that it declined from $(9,069) million in 2021. It also mentions the reasons for this decline, specifically increased capital expenditures. However, it does not reference any specific context documents to support these claims, which diminishes its reliability.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for verifying the information provided.
2. **Absence of Limitations or Caveats**: There are no disclaimers or notes about the potential variability in financial data or external factors that could affect the interpretation of free cash flow.
3. **No Actionable Content**: The response does not provide any recommendations or next steps for the user, which could enhance its usefulness.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to substantiate the claims made about free cash flow.
- Add any necessary limitations or caveats regarding the financial data to provide a more nuanced understanding.
- Consider including actionable content or recommendations for the user based on the financial position discussed. 

Overall, while the response answers the query, it needs to be better grounded in the provided context and structured to enhance clarity and reliability.
"""
