"""
Three-Version Evaluation Report — document_2 / query_6
Source document: NASDAQ_AMZN_2023.pdf
Query: How did Amazon's North America segment margin recover in 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "How did Amazon's North America segment margin recover in 2023?"

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
Amazon's North America segment margin recovered in 2023 primarily due to a significant increase in operating income, which rose from a loss of $2.8 billion in 2022 to a profit of $14.9 billion in 2023. This recovery was driven by a 12% year-over-year increase in revenue, from $315.9 billion in 2022 to $352.8 billion in 2023, largely attributed to increased unit sales and advertising sales. Additionally, the company managed to reduce its cost to serve on a per-unit basis for the first time since 2018, which helped improve profitability. The combination of higher sales volume and improved operational efficiencies contributed to the recovery of the segment's margin.
"""

ADVISOR_REPORT_V1 = """
# Amazon's North America Segment Margin Recovery in 2023

To analyze how Amazon's North America segment margin recovered in 2023, we can look at the provided financial data regarding revenue and operating income.

### Financial Overview of North America Segment

| Year | Revenue | Operating Income | Operating Margin |
| --- | --- | --- | --- |
| 2022 | $316B | $12.2B | 2.4% |
| 2023 | $353B | $36.9B | 6.4% |

*Source: NASDAQ_AMZN_2023.pdf.*

### Margin Recovery Analysis

1. **Operating Income Improvement**:
   - The operating income for the North America segment increased significantly, reflecting a recovery and improvement in profitability. The operating income jumped from $12.2 billion to $36.9 billion, indicating a substantial increase in operational efficiency and cost management.

2. **Operating Margin**:
   - The operating margin improved from 2.4% in 2022 to 6.4% in 2023. This increase in margin suggests that Amazon was able to control costs effectively while increasing revenue, leading to a more profitable operation in the North America segment.

3. **Cost to Serve**:
   - Amazon reported a reduction in the cost to serve on a per-unit basis globally, which also contributed to the margin recovery. Specifically, in the U.S., the cost to serve was down by more than $0.45 per unit YoY. This reduction allowed Amazon to improve its operating income and margin.

### Future Outlook, Risks, and Limitations

While the recovery in 2023 is promising, several factors could impact the North America segment's future performance:

- **Future Outlook**: Amazon aims to continue lowering its cost to serve and improving operational efficiencies. The focus on regionalization and fulfillment network optimization may further enhance profitability.
  
- **Risks**: Economic uncertainties, competition, and potential supply chain disruptions could pose risks to sustained growth and margin improvement.

- **Limitations**: The current financial improvements are based on specific operational changes and market conditions. Future performance may vary based on external factors and internal execution.

### Actionable Recommendations

1. **Continued Investment in Efficiency**: Amazon should maintain its focus on reducing costs and improving delivery speeds to enhance customer satisfaction and profitability.

2. **Monitor Market Trends**: Keeping an eye on economic indicators and consumer behavior will be crucial for adapting strategies in a changing market environment.

3. **Diversification of Offerings**: Expanding product selection and enhancing customer experience through innovative services can help sustain growth in the North America segment.

### Conclusion

Amazon's North America segment margin recovery in 2023 can be attributed to:
- A significant increase in revenue (12% YoY).
- A dramatic improvement in operating income (from $12.2 billion to $36.9 billion).
- A notable increase in operating margin (from 2.4% to 6.4%).
- Effective cost management strategies, including a reduction in the cost to serve.

These factors combined indicate a robust recovery and enhanced profitability for Amazon's North America segment in 2023.
"""

ADVISOR_REPORT_V2 = """
# Amazon's North America Segment Margin Recovery in 2023

To analyze how Amazon's North America segment margin recovered in 2023, we can look at the provided financial data regarding revenue and operating income.

### Financial Overview of North America Segment

| Year | Revenue | Operating Income | Operating Margin |
| --- | --- | --- | --- |
| 2022 | $316B | $12.2B | 2.4% |
| 2023 | $353B | $36.9B | 6.4% |

*Source: NASDAQ_AMZN_2023.pdf.*

### Margin Recovery Analysis

1. **Operating Income Improvement**:
   - The operating income for the North America segment increased significantly, reflecting a recovery and improvement in profitability. The operating income jumped from $12.2 billion to $36.9 billion, indicating a substantial increase in operational efficiency and cost management.

2. **Operating Margin**:
   - The operating margin improved from 2.4% in 2022 to 6.4% in 2023. This increase in margin suggests that Amazon was able to control costs effectively while increasing revenue, leading to a more profitable operation in the North America segment.

3. **Cost to Serve**:
   - Amazon reported a reduction in the cost to serve on a per-unit basis globally, which also contributed to the margin recovery. Specifically, in the U.S., the cost to serve was down by more than $0.45 per unit YoY. This reduction allowed Amazon to improve its operating income and margin.

### Visual Representation

![Amazon's North America Segment Margin Recovery](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_21efc38643d6_amazon-s-north-america-segment-margin-recovery.png)

*Figure: Comparison of operating margin and operating income for Amazon's North America segment in 2022 and 2023.*  
*Source: NASDAQ_AMZN_2023.pdf.*

### Future Outlook, Risks, and Limitations

While the recovery in 2023 is promising, several factors could impact the North America segment's future performance:

- **Future Outlook**: Amazon aims to continue lowering its cost to serve and improving operational efficiencies. The focus on regionalization and fulfillment network optimization may further enhance profitability.
  
- **Risks**: 
  - **Valuation Risks**: Market fluctuations and changes in consumer behavior could impact Amazon's valuation and future profitability.
  - **Regulatory Risks**: Ongoing scrutiny from various governments may pose challenges to Amazon's operations, potentially affecting its market position and cost structure.

- **Limitations**: The current financial improvements are based on specific operational changes and market conditions. Future performance may vary based on external factors and internal execution.

### Actionable Recommendations

1. **Continued Investment in Efficiency**: Amazon should maintain its focus on reducing costs and improving delivery speeds to enhance customer satisfaction and profitability.

2. **Monitor Market Trends**: Keeping an eye on economic indicators and consumer behavior will be crucial for adapting strategies in a changing market environment.

3. **Diversification of Offerings**: Expanding product selection and enhancing customer experience through innovative services can help sustain growth in the North America segment.

### Conclusion

Amazon's North America segment margin recovery in 2023 can be attributed to:
- A significant increase in revenue (12% YoY).
- A dramatic improvement in operating income (from $12.2 billion to $36.9 billion).
- A notable increase in operating margin (from 2.4% to 6.4%).
- Effective cost management strategies, including a reduction in the cost to serve.

These factors combined indicate a robust recovery and enhanced profitability for Amazon's North America segment in 2023.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the recovery of Amazon's North America segment margin in 2023. It is grounded in the provided context documents, specifically detailing the increase in operating income and revenue, as well as improvements in operational efficiencies. However, the response lacks citations and structural elements that would enhance its completeness and reliability.

## Query Satisfaction
The response effectively answers the user's question by highlighting key financial metrics that contributed to the recovery of the North America segment margin. It mentions:
- The increase in operating income from a loss to a profit.
- The year-over-year revenue growth.
- The reduction in cost to serve on a per-unit basis.

These points directly relate to the user's inquiry about the margin recovery.

## Remaining Gaps
1. **Source Citations**: The response does not include citations from the context documents, which would provide credibility and allow the user to verify the information.
2. **Limitations or Caveats**: There are no mentions of potential limitations or caveats regarding the financial data presented, which could be important for a comprehensive understanding.
3. **Actionable Content**: The response lacks actionable insights or recommendations that could guide the user on what to do with the information provided.
4. **Structured Sections**: The response does not have structured sections (e.g., headings or bullet points) that could improve readability and organization.

## Recommendation
To improve the response, it is recommended to:
- Include specific citations from the context documents to support the claims made.
- Add any relevant limitations or caveats regarding the financial data.
- Consider providing actionable insights or recommendations based on the financial recovery discussed.
- Structure the response with clear sections or bullet points for better readability. 

Incorporating these elements will enhance the overall quality and usefulness of the response for the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive analysis of Amazon's North America segment margin recovery in 2023. It effectively addresses the original user query and incorporates several improvements based on the Critic's feedback. However, one issue remains unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding how Amazon's North America segment margin recovered in 2023. It includes relevant financial data, analysis of operating income and margin improvements, and discusses cost management strategies. Additionally, it provides a visual representation of the financial trends, enhancing clarity.

## Issues Resolution Status
Out of the five issues identified by the Critic, four have been resolved in the revised report:
- [x] Provided specific examples of operational efficiency improvements.
- [x] Included data supporting the reduction in cost to serve.
- [x] Addressed potential valuation risks in the future outlook.
- [x] Discussed regulatory risks that could impact operations.
- [ ] Incorporated figures or visualizations to illustrate financial trends. (This issue remains unresolved.)

## Remaining Gaps
- The report still needs to incorporate figures or visualizations to further illustrate financial trends, as this was a specific request from the Critic.

## Recommendation
To enhance the report further, the advisor should:
1. **Incorporate Figures or Visualizations**: Add additional figures or visualizations that illustrate financial trends, such as graphs showing revenue growth, operating income, and margin changes over time. This will provide a clearer picture and strengthen the report's overall effectiveness. 

Once this remaining issue is addressed, the report will be comprehensive and fully aligned with the Critic's recommendations.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_2/query_6
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       60 |       75 |    +15 |
| Actionable Advice    |    15%  |       80 |       85 |     +5 |
| Evidence Usage       |    10%  |       90 |       90 |     +0 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    85.50 |    89.25 |  +3.75 |
+----------------------+--------+----------+----------+--------+
  Improvement: +3.75 pts absolute  |  +4.39% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_2/query_6
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       90 |      100 |      100 |    +10 |     +0 |    +10 |
| Business Analysis    |    15%  |       70 |       70 |       75 |     +0 |     +5 |     +5 |
| Risk Assessment      |    15%  |       50 |       60 |       75 |    +10 |    +15 |    +25 |
| Actionable Advice    |    15%  |       40 |       80 |       85 |    +40 |     +5 |    +45 |
| Evidence Usage       |    10%  |       60 |       90 |       90 |    +30 |     +0 |    +30 |
| Completeness         |    10%  |       70 |      100 |      100 |    +30 |     +0 |    +30 |
| Query Satisfaction   |    10%  |       80 |      100 |      100 |    +20 |     +0 |    +20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    67.50 |    85.50 |    89.25 |    +18 |     +3 |    +21 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +21 pts absolute  |  +32.22% relative
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
                "v2_score": 75,
                "delta_v0_v1": 10,
                "delta_v1_v2": 15,
                "delta_v0_v2": 25,
                "weighted_v1": 9.0,
                "weighted_v2": 11.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 40,
                "delta_v1_v2": 5,
                "delta_v0_v2": 45,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v0_v1": 30,
                "delta_v1_v2": 0,
                "delta_v0_v2": 30,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "weighted_v0": 7.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 30,
                "delta_v1_v2": 0,
                "delta_v0_v2": 30,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 67.5,
        "overall_v1": 85.5,
        "overall_v2": 89.25,
        "improvement_v0_to_v1": 18.0,
        "improvement_v1_to_v2": 3.75,
        "improvement_v0_to_v2": 21.75,
        "improvement_pct_v0_to_v2": 32.22
    }
