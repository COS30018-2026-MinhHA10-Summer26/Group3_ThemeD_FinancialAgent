"""
Full 4-stage evaluation pipeline — 7 documents × 8 queries = ~56 scenarios.

For each document (document_1 .. document_7) and each query in USER_QUERIES,
the pipeline runs:

  Stage 1: AdvisorAgent.run()              → advisor_v1.py
  Stage 2: CriticAgent.run()               → critic_feedback.py
  Stage 3: AdvisorAgent.revise_with_feedback() → advisor_v2.py
  Stage 4: EvaluatorAgent.run() + 7-criterion metrics → final_report.py

Output structure:
  evaluation_for_paper/results/document_{i}/query_{q}/
      advisor_v1.py
      critic_feedback.py
      advisor_v2.py
      final_report.py

Scenarios that already have a final_report.py are skipped automatically,
so the script is safe to re-run after an interruption.

Run from the workspace root:
    python evaluation_for_paper/result_for_7_document/run_pipeline.py
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
# Project root  (file is 2 levels below workspace root)
# ---------------------------------------------------------------------------

project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# ---------------------------------------------------------------------------
# .env loading
# ---------------------------------------------------------------------------

from dotenv import load_dotenv  # noqa: E402

env_path = Path(project_root) / "backend" / ".env"
load_dotenv(dotenv_path=str(env_path))

# ---------------------------------------------------------------------------
# Agent imports (after sys.path is set)
# ---------------------------------------------------------------------------

from ai_integration.agent2_advisor.advisor import AdvisorAgent          # noqa: E402
from ai_integration.agent3_critic.critic import CriticAgent             # noqa: E402
from ai_integration.agent4_evaluator.evaluator import (                 # noqa: E402
    EvaluatorAgent,
    _safe_chat_completion,
)

# ---------------------------------------------------------------------------
# 7-criterion scoring rubric
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
# LLM-based criterion scorer
# ---------------------------------------------------------------------------

def score_report_on_criteria(
    client: Any,
    model: str,
    query: str,
    report_v1: str,
    report_v2: str,
    criteria: List[Dict[str, Any]],
) -> Dict[str, Dict[str, int]]:
    """Score both V1 and V2 reports on every criterion in a single LLM call."""
    criteria_block = "\n".join(
        f"- **{c['key']}** ({int(c['weight'] * 100)}%): {c['description']}"
        for c in criteria
    )

    prompt = textwrap.dedent(f"""
        You are an objective financial-report quality scorer.

        USER QUERY:
        {query}

        REPORT V1 (original):
        {report_v1}

        REPORT V2 (revised):
        {report_v2}

        SCORING CRITERIA:
        {criteria_block}

        TASK:
        Score BOTH reports on EACH criterion using an integer from 0 to 100.
        0 = completely absent/wrong, 100 = exemplary.

        Respond ONLY with a JSON object in this exact format (no prose, no markdown fence):
        {{
            "financial_accuracy":  {{"v1": <int>, "v2": <int>}},
            "business_analysis":   {{"v1": <int>, "v2": <int>}},
            "risk_assessment":     {{"v1": <int>, "v2": <int>}},
            "actionable_advice":   {{"v1": <int>, "v2": <int>}},
            "evidence_usage":      {{"v1": <int>, "v2": <int>}},
            "completeness":        {{"v1": <int>, "v2": <int>}},
            "query_satisfaction":  {{"v1": <int>, "v2": <int>}}
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
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()
            scores = json.loads(raw)
            for c in criteria:
                key = c["key"]
                if key not in scores:
                    raise ValueError(f"Missing criterion key: {key}")
                for version in ("v1", "v2"):
                    val = scores[key][version]
                    if not isinstance(val, (int, float)):
                        raise ValueError(f"Score for {key}.{version} not numeric: {val}")
                    scores[key][version] = max(0, min(100, int(val)))
            return scores
        except (json.JSONDecodeError, ValueError, KeyError) as exc:
            if attempt == max_retries - 1:
                print(f"   [MetricsScorer] Failed after {max_retries} attempts: {exc}")
                return {c["key"]: {"v1": 50, "v2": 50} for c in criteria}
            wait = (attempt + 1) * 3
            print(f"   [MetricsScorer] Parse error, retrying in {wait}s... ({exc})")
            time.sleep(wait)


# ---------------------------------------------------------------------------
# Metric computation helpers
# ---------------------------------------------------------------------------

def compute_weighted_scores(
    raw_scores: Dict[str, Dict[str, int]],
    criteria: List[Dict[str, Any]],
) -> Dict[str, Any]:
    details: Dict[str, Any] = {}
    weighted_v1 = 0.0
    weighted_v2 = 0.0

    for c in criteria:
        key = c["key"]
        w = c["weight"]
        v1 = raw_scores[key]["v1"]
        v2 = raw_scores[key]["v2"]
        contrib_v1 = v1 * w
        contrib_v2 = v2 * w
        weighted_v1 += contrib_v1
        weighted_v2 += contrib_v2
        details[key] = {
            "label": c["label"],
            "weight_pct": int(w * 100),
            "v1_score": v1,
            "v2_score": v2,
            "delta": v2 - v1,
            "weighted_v1": round(contrib_v1, 2),
            "weighted_v2": round(contrib_v2, 2),
        }

    overall_v1 = round(weighted_v1, 2)
    overall_v2 = round(weighted_v2, 2)
    abs_improvement = round(overall_v2 - overall_v1, 2)
    pct_improvement = (
        round(((overall_v2 - overall_v1) / overall_v1) * 100, 2)
        if overall_v1 != 0 else 0.0
    )
    return {
        "criteria_detail": details,
        "overall_v1": overall_v1,
        "overall_v2": overall_v2,
        "absolute_improvement": abs_improvement,
        "improvement_percentage": pct_improvement,
    }


def print_metrics_table(metrics: Dict[str, Any], label: str) -> str:
    details = metrics["criteria_detail"]
    sep = "+" + "+".join("-" * w for w in [22, 8, 10, 10, 8]) + "+"
    header = "| {:<20} | {:>6} | {:>8} | {:>8} | {:>6} |".format(
        "Criterion", "Weight", "V1 Score", "V2 Score", "Delta"
    )
    abs_str = (
        f"+{metrics['absolute_improvement']}"
        if metrics["absolute_improvement"] >= 0
        else str(metrics["absolute_improvement"])
    )
    pct_str = (
        f"+{metrics['improvement_percentage']}%"
        if metrics["improvement_percentage"] >= 0
        else f"{metrics['improvement_percentage']}%"
    )
    lines = [
        "",
        "=" * 62,
        f"  Weighted Metrics — {label}",
        "=" * 62,
        sep, header, sep,
    ]
    for key, d in details.items():
        delta_str = f"+{d['delta']}" if d["delta"] >= 0 else str(d["delta"])
        lines.append(
            "| {:<20} | {:>5}%  | {:>8} | {:>8} | {:>6} |".format(
                d["label"], d["weight_pct"], d["v1_score"], d["v2_score"], delta_str
            )
        )
    lines += [
        sep,
        "| {:<20} | {:>6} | {:>8.2f} | {:>8.2f} | {:>6} |".format(
            "OVERALL (weighted)", "", metrics["overall_v1"], metrics["overall_v2"], abs_str
        ),
        sep,
        f"  Improvement: {abs_str} pts absolute  |  {pct_str} relative",
        "=" * 62,
        "",
    ]
    table_str = "\n".join(lines)
    print(table_str)
    return table_str


# ---------------------------------------------------------------------------
# Document module loader
# ---------------------------------------------------------------------------

def load_document_module(doc_index: int) -> Any:
    """Load evaluation_for_paper/paper_sources/document_{i}.py via importlib."""
    source_path = (
        Path(__file__).parent.parent / "paper_sources" / f"document_{doc_index}.py"
    )
    module_name = f"paper_document_{doc_index}"
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load document module from {source_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# File writers  (doc_index + query_index used for docstrings only)
# ---------------------------------------------------------------------------

def write_advisor_v1(
    path: Path, user_query: str, report: str, doc_index: int, query_index: int
) -> None:
    content = (
        f'"""Advisor Agent Report V1 — document_{doc_index} / query_{query_index}"""\n'
        "from __future__ import annotations\n\n"
        f"USER_QUERY = {json.dumps(user_query, ensure_ascii=False)}\n\n"
        'ADVISOR_REPORT_V1 = """\n'
        f"{report}\n"
        '"""\n'
    )
    path.write_text(content, encoding="utf-8")


def write_critic_feedback(
    path: Path,
    user_query: str,
    advisor_report_v1: str,
    critic_feedback: str,
    doc_index: int,
    query_index: int,
) -> None:
    content = (
        f'"""Critic Agent Feedback — document_{doc_index} / query_{query_index}"""\n'
        "from __future__ import annotations\n\n"
        f"USER_QUERY = {json.dumps(user_query, ensure_ascii=False)}\n\n"
        'ADVISOR_REPORT_V1 = """\n'
        f"{advisor_report_v1}\n"
        '"""\n\n'
        "CRITIC_FEEDBACK = {\n"
        '    "passes": False,\n'
        '    "issues": ["See revision_instructions for the full critique output."],\n'
        f'    "revision_instructions": {json.dumps(critic_feedback, ensure_ascii=False)}\n'
        "}\n"
    )
    path.write_text(content, encoding="utf-8")


def write_advisor_v2(
    path: Path, user_query: str, report: str, doc_index: int, query_index: int
) -> None:
    content = (
        f'"""Advisor Agent Report V2 — document_{doc_index} / query_{query_index}"""\n'
        "from __future__ import annotations\n\n"
        f"USER_QUERY = {json.dumps(user_query, ensure_ascii=False)}\n\n"
        'ADVISOR_REPORT_V2 = """\n'
        f"{report}\n"
        '"""\n'
    )
    path.write_text(content, encoding="utf-8")


def write_final_report(
    path: Path,
    doc_index: int,
    query_index: int,
    pdf_filename: str,
    user_query: str,
    user_queries: List[str],
    advisor_report_v1: str,
    advisor_report_v2: str,
    evaluation_report: str,
    metrics: Dict[str, Any],
) -> None:
    queries_lines = ["USER_QUERIES = ["]
    for q in user_queries:
        queries_lines.append(f"    {json.dumps(q, ensure_ascii=False)},")
    queries_lines.append("]")
    user_queries_block = "\n".join(queries_lines)

    metrics_repr = json.dumps(metrics, indent=4, ensure_ascii=False)
    metrics_repr_indented = textwrap.indent(metrics_repr, "    ")

    content = (
        '"""\n'
        f"Full Pipeline Evaluation Report — document_{doc_index} / query_{query_index}\n"
        f"Source document: {pdf_filename}\n"
        f"Query: {user_query}\n"
        '"""\n'
        "from __future__ import annotations\n"
        "import json\n\n"
        f"USER_QUERY = {json.dumps(user_query, ensure_ascii=False)}\n\n"
        f"{user_queries_block}\n\n"
        'ADVISOR_REPORT_V1 = """\n'
        f"{advisor_report_v1}\n"
        '"""\n\n'
        'ADVISOR_REPORT_V2 = """\n'
        f"{advisor_report_v2}\n"
        '"""\n\n'
        'EVALUATION_REPORT = """\n'
        f"{evaluation_report}\n"
        '"""\n\n'
        "METRICS = \\\n"
        f"{metrics_repr_indented}\n"
    )
    path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Single-scenario runner (one query against one document)
# ---------------------------------------------------------------------------

def run_scenario(
    advisor: AdvisorAgent,
    critic: CriticAgent,
    evaluator: EvaluatorAgent,
    doc_index: int,
    query_index: int,
    user_query: str,
    user_queries: List[str],
    context_docs: List[Dict[str, Any]],
    pdf_filename: str,
) -> None:
    """Run all 4 stages for a single (document, query) scenario."""

    scenario_dir = (
        Path(project_root)
        / "evaluation_for_paper"
        / "results"
        / f"document_{doc_index}"
        / f"query_{query_index}"
    )
    scenario_dir.mkdir(parents=True, exist_ok=True)

    # Skip if already completed
    if (scenario_dir / "final_report.py").exists():
        print(f"  [SKIP] document_{doc_index}/query_{query_index} already complete.")
        return

    label = f"document_{doc_index}/query_{query_index}"

    print(f"\n  [Stage 1] Advisor v1 — {label}")
    print(f"    Query: {user_query[:90]}{'...' if len(user_query) > 90 else ''}")
    advisor_report_v1 = advisor.run(user_query, context_docs)
    write_advisor_v1(scenario_dir / "advisor_v1.py", user_query, advisor_report_v1, doc_index, query_index)
    print(f"    Saved: {label}/advisor_v1.py")

    print(f"\n  [Stage 2] Critic — {label}")
    critic_feedback = critic.run(user_query, context_docs, advisor_report_v1)
    write_critic_feedback(
        scenario_dir / "critic_feedback.py",
        user_query, advisor_report_v1, critic_feedback, doc_index, query_index,
    )
    print(f"    Saved: {label}/critic_feedback.py")

    print(f"\n  [Stage 3] Advisor v2 (revision) — {label}")
    advisor_report_v2 = advisor.revise_with_feedback(
        query=user_query,
        context_docs=context_docs,
        current_report=advisor_report_v1,
        critic_feedback=critic_feedback,
    )
    write_advisor_v2(scenario_dir / "advisor_v2.py", user_query, advisor_report_v2, doc_index, query_index)
    print(f"    Saved: {label}/advisor_v2.py")

    print(f"\n  [Stage 4] Evaluator + Metrics — {label}")
    evaluation_report = evaluator.run(
        query=user_query,
        context_docs=context_docs,
        response=advisor_report_v1,
        critic_issues=critic_feedback,
        advisor_report_v2=advisor_report_v2,
    )

    print(f"    Computing 7-criterion weighted metrics...")
    raw_scores = score_report_on_criteria(
        client=evaluator.client,
        model=evaluator.model,
        query=user_query,
        report_v1=advisor_report_v1,
        report_v2=advisor_report_v2,
        criteria=CRITERIA,
    )
    metrics = compute_weighted_scores(raw_scores, CRITERIA)
    metrics_table_str = print_metrics_table(metrics, label)

    evaluation_report_with_table = (
        evaluation_report.rstrip()
        + "\n\n## Estimated Improvement (Weighted Metrics)\n"
        + "```\n"
        + metrics_table_str.strip()
        + "\n```"
    )

    write_final_report(
        path=scenario_dir / "final_report.py",
        doc_index=doc_index,
        query_index=query_index,
        pdf_filename=pdf_filename,
        user_query=user_query,
        user_queries=user_queries,
        advisor_report_v1=advisor_report_v1,
        advisor_report_v2=advisor_report_v2,
        evaluation_report=evaluation_report_with_table,
        metrics=metrics,
    )
    print(f"    Saved: {label}/final_report.py")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        print("[ERROR] OPENAI_API_KEY is missing. Please define it in backend/.env")
        sys.exit(1)

    advisor = AdvisorAgent(model="gpt-4o-mini")
    critic = CriticAgent(model="gpt-4o-mini")
    evaluator = EvaluatorAgent(model="gpt-4o-mini")

    total_docs = 7
    total_scenarios = 0
    completed = 0
    failed: List[str] = []

    for doc_index in range(3, total_docs + 1):
        try:
            doc_module = load_document_module(doc_index)
            user_queries: List[str] = doc_module.USER_QUERIES
            context_docs: List[Dict[str, Any]] = doc_module.CONTEXT_DOCS
            pdf_filename: str = context_docs[0]["source"].split(" (")[0]

            print()
            print("=" * 60)
            print(f"DOCUMENT {doc_index}/{total_docs} — {pdf_filename}")
            print(f"  {len(user_queries)} queries → {len(user_queries)} scenarios")
            print("=" * 60)

            for query_index, user_query in enumerate(user_queries, start=1):
                total_scenarios += 1
                scenario_label = f"document_{doc_index}/query_{query_index}"
                try:
                    run_scenario(
                        advisor=advisor,
                        critic=critic,
                        evaluator=evaluator,
                        doc_index=doc_index,
                        query_index=query_index,
                        user_query=user_query,
                        user_queries=user_queries,
                        context_docs=context_docs,
                        pdf_filename=pdf_filename,
                    )
                    completed += 1
                    print(f"\n  ✓ {scenario_label} DONE  ({completed} completed so far)")
                except Exception:
                    traceback.print_exc()
                    failed.append(scenario_label)
                    print(f"\n  [ERROR] {scenario_label} failed — skipping\n")
                    continue

        except Exception:
            traceback.print_exc()
            print(f"\n[ERROR] Failed to load document_{doc_index} — skipping entire document\n")
            continue

    print()
    print("=" * 60)
    print("PIPELINE COMPLETE")
    print(f"  Total scenarios : {total_scenarios}")
    print(f"  Completed       : {completed}")
    print(f"  Failed          : {len(failed)}")
    if failed:
        print("  Failed scenarios:")
        for s in failed:
            print(f"    - {s}")
    print("=" * 60)


if __name__ == "__main__":
    main()
