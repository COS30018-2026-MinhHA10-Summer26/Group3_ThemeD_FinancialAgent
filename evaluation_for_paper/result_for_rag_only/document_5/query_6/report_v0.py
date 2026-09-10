"""
RAG-only Evaluation Report: document_5 / query_6
Source document: NASDAQ_TSLA_2022.pdf
Query: What were Tesla's capital expenditures and free cash flow in 2022?
"""
from __future__ import annotations

USER_QUERY = "What were Tesla's capital expenditures and free cash flow in 2022?"

RAG_RESPONSE = """
In 2022, Tesla's capital expenditures amounted to $7.16 billion. The cash flows provided by operating activities during the same year were $14.72 billion, which indicates that Tesla generated significant free cash flow, although the exact figure for free cash flow is not explicitly stated in the documents. Free cash flow can be calculated as cash flows from operating activities minus capital expenditures, which would be approximately $7.56 billion ($14.72 billion - $7.16 billion).
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's capital expenditures and provides a calculated estimate of free cash flow for 2022. However, it lacks explicit mention of free cash flow in the context of the provided documents, which could lead to confusion.

## Query Satisfaction
The response directly addresses the user's query by stating that Tesla's capital expenditures in 2022 were $7.16 billion and provides an estimated free cash flow of approximately $7.56 billion. This information is relevant and derived from the context documents, particularly Document 4, which details Tesla's financial performance for the year.

## Remaining Gaps
1. **Explicit Free Cash Flow Definition**: The response does not explicitly define free cash flow or clarify how it is calculated, which may leave some users unclear about the term.
2. **Limitations and Caveats**: The response lacks a discussion of any limitations or caveats regarding the financial data, which is important for users to understand the context of the figures provided.
3. **Actionable Content**: There is no actionable content or recommendations for the user, which could enhance the response's utility.
4. **Structured Sections**: The response does not have structured sections that could improve readability and comprehension.

## Recommendation
To improve the response, it should:
- Include a clear definition of free cash flow and the formula used for its calculation.
- Mention any limitations or caveats regarding the financial data, such as potential fluctuations or uncertainties in future projections.
- Provide actionable insights or recommendations based on the financial data presented.
- Organize the response into structured sections for better clarity and readability.
"""
