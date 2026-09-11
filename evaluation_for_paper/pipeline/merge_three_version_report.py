"""
Three-version merge pipeline — 7 documents × 8 queries = 56 scenarios.

For each scenario this script:
  1. Loads RAG_RESPONSE from
       result_for_rag_only/document_{i}/query_{q}/report_v0.py
  2. Loads ADVISOR_REPORT_V1, ADVISOR_REPORT_V2, METRICS, USER_QUERIES from
       results/document_{i}/query_{q}/final_report.py
  3. Scores the V0 response on the same 7 criteria via a single LLM call
     (gpt-4o-mini, temperature=0.0)
  4. Merges all three sets of scores into an extended metrics dict that
     adds v0_score / weighted_v0 to every criterion and overall_v0
  5. Writes a self-contained final_report_{q}.py to
       final_result/document_{i}/query_{q}/

Existing output files are skipped (resume-safe).

Run from the workspace root:
    python evaluation_for_paper/pipeline/merge_three_version_report.py
"""

from __future__ import annotations

import importlib.util
import json
import os
import sys
import textwrap
import time
import traceback
from pathlib import Path
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]           # workspace root
EVAL_DIR = PROJECT_ROOT / "evaluation_for_paper"

RAG_RESULTS_BASE = EVAL_DIR / "result_for_rag_only"
PIPELINE_RESULTS_BASE = EVAL_DIR / "results"
OUTPUT_BASE = EVAL_DIR / "final_result"

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ---------------------------------------------------------------------------
# .env loading
# ---------------------------------------------------------------------------

from dotenv import load_dotenv  # noqa: E402

load_dotenv(dotenv_path=str(PROJECT_ROOT / "backend" / ".env"))

# ---------------------------------------------------------------------------
# OpenAI client (lazy — created after env is loaded)
# ---------------------------------------------------------------------------

import openai          # noqa: E402
from openai import OpenAI  # noqa: E402

# Re-use the retry wrapper from the evaluator module
from ai_integration.agent4_evaluator.evaluator import _safe_chat_completion  # noqa: E402

# ---------------------------------------------------------------------------
# Criteria — identical to run_pipeline.py so scores are comparable
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
            "Structural completeness — all required report sections are present "
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

assert abs(sum(c["weight"] for c in CRITERIA) - 1.0) < 1e-9, (
    "Criterion weights must sum to 1.0"
)

# ---------------------------------------------------------------------------
# Module loader
# ---------------------------------------------------------------------------

def _load_module(path: Path, module_name: str) -> Any:
    """Load an arbitrary .py file as a module via importlib."""
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# V0 scorer — single LLM call for all 7 criteria
# ---------------------------------------------------------------------------

def score_v0_on_criteria(
    client: OpenAI,
    model: str,
    query: str,
    report_v0: str,
    criteria: List[Dict[str, Any]],
) -> Dict[str, int]:
    """
    Score the RAG-only V0 response on every criterion.
    Returns a dict: {criterion_key: score_0_to_100}
    """
    criteria_block = "\n".join(
        f"- **{c['key']}** ({int(c['weight'] * 100)}%): {c['description']}"
        for c in criteria
    )

    prompt = textwrap.dedent(f"""
        You are an objective financial-report quality scorer.

        USER QUERY:
        {query}

        REPORT V0 (direct RAG response, no multi-agent pipeline):
        {report_v0}

        SCORING CRITERIA:
        {criteria_block}

        TASK:
        Score REPORT V0 on EACH criterion using an integer from 0 to 100.
        0 = completely absent/wrong, 100 = exemplary.

        Respond ONLY with a JSON object in this exact format (no prose, no markdown fence):
        {{
            "financial_accuracy":  <int>,
            "business_analysis":   <int>,
            "risk_assessment":     <int>,
            "actionable_advice":   <int>,
            "evidence_usage":      <int>,
            "completeness":        <int>,
            "query_satisfaction":  <int>
        }}
    """).strip()

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
            # Strip markdown fences if present
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()
            scores = json.loads(raw)
            result: Dict[str, int] = {}
            for c in criteria:
                key = c["key"]
                if key not in scores:
                    raise ValueError(f"Missing key in V0 score response: {key}")
                val = scores[key]
                if not isinstance(val, (int, float)):
                    raise ValueError(f"Non-numeric score for {key}: {val}")
                result[key] = max(0, min(100, int(val)))
            return result
        except (json.JSONDecodeError, ValueError, KeyError) as exc:
            if attempt == max_retries - 1:
                print(f"   [V0Scorer] Failed after {max_retries} attempts: {exc}")
                return {c["key"]: 50 for c in criteria}
            wait = (attempt + 1) * 3
            print(f"   [V0Scorer] Parse error, retrying in {wait}s… ({exc})")
            time.sleep(wait)

    # Unreachable, but satisfies type checker
    return {c["key"]: 50 for c in criteria}


# ---------------------------------------------------------------------------
# Metrics merger
# ---------------------------------------------------------------------------

def merge_metrics(
    existing_metrics: Dict[str, Any],
    v0_scores: Dict[str, int],
    criteria: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Take the existing METRICS dict (which has v1/v2 data) and inject v0
    scores to produce an extended three-version metrics dict.
    """
    details: Dict[str, Any] = {}
    weighted_v0 = 0.0
    weighted_v1 = 0.0
    weighted_v2 = 0.0

    for c in criteria:
        key = c["key"]
        w = c["weight"]
        existing = existing_metrics["criteria_detail"][key]

        v0 = v0_scores[key]
        v1 = existing["v1_score"]
        v2 = existing["v2_score"]

        contrib_v0 = round(v0 * w, 2)
        contrib_v1 = existing["weighted_v1"]
        contrib_v2 = existing["weighted_v2"]

        weighted_v0 += v0 * w
        weighted_v1 += v1 * w
        weighted_v2 += v2 * w

        details[key] = {
            "label": existing["label"],
            "weight_pct": existing["weight_pct"],
            # ---- new ----
            "v0_score": v0,
            "weighted_v0": contrib_v0,
            # ---- existing ----
            "v1_score": v1,
            "v2_score": v2,
            "delta_v0_v1": v1 - v0,          # improvement from RAG → V1
            "delta_v1_v2": v2 - v1,          # improvement from V1 → V2
            "delta_v0_v2": v2 - v0,          # total improvement
            "weighted_v1": contrib_v1,
            "weighted_v2": contrib_v2,
        }

    overall_v0 = round(weighted_v0, 2)
    overall_v1 = round(weighted_v1, 2)
    overall_v2 = round(weighted_v2, 2)

    return {
        "criteria_detail": details,
        "overall_v0": overall_v0,
        "overall_v1": overall_v1,
        "overall_v2": overall_v2,
        "improvement_v0_to_v1": round(overall_v1 - overall_v0, 2),
        "improvement_v1_to_v2": round(overall_v2 - overall_v1, 2),
        "improvement_v0_to_v2": round(overall_v2 - overall_v0, 2),
        "improvement_pct_v0_to_v2": (
            round(((overall_v2 - overall_v0) / overall_v0) * 100, 2)
            if overall_v0 != 0 else 0.0
        ),
    }


# ---------------------------------------------------------------------------
# Table printer / string builder
# ---------------------------------------------------------------------------

def build_metrics_table(metrics: Dict[str, Any], label: str) -> str:
    """Return a formatted plaintext metrics table string (three-version)."""
    details = metrics["criteria_detail"]

    col_widths = [22, 8, 10, 10, 10, 8, 8, 8]
    sep = "+" + "+".join("-" * w for w in col_widths) + "+"
    header = (
        "| {:<20} | {:>6} | {:>8} | {:>8} | {:>8} | {:>6} | {:>6} | {:>6} |".format(
            "Criterion", "Weight",
            "V0 Score", "V1 Score", "V2 Score",
            "Δ V0→V1", "Δ V1→V2", "Δ V0→V2",
        )
    )

    def _delta(n: int) -> str:
        return f"+{n}" if n >= 0 else str(n)

    lines = [
        "",
        "=" * 90,
        f"  Weighted Metrics (3 versions) — {label}",
        "=" * 90,
        sep, header, sep,
    ]

    for d in details.values():
        lines.append(
            "| {:<20} | {:>5}%  | {:>8} | {:>8} | {:>8} | {:>6} | {:>6} | {:>6} |".format(
                d["label"],
                d["weight_pct"],
                d["v0_score"],
                d["v1_score"],
                d["v2_score"],
                _delta(d["delta_v0_v1"]),
                _delta(d["delta_v1_v2"]),
                _delta(d["delta_v0_v2"]),
            )
        )

    lines += [
        sep,
        "| {:<20} | {:>6} | {:>8.2f} | {:>8.2f} | {:>8.2f} | {:>6} | {:>6} | {:>6} |".format(
            "OVERALL (weighted)", "",
            metrics["overall_v0"],
            metrics["overall_v1"],
            metrics["overall_v2"],
            _delta(int(metrics["improvement_v0_to_v1"])),
            _delta(int(metrics["improvement_v1_to_v2"])),
            _delta(int(metrics["improvement_v0_to_v2"])),
        ),
        sep,
        f"  V0→V2 total improvement: {_delta(int(metrics['improvement_v0_to_v2']))} pts "
        f"absolute  |  {metrics['improvement_pct_v0_to_v2']:+.2f}% relative",
        "=" * 90,
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Output file writer
# ---------------------------------------------------------------------------

def write_final_report(
    path: Path,
    doc_index: int,
    query_index: int,
    pdf_filename: str,
    user_query: str,
    user_queries: List[str],
    rag_response: str,
    advisor_report_v1: str,
    advisor_report_v2: str,
    v0_evaluation_report: str,
    pipeline_evaluation_report: str,
    metrics: Dict[str, Any],
    metrics_table: str,
) -> None:
    """Write the self-contained three-version final_report_{query_index}.py."""
    queries_lines = ["USER_QUERIES = ["]
    for q in user_queries:
        queries_lines.append(f"    {json.dumps(q, ensure_ascii=False)},")
    queries_lines.append("]")
    user_queries_block = "\n".join(queries_lines)

    metrics_repr = json.dumps(metrics, indent=4, ensure_ascii=False)
    metrics_repr_indented = textwrap.indent(metrics_repr, "    ")

    content = (
        '"""\n'
        f"Three-Version Evaluation Report — document_{doc_index} / query_{query_index}\n"
        f"Source document: {pdf_filename}\n"
        f"Query: {user_query}\n"
        "\n"
        "Versions compared:\n"
        "  V0 — Direct RAG response (no agent pipeline)\n"
        "  V1 — Advisor Agent first draft\n"
        "  V2 — Advisor Agent revised draft (post Critic feedback)\n"
        '"""\n'
        "from __future__ import annotations\n"
        "import json\n\n"
        f"USER_QUERY = {json.dumps(user_query, ensure_ascii=False)}\n\n"
        f"{user_queries_block}\n\n"
        '# ---------------------------------------------------------------------------\n'
        '# Responses\n'
        '# ---------------------------------------------------------------------------\n\n'
        'RAG_RESPONSE = """\n'
        f"{rag_response}\n"
        '"""\n\n'
        'ADVISOR_REPORT_V1 = """\n'
        f"{advisor_report_v1}\n"
        '"""\n\n'
        'ADVISOR_REPORT_V2 = """\n'
        f"{advisor_report_v2}\n"
        '"""\n\n'
        '# ---------------------------------------------------------------------------\n'
        '# Evaluation narratives\n'
        '# ---------------------------------------------------------------------------\n\n'
        'V0_EVALUATION_REPORT = """\n'
        f"{v0_evaluation_report}\n"
        '"""\n\n'
        'PIPELINE_EVALUATION_REPORT = """\n'
        f"{pipeline_evaluation_report}\n"
        '"""\n\n'
        '# ---------------------------------------------------------------------------\n'
        '# Metrics (three-version)\n'
        '# ---------------------------------------------------------------------------\n\n'
        'METRICS_TABLE = """\n'
        f"{metrics_table}\n"
        '"""\n\n'
        "METRICS = \\\n"
        f"{metrics_repr_indented}\n"
    )
    path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Single-scenario processor
# ---------------------------------------------------------------------------

def process_scenario(
    client: OpenAI,
    model: str,
    doc_index: int,
    query_index: int,
) -> None:
    label = f"document_{doc_index}/query_{query_index}"

    # Output path
    out_dir = OUTPUT_BASE / f"document_{doc_index}" / f"query_{query_index}"
    out_file = out_dir / f"final_report_{query_index}.py"

    if out_file.exists():
        print(f"  [SKIP] {label} already complete.")
        return

    # ---- Load V0 data -------------------------------------------------------
    v0_path = RAG_RESULTS_BASE / f"document_{doc_index}" / f"query_{query_index}" / "report_v0.py"
    if not v0_path.exists():
        print(f"  [WARN] V0 report missing, skipping: {v0_path}")
        return

    v0_module = _load_module(v0_path, f"v0_doc{doc_index}_q{query_index}")
    rag_response: str = getattr(v0_module, "RAG_RESPONSE", "").strip()
    v0_evaluation_report: str = getattr(v0_module, "EVALUATION_REPORT", "").strip()

    # ---- Load V1/V2 pipeline data -------------------------------------------
    pipeline_path = (
        PIPELINE_RESULTS_BASE
        / f"document_{doc_index}"
        / f"query_{query_index}"
        / "final_report.py"
    )
    if not pipeline_path.exists():
        print(f"  [WARN] Pipeline report missing, skipping: {pipeline_path}")
        return

    pipe_module = _load_module(pipeline_path, f"pipe_doc{doc_index}_q{query_index}")
    user_query: str = getattr(pipe_module, "USER_QUERY", "")
    user_queries: List[str] = getattr(pipe_module, "USER_QUERIES", [user_query])
    advisor_report_v1: str = getattr(pipe_module, "ADVISOR_REPORT_V1", "").strip()
    advisor_report_v2: str = getattr(pipe_module, "ADVISOR_REPORT_V2", "").strip()
    pipeline_evaluation_report: str = getattr(pipe_module, "EVALUATION_REPORT", "").strip()
    existing_metrics: Dict[str, Any] = getattr(pipe_module, "METRICS", {})

    # Derive PDF filename from the pipeline eval report docstring
    # Fall back to a generic name if the attribute isn't present
    pdf_filename = "unknown.pdf"
    try:
        doc_str = pipe_module.__doc__ or ""
        for line in doc_str.splitlines():
            if line.startswith("Source document:"):
                pdf_filename = line.split(":", 1)[1].strip()
                break
    except Exception:
        pass

    # ---- Score V0 -----------------------------------------------------------
    print(f"    Scoring V0 on 7 criteria…")
    v0_scores = score_v0_on_criteria(client, model, user_query, rag_response, CRITERIA)
    print(f"    V0 raw scores: { {k: v0_scores[k] for k in v0_scores} }")

    # ---- Merge metrics ------------------------------------------------------
    merged = merge_metrics(existing_metrics, v0_scores, CRITERIA)
    metrics_table = build_metrics_table(merged, label)
    print(metrics_table)

    # ---- Write output -------------------------------------------------------
    out_dir.mkdir(parents=True, exist_ok=True)
    write_final_report(
        path=out_file,
        doc_index=doc_index,
        query_index=query_index,
        pdf_filename=pdf_filename,
        user_query=user_query,
        user_queries=user_queries,
        rag_response=rag_response,
        advisor_report_v1=advisor_report_v1,
        advisor_report_v2=advisor_report_v2,
        v0_evaluation_report=v0_evaluation_report,
        pipeline_evaluation_report=pipeline_evaluation_report,
        metrics=merged,
        metrics_table=metrics_table,
    )
    print(f"    Saved: {label}/final_report_{query_index}.py")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[ERROR] OPENAI_API_KEY is missing. Please define it in backend/.env")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    model = "gpt-4o-mini"

    total_scenarios = 0
    completed = 0
    skipped = 0
    failed: List[str] = []

    for doc_index in range(1, 8):        # documents 1–7
        for query_index in range(1, 9):  # queries 1–8
            total_scenarios += 1
            label = f"document_{doc_index}/query_{query_index}"
            print(f"\n[{total_scenarios}/56] Processing {label}…")
            try:
                out_file = (
                    OUTPUT_BASE
                    / f"document_{doc_index}"
                    / f"query_{query_index}"
                    / f"final_report_{query_index}.py"
                )
                if out_file.exists():
                    print(f"  [SKIP] {label} already complete.")
                    skipped += 1
                    completed += 1
                    continue

                process_scenario(client, model, doc_index, query_index)
                completed += 1
                print(f"  ✓ {label} DONE  ({completed} completed so far)")

            except Exception:
                traceback.print_exc()
                failed.append(label)
                print(f"  [ERROR] {label} failed — skipping\n")

    print()
    print("=" * 60)
    print("MERGE PIPELINE COMPLETE")
    print(f"  Total scenarios : {total_scenarios}")
    print(f"  Completed       : {completed}")
    print(f"  Skipped (cached): {skipped}")
    print(f"  Failed          : {len(failed)}")
    if failed:
        print("  Failed scenarios:")
        for s in failed:
            print(f"    - {s}")
    print("=" * 60)


if __name__ == "__main__":
    main()
