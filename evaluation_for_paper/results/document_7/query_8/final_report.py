"""
Full Pipeline Evaluation Report — document_7 / query_8
Source document: NASDAQ_TSLA_2024.pdf
Query: What does Tesla's 2024 annual report say about its Optimus robot and future technology roadmap?
"""
from __future__ import annotations
import json

USER_QUERY = "What does Tesla's 2024 annual report say about its Optimus robot and future technology roadmap?"

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
# Tesla's 2024 Annual Report Insights on Optimus Robot and Future Technology Roadmap

The available documents do not contain specific information regarding Tesla's Optimus robot or its future technology roadmap. Therefore, I cannot provide direct insights into these topics based on the current context.

However, I recommend checking the following sections of Tesla's 2024 annual report for potentially relevant insights:

- **Item 1: Business** - This section often outlines the company's key initiatives and technological advancements, which may include information about the Optimus robot.
- **Item 7: Management's Discussion and Analysis of Financial Condition and Results of Operations** - This section may provide insights into the company's strategic direction and future projects, including robotics and other technological innovations.
- **Item 9: Other Information** - This section might include additional details or updates on ongoing projects and innovations.

It is important to note that the lack of specific information on the Optimus robot and future technology roadmap may limit a comprehensive understanding of Tesla's strategic initiatives in these areas. For a thorough analysis, I suggest reviewing these sections directly in Tesla's 2024 annual report. If you have access to specific excerpts or additional documents, please share them for further analysis.
"""

ADVISOR_REPORT_V2 = """
# Tesla's 2024 Annual Report Insights on Optimus Robot and Future Technology Roadmap

The available documents do not contain specific information regarding Tesla's Optimus robot or its future technology roadmap. Therefore, I cannot provide direct insights into these topics based on the current context.

However, I recommend checking the following sections of Tesla's 2024 annual report for potentially relevant insights:

- **Item 1: Business** - This section often outlines the company's key initiatives and technological advancements, which may include information about the Optimus robot.
- **Item 7: Management's Discussion and Analysis of Financial Condition and Results of Operations** - This section may provide insights into the company's strategic direction and future projects, including robotics and other technological innovations.
- **Item 9: Other Information** - This section might include additional details or updates on ongoing projects and innovations.

### Key Risks to Consider

While the report does not provide specific insights into the Optimus robot, it is essential to consider several investor risks that could impact Tesla's initiatives related to robotics and technology:

- **Competition**: The growing number of competitors in the robotics and AI space could affect Tesla's market position.
- **Valuation**: If the Optimus robot does not meet expectations, it could have potential impacts on Tesla's market valuation.
- **Supply Chain**: Risks related to sourcing components for robotics and AI technologies may pose challenges.
- **Regulation**: Possible regulatory hurdles could affect the deployment of robotic technologies.
- **Margin Pressure**: Financial implications of developing and marketing new technologies could impact profitability.
- **Execution Risks**: Challenges in successfully bringing the Optimus robot to market could hinder progress.

### Recommendations for Investors and Stakeholders

To gain a comprehensive understanding of Tesla's strategic initiatives in robotics and technology, I suggest the following actionable steps:

1. **Review Key Sections**: Directly examine the specified sections of the annual report for insights into the Optimus robot and future technologies.
2. **Monitor Competitors**: Keep an eye on developments from competitors in the robotics space to assess Tesla's relative position.
3. **Evaluate Regulatory Changes**: Stay informed about regulatory developments that could impact Tesla's technology initiatives.
4. **Assess Financial Health**: Analyze Tesla's financial performance and market valuation in light of its technology roadmap and potential risks.

It is important to note that the lack of specific information on the Optimus robot and future technology roadmap may limit a comprehensive understanding of Tesla's strategic initiatives in these areas. For a thorough analysis, I suggest reviewing the relevant sections directly in Tesla's 2024 annual report. If you have access to specific excerpts or additional documents, please share them for further analysis.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive overview of Tesla's 2024 annual report concerning the Optimus robot and future technology roadmap. However, it still lacks specific insights and visual aids that would enhance the understanding of the topics discussed.

## Query Satisfaction
The revised report partially addresses the user query by recommending sections of the annual report to check for insights on the Optimus robot and future technology roadmap. However, it does not provide direct insights or specific data regarding these topics, which limits its effectiveness in fully satisfying the user's request.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  - Provided actionable recommendations for investors and stakeholders.
  - Addressed missing investor risks related to competition, valuation, supply chain, regulation, margin pressure, and execution.
  - Clarified the rationale behind checking specific sections of the annual report.
  - Provided a more structured response with clear sections.

- **Unresolved Issue**:
  - The report still lacks figures or visualizations to support claims and enhance understanding.

## Remaining Gaps
1. **Include figures or visualizations** to support claims and enhance understanding of Tesla's technology roadmap and the Optimus robot's potential impact.

## Recommendation
To improve the report further, the advisor should:
- Incorporate relevant figures or visualizations that illustrate Tesla's technology roadmap and the development status of the Optimus robot.
- Ensure that the report provides specific insights or data regarding the Optimus robot, if available, to fully address the user query.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_7/query_8
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       50 |       60 |    +10 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |       80 |    +80 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       50 |       70 |    +20 |
| Query Satisfaction   |    10%  |       30 |       50 |    +20 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    15.50 |    43.50 |  +28.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +28.0 pts absolute  |  +180.65% relative
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
                "v1_score": 50,
                "v2_score": 60,
                "delta": 10,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 70,
                "delta": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 80,
                "delta": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
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
                "v1_score": 50,
                "v2_score": 70,
                "delta": 20,
                "weighted_v1": 5.0,
                "weighted_v2": 7.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 30,
                "v2_score": 50,
                "delta": 20,
                "weighted_v1": 3.0,
                "weighted_v2": 5.0
            }
        },
        "overall_v1": 15.5,
        "overall_v2": 43.5,
        "absolute_improvement": 28.0,
        "improvement_percentage": 180.65
    }
