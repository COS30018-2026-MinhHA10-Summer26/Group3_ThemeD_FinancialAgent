"""
RAG vs Pipeline Metrics -- document_5 / query_3
Query: What were the key financial ratios and margins for Tesla in 2022?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the key financial ratios and margins for Tesla in 2022?"

RAG_RESPONSE = "\nIn 2022, Tesla's key financial ratios and margins were as follows:\n\n1. **Gross Margin**:\n   - Total automotive gross margin decreased from 29.3% in 2021 to **28.5%** in 2022.\n   - Gross margin for the total automotive and services segment decreased from 26.9% in 2021 to **26.5%** in 2022.\n\n2. **Selling, General and Administrative (SG&A) Expenses**:\n   - SG&A expenses were **$3,946 million**, which represented **5%** of total revenues, down from **8%** in 2021.\n\n3. **Net Income**:\n   - Tesla reported a net income of **$12,556 million** for 2022.\n\n4. **Revenue**:\n   - Total revenues for Tesla in 2022 were **$81,462 million**, an increase from **$53,823 million** in 2021.\n\nThese figures indicate a solid financial performance for Tesla in 2022, despite a slight decrease in gross margins.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_5/query_3
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       90 |       90 |       90 |      +0 |      +0 |
| Business Analysis    |    15% |       30 |       70 |       75 |     +40 |      +5 |
| Risk Assessment      |    15% |       20 |       20 |       50 |      +0 |     +30 |
| Actionable Advice    |    15% |       10 |       60 |       60 |     +50 |      +0 |
| Evidence Usage       |    10% |       50 |       70 |       80 |     +20 |     +10 |
| Completeness         |    10% |       70 |       90 |       90 |     +20 |      +0 |
| Query Satisfaction   |    10% |       90 |      100 |      100 |     +10 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    52.50 |    71.00 |    77.25 |   +18.5 |   +6.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +18.5 pts  |  +35.24%
  V2 vs V1: +6.25 pts  |  +8.80%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 90,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 22.5,
                "weighted_v1": 22.5,
                "weighted_v2": 22.5
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 30,
                "v1_score": 70,
                "v2_score": 75,
                "delta_v1_v0": 40,
                "delta_v2_v1": 5,
                "weighted_v0": 4.5,
                "weighted_v1": 10.5,
                "weighted_v2": 11.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 20,
                "v1_score": 20,
                "v2_score": 50,
                "delta_v1_v0": 0,
                "delta_v2_v1": 30,
                "weighted_v0": 3.0,
                "weighted_v1": 3.0,
                "weighted_v2": 7.5
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 10,
                "v1_score": 60,
                "v2_score": 60,
                "delta_v1_v0": 50,
                "delta_v2_v1": 0,
                "weighted_v0": 1.5,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 50,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 20,
                "delta_v2_v1": 10,
                "weighted_v0": 5.0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 7.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 10,
                "delta_v2_v1": 0,
                "weighted_v0": 9.0,
                "weighted_v1": 10.0,
                "weighted_v2": 10.0
            }
        },
        "overall_v0": 52.5,
        "overall_v1": 71.0,
        "overall_v2": 77.25,
        "v1_vs_v0_abs": 18.5,
        "v1_vs_v0_pct": 35.24,
        "v2_vs_v1_abs": 6.25,
        "v2_vs_v1_pct": 8.8
    }
