"""
RAG-only Evaluation Report — document_3 / query_2
Source document: NASDAQ_AMZN_2024.pdf
Query: How did AWS perform in 2024 and what was its contribution to operating profit?
"""
from __future__ import annotations

USER_QUERY = "How did AWS perform in 2024 and what was its contribution to operating profit?"

RAG_RESPONSE = """
In 2024, AWS (Amazon Web Services) performed strongly, with revenue increasing by 19% year-over-year, rising from $91 billion in 2023 to $108 billion in 2024. This growth was attributed to increased customer usage and the launch of new services, despite some pricing changes due to long-term customer contracts.

AWS made a significant contribution to Amazon's overall operating profit, with its operating income reaching $39.8 billion in 2024, compared to $24.6 billion in 2023. This increase in operating income was primarily driven by higher sales, reduced payroll and related expenses, and a decrease in depreciation and amortization expenses. Overall, Amazon's consolidated operating income for 2024 was $68.6 billion, indicating that AWS was a major contributor to the company's profitability.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding AWS's performance in 2024 and its contribution to operating profit. However, it lacks citations from the provided context documents and does not include any limitations or caveats, which diminishes its overall quality.

## Query Satisfaction
The response effectively addresses the user's query by providing specific figures for AWS's revenue growth (19% increase from $91 billion to $108 billion) and operating income (from $24.6 billion to $39.8 billion). It also contextualizes AWS's contribution to Amazon's overall operating profit, which was $68.6 billion in 2024. Therefore, the response satisfies the query.

## Remaining Gaps
1. **Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There are no mentions of any limitations or potential uncertainties regarding the figures or claims made.
3. **Actionable Content**: The response lacks actionable insights or recommendations that could be beneficial for the user.
4. **Structured Sections**: The response does not have a clear structure or sections, which could enhance readability and comprehension.

## Recommendation
To improve the response, it should include:
- Citations from the relevant context documents to support the claims made.
- A section discussing any limitations or uncertainties related to the financial data provided.
- Actionable insights or recommendations based on the performance data.
- A more structured format to enhance clarity and organization.
"""
