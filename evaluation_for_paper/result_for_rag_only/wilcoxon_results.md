## Wilcoxon Signed-Rank Test Results

> **H₀**: No difference between paired scores across 56 scenarios.
> Effect size *r* = |Z| / √N_nonzero  (small ≥ 0.1 · medium ≥ 0.3 · large ≥ 0.5)

### Overall Weighted Scores

| Comparison                   | N  | Mean (x → y)        |        W |       p |       Z |      r | Sig  |
|:-----------------------------|---:|:--------------------|---------:|--------:|--------:|-------:|:----:|
| V0 (RAG) vs V1 (Advisor)     | 50 |   52.97 →   72.74 |      0.0 |   < 0.0001 |  -6.154 |   0.87 |  *** |
| V0 (RAG) vs V2 (Revised)     | 50 |   52.97 →   80.17 |      0.0 |   < 0.0001 |  -6.154 |   0.87 |  *** |
| V1 (Advisor) vs V2 (Revised) | 50 |   72.74 →   80.17 |      0.0 |   < 0.0001 |  -6.031 |   0.87 |  *** |

### Per-Criterion (V1 Advisor vs V2 Revised, averaged across all scenarios)

| Comparison                   | N  | Mean (x → y)        |        W |       p |       Z |      r | Sig  |
|:-----------------------------|---:|:--------------------|---------:|--------:|--------:|-------:|:----:|
| Fin. Accuracy (V1→V2)        | 50 |   89.70 →   91.90 |      0.0 |     0.0273 |  -2.201 |  0.899 |    * |
| Biz. Analysis (V1→V2)        | 50 |   65.40 →   72.60 |      0.0 |   < 0.0001 |  -4.782 |  0.873 |  *** |
| Risk Assess. (V1→V2)         | 50 |   61.00 →   74.80 |      0.0 |   < 0.0001 |  -5.442 |  0.871 |  *** |
| Action. Advice (V1→V2)       | 50 |   53.90 →   66.40 |      0.0 |   < 0.0001 |  -5.086 |  0.872 |  *** |
| Evidence Usage (V1→V2)       | 50 |   63.20 →   72.50 |      0.0 |   < 0.0001 |  -4.372 |  0.874 |  *** |
| Completeness (V1→V2)         | 50 |   79.30 →   86.00 |      0.0 |   < 0.0001 |  -4.015 |  0.876 |  *** |
| Query Satisf. (V1→V2)        | 50 |   90.20 →   92.70 |      0.0 |     0.0012 |   -3.18 |  0.882 |   ** |

**Significance**: \*\*\* p<0.001 · \*\* p<0.01 · \* p<0.05 · ns = not significant
