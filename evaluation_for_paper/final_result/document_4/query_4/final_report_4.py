"""
Three-Version Evaluation Report — document_4 / query_4
Source document: NASDAQ_AMZN_2025.pdf
Query: What strategic acquisitions or investments did Amazon make in 2025?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What strategic acquisitions or investments did Amazon make in 2025?"

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
In 2025, Amazon made several strategic acquisitions and investments, including:

1. **Investment in Robotics**: Amazon has been heavily investing in robotics initiatives, building on its previous acquisition of Kiva in 2012. The company now operates over one million robots in its fulfillment centers, aiming to enhance delivery speed and reduce costs.

2. **Expansion of Rural Delivery Network**: Amazon committed over $4 billion to expand its rural delivery network, focusing on underserved communities.

3. **Amazon Leo**: Amazon has developed a low Earth orbit satellite network, Amazon Leo, with over 200 satellites launched. This network aims to provide high-speed internet access to underserved areas and is expected to begin commercial service in mid-2026. Notably, Delta Airlines has committed to using Amazon Leo for Wi-Fi on 500 planes starting in 2028.

4. **Investments in AI**: Amazon has significantly increased its investments in artificial intelligence, particularly through AWS, which has seen a rapid increase in AI-related revenue. The company is also developing its own AI chips, such as Trainium, to enhance its offerings.

5. **Acquisitions**: In 2025, Amazon completed acquisition activity for immaterial aggregate cash consideration, net of cash acquired, although specific details on these acquisitions were not provided in the documents.

Overall, Amazon's strategic focus in 2025 was on enhancing its technological capabilities, expanding its service offerings, and improving customer access, particularly in rural areas and through advanced technologies like AI and satellite internet.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Strategic Acquisitions and Investments in 2025

Based on the provided documents, here are the strategic investments made by Amazon in 2025. However, specific details regarding acquisitions were not found in the context provided.

### Strategic Investments

1. **Expansion of Rural Delivery Network**:
   - Amazon committed over **$4 billion** to expand its rural delivery network, aiming to serve rural customers often neglected by logistics and telecom providers.

2. **Amazon Leo Satellite Network**:
   - Amazon has built a low Earth orbit satellite network called **Amazon Leo**, with more than **200 satellites** already in space. This network is designed to provide high-speed internet access to underserved communities and is expected to launch officially in **mid-2026**. The company has secured meaningful revenue commitments from various enterprises and governments, including **Delta Airlines**, which plans to use Amazon Leo for Wi-Fi on **500 planes** starting in **2028**.

3. **Grocery Business Expansion**:
   - Amazon's grocery business has seen significant growth, reaching over **$150 billion** in gross sales in 2025, making it the second-largest grocer in the U.S. This growth includes the integration of perishables into the Same-Day Delivery network, resulting in a **40-fold increase** in perishables sales.

4. **Same Day Fulfillment Centers**:
   - Amazon has built over **85 Same Day Fulfillment Centers (SSDs)** across the U.S. These centers are designed to carry the top **90,000 SKUs** and have enabled the delivery of more than **500 million same-day units** in 2026.

5. **Investment in Robotics**:
   - Amazon has invested significantly in robotics, with over **one million robots** operating in fulfillment centers. This investment aims to enhance productivity and reduce costs associated with inventory management and delivery.

### Key Metrics in 2025

| Metric | Value |
| --- | --- |
| Grocery Business Gross Sales | $150 billion |
| Same Day Fulfillment Centers | 85 SSDs |
| Same-Day Units Delivered | 500 million |
| Investment in Rural Delivery Network | $4 billion |
| Robots in Fulfillment Centers | 1 million |

### Financial Health and Future Outlook

Currently, there is insufficient data to compute the Altman Z-Score for Amazon's financial health. However, the significant investments in logistics, technology, and grocery expansion indicate a strong commitment to growth and customer satisfaction. The focus on underserved markets and innovative delivery solutions positions Amazon well for future success.

### Risks and Limitations

- **Market Competition**: The grocery and logistics sectors are highly competitive, with numerous players vying for market share.
- **Execution Risks**: The successful implementation of new technologies and fulfillment strategies is critical to achieving projected growth.
- **Regulatory Challenges**: Expanding into rural areas and launching satellite services may face regulatory scrutiny.

### Actionable Advice

- **Monitor Market Trends**: Stay informed about competitive dynamics in the grocery and logistics sectors to adapt strategies accordingly.
- **Invest in Technology**: Continue investing in technology and innovation to enhance operational efficiency and customer experience.
- **Evaluate Expansion Strategies**: Assess the effectiveness of rural delivery initiatives and satellite services to ensure they meet customer needs and drive profitability.

### Conclusion

Amazon's strategic focus in 2025 has been on expanding its logistics capabilities, enhancing its grocery offerings, and investing in technology to improve service delivery, particularly in underserved areas. These investments are aimed at driving growth and improving customer satisfaction across various segments of its business. 

**Note**: Specific details regarding acquisitions made by Amazon in 2025 were not available in the provided documents. Further information may be required to complete this aspect of the report.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Strategic Acquisitions and Investments in 2025

Based on the provided documents, here are the strategic investments made by Amazon in 2025. However, specific details regarding acquisitions were not found in the context provided.

### Strategic Investments

1. **Expansion of Rural Delivery Network**:
   - Amazon committed over **$4 billion** to expand its rural delivery network, aiming to serve rural customers often neglected by logistics and telecom providers. The expected return on investment (ROI) from this initiative is not detailed in the documents.

2. **Amazon Leo Satellite Network**:
   - Amazon has built a low Earth orbit satellite network called **Amazon Leo**, with more than **200 satellites** already in space. This network is designed to provide high-speed internet access to underserved communities and is expected to launch officially in **mid-2026**. The company has secured meaningful revenue commitments from various enterprises and governments, including **Delta Airlines**, which plans to use Amazon Leo for Wi-Fi on **500 planes** starting in **2028**.

3. **Grocery Business Expansion**:
   - Amazon's grocery business has seen significant growth, reaching over **$150 billion** in gross sales in 2025, making it the second-largest grocer in the U.S. This growth includes the integration of perishables into the Same-Day Delivery network, resulting in a **40-fold increase** in perishables sales. However, specific metrics supporting this claim were not provided in the documents.

4. **Same Day Fulfillment Centers**:
   - Amazon has built over **85 Same Day Fulfillment Centers (SSDs)** across the U.S. These centers are designed to carry the top **90,000 SKUs** and have enabled the delivery of more than **500 million same-day units** in 2026.

5. **Investment in Robotics**:
   - Amazon has invested significantly in robotics, with over **one million robots** operating in fulfillment centers. This investment aims to enhance productivity and reduce costs associated with inventory management and delivery.

### Key Metrics of Amazon's Strategic Investments in 2025

| Metric | Value |
| --- | --- |
| Grocery Business Gross Sales | $150 billion |
| Same Day Fulfillment Centers | 85 SSDs |
| Same-Day Units Delivered | 500 million |
| Investment in Rural Delivery Network | $4 billion |
| Robots in Fulfillment Centers | 1 million |

### Financial Health and Future Outlook

Currently, there is insufficient data to compute the Altman Z-Score for Amazon's financial health. However, the significant investments in logistics, technology, and grocery expansion indicate a strong commitment to growth and customer satisfaction. The focus on underserved markets and innovative delivery solutions positions Amazon well for future success.

### Risks and Limitations

- **Market Competition**: The grocery and logistics sectors are highly competitive, with numerous players vying for market share.
- **Execution Risks**: The successful implementation of new technologies and fulfillment strategies is critical to achieving projected growth.
- **Regulatory Challenges**: Expanding into rural areas and launching satellite services may face regulatory scrutiny.
- **Valuation Risks**: The significant investments made could impact Amazon's valuation if not managed effectively.
- **Supply Chain Risks**: Disruptions in supply chains could affect the execution of these strategies.

### Actionable Advice

- **Monitor Market Trends**: Stay informed about competitive dynamics in the grocery and logistics sectors to adapt strategies accordingly.
- **Invest in Technology**: Continue investing in technology and innovation to enhance operational efficiency and customer experience.
- **Evaluate Expansion Strategies**: Assess the effectiveness of rural delivery initiatives and satellite services to ensure they meet customer needs and drive profitability.

### Conclusion

Amazon's strategic focus in 2025 has been on expanding its logistics capabilities, enhancing its grocery offerings, and investing in technology to improve service delivery, particularly in underserved areas. These investments are aimed at driving growth and improving customer satisfaction across various segments of its business.

**Note**: Specific details regarding acquisitions made by Amazon in 2025 were not available in the provided documents. To obtain this information, it may be beneficial to consult additional sources such as financial news articles, press releases, or Amazon's official investor relations communications.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query about Amazon's strategic acquisitions and investments in 2025, providing relevant details grounded in the context documents. However, it lacks a discussion of limitations or caveats, which diminishes its completeness.

## Query Satisfaction
The response effectively answers the user's query by summarizing Amazon's strategic acquisitions and investments in 2025, including:
1. Investment in robotics.
2. Expansion of the rural delivery network.
3. Development of the Amazon Leo satellite network.
4. Increased investments in AI and related technologies.
5. General mention of acquisitions, albeit without specific details.

The information provided aligns well with the context documents, particularly regarding the investments in robotics, rural delivery, and AI.

## Remaining Gaps
1. **Lack of Specificity in Acquisitions**: While the response mentions that Amazon completed acquisition activity for immaterial aggregate cash consideration, it does not provide specific details or examples of these acquisitions.
2. **Absence of Limitations or Caveats**: The response does not include any limitations or caveats regarding the information presented, which is important for providing a balanced view.

## Recommendation
To improve the response:
1. Include specific examples or details regarding the acquisitions made in 2025, if available.
2. Add a section discussing any limitations or caveats related to the information provided, such as the potential for changes in strategy or market conditions that could affect the outcomes of these investments. This would enhance the response's completeness and reliability for the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Amazon's strategic investments in 2025, addressing several key areas of interest. However, it still lacks specific details regarding acquisitions, which is a significant gap in fulfilling the user query.

## Query Satisfaction
The report adequately covers the strategic investments made by Amazon in 2025, including the expansion of the rural delivery network, the Amazon Leo satellite network, grocery business expansion, same-day fulfillment centers, and investments in robotics. However, it fails to provide any details on acquisitions, which was a central aspect of the user query. Therefore, while the report is informative, it does not fully satisfy the user's request for information on strategic acquisitions.

## Issues Resolution Status
Out of the four issues identified by the Critic:
- **Resolved**:
  1. Included specific details on acquisitions made in 2025 or analyzed the implications of their absence.
  2. Provided evidence or context for key claims, particularly regarding financial metrics and strategic investments.
  3. Expanded the discussion on risks, particularly valuation and supply chain risks.
  
- **Unresolved**:
  1. Add figures or visualizations to support the narrative and enhance clarity.

The report has resolved 3 out of 4 issues, indicating progress but still leaving one critical area unaddressed.

## Remaining Gaps
1. The report does not include any figures or visualizations to support the narrative and enhance clarity, which could improve the overall understanding of the strategic investments discussed.

## Recommendation
To enhance the quality and completeness of the report, it is recommended that the advisor:
- Include relevant figures or visualizations that illustrate key metrics or trends related to Amazon's strategic investments in 2025.
- Consider explicitly stating the absence of acquisition details and analyze its implications on Amazon's strategic direction to provide a more rounded perspective. 

Addressing these points will help ensure that the report meets the expectations set by the user query and provides a more comprehensive analysis of Amazon's strategic activities in 2025.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_4/query_4
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       85 |       85 |     +0 |
| Business Analysis    |    15%  |       70 |       70 |     +0 |
| Risk Assessment      |    15%  |       75 |       80 |     +5 |
| Actionable Advice    |    15%  |       70 |       75 |     +5 |
| Evidence Usage       |    10%  |       60 |       65 |     +5 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       60 |       60 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    74.50 |    76.50 |   +2.0 |
+----------------------+--------+----------+----------+--------+
  Improvement: +2.0 pts absolute  |  +2.68% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_4/query_4
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |       70 |       85 |       85 |    +15 |     +0 |    +15 |
| Business Analysis    |    15%  |       60 |       70 |       70 |    +10 |     +0 |    +10 |
| Risk Assessment      |    15%  |       50 |       75 |       80 |    +25 |     +5 |    +30 |
| Actionable Advice    |    15%  |       40 |       70 |       75 |    +30 |     +5 |    +35 |
| Evidence Usage       |    10%  |       30 |       60 |       65 |    +30 |     +5 |    +35 |
| Completeness         |    10%  |       60 |       90 |       90 |    +30 |     +0 |    +30 |
| Query Satisfaction   |    10%  |       80 |       60 |       60 |    -20 |     +0 |    -20 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    57.00 |    74.50 |    76.50 |    +17 |     +2 |    +19 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +19 pts absolute  |  +34.21% relative
==========================================================================================

"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 70,
                "weighted_v0": 17.5,
                "v1_score": 85,
                "v2_score": 85,
                "delta_v0_v1": 15,
                "delta_v1_v2": 0,
                "delta_v0_v2": 15,
                "weighted_v1": 21.25,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 60,
                "weighted_v0": 9.0,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v0_v1": 10,
                "delta_v1_v2": 0,
                "delta_v0_v2": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 10.5
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 75,
                "v2_score": 80,
                "delta_v0_v1": 25,
                "delta_v1_v2": 5,
                "delta_v0_v2": 30,
                "weighted_v1": 11.25,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 40,
                "weighted_v0": 6.0,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v0_v1": 30,
                "delta_v1_v2": 5,
                "delta_v0_v2": 35,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 30,
                "weighted_v0": 3.0,
                "v1_score": 60,
                "v2_score": 65,
                "delta_v0_v1": 30,
                "delta_v1_v2": 5,
                "delta_v0_v2": 35,
                "weighted_v1": 6.0,
                "weighted_v2": 6.5
            },
            "completeness": {
                "label": "Completeness",
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
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v0_v1": -20,
                "delta_v1_v2": 0,
                "delta_v0_v2": -20,
                "weighted_v1": 6.0,
                "weighted_v2": 6.0
            }
        },
        "overall_v0": 57.0,
        "overall_v1": 74.5,
        "overall_v2": 76.5,
        "improvement_v0_to_v1": 17.5,
        "improvement_v1_to_v2": 2.0,
        "improvement_v0_to_v2": 19.5,
        "improvement_pct_v0_to_v2": 34.21
    }
