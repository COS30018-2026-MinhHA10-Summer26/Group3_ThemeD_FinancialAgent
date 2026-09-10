"""
RAG-only Evaluation Report — document_4 / query_1
Source document: NASDAQ_AMZN_2025.pdf
Query: What were Amazon's key financial results and revenue breakdown for fiscal year 2025?
"""
from __future__ import annotations

USER_QUERY = "What were Amazon's key financial results and revenue breakdown for fiscal year 2025?"

RAG_RESPONSE = """
In fiscal year 2025, Amazon reported key financial results as follows:

- **Total Revenue**: $717 billion, which represents a 12% increase from $638 billion in 2024.
- **Revenue Breakdown**:
  - **North America**: $426 billion (up 10% from $387 billion)
  - **International**: $162 billion (up 13% from $143 billion)
  - **Amazon Web Services (AWS)**: $129 billion (up 20% from $108 billion)

- **Operating Income**: $80 billion, an increase of 17% from $69 billion in 2024.
- **Free Cash Flow**: Decreased to $11 billion from $38 billion in 2024, primarily due to a significant increase in capital expenditures related to investments in artificial intelligence and other initiatives.

These results indicate a strong performance across all segments, particularly in AWS, which continues to show robust growth.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Amazon's key financial results and revenue breakdown for fiscal year 2025. However, it lacks grounding in the provided context documents and misses several structural elements that would enhance its quality.

## Query Satisfaction
The response provides the key financial results, including total revenue, revenue breakdown by segment, operating income, and free cash flow, which directly addresses the user's query. However, it does not reference any specific source or document, which diminishes its credibility.

## Remaining Gaps
1. **Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There are no mentions of limitations or caveats regarding the financial data, which could be important for users to understand the context of the figures.
3. **Actionable Content**: The response lacks actionable insights or recommendations based on the financial results, which could provide additional value to the user.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to enhance credibility and grounding.
- Add any necessary limitations or caveats regarding the financial data to provide a more comprehensive view.
- Consider including actionable insights or implications of the financial results to offer more value to the user.
"""
