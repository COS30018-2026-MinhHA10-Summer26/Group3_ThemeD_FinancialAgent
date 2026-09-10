"""
Full Pipeline Evaluation Report — document_1 / query_8
Source document: NASDAQ_AMZN_2022.pdf
Query: What is Amazon's outlook and strategic priorities discussed in the 2022 annual report?
"""
from __future__ import annotations
import json

USER_QUERY = "What is Amazon's outlook and strategic priorities discussed in the 2022 annual report?"

USER_QUERIES = [
    "What were Amazon's total net sales and net income for fiscal year 2022?",
    "How did Amazon's AWS segment perform in 2022 compared to prior years?",
    "What were the major cost drivers that impacted Amazon's operating income in 2022?",
    "What is Amazon's free cash flow position and how did it change in 2022?",
    "What key risks does Amazon identify in its 2022 annual report?",
    "How did Amazon's international segment perform financially in 2022?",
    "What were Amazon's capital expenditure and investment priorities in 2022?",
    "What is Amazon's outlook and strategic priorities discussed in the 2022 annual report?",
]

ADVISOR_REPORT_V1 = """
# Amazon's Outlook and Strategic Priorities from the 2022 Annual Report

## Overview
In the 2022 annual report, Amazon's leadership reflects on the challenges faced during the year, the strategic adjustments made, and the optimistic outlook for the future. The report emphasizes a commitment to long-term growth, customer experience, and operational efficiency.

## Key Strategic Priorities

### 1. **Customer Experience and Innovation**
- Amazon continues to prioritize enhancing customer experience across its platforms. The leadership acknowledges the importance of innovation in maintaining a competitive edge and improving customer satisfaction.
- The report highlights the success of Amazon Web Services (AWS) and its significant revenue contribution, indicating a focus on expanding and optimizing this segment.

### 2. **Operational Efficiency**
- The company is actively working to reduce fulfillment costs and improve delivery speed. This includes:
  - Reevaluating and restructuring the fulfillment network to transition from a national to a regional model, which aims to lower costs and enhance delivery efficiency.
  - Implementing advanced machine learning algorithms to better predict customer needs and optimize inventory placement.

### 3. **Cost Management and Streamlining Operations**
- Amazon has made tough decisions to eliminate underperforming initiatives and streamline operations. This includes:
  - Shuttering certain physical store concepts and reducing corporate roles by 27,000 to focus resources on more promising ventures.
  - Adjusting programs that were not yielding expected returns, such as free shipping for online grocery orders.

### 4. **Long-Term Investment Focus**
- Despite short-term challenges, Amazon remains committed to long-term investments that can drive future growth. The leadership emphasizes the importance of maintaining a long-term perspective, especially in the face of macroeconomic uncertainties.
- The report discusses the necessity of balancing immediate operational adjustments with ongoing investments in technology and infrastructure.

### 5. **Adaptability to Market Changes**
- Amazon acknowledges the dynamic nature of the market and the need to adapt to changing conditions. The leadership expresses confidence in the company's ability to respond effectively to both challenges and opportunities.

## Financial Performance
Amazon's revenue has shown significant growth, increasing from $245 billion in 2019 to $434 billion in 2022. This growth reflects the company's ability to adapt and innovate in a challenging economic environment.

| Year | Revenue (in billions) |
| --- | --- |
| 2019 | 245 |
| 2022 | 434 |

*Source: NASDAQ_AMZN_2022.pdf*

## Potential Risks and Limitations
While Amazon's strategies are focused on growth and efficiency, potential risks include:
- **Macroeconomic Conditions**: Ongoing economic uncertainties may impact consumer spending and operational costs.
- **Competitive Landscape**: The presence of well-funded competitors in the market may challenge Amazon's market share and pricing strategies.
- **Operational Challenges**: The transition to a regional fulfillment model may encounter unforeseen logistical issues.

## Outlook
The report conveys an optimistic outlook for Amazon's future, driven by a commitment to innovation, customer-centric strategies, and operational improvements. The leadership believes that by focusing on these areas, Amazon can continue to thrive and expand its market presence.

## Conclusion
Amazon's 2022 annual report outlines a strategic focus on enhancing customer experience, improving operational efficiency, managing costs, and maintaining a long-term investment perspective. The leadership's optimism reflects confidence in the company's ability to navigate challenges and seize growth opportunities in the evolving market landscape. 

*Note: Additional financial figures for 2020 and 2021 revenue were not available in the provided context, which could provide a more comprehensive overview of Amazon's growth trajectory.*
"""

ADVISOR_REPORT_V2 = """
# Amazon's Outlook and Strategic Priorities from the 2022 Annual Report

## Overview
In the 2022 annual report, Amazon's leadership reflects on the challenges faced during the year, the strategic adjustments made, and the optimistic outlook for the future. The report emphasizes a commitment to long-term growth, customer experience, and operational efficiency.

## Key Strategic Priorities

### 1. **Customer Experience and Innovation**
- Amazon continues to prioritize enhancing customer experience across its platforms. The leadership acknowledges the importance of innovation in maintaining a competitive edge and improving customer satisfaction.
- The report highlights the success of Amazon Web Services (AWS) and its significant revenue contribution, indicating a focus on expanding and optimizing this segment.

### 2. **Operational Efficiency**
- The company is actively working to reduce fulfillment costs and improve delivery speed. This includes:
  - Reevaluating and restructuring the fulfillment network to transition from a national to a regional model, which aims to lower costs and enhance delivery efficiency.
  - Implementing advanced machine learning algorithms to better predict customer needs and optimize inventory placement.

### 3. **Cost Management and Streamlining Operations**
- Amazon has made tough decisions to eliminate underperforming initiatives and streamline operations. This includes:
  - Shuttering certain physical store concepts and reducing corporate roles by 27,000 to focus resources on more promising ventures.
  - Adjusting programs that were not yielding expected returns, such as free shipping for online grocery orders.

### 4. **Long-Term Investment Focus**
- Despite short-term challenges, Amazon remains committed to long-term investments that can drive future growth. The leadership emphasizes the importance of maintaining a long-term perspective, especially in the face of macroeconomic uncertainties. However, specific details on the nature of these long-term investments and their funding sources were not available in the provided context.

### 5. **Adaptability to Market Changes**
- Amazon acknowledges the dynamic nature of the market and the need to adapt to changing conditions. The leadership expresses confidence in the company's ability to respond effectively to both challenges and opportunities.

## Financial Performance
Amazon's revenue has shown significant growth, increasing from $245 billion in 2019 to $434 billion in 2022. However, revenue figures for 2020 and 2021 are currently unavailable, which limits a comprehensive overview of Amazon's growth trajectory.

| Year | Revenue (in billions) |
| --- | --- |
| 2019 | 245 |
| 2020 | Unavailable |
| 2021 | Unavailable |
| 2022 | 434 |

*Source: NASDAQ_AMZN_2022.pdf*

## Potential Risks and Limitations
While Amazon's strategies are focused on growth and efficiency, potential risks include:
- **Macroeconomic Conditions**: Ongoing economic uncertainties may impact consumer spending and operational costs.
- **Competitive Landscape**: The presence of well-funded competitors in the market may challenge Amazon's market share and pricing strategies.
- **Operational Challenges**: The transition to a regional fulfillment model may encounter unforeseen logistical issues, which could affect delivery times and costs.
- **Valuation and Margin Pressure**: Fluctuations in market valuation and pressure on profit margins due to increased competition and operational costs could pose risks to long-term growth.

## Outlook
The report conveys an optimistic outlook for Amazon's future, driven by a commitment to innovation, customer-centric strategies, and operational improvements. The leadership believes that by focusing on these areas, Amazon can continue to thrive and expand its market presence.

## Conclusion
Amazon's 2022 annual report outlines a strategic focus on enhancing customer experience, improving operational efficiency, managing costs, and maintaining a long-term investment perspective. The leadership's optimism reflects confidence in the company's ability to navigate challenges and seize growth opportunities in the evolving market landscape.

*Note: Specific details on the nature of long-term investments and their funding sources were not available in the provided context, as well as financial figures for 2020 and 2021 revenue.*
"""

EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Amazon's strategic priorities and outlook for 2022. It addresses many of the issues raised in the Critic's report but still leaves some gaps that need to be addressed.

## Query Satisfaction
The revised report adequately answers the original user query regarding Amazon's outlook and strategic priorities discussed in the 2022 annual report. It covers key strategic priorities, operational efficiency, customer experience, and potential risks, aligning well with the user's request.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  1. Provided context and evidence for revenue figures.
  2. Discussed potential challenges of transitioning to a regional fulfillment model.
  3. Included a financial performance chart or figure.
  4. Expanded on long-term investment strategies and funding sources.

- **Unresolved Issue**:
  - Address missing risks related to valuation, supply chain, regulation, and margin pressure.

## Remaining Gaps
The following issue remains unresolved:
- Address missing risks related to valuation, supply chain, regulation, and margin pressure.

## Recommendation
It is recommended that the advisor revises the report to include a detailed discussion of the remaining risks associated with Amazon's strategic initiatives. This will ensure a more comprehensive understanding of the potential challenges the company may face moving forward.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_1/query_8
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       90 |       90 |     +0 |
| Business Analysis    |    15%  |       80 |       80 |     +0 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       60 |       60 |     +0 |
| Evidence Usage       |    10%  |       80 |       80 |     +0 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       90 |       90 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    80.00 |    81.50 |   +1.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +1.5 pts absolute  |  +1.88% relative
==============================================================
```
"""

METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 80,
                "v2_score": 80,
                "delta": 0,
                "weighted_v1": 12.0,
                "weighted_v2": 12.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 80,
                "delta": 10,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v1_score": 60,
                "v2_score": 60,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v1_score": 80,
                "v2_score": 80,
                "delta": 0,
                "weighted_v1": 8.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v1_score": 90,
                "v2_score": 90,
                "delta": 0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v1": 80.0,
        "overall_v2": 81.5,
        "absolute_improvement": 1.5,
        "improvement_percentage": 1.88
    }
