"""
Full Pipeline Evaluation Report — document_7 / query_7
Source document: NASDAQ_TSLA_2024.pdf
Query: What regulatory and competitive risks did Tesla highlight in its 2024 annual report?
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

EVALUATION_REPORT = """
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

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 80,
                "delta": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 0,
                "delta": 0,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 0,
                "v2_score": 80,
                "delta": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v1": 0.0,
        "overall_v2": 37.5,
        "absolute_improvement": 37.5,
        "improvement_percentage": 0.0
    }
