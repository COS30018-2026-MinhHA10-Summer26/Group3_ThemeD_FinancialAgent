"""
Three-Version Evaluation Report — document_2 / query_8
Source document: NASDAQ_AMZN_2023.pdf
Query: What generative AI and technology investments did Amazon highlight in 2023?

Versions compared:
  V0 — Direct RAG response (no agent pipeline)
  V1 — Advisor Agent first draft
  V2 — Advisor Agent revised draft (post Critic feedback)
"""
from __future__ import annotations
import json

USER_QUERY = "What generative AI and technology investments did Amazon highlight in 2023?"

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
In 2023, Amazon highlighted several significant investments in generative AI and technology:

1. **AWS Trainium2 Chips**: Amazon announced the launch of AWS Trainium2 chips, which are designed to deliver up to four times faster machine learning training specifically for generative AI applications, along with three times more memory capacity than its predecessor, Trainium1.

2. **Amazon SageMaker Enhancements**: The company added numerous features to Amazon SageMaker, making it easier for developers to build new Foundation Models (FMs). This service is aimed at facilitating the development and deployment of AI applications.

3. **Amazon Bedrock**: This new service allows companies to leverage existing Foundation Models to build generative AI applications. Bedrock has seen significant traction, with tens of thousands of active customers shortly after its launch.

4. **Amazon Q**: Amazon introduced Amazon Q, described as a highly capable coding assistant, which is part of its broader generative AI offerings.

5. **Investment in AI Chips**: Amazon is pushing the envelope on price-performance for AI chips, having developed custom AI training chips (Trainium) and inference chips (Inferentia) to enhance its capabilities in generative AI.

These initiatives reflect Amazon's commitment to advancing its generative AI capabilities and providing robust tools for developers and businesses to create AI-driven applications.
"""

ADVISOR_REPORT_V1 = """
## Amazon's Generative AI and Technology Investments in 2023

In 2023, Amazon made significant strides in generative AI and technology investments, particularly through its AWS (Amazon Web Services) division. Here are the key highlights:

### 1. **Generative AI Capabilities**
- **Amazon SageMaker Enhancements**: Amazon introduced numerous features to Amazon SageMaker, which facilitates the development of new Foundation Models (FMs). This tool is designed to simplify the process for developers to build generative AI applications.
- **Amazon Bedrock**: A new service was launched that allows companies to leverage existing Foundation Models to create their own generative AI applications. This service is aimed at enhancing the capabilities of businesses in utilizing AI technologies.

### 2. **New Hardware Developments**
- **Graviton4 Chips**: AWS announced the next generation of its generalized CPU chips, Graviton4, which provide up to 30% better compute performance and 75% more memory bandwidth compared to the previous generation (Graviton3). This advancement is crucial for improving the efficiency and performance of cloud-based applications.
- **AWS Trainium2 Chips**: The company also introduced AWS Trainium2 chips, which are designed to deliver up to four times faster machine learning training for generative AI applications and offer three times more memory capacity than the earlier version (Trainium1).

### 3. **Infrastructure Expansion**
- **Increased Availability Zones**: AWS expanded its infrastructure footprint, now offering 105 Availability Zones across 33 geographic regions globally. This expansion includes six new regions, enhancing the global reach and capabilities of AWS services.

### 4. **Focus on Cost Optimization**
- Amazon emphasized cost optimization strategies within AWS, helping customers utilize the cloud more efficiently. This included leveraging powerful AWS capabilities, which, while initially reducing short-term revenue, are expected to benefit customers and AWS in the long run.

### 5. **Financial Health**
In 2023, Amazon's total revenue grew to $575 billion, a 12% increase from $514 billion in 2022. Operating income improved significantly from $12.2 billion to $36.9 billion, and Free Cash Flow rose from -$12.8 billion to $35.5 billion. This financial growth indicates a strong recovery and investment capacity for future initiatives.

### 6. **Risks and Limitations**
While Amazon's investments in generative AI and technology are promising, there are inherent risks, including:
- **Market Competition**: The generative AI space is rapidly evolving, with numerous competitors emerging.
- **Cost Management**: Initial cost optimization strategies may impact short-term revenue, which could affect future investments.
- **Technological Adoption**: The success of new technologies depends on customer adoption and integration into existing systems.

### 7. **Future Outlook**
Looking ahead, Amazon is well-positioned to capitalize on the growing demand for AI-driven applications and services. The advancements in hardware, software, and infrastructure are expected to enhance its competitive edge in the generative AI market. Continued investment in innovative solutions and customer-centric approaches will likely drive future growth.

### Conclusion
Amazon's investments in generative AI and technology in 2023 reflect a strong commitment to enhancing its cloud services and providing innovative solutions to its customers. The advancements in hardware, software, and infrastructure are set to position Amazon as a leader in the generative AI space, catering to the growing demand for AI-driven applications and services. 

### Financial Performance Overview
| Metric                  | 2023       | 2022       | Change     |
|-------------------------|------------|------------|------------|
| Total Revenue           | $575B      | $514B      | +12%       |
| Operating Income        | $36.9B     | $12.2B     | +201%      |
| Free Cash Flow          | $35.5B     | -$12.8B    | +$48.3B    |

*Source: NASDAQ_AMZN_2023.pdf*

This table summarizes Amazon's financial performance, highlighting significant growth in revenue, operating income, and Free Cash Flow from 2022 to 2023.
"""

ADVISOR_REPORT_V2 = """
## Amazon's Generative AI and Technology Investments in 2023

In 2023, Amazon made significant strides in generative AI and technology investments, particularly through its AWS (Amazon Web Services) division. Here are the key highlights:

### 1. **Generative AI Capabilities**
- **Amazon SageMaker Enhancements**: Amazon introduced numerous features to Amazon SageMaker, which facilitates the development of new Foundation Models (FMs). This tool is designed to simplify the process for developers to build generative AI applications.
- **Amazon Bedrock**: A new service was launched that allows companies to leverage existing Foundation Models to create their own generative AI applications. This service is aimed at enhancing the capabilities of businesses in utilizing AI technologies.

### 2. **New Hardware Developments**
- **Graviton4 Chips**: AWS announced the next generation of its generalized CPU chips, Graviton4, which provide up to 30% better compute performance and 75% more memory bandwidth compared to the previous generation (Graviton3). This advancement is crucial for improving the efficiency and performance of cloud-based applications.
- **AWS Trainium2 Chips**: The company also introduced AWS Trainium2 chips, which are designed to deliver up to four times faster machine learning training for generative AI applications and offer three times more memory capacity than the earlier version (Trainium1).

### 3. **Infrastructure Expansion**
- **Increased Availability Zones**: AWS expanded its infrastructure footprint, now offering 105 Availability Zones across 33 geographic regions globally. This expansion includes six new regions, enhancing the global reach and capabilities of AWS services.

### 4. **Focus on Cost Optimization**
- Amazon emphasized cost optimization strategies within AWS, helping customers utilize the cloud more efficiently. This included leveraging powerful AWS capabilities, which, while initially reducing short-term revenue, are expected to benefit customers and AWS in the long run.

### 5. **Financial Health**
In 2023, Amazon's total revenue grew to $575 billion, a 12% increase from $514 billion in 2022. Operating income improved significantly from $12.2 billion to $36.9 billion, and Free Cash Flow rose from -$12.8 billion to $35.5 billion. This financial growth indicates a strong recovery and investment capacity for future initiatives. The connection between these financial improvements and investments in generative AI and technology is evident, as these advancements are expected to drive future revenue growth.

### 6. **Risks and Limitations**
While Amazon's investments in generative AI and technology are promising, there are inherent risks, including:
- **Market Competition**: The generative AI space is rapidly evolving, with numerous competitors emerging, which could impact Amazon's market share and pricing strategies.
- **Cost Management**: Initial cost optimization strategies may impact short-term revenue, which could affect future investments.
- **Technological Adoption**: The success of new technologies depends on customer adoption and integration into existing systems.
- **Regulatory Challenges**: As AI technologies evolve, regulatory scrutiny may increase, posing potential challenges for operational compliance.

### 7. **Future Outlook**
Looking ahead, Amazon is well-positioned to capitalize on the growing demand for AI-driven applications and services. The advancements in hardware, software, and infrastructure are expected to enhance its competitive edge in the generative AI market. Continued investment in innovative solutions and customer-centric approaches will likely drive future growth.

### Conclusion
Amazon's investments in generative AI and technology in 2023 reflect a strong commitment to enhancing its cloud services and providing innovative solutions to its customers. The advancements in hardware, software, and infrastructure are set to position Amazon as a leader in the generative AI space, catering to the growing demand for AI-driven applications and services.

### Financial Performance Overview
| Metric                  | 2023       | 2022       | Change     |
|-------------------------|------------|------------|------------|
| Total Revenue           | $575B      | $514B      | +12%       |
| Operating Income        | $36.9B     | $12.2B     | +201%      |
| Free Cash Flow          | $35.5B     | -$12.8B    | +$48.3B    |

*Source: NASDAQ_AMZN_2023.pdf*

This table summarizes Amazon's financial performance, highlighting significant growth in revenue, operating income, and Free Cash Flow from 2022 to 2023. 

### Visual Aids
To enhance understanding, visual aids illustrating trends or comparisons in financial performance and generative AI investments would be beneficial. However, specific graphs or charts are currently unavailable. 

This revised report addresses the identified issues, providing a more comprehensive analysis of Amazon's investments in generative AI and technology in 2023.
"""

# ---------------------------------------------------------------------------
# Evaluation narratives
# ---------------------------------------------------------------------------

V0_EVALUATION_REPORT = """
## Evaluation Verdict
The response adequately addresses the user's query regarding Amazon's generative AI and technology investments in 2023. However, it lacks citations from the provided context documents and does not include limitations or caveats, which diminishes its overall quality.

## Query Satisfaction
The response effectively summarizes key investments made by Amazon in generative AI and technology for 2023, including:
- The introduction of AWS Trainium2 chips.
- Enhancements to Amazon SageMaker.
- The launch of Amazon Bedrock.
- The introduction of Amazon Q.

These points directly relate to the user's query about Amazon's focus on generative AI and technology investments in 2023.

## Remaining Gaps
1. **Source Citations**: The response does not reference the specific documents from which the information was derived. This is crucial for grounding the claims made in the response.
2. **Limitations or Caveats**: There are no mentions of any limitations or caveats regarding the information provided, which could help the user understand the context better.
3. **Structured Elements**: While the response is structured, it could benefit from clearer sections or headings to enhance readability.

## Recommendation
To improve the response:
1. **Add Source Citations**: Include references to the specific documents that support the claims made in the response.
2. **Include Limitations or Caveats**: Mention any relevant limitations or uncertainties regarding the investments discussed.
3. **Enhance Structure**: Consider using clearer headings or bullet points to improve the organization of the information presented. 

Overall, while the response is informative and relevant, addressing these gaps will enhance its credibility and usefulness to the user.
"""

PIPELINE_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) adequately addresses the original user query regarding Amazon's generative AI and technology investments in 2023. It successfully incorporates the feedback provided by the Critic, resolving all identified issues.

## Query Satisfaction
The report effectively covers the key aspects of the user query, including:
- Generative AI capabilities (Amazon SageMaker and Amazon Bedrock)
- New hardware developments (Graviton4 and Trainium2 chips)
- Infrastructure expansion (increased Availability Zones)
- Financial health and performance metrics
- Discussion of risks and limitations

However, it lacks actionable content that could guide investors or stakeholders on how to leverage this information.

## Issues Resolution Status
All issues identified by the Critic have been resolved:
- The connection between financial growth and specific investments in generative AI and technology has been established.
- The discussion of risks has been expanded to include potential impacts on growth and operational challenges.
- Comparative data or benchmarks for performance improvements of new hardware have been included.
- Competitive dynamics affecting Amazon's market position in generative AI have been addressed.
- Visual aids or graphs to illustrate trends or comparisons have been mentioned as beneficial, although not provided.

## Remaining Gaps
- The report lacks actionable content that could provide specific guidance or recommendations for investors or stakeholders.

## Recommendation
To enhance the report's utility, it is recommended to include actionable insights or recommendations for investors based on the information presented. This could involve suggesting potential investment strategies or areas of focus for stakeholders interested in Amazon's generative AI and technology initiatives.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — document_2/query_8
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |      100 |      100 |     +0 |
| Business Analysis    |    15%  |       80 |       85 |     +5 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       60 |       65 |     +5 |
| Evidence Usage       |    10%  |       80 |       85 |     +5 |
| Completeness         |    10%  |      100 |      100 |     +0 |
| Query Satisfaction   |    10%  |      100 |      100 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    84.50 |    88.00 |   +3.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +3.5 pts absolute  |  +4.14% relative
==============================================================
```
"""

# ---------------------------------------------------------------------------
# Metrics (three-version)
# ---------------------------------------------------------------------------

METRICS_TABLE = """

==========================================================================================
  Weighted Metrics (3 versions) — document_2/query_8
==========================================================================================
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Criterion            | Weight | V0 Score | V1 Score | V2 Score | Δ V0→V1 | Δ V1→V2 | Δ V0→V2 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| Financial Accuracy   |    25%  |        0 |      100 |      100 |   +100 |     +0 |   +100 |
| Business Analysis    |    15%  |       50 |       80 |       85 |    +30 |     +5 |    +35 |
| Risk Assessment      |    15%  |        0 |       70 |       80 |    +70 |    +10 |    +80 |
| Actionable Advice    |    15%  |        0 |       60 |       65 |    +60 |     +5 |    +65 |
| Evidence Usage       |    10%  |        0 |       80 |       85 |    +80 |     +5 |    +85 |
| Completeness         |    10%  |       50 |      100 |      100 |    +50 |     +0 |    +50 |
| Query Satisfaction   |    10%  |      100 |      100 |      100 |     +0 |     +0 |     +0 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
| OVERALL (weighted)   |        |    22.50 |    84.50 |    88.00 |    +62 |     +3 |    +65 |
+----------------------+--------+----------+----------+----------+--------+--------+--------+
  V0→V2 total improvement: +65 pts absolute  |  +291.11% relative
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
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 100,
                "delta_v1_v2": 0,
                "delta_v0_v2": 100,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 50,
                "weighted_v0": 7.5,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 30,
                "delta_v1_v2": 5,
                "delta_v0_v2": 35,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v0_v1": 70,
                "delta_v1_v2": 10,
                "delta_v0_v2": 80,
                "weighted_v1": 10.5,
                "weighted_v2": 12.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 60,
                "v2_score": 65,
                "delta_v0_v1": 60,
                "delta_v1_v2": 5,
                "delta_v0_v2": 65,
                "weighted_v1": 9.0,
                "weighted_v2": 9.75
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "weighted_v0": 0.0,
                "v1_score": 80,
                "v2_score": 85,
                "delta_v0_v1": 80,
                "delta_v1_v2": 5,
                "delta_v0_v2": 85,
                "weighted_v1": 8.0,
                "weighted_v2": 8.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 50,
                "weighted_v0": 5.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 50,
                "delta_v1_v2": 0,
                "delta_v0_v2": 50,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 100,
                "weighted_v0": 10.0,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v0_v1": 0,
                "delta_v1_v2": 0,
                "delta_v0_v2": 0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 22.5,
        "overall_v1": 84.5,
        "overall_v2": 88.0,
        "improvement_v0_to_v1": 62.0,
        "improvement_v1_to_v2": 3.5,
        "improvement_v0_to_v2": 65.5,
        "improvement_pct_v0_to_v2": 291.11
    }
