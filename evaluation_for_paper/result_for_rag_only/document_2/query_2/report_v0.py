"""
RAG-only Evaluation Report — document_2 / query_2
Source document: NASDAQ_AMZN_2023.pdf
Query: How did AWS revenue growth trend in 2023 and what drove it?
"""
from __future__ import annotations

USER_QUERY = "How did AWS revenue growth trend in 2023 and what drove it?"

RAG_RESPONSE = """
In 2023, AWS (Amazon Web Services) revenue grew by 13% year-over-year, increasing from $80 billion to $91 billion. This growth was primarily driven by increased customer usage, although it was partially offset by pricing changes associated with long-term customer contracts. The overall revenue growth trend for AWS was influenced by substantial cost optimization efforts among customers, who were looking to save money in an uncertain economic environment. AWS helped customers leverage more efficient cloud capabilities, such as Graviton chips and intelligent storage solutions, which initially diminished short-term revenue but were beneficial for customers in the long run. By the end of 2023, AWS saw a resurgence in new deals and customer renewals at larger commitments, indicating a positive outlook for future growth.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding AWS revenue growth in 2023 and the factors driving that growth. However, it lacks citations from the provided context documents and does not include limitations or actionable content, which diminishes its overall quality.

## Query Satisfaction
The response effectively answers the user's question about AWS revenue growth in 2023, stating that it increased by 13% from $80 billion to $91 billion. It also identifies key drivers of this growth, such as increased customer usage and cost optimization efforts. However, it does not mention specific figures or details from the context documents that could enhance the response's credibility.

## Remaining Gaps
1. **Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There are no limitations or caveats mentioned regarding the revenue growth or the factors influencing it.
3. **Actionable Content**: The response lacks actionable insights or recommendations for the user based on the information provided.
4. **Structured Sections**: The response does not have structured sections that could help in organizing the information more clearly.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made.
- Add any limitations or caveats regarding the revenue growth and its drivers.
- Provide actionable insights or recommendations based on the information discussed.
- Consider structuring the response into clear sections for better readability and comprehension.
"""
