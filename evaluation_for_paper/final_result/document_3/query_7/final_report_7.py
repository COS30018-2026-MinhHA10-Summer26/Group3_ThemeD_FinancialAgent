"""
Three-Version Evaluation Report — document_3 / query_7
Source document: NASDAQ_AMZN_2024.pdf
Query: What were the significant legal and regulatory risks Amazon faced in 2024?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What were the significant legal and regulatory risks Amazon faced in 2024?"

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
In 2024, Amazon faced several significant legal and regulatory risks, including:

1. **Government Regulation and Compliance**: Amazon is subject to evolving regulations across various sectors, including e-commerce, digital content, data protection, and artificial intelligence. Changes in these regulations could increase compliance costs and limit operational flexibility. The company is regularly under review by regulatory authorities, which could lead to investigations and potential penalties.

2. **Antitrust Investigations**: Amazon is involved in multiple investigations related to competition and consumer protection laws. These include claims of price fixing, monopolization, and other anticompetitive practices. The outcomes of these investigations could result in significant fines, operational changes, or restrictions on business practices.

3. **Tax Controversies**: The company is engaged in various tax disputes in multiple jurisdictions, including claims from foreign tax authorities that could result in substantial tax liabilities. For instance, the Indian tax authority has asserted that taxes apply to cloud services fees, which could lead to significant payments if the matter is resolved unfavorably.

4. **Intellectual Property Claims**: Amazon is facing lawsuits alleging infringement of patents related to its products and services. These claims could result in substantial damages or require changes to its business practices.

5. **Data Privacy and Security Risks**: The company is under scrutiny for its data handling practices, particularly concerning compliance with privacy laws like the EU General Data Protection Regulation. Any breaches or failures to comply could lead to fines and reputational damage.

6. **Product Liability**: Amazon is exposed to product liability claims for items sold through its platform, including those from third-party sellers. This could result in financial liabilities and impact customer trust.

These risks highlight the complex legal landscape in which Amazon operates, necessitating ongoing vigilance and adaptation to regulatory changes.
"""

ADVISOR_REPORT_V1 = """
# Amazon's Legal and Regulatory Risks in 2024

⚠️ The available documents do not provide specific details regarding significant legal and regulatory risks faced by Amazon in 2024. There are no mentions of legal challenges, regulatory compliance issues, or changes in legislation that could have impacted Amazon during this period.

To obtain a comprehensive analysis of Amazon's legal and regulatory risks in 2024, I recommend checking the following sources:

1. **SEC Filings**: Review Amazon's annual report (10-K) and quarterly reports (10-Q) filed with the Securities and Exchange Commission, which often detail legal proceedings and regulatory risks.
2. **News Articles**: Look for news coverage from reputable financial news outlets that may have reported on any significant legal issues or regulatory changes affecting Amazon in 2024.
3. **Industry Reports**: Consider industry analysis reports that focus on e-commerce and technology sectors, which may highlight regulatory trends and challenges faced by major players like Amazon.

If you have access to additional documents or sources that might contain this information, please share them for further analysis.
"""

ADVISOR_REPORT_V2 = """
# Amazon's Legal and Regulatory Risks in 2024

In 2024, Amazon faced several significant legal and regulatory risks that could impact its operations and financial performance. Here are the key areas of concern based on the provided document context:

## Legal Proceedings and Regulatory Scrutiny

1. **Ongoing Legal Challenges**: Amazon has been involved in various legal proceedings, including antitrust investigations and lawsuits related to its market practices. These challenges have drawn scrutiny from regulators in multiple jurisdictions, which could materially affect its business.

2. **Regulatory Compliance Issues**: The company has faced increasing regulatory compliance challenges, particularly concerning data privacy and consumer protection laws. As regulations evolve, Amazon must ensure that its practices align with new legal requirements to avoid potential fines and sanctions.

3. **Intellectual Property Disputes**: Amazon has also been involved in disputes over intellectual property rights, which could lead to costly litigation and impact its ability to innovate and expand its product offerings.

## Additional Risks

- **Competition**: The intense competition in the e-commerce and cloud computing sectors poses a significant risk. Amazon must continuously adapt to maintain its market position against rivals who may leverage legal challenges to gain an advantage.

- **Valuation Risks**: Ongoing legal issues could impact Amazon's valuation, particularly if they result in financial liabilities or affect investor confidence.

- **Supply Chain Risks**: Given Amazon's extensive logistics operations, any disruptions related to legal or regulatory challenges could impact its supply chain efficiency and customer satisfaction.

- **Margin Pressure**: Legal and regulatory challenges may lead to increased operational costs, which could pressure profit margins if not managed effectively.

- **Execution Risks**: The company faces risks associated with executing new initiatives amidst ongoing legal scrutiny, which could hinder its ability to innovate and respond to market demands.

## Financial Performance Overview

To provide context regarding Amazon's financial health amidst these risks, here is a comparison of its total revenue and operating income between 2023 and 2024:

| Year | Total Revenue (Billion $) | Operating Income (Billion $) |
| --- | --- | --- |
| 2023 | 575 | 36.9 |
| 2024 | 638 | 68.6 |

This data highlights a significant increase in both total revenue and operating income, indicating a strong financial position that may help mitigate some of the risks faced.

## Recommendations for Stakeholders

To navigate these risks effectively, stakeholders should consider the following actions:

1. **Monitor Legal Developments**: Stay informed about ongoing legal proceedings and regulatory changes that could impact Amazon's operations.

2. **Evaluate Compliance Strategies**: Assess and enhance compliance strategies to align with evolving regulations, particularly in data privacy and consumer protection.

3. **Analyze Competitive Landscape**: Regularly review the competitive landscape to identify potential threats and opportunities arising from legal challenges faced by competitors.

4. **Risk Management Framework**: Implement a robust risk management framework that addresses legal, regulatory, and operational risks to safeguard against potential impacts on the business.

By addressing these legal and regulatory risks proactively, Amazon can better position itself for sustainable growth and maintain its leadership in the market.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding the significant legal and regulatory risks Amazon faced in 2024. However, it lacks citations from the provided context documents and actionable content, which diminishes its overall quality.

## Query Satisfaction
The response effectively covers the key legal and regulatory risks Amazon faced in 2024, including:
1. Government regulation and compliance
2. Antitrust investigations
3. Tax controversies
4. Intellectual property claims
5. Data privacy and security risks
6. Product liability

These points align well with the user's query, indicating satisfactory coverage of the topic.

## Remaining Gaps
1. **Source Citations**: The response does not include citations from the context documents, which are essential for grounding the information provided.
2. **Actionable Content**: There are no recommendations or actionable insights for the user, which could enhance the utility of the response.
3. **Limitations or Caveats**: While the response mentions some risks, it could benefit from a clearer acknowledgment of the uncertainties associated with these risks.

## Recommendation
To improve the response:
1. Include citations from the relevant context documents to substantiate the claims made.
2. Add actionable content or recommendations for the user regarding how to navigate or respond to these risks.
3. Consider incorporating a brief discussion of the uncertainties or limitations related to the risks mentioned to provide a more comprehensive view.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a more comprehensive overview of Amazon's legal and regulatory risks in 2024 compared to the initial version. It addresses several significant risks and incorporates specific details from the context documents. However, one issue remains unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding the significant legal and regulatory risks Amazon faced in 2024. It covers various aspects, including ongoing legal challenges, regulatory compliance issues, and additional risks such as competition and valuation risks. The inclusion of financial performance data adds context to the discussion.

## Issues Resolution Status
Out of the three issues identified by the Critic:
- **Resolved**:
  - [Incorporate specific legal and regulatory risks from context documents.]
  - [Address missing risk topics: competition, valuation, supply chain, margin pressure, execution.]
  
- **Unresolved**:
  - [Strengthen recommendations with actionable insights based on available information.]

The report has successfully addressed two of the three issues identified by the Critic.

## Remaining Gaps
The remaining unresolved issue is:
- The recommendations section could be strengthened with more actionable insights based on the specific legal and regulatory risks discussed in the report.

## Recommendation
To enhance the report further, the advisor should:
1. Revise the recommendations section to include specific, actionable strategies that stakeholders can implement in light of the identified legal and regulatory risks. This could involve more detailed compliance strategies, risk management frameworks, or specific monitoring practices tailored to the risks mentioned. 

By addressing this remaining gap, the report will provide a more robust and actionable analysis for stakeholders.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_3/query_7
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |        0 |       85 |    +85 |
| Business Analysis    |    15%  |        0 |       70 |    +70 |
| Risk Assessment      |    15%  |        0 |       90 |    +90 |
| Actionable Advice    |    15%  |        0 |       80 |    +80 |
| Evidence Usage       |    10%  |        0 |       75 |    +75 |
| Completeness         |    10%  |        0 |       90 |    +90 |
| Query Satisfaction   |    10%  |        0 |       95 |    +95 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |     0.00 |    83.25 | +83.25 |
+----------------------+--------+----------+----------+--------+
  Improvement: +83.25 pts absolute  |  +0.0% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_3/query_7
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |        0 |        0 |       85 |     +0 |    +85 |    +85 |
| Business Analysis    |    15%  |        0 |        0 |       70 |     +0 |    +70 |    +70 |
| Risk Assessment      |    15%  |       85 |        0 |       90 |    -85 |    +90 |     +5 |
| Actionable Advice    |    15%  |        0 |        0 |       80 |     +0 |    +80 |    +80 |
| Evidence Usage       |    10%  |        0 |        0 |       75 |     +0 |    +75 |    +75 |
| Completeness         |    10%  |       60 |        0 |       90 |    -60 |    +90 |    +30 |
| Query Satisfaction   |    10%  |       90 |        0 |       95 |    -90 |    +95 |     +5 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    27.75 |     0.00 |    83.25 |    -27 |    +83 |    +55 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +55 pts absolute  |  +200.00% relative
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
                "v2_score": 85,
                "delta_v0_v1": 0,
                "delta_v1_v2": 85,
                "delta_v0_v2": 85,
                "weighted_v1": 0.0,
                "weighted_v2": 21.25
            },
            "business_analysis": {
                "label": "Business Analysis",
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
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 85,
                "weighted_v0": 12.75,
                "v1_score": 0,
                "v2_score": 90,
                "delta_v0_v1": -85,
                "delta_v1_v2": 90,
                "delta_v0_v2": 5,
                "weighted_v1": 0.0,
                "weighted_v2": 13.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 80,
                "delta_v0_v1": 0,
                "delta_v1_v2": 80,
                "delta_v0_v2": 80,
                "weighted_v1": 0.0,
                "weighted_v2": 12.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 0,
                "v2_score": 75,
                "delta_v0_v1": 0,
                "delta_v1_v2": 75,
                "delta_v0_v2": 75,
                "weighted_v1": 0.0,
                "weighted_v2": 7.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 60,
                "weighted_v0": 6.0,
                "v1_score": 0,
                "v2_score": 90,
                "delta_v0_v1": -60,
                "delta_v1_v2": 90,
                "delta_v0_v2": 30,
                "weighted_v1": 0.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "weighted_v0": 9.0,
                "v1_score": 0,
                "v2_score": 95,
                "delta_v0_v1": -90,
                "delta_v1_v2": 95,
                "delta_v0_v2": 5,
                "weighted_v1": 0.0,
                "weighted_v2": 9.5
            }
        },
        "overall_v0": 27.75,
        "overall_v1": 0.0,
        "overall_v2": 83.25,
        "improvement_v0_to_v1": -27.75,
        "improvement_v1_to_v2": 83.25,
        "improvement_v0_to_v2": 55.5,
        "improvement_pct_v0_to_v2": 200.0
    }
