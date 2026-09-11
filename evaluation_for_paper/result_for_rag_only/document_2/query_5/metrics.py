"""
RAG vs Pipeline Metrics -- document_2 / query_5
Query: What were the key balance sheet highlights for Amazon at the end of 2023?
"""
from __future__ import annotations
import json

USER_QUERY = "What were the key balance sheet highlights for Amazon at the end of 2023?"

RAG_RESPONSE = "\nAt the end of 2023, Amazon's key balance sheet highlights included:\n\n1. **Total Assets**: Amazon's total assets increased from $462.7 billion in 2022 to $527.9 billion in 2023.\n\n2. **Cash and Cash Equivalents**: The company reported cash and cash equivalents of $73.4 billion, up from $53.9 billion in the previous year.\n\n3. **Marketable Securities**: Marketable securities decreased slightly from $16.1 billion in 2022 to $13.4 billion in 2023.\n\n4. **Inventories**: Inventories were reported at $33.3 billion, a slight decrease from $34.4 billion in 2022.\n\n5. **Accounts Receivable**: Accounts receivable increased from $42.4 billion in 2022 to $52.3 billion in 2023.\n\n6. **Total Liabilities**: Total liabilities rose from $316.6 billion in 2022 to $326.5 billion in 2023.\n\n7. **Long-term Debt**: Long-term debt decreased from $67.2 billion in 2022 to $58.3 billion in 2023.\n\n8. **Stockholders' Equity**: Stockholders' equity increased significantly from $146.0 billion in 2022 to $201.9 billion in 2023.\n\nThese figures reflect Amazon's strong financial position and growth in various areas, particularly in cash and accounts receivable.\n"

# -------------------------------------------------------------------
# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)
#   >> EDIT the V0 / V1 / V2 columns in the table below, then run:
#   >> python3 recalc_metrics.py <this_file>  to recalculate OVERALL
# -------------------------------------------------------------------
METRICS_TABLE = """

==================================================================================
  RAG vs Pipeline Metrics -- document_2/query_5
  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised
==================================================================================
+----------------------+--------+----------+----------+----------+---------+---------+
| Criterion            | Weight | V0 (RAG) |  V1 Adv. |  V2 Rev. |  dV1-V0 | dV2-dV1 |
+----------------------+--------+----------+----------+----------+---------+---------+
| Financial Accuracy   |    25% |       95 |       80 |       80 |     -15 |      +0 |
| Business Analysis    |    15% |       20 |       50 |       60 |     +30 |     +10 |
| Risk Assessment      |    15% |       10 |       40 |       60 |     +30 |     +20 |
| Actionable Advice    |    15% |       10 |        0 |        0 |     -10 |      +0 |
| Evidence Usage       |    10% |       15 |       70 |       70 |     +55 |      +0 |
| Completeness         |    10% |       70 |       70 |       80 |      +0 |     +10 |
| Query Satisfaction   |    10% |       90 |       50 |       60 |     -40 |     +10 |
+----------------------+--------+----------+----------+----------+---------+---------+
| OVERALL (weighted)   |        |    47.25 |    52.50 |    59.00 |   +5.25 |    +6.5 |
+----------------------+--------+----------+----------+----------+---------+---------+
  V1 vs V0: +5.25 pts  |  +11.11%
  V2 vs V1: +6.5 pts  |  +12.38%
==================================================================================

"""

# Raw metrics dict (auto-generated from METRICS_TABLE — do not edit here)
METRICS = \
    {
        "criteria_detail": {
            "financial_accuracy": {
                "label": "Financial Accuracy",
                "weight_pct": 25,
                "v0_score": 95,
                "v1_score": 80,
                "v2_score": 80,
                "delta_v1_v0": -15,
                "delta_v2_v1": 0,
                "weighted_v0": 23.75,
                "weighted_v1": 20.0,
                "weighted_v2": 20.0
            },
            "business_analysis": {
                "label": "Business Analysis",
                "weight_pct": 15,
                "v0_score": 20,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": 30,
                "delta_v2_v1": 10,
                "weighted_v0": 3.0,
                "weighted_v1": 7.5,
                "weighted_v2": 9.0
            },
            "risk_assessment": {
                "label": "Risk Assessment",
                "weight_pct": 15,
                "v0_score": 10,
                "v1_score": 40,
                "v2_score": 60,
                "delta_v1_v0": 30,
                "delta_v2_v1": 20,
                "weighted_v0": 1.5,
                "weighted_v1": 6.0,
                "weighted_v2": 9.0
            },
            "actionable_advice": {
                "label": "Actionable Advice",
                "weight_pct": 15,
                "v0_score": 10,
                "v1_score": 0,
                "v2_score": 0,
                "delta_v1_v0": -10,
                "delta_v2_v1": 0,
                "weighted_v0": 1.5,
                "weighted_v1": 0.0,
                "weighted_v2": 0.0
            },
            "evidence_usage": {
                "label": "Evidence Usage",
                "weight_pct": 10,
                "v0_score": 15,
                "v1_score": 70,
                "v2_score": 70,
                "delta_v1_v0": 55,
                "delta_v2_v1": 0,
                "weighted_v0": 1.5,
                "weighted_v1": 7.0,
                "weighted_v2": 7.0
            },
            "completeness": {
                "label": "Completeness",
                "weight_pct": 10,
                "v0_score": 70,
                "v1_score": 70,
                "v2_score": 80,
                "delta_v1_v0": 0,
                "delta_v2_v1": 10,
                "weighted_v0": 7.0,
                "weighted_v1": 7.0,
                "weighted_v2": 8.0
            },
            "query_satisfaction": {
                "label": "Query Satisfaction",
                "weight_pct": 10,
                "v0_score": 90,
                "v1_score": 50,
                "v2_score": 60,
                "delta_v1_v0": -40,
                "delta_v2_v1": 10,
                "weighted_v0": 9.0,
                "weighted_v1": 5.0,
                "weighted_v2": 6.0
            }
        },
        "overall_v0": 47.25,
        "overall_v1": 52.5,
        "overall_v2": 59.0,
        "v1_vs_v0_abs": 5.25,
        "v1_vs_v0_pct": 11.11,
        "v2_vs_v1_abs": 6.5,
        "v2_vs_v1_pct": 12.38
    }
