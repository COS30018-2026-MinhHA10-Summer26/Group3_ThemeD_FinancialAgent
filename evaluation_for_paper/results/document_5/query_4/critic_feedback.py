"""Critic Agent Feedback — document_5 / query_4"""
from __future__ import annotations

USER_QUERY = "How did Tesla's energy generation and storage segment perform in 2022?"

ADVISOR_REPORT_V1 = """
# Tesla's Energy Generation and Storage Segment Performance in 2022

Tesla's energy generation and storage segment is a crucial part of its mission to accelerate the world’s transition to sustainable energy. However, specific financial performance metrics such as revenue, net income, and market share for this segment in 2022 were not found in the available documents. This absence of data limits our ability to provide a comprehensive analysis of the segment's performance.

### Key Insights from Available Information

1. **Product Offerings**: Tesla markets and sells solar and energy storage products to a variety of customers, including residential, commercial, industrial, and utilities. The company emphasizes simplicity and accessibility to encourage the adoption of clean energy.

2. **Sales Channels**: The energy products are sold through multiple channels, including Tesla's website, stores, galleries, and a network of channel partners. This diversified approach aims to reduce customer acquisition costs.

3. **Service and Warranties**: Tesla provides service and repairs for its energy products, including warranties and performance guarantees. These warranties cover workmanship and defects, which can enhance customer trust and satisfaction.

### Financial Health and Future Outlook

Due to the lack of specific financial metrics, we cannot assess the financial health or future outlook of Tesla's energy generation and storage segment accurately. Understanding the revenue growth, profitability, and market share would be essential to gauge the segment's performance and potential risks.

### Risks and Limitations

- **Data Availability**: The absence of financial metrics limits our ability to provide a detailed analysis.
- **Market Competition**: The energy generation and storage market is competitive, and Tesla must continue to innovate and reduce costs to maintain its market position.

### Conclusion

For a more detailed analysis of Tesla's energy generation and storage segment performance in 2022, specific financial metrics are necessary. Unfortunately, these metrics are currently unavailable. If you have access to additional documents or reports that contain this information, please provide them for further insights.
"""

CRITIC_FEEDBACK = {
    "passes": False,
    "issues": ["See revision_instructions for the full critique output."],
    "revision_instructions": "## Overall Verdict\nThe advisor report on Tesla's energy generation and storage segment performance in 2022 lacks critical financial metrics and insights, which significantly limits its usefulness for decision-making. While it provides some context and general information, the absence of specific data undermines the report's credibility and comprehensiveness.\n\n## Major Logic Gaps\n- The report claims that specific financial performance metrics were not found, yet it fails to utilize available data from the context documents that detail revenue and growth figures for the energy generation and storage segment.\n- The conclusion suggests that additional documents are needed for a detailed analysis, which contradicts the potential insights that could be drawn from the existing context.\n\n## Unsupported or Weakly Supported Claims\n- The assertion that the absence of financial metrics limits the ability to assess financial health is misleading. The report could have referenced specific figures, such as the $3.909 billion in revenue for the energy generation and storage segment, which reflects a 40% increase from the previous year.\n- The claim regarding the competitive nature of the market is vague and lacks specific examples or data to substantiate the assertion.\n\n## Missing Investor Risks\n- The report does not address several visible risks from the context documents, including:\n  - **Supply Chain Risks**: The impact of supply chain disruptions on production and delivery is a significant concern that is not mentioned.\n  - **Regulatory Risks**: The evolving regulatory landscape for energy storage and generation is crucial for understanding potential challenges.\n  - **Execution Risks**: The report fails to discuss the risks associated with Tesla's ability to execute its growth strategy effectively.\n\n## Figure and Visualization Issues\n- There are no figures or visualizations included in the report, which could have enhanced the presentation of data and insights. The absence of visual aids limits the report's effectiveness in conveying complex information.\n\n## Competitor Counterarguments\n- Competitors could argue that Tesla's reliance on its brand and innovation may not be sufficient to maintain market share in a rapidly evolving energy sector. They might highlight their own advancements in energy storage and generation technologies as a threat to Tesla's position.\n\n## Revision Priorities\n1. Incorporate specific financial metrics from the context documents to provide a clearer picture of the segment's performance.\n2. Address the missing risks related to supply chain, regulation, and execution to present a more balanced view.\n3. Include visual aids or figures to support claims and enhance the report's clarity and impact.\n4. Strengthen competitive analysis by providing examples of competitors and their strategies.\n\n## Issues to Resolve\n- [ ] Include specific financial metrics such as revenue and growth figures for the energy generation and storage segment.\n- [ ] Address missing risks related to supply chain, regulation, and execution.\n- [ ] Add visual aids or figures to support claims and enhance clarity.\n- [ ] Strengthen competitive analysis with examples of competitors and their strategies."
}
