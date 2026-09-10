"""
RAG-only Evaluation Report — document_1 / query_2
Source document: NASDAQ_AMZN_2022.pdf
Query: How did Amazon's AWS segment perform in 2022 compared to prior years?
"""
from __future__ import annotations

USER_QUERY = "How did Amazon's AWS segment perform in 2022 compared to prior years?"

RAG_RESPONSE = """
In 2022, Amazon's AWS segment experienced a year-over-year revenue growth of 29%, reaching an annualized revenue run rate of $85 billion. This growth was notable despite facing short-term headwinds due to macroeconomic conditions, which led many companies to be more cautious in their spending. The AWS segment's performance in 2022 continued to reflect strong demand, although it was slower compared to the 37% growth rate seen in 2021. Overall, AWS maintained its trajectory of growth, driven by increased customer usage and a robust pipeline of new customers, despite the challenges presented by the economic environment.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the performance of Amazon's AWS segment in 2022, highlighting the year-over-year revenue growth and contextualizing it within the broader economic challenges. However, it lacks citations from the provided context documents and does not include limitations or caveats, which diminishes its completeness and reliability.

## Query Satisfaction
The response effectively answers the user's question about AWS's performance in 2022 by stating that it achieved a 29% growth rate and reached an annualized revenue run rate of $85 billion. It also compares this performance to the previous year's growth rate of 37%, providing a clear picture of the segment's trajectory. However, it does not delve into specific financial health indicators or future outlooks beyond the immediate context of growth.

## Remaining Gaps
1. **Source Citations**: The response does not reference any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There is no mention of potential limitations or caveats regarding the growth figures or the economic conditions affecting AWS.
3. **Actionable Content**: The response lacks actionable insights or recommendations for the user, which could enhance its utility.
4. **Structured Sections**: The response does not follow a structured format that could improve readability and comprehension.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made.
- Add limitations or caveats regarding the growth figures and economic conditions.
- Consider providing actionable insights or recommendations based on the AWS performance data.
- Structure the response into clear sections to enhance clarity and user engagement.
"""
