"""
RAG vs Pipeline Metrics -- document_6 / query_6
Query: What were the key balance sheet metrics for Tesla at the end of 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the key balance sheet metrics for Tesla at the end of 2023?"

RAG_RESPONSE = "\nAt the end of 2023, Tesla's key balance sheet metrics were as follows:\n\n- **Total Assets**: $106.62 billion\n- **Total Liabilities**: $43.01 billion\n- **Total Stockholders' Equity**: $62.63 billion\n- **Cash and Cash Equivalents**: $16.40 billion\n- **Short-term Investments**: $12.70 billion\n- **Accounts Receivable**: $12.70 billion\n- **Inventory**: $13.63 billion\n- **Accrued Liabilities**: $9.08 billion\n- **Debt and Finance Leases**: $4.68 billion\n\nThese figures reflect Tesla's financial position as of December 31, 2023, as detailed in their consolidated balance sheets and financial statements.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_6/query_6
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |      100 |      100 |      100 |      +0 |      +0 |
| Business Analysis    |    15% |        0 |       20 |       55 |     +20 |     +35 |
| Risk Assessment      |    15% |        0 |       20 |       60 |     +20 |     +40 |
| Actionable Advice    |    15% |        0 |       30 |       60 |     +30 |     +30 |
| Evidence Usage       |    10% |        0 |       50 |       55 |     +50 |      +5 |
| Completeness         |    10% |       30 |       50 |       50 |     +20 |      +0 |
| Query Satisfaction   |    10% |       30 |       90 |       90 |     +60 |      +0 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    31.00 |    54.50 |    70.75 |   +23.5 |  +16.25 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +23.5 pts  |  +75.81%
  V2 vs V1: +16.25 pts  |  +29.82%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 100,
                "v1_score": 100,
                "v2_score": 100,
                "delta_v1_v0": 0,
                "delta_v2_v1": 0,
                "weighted_v0": 25.0,
                "weighted_v1": 25.0,
                "weighted_v2": 25.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 20,
                "v2_score": 55,
                "delta_v1_v0": 20,
                "delta_v2_v1": 35,
                "weighted_v0": 0.0,
                "weighted_v1": 3.0,
                "weighted_v2": 8.25
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 20,
                "v2_score": 60,
                "delta_v1_v0": 20,
                "delta_v2_v1": 40,
                "weighted_v0": 0.0,
                "weighted_v1": 3.0,
                "weighted_v2": 9.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 0,
                "v1_score": 30,
                "v2_score": 60,
                "delta_v1_v0": 30,
                "delta_v2_v1": 30,
                "weighted_v0": 0.0,
                "weighted_v1": 4.5,
                "weighted_v2": 9.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 0,
                "v1_score": 50,
                "v2_score": 55,
                "delta_v1_v0": 50,
                "delta_v2_v1": 5,
                "weighted_v0": 0.0,
                "weighted_v1": 5.0,
                "weighted_v2": 5.5
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 30,
                "v1_score": 50,
                "v2_score": 50,
                "delta_v1_v0": 20,
                "delta_v2_v1": 0,
                "weighted_v0": 3.0,
                "weighted_v1": 5.0,
                "weighted_v2": 5.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 30,
                "v1_score": 90,
                "v2_score": 90,
                "delta_v1_v0": 60,
                "delta_v2_v1": 0,
                "weighted_v0": 3.0,
                "weighted_v1": 9.0,
                "weighted_v2": 9.0
            }
        },
        "overall_v0": 31.0,
        "overall_v1": 54.5,
        "overall_v2": 70.75,
        "v1_vs_v0_abs": 23.5,
        "v1_vs_v0_pct": 75.81,
        "v2_vs_v1_abs": 16.25,
        "v2_vs_v1_pct": 29.82
    }
