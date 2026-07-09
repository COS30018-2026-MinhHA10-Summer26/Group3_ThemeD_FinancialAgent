"""
Mock inputs for testing the Critic Agent.

Auto-generated from critic run: mock_data_1.py.
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY

MOCK_ADVISOR_REPORT_V1 = """

# Tesla Financial Health and Future Outlook

## Preliminary Analysis

Tesla, Inc. operates in the automotive and energy sectors, focusing on electric vehicles (EVs) and renewable energy solutions. The company has established itself as a leader in EV technology, with significant investments in research and development (R&D) for battery technology, self-driving capabilities, and energy storage systems. 

### Business Model
Tesla's business model is centered around:
- **Electric Vehicles**: Manufacturing and selling a range of electric vehicles, including the Model S, Model 3, Model X, and Model Y.
- **Energy Generation and Storage**: Offering solar energy products and energy storage solutions like the Powerwall and Megapack.
- **Direct Sales Model**: Utilizing a direct-to-consumer sales approach, which allows for better control over customer experience and inventory management.

### Competitive Landscape
The automotive market is highly competitive, with traditional automakers and new entrants increasingly focusing on electric vehicles. Tesla competes not only with established brands but also with emerging companies in the EV space. The energy storage market is similarly competitive, with various players offering alternative solutions.

### Potential Risks
- **Regulatory Challenges**: Tesla faces various regulations regarding vehicle safety, emissions, and self-driving technology, which could impact its operations.
- **Supply Chain Vulnerabilities**: The company relies on a global supply chain for critical components, making it susceptible to disruptions.
- **Market Volatility**: The automotive industry is cyclical, and Tesla's sales may be affected by economic downturns or shifts in consumer preferences.

## Key Financial Metrics Comparison

### Financial Metrics Overview
Here are the key financial metrics for Tesla for the fiscal year 2022 compared to 2021:

| Metric | Tesla 2022 | Tesla 2021 | Change (Abs) | Change (%) |
| :--- | :---: | :---: | :---: | :---: |
| EBIT | 150,000,000.00 | 140,000,000.00 | +10,000,000.00 | +7.14% |
| Equity | 200,000,000.00 | 200,000,000.00 | +0.00 | +0.00% |
| Market Capitalization | 800,000,000.00 | 750,000,000.00 | +50,000,000.00 | +6.67% |
| Sales | 600,000,000.00 | 550,000,000.00 | +50,000,000.00 | +9.09% |
| Total Assets | 500,000,000.00 | 450,000,000.00 | +50,000,000.00 | +11.11% |
| Total Liabilities | 300,000,000.00 | 250,000,000.00 | +50,000,000.00 | +20.00% |

### Risk Assessment
The Altman Z-Score for Tesla indicates a score of **4.589**, placing it in the **Safe Zone (Low Bankruptcy Risk)**. Here are the key components of the Z-Score:

- **Working Capital to Assets**: 0.2
- **Retained Earnings to Assets**: 0.4
- **EBIT to Assets**: 0.3
- **Equity Market Value to Liabilities**: 2.67
- **Sales to Assets**: 1.2

Additionally, the liabilities to market capitalization ratio is **0.375**, indicating a healthy balance between debt and equity.

## Conclusion and Future Outlook
Tesla's financial health appears robust, with increasing sales, stable equity, and a strong market capitalization. The company is well-positioned to continue its leadership in the EV market and expand its energy solutions. However, it must navigate regulatory challenges and supply chain vulnerabilities to maintain its growth trajectory.

### Next Steps
Continue monitoring Tesla's financial performance and market conditions, especially in light of regulatory changes and competition in the EV and energy sectors.

"""

MOCK_CRITIC_FEEDBACK = {
    "passes": False,
    "issues": [
        "See revision_instructions for the full critique output."
    ],
    "revision_instructions": "## Overall Verdict\nThe advisor report provides a general overview of Tesla's financial health and future outlook, but it lacks actionable advice and sufficient evidence to support its claims. Additionally, there are several areas where the analysis could be strengthened to provide a more robust assessment.\n\n## Major Logic Gaps\n- The report states that Tesla's financial health appears robust but does not adequately explain the basis for this conclusion. The metrics presented are not sufficiently contextualized, making it difficult to assess their significance.\n- The competitive landscape section mentions competition but does not provide specific examples or data to illustrate how Tesla compares to its competitors, which weakens the analysis.\n\n## Unsupported or Weakly Supported Claims\n- The report claims Tesla is a leader in EV technology without providing specific evidence or metrics to substantiate this assertion.\n- The financial metrics comparison includes figures that appear to be inconsistent with the provided context documents, particularly regarding EBIT and equity values, which raises questions about their accuracy.\n\n## Missing Investor Risks\n- While the report mentions regulatory challenges and supply chain vulnerabilities, it fails to address other potential risks such as margin pressure and competition from new entrants in the EV market.\n- The report does not discuss the impact of economic downturns on consumer preferences, which could significantly affect Tesla's sales.\n\n## Figure and Visualization Issues\n- The report does not include any figures or visualizations to support its analysis, which could enhance understanding and provide a clearer picture of Tesla's financial health.\n\n## Competitor Counterarguments\n- A serious competitor could argue that Tesla's reliance on a single-source supplier for key components poses a significant risk, especially in light of recent supply chain disruptions.\n- The report does not adequately address how Tesla's pricing strategy compares to competitors, which could impact its market share and profitability.\n\n## Revision Priorities\n1. Provide actionable advice based on the analysis, outlining specific steps Tesla should take to mitigate risks and capitalize on opportunities.\n2. Include evidence or citations to support claims made about Tesla's market position and financial health.\n3. Expand the risk assessment to include additional risks such as margin pressure and competition.\n4. Improve the competitive landscape analysis by providing specific examples and data on competitors.\n5. Consider adding figures or visualizations to enhance the report's clarity and impact.\n\n## Issues to Resolve\n- [ ] Provide actionable advice for Tesla's future strategy.\n- [ ] Include evidence or citations to support claims about Tesla's market position.\n- [ ] Expand the risk assessment to cover margin pressure and competition.\n- [ ] Enhance the competitive landscape analysis with specific examples.\n- [ ] Add figures or visualizations to support the financial analysis."
}
