"""
Test runner for the Evaluator Agent - with 7-criterion weighted metric scoring.

Loads advisor v1, critic feedback, and advisor v2 mock data, runs the full
evaluator pipeline in Mode B, then scores both V1 and V2 reports on each
criterion using an LLM-based rubric and prints a formatted comparison table.

The output mock file includes all original fields plus a MOCK_METRICS dict.
"""

# pyright: reportMissingImports=false

import importlib.util
import json
import os
import sys
import textwrap
import time
from pathlib import Path
from typing import Any, Dict, List, Optional


project_root = str(Path(__file__).resolve().parents[2])
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from ai_integration.agent4_evaluator.evaluator import EvaluatorAgent, _safe_chat_completion


# ---------------------------------------------------------------------------
# Scoring rubric
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

assert abs(sum(c["weight"] for c in CRITERIA) - 1.0) < 1e-9, "Criterion weights must sum to 1.0"


# ---------------------------------------------------------------------------
# LLM-based criterion scorer
# ---------------------------------------------------------------------------

def score_report_on_criteria(
    client,
    model: str,
    query: str,
    report_v1: str,
    report_v2: str,
    criteria: List[Dict[str, Any]],
) -> Dict[str, Dict[str, int]]:
    """
    Ask the LLM to score both V1 and V2 reports on every criterion in a
    single prompt call (one call for all criteria = cheaper + consistent).

    Returns a dict:
        {
            "<criterion_key>": {"v1": <0-100>, "v2": <0-100>},
            ...
        }
    """
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

            # Strip accidental markdown fences if the model adds them
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            raw = raw.strip()

            scores = json.loads(raw)

            # Validate all keys present and values are ints in [0, 100]
            for c in criteria:
                key = c["key"]
                if key not in scores:
                    raise ValueError(f"Missing criterion key in LLM response: {key}")
                for version in ("v1", "v2"):
                    val = scores[key][version]
                    if not isinstance(val, (int, float)):
                        raise ValueError(f"Score for {key}.{version} is not numeric: {val}")
                    scores[key][version] = max(0, min(100, int(val)))

            return scores

        except (json.JSONDecodeError, ValueError, KeyError) as exc:
            if attempt == max_retries - 1:
                print(f"   [MetricsScorer] Failed to parse LLM scores after {max_retries} attempts: {exc}")
                # Return neutral scores rather than crashing the whole run
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
    """
    Compute weighted overall scores for V1 and V2, plus improvement metrics.

    Returns a dict with per-criterion detail and aggregate figures.
    """
    details = {}
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
        if overall_v1 != 0
        else 0.0
    )

    return {
        "criteria_detail": details,
        "overall_v1": overall_v1,
        "overall_v2": overall_v2,
        "absolute_improvement": abs_improvement,
        "improvement_percentage": pct_improvement,
    }


def print_metrics_table(metrics: Dict[str, Any], source_name: str) -> str:
    """Build, print, and return a formatted comparison table string."""
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
        f"  Weighted Metrics — {source_name}",
        "=" * 62,
        sep,
        header,
        sep,
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
# Mock file builder
# ---------------------------------------------------------------------------

def build_python_mock_file_with_metrics(
    source_report_v1: str,
    source_report_v2: str,
    evaluation_report: str,
    metrics: Dict[str, Any],
    source_name: str,
) -> str:
    metrics_repr = json.dumps(metrics, indent=4, ensure_ascii=False)
    # Indent the JSON block so it reads cleanly inside the Python file
    metrics_repr_indented = textwrap.indent(metrics_repr, "    ")

    return (
        '"""\n'
        "Mock inputs for testing the Evaluator Agent (with weighted metrics).\n\n"
        f"Auto-generated from evaluator run: {source_name}.\n"
        '"""\n\n'
        "from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY\n\n"
        "MOCK_ADVISOR_REPORT_V1 = \"\"\"\n"
        f"{source_report_v1}\n"
        "\"\"\"\n\n"
        "MOCK_ADVISOR_REPORT_V2 = \"\"\"\n"
        f"{source_report_v2}\n"
        "\"\"\"\n\n"
        "MOCK_EVALUATION_REPORT = \"\"\"\n"
        f"{evaluation_report}\n"
        "\"\"\"\n\n"
        "MOCK_METRICS = \\\n"
        f"{metrics_repr_indented}\n"
    )


# ---------------------------------------------------------------------------
# Original helpers (preserved from run_test_loop.py)
# ---------------------------------------------------------------------------

def build_python_mock_file(
    source_report_v1: str,
    source_report_v2: str,
    evaluation_report: str,
    source_name: str,
) -> str:
    """Legacy builder without metrics (kept for compatibility)."""
    return (
        '"""\n'
        "Mock inputs for testing the Evaluator Agent.\n\n"
        f"Auto-generated from evaluator run: {source_name}.\n"
        '"""\n\n'
        "from ai_integration.agent2_advisor.mock_data import MOCK_CONTEXT_DOCS, USER_QUERY\n\n"
        "MOCK_ADVISOR_REPORT_V1 = \"\"\"\n"
        f"{source_report_v1}\n"
        "\"\"\"\n\n"
        "MOCK_ADVISOR_REPORT_V2 = \"\"\"\n"
        f"{source_report_v2}\n"
        "\"\"\"\n\n"
        "MOCK_EVALUATION_REPORT = \"\"\"\n"
        f"{evaluation_report}\n"
        "\"\"\"\n"
    )


def load_mock_data_module(base_dir: str, index: int):
    source_path = (
        Path(__file__).parent.parent / "agent2_advisor" / base_dir / f"mock_data_{index}.py"
    )
    module_name = f"evaluator_mock_data_{base_dir}_{index}"
    spec = importlib.util.spec_from_file_location(module_name, source_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Unable to load mock data module from {source_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Main test loop
# ---------------------------------------------------------------------------

def run_mode_b_with_metrics(agent: EvaluatorAgent) -> None:
    print("\n" + "=" * 60)
    print("MODE B — Full Pipeline Evaluation Loop  (with metrics)")
    print("=" * 60)

    after_critic_dir = "mock_data_after_critic"
    revision_dir = "mock_data_revision"
    output_dir = (
        Path(project_root) / "evaluation" / "agent4_evaluator" / "mock_data_with_metrics"
    )
    output_dir.mkdir(parents=True, exist_ok=True)

    for index in range(16, 21):
        after_critic_module = load_mock_data_module(after_critic_dir, index)
        revision_module = load_mock_data_module(revision_dir, index)

        user_query: str = after_critic_module.USER_QUERY
        mock_context_docs: List[Dict[str, Any]] = after_critic_module.MOCK_CONTEXT_DOCS
        current_report: str = after_critic_module.MOCK_ADVISOR_REPORT_V1
        critic_feedback: str = after_critic_module.MOCK_CRITIC_FEEDBACK["revision_instructions"]
        revised_report: str = revision_module.MOCK_ADVISOR_REPORT_V2

        print(f"\n--- RUNNING MOCK DATA FILE: mock_data_{index}.py ---")
        print(f"User Query:\n{user_query}\n")
        print("Running evaluator (comparing advisor report v1 and v2)...")

        # --- Step 1: run the evaluator (same as original loop) ---
        evaluation_report = agent.run(
            query=user_query,
            context_docs=mock_context_docs,
            response=current_report,
            critic_issues=critic_feedback,
            advisor_report_v2=revised_report,
        )

        # --- Step 2: score both reports on the 7 criteria ---
        print("Computing 7-criterion weighted metrics (LLM scoring)...")
        raw_scores = score_report_on_criteria(
            client=agent.client,
            model=agent.model,
            query=user_query,
            report_v1=current_report,
            report_v2=revised_report,
            criteria=CRITERIA,
        )

        # --- Step 3: compute weighted aggregates + improvement ---
        metrics = compute_weighted_scores(raw_scores, CRITERIA)

        # --- Step 4: display formatted table and capture as string ---
        metrics_table_str = print_metrics_table(metrics, f"mock_data_{index}.py")

        # Append the metrics table below the Recommendation section
        evaluation_report_with_table = (
            evaluation_report.rstrip()
            + "\n\n## Estimated Improvement (Weighted Metrics)\n"
            + "```\n"
            + metrics_table_str.strip()
            + "\n```"
        )

        # --- Step 5: save output with metrics ---
        output_file = output_dir / f"mock_data_{index}.py"
        output_file.write_text(
            build_python_mock_file_with_metrics(
                current_report,
                revised_report,
                evaluation_report_with_table,
                metrics,
                f"mock_data_{index}.py",
            ),
            encoding="utf-8",
        )

        print(
            f"=== FINAL REPORT + METRICS SAVED TO: "
            f"evaluation/agent4_evaluator/mock_data_with_metrics/mock_data_{index}.py ===\n"
        )


def main() -> None:
    print("=== STARTING EVALUATOR AGENT TEST LOOP (with metrics) ===")
    print(f"Project root added to path: {project_root}")
    print("Targeting model: gpt-4o-mini")

    from dotenv import load_dotenv

    env_path = Path(project_root) / "backend" / ".env"
    load_dotenv(dotenv_path=str(env_path))

    if not os.getenv("OPENAI_API_KEY"):
        print(
            "[ERROR] OPENAI_API_KEY is missing! "
            "Please make sure it is defined in backend/.env"
        )
        sys.exit(1)

    agent = EvaluatorAgent(model="gpt-4o-mini")
    run_mode_b_with_metrics(agent)

    print("\n=== TEST LOOP COMPLETED SUCCESSFULLY ===")


if __name__ == "__main__":
    main()
