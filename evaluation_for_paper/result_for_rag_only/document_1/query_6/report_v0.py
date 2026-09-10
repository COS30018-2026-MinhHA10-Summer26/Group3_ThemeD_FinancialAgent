"""
RAG-only Evaluation Report — document_1 / query_6
Source document: NASDAQ_AMZN_2022.pdf
Query: How did Amazon's international segment perform financially in 2022?
"""
from __future__ import annotations

USER_QUERY = "How did Amazon's international segment perform financially in 2022?"

RAG_RESPONSE = """
In 2022, Amazon's international segment experienced a decline in financial performance. The international segment generated $118 billion in revenue, which represented an 8% decrease compared to the previous year. This decline was primarily attributed to the impact of foreign currency exchange rates, which reduced international net sales by approximately $15 billion. Despite this decrease, the segment saw some growth in unit sales, including sales by third-party sellers and advertising sales, but these were not sufficient to offset the overall revenue decline. Additionally, the operating loss for the international segment increased significantly to $7.7 billion, compared to a loss of $924 million in 2021, largely due to rising fulfillment and shipping costs, as well as increased technology and content costs.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Amazon's international segment performance in 2022, but it lacks grounding in the provided context documents and misses several structural elements that would enhance its quality.

## Query Satisfaction
The response provides a clear summary of the financial performance of Amazon's international segment in 2022, including revenue figures and the reasons for the decline. It mentions the $118 billion revenue, the 8% decrease, and the significant increase in operating loss. However, it does not reference specific documents or provide citations, which diminishes its credibility.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Missing Limitations or Caveats**: The response does not mention any potential limitations or caveats regarding the financial data, such as the impact of foreign exchange rates.
3. **No Actionable Content**: The response lacks actionable insights or recommendations for the user based on the financial performance discussed.
4. **No Structured Sections**: The response does not follow a structured format that could help in better understanding the information presented.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made.
- Add any necessary limitations or caveats regarding the financial data.
- Provide actionable insights or recommendations based on the financial performance.
- Structure the response into clear sections to enhance readability and comprehension.
"""
