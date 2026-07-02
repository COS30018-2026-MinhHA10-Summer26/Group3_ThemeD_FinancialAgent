"""
Mock data for testing the Evaluator Agent in both Mode A (RAG-only) and
Mode B (full advisor/critic pipeline).
"""

from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY


# ---------------------------------------------------------------------------
# Mode A — RAG-only mock response
# ---------------------------------------------------------------------------

MOCK_RAG_RESPONSE = """\
Query: Please give some advice of Tesla's financial health and future outlook, \
based on the attached financial statements

Retrieval confidence: 0.72
Web augmentation used: no

Grounded findings:
1. [NASDAQ_TSLA_2022.pdf (Part II, Item 8)] Tesla reported total revenues of \
$81,462M and income from operations (EBIT) of $13,656M for FY 2022. Total \
assets stood at $82,338M against total liabilities of $36,440M, yielding a \
shareholders' equity of $45,898M.
2. [NASDAQ_TSLA_2022.pdf (Page 8 & 9)] Single-source supplier dependencies for \
key components pose supply chain disruption risks. The Inflation Reduction Act \
provides federal tax credits of up to $7,500 for eligible Tesla EV buyers.
3. [NASDAQ_TSLA_2022.pdf (Page 5 & 8)] Tesla operates Gigafactories globally \
(Austin, Fremont, Nevada, Shanghai, Berlin-Brandenburg), which helps mitigate \
transportation costs and tariff exposure.

Summary: The answer above is synthesized from the highest ranked retrieved context.
"""


# ---------------------------------------------------------------------------
# Mode B — Full pipeline mock data
# ---------------------------------------------------------------------------

# Critic report with '## Issues to Resolve' checklist
MOCK_CRITIC_REPORT = """\
## Overall Verdict
The advisor report provides a comprehensive overview of Tesla's financial health \
and future outlook. However, it contains several unsupported claims and lacks depth \
in risk assessment.

## Major Logic Gaps
- The Altman Z-Score of 8.367 is presented without context or explanation.
- The low debt-to-equity ratio is praised without industry comparison.

## Unsupported or Weakly Supported Claims
- Market capitalization claim lacks supporting trend data.

## Missing Investor Risks
- No mention of margin pressures from competition or rising raw material costs.

## Figure and Visualization Issues
- Report discusses a chart but does not embed a visual comparison figure.

## Competitor Counterarguments
- Competitors may argue Tesla's single-source supplier reliance is a major risk.

## Revision Priorities
1. Provide context for financial ratios.
2. Include a visual chart.
3. Expand risk assessment.

## Issues to Resolve
- [ ] Provide context for the Altman Z-Score and its relevance.
- [ ] Explain the debt-to-equity ratio in comparison to industry standards.
- [ ] Include a visual chart comparing key financial metrics.
- [ ] Address potential margin pressures from competition and rising costs.
- [ ] Strengthen evidence for market capitalization and investor confidence claims.
- [ ] Discuss challenges associated with diversifying the supply chain.
"""

# Revised advisor report v2 — intentionally fixes SOME but NOT ALL issues
# so the evaluator has something meaningful to flag.
MOCK_ADVISOR_REPORT_V2 = """\
# Tesla, Inc. Financial Health and Future Outlook (Revised)

## Key Financial Metrics (2022)

| Metric                           | Value       |
|----------------------------------|-------------|
| Total Revenues (Sales)          | $81,462M    |
| Income from Operations (EBIT)    | $13,656M    |
| Total Assets                     | $82,338M    |
| Total Liabilities                | $36,440M    |
| Retained Earnings                 | $12,885M    |
| Working Capital                   | $14,208M    |
| Market Capitalization             | $389,000M   |
| Total Debt                       | $5,748M     |
| Interest Expense                  | $191M       |

*Source: NASDAQ_TSLA_2022.pdf (Part II, Item 8) - Consolidated Balance Sheets & Operations*

## Financial Health Assessment

### 1. Risk Assessment

**Altman Z-Score: 8.367 (Safe Zone)**

The Altman Z-Score is a widely used financial model that predicts the probability \
of bankruptcy within two years. It combines five financial ratios weighted by \
coefficients derived from historical data. A score above 2.99 indicates a "Safe \
Zone" with low bankruptcy risk. Tesla's score of 8.367 places it well above this \
threshold, reflecting strong working capital, retained earnings, and high market \
capitalization relative to liabilities.

**Debt-to-Equity Ratio: 0.1252**

Tesla's debt-to-equity ratio of 0.1252 is significantly below the automotive \
industry average of approximately 1.0–1.5. This indicates Tesla relies far less \
on debt financing than typical automakers, reducing interest-rate sensitivity and \
financial leverage risk.

**Interest Coverage Ratio: 71.5**

This ratio indicates Tesla generates 71.5x its interest expense in operating \
earnings, demonstrating exceptional ability to service debt obligations.

### 2. Working Capital
- **Working Capital**: $14,208M — positive, indicating sufficient short-term \
liquidity to cover current obligations.

### 3. Market Capitalization
- **Market Capitalization**: $389,000M (approximately 3.16B shares at ~$123/share \
as of Dec 31, 2022). This valuation reflects strong investor confidence, though it \
should be noted that the stock declined approximately 65% during 2022, indicating \
significant market re-pricing of growth expectations.

## Future Outlook

Tesla's future outlook is shaped by several factors:

- **Battery Technology Leadership**: Proprietary 4680 cell manufacturing and \
vertical integration in battery production provide cost advantages.
- **Global Manufacturing Presence**: Six Gigafactories reduce logistics costs and \
tariff exposure.
- **Government Incentives**: The IRA provides up to $7,500 in federal tax credits \
for eligible EV purchases through 2032.

### Risks and Limitations

- **Supply Chain Vulnerabilities**: Dependency on single-source suppliers for key \
components (lithium, cobalt, nickel) poses disruption risks. Diversifying the \
supplier base would require significant investment in qualifying alternative \
suppliers and may temporarily increase costs during the transition period.
- **Market Competition**: Legacy automakers and new entrants are investing heavily; \
however, Tesla's technology moat in autonomous driving (FSD) and battery efficiency \
remains substantial.
- **Regulatory Changes**: Government policy shifts on EV incentives could affect demand.

### Actionable Advice
1. **Diversify Supply Chain**: Prioritize multi-sourcing for critical raw materials.
2. **Enhance Competitive Position**: Continue R&D investment in battery and FSD technology.
3. **Monitor Regulatory Environment**: Maintain flexibility for policy changes.

## Conclusion

Tesla demonstrates strong financial health with a high Altman Z-Score, low leverage, \
and exceptional interest coverage. While the company's market position is robust, \
addressing supply chain diversification challenges and monitoring competitive dynamics \
will be essential for sustained growth.

*Source: NASDAQ_TSLA_2022.pdf (Part II, Item 8)*
"""
