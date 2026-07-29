"""
Mock inputs for testing the Evaluator Agent (with weighted metrics).

Auto-generated from evaluator run: mock_data_7.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """


# Tesla's Financial Health and Future Outlook

## Financial Health Assessment

Based on the analysis of Tesla's financial metrics for 2022, the company demonstrates a strong financial position with a favorable outlook. Here are the key findings:

### Altman Z-Score Analysis
- **Z-Score**: 12.88
- **Zone**: Safe Zone (Low Bankruptcy Risk)

The Altman Z-Score indicates that Tesla is in a safe zone with a low risk of bankruptcy. This score is derived from the following ratios:
- **Working Capital to Assets**: 32.63%
- **Retained Earnings to Assets**: 17.65%
- **EBIT to Assets**: 18.47%
- **Market Capitalization to Liabilities**: 17.39
- **Sales to Assets**: 119.79%

### Key Financial Metrics Comparison (2022 vs 2021)

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|-------------|-------------|--------------|-------------|
| Capital Expenditures       | $7,160M     | $6,480M     | +$680M       | +10.49%     |
| Cash and Cash Equivalents  | $22,190M    | $17,741M    | +$4,449M     | +25.08%     |
| Net Income                 | $12,560M    | $5,252M     | +$7,308M     | +139.15%    |
| Revenue                    | $81,460M    | $54,896M    | +$26,564M    | +48.39%     |

### Key Observations
- **Revenue Growth**: Tesla's revenue increased significantly by 48.39%, reflecting strong demand for its electric vehicles and energy products.
- **Net Income Surge**: The net income rose by 139.15%, indicating improved profitability and operational efficiency.
- **Cash Reserves**: The cash and cash equivalents increased by 25.08%, providing a solid liquidity position to fund future growth initiatives.
- **Capital Expenditures**: Increased capital expenditures by 10.49% suggest ongoing investments in production capacity and technology development.

## Future Outlook

Tesla's future outlook appears promising, driven by several factors:
1. **Production Capacity Expansion**: The company is ramping up production capabilities at its Gigafactories, which will support increased vehicle deliveries and energy product deployments.
2. **Technological Advancements**: Continued focus on battery technology and AI-driven features (like Full Self-Driving) is expected to enhance product offerings and competitiveness.
3. **Market Demand**: The ongoing shift towards electrification in the automotive sector and increasing environmental awareness will likely sustain demand for Tesla's products.
4. **Global Expansion**: New factories in strategic locations will help mitigate supply chain issues and improve delivery efficiency.

However, Tesla must navigate challenges such as inflationary pressures, rising interest rates, and potential supply chain disruptions. The cyclical nature of the automotive industry also poses risks that could affect sales volatility.

![Key Financial Metrics Comparison: Tesla 2022 vs 2021](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_35749045fc9f)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*  
*Source: Data sourced from Tesla's 2022 financial statements.*

## Actionable Recommendations
- **Invest in Technology**: Continue investing in battery technology and AI features to maintain a competitive edge.
- **Expand Production**: Focus on ramping up production at new Gigafactories to meet growing demand.
- **Monitor Economic Factors**: Keep a close eye on inflation and interest rates, adjusting pricing strategies as necessary to maintain sales momentum.
- **Enhance Supply Chain Resilience**: Develop strategies to mitigate supply chain disruptions, including diversifying suppliers and increasing local sourcing.

## Conclusion

Tesla's financial health is robust, with strong revenue growth, improved profitability, and a solid cash position. The company's strategic investments and focus on innovation position it well for future growth, despite the inherent risks in the automotive sector.


"""

MOCK_ADVISOR_REPORT_V2 = """

# Tesla's Financial Health and Future Outlook

## Financial Health Assessment

Based on the analysis of Tesla's financial metrics for 2022, the company demonstrates a strong financial position with a favorable outlook. Here are the key findings:

### Altman Z-Score Analysis
- **Z-Score**: 8.37
- **Zone**: Safe Zone (Low Bankruptcy Risk)

The Altman Z-Score indicates that Tesla is in a safe zone with a low risk of bankruptcy. This score is derived from the following ratios:
- **Working Capital to Assets**: 17.26%
- **Retained Earnings to Assets**: 15.65%
- **EBIT to Assets**: 16.59%
- **Market Capitalization to Liabilities**: 10.68
- **Sales to Assets**: 98.94%

### Key Financial Metrics Comparison (2022 vs 2021)

| Metric                     | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%)  |
|----------------------------|-------------|-------------|--------------|-------------|
| Capital Expenditures       | $7,160M     | $6,480M     | +$680M       | +10.49%     |
| Cash and Cash Equivalents  | $22,190M    | $17,741M    | +$4,449M     | +25.08%     |
| Net Income                 | $12,560M    | $5,252M     | +$7,308M     | +139.15%    |
| Revenue                    | $81,460M    | $54,896M    | +$26,564M    | +48.39%    |

### Key Observations
- **Revenue Growth**: Tesla's revenue increased significantly by 48.39%, reflecting strong demand for its electric vehicles and energy products. This growth is supported by the increasing shift towards electrification in the automotive sector.
- **Net Income Surge**: The net income rose by 139.15%, indicating improved profitability and operational efficiency.
- **Cash Reserves**: The cash and cash equivalents increased by 25.08%, providing a solid liquidity position to fund future growth initiatives.
- **Capital Expenditures**: Increased capital expenditures by 10.49% suggest ongoing investments in production capacity and technology development.

## Future Outlook

Tesla's future outlook appears promising, driven by several factors:
1. **Production Capacity Expansion**: The company is ramping up production capabilities at its Gigafactories, which will support increased vehicle deliveries and energy product deployments.
2. **Technological Advancements**: Continued focus on battery technology and AI-driven features (like Full Self-Driving) is expected to enhance product offerings and competitiveness.
3. **Market Demand**: The ongoing shift towards electrification in the automotive sector and increasing environmental awareness will likely sustain demand for Tesla's products.
4. **Global Expansion**: New factories in strategic locations will help mitigate supply chain issues and improve delivery efficiency.

However, Tesla must navigate challenges such as inflationary pressures, rising interest rates, and potential supply chain disruptions. The cyclical nature of the automotive industry also poses risks that could affect sales volatility.

### Risks to Consider
- **Regulatory Risks**: Evolving automotive regulations and environmental policies could impact Tesla's operations and profitability.
- **Competition**: The increasing number of players in the electric vehicle market may exert pressure on Tesla's market share and pricing strategies.
- **Supply Chain Vulnerabilities**: Tesla's reliance on a few key suppliers for raw materials poses a significant risk, especially in light of potential supply chain disruptions.

![Key Financial Metrics Comparison: Tesla 2022 vs 2021](https://breifexaedmnpwlgtgpr.supabase.co/storage/v1/object/public/Financial-agent/advisor_figure/fig_35749045fc9f)

*Figure: Comparison of key financial metrics for Tesla in 2022 and 2021.*  
*Source: Data sourced from Tesla's 2022 financial statements.*

## Actionable Recommendations
- **Invest in Technology**: Continue investing in battery technology and AI features to maintain a competitive edge.
- **Expand Production**: Focus on ramping up production at new Gigafactories to meet growing demand.
- **Monitor Economic Factors**: Keep a close eye on inflation and interest rates, adjusting pricing strategies as necessary to maintain sales momentum.
- **Enhance Supply Chain Resilience**: Develop strategies to mitigate supply chain disruptions, including diversifying suppliers and increasing local sourcing.

## Conclusion

Tesla's financial health is robust, with strong revenue growth, improved profitability, and a solid cash position. The company's strategic investments and focus on innovation position it well for future growth, despite the inherent risks in the automotive sector.

"""

MOCK_EVALUATION_REPORT = """
## Evaluation Verdict
The revised advisor report (v2) provides a comprehensive overview of Tesla's financial health and future outlook. It addresses several of the issues raised by the Critic but leaves one critical issue unresolved.

## Query Satisfaction
The revised report adequately answers the original user query regarding Tesla's financial health and future outlook. It covers key financial metrics, provides an analysis of the Altman Z-Score, discusses future growth prospects, and includes actionable recommendations. Additionally, it addresses risks associated with regulatory changes and competition, which were not present in the original report.

## Issues Resolution Status
Out of the five issues identified by the Critic:
- **Resolved Issues**:
  1. Provided context for the Altman Z-Score and its components.
  2. Included evidence to support claims of strong demand for Tesla's products.
  3. Addressed regulatory risks in the report.
  4. Discussed competition as a potential risk factor.

- **Unresolved Issue**:
  1. Fix the figure's image URL and ensure proper citation for the data.

## Remaining Gaps
The following issue remains unresolved:
- **Fix the figure's image URL and ensure proper citation for the data.** This is critical for ensuring the credibility and accessibility of the report.

## Recommendation
It is recommended that the advisor address the unresolved issue regarding the figure's image URL and citation. Once this is rectified, the report will be complete and ready for final approval.

## Estimated Improvement (Weighted Metrics)
```
==============================================================
  Weighted Metrics — mock_data_7.py
==============================================================
+----------------------+--------+----------+----------+--------+
| Criterion            | Weight | V1 Score | V2 Score |  Delta |
+----------------------+--------+----------+----------+--------+
| Financial Accuracy   |    25%  |       90 |       80 |    -10 |
| Business Analysis    |    15%  |       70 |       75 |     +5 |
| Risk Assessment      |    15%  |       70 |       80 |    +10 |
| Actionable Advice    |    15%  |       80 |       85 |     +5 |
| Evidence Usage       |    10%  |       80 |       80 |     +0 |
| Completeness         |    10%  |       90 |       90 |     +0 |
| Query Satisfaction   |    10%  |       90 |       90 |     +0 |
+----------------------+--------+----------+----------+--------+
| OVERALL (weighted)   |        |    81.50 |    82.00 |   +0.5 |
+----------------------+--------+----------+----------+--------+
  Improvement: +0.5 pts absolute  |  +0.61% relative
==============================================================
```
"""

MOCK_METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v1_score": 90,
                "v2_score": 80,
                "delta": -10,
                "weighted_v1": 22.5,
                "weighted_v2": 20.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v1_score": 70,
                "v2_score": 75,
                "delta": 5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
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
                "v1_score": 80,
                "v2_score": 85,
                "delta": 5,
                "weighted_v1": 12.0,
                "weighted_v2": 12.75
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
        "overall_v1": 81.5,
        "overall_v2": 82.0,
        "absolute_improvement": 0.5,
        "improvement_percentage": 0.61
    }
