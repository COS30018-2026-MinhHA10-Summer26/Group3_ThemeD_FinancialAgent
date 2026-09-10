"""
RAG-only Evaluation Report — document_1 / query_1
Source document: NASDAQ_AMZN_2022.pdf
Query: What were Amazon's total net sales and net income for fiscal year 2022?
"""
from __future__ import annotations

USER_QUERY = "What were Amazon's total net sales and net income for fiscal year 2022?"

RAG_RESPONSE = """
For the fiscal year 2022, Amazon's total net sales were $513.98 billion, and the net income was a loss of $2.72 billion.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user's query regarding Amazon's total net sales and net income for fiscal year 2022. However, it lacks proper grounding in the provided context documents and does not include necessary citations or structural elements.

## Query Satisfaction
The response directly addresses the user's question by providing the total net sales of $513.98 billion and a net income loss of $2.72 billion for fiscal year 2022. Therefore, it satisfies the query in terms of content.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents from which the financial figures were derived. This is crucial for verifying the accuracy of the information provided.
2. **Missing Limitations or Caveats**: The response does not mention any limitations or caveats regarding the financial data, which could be important for the user to understand the context of the figures.
3. **Absence of Actionable Content**: There is no actionable content or recommendations provided in the response, which could enhance its usefulness.
4. **No Structured Sections**: The response lacks a structured format that could help in presenting the information more clearly.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the financial figures provided.
- Add any necessary limitations or caveats regarding the financial data.
- Consider including actionable content or recommendations based on the financial results.
- Structure the response into clear sections for better readability and comprehension.
"""
