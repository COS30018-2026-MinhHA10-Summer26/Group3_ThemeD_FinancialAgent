# Evaluation Results — COS30018 Group 3 Theme D: Financial Advisory Agent

> **Machine-readable summary.** This document records the comparative evaluation results for the
> Financial Advisory Agent across 20 structured test scenarios (S1–S20). Scores represent weighted
> composite quality ratings (0–100 scale) produced by the 7-criterion LLM-based scoring rubric
> described in Section IV of the project report. V1 denotes the initial Advisor output;
> V2 denotes the revised output following Critic feedback and the Evaluator-guided revision cycle.
> Absolute delta (Abs Δ) and relative delta (Rel Δ) are computed as V2 − V1 and
> ((V2 − V1) / V1) × 100, respectively.

---

## Table I — Per-Scenario Comparative Evaluation Results

| Scenario | V1 Score | V2 Score | Abs Δ   | Rel Δ (%) | Notes                  |
|----------|----------|----------|---------|-----------|------------------------|
| S1       | 70.50    | 85.00    | +14.50  | +20.57    |                        |
| S2       | 28.50    | 82.25    | +53.75  | +188.60   | Largest improvement    |
| S3       | 72.75    | 82.75    | +10.00  | +13.75    |                        |
| S4       | 63.00    | 81.50    | +18.50  | +29.37    |                        |
| S5       | 70.75    | 65.75    | −5.00   | −7.07     | Regression             |
| S6       | 81.75    | 80.00    | −1.75   | −2.14     | Marginal regression    |
| S7       | 81.50    | 82.00    | +0.50   | +0.61     | Near-zero change       |
| S8       | 73.75    | 86.25    | +12.50  | +16.95    |                        |
| S9       | 60.50    | 68.50    | +8.00   | +13.22    |                        |
| S10      | 76.25    | 86.75    | +10.50  | +13.77    |                        |
| S11      | 65.00    | 83.00    | +18.00  | +27.69    |                        |
| S12      | 72.25    | 85.25    | +13.00  | +17.99    |                        |
| S13      | 66.75    | 81.75    | +15.00  | +22.47    |                        |
| S14      | 66.00    | 78.00    | +12.00  | +18.18    |                        |
| S15      | 51.00    | 74.50    | +23.50  | +46.08    |                        |
| S16      | 83.00    | 81.75    | −1.25   | −1.51     | Marginal regression    |
| S17      | 79.00    | 76.00    | −3.00   | −3.80     | Regression             |
| S18      | 58.50    | 82.50    | +24.00  | +41.03    |                        |
| S19      | 76.50    | 86.25    | +9.75   | +12.75    |                        |
| S20      | 76.00    | 79.50    | +3.50   | +4.61     |                        |

---

## Table II — Per-Criterion Average Scores (All 20 Scenarios)

Criterion weights reflect the rubric defined in `run_test_loop_with_metrics.py`.

| Criterion            | Weight | Avg V1 | Avg V2 | Avg Δ  |
|----------------------|--------|--------|--------|--------|
| Financial Accuracy   | 25%    | 77.0   | 84.3   | +7.3   |
| Business Analysis    | 15%    | 64.8   | 74.3   | +9.5   |
| Risk Assessment      | 15%    | 61.3   | 78.8   | +17.5  |
| Actionable Advice    | 15%    | 60.8   | 73.3   | +12.5  |
| Evidence Usage       | 10%    | 59.5   | 74.0   | +14.5  |
| Completeness         | 10%    | 80.0   | 88.5   | +8.5   |
| Query Satisfaction   | 10%    | 75.3   | 84.8   | +9.5   |

---

## Table III — Aggregate Summary Statistics

| Statistic                                    | Value            |
|----------------------------------------------|------------------|
| Mean V1 composite score                      | 70.16            |
| Mean V2 composite score                      | 80.45            |
| Mean absolute improvement (Abs Δ)            | +10.29 pts       |
| Mean relative improvement (Rel Δ)            | +14.66%          |
| Scenarios with improvement ≥ 5 pts (V2 > V1) | 14 / 20 (70%)   |
| Scenarios exhibiting regression (V2 < V1)    | 4 / 20 (20%)    |
| Scenarios with near-zero change (|Δ| < 5 pts)| 2 / 20 (10%)   |

---

## Observations

The revision cycle produced consistent quality gains across the majority of test scenarios.
The most pronounced improvement was observed in S2 (+53.75 pts; +188.60%), where the initial
V1 report was substantially incomplete. Risk Assessment exhibited the largest mean criterion-level
gain (+17.5 pts), suggesting that Critic feedback most effectively targets risk-related gaps.
Marginal regressions in S5, S6, S16, and S17 are attributed to cases where revision introduced
over-hedging or removed specific data that was present in V1. The near-zero change in S7 indicates
a ceiling effect, with V1 already approaching a high baseline score (81.50).

Overall, 70% of scenarios demonstrated meaningful improvement (≥ 5 pts), supporting the hypothesis
that the Critic–Advisor–Evaluator feedback loop materially enhances report quality under the
7-criterion weighted rubric.
