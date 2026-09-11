"""
Three-Version Evaluation Report — document_7 / query_4
Source document: NASDAQ_TSLA_2024.pdf
Query: How did Tesla's Full Self-Driving and AI initiatives progress in 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
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

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2024, Tesla's Full Self-Driving (FSD) and AI initiatives made significant progress. The company continued to enhance its FSD (Supervised) capabilities, which included the deployment of advanced driver-assist systems that relieve drivers of many tedious aspects of road travel. Tesla's FSD Computer, which runs neural networks in its vehicles, was further developed to improve real-world performance through continuous training with field data.

A notable milestone was the anticipation of launching the Robotaxi business in 2025, which aims to operate fully autonomous vehicles. This initiative is expected to open access to a new customer base and reflects Tesla's commitment to advancing its AI capabilities. The company also emphasized the importance of its AI learnings from self-driving technology in other areas, such as robotics, exemplified by the development of Optimus, a robotic humanoid.

Financially, Tesla recognized $596 million in revenue from FSD (Supervised) features in 2024, indicating a growing monetization of its AI technologies. Overall, Tesla's focus on improving and deploying its FSD capabilities, alongside its broader AI initiatives, positions the company for continued innovation and market leadership in autonomous driving technology.
"""

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

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The RAG-generated response provides a general overview of Tesla's Full Self-Driving and AI initiatives in 2024, but it lacks specific grounding in the provided context documents and misses critical structural elements.

## Query Satisfaction
The response addresses the user's query about Tesla's Full Self-Driving and AI initiatives in 2024 by mentioning advancements in FSD capabilities, the anticipated launch of the Robotaxi business, and financial performance related to FSD features. However, it does not provide detailed insights or specific data from the context documents that would enhance the response's credibility and depth.

## Remaining Gaps
1. **Lack of Source Citations**: The response does not cite any of the context documents, which is essential for grounding the information provided.
2. **Missing Limitations or Caveats**: There are no acknowledgments of potential limitations or uncertainties regarding the information presented.
3. **Absence of Actionable Content**: The response does not offer any actionable insights or recommendations based on the information provided.
4. **No Structured Sections**: The response lacks a clear structure that would help in organizing the information effectively, making it harder for the user to digest the content.

## Recommendation
To improve the response:
- Include citations from the context documents to support claims made about Tesla's FSD and AI initiatives.
- Acknowledge any limitations or uncertainties related to the information provided.
- Offer actionable insights or recommendations based on the advancements discussed.
- Structure the response into clear sections to enhance readability and comprehension. 

By addressing these gaps, the response would better satisfy the user's query and provide a more comprehensive overview of Tesla's progress in 2024.
"""

PIPELINE_EVALUATION_REPORT = """
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

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_7/query_4
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       85 |        0 |        0 |    -85 |     +0 |    -85 |
| Business Analysis    |    15%  |       70 |       60 |       70 |    -10 |    +10 |     +0 |
| Risk Assessment      |    15%  |       60 |        0 |       30 |    -60 |    +30 |    -30 |
| Actionable Advice    |    15%  |       50 |        0 |       20 |    -50 |    +20 |    -30 |
| Evidence Usage       |    10%  |       40 |        0 |        0 |    -40 |     +0 |    -40 |
| Completeness         |    10%  |       75 |       70 |       80 |     -5 |    +10 |     +5 |
| Query Satisfaction   |    10%  |       80 |       60 |       70 |    -20 |    +10 |    -10 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    67.75 |    22.00 |    33.00 |    -45 |    +11 |    -34 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: -34 pts absolute  |  -51.29% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 85,
                "weighted_v0": 21.25,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -85,
                "delta_v1_v2": 0,
                "delta_v0_v2": -85,
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
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 30,
                "delta_v0_v1": -60,
                "delta_v1_v2": 30,
                "delta_v0_v2": -30,
                "weighted_v1": 0.0,
                "weighted_v2": 4.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 0,
                "v2_score": 20,
                "delta_v0_v1": -50,
                "delta_v1_v2": 20,
                "delta_v0_v2": -30,
                "weighted_v1": 0.0,
                "weighted_v2": 3.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 40,
                "weighted_v0": 4.0,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v0_v1": -40,
                "delta_v1_v2": 0,
                "delta_v0_v2": -40,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 75,
                "weighted_v0": 7.5,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": -5,
                "delta_v1_v2": 10,
                "delta_v0_v2": 5,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
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
            }
        },
        "overall_v0": 67.75,
        "overall_v1": 22.0,
        "overall_v2": 33.0,
        "improvement_v0_to_v1": -45.75,
        "improvement_v1_to_v2": 11.0,
        "improvement_v0_to_v2": -34.75,
        "improvement_pct_v0_to_v2": -51.29
    }
