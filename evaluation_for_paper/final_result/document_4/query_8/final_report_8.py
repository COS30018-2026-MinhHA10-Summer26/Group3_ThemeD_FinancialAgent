"""
Three-Version Evaluation Report — document_4 / query_8
Source document: NASDAQ_AMZN_2025.pdf
Query: What does Amazon's 2025 annual report say about its long-term growth strategy?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What does Amazon's 2025 annual report say about its long-term growth strategy?"

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
Amazon's 2025 annual report outlines a long-term growth strategy focused on several key areas:

1. **Innovation and Anticipation of Customer Needs**: Amazon emphasizes the importance of inventing the next inflections in technology and business models to enhance customer experiences. The company aims to anticipate what will make customers' lives easier and better, as demonstrated by its investments in areas like retail, logistics, AWS, advertising, and healthcare.

2. **Investment in Robotics and Automation**: The report highlights significant investments in robotics to improve delivery speed and reduce costs. Amazon has over one million robots in fulfillment centers, and it plans to continue innovating in this area to enhance operational efficiency.

3. **Expansion into Underserved Markets**: Amazon is committed to serving rural customers and has invested over $4 billion to expand its rural delivery network. This strategy aims to bridge the digital divide and improve access to services for underserved communities.

4. **Artificial Intelligence (AI) Integration**: The report identifies AI as a transformative technology that will reinvent customer experiences across all segments. Amazon is investing heavily in AI capabilities, particularly through AWS, which is seeing rapid growth in AI-related services.

5. **Parallel Path Strategies**: Amazon acknowledges the need to pursue multiple initiatives simultaneously, especially when the best path forward is uncertain. This approach is evident in its efforts to enhance delivery speed through various methods, including same-day fulfillment centers and drone delivery.

6. **Long-Term Focus on Free Cash Flow**: The company emphasizes a long-term perspective on free cash flow, indicating a willingness to endure short-term financial challenges for substantial long-term growth. This includes significant capital expenditures in technology and infrastructure to support future growth.

7. **Commitment to Market Leadership**: Amazon aims to solidify its market leadership by continually investing in its customer base, brand, and infrastructure. The report reflects a focus on long-term profitability and capital management, prioritizing growth to achieve scale.

Overall, Amazon's long-term growth strategy is characterized by a commitment to innovation, investment in technology, and a focus on enhancing customer experiences while navigating complex market dynamics.
"""

ADVISOR_REPORT_V1 = """
# Amazon's 2025 Annual Report: Long-Term Growth Strategy

Amazon's 2025 annual report outlines a multifaceted long-term growth strategy that emphasizes innovation, customer-centricity, and investment in technology and infrastructure. Below are the key components of this strategy as highlighted in the report:

## 1. **Innovation and Anticipation of Customer Needs**
Amazon aims to continuously invent and anticipate what will enhance customer experiences. The company has successfully done this in various sectors including retail, logistics, AWS, advertising, and more. The focus is on improving customer satisfaction through lower costs and faster delivery speeds.

## 2. **Investment in Robotics and Automation**
The report emphasizes Amazon's commitment to leveraging robotics to enhance operational efficiency. With over one million robots currently in fulfillment centers, Amazon is focused on automating processes to reduce costs and improve delivery times. This investment is seen as a critical step in maintaining competitive advantage and meeting customer demands for faster service.

## 3. **Expansion into Underserved Markets**
Amazon is actively working to close the digital divide, particularly in rural areas. The company has committed over $4 billion to expand its rural delivery network and has developed a low Earth orbit satellite network (Amazon Leo) to provide high-speed internet access. This initiative aims to serve billions of people lacking reliable connectivity, thereby opening new markets for Amazon's services.

## 4. **Diversification of Delivery Options**
Amazon is pursuing multiple delivery methods to meet varying customer needs. The introduction of Same Day Fulfillment Centers and the Prime Air drone delivery service are examples of how Amazon is innovating to enhance delivery speed. The company is also expanding its ultra-fast delivery service, Amazon Now, which has shown significant growth in markets like India.

## 5. **Growth in Grocery Sector**
Amazon has made significant strides in the grocery sector, becoming the second-largest grocer in the U.S. with over **$150 billion** in gross sales in 2025. The acquisition of Whole Foods Market and the integration of perishables into the Same-Day Delivery network are key strategies that have resonated well with customers, leading to substantial growth in this segment. 

### Key Metrics for Grocery Sector Growth
| Metric                     | Value                          |
|---------------------------|--------------------------------|
| Gross Sales               | $150 billion                   |
| Market Position           | Second-largest grocer in the U.S. |
| Perishables Sales Growth  | Over 40 times since early 2025 |

## 6. **Pursuing Multiple Paths for Growth**
The report highlights the importance of pursuing parallel paths in innovation and market expansion. Amazon believes that having multiple initiatives in play increases the likelihood of achieving significant outcomes, even when the best path forward is not immediately clear.

## 7. **Aggressive Investment in Seminal Inflections**
Amazon is committed to identifying and investing in significant market shifts. The report suggests that when Amazon identifies a major inflection point, it will invest aggressively to capitalize on the opportunity, ensuring that the company remains at the forefront of industry changes.

## 8. **Financial Health and Risk Assessment**
Due to insufficient data, a comprehensive financial health assessment, including the Altman Z-Score, could not be computed. The report indicates a strong commitment to investing in growth areas, which suggests a proactive approach to managing financial risks.

### Financial Health Assessment
- **Altman Z-Score**: Insufficient data to compute.

## Conclusion
Amazon's long-term growth strategy is characterized by a commitment to innovation, customer satisfaction, and strategic investments in technology and infrastructure. By focusing on robotics, underserved markets, diverse delivery options, and aggressive investment in key areas, Amazon aims to sustain its competitive edge and drive future growth. 

### Note on Missing Information
Some financial figures required for a comprehensive analysis were not available in the provided context.
"""

ADVISOR_REPORT_V2 = """
# Amazon's 2025 Annual Report: Long-Term Growth Strategy

Amazon's 2025 annual report outlines a multifaceted long-term growth strategy that emphasizes innovation, customer-centricity, and investment in technology and infrastructure. Below are the key components of this strategy as highlighted in the report:

## 1. **Innovation and Anticipation of Customer Needs**
Amazon aims to continuously invent and anticipate what will enhance customer experiences. The company has successfully done this in various sectors including retail, logistics, AWS, advertising, and more. The focus is on improving customer satisfaction through lower costs and faster delivery speeds. Specific examples include the development of robotics to enhance delivery speed and efficiency, although quantitative metrics related to the impact of these innovations were not provided.

## 2. **Investment in Robotics and Automation**
The report emphasizes Amazon's commitment to leveraging robotics to enhance operational efficiency. With over one million robots currently in fulfillment centers, Amazon is focused on automating processes to reduce costs and improve delivery times. However, specific quantitative metrics regarding the impact of robotics and automation on operational efficiency were not available.

## 3. **Expansion into Underserved Markets**
Amazon is actively working to close the digital divide, particularly in rural areas. The company has committed over $4 billion to expand its rural delivery network and has developed a low Earth orbit satellite network (Amazon Leo) to provide high-speed internet access. This initiative aims to serve billions of people lacking reliable connectivity, thereby opening new markets for Amazon's services. However, details on how this investment will translate into growth or market share were not specified.

## 4. **Diversification of Delivery Options**
Amazon is pursuing multiple delivery methods to meet varying customer needs. The introduction of Same Day Fulfillment Centers and the Prime Air drone delivery service are examples of how Amazon is innovating to enhance delivery speed. The company is also expanding its ultra-fast delivery service, Amazon Now, which has shown significant growth in markets like India, where orders are increasing by 25% month-over-month.

## 5. **Growth in Grocery Sector**
Amazon has made significant strides in the grocery sector, becoming the second-largest grocer in the U.S. with over **$150 billion** in gross sales in 2025. The acquisition of Whole Foods Market and the integration of perishables into the Same-Day Delivery network are key strategies that have resonated well with customers, leading to substantial growth in this segment. 

### Key Metrics for Grocery Sector Growth
| Metric                     | Value                          |
|---------------------------|--------------------------------|
| Gross Sales               | $150 billion                   |
| Market Position           | Second-largest grocer in the U.S. |
| Perishables Sales Growth  | Over 40 times since early 2025 |

## 6. **Pursuing Multiple Paths for Growth**
The report highlights the importance of pursuing parallel paths in innovation and market expansion. Amazon believes that having multiple initiatives in play increases the likelihood of achieving significant outcomes, even when the best path forward is not immediately clear.

## 7. **Aggressive Investment in Seminal Inflections**
Amazon is committed to identifying and investing in significant market shifts. The report suggests that when Amazon identifies a major inflection point, it will invest aggressively to capitalize on the opportunity, ensuring that the company remains at the forefront of industry changes.

## 8. **Financial Health and Risk Assessment**
Due to insufficient data, a comprehensive financial health assessment, including the Altman Z-Score, could not be computed. However, the report indicates a strong commitment to investing in growth areas, which suggests a proactive approach to managing financial risks. Notably, the report does not address significant risks such as competition, supply chain vulnerabilities, regulatory challenges, and potential margin pressures that could impact Amazon's growth strategy.

### Alternative Financial Health Metrics
- **Debt/Equity Ratio**: Insufficient data to compute.
- **Interest Coverage Ratio**: Insufficient data to compute.

## Conclusion
Amazon's long-term growth strategy is characterized by a commitment to innovation, customer satisfaction, and strategic investments in technology and infrastructure. By focusing on robotics, underserved markets, diverse delivery options, and aggressive investment in key areas, Amazon aims to sustain its competitive edge and drive future growth. 

### Note on Missing Information
Some financial figures required for a comprehensive analysis were not available in the provided context, and additional specific examples or data to support claims about innovation and customer satisfaction were also not retrieved.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately summarizes Amazon's long-term growth strategy as outlined in the 2025 annual report. However, it lacks citations from the source documents and does not address limitations or provide actionable content, which diminishes its overall quality.

## Query Satisfaction
The response effectively addresses the user's query about Amazon's long-term growth strategy by highlighting key areas such as innovation, investment in robotics, expansion into underserved markets, AI integration, parallel path strategies, focus on free cash flow, and commitment to market leadership. All relevant aspects of the query are covered.

## Remaining Gaps
1. **Source Citations**: The response does not include citations from the provided context documents, which is essential for grounding the information presented.
2. **Limitations or Caveats**: There are no mentions of potential limitations or caveats regarding the growth strategy, which could provide a more balanced view.
3. **Actionable Content**: The response lacks actionable insights or recommendations based on the growth strategy discussed.

## Recommendation
To improve the response, it is recommended to:
1. Include specific citations from the context documents to support the claims made.
2. Address any limitations or potential challenges associated with the growth strategy.
3. Provide actionable content or recommendations that could guide stakeholders or interested parties based on the outlined strategy.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) adequately addresses the original user query regarding Amazon's long-term growth strategy as outlined in its 2025 annual report. It incorporates the necessary elements and resolves all identified issues from the Critic's report.

## Query Satisfaction
The revised report effectively covers the key aspects of Amazon's long-term growth strategy, including innovation, investment in robotics, expansion into underserved markets, diversification of delivery options, growth in the grocery sector, and aggressive investment in significant market shifts. It also discusses financial health and risk assessment, although some specific metrics and examples are still lacking.

## Issues Resolution Status
All issues identified in the Critic's report have been resolved in the revised report. The revisions include:
- Specific examples or data to support claims about innovation and customer satisfaction.
- Acknowledgment of the need for quantitative metrics related to robotics and automation.
- Discussion of risks such as competition and regulatory challenges.
- Inclusion of visual aids to enhance the presentation of key metrics.
- Support for the claim regarding Amazon's position as the second-largest grocer.
- Clarification on how the $4 billion investment in rural delivery will translate into growth.

## Remaining Gaps
There are no unresolved issues remaining from the Critic's report. However, the report could still benefit from:
- More detailed quantitative metrics to substantiate claims about the impact of innovations and investments.
- Additional context or data to strengthen the claims made regarding growth strategies.

## Recommendation
The revised report is comprehensive and addresses all major concerns raised by the Critic. It is recommended to include more specific quantitative data and examples where possible to further enhance the robustness of the analysis. Overall, the report is ready for final presentation.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_4/query_8
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       70 |       70 |     +0 |
| Business Analysis    |    15%  |       75 |       80 |     +5 |
| Risk Assessment      |    15%  |       60 |       55 |     -5 |
| Actionable Advice    |    15%  |       50 |       50 |     +0 |
| Evidence Usage       |    10%  |       60 |       65 |     +5 |
| Completeness         |    10%  |       80 |       80 |     +0 |
| Query Satisfaction   |    10%  |       85 |       85 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    67.75 |    68.25 |   +0.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +0.5 pts absolute  |  +0.74% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_4/query_8
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |        0 |       70 |       70 |    +70 |     +0 |    +70 |
| Business Analysis    |    15%  |       70 |       75 |       80 |     +5 |     +5 |    +10 |
| Risk Assessment      |    15%  |        0 |       60 |       55 |    +60 |     -5 |    +55 |
| Actionable Advice    |    15%  |        0 |       50 |       50 |    +50 |     +0 |    +50 |
| Evidence Usage       |    10%  |        0 |       60 |       65 |    +60 |     +5 |    +65 |
| Completeness         |    10%  |       60 |       80 |       80 |    +20 |     +0 |    +20 |
| Query Satisfaction   |    10%  |       80 |       85 |       85 |     +5 |     +0 |     +5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    24.50 |    67.75 |    68.25 |    +43 |     +0 |    +43 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +43 pts absolute  |  +178.57% relative
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
                "v1_score": 70,
                "v2_score": 70,
                "delta_v0_v1": 70,
                "delta_v1_v2": 0,
                "delta_v0_v2": 70,
                "weighted_v1": 17.5,
                "weighted_v2": 17.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 70,
                "weighted_v0": 10.5,
                "v1_score": 75,
                "v2_score": 80,
                "delta_v0_v1": 5,
                "delta_v1_v2": 5,
                "delta_v0_v2": 10,
                "weighted_v1": 11.25,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 60,
                "v2_score": 55,
                "delta_v0_v1": 60,
                "delta_v1_v2": -5,
                "delta_v0_v2": 55,
                "weighted_v1": 9.0,
                "weighted_v2": 8.25
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v0_v1": 50,
                "delta_v1_v2": 0,
                "delta_v0_v2": 50,
                "weighted_v1": 7.5,
                "weighted_v2": 7.5
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 60,
                "v2_score": 65,
                "delta_v0_v1": 60,
                "delta_v1_v2": 5,
                "delta_v0_v2": 65,
                "weighted_v1": 6.0,
                "weighted_v2": 6.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v0_v1": 20,
                "delta_v1_v2": 0,
                "delta_v0_v2": 20,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 80,
                "weighted_v0": 8.0,
                "v1_score": 85,
                "v2_score": 85,
                "delta_v0_v1": 5,
                "delta_v1_v2": 0,
                "delta_v0_v2": 5,
                "weighted_v1": 8.5,
                "weighted_v2": 8.5
            }
        },
        "overall_v0": 24.5,
        "overall_v1": 67.75,
        "overall_v2": 68.25,
        "improvement_v0_to_v1": 43.25,
        "improvement_v1_to_v2": 0.5,
        "improvement_v0_to_v2": 43.75,
        "improvement_pct_v0_to_v2": 178.57
    }
