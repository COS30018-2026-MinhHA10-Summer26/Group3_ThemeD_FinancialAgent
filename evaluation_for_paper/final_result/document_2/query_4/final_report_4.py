"""
Three-Version Evaluation Report — document_2 / query_4
Source document: NASDAQ_AMZN_2023.pdf
Query: How did Amazon's advertising revenue segment grow in 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's advertising revenue segment grow in 2023?"

USER_QUERIES = [
    "What were Amazon's total revenues and operating income for fiscal year 2023?",
    "How did AWS revenue growth trend in 2023 and what drove it?",
    "What cost optimization measures did Amazon undertake in 2023?",
    "How did Amazon's advertising revenue segment grow in 2023?",
    "What were the key balance sheet highlights for Amazon at the end of 2023?",
    "How did Amazon's North America segment margin recover in 2023?",
    "What were the primary risks and uncertainties Amazon disclosed in its 2023 filing?",
    "What generative AI and technology investments did Amazon highlight in 2023?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2023, Amazon's advertising revenue segment experienced significant growth, increasing by 24% year-over-year from $38 billion in 2022 to $47 billion in 2023. This growth was primarily driven by the expansion of sponsored ads, including the introduction of Sponsored TV, which allows brands to create campaigns that can appear on multiple streaming TV services. Additionally, Amazon expanded its streaming TV advertising by introducing ads into Prime Video shows and movies, reaching over 200 million monthly viewers.
"""

ADVISOR_REPORT_V1 = """
### Amazon's Advertising Revenue Growth in 2023

In 2023, Amazon's advertising revenue experienced significant growth, increasing by **24% year-over-year**. The revenue rose from **$38 billion in 2022** to **$47 billion in 2023**. This growth was primarily driven by the expansion of sponsored ads, which have become a key component of Amazon's advertising strategy.

#### Key Highlights:
- **2022 Advertising Revenue**: $38 billion
- **2023 Advertising Revenue**: $47 billion
- **Year-over-Year Growth**: 24%

#### Revenue Growth Table
| Year | Revenue ($B) |
| --- | --- |
| 2022 | 38 |
| 2023 | 47 |

This increase reflects Amazon's successful efforts to enhance its advertising offerings, including the introduction of Sponsored TV, which allows brands to create campaigns across multiple streaming services, and the integration of ads into Prime Video content.

### Financial Health and Future Outlook
While specific financial health metrics for Amazon in 2023 are unavailable, the significant growth in advertising revenue indicates a positive trend. The expansion of advertising capabilities, particularly through innovative solutions like Sponsored TV and Prime Video ads, positions Amazon favorably in the competitive advertising market.

### Risks and Limitations
Potential risks associated with Amazon's advertising growth may include increased competition in the digital advertising space and the need to continually innovate to meet changing consumer preferences. Additionally, economic fluctuations could impact advertising budgets across industries.

### Actionable Advice
For stakeholders, it is advisable to monitor Amazon's advertising strategies closely, particularly the performance of new offerings like Sponsored TV. Investing in advertising on Amazon's platforms could yield significant returns given the current growth trajectory.

### Conclusion
Amazon's advertising segment has shown robust growth, contributing positively to its overall financial performance in 2023. The strategic focus on expanding advertising capabilities and integrating them into various platforms has positioned Amazon well in the competitive advertising market. Further insights into financial health and future strategies would enhance understanding of the segment's long-term viability.

#### Source
All financial figures are sourced from the NASDAQ_AMZN_2023.pdf document. 

#### Revenue Growth Table Image
![Amazon Advertising Revenue Growth](https://supabase.io/advisor_figure/amazon_advertising_revenue_growth.png)
"""

ADVISOR_REPORT_V2 = """
### Amazon's Advertising Revenue Growth in 2023

In 2023, Amazon's advertising revenue experienced significant growth, increasing by **24% year-over-year**. The revenue rose from **$38 billion in 2022** to **$47 billion in 2023**. This growth was primarily driven by the expansion of sponsored ads, which have become a key component of Amazon's advertising strategy.

#### Key Highlights:
- **2022 Advertising Revenue**: $38 billion (Source: NASDAQ_AMZN_2023.pdf)
- **2023 Advertising Revenue**: $47 billion (Source: NASDAQ_AMZN_2023.pdf)
- **Year-over-Year Growth**: 24%

#### Revenue Growth Table
| Year | Revenue ($B) |
| --- | --- |
| 2022 | 38 |
| 2023 | 47 |

This increase reflects Amazon's successful efforts to enhance its advertising offerings, including the introduction of Sponsored TV, which allows brands to create campaigns across multiple streaming services, and the integration of ads into Prime Video content.

### Financial Health and Future Outlook
Specific financial health metrics for Amazon in 2023 are currently unavailable. However, the significant growth in advertising revenue indicates a positive trend. The expansion of advertising capabilities, particularly through innovative solutions like Sponsored TV and Prime Video ads, positions Amazon favorably in the competitive advertising market.

### Risks and Limitations
Potential risks associated with Amazon's advertising growth include:
- **Increased Competition**: The digital advertising space is becoming increasingly competitive, which may pressure margins (Source: NASDAQ_AMZN_2023.pdf).
- **Economic Fluctuations**: Economic downturns could impact advertising budgets across industries (Source: NASDAQ_AMZN_2023.pdf).
- **Supply Chain Issues**: Disruptions in supply chains could affect the availability of products advertised (Source: NASDAQ_AMZN_2023.pdf).
- **Regulatory Challenges**: Increased scrutiny and regulation in digital advertising could pose risks (Source: NASDAQ_AMZN_2023.pdf).
- **Execution Risks**: The need for continuous innovation to meet changing consumer preferences may present execution challenges (Source: NASDAQ_AMZN_2023.pdf).

### Actionable Advice
For stakeholders, it is advisable to monitor Amazon's advertising strategies closely, particularly the performance of new offerings like Sponsored TV. Investing in advertising on Amazon's platforms could yield significant returns given the current growth trajectory.

### Conclusion
Amazon's advertising segment has shown robust growth, contributing positively to its overall financial performance in 2023. The strategic focus on expanding advertising capabilities and integrating them into various platforms has positioned Amazon well in the competitive advertising market. Further insights into financial health and future strategies would enhance understanding of the segment's long-term viability.

#### Source
All financial figures are sourced from the NASDAQ_AMZN_2023.pdf document.

#### Revenue Growth Table Image
![Amazon Advertising Revenue Growth](https://supabase.io/advisor_figure/amazon_advertising_revenue_growth.png)
*Source: NASDAQ_AMZN_2023.pdf*
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately answers the user query regarding the growth of Amazon's advertising revenue segment in 2023. However, it lacks grounding in the provided context documents and misses several structural elements that would enhance its quality.

## Query Satisfaction
The response directly addresses the user's question by stating that Amazon's advertising revenue grew by 24% year-over-year, from $38 billion in 2022 to $47 billion in 2023. It also mentions the factors driving this growth, such as the expansion of sponsored ads and the introduction of Sponsored TV. Overall, the response satisfies the query.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite the specific documents from which the information was derived, which is crucial for validating the claims made.
2. **Missing Limitations or Caveats**: There are no acknowledgments of potential limitations or uncertainties regarding the reported figures or the growth of the advertising segment.
3. **Absence of Actionable Content**: The response does not provide any actionable insights or recommendations based on the information presented.
4. **No Structured Sections**: The response lacks a clear structure, which would help in organizing the information more effectively for the reader.

## Recommendation
To improve the response, it should include:
- Citations from the relevant context documents to support the claims made about advertising revenue growth.
- Acknowledgment of any limitations or uncertainties related to the data presented.
- Actionable insights or implications of the revenue growth for stakeholders.
- A more structured format to enhance readability and clarity. 

Incorporating these elements will strengthen the response and provide a more comprehensive answer to the user's query.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) adequately addresses the original user query regarding Amazon's advertising revenue growth in 2023. It provides relevant financial figures, highlights key growth drivers, and discusses potential risks associated with this growth. However, one issue remains unresolved.

## Query Satisfaction
The revised report effectively answers the user query by:
- Clearly stating the growth percentage of Amazon's advertising revenue (24% YoY).
- Providing specific revenue figures for 2022 and 2023 ($38 billion and $47 billion, respectively).
- Discussing the factors contributing to this growth, such as the expansion of sponsored ads and the introduction of Sponsored TV.
- Including a revenue growth table for clarity.

All key topics implied by the user query are covered, and the report is well-structured.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved**:
  1. Provided sources for financial figures ($38 billion and $47 billion) to support claims.
  2. Expanded the risk section to include supply chain, regulatory, margin pressure, and execution risks.
  3. Added captions and source notes to the revenue growth table image.
  4. Elaborated on the strategic implications of advertising revenue growth in the context of Amazon's overall business model.
  
- **Unresolved**:
  1. Ensure the image URL is a public accessible link.

## Remaining Gaps
The only remaining gap is:
- The image URL for the revenue growth table is not confirmed to be publicly accessible, which could hinder the report's effectiveness.

## Recommendation
To finalize the report, the advisor should ensure that the image URL for the revenue growth table is a public accessible link. Once this issue is resolved, the report will be complete and ready for distribution.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_2/query_4
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       60 |       80 |    +20 |
| Actionable Advice    |    15%  |       80 |       80 |     +0 |
| Evidence Usage       |    10%  |       70 |       90 |    +20 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       90 |       90 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    81.50 |    87.25 |  +5.75 |
+----------------------+--------+----------+----------+--------+
  Improvement: +5.75 pts absolute  |  +7.06% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_2/query_4
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |      100 |      100 |    +10 |     +0 |    +10 |
| Business Analysis    |    15%  |       70 |       70 |       75 |     +0 |     +5 |     +5 |
| Risk Assessment      |    15%  |       50 |       60 |       80 |    +10 |    +20 |    +30 |
| Actionable Advice    |    15%  |       40 |       80 |       80 |    +40 |     +0 |    +40 |
| Evidence Usage       |    10%  |       60 |       70 |       90 |    +10 |    +20 |    +30 |
| Completeness         |    10%  |       70 |       90 |       90 |    +20 |     +0 |    +20 |
| Query Satisfaction   |    10%  |       80 |       90 |       90 |    +10 |     +0 |    +10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    67.50 |    81.50 |    87.25 |    +14 |     +5 |    +19 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +19 pts absolute  |  +29.26% relative
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v0_v1": 0,
                "delta_v1_v2": 5,
                "delta_v0_v2": 5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 60,
                "v2_score": 80,
                "delta_v0_v1": 10,
                "delta_v1_v2": 20,
                "delta_v0_v2": 30,
                "weighted_v1": 9.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v0_v1": 40,
                "delta_v1_v2": 0,
                "delta_v0_v2": 40,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 70,
                "v2_score": 90,
                "delta_v0_v1": 10,
                "delta_v1_v2": 20,
                "delta_v0_v2": 30,
                "weighted_v1": 7.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 67.5,
        "overall_v1": 81.5,
        "overall_v2": 87.25,
        "improvement_v0_to_v1": 14.0,
        "improvement_v1_to_v2": 5.75,
        "improvement_v0_to_v2": 19.75,
        "improvement_pct_v0_to_v2": 29.26
    }
