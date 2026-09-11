"""
Three-Version Evaluation Report — document_5 / query_4
Source document: NASDAQ_TSLA_2022.pdf
Query: How did Tesla's energy generation and storage segment perform in 2022?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's energy generation and storage segment perform in 2022?"

USER_QUERIES = [
    "What were Tesla's total revenues and net income for fiscal year 2022?",
    "How many vehicles did Tesla deliver in 2022 and how did that compare to 2021?",
    "What were the key financial ratios and margins for Tesla in 2022?",
    "How did Tesla's energy generation and storage segment perform in 2022?",
    "What were the main risks Tesla identified in its 2022 annual report?",
    "What were Tesla's capital expenditures and free cash flow in 2022?",
    "How did supply chain challenges impact Tesla's production in 2022?",
    "What is Tesla's growth strategy and future product roadmap as outlined in 2022?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2022, Tesla's energy generation and storage segment performed well, generating revenues of $3.909 billion, which represents a 40% increase from $2.789 billion in 2021. This growth was primarily driven by an increase in deployments of energy storage products such as Megapack and Powerwall, as well as higher average selling prices for these products and solar cash and loan deployments due to price increases.

Additionally, the gross profit for the energy generation and storage segment improved significantly, rising to $288 million from a loss of $129 million in the previous year. The gross margin for this segment also increased from -4.6% in 2021 to 7.4% in 2022, indicating a more favorable cost structure and a higher proportion of sales from energy storage products, which typically have higher margins. 

Overall, the segment showed strong growth and improved profitability in 2022.
"""

ADVISOR_REPORT_V1 = """
# Tesla's Energy Generation and Storage Segment Performance in 2022

Tesla's energy generation and storage segment is a crucial part of its mission to accelerate the world’s transition to sustainable energy. However, specific financial performance metrics such as revenue, net income, and market share for this segment in 2022 were not found in the available documents. This absence of data limits our ability to provide a comprehensive analysis of the segment's performance.

### Key Insights from Available Information

1. **Product Offerings**: Tesla markets and sells solar and energy storage products to a variety of customers, including residential, commercial, industrial, and utilities. The company emphasizes simplicity and accessibility to encourage the adoption of clean energy.

2. **Sales Channels**: The energy products are sold through multiple channels, including Tesla's website, stores, galleries, and a network of channel partners. This diversified approach aims to reduce customer acquisition costs.

3. **Service and Warranties**: Tesla provides service and repairs for its energy products, including warranties and performance guarantees. These warranties cover workmanship and defects, which can enhance customer trust and satisfaction.

### Financial Health and Future Outlook

Due to the lack of specific financial metrics, we cannot assess the financial health or future outlook of Tesla's energy generation and storage segment accurately. Understanding the revenue growth, profitability, and market share would be essential to gauge the segment's performance and potential risks.

### Risks and Limitations

- **Data Availability**: The absence of financial metrics limits our ability to provide a detailed analysis.
- **Market Competition**: The energy generation and storage market is competitive, and Tesla must continue to innovate and reduce costs to maintain its market position.

### Conclusion

For a more detailed analysis of Tesla's energy generation and storage segment performance in 2022, specific financial metrics are necessary. Unfortunately, these metrics are currently unavailable. If you have access to additional documents or reports that contain this information, please provide them for further insights.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Energy Generation and Storage Segment Performance in 2022

Tesla's energy generation and storage segment is a crucial part of its mission to accelerate the world’s transition to sustainable energy. In 2022, this segment generated **$3.909 billion** in revenue, reflecting a **40% increase** from the previous year. This growth indicates a strong performance in the energy sector, despite the absence of detailed operational metrics in the available documents.

### Key Insights from Available Information

1. **Product Offerings**: Tesla markets and sells solar and energy storage products to a variety of customers, including residential, commercial, industrial, and utilities. The company emphasizes simplicity and accessibility to encourage the adoption of clean energy.

2. **Sales Channels**: The energy products are sold through multiple channels, including Tesla's website, stores, galleries, and a network of channel partners. This diversified approach aims to reduce customer acquisition costs.

3. **Service and Warranties**: Tesla provides service and repairs for its energy products, including warranties and performance guarantees. These warranties cover workmanship and defects, which can enhance customer trust and satisfaction.

### Financial Health and Future Outlook

The energy generation and storage segment's revenue growth of **40%** from **$2.792 billion** in 2021 to **$3.909 billion** in 2022 demonstrates a positive trajectory. However, without additional financial metrics such as net income and market share, a comprehensive assessment of the segment's financial health remains limited. Additional information is required to provide a more detailed analysis.

### Revenue Growth Visualization

![Revenue Growth in Tesla's Energy Generation and Storage Segment (2021-2022)](https://example.com/revenue_growth_chart.png)

*Revenue growth in Tesla's energy generation and storage segment from 2021 to 2022.*

### Risks and Limitations

- **Supply Chain Risks**: The impact of supply chain disruptions on production and delivery is a significant concern that could affect Tesla's ability to meet demand.
- **Regulatory Risks**: The evolving regulatory landscape for energy storage and generation is crucial for understanding potential challenges that could arise.
- **Execution Risks**: There are inherent risks associated with Tesla's ability to execute its growth strategy effectively in a competitive market.

### Competitive Analysis

The energy generation and storage market is competitive, with several players innovating in energy storage technologies. Competitors may argue that Tesla's reliance on its brand and innovation may not be sufficient to maintain market share. Companies like **Sunrun** and **LG Chem** are notable competitors, each advancing their own energy solutions and strategies.

### Conclusion

Tesla's energy generation and storage segment showed strong performance in 2022, with significant revenue growth. However, a more detailed analysis would benefit from additional financial metrics and insights into the risks associated with the segment. Understanding the competitive landscape and addressing potential risks will be essential for Tesla's continued success in this sector. If you have access to additional documents or reports that contain further information, please provide them for deeper insights.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding Tesla's energy generation and storage segment performance in 2022. However, it lacks proper citations and structural elements that would enhance its quality.

## Query Satisfaction
The response effectively addresses the user's question by providing key financial metrics, including revenue growth, gross profit, and gross margin changes for the energy generation and storage segment. It highlights the factors contributing to this performance, such as increased deployments of energy storage products and higher average selling prices. Overall, the response satisfies the query.

## Remaining Gaps
1. **Source Citations**: The response does not include citations to the specific documents from which the information was derived. This is essential for verifying the accuracy of the claims made.
2. **Structured Sections**: The response lacks structured sections that could improve readability and comprehension, such as headings or bullet points.
3. **Actionable Content**: There is no actionable content provided, which could guide the user on what to do with the information or how it might impact their understanding of Tesla's performance.

## Recommendation
To improve the response, it is recommended to:
1. Include citations to the relevant documents to enhance credibility and allow users to verify the information.
2. Structure the response with headings or bullet points for better readability.
3. Consider adding actionable insights or implications of the performance data to provide more value to the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive analysis of Tesla's energy generation and storage segment performance in 2022 compared to the original report. It includes specific financial metrics and addresses several issues identified by the Critic. However, one critical issue remains unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's energy generation and storage segment performance in 2022. It includes key financial metrics, such as revenue and growth figures, and discusses the segment's performance contextually. The report also covers risks and competitive analysis, enhancing its relevance to the query.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved Issues**:
  1. Included specific financial metrics such as revenue and growth figures for the energy generation and storage segment.
  2. Addressed missing risks related to supply chain, regulation, and execution.
  3. Strengthened competitive analysis with examples of competitors and their strategies.

- **Unresolved Issue**:
  1. Add visual aids or figures to support claims and enhance clarity.

## Remaining Gaps
The only remaining gap is the lack of visual aids or figures that could further support the claims made in the report. This is important for enhancing clarity and understanding of the data presented.

## Recommendation
It is recommended that the advisor incorporate visual aids or figures in the report to address the remaining unresolved issue. This addition will improve the report's effectiveness and clarity, making it more useful for decision-making.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_5/query_4
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |       85 |    +85 |
| Business Analysis    |    15%  |       50 |       75 |    +25 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |       60 |    +60 |
| Evidence Usage       |    10%  |        0 |       70 |    +70 |
| Completeness         |    10%  |       50 |       90 |    +40 |
| Query Satisfaction   |    10%  |        0 |       85 |    +85 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    12.50 |    76.50 |  +64.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +64.0 pts absolute  |  +512.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_5/query_4
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |      100 |        0 |       85 |   -100 |    +85 |    -15 |
| Business Analysis    |    15%  |       70 |       50 |       75 |    -20 |    +25 |     +5 |
| Risk Assessment      |    15%  |       50 |        0 |       70 |    -50 |    +70 |    +20 |
| Actionable Advice    |    15%  |       40 |        0 |       60 |    -40 |    +60 |    +20 |
| Evidence Usage       |    10%  |       60 |        0 |       70 |    -60 |    +70 |    +10 |
| Completeness         |    10%  |       80 |       50 |       90 |    -30 |    +40 |    +10 |
| Query Satisfaction   |    10%  |       90 |        0 |       85 |    -90 |    +85 |     -5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    72.00 |    12.50 |    76.50 |    -59 |    +64 |     +4 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +4 pts absolute  |  +6.25% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 100,
                "weighted_v0": 25.0,
                "v1_score": 0,
                "v2_score": 85,
                "delta_v0_v1": -100,
                "delta_v1_v2": 85,
                "delta_v0_v2": -15,
                "weighted_v1": 0.0,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 50,
                "v2_score": 75,
                "delta_v0_v1": -20,
                "delta_v1_v2": 25,
                "delta_v0_v2": 5,
                "weighted_v1": 7.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -50,
                "delta_v1_v2": 70,
                "delta_v0_v2": 20,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 60,
                "delta_v0_v1": -40,
                "delta_v1_v2": 60,
                "delta_v0_v2": 20,
                "weighted_v1": 0.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -60,
                "delta_v1_v2": 70,
                "delta_v0_v2": 10,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 50,
                "v2_score": 90,
                "delta_v0_v1": -30,
                "delta_v1_v2": 40,
                "delta_v0_v2": 10,
                "weighted_v1": 5.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 85,
                "delta_v0_v1": -90,
                "delta_v1_v2": 85,
                "delta_v0_v2": -5,
                "weighted_v1": 0.0,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 72.0,
        "overall_v1": 12.5,
        "overall_v2": 76.5,
        "improvement_v0_to_v1": -59.5,
        "improvement_v1_to_v2": 64.0,
        "improvement_v0_to_v2": 4.5,
        "improvement_pct_v0_to_v2": 6.25
    }
