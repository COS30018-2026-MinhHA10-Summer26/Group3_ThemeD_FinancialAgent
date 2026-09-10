"""
RAG-only Evaluation Report — document_3 / query_1
Source document: NASDAQ_AMZN_2024.pdf
Query: What were Amazon's total net sales and earnings per share for fiscal year 2024?
"""
from __future__ import annotations

USER_QUERY = "What were Amazon's total net sales and earnings per share for fiscal year 2024?"

RAG_RESPONSE = """
For fiscal year 2024, Amazon's total net sales were $638 billion, and the earnings per share (EPS) were $5.66.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Amazon's total net sales and earnings per share for fiscal year 2024. However, it lacks grounding in the provided context documents and does not include necessary citations or structural elements.

## Query Satisfaction
The response directly addresses the user's query by providing the total net sales of $638 billion and earnings per share of $5.66 for fiscal year 2024. Therefore, it satisfies the query in terms of content.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite the specific documents from which the information was derived, which is essential for verifying the accuracy of the data provided.
2. **Missing Limitations or Caveats**: There are no disclaimers or notes regarding the potential variability or context of the financial figures, which could be important for users to understand.
3. **No Actionable Content**: The response does not provide any additional context or implications of the financial results, which could enhance the user's understanding.
4. **Absence of Structured Sections**: The response lacks a clear structure that could help in organizing the information better, such as headings or bullet points.

## Recommendation
To improve the response:
- Include citations to the relevant documents that support the figures provided.
- Add any necessary limitations or caveats regarding the financial data.
- Consider providing additional context or implications of the financial results to enhance user understanding.
- Structure the response with clear sections or bullet points for better readability.
"""
