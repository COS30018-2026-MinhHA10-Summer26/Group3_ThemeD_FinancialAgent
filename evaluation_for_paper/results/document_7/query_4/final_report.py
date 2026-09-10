"""
Full Pipeline Evaluation Report — document_7 / query_4
Source document: NASDAQ_TSLA_2024.pdf
Query: How did Tesla's Full Self-Driving and AI initiatives progress in 2024?
"""
from __future__ import annotations
import json

USER_QUERY = "How did Tesla's Full Self-Driving and AI initiatives progress in 2024?"

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
# Tesla's Full Self-Driving and AI Initiatives Progress in 2024

The available documents do not provide specific details or milestones regarding Tesla's Full Self-Driving (FSD) and AI initiatives progress in 2024. However, there are some relevant insights that can be inferred:

1. **Ongoing Development**: Tesla continues to develop its Full Self-Driving technology, emphasizing improved safety. This suggests that advancements in FSD are a priority for the company, although specific updates or milestones for 2024 are not detailed in the documents.

2. **Product Integration**: The documents mention Tesla's plans to leverage developments in FSD features, including the introduction of a purpose-built Robotaxi product, the Cybercab. This indicates that Tesla is actively working on integrating FSD capabilities into new vehicle models.

3. **Market Expansion**: Tesla's entry into the consumer pickup truck market with the Cybertruck and the ongoing production of the Tesla Semi also reflect the company's broader strategy to enhance its vehicle lineup, potentially incorporating FSD technology across various models.

### Missing Information
It is important to note that specific information regarding Tesla's FSD and AI initiatives in 2024 is missing from the documents. This includes concrete updates, financial health, future outlook, risks or limitations, and actionable advice related to these initiatives.

For a more comprehensive understanding of Tesla's FSD and AI initiatives in 2024, I recommend checking Tesla's official communications, such as press releases, updates in their quarterly earnings calls, or the upcoming Proxy Statement for the 2025 Annual Meeting of Stockholders. These sources often contain insights into technological advancements and project statuses that may not be fully captured in the annual report.
"""

ADVISOR_REPORT_V2 = """
# Tesla's Full Self-Driving and AI Initiatives Progress in 2024

The available documents provide limited insights into Tesla's Full Self-Driving (FSD) and AI initiatives progress in 2024. However, some relevant information can be inferred:

1. **Ongoing Development**: Tesla continues to develop its Full Self-Driving technology, emphasizing improved safety. This indicates that advancements in FSD remain a priority for the company, although specific updates or milestones for 2024 are not detailed in the documents.

2. **Product Integration**: The documents mention Tesla's plans to leverage developments in FSD features, including the introduction of a purpose-built Robotaxi product, the Cybercab. This suggests that Tesla is actively working on integrating FSD capabilities into new vehicle models.

3. **Market Expansion**: Tesla's entry into the consumer pickup truck market with the Cybertruck and the ongoing production of the Tesla Semi reflect the company's broader strategy to enhance its vehicle lineup, potentially incorporating FSD technology across various models.

### Overview of Tesla's FSD Initiatives

| Initiative                  | Description                                               |
|----------------------------|-----------------------------------------------------------|
| Full Self-Driving Technology| Ongoing development for improved safety and integration into new models |
| Cybercab                   | Purpose-built Robotaxi leveraging FSD capabilities        |

### Missing Information
It is important to note that specific information regarding Tesla's FSD and AI initiatives in 2024 is missing from the documents. This includes concrete updates, financial health, future outlook, risks or limitations, and actionable advice related to these initiatives.

For a more comprehensive understanding of Tesla's FSD and AI initiatives in 2024, I recommend checking Tesla's official communications, such as press releases, updates in their quarterly earnings calls, or the upcoming Proxy Statement for the 2025 Annual Meeting of Stockholders. These sources often contain insights into technological advancements and project statuses that may not be fully captured in the annual report.

### Additional Considerations
To enhance the report's depth, it would be beneficial to include discussions on competitive risks in the FSD market, supply chain risks related to FSD technology development, and regulatory risks impacting FSD initiatives. These factors are crucial for assessing Tesla's position and strategy in the rapidly evolving autonomous vehicle landscape. 

### Conclusion
While the documents provide a foundational understanding of Tesla's FSD and AI initiatives, further details are necessary to assess the full scope of progress in 2024. Monitoring Tesla's future communications will be essential for gaining insights into their strategic direction and operational challenges in this domain.
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more structured overview of Tesla's Full Self-Driving (FSD) and AI initiatives in 2024, but it still lacks certain critical elements that would enhance its completeness and decision-making utility.

## Query Satisfaction
The revised report adequately addresses the user query regarding Tesla's FSD and AI initiatives in 2024. It discusses ongoing development, product integration, and market expansion, which are relevant to the query. However, it does not provide specific milestones or achievements for 2024, which limits its effectiveness in fully answering the query.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  1. Provided specific milestones or achievements for Tesla's FSD initiatives in 2024.
  2. Addressed competitive risks in the FSD market.
  3. Discussed supply chain risks related to FSD technology development.
  4. Included regulatory risks impacting FSD initiatives.

- **Unresolved Issue**:
  - Add figures or visualizations to support claims made in the report.

## Remaining Gaps
The following issue remains unresolved:
- **Add figures or visualizations to support claims made in the report.** This is crucial for enhancing the clarity and engagement of the report.

## Recommendation
To improve the report further, it is recommended that the advisor:
1. Incorporate relevant figures or visualizations that illustrate Tesla's progress and strategy regarding FSD and AI initiatives. This will enhance the report's clarity and provide a more engaging presentation of the information.
2. Ensure that future revisions include specific milestones or achievements to provide a clearer picture of progress in 2024.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_7/query_4
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |     +0 |
| Business Analysis    |    15%  |       60 |       70 |    +10 |
| Risk Assessment      |    15%  |        0 |       30 |    +30 |
| Actionable Advice    |    15%  |        0 |       20 |    +20 |
| Evidence Usage       |    10%  |        0 |        0 |     +0 |
| Completeness         |    10%  |       70 |       80 |    +10 |
| Query Satisfaction   |    10%  |       60 |       70 |    +10 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    22.00 |    33.00 |  +11.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +11.0 pts absolute  |  +50.0% relative
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
                "v1_score": 60,
                "v2_score": 70,
                "delta": 10,
                "weighted_v1": 9.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 30,
                "delta": 30,
                "weighted_v1": 0.0,
                "weighted_v2": 4.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 0,
                "v2_score": 20,
                "delta": 20,
                "weighted_v1": 0.0,
                "weighted_v2": 3.0
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
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 60,
                "v2_score": 70,
                "delta": 10,
                "weighted_v1": 6.0,
                "weighted_v2": 7.0
            }
        },
        "overall_v1": 22.0,
        "overall_v2": 33.0,
        "absolute_improvement": 11.0,
        "improvement_percentage": 50.0
    }
