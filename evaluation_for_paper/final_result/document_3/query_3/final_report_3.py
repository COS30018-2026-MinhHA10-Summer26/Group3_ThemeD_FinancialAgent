"""
Three-Version Evaluation Report — document_3 / query_3
Source document: NASDAQ_AMZN_2024.pdf
Query: What were the highlights of Amazon's logistics and fulfillment network in 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were the highlights of Amazon's logistics and fulfillment network in 2024?"

USER_QUERIES = [
    "What were Amazon's total net sales and earnings per share for fiscal year 2024?",
    "How did AWS perform in 2024 and what was its contribution to operating profit?",
    "What were the highlights of Amazon's logistics and fulfillment network in 2024?",
    "How did Amazon's subscription services revenue evolve in 2024?",
    "What were Amazon's major capital allocation decisions in 2024?",
    "How did Amazon's international operations perform in 2024?",
    "What were the significant legal and regulatory risks Amazon faced in 2024?",
    "What AI and cloud strategy shifts did Amazon announce or execute in 2024?",
]

# ---------------------------------------------------------------------------
# Responses
# ---------------------------------------------------------------------------

RAG_RESPONSE = """
In 2024, Amazon's logistics and fulfillment network achieved several significant highlights:

1. **Record Shipping Speeds**: Amazon continued to ship at record speeds for Prime members, marking the second consecutive year of such performance. This was attributed to enhancements in their fulfillment network, including regionalization redesign and new placement algorithms.

2. **Expansion of Same-Day and Overnight Delivery**: The company expanded its same-day and overnight delivery services to dozens of smaller cities and towns across the U.S., aiming to improve service for rural customers. This initiative is expected to enable Amazon to deliver over a billion packages annually to customers in 13,000 zip codes.

3. **Innovative Fulfillment Centers**: The introduction of innovative same-day fulfillment centers contributed to the improvement in delivery speeds. These centers are part of Amazon's strategy to enhance customer experience by ensuring faster access to products.

4. **Regionalization of Fulfillment Network**: Amazon's fulfillment network underwent a regionalization redesign, which helped optimize delivery times and efficiency, allowing for faster shipping options.

5. **Investment in Technology and Infrastructure**: Amazon invested heavily in technology and infrastructure to support its logistics capabilities, including enhancements to its fulfillment centers and the introduction of new technologies aimed at improving operational efficiency.

6. **Prime Air Drones**: Amazon continued to develop its Prime Air drone delivery service, which aims to deliver items to customers within an hour, further enhancing the speed of delivery.

These highlights reflect Amazon's ongoing commitment to improving its logistics and fulfillment capabilities, ensuring that customers receive their orders as quickly and efficiently as possible.
"""

ADVISOR_REPORT_V1 = """
# Highlights of Amazon's Logistics and Fulfillment Network in 2024

The available documents do not provide specific highlights or developments regarding Amazon's logistics and fulfillment network for 2024. They primarily focus on Amazon's overall financial performance, customer-centric initiatives, and corporate culture.

However, it is noted that Amazon continued to enhance customer experiences by shipping at record speed to Prime members, indicating improvements in their logistics capabilities. This achievement suggests advancements in their fulfillment processes, although specific details about logistics enhancements, metrics, or initiatives are not provided in the documents.

If you have access to additional documents or sources that might contain more detailed information about Amazon's logistics and fulfillment network in 2024, please share them, and I can assist further.
"""

ADVISOR_REPORT_V2 = """
# Highlights of Amazon's Logistics and Fulfillment Network in 2024

In 2024, Amazon made significant strides in enhancing its logistics and fulfillment network, although specific metrics and detailed initiatives are not explicitly outlined in the available documents. However, several key highlights can be inferred from the overall performance and customer-centric initiatives mentioned in the reports.

1. **Record Shipping Speeds**: Amazon achieved record shipping speeds for Prime members for the second consecutive year. This improvement indicates advancements in their logistics capabilities and fulfillment processes, enhancing customer satisfaction and loyalty.

2. **Expansion of Selection and Price Transparency**: The company continued to expand its product selection and improve price transparency, which likely involved optimizing logistics to ensure efficient inventory management and delivery.

3. **Fulfillment by Amazon (FBA)**: While specific updates on FBA are not provided, the ongoing emphasis on allowing third-party sellers to utilize Amazon's fulfillment network suggests continued investment in logistics infrastructure to support a broader range of products and sellers.

### Revenue Growth by Segment in 2024

While specific logistics metrics are unavailable, the following table summarizes Amazon's revenue growth across different segments in 2024, which may indirectly reflect the effectiveness of their logistics and fulfillment network:

| Segment        | 2023 Revenue ($B) | 2024 Revenue ($B) | YoY Growth (%) |
|----------------|--------------------|--------------------|-----------------|
| North America   | 353                | 387                | 10              |
| International   | 131                | 143                | 9               |
| AWS             | 91                 | 108                | 19              |

### Potential Risks

The report does not address significant risks related to Amazon's logistics operations, which are critical for investors to consider. Key risks may include:

- **Competition**: The logistics and fulfillment sector is highly competitive, with other companies continuously improving their delivery capabilities.
- **Supply Chain Disruptions**: Global supply chain issues can impact inventory levels and delivery times, affecting customer satisfaction.
- **Regulatory Challenges**: Changes in regulations regarding logistics and transportation could impose additional costs or operational constraints.
- **Margin Pressures**: Increased costs associated with logistics improvements could impact profit margins if not managed effectively.
- **Execution Risks**: The complexity of scaling logistics operations while maintaining service quality poses inherent risks.

### Conclusion

While specific details about Amazon's logistics and fulfillment network in 2024 are limited, the company's focus on enhancing customer experiences through faster shipping and expanded selection indicates ongoing improvements in its logistics capabilities. However, investors should remain aware of potential risks that could impact the stability and future performance of Amazon's logistics operations. If you have access to additional documents or sources that might contain more detailed information about Amazon's logistics and fulfillment network in 2024, please share them, and I can assist further.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the highlights of Amazon's logistics and fulfillment network in 2024. However, it lacks citations from the provided context documents and does not include limitations or actionable content, which diminishes its overall quality.

## Query Satisfaction
The response effectively summarizes key highlights of Amazon's logistics and fulfillment network in 2024, including record shipping speeds, expansion of delivery services, innovative fulfillment centers, and investments in technology. These points align well with the user's query.

## Remaining Gaps
1. **Source Citations**: The response does not reference any of the context documents, which is essential for grounding the information provided.
2. **Limitations or Caveats**: There are no mentions of potential limitations or caveats regarding the information presented, which could provide a more balanced view.
3. **Actionable Content**: The response lacks actionable insights or recommendations for the user, which could enhance its utility.

## Recommendation
To improve the response:
- Include citations from the relevant context documents to support the claims made.
- Add any limitations or caveats related to the logistics and fulfillment highlights.
- Consider providing actionable insights or recommendations based on the highlights discussed. 

Incorporating these elements will enhance the credibility and usefulness of the response for the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive overview of Amazon's logistics and fulfillment network in 2024 compared to the initial version. However, it still lacks specific visual data to illustrate logistics performance, which is a critical element for a complete analysis.

## Query Satisfaction
The revised report adequately addresses the user query regarding the highlights of Amazon's logistics and fulfillment network in 2024. It discusses record shipping speeds, expansion of selection, and the implications of these improvements on customer satisfaction. However, it does not provide specific metrics or visual data, which would enhance the understanding of the logistics advancements.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Provided specific metrics on shipping speeds and fulfillment improvements.
  2. Discussed potential risks related to competition, supply chain, regulation, margin pressure, and execution.
  3. Clarified and substantiated claims regarding advancements in logistics capabilities.
  
- **Unresolved**:
  1. Include visual data to illustrate logistics performance.

## Remaining Gaps
The remaining gap is the lack of visual data to illustrate logistics performance. This is essential for providing a clearer understanding of the improvements and their impact.

## Recommendation
It is recommended that the advisor include visual data, such as charts or graphs, that illustrate logistics performance metrics and improvements. This addition would strengthen the report and provide a more comprehensive view of Amazon's logistics and fulfillment network in 2024.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_3/query_3
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |       80 |    +80 |
| Business Analysis    |    15%  |        0 |       70 |    +70 |
| Risk Assessment      |    15%  |        0 |       70 |    +70 |
| Actionable Advice    |    15%  |        0 |       50 |    +50 |
| Evidence Usage       |    10%  |        0 |       60 |    +60 |
| Completeness         |    10%  |       30 |       80 |    +50 |
| Query Satisfaction   |    10%  |       20 |       80 |    +60 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     5.00 |    70.50 |  +65.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +65.5 pts absolute  |  +1310.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_3/query_3
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |       80 |     +0 |    +80 |    +80 |
| Business Analysis    |    15%  |       60 |        0 |       70 |    -60 |    +70 |    +10 |
| Risk Assessment      |    15%  |        0 |        0 |       70 |     +0 |    +70 |    +70 |
| Actionable Advice    |    15%  |        0 |        0 |       50 |     +0 |    +50 |    +50 |
| Evidence Usage       |    10%  |        0 |        0 |       60 |     +0 |    +60 |    +60 |
| Completeness         |    10%  |       40 |       30 |       80 |    -10 |    +50 |    +40 |
| Query Satisfaction   |    10%  |       80 |       20 |       80 |    -60 |    +60 |     +0 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    21.00 |     5.00 |    70.50 |    -16 |    +65 |    +49 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +49 pts absolute  |  +235.71% relative
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
                "v2_score": 80,
                "delta_v0_v1": 0,
                "delta_v1_v2": 80,
                "delta_v0_v2": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 20.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": -60,
                "delta_v1_v2": 70,
                "delta_v0_v2": 10,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 70,
                "delta_v0_v1": 0,
                "delta_v1_v2": 70,
                "delta_v0_v2": 70,
                "weighted_v1": 0.0,
                "weighted_v2": 10.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 50,
                "delta_v0_v1": 0,
                "delta_v1_v2": 50,
                "delta_v0_v2": 50,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 60,
                "delta_v0_v1": 0,
                "delta_v1_v2": 60,
                "delta_v0_v2": 60,
                "weighted_v1": 0.0,
                "weighted_v2": 6.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 40,
                "weighted_v0": 4.0,
                "v1_score": 30,
                "v2_score": 80,
                "delta_v0_v1": -10,
                "delta_v1_v2": 50,
                "delta_v0_v2": 40,
                "weighted_v1": 3.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 20,
                "v2_score": 80,
                "delta_v0_v1": -60,
                "delta_v1_v2": 60,
                "delta_v0_v2": 0,
                "weighted_v1": 2.0,
                "weighted_v2": 8.0
            }
        },
        "overall_v0": 21.0,
        "overall_v1": 5.0,
        "overall_v2": 70.5,
        "improvement_v0_to_v1": -16.0,
        "improvement_v1_to_v2": 65.5,
        "improvement_v0_to_v2": 49.5,
        "improvement_pct_v0_to_v2": 235.71
    }
