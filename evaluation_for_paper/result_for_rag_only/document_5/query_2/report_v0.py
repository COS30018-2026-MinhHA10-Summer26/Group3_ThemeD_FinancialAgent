"""
RAG-only Evaluation Report: document_5 / query_2
Source document: NASDAQ_TSLA_2022.pdf
Query: How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?
"""
from __future__ import annotations

USER_QUERY = "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?"

RAG_RESPONSE = """
In 2022, Tesla delivered a total of 1,313,851 vehicles. This represented an increase of 385,000 vehicles compared to 2021, when Tesla delivered 928,000 vehicles.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's vehicle deliveries in 2022 and provides a comparison to 2021. However, it lacks proper grounding in the provided context documents and does not include necessary structural elements.

## Query Satisfaction
The response directly addresses the user's question by stating that Tesla delivered 1,313,851 vehicles in 2022, which is an increase of 385,000 vehicles compared to the 928,000 vehicles delivered in 2021. This satisfies the user's request for both the delivery numbers and the year-over-year comparison.

## Remaining Gaps
1. **Lack of Source Citation**: The response does not cite any of the context documents, which is essential for verifying the accuracy of the information provided.
2. **Missing Limitations or Caveats**: There are no disclaimers or notes regarding the data, which could be important for understanding the context of the figures.
3. **No Actionable Content**: The response does not provide any additional insights or recommendations based on the data presented.
4. **Structural Elements**: The response lacks structured sections that could enhance clarity and readability.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the figures provided.
- Add any necessary limitations or caveats regarding the data.
- Consider providing additional insights or implications of the delivery numbers.
- Structure the response into clear sections for better readability.
"""
