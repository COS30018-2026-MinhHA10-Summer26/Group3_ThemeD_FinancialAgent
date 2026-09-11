"""
Three-Version Evaluation Report — document_7 / query_7
Source document: NASDAQ_TSLA_2024.pdf
Query: What regulatory and competitive risks did Tesla highlight in its 2024 annual report?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What regulatory and competitive risks did Tesla highlight in its 2024 annual report?"

USER_QUERIES = [
    "What were Tesla's total revenues, operating income, and net income for fiscal year 2024?",
    "How did Tesla's vehicle delivery volumes and production change in 2024?",
    "What was Tesla's gross margin on automotive sales in 2024 and how did it compare to 2023?",
    "How did Tesla's Full Self-Driving and AI initiatives progress in 2024?",
    "What were the highlights of Tesla's energy and services segments in 2024?",
    "What major capital investments did Tesla make in 2024?",
    "What regulatory and competitive risks did Tesla highlight in its 2024 annual report?",
    "What does Tesla's 2024 annual report say about its Optimus robot and future technology roadmap?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In its 2024 annual report, Tesla highlighted several regulatory and competitive risks:

1. **Regulatory Risks**:
   - Tesla's operations are subject to numerous governmental regulations that vary by jurisdiction, which can impact the sale and operation of its vehicles and energy products. This includes compliance with vehicle safety standards, emissions regulations, and other environmental laws.
   - The company noted the evolving nature of laws regarding self-driving vehicles, which could restrict the design and functionality of its Autopilot and Full Self-Driving (FSD) features. This regulatory patchwork increases complexity and may delay or limit the rollout of new technologies.
   - Changes in government incentives, such as tax credits and rebates for electric vehicles and renewable energy products, could adversely affect demand for Tesla's products. The expiration or reduction of such incentives could make Tesla's offerings less competitive.

2. **Competitive Risks**:
   - The automotive market is highly competitive, with many established and new manufacturers entering the electric vehicle space. This competition could lead to reduced market share and pricing pressures for Tesla.
   - Tesla faces competition not only from traditional automakers but also from new entrants in the electric vehicle market, which could impact its sales and profitability.
   - The energy generation and storage market is also competitive, with various companies offering similar products, which could affect Tesla's market position and pricing strategies.

These risks, if realized, could materially impact Tesla's business, financial condition, and operating results.
"""

ADVISOR_REPORT_V1 = """
# Tesla 2024 Annual Report: Regulatory and Competitive Risks

The regulatory and competitive risks highlighted by Tesla in its 2024 annual report are not explicitly detailed in the available documents. The "Risk Factors" section, which typically contains this critical information, is referenced but not analyzed in the provided context.

To provide a comprehensive analysis of the regulatory and competitive risks, I would need specific details from the "Risk Factors" section of the report. Unfortunately, that section is not included in the documents available for review.

If you have access to the "Risk Factors" section or any additional documents, please share them for further analysis. Otherwise, the specific regulatory and competitive risks Tesla faces in 2024 cannot be confirmed without that information.
"""

ADVISOR_REPORT_V2 = """
# Tesla 2024 Annual Report: Regulatory and Competitive Risks

The regulatory and competitive risks highlighted by Tesla in its 2024 annual report are not explicitly detailed in the available documents. However, some insights can be drawn from the context provided.

## Key Regulatory Risks
1. **Regulatory Environment**: Tesla operates under various regulations related to zero-emission vehicles (ZEVs) and greenhouse gas emissions. The evolving regulatory landscape may impact Tesla's operations and profitability, particularly as it pertains to compliance with emission standards and other regulatory requirements.

2. **Automotive Regulatory Credits**: Tesla earns tradable credits under regulations for ZEVs, which are sold to other regulated entities. Changes in these regulations could affect Tesla's revenue from these credits.

3. **Energy Storage Regulations**: The regulatory framework for energy storage projects is still developing. While there are incentives at federal, state, and local levels, any changes to these policies could impact Tesla's energy storage business.

## Key Competitive Risks
1. **Competition**: Tesla faces significant competition from both established automotive manufacturers and new entrants in the electric vehicle market. This competitive pressure could affect market share and pricing strategies.

2. **Supply Chain Constraints**: The report mentions supply chain constraints, which could impact production and delivery capabilities. These constraints may arise from global supply chain disruptions or increased demand for components.

3. **Margin Pressure**: While not explicitly mentioned in the available documents, the competitive landscape and regulatory changes could exert pressure on Tesla's profit margins.

4. **Execution Risks**: Tesla's ambitious production and technological goals come with inherent execution risks. The ability to meet production targets and maintain quality standards is crucial for sustaining its competitive edge.

## Conclusion
While specific details from the "Risk Factors" section of Tesla's 2024 annual report are not available, the insights drawn from the context highlight several regulatory and competitive risks that could impact Tesla's operations. Unfortunately, without access to the "Risk Factors" section, a comprehensive analysis remains limited. 

If you have access to additional documents or specific details from the "Risk Factors" section, please share them for further analysis.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the regulatory and competitive risks highlighted by Tesla in its 2024 annual report. However, it lacks citations from the provided context documents, which diminishes its credibility and completeness.

## Query Satisfaction
The response effectively covers the key regulatory and competitive risks mentioned in Tesla's 2024 annual report. It identifies specific areas of concern, such as compliance with governmental regulations, the evolving nature of self-driving vehicle laws, and the competitive landscape in both the automotive and energy sectors. Therefore, the response satisfies the user's query.

## Remaining Gaps
1. **Source Citations**: The response does not include citations from the context documents, which are essential for verifying the information provided.
2. **Actionable Content**: The response lacks actionable insights or recommendations for the user regarding how to navigate or respond to these risks.
3. **Structured Elements**: While the response is organized into sections, it could benefit from clearer headings or bullet points to enhance readability.

## Recommendation
To improve the response, it is recommended to:
1. Include specific citations from the context documents to support the claims made about regulatory and competitive risks.
2. Add actionable content or recommendations for stakeholders or investors on how to address or mitigate these risks.
3. Enhance the structure of the response for better clarity and readability.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive overview of the regulatory and competitive risks faced by Tesla in 2024 compared to the initial version. However, it still lacks a visual representation of the risks, which limits its effectiveness.

## Query Satisfaction
The revised report adequately addresses the user query regarding the regulatory and competitive risks highlighted by Tesla in its 2024 annual report. It summarizes key regulatory and competitive risks based on the available context, fulfilling the primary requirement of the query.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**: 
  1. Summarized key regulatory and competitive risks based on available context.
  2. Analyzed and incorporated insights from the context documents regarding competition and supply chain.
  3. Explicitly mentioned and discussed missing risks such as margin pressure and execution risks.
  
- **Unresolved**: 
  1. Consider including figures or visual aids to enhance the report's clarity and effectiveness.

## Remaining Gaps
The only remaining gap is the absence of visual aids or figures that could enhance the clarity and effectiveness of the report. This is a critical aspect that should be addressed to improve the overall quality of the report.

## Recommendation
It is recommended that the advisor include relevant figures or visual aids in the report to better illustrate the regulatory and competitive risks discussed. This addition would significantly enhance the report's clarity and effectiveness for the reader.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_7/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |        0 |       70 |    +70 |
| Risk Assessment      |    15%  |        0 |       80 |    +80 |
| Actionable Advice    |    15%  |        0 |        0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |        0 |       70 |    +70 |
| Query Satisfaction   |    10%  |        0 |       80 |    +80 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     0.00 |    37.50 |  +37.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +37.5 pts absolute  |  +0.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_7/query_7
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Business Analysis    |    15%  |       70 |        0 |       70 |    -70 |    +70 |     +0 |
| Risk Assessment      |    15%  |       85 |        0 |       80 |    -85 |    +80 |     -5 |
| Actionable Advice    |    15%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Evidence Usage       |    10%  |        0 |        0 |        0 |     +0 |     +0 |     +0 |
| Completeness         |    10%  |       70 |        0 |       70 |    -70 |    +70 |     +0 |
| Query Satisfaction   |    10%  |      100 |        0 |       80 |   -100 |    +80 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    40.25 |     0.00 |    37.50 |    -40 |    +37 |     -2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -2 pts absolute  |  -6.83% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -70,
                "delta_v1_v2": 70,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 85,
                "weighted_v0": 12.75,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": -85,
                "delta_v1_v2": 80,
                "delta_v0_v2": -5,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -70,
                "delta_v1_v2": 70,
                "delta_v0_v2": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "weighted_v0": 10.0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": -100,
                "delta_v1_v2": 80,
                "delta_v0_v2": -20,
                "weighted_v1": 0.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v0": 40.25,
        "overall_v1": 0.0,
        "overall_v2": 37.5,
        "improvement_v0_to_v1": -40.25,
        "improvement_v1_to_v2": 37.5,
        "improvement_v0_to_v2": -2.75,
        "improvement_pct_v0_to_v2": -6.83
    }
