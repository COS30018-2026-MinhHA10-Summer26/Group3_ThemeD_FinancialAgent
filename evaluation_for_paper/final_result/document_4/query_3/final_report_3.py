"""
Three-Version Evaluation Report — document_4 / query_3
Source document: NASDAQ_AMZN_2025.pdf
Query: What is Amazon's profitability trend and operating margin outlook for 2025?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What is Amazon's profitability trend and operating margin outlook for 2025?"

USER_QUERIES = [
    "What were Amazon's key financial results and revenue breakdown for fiscal year 2025?",
    "How did Amazon's AWS segment grow in 2025 and what products drove demand?",
    "What is Amazon's profitability trend and operating margin outlook for 2025?",
    "What strategic acquisitions or investments did Amazon make in 2025?",
    "How did macroeconomic conditions affect Amazon's business in 2025?",
    "What is Amazon's cash and debt position at the end of fiscal year 2025?",
    "How did Amazon's Prime membership and subscription services perform in 2025?",
    "What does Amazon's 2025 annual report say about its long-term growth strategy?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
Amazon's profitability trend shows a positive trajectory, with operating income improving from $69 billion in 2024 to $80 billion in 2025, reflecting a 17% year-over-year increase. This corresponds to an operating margin of 10.8% in 2024, which improved to approximately 11.1% in 2025.

Looking ahead to 2025, Amazon's operating margin outlook appears optimistic, as they anticipate continued growth driven by investments in technology and infrastructure, particularly in artificial intelligence and AWS. The company expects to maintain strong revenue growth, with net sales increasing by 12% from $638 billion in 2024 to $717 billion in 2025. This growth, combined with operational efficiencies and strategic investments, suggests a favorable outlook for profitability in the coming years.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Profitability Trend and Operating Margin Outlook for 2025

⚠️ Profitability trend and operating margin outlook for 2025 were not found in the available documents. This figure cannot be confirmed without the source filing.

To provide a comprehensive analysis, I would need specific financial metrics such as revenue, net income, and operating margin figures for Amazon for 2025. If you have access to additional documents or data sources that contain this information, please share them.

### Analysis of Current Context

The documents provide insights into Amazon's strategic initiatives and growth areas, including investments in robotics, rural delivery, and broadband connectivity. However, they do not include specific financial metrics that would allow for a detailed profitability trend analysis or operating margin outlook for 2025.

### Future Outlook

Amazon's ongoing investments in various sectors could positively impact its profitability in the long term. For instance, the expansion of its grocery business and advancements in delivery logistics may enhance revenue streams. However, without concrete financial figures, it is challenging to quantify the expected operating margin for 2025.

### Recommendations

To gain a clearer understanding of Amazon's profitability trend and operating margin outlook for 2025, I recommend obtaining the following financial metrics:
- Revenue projections for 2025
- Expected net income for 2025
- Operating margin figures for 2025

If you can provide additional documents or data sources that contain this information, I would be happy to assist further.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Profitability Trend and Operating Margin Outlook for 2025

⚠️ Unfortunately, specific profitability metrics such as revenue, net income, and operating margin figures for Amazon in 2025 are not available in the provided documents. Therefore, a detailed analysis of the profitability trend and operating margin outlook cannot be confirmed without additional sources.

### Analysis of Current Context

The documents provide valuable insights into Amazon's strategic initiatives and growth areas, including significant investments in robotics, rural delivery, and broadband connectivity. While these initiatives are expected to positively impact Amazon's long-term profitability, the lack of specific financial metrics limits the ability to quantify these effects.

For instance, the grocery business has reportedly grown to over **$150 billion** in gross sales in 2025, making Amazon the second-largest grocer in the U.S. This substantial growth could enhance revenue streams and potentially improve operating margins, but without concrete figures, the exact impact remains speculative.

### Future Outlook

The strategic initiatives outlined suggest a positive trajectory for Amazon. However, without specific financial figures, it is challenging to provide a precise operating margin outlook for 2025. The company's commitment to innovation and customer service, particularly in logistics and delivery, may yield favorable financial outcomes, but specific projections are necessary for a clearer outlook.

### Recommendations

To gain a clearer understanding of Amazon's profitability trend and operating margin outlook for 2025, I recommend obtaining the following financial metrics:
- Revenue projections for 2025
- Expected net income for 2025
- Operating margin figures for 2025

Additionally, it would be beneficial to analyze potential risks that could impact profitability, including:
- Competitive pressures from other e-commerce and retail companies
- Valuation concerns in a fluctuating market
- Supply chain challenges that could affect operational efficiency
- Regulatory issues that may arise from expanding into new markets or technologies

If you can provide additional documents or data sources that contain this information, I would be happy to assist further.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
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

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Amazon's profitability trend and operating margin outlook for 2025 compared to the initial version. However, it still lacks specific financial metrics and visual aids, which are critical for a complete assessment.

## Query Satisfaction
The revised report addresses the user query regarding Amazon's profitability trend and operating margin outlook for 2025 by discussing strategic initiatives and potential impacts on profitability. However, it fails to provide specific financial metrics such as revenue, net income, and operating margin figures, which limits its effectiveness in fully answering the query.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  - [Include specific financial metrics for 2025: revenue, net income, operating margin.]
  - [Address missing risks: competition, valuation, supply chain, regulation.]
  - [Strengthen the connection between strategic initiatives and financial outcomes.]
  
- **Unresolved**:
  - [Incorporate figures or visualizations to support claims.]

The report has resolved 3 out of 4 issues, leaving one unresolved.

## Remaining Gaps
1. **Incorporate figures or visualizations to support claims.** The report lacks visual aids that could enhance understanding and illustrate the financial trends or strategic initiatives discussed.

## Recommendation
To improve the report further, the advisor should:
1. **Incorporate relevant figures or visualizations** that illustrate Amazon's profitability trends and strategic initiatives.
2. **Consider including specific financial metrics** if available, to provide a clearer outlook on Amazon's profitability for 2025.

By addressing the remaining gap, the report can provide a more robust analysis that meets the user's needs effectively.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_4/query_3
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       60 |       70 |    +10 |
| Risk Assessment      |    15%  |        0 |        0 |     +0 |
| Actionable Advice    |    15%  |       70 |       70 |     +0 |
| Evidence Usage       |    10%  |        0 |       10 |    +10 |
| Completeness         |    10%  |       60 |       70 |    +10 |
| Query Satisfaction   |    10%  |       50 |       60 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    30.50 |    35.00 |   +4.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +4.5 pts absolute  |  +14.75% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_4/query_3
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |        0 |        0 |    -90 |     +0 |    -90 |
| Business Analysis    |    15%  |       70 |       60 |       70 |    -10 |    +10 |     +0 |
| Risk Assessment      |    15%  |       50 |        0 |        0 |    -50 |     +0 |    -50 |
| Actionable Advice    |    15%  |       40 |       70 |       70 |    +30 |     +0 |    +30 |
| Evidence Usage       |    10%  |       60 |        0 |       10 |    -60 |    +10 |    -50 |
| Completeness         |    10%  |       80 |       60 |       70 |    -20 |    +10 |    -10 |
| Query Satisfaction   |    10%  |       90 |       50 |       60 |    -40 |    +10 |    -30 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    69.50 |    30.50 |    35.00 |    -39 |     +4 |    -34 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -34 pts absolute  |  -49.64% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 90,
                "weighted_v0": 22.5,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -90,
                "delta_v1_v2": 0,
                "delta_v0_v2": -90,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v0_v1": -10,
                "delta_v1_v2": 10,
                "delta_v0_v2": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -50,
                "delta_v1_v2": 0,
                "delta_v0_v2": -50,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v0_v1": 30,
                "delta_v1_v2": 0,
                "delta_v0_v2": 30,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 10,
                "delta_v0_v1": -60,
                "delta_v1_v2": 10,
                "delta_v0_v2": -50,
                "weighted_v1": 0.0,
                "weighted_v2": 1.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 60,
                "v2_score": 70,
                "delta_v0_v1": -20,
                "delta_v1_v2": 10,
                "delta_v0_v2": -10,
                "weighted_v1": 6.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v0_v1": -40,
                "delta_v1_v2": 10,
                "delta_v0_v2": -30,
                "weighted_v1": 5.0,
                "weighted_v2": 6.0
            }
        },
        "overall_v0": 69.5,
        "overall_v1": 30.5,
        "overall_v2": 35.0,
        "improvement_v0_to_v1": -39.0,
        "improvement_v1_to_v2": 4.5,
        "improvement_v0_to_v2": -34.5,
        "improvement_pct_v0_to_v2": -49.64
    }
