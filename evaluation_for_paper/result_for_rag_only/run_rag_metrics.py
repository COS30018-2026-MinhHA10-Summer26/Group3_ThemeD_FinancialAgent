"""
RAG-only 7-criterion metric scorer.

For each document (document_1 .. document_7) and each query folder in
result_for_rag_only/, this script:

  1. Loads USER_QUERY + RAG_RESPONSE from report_v0.py  (RAG baseline → V0)
  2. Loads V1/V2 scores from results/document_X/query_Y/final_report.py
     (already computed by the full pipeline — FREE, no LLM call needed)
  3. Calls the LLM once to score RAG_RESPONSE on the 7 criteria   (V0 score)
  4. Writes metrics.py in the same folder as report_v0.py, containing:
       - METRICS dict (v0 + v1 + v2 for each criterion)
       - A formatted comparison table printed to stdout

Skip behaviour: if metrics.py already exists for a scenario, it is skipped.

Run from workspace root:
    python evaluation_for_paper/result_for_rag_only/run_rag_metrics.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import textwrap
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR   = Path(__file__).resolve().parent          # result_for_rag_only/
PAPER_DIR    = SCRIPT_DIR.parent                        # evaluation_for_paper/
PROJECT_ROOT = PAPER_DIR.parent                         # workspace root

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ---------------------------------------------------------------------------
# .env loading
# ---------------------------------------------------------------------------

from dotenv import load_dotenv  # noqa: E402

load_dotenv(dotenv_path=str(PROJECT_ROOT / "backend" / ".env"))
load_dotenv(dotenv_path=str(PROJECT_ROOT / ".env"))

# ---------------------------------------------------------------------------
# OpenAI client
# ---------------------------------------------------------------------------

import openai  # noqa: E402
from openai import OpenAI  # noqa: E402


def _get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found. Check backend/.env or .env")
    return OpenAI(api_key=api_key)


def _safe_chat_completion(client: OpenAI, **kwargs) -> Any:
    """Chat completion with retry on RateLimitError (429)."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(**kwargs)
        except openai.RateLimitError:
            if attempt == max_retries - 1:
                raise
            wait = (attempt + 1) * 4
            print(f"   [RagMetrics] RateLimitError. Retrying in {wait}s "
                  f"(attempt {attempt + 1}/{max_retries})...")
            time.sleep(wait)


# ---------------------------------------------------------------------------
# 7-criterion scoring rubric  (identical to run_pipeline.py)
# ---------------------------------------------------------------------------

CRITERIA: List[Dict[str, Any]] = [
    {
        "key": "financial_accuracy",
        "label": "Financial Accuracy",
        "weight": 0.25,
        "description": (
            "How accurately financial figures and calculations are reported. "
            "Check for correct numbers, valid formulas, and consistency between "
            "stated values (e.g., Z-Score components, revenue, liabilities)."
        ),
    },
    {
        "key": "business_analysis",
        "label": "Business Analysis",
        "weight": 0.15,
        "description": (
            "Quality of business model and competitive landscape analysis. "
            "Look for depth, named competitors, and specific industry context."
        ),
    },
    {
        "key": "risk_assessment",
        "label": "Risk Assessment",
        "weight": 0.15,
        "description": (
            "Depth and accuracy of risk identification and assessment. "
            "Covers market, regulatory, operational, and financial risks with specifics."
        ),
    },
    {
        "key": "actionable_advice",
        "label": "Actionable Advice",
        "weight": 0.15,
        "description": (
            "Presence and quality of concrete, actionable recommendations. "
            "Generic suggestions score low; prioritised, specific actions score high."
        ),
    },
    {
        "key": "evidence_usage",
        "label": "Evidence Usage",
        "weight": 0.10,
        "description": (
            "Use of citations, evidence, or data to support claims. "
            "Named sources, document references, or inline data citations raise the score."
        ),
    },
    {
        "key": "completeness",
        "label": "Completeness",
        "weight": 0.10,
        "description": (
            "Structural completeness -- all required report sections are present "
            "(financial overview, risk section, conclusion/outlook, actionable advice)."
        ),
    },
    {
        "key": "query_satisfaction",
        "label": "Query Satisfaction",
        "weight": 0.10,
        "description": (
            "How well the report answers the original user query. "
            "Does it address every sub-question raised by the user?"
        ),
    },
]

assert abs(sum(c["weight"] for c in CRITERIA) - 1.0) < 1e-9, \
    "Criterion weights must sum to 1.0"


# ---------------------------------------------------------------------------
# LLM scorer -- single response (V0 only)
# ---------------------------------------------------------------------------

def score_rag_response(
    client: OpenAI,
    model: str,
    query: str,
    rag_response: str,
    criteria: List[Dict[str, Any]],
) -> Dict[str, int]:
    """
    Ask the LLM to score the RAG response (V0) on every criterion.

    Returns:
        { "<criterion_key>": <score 0-100>, ... }
    """
    criteria_block = "\n".join(
        f"- **{c['key']}** ({int(c['weight'] * 100)}%): {c['description']}"
        for c in criteria
    )

    prompt = (
        "You are an objective financial-report quality scorer.\n\n"
        "USER QUERY:\n"
        f"{query}\n\n"
        "RAG RESPONSE (the response to score):\n"
        f"{rag_response}\n\n"
        "SCORING CRITERIA:\n"
        f"{criteria_block}\n\n"
        "TASK:\n"
        "Score the RAG RESPONSE on EACH criterion using an integer from 0 to 100.\n"
        "0 = completely absent/wrong, 100 = exemplary.\n\n"
        "Respond ONLY with a JSON object in this exact format (no prose, no markdown fence):\n"
        "{\n"
        '    "financial_accuracy": <int>,\n'
        '    "business_analysis":  <int>,\n'
        '    "risk_assessment":    <int>,\n'
        '    "actionable_advice":  <int>,\n'
        '    "evidence_usage":     <int>,\n'
        '    "completeness":       <int>,\n'
        '    "query_satisfaction": <int>\n'
        "}"
    )

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = _safe_chat_completion(
                client,
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
            )
            raw = response.choices[0].message.content.strip()

            # Strip accidental markdown fences
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()

            scores = json.loads(raw)

            # Validate + clamp
            for c in criteria:
                key = c["key"]
                if key not in scores:
                    raise ValueError(f"Missing criterion key in LLM response: {key}")
                val = scores[key]
                if not isinstance(val, (int, float)):
                    raise ValueError(f"Score for {key} is not numeric: {val}")
                scores[key] = max(0, min(100, int(val)))

            return scores

        except (json.JSONDecodeError, ValueError, KeyError) as exc:
            if attempt == max_retries - 1:
                print(f"   [RagMetrics] Failed to parse LLM scores after "
                      f"{max_retries} attempts: {exc}")
                return {c["key"]: 50 for c in criteria}
            wait = (attempt + 1) * 3
            print(f"   [RagMetrics] Parse error, retrying in {wait}s... ({exc})")
            time.sleep(wait)


# ---------------------------------------------------------------------------
# Metric computation
# ---------------------------------------------------------------------------

def compute_metrics(
    v0_scores: Dict[str, int],
    v1_scores: Dict[str, int],
    v2_scores: Dict[str, int],
    criteria: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Build the METRICS dict with per-criterion detail and overall weighted scores."""
    details: Dict[str, Any] = {}
    weighted_v0 = 0.0
    weighted_v1 = 0.0
    weighted_v2 = 0.0

    for c in criteria:
        key = c["key"]
        w = c["weight"]
        v0 = v0_scores[key]
        v1 = v1_scores.get(key, 0)
        v2 = v2_scores.get(key, 0)

        contrib_v0 = v0 * w
        contrib_v1 = v1 * w
        contrib_v2 = v2 * w
        weighted_v0 += contrib_v0
        weighted_v1 += contrib_v1
        weighted_v2 += contrib_v2

        details[key] = {
            "label": c["label"],
            "weight_pct": int(w * 100),
            "v0_score": v0,
            "v1_score": v1,
            "v2_score": v2,
            "delta_v1_v0": v1 - v0,
            "delta_v2_v1": v2 - v1,
            "weighted_v0": round(contrib_v0, 2),
            "weighted_v1": round(contrib_v1, 2),
            "weighted_v2": round(contrib_v2, 2),
        }

    overall_v0 = round(weighted_v0, 2)
    overall_v1 = round(weighted_v1, 2)
    overall_v2 = round(weighted_v2, 2)

    def _pct(new: float, base: float) -> float:
        return round(((new - base) / base) * 100, 2) if base != 0 else 0.0

    return {
        "criteria_detail": details,
        "overall_v0": overall_v0,
        "overall_v1": overall_v1,
        "overall_v2": overall_v2,
        "v1_vs_v0_abs": round(overall_v1 - overall_v0, 2),
        "v1_vs_v0_pct": _pct(overall_v1, overall_v0),
        "v2_vs_v1_abs": round(overall_v2 - overall_v1, 2),
        "v2_vs_v1_pct": _pct(overall_v2, overall_v1),
    }


# ---------------------------------------------------------------------------
# Table formatter
# ---------------------------------------------------------------------------

def format_metrics_table(metrics: Dict[str, Any], label: str) -> str:
    """Format the 7-column comparison table (V0 | V1 | V2) as a string."""
    details = metrics["criteria_detail"]

    col_widths = [22, 8, 10, 10, 10, 9, 9]  # label, weight, v0, v1, v2, dv1, dv2
    sep = "+" + "+".join("-" * w for w in col_widths) + "+"

    def _cell(val, width, is_label=False):
        s = str(val)
        if is_label:
            return f" {s:<{width - 2}} "
        return f" {s:>{width - 2}} "

    def _row(cells, label_col=0):
        parts = [_cell(cells[i], col_widths[i], is_label=(i == label_col))
                 for i in range(len(col_widths))]
        return "|" + "|".join(parts) + "|"

    def _d(n):
        return f"+{n}" if n >= 0 else str(n)

    lines = [
        "",
        "=" * 82,
        f"  RAG vs Pipeline Metrics -- {label}",
        "  Columns: V0 = RAG baseline | V1 = Advisor initial | V2 = Advisor revised",
        "=" * 82,
        sep,
        _row(["Criterion", "Weight", "V0 (RAG)", "V1 Adv.", "V2 Rev.", "dV1-V0", "dV2-dV1"]),
        sep,
    ]

    for key, d in details.items():
        lines.append(_row([
            d["label"],
            f"{d['weight_pct']}%",
            d["v0_score"],
            d["v1_score"],
            d["v2_score"],
            _d(d["delta_v1_v0"]),
            _d(d["delta_v2_v1"]),
        ]))

    lines.append(sep)
    lines.append(_row([
        "OVERALL (weighted)", "",
        f"{metrics['overall_v0']:.2f}",
        f"{metrics['overall_v1']:.2f}",
        f"{metrics['overall_v2']:.2f}",
        _d(metrics["v1_vs_v0_abs"]),
        _d(metrics["v2_vs_v1_abs"]),
    ]))
    lines.append(sep)
    lines += [
        f"  V1 vs V0: {_d(metrics['v1_vs_v0_abs'])} pts  |  {metrics['v1_vs_v0_pct']:+.2f}%",
        f"  V2 vs V1: {_d(metrics['v2_vs_v1_abs'])} pts  |  {metrics['v2_vs_v1_pct']:+.2f}%",
        "=" * 82,
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Module loader helpers
# ---------------------------------------------------------------------------

def _load_py_module(path: Path, module_name: str) -> Any:
    """Load an arbitrary .py file as a module."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_report_v0(path: Path, doc_idx: int, q_idx: int):
    """Return (USER_QUERY, RAG_RESPONSE) from a report_v0.py file."""
    m = _load_py_module(path, f"report_v0_d{doc_idx}_q{q_idx}")
    query    = getattr(m, "USER_QUERY",   "")
    response = getattr(m, "RAG_RESPONSE", "")
    return query, response


def load_final_report_metrics(path: Path, doc_idx: int, q_idx: int) -> Optional[Dict[str, Any]]:
    """
    Load METRICS from evaluation_for_paper/results/document_X/query_Y/final_report.py.
    Returns None if the file does not exist.
    """
    if not path.exists():
        return None
    m = _load_py_module(path, f"final_report_d{doc_idx}_q{q_idx}")
    return getattr(m, "METRICS", None)


# ---------------------------------------------------------------------------
# metrics.py writer
# ---------------------------------------------------------------------------

def write_metrics_py(
    out_path: Path,
    doc_index: int,
    query_index: int,
    user_query: str,
    rag_response: str,
    metrics: Dict[str, Any],
    table_str: str,
) -> None:
    """Write metrics.py alongside report_v0.py."""
    metrics_repr = json.dumps(metrics, indent=4, ensure_ascii=False)
    metrics_repr_indented = textwrap.indent(metrics_repr, "    ")

    content = (
        '"""\n'
        f"RAG vs Pipeline Metrics -- document_{doc_index} / query_{query_index}\n"
        f"Query: {user_query}\n"
        '"""\n'
        "from __future__ import annotations\n"
        "import json\n\n"
        f"USER_QUERY = {json.dumps(user_query, ensure_ascii=False)}\n\n"
        f"RAG_RESPONSE = {json.dumps(rag_response, ensure_ascii=False)}\n\n"
        "# -------------------------------------------------------------------\n"
        "# Comparison table: V0 (RAG baseline) | V1 (Advisor) | V2 (Revised)\n"
        "# -------------------------------------------------------------------\n"
        'METRICS_TABLE = """\n'
        f"{table_str}\n"
        '"""\n\n'
        "# Raw metrics dict\n"
        "METRICS = \\\n"
        f"{metrics_repr_indented}\n"
    )
    out_path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Single-scenario runner
# ---------------------------------------------------------------------------

def run_scenario(
    client: OpenAI,
    model: str,
    doc_index: int,
    query_index: int,
) -> None:
    label = f"document_{doc_index}/query_{query_index}"

    rag_dir       = SCRIPT_DIR / f"document_{doc_index}" / f"query_{query_index}"
    report_v0_path = rag_dir / "report_v0.py"
    out_path      = rag_dir / "metrics.py"

    if not report_v0_path.exists():
        print(f"  [SKIP] {label} -- report_v0.py not found")
        return

    if out_path.exists():
        print(f"  [SKIP] {label} -- metrics.py already exists")
        return

    # 1. Load V0 data
    user_query, rag_response = load_report_v0(report_v0_path, doc_index, query_index)
    if not user_query or not rag_response:
        print(f"  [WARN] {label} -- USER_QUERY or RAG_RESPONSE is empty, skipping")
        return

    # 2. Load V1/V2 scores from existing final_report.py (free, no LLM)
    final_report_path = (
        PAPER_DIR / "results"
        / f"document_{doc_index}"
        / f"query_{query_index}"
        / "final_report.py"
    )
    pipeline_metrics = load_final_report_metrics(final_report_path, doc_index, query_index)

    if pipeline_metrics is None:
        print(f"  [WARN] {label} -- final_report.py not found, V1/V2 = 0")
        v1_scores = {c["key"]: 0 for c in CRITERIA}
        v2_scores = {c["key"]: 0 for c in CRITERIA}
    else:
        cd = pipeline_metrics.get("criteria_detail", {})
        v1_scores = {key: cd[key]["v1_score"] for key in cd}
        v2_scores = {key: cd[key]["v2_score"] for key in cd}

    # 3. Score V0 (RAG response) via LLM
    print(f"\n  [Scoring V0] {label}")
    print(f"    Query: {user_query[:90]}{'...' if len(user_query) > 90 else ''}")
    v0_scores = score_rag_response(client, model, user_query, rag_response, CRITERIA)

    # 4. Compute combined metrics
    metrics = compute_metrics(v0_scores, v1_scores, v2_scores, CRITERIA)

    # 5. Format and print table
    table_str = format_metrics_table(metrics, label)
    print(table_str)

    # 6. Write metrics.py
    write_metrics_py(out_path, doc_index, query_index, user_query, rag_response, metrics, table_str)
    print(f"    Saved: {label}/metrics.py")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    model = "gpt-4o-mini"

    print("=" * 82)
    print("  RAG Metrics Scorer -- 7-criterion evaluation (V0 RAG vs V1/V2 Pipeline)")
    print(f"  Model: {model}")
    print("=" * 82)

    client = _get_client()

    doc_dirs = sorted(
        p for p in SCRIPT_DIR.iterdir()
        if p.is_dir() and p.name.startswith("document_")
    )

    if not doc_dirs:
        print("No document_* directories found under result_for_rag_only/")
        return

    total = 0
    skipped = 0
    errors = 0

    for doc_dir in doc_dirs:
        doc_index = int(doc_dir.name.split("_")[1])
        query_dirs = sorted(
            p for p in doc_dir.iterdir()
            if p.is_dir() and p.name.startswith("query_")
        )
        print(f"\n[Document {doc_index}]  ({len(query_dirs)} queries)")

        for q_dir in query_dirs:
            query_index = int(q_dir.name.split("_")[1])
            total += 1
            try:
                if (q_dir / "metrics.py").exists():
                    print(f"  [SKIP] document_{doc_index}/query_{query_index}"
                          " -- metrics.py already exists")
                    skipped += 1
                    continue
                run_scenario(client, model, doc_index, query_index)
            except Exception as exc:
                errors += 1
                print(f"  [ERROR] document_{doc_index}/query_{query_index}: {exc}")

    print("\n" + "=" * 82)
    print(f"  Done.  Total: {total}  |  Skipped: {skipped}  |  Errors: {errors}")
    print("=" * 82)


if __name__ == "__main__":
    main()
