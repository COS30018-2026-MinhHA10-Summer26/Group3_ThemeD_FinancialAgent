"""
RAG-only Evaluation Report — document_4 / query_3
Source document: NASDAQ_AMZN_2025.pdf
Query: What is Amazon's profitability trend and operating margin outlook for 2025?
"""
from __future__ import annotations

USER_QUERY = "What is Amazon's profitability trend and operating margin outlook for 2025?"

RAG_RESPONSE = """
Amazon's profitability trend shows a positive trajectory, with operating income improving from $69 billion in 2024 to $80 billion in 2025, reflecting a 17% year-over-year increase. This corresponds to an operating margin of 10.8% in 2024, which improved to approximately 11.1% in 2025.

Looking ahead to 2025, Amazon's operating margin outlook appears optimistic, as they anticipate continued growth driven by investments in technology and infrastructure, particularly in artificial intelligence and AWS. The company expects to maintain strong revenue growth, with net sales increasing by 12% from $638 billion in 2024 to $717 billion in 2025. This growth, combined with operational efficiencies and strategic investments, suggests a favorable outlook for profitability in the coming years.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's profitability trend and operating margin outlook for 2025. However, it lacks grounding in the provided context documents and misses essential structural elements.

## Query Satisfaction
The response effectively summarizes Amazon's profitability trend, noting the increase in operating income and operating margin from 2024 to 2025. It also provides a positive outlook for future profitability, aligning with the user's request for information on both the trend and outlook. However, it does not reference specific data or insights from the context documents, which diminishes its reliability.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is crucial for validating the information presented.
2. **Missing Limitations or Caveats**: The response does not mention any potential risks or uncertainties that could affect the profitability outlook, which is important for a comprehensive understanding.
3. **Absence of Structured Sections**: The response lacks clear structural elements such as headings or sections that would enhance readability and organization.

## Recommendation
To improve the response:
- Include citations from the context documents to support the claims made about profitability and operating margins.
- Address any potential risks or uncertainties that could impact the outlook for 2025.
- Structure the response with clear headings or sections to enhance clarity and organization. 

Incorporating these elements will provide a more robust and credible answer to the user's query.
"""
