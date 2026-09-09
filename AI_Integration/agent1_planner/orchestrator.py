"""
Planning/orchestration agent for the financial multi-agent system.

Primary behavior:
- use ExternalLLM to classify the query
- use ExternalLLM to generate a structured JSON workflow plan
- execute the planned agent nodes in order
"""

from __future__ import annotations

import importlib
import json
import logging
from pathlib import Path
import re
from typing import Any, Callable

logger = logging.getLogger(__name__)

import yaml

from ai_integration.agent1_planner.answer_agent import AnswerAgent
from ai_integration.agent1_planner.retrieval_agent import RetrievalAgent
from ai_integration.agent5_searcher.searching_agent import SearchingAgent
from ai_integration.entity_filter import (
    extract_query_entities,
    filter_documents_for_query_entity,
    missing_query_entities,
)
from ai_integration.memory.session_memory import ShortTermMemory
from ai_integration.memory.semantic_memory import get_reader as _get_semantic_reader, get_writer as _get_semantic_writer, is_semantic_memory_enabled
from ai_integration.memory.user_preference_memory import get_reader as _get_pref_reader, get_writer as _get_pref_writer, is_preference_memory_enabled


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAW_DIR = PROJECT_ROOT / "data" / "raw"
CONFIG_PATH = PROJECT_ROOT / "ai_integration" / "config.yaml"

LLM_CLASSIFICATION_PROMPT = """
You are a planning/orchestration agent for a financial AI system.

Classify the user's query into exactly one route:
- "skip": not related to finance, markets, companies, investing, or business analysis
- "qa": finance-related question answering that mainly needs retrieval/search and a grounded answer
- "deep_advice": deeper strategic or investment advice that should orchestrate specialist agents

Return only valid JSON with this schema:
{
  "route": "skip|qa|deep_advice",
  "reason": "short explanation",
  "confidence": 0.0
}
"""

LLM_PLAN_PROMPT = """
You are a planning/orchestration agent for a financial AI system.

Create a JSON workflow plan for the user query.

Rules:
- Return only valid JSON.
- `required_information` must list the key missing or needed information.
- `workflow` must be an ordered list of execution steps.
- Allowed agent names:
  - "SkipAgent"
  - "RetrievalAgent"
  - "SearchAgent"
  - "AnswerAgent"
  - "AdvisorAgent"
  - "CriticAgent"
  - "EvaluatorAgent"
  - "ReportAgent"
- For finance Q&A, the workflow should usually center on RetrievalAgent -> optional SearchAgent -> AnswerAgent.
- For deep advice, the workflow should usually involve RetrievalAgent, optional SearchAgent, then AdvisorAgent, then optional CriticAgent, optional EvaluatorAgent, and optional ReportAgent.

Return JSON in this shape:
{
  "route": "skip|qa|deep_advice",
  "required_information": ["..."],
  "workflow": [
    {
      "step": 1,
      "agent": "RetrievalAgent"
    },
    {
      "step": 2,
      "agent": "SearchAgent",
      "condition": "coverage_score < 0.72"
    }
  ]
}
"""


class PlanningOrchestrator:
    """Classifier + planner + executor for the financial agent stack."""

    def __init__(
        self,
        progress_callback=None,
        context_searcher: Callable[[str], list[dict[str, Any]]] | None = None,
    ) -> None:
        self.config = self._load_config()
        self._progress_callback = progress_callback
        self._context_searcher = context_searcher

    def _emit_progress(self, step: str, message: str) -> None:
        """Send a progress update to the caller if a callback is registered."""
        if self._progress_callback is not None:
            try:
                self._progress_callback(step, message)
            except Exception:
                pass

    def run(self, query: str, memory: dict[str, Any] | None = None) -> dict[str, Any]:
        memory = dict(memory or {})
        workflow_steps: list[str] = ["input_processed"]
        errors: list[str] = []
        metadata = dict(memory.get("metadata", {}))

        cleaned_query = query.strip()
        original_query = metadata.get("original_query", cleaned_query)
        decision = self.classify_query(cleaned_query)
        workflow_steps.append(f"classified:{decision['route']}")
        self._emit_progress("classifying", f"Classifying: {decision['route']}")
        plan = self.plan_query(cleaned_query, decision)
        workflow_steps.append("planned_workflow")
        self._emit_progress("planning", "Workflow planned")

        # Initialise per-request shared memory
        shared_memory = ShortTermMemory()
        route = plan.get("route", decision["route"])
        shared_memory.set_context(
            query=cleaned_query,
            route=route,
            metadata=metadata,
            plan=plan,
        )

        state: dict[str, Any] = {
            "query": query,
            "original_query": original_query,
            "cleaned_query": cleaned_query,
            "route": route,
            "classification_reason": decision["reason"],
            "classification_confidence": decision["confidence"],
            "messages": [{"role": "user", "content": cleaned_query}],
            "tool_calls": [],
            "tool_results": [],
            "workflow_steps": workflow_steps,
            "errors": errors,
            "metadata": metadata,
            "required_information": plan.get("required_information", []),
            "planned_workflow": plan.get("workflow", []),
            "plan": plan,
            "context_docs": [],
            "coverage_score": 0.0,
            "executed_agents": [],
            "final_output": "",
            "response": "",
            "report": None,
            "artifacts": {},
            "shared_memory": shared_memory,
        }

        self._execute_plan(state, memory)
        workflow_steps.append("completed")
        state["shared_memory_snapshot"] = shared_memory.snapshot()
        return state

    def classify_query(self, query: str) -> dict[str, Any]:
        llm = self._build_external_llm()
        if llm is not None:
            prompt = f"{LLM_CLASSIFICATION_PROMPT}\n\nUser Query:\n{query}"
            try:
                raw = llm.generate_response(prompt)
                parsed = self._parse_json_response(raw)
                route = str(parsed.get("route", "")).strip()
                if route in {"skip", "qa", "deep_advice"}:
                    return {
                        "route": route,
                        "reason": str(parsed.get("reason", "LLM classified the query.")),
                        "confidence": float(parsed.get("confidence", 0.8)),
                    }
            except Exception:
                pass
        return self._fallback_classification(query)

    def plan_query(self, query: str, decision: dict[str, Any]) -> dict[str, Any]:
        llm = self._build_external_llm()
        if llm is not None:
            prompt = (
                f"{LLM_PLAN_PROMPT}\n\n"
                f"Classification Decision:\n{json.dumps(decision, indent=2)}\n\n"
                f"User Query:\n{query}"
            )
            try:
                raw = llm.generate_response(prompt)
                parsed = self._parse_json_response(raw)
                normalized = self._normalize_plan(parsed, decision["route"])
                if normalized["workflow"]:
                    return normalized
            except Exception:
                pass
        return self._fallback_plan(decision["route"])

    def _handle_skip(self, query: str) -> str:
        return (
            f"This query is outside the financial-analysis workflow: {query}\n\n"
            "Supported requests are finance-related Q&A, company/market analysis, report lookup, "
            "and deeper investment or strategic advice."
        )

    def _execute_plan(self, state: dict[str, Any], memory: dict[str, Any]) -> None:
        workflow = sorted(state.get("planned_workflow", []), key=lambda item: item.get("step", 0))
        # A planner model may omit SearchAgent from an otherwise valid plan.
        # For a multi-company comparison, add it after retrieval so missing
        # company evidence is always eligible for external search.
        if (
            state.get("route") != "skip"
            and len(extract_query_entities(state["cleaned_query"], state.get("metadata", {}))) > 1
            and not any(str(step.get("agent", "")).strip() == "SearchAgent" for step in workflow)
        ):
            retrieval_index = next(
                (index for index, step in enumerate(workflow) if step.get("agent") == "RetrievalAgent"),
                len(workflow),
            )
            previous_step = float(workflow[retrieval_index].get("step", retrieval_index + 1)) if retrieval_index < len(workflow) else 0.0
            workflow.insert(
                retrieval_index + 1,
                {"step": previous_step + 0.5, "agent": "SearchAgent", "condition": "coverage_score < 0.72"},
            )
        for step in workflow:
            agent_name = str(step.get("agent", "")).strip()
            if not agent_name:
                continue
            if not self._should_execute_step(step, state):
                state["workflow_steps"].append(f"skipped:{agent_name}")
                continue
            state["executed_agents"].append(agent_name)
            state["workflow_steps"].append(f"agent_started:{agent_name}")
            self._emit_progress(f"agent_{agent_name}", f"{agent_name} is running...")
            self._execute_agent_step(agent_name, state, memory)
            state["workflow_steps"].append(f"agent_completed:{agent_name}")
            self._emit_progress(f"agent_{agent_name}_done", f"{agent_name} completed")
            if agent_name == "SkipAgent":
                break

    def _should_execute_step(self, step: dict[str, Any], state: dict[str, Any]) -> bool:
        # A comparison requires evidence for every company named in the query.
        # Overall retrieval coverage can be high when it only found documents
        # for one company (for example Tesla but not Google), so do not let it
        # suppress the external search step in that case.
        if str(step.get("agent", "")).strip() == "SearchAgent":
            missing_entities = missing_query_entities(
                state["cleaned_query"],
                state.get("context_docs", []),
                state.get("metadata", {}),
            )
            if missing_entities:
                state["metadata"]["missing_query_entities"] = sorted(missing_entities)
                return True

        condition = str(step.get("condition", "")).strip()
        if not condition:
            return True
        match = re.fullmatch(r"coverage_score\s*([<>]=?)\s*([0-9]*\.?[0-9]+)", condition)
        if not match:
            return True
        operator = match.group(1)
        threshold = float(match.group(2))
        coverage = float(state.get("coverage_score", 0.0))
        if operator == "<":
            return coverage < threshold
        if operator == "<=":
            return coverage <= threshold
        if operator == ">":
            return coverage > threshold
        if operator == ">=":
            return coverage >= threshold
        return True

    def _execute_agent_step(self, agent_name: str, state: dict[str, Any], memory: dict[str, Any]) -> None:
        if agent_name == "SkipAgent":
            response = self._handle_skip(state["cleaned_query"])
            state["response"] = response
            state["final_output"] = response
            state["messages"].append({"role": "assistant", "content": response})
            state["tool_calls"].append({"tool": "SkipAgent"})
            state["tool_results"].append({"tool": "SkipAgent", "status": "completed"})
            return
        if agent_name == "RetrievalAgent":
            self._run_retrieval_agent(state, memory)
            return
        if agent_name == "SearchAgent":
            self._run_search_agent(state)
            return
        if agent_name == "AnswerAgent":
            self._run_answer_agent(state)
            return
        if agent_name == "AdvisorAgent":
            self._run_advisor_agent(state)
            return
        if agent_name == "CriticAgent":
            self._run_critic_agent(state)
            return
        if agent_name == "EvaluatorAgent":
            self._run_evaluator_agent(state)
            return
        if agent_name == "ReportAgent":
            self._run_report_agent(state)
            return

    def _run_retrieval_agent(self, state: dict[str, Any], memory: dict[str, Any]) -> None:
        agent = self._build_retrieval_agent()
        result = agent.run(state["cleaned_query"], memory)
        state["context_docs"] = result["context_docs"]
        state["coverage_score"] = float(result.get("coverage_score", 0.0))
        state["tool_calls"].append({"tool": "RetrievalAgent"})
        state["tool_calls"].extend(result.get("tool_calls", []))
        state["tool_results"].append(
            {"tool": "RetrievalAgent", "document_count": len(state["context_docs"]), "coverage_score": state["coverage_score"]}
        )
        state["tool_results"].extend(result.get("tool_results", []))
        state["workflow_steps"].extend(result.get("workflow_steps", []))
        state["errors"].extend(result.get("errors", []))
        state["metadata"].update(result.get("metadata", {}))
        self._emit_progress(
            "retrieving",
            f"{len(state['context_docs'])} related docs found",
        )

        # Sync to shared memory
        shared_memory: ShortTermMemory = state["shared_memory"]
        shared_memory.set_retrieval_docs(state["context_docs"])

        # ── Semantic Memory: inject cached facts (read path) ────────────
        if is_semantic_memory_enabled():
            try:
                metadata = state.get("metadata", {})
                project_id = metadata.get("project_id")
                conversation_id = metadata.get("conversation_id")
                if project_id:
                    reader = _get_semantic_reader()
                    semantic_facts = reader.recall(
                        query=state["cleaned_query"],
                        project_id=project_id,
                        conversation_id=conversation_id,
                    )
                    if semantic_facts:
                        merged = self._deduplicate_documents(
                            state["context_docs"] + semantic_facts
                        )
                        state["context_docs"] = merged
                        shared_memory.set_retrieval_docs(merged)
                        state["workflow_steps"].append(
                            f"semantic_memory_injected:{len(semantic_facts)}_facts"
                        )
                        self._emit_progress(
                            "semantic_memory",
                            f"Injected {len(semantic_facts)} cached facts from semantic memory",
                        )
            except Exception as _sem_exc:
                state["errors"].append(f"semantic_memory_read_error: {_sem_exc}")

    def _run_search_agent(self, state: dict[str, Any]) -> None:
        if self._context_searcher is not None:
            search_docs = self._context_searcher(state["cleaned_query"])
            search_docs = filter_documents_for_query_entity(
                state["cleaned_query"],
                search_docs,
                state.get("metadata", {}),
            )
        else:
            agent = self._build_search_agent()
            search_docs = agent.run(state["cleaned_query"], state.get("context_docs", []))
        merged_docs = self._deduplicate_documents(state.get("context_docs", []) + search_docs)
        state["context_docs"] = merged_docs
        top_k = int(self.config.get("top_k", 5))
        state["coverage_score"] = max(float(state.get("coverage_score", 0.0)), min(1.0, len(merged_docs) / max(top_k, 1)))
        state["tool_calls"].append({"tool": "SearchAgent"})
        state["tool_results"].append({"tool": "SearchAgent", "document_count": len(search_docs)})
        state["metadata"]["final_context_count"] = len(merged_docs)
        state["metadata"]["coverage_score"] = state["coverage_score"]
        state["workflow_steps"].append("searched_external_context")

        # Sync to shared memory (set, not append, to avoid duplicates)
        shared_memory: ShortTermMemory = state["shared_memory"]
        shared_memory.set_retrieval_docs(merged_docs)

    def _run_answer_agent(self, state: dict[str, Any]) -> None:
        shared_memory: ShortTermMemory = state["shared_memory"]
        revision_config = self.config.get("revision", {})
        max_loops = int(revision_config.get("max_loops", 2))
        search_on_missing = bool(revision_config.get("search_on_missing", True))
        retrieval_threshold = float(self.config.get("retrieval_threshold", 0.25))

        evaluator_cls = self._load_class(
            "ai_integration.agent4_evaluator.evaluator", "EvaluatorAgent",
        )

        # Initial answer generation
        # AnswerAgent consumes exactly the context written by the preceding
        # retrieval/search agents into request-scoped shared memory.
        memory_docs = shared_memory.get_retrieval_docs()
        if memory_docs:
            state["context_docs"] = self._deduplicate_documents(memory_docs)

        if state.get("route") == "qa" and (
            not state.get("context_docs")
            or float(state.get("coverage_score", 0.0)) < retrieval_threshold
        ):
            response = (
                f"I do not have enough information to answer this question reliably: {state['cleaned_query']}\n\n"
                "Please provide more relevant source documents or ask a narrower finance question."
            )
            state["response"] = response
            state["final_output"] = response
            state["messages"].append({"role": "assistant", "content": response})
            state["tool_calls"].append({"tool": "AnswerAgent", "status": "insufficient_information"})
            state["tool_results"].append({
                "tool": "AnswerAgent",
                "status": "insufficient_information",
                "document_count": len(state.get("context_docs", [])),
                "coverage_score": float(state.get("coverage_score", 0.0)),
            })
            self._emit_progress("answering", "QA does not have enough information to answer")
            return

        agent = self._build_answer_agent()
        response = agent.run(
            state["cleaned_query"],
            state.get("context_docs", []),
            state.get("metadata", {}),
        )
        state["response"] = response
        state["final_output"] = response
        state["messages"].append({"role": "assistant", "content": response})
        state["tool_calls"].append({"tool": "AnswerAgent"})
        answer_error = getattr(agent, "last_error", None)
        if answer_error:
            state["errors"].append(str(answer_error))
        state["tool_results"].append({
            "tool": "AnswerAgent",
            "status": "fallback" if answer_error else "completed",
            "context_source": "shared_memory.retrieval_docs",
            "document_count": len(state["context_docs"]),
        })
        self._emit_progress("answering", "AnswerAgent đã trả lời")

        # A model/configuration failure cannot be improved by the evaluator
        # loop. Return the explicit fallback and preserve the error in state.
        if answer_error:
            state["workflow_steps"].append("answer_generation_fallback")
            return

        # QA evaluation loop
        if state.get("route") == "qa":
            return

        if evaluator_cls is None:
            return

        for loop_index in range(max_loops):
            try:
                evaluator = evaluator_cls()
                verdict_result = evaluator.evaluate_structured(
                    query=state["cleaned_query"],
                    context_docs=state.get("context_docs", []),
                    response=state["final_output"],
                )
                shared_memory.set_evaluator_verdict(verdict_result)
                state["tool_calls"].append({"tool": "EvaluatorAgent", "mode": "qa"})
                state["tool_results"].append(
                    {
                        "tool": "EvaluatorAgent",
                        "status": "completed",
                        "verdict": verdict_result["verdict"],
                        "loop": loop_index + 1,
                    },
                )
                state["artifacts"]["evaluator_report"] = verdict_result["evaluation_markdown"]
                state["workflow_steps"].append(
                    f"qa_evaluated:{verdict_result['verdict']}:loop_{loop_index + 1}",
                )
                self._emit_progress(
                    f"qa_eval_loop_{loop_index + 1}",
                    f"QA Evaluator: {verdict_result['verdict']} (loop {loop_index + 1})",
                )

                if verdict_result["verdict"] == "PASS":
                    break

                # Search for additional context if missing topics detected
                if search_on_missing and verdict_result.get("missing_topics"):
                    missing = verdict_result["missing_topics"]
                    search_query = f"{state['cleaned_query']}\n{' '.join(str(t) for t in missing[:3])}"
                    search_docs = self._search_for_context(search_query)
                    if search_docs:
                        merged = self._deduplicate_documents(
                            state.get("context_docs", []) + search_docs,
                        )
                        state["context_docs"] = merged
                        shared_memory.set_retrieval_docs(merged)
                        state["workflow_steps"].append("qa_searched_additional_context")

                # Regenerate answer with improved context
                memory_docs = shared_memory.get_retrieval_docs()
                if memory_docs:
                    state["context_docs"] = self._deduplicate_documents(memory_docs)
                agent = self._build_answer_agent()
                response = agent.run(
                    state["cleaned_query"],
                    state.get("context_docs", []),
                    state.get("metadata", {}),
                )
                state["response"] = response
                state["final_output"] = response
                state["messages"].append({"role": "assistant", "content": response})
                state["tool_calls"].append({"tool": "AnswerAgent", "loop": loop_index + 1})
                state["tool_results"].append(
                    {
                        "tool": "AnswerAgent",
                        "status": "fallback" if getattr(agent, "last_error", None) else "completed",
                        "loop": loop_index + 1,
                        "context_source": "shared_memory.retrieval_docs",
                        "document_count": len(state["context_docs"]),
                    },
                )
                if getattr(agent, "last_error", None):
                    state["errors"].append(str(agent.last_error))
                shared_memory.increment_revision_count()

            except Exception as exc:
                state["errors"].append(f"qa_evaluator_error: {exc}")
                break
        else:
            state["workflow_steps"].append(
                f"qa_evaluation_limit_reached:max_loops={max_loops}",
            )

    def _run_advisor_agent(self, state: dict[str, Any]) -> None:
        shared_memory: ShortTermMemory = state["shared_memory"]

        # ── User Preference Memory: load for this user (read path) ────────
        user_preferences: dict[str, Any] = {}
        if is_preference_memory_enabled():
            try:
                user_id = state.get("metadata", {}).get("user_id")
                if user_id:
                    user_preferences = _get_pref_reader().load(user_id)
                    if user_preferences:
                        state["workflow_steps"].append(
                            f"preference_memory_loaded:{len(user_preferences)}_prefs"
                        )
            except Exception as _pref_exc:
                state["errors"].append(f"preference_memory_read_error: {_pref_exc}")

        result = self._run_deep_advice(
            state["cleaned_query"],
            state.get("context_docs", []),
            state.get("metadata", {}),
            shared_memory,
            user_preferences=user_preferences,
        )
        state["tool_calls"].extend(result["tool_calls"])
        state["tool_results"].extend(result["tool_results"])
        state["workflow_steps"].extend(result["workflow_steps"])
        state["errors"].extend(result["errors"])
        state["artifacts"].update(result["artifacts"])
        state["report"] = result.get("advisor_report")
        if result.get("context_docs") is not None:
            state["context_docs"] = result["context_docs"]
            state["metadata"]["final_context_count"] = len(state["context_docs"])
            state["metadata"]["coverage_score"] = result.get("coverage_score", state.get("coverage_score", 0.0))
            state["coverage_score"] = float(state["metadata"]["coverage_score"])
        state["response"] = result["final_output"]
        state["final_output"] = result["final_output"]
        if result["final_output"]:
            state["messages"].append({"role": "assistant", "content": result["final_output"]})

    def _run_critic_agent(self, state: dict[str, Any]) -> None:
        if state["artifacts"].get("critic_report"):
            state["tool_calls"].append({"tool": "CriticAgent"})
            state["tool_results"].append({"tool": "CriticAgent", "status": "completed"})
        elif not state.get("report"):
            state["errors"].append("critic_agent_skipped_missing_advisor_report")

    def _run_evaluator_agent(self, state: dict[str, Any]) -> None:
        shared_memory: ShortTermMemory = state["shared_memory"]
        verdict = shared_memory.get_evaluator_verdict()
        if state["artifacts"].get("evaluator_report") or verdict:
            state["tool_calls"].append({"tool": "EvaluatorAgent"})
            state["tool_results"].append({
                "tool": "EvaluatorAgent",
                "status": "completed",
                "verdict": verdict.get("verdict", "N/A") if verdict else "N/A",
            })
        elif not state.get("report"):
            state["errors"].append("evaluator_agent_skipped_missing_advisor_report")

    def _run_report_agent(self, state: dict[str, Any]) -> None:
        if state.get("report"):
            state["final_output"] = state["report"]
        state["tool_calls"].append({"tool": "ReportAgent"})
        state["tool_results"].append({"tool": "ReportAgent", "status": "completed"})

    def _run_deep_advice(
        self,
        query: str,
        context_docs: list[dict[str, Any]],
        metadata: dict[str, Any],
        shared_memory: ShortTermMemory,
        user_preferences: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Run the full deep-advice pipeline with a revision loop.

        Flow
        ----
        1. Advisor produces report **v1**.
        2. **Revision loop** (up to *max_loops* iterations):
           a. Critic reviews the latest advisor report.
           b. Advisor revises the report using Critic (+ optional Evaluator) feedback.
           c. Evaluator produces a structured PASS/FAIL verdict.
           d. If PASS → break early.
           e. If missing topics detected → SearchAgent fetches more context.
        3. Return the latest (best) advisor report.

        All intermediate results are written to *shared_memory* so that
        every agent can read from the shared four-compartment store.
        """
        workflow_steps: list[str] = []
        tool_calls: list[dict[str, Any]] = []
        tool_results: list[dict[str, Any]] = []
        errors: list[str] = []
        artifacts: dict[str, Any] = {}

        revision_config = self.config.get("revision", {})
        max_loops = int(revision_config.get("max_loops", 2))
        search_on_missing = bool(revision_config.get("search_on_missing", True))

        advisor_report = None

        advisor_cls = self._load_class("ai_integration.agent2_advisor.advisor", "AdvisorAgent")
        critic_cls = self._load_class("ai_integration.agent3_critic.critic", "CriticAgent")
        evaluator_cls = self._load_class("ai_integration.agent4_evaluator.evaluator", "EvaluatorAgent")

        # ── Pre-Search: bổ sung context trước khi gọi Advisor ─────────────
        # Nếu coverage hiện tại dưới threshold, chủ động search trước để Advisor
        # (hoặc fallback AnswerAgent) có đủ tài liệu NVIDIA/công ty được hỏi.
        top_k = int(self.config.get("top_k", 5))
        retrieval_threshold = float(self.config.get("retrieval_threshold", 0.25))
        current_coverage = min(1.0, len(context_docs) / max(top_k, 1))
        if current_coverage < retrieval_threshold or not context_docs:
            self._emit_progress("pre_search", "Coverage thấp – đang tìm kiếm thêm context...")
            pre_search_docs = self._search_for_context(query)
            if pre_search_docs:
                context_docs = self._deduplicate_documents(context_docs + pre_search_docs)
                shared_memory.set_retrieval_docs(context_docs)
                workflow_steps.append(f"pre_searched:{len(pre_search_docs)}_docs")
                self._emit_progress(
                    "pre_search_done",
                    f"Pre-search: thêm {len(pre_search_docs)} docs (total {len(context_docs)})",
                )
                tool_calls.append({"tool": "SearchAgent", "reason": "pre_search_low_coverage"})
                tool_results.append({
                    "tool": "SearchAgent",
                    "status": "completed",
                    "reason": "pre_search_low_coverage",
                    "added_docs": len(pre_search_docs),
                })

        if advisor_cls is None:
            errors.append("advisor_agent_unavailable")
            # Graceful: dùng AnswerAgent để tận dụng context đã thu thập
            final_output = self._graceful_advisor_fallback(query, context_docs, errors)
            return {
                "workflow_steps": workflow_steps,
                "tool_calls": tool_calls,
                "tool_results": tool_results,
                "errors": errors,
                "artifacts": artifacts,
                "advisor_report": None,
                "final_output": final_output,
                "context_docs": context_docs,
            }

        # ── Advisor v1 ──────────────────────────────────────────────────
        try:
            advisor = self._build_advisor_agent(advisor_cls)
            advisor_report = advisor.run(
                query, context_docs,
                user_preferences=user_preferences or {},
            )
            context_docs = self._deduplicate_documents(
                getattr(advisor, "current_context_docs", context_docs),
            )
            delegated_events = list(getattr(advisor, "delegated_context_events", []))
            workflow_steps.append("advisor_v1_completed")
            self._emit_progress("advisor_v1", "Advisor v1 hoàn thành")
            tool_calls.append({"tool": "AdvisorAgent", "version": "v1"})
            if delegated_events:
                workflow_steps.append("advisor_delegated_context_retrieval")
                tool_calls.append({"tool": "AdvisorAgent.request_additional_context"})
            tool_results.append(
                {
                    "tool": "AdvisorAgent",
                    "status": "completed",
                    "version": "v1",
                    "context_document_count": len(context_docs),
                    "delegated_context_events": delegated_events,
                },
            )
            artifacts["advisor_report"] = advisor_report
            artifacts["advisor_report_v1"] = advisor_report
            artifacts["advisor_context_events"] = delegated_events
            shared_memory.set_retrieval_docs(context_docs)
            shared_memory.set_advisor_report(advisor_report, version_label="v1")
        except Exception as exc:
            errors.append(f"advisor_agent_error: {exc}")
            logger.error("AdvisorAgent.run() failed: %s", exc, exc_info=True)
            # Graceful: dùng AnswerAgent với context đã thu thập thay vì trả về
            # boilerplate text không có giá trị cho người dùng.
            final_output = self._graceful_advisor_fallback(query, context_docs, errors)
            return {
                "workflow_steps": workflow_steps,
                "tool_calls": tool_calls,
                "tool_results": tool_results,
                "errors": errors,
                "artifacts": artifacts,
                "advisor_report": advisor_report,
                "final_output": final_output,
                "context_docs": context_docs,
            }

        # ── Revision loop: Critic → Advisor revision → Evaluator ────────
        for loop_index in range(max_loops):
            loop_label = f"loop_{loop_index + 1}"

            # ── Critic ──────────────────────────────────────────────────
            if critic_cls is not None:
                try:
                    critic = critic_cls()
                    advisor_latest = shared_memory.get_advisor_report() or advisor_report
                    critic_report = critic.run(query, context_docs, advisor_latest)
                    workflow_steps.append(f"critic_completed:{loop_label}")
                    self._emit_progress(f"critic_{loop_label}", f"Critic đã review ({loop_label})")
                    tool_calls.append({"tool": "CriticAgent", "loop": loop_label})
                    tool_results.append(
                        {"tool": "CriticAgent", "status": "completed", "loop": loop_label},
                    )
                    artifacts["critic_report"] = critic_report
                    shared_memory.set_critic_argument(
                        critique=critic_report,
                        issues=self._extract_issues_from_critique(critic_report),
                    )
                except Exception as exc:
                    errors.append(f"critic_agent_error:{loop_label}: {exc}")

            # ── Advisor revision ────────────────────────────────────────
            critic_arg = shared_memory.get_critic_argument()
            critic_feedback = critic_arg.get("critique", "")

            if critic_feedback:
                try:
                    evaluator_verdict = shared_memory.get_evaluator_verdict()
                    evaluator_feedback = (
                        evaluator_verdict.get("evaluation_markdown")
                        if evaluator_verdict
                        else None
                    )
                    advisor_latest = shared_memory.get_advisor_report() or advisor_report
                    advisor_for_revision = self._build_advisor_agent(advisor_cls)
                    revised_report = advisor_for_revision.revise_with_feedback(
                        query=query,
                        context_docs=context_docs,
                        current_report=advisor_latest,
                        critic_feedback=critic_feedback,
                        evaluator_feedback=evaluator_feedback,
                    )
                    context_docs = self._deduplicate_documents(
                        getattr(advisor_for_revision, "current_context_docs", context_docs),
                    )
                    version_label = f"v{loop_index + 2}"
                    shared_memory.set_advisor_report(revised_report, version_label=version_label)
                    shared_memory.set_retrieval_docs(context_docs)
                    advisor_report = revised_report
                    artifacts["advisor_report"] = revised_report
                    artifacts[f"advisor_report_{version_label}"] = revised_report
                    workflow_steps.append(f"advisor_revised:{version_label}:{loop_label}")
                    self._emit_progress(f"advisor_{version_label}", f"Advisor đã sửa → {version_label}")
                    tool_calls.append(
                        {"tool": "AdvisorAgent", "version": version_label, "loop": loop_label},
                    )
                    tool_results.append(
                        {
                            "tool": "AdvisorAgent",
                            "status": "completed",
                            "version": version_label,
                            "loop": loop_label,
                            "context_document_count": len(context_docs),
                        },
                    )
                except Exception as exc:
                    errors.append(f"advisor_revision_error:{loop_label}: {exc}")

            # ── Evaluator (structured verdict) ──────────────────────────
            if evaluator_cls is not None:
                try:
                    evaluator = evaluator_cls()
                    advisor_v1 = shared_memory.get_advisor_report("v1")
                    advisor_latest = shared_memory.get_advisor_report()
                    critic_arg = shared_memory.get_critic_argument()

                    verdict_result = evaluator.evaluate_structured(
                        query=query,
                        context_docs=context_docs,
                        response=advisor_v1 or advisor_report,
                        critic_issues=critic_arg.get("critique"),
                        advisor_report_v2=(
                            advisor_latest if advisor_latest != advisor_v1 else None
                        ),
                    )
                    shared_memory.set_evaluator_verdict(verdict_result)
                    artifacts["evaluator_report"] = verdict_result["evaluation_markdown"]
                    artifacts[f"evaluator_verdict_{loop_label}"] = verdict_result["verdict"]
                    workflow_steps.append(
                        f"evaluator_completed:{verdict_result['verdict']}:{loop_label}",
                    )
                    self._emit_progress(
                        f"evaluator_{loop_label}",
                        f"Evaluator: {verdict_result['verdict']} ({loop_label})",
                    )
                    tool_calls.append({"tool": "EvaluatorAgent", "loop": loop_label})
                    tool_results.append(
                        {
                            "tool": "EvaluatorAgent",
                            "status": "completed",
                            "verdict": verdict_result["verdict"],
                            "loop": loop_label,
                        },
                    )

                    # ── Check verdict ────────────────────────────────────
                    if verdict_result["verdict"] == "PASS":
                        workflow_steps.append(f"revision_passed:{loop_label}")
                        self._emit_progress("revision_passed", f"Đánh giá PASS ✓ ({loop_label})")
                        break

                    # ── Search for missing context if needed ────────────
                    if search_on_missing and verdict_result.get("missing_topics"):
                        missing = verdict_result["missing_topics"]
                        search_query = (
                            f"{query}\n{' '.join(str(t) for t in missing[:3])}"
                        )
                        search_docs = self._search_for_context(search_query)
                        if search_docs:
                            merged = self._deduplicate_documents(
                                context_docs + search_docs,
                            )
                            context_docs = merged
                            shared_memory.set_retrieval_docs(merged)
                            workflow_steps.append(
                                f"searched_missing_context:{loop_label}",
                            )
                            tool_calls.append(
                                {
                                    "tool": "SearchAgent",
                                    "loop": loop_label,
                                    "reason": "missing_topics",
                                },
                            )
                            tool_results.append(
                                {
                                    "tool": "SearchAgent",
                                    "status": "completed",
                                    "loop": loop_label,
                                    "added_docs": len(search_docs),
                                },
                            )

                except Exception as exc:
                    errors.append(f"evaluator_agent_error:{loop_label}: {exc}")

            shared_memory.increment_revision_count()
        else:
            # Loop exhausted without a PASS verdict
            workflow_steps.append(
                f"revision_limit_reached:max_loops={max_loops}",
            )

        # ── Semantic Memory: persist extracted facts (write path) ────────
        if advisor_report and is_semantic_memory_enabled():
            try:
                project_id = metadata.get("project_id")
                conversation_id = metadata.get("conversation_id")
                if project_id:
                    writer = _get_semantic_writer()
                    saved_facts = writer.extract_and_save(
                        final_report=advisor_report,
                        query=query,
                        project_id=project_id,
                        conversation_id=conversation_id,
                        context_docs=context_docs,
                    )
                    if saved_facts:
                        workflow_steps.append(
                            f"semantic_facts_persisted:{len(saved_facts)}_facts"
                        )
                        self._emit_progress(
                            "semantic_memory_write",
                            f"Persisted {len(saved_facts)} facts to semantic memory",
                        )
            except Exception as _sem_exc:
                errors.append(f"semantic_memory_write_error: {_sem_exc}")

        # ── Preference Memory: detect & persist user preferences (write path) ──
        if advisor_report and is_preference_memory_enabled():
            try:
                user_id = metadata.get("user_id")
                if user_id:
                    detected = _get_pref_writer().detect_and_save(
                        query=query,
                        report=advisor_report,
                        user_id=user_id,
                    )
                    if detected:
                        workflow_steps.append(
                            f"preference_memory_updated:{len(detected)}_prefs"
                        )
            except Exception as _pref_exc:
                errors.append(f"preference_memory_write_error: {_pref_exc}")

        return {
            "workflow_steps": workflow_steps,
            "tool_calls": tool_calls,
            "tool_results": tool_results,
            "errors": errors,
            "artifacts": artifacts,
            "advisor_report": advisor_report,
            "final_output": advisor_report or self._deep_advice_fallback(query, context_docs),
            "context_docs": context_docs,
            "coverage_score": min(
                1.0,
                len(context_docs) / max(int(self.config.get("top_k", 5)), 1),
            ),
        }

    def _build_advisor_agent(self, advisor_cls):
        try:
            return advisor_cls(context_provider=self._delegate_context_request)
        except TypeError:
            return advisor_cls()

    def _delegate_context_request(
        self,
        query: str,
        current_context_docs: list[dict[str, Any]],
        request: dict[str, Any],
    ) -> dict[str, Any]:
        missing_information = request.get("missing_information", [])
        search_queries = request.get("search_queries", [])
        if not isinstance(missing_information, list):
            missing_information = [str(missing_information)]
        if not isinstance(search_queries, list):
            search_queries = [str(search_queries)]

        focused_query_parts = [query]
        focused_query_parts.extend(str(item) for item in missing_information if str(item).strip())
        focused_query = "\n".join(focused_query_parts)

        retrieved_docs: list[dict[str, Any]] = []
        retrieval_errors: list[str] = []
        retrieval_metadata: dict[str, Any] = {}
        coverage_score = 0.0

        try:
            result = self._build_retrieval_agent().run(
                focused_query,
                {
                    "documents": current_context_docs,
                    "top_k": self.config.get("top_k", 5),
                    "retrieval_threshold": self.config.get("retrieval_threshold", 0.45),
                },
            )
            retrieved_docs.extend(result.get("context_docs", []))
            retrieval_errors.extend(result.get("errors", []))
            retrieval_metadata.update(result.get("metadata", {}))
            coverage_score = max(coverage_score, float(result.get("coverage_score", 0.0)))
        except Exception as exc:
            retrieval_errors.append(f"advisor_delegate_retrieval_error: {exc}")

        top_k = int(self.config.get("top_k", 5))
        threshold = float(self.config.get("advisor_context_threshold", self.config.get("retrieval_threshold", 0.8)))
        should_search = coverage_score < threshold or not retrieved_docs

        search_docs: list[dict[str, Any]] = []
        if should_search:
            targeted_queries = [str(item) for item in search_queries if str(item).strip()]
            if not targeted_queries:
                targeted_queries = [focused_query]
            for search_query in targeted_queries[:3]:
                focused_search_query = f"{query}\n{search_query}"
                search_docs.extend(self._search_for_context(focused_search_query))

        merged_docs = filter_documents_for_query_entity(query, self._deduplicate_documents(retrieved_docs + search_docs))[:top_k]
        coverage_score = max(coverage_score, min(1.0, len(merged_docs) / max(top_k, 1)))

        return {
            "context_docs": merged_docs,
            "coverage_score": coverage_score,
            "errors": retrieval_errors,
            "metadata": {
                **retrieval_metadata,
                "missing_information": missing_information,
                "search_queries": search_queries,
                "searched_external_context": bool(search_docs),
                "added_context_count": len(merged_docs),
            },
        }

    @staticmethod
    def _extract_issues_from_critique(critique: str) -> list[str]:
        """Extract ``- [ ] ...`` checklist items from a Critic Markdown report."""
        issues: list[str] = []
        for line in critique.splitlines():
            stripped = line.strip()
            if stripped.startswith("- [ ]"):
                issue_text = stripped[len("- [ ]"):].strip()
                if issue_text:
                    issues.append(issue_text)
        return issues

    def _graceful_advisor_fallback(
        self,
        query: str,
        context_docs: list[dict[str, Any]],
        errors: list[str],
    ) -> str:
        """Khi AdvisorAgent không khả dụng, dùng AnswerAgent để tạo câu trả lời
        từ context đã thu thập. Chỉ khi AnswerAgent cũng fail thì mới dùng
        _deep_advice_fallback (plain text) làm phương án cuối cùng."""
        self._emit_progress("graceful_fallback", "AdvisorAgent không khả dụng – dùng AnswerAgent để trả lời...")
        try:
            agent = self._build_answer_agent()
            result = agent.run(query, context_docs, {})
            if result and str(result).strip():
                return result
        except Exception as exc:
            errors.append(f"graceful_fallback_answer_agent_error: {exc}")
            logger.warning("AnswerAgent graceful fallback also failed: %s", exc)
        return self._deep_advice_fallback(query, context_docs)

    def _deep_advice_fallback(self, query: str, context_docs: list[dict[str, Any]]) -> str:
        lines = [
            "## Planner Decision",
            "Route: deep_advice",
            "",
            "The query looks like it needs the advisor pipeline, but the advisor stack is not currently runnable in this environment.",
        ]
        if context_docs:
            lines.extend(["", "## Retrieved Context Preview"])
            for index, doc in enumerate(context_docs[:3], start=1):
                text = str(doc.get("text", doc.get("content", ""))).replace("\n", " ").strip()
                lines.append(f"{index}. [{doc.get('source', f'doc-{index}')}] {text[:220]}")
        else:
            lines.extend(["", f"No grounded context was found yet for: {query}"])
        return "\n".join(lines)

    def _build_search_agent(self) -> SearchingAgent:
        from ai_integration.agent5_searcher.searching_agent import SearchingAgent
        return SearchingAgent(
            coverage_threshold=float(self.config.get("search_coverage_threshold", 0.4)),
            max_iterations=int(self.config.get("search_max_iterations", 5)),
            top_k=int(self.config.get("search_top_k", 5)),
        )
    def _build_retrieval_agent(self) -> RetrievalAgent:
        return RetrievalAgent(self.config, DEFAULT_RAW_DIR)

    def _build_answer_agent(self) -> AnswerAgent:
        return AnswerAgent()

    def _build_external_llm(self):
        try:
            module = importlib.import_module("ai_integration.models.external_llm")
            return module.ExternalLLM()
        except Exception:
            return None

    def _parse_json_response(self, raw_text: str) -> dict[str, Any]:
        text = str(raw_text).strip()
        try:
            parsed = json.loads(text)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            pass
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            parsed = json.loads(match.group(0))
            if isinstance(parsed, dict):
                return parsed
        raise ValueError("No valid JSON object found in LLM response.")

    def _normalize_plan(self, plan: dict[str, Any], route: str) -> dict[str, Any]:
        required_information = plan.get("required_information", [])
        if not isinstance(required_information, list):
            required_information = []
        required_information = [str(item) for item in required_information if str(item).strip()]

        normalized_route = str(plan.get("route", route)).strip()
        if normalized_route not in {"skip", "qa", "deep_advice"}:
            normalized_route = route

        workflow = plan.get("workflow", [])
        normalized_workflow: list[dict[str, Any]] = []
        if isinstance(workflow, list):
            for index, step in enumerate(workflow, start=1):
                if not isinstance(step, dict):
                    continue
                agent = str(step.get("agent", "")).strip()
                if not agent:
                    continue

                # Finance Q&A may need external evidence, so SearchAgent is
                # valid between local retrieval and answer generation.
                if normalized_route == "qa" and agent not in {"RetrievalAgent", "SearchAgent", "AnswerAgent"}:
                    continue

                normalized_step: dict[str, Any] = {
                    "step": int(step.get("step", index)),
                    "agent": agent,
                }
                if step.get("condition"):
                    normalized_step["condition"] = str(step["condition"])
                normalized_workflow.append(normalized_step)

        return {
            "route": normalized_route,
            "required_information": required_information,
            "workflow": normalized_workflow,
        }

    def _fallback_classification(self, query: str) -> dict[str, Any]:
        lowered = query.lower()
        finance_keywords = (
            "stock", "market", "revenue", "profit", "earnings", "financial",
            "invest", "company", "valuation", "annual report", "10-k", "risk",
            "tesla", "nvidia", "apple", "microsoft",
        )
        deep_keywords = (
            "should i", "recommend", "strategy", "strategic", "advice",
            "portfolio", "outlook", "buy or sell", "thesis", "deep analysis",
        )
        finance_hits = sum(1 for item in finance_keywords if item in lowered)
        deep_hits = sum(1 for item in deep_keywords if item in lowered)
        if finance_hits == 0 and not re.search(r"\b[A-Z]{1,5}\b", query):
            return {
                "route": "skip",
                "reason": "Fallback classifier judged the query as non-financial.",
                "confidence": 0.55,
            }
        if deep_hits > 0:
            return {
                "route": "deep_advice",
                "reason": "Fallback classifier judged the query as strategic/advisory.",
                "confidence": 0.55,
            }
        return {
            "route": "qa",
            "reason": "Fallback classifier judged the query as finance Q&A.",
            "confidence": 0.55,
        }

    def _fallback_plan(self, route: str) -> dict[str, Any]:
        if route == "skip":
            return {
                "route": "skip",
                "required_information": [],
                "workflow": [{"step": 1, "agent": "SkipAgent"}],
            }
        if route == "qa":
            return {
                "route": "qa",
                "required_information": ["relevant filings or market context", "supporting evidence for the answer"],
                "workflow": [
                    {"step": 1, "agent": "RetrievalAgent"},
                    {"step": 2, "agent": "SearchAgent", "condition": "coverage_score < 0.72"},
                    {"step": 3, "agent": "AnswerAgent"},
                ],
            }
        return {
            "route": "deep_advice",
            "required_information": [
                "recent financial performance",
                "key strategic risks",
                "management outlook",
                "supporting evidence for recommendation",
            ],
            "workflow": [
                {"step": 1, "agent": "RetrievalAgent"},
                {"step": 2, "agent": "SearchAgent", "condition": "coverage_score < 0.72"},
                {"step": 3, "agent": "AdvisorAgent"},
                {"step": 4, "agent": "CriticAgent"},
                {"step": 5, "agent": "EvaluatorAgent"},
            ],
        }

    def _load_class(self, module_name: str, class_name: str):
        try:
            module = importlib.import_module(module_name)
            return getattr(module, class_name)
        except Exception as exc:
            logger.warning(
                "Failed to load %s.%s – agent will be skipped. Reason: %s",
                module_name,
                class_name,
                exc,
            )
            return None

    def _load_config(self) -> dict[str, Any]:
        if not CONFIG_PATH.exists():
            return {"top_k": 5}
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file) or {"top_k": 5}

    def _search_for_context(self, query: str) -> list[dict[str, Any]]:
        if self._context_searcher is not None:
            try:
                return self._context_searcher(query)
            except Exception:
                return []

        try:
            module = importlib.import_module("ai_integration.tools.report_search_tool")
            report_search_tool = module.report_search_tool
            result = report_search_tool(query)
        except Exception:
            return []

        raw_docs: list[dict[str, Any]] = []
        sources = result.get("sources", [])
        texts = result.get("synthetic_results", [])
        for index, item in enumerate(texts):
            if isinstance(item, dict):
                text_content = str(item.get("text", item.get("content", ""))).strip()
                source = item.get("source") or (sources[index]["url"] if index < len(sources) else f"search_result_{index + 1}")
                page = item.get("page", 1)
            else:
                text_content = str(item).strip()
                source = sources[index]["url"] if index < len(sources) else f"search_result_{index + 1}"
                page = 1

            if text_content:
                raw_docs.append({
                    "text": text_content,
                    "source": source,
                    "page": page,
                })

        filtered_docs = filter_documents_for_query_entity(query, raw_docs)

        # Rerank to keep the context size small
        try:
            reranker_module = importlib.import_module("ai_integration.agent5_searcher.search_reranker")
            rerank_search = reranker_module.rerank_search_results
            top_k = int(self.config.get("top_k", 5))
            return rerank_search(query, filtered_docs, top_k=top_k)
        except Exception as e:
            print(f"Reranking failed in _search_for_context: {e}")
            return filtered_docs[:5]

    def _deduplicate_documents(self, documents: list[dict[str, Any]]) -> list[dict[str, Any]]:
        seen: set[tuple[str, str]] = set()
        unique: list[dict[str, Any]] = []
        for document in documents:
            text = str(document.get("text", document.get("content", ""))).strip()
            source = str(document.get("source", "unknown"))
            key = (source, text)
            if key in seen:
                continue
            seen.add(key)
            normalized = dict(document)
            normalized["text"] = text
            normalized["content"] = text
            normalized["source"] = source
            normalized["page"] = normalized.get("page", 1)
            unique.append(normalized)
        return unique


def run_agent_state(
    query: str,
    memory: dict[str, Any] | None = None,
    progress_callback=None,
    context_searcher: Callable[[str], list[dict[str, Any]]] | None = None,
) -> dict[str, Any]:
    orchestrator = PlanningOrchestrator(
        progress_callback=progress_callback,
        context_searcher=context_searcher,
    )
    return orchestrator.run(query, memory)


def run_agent(query: str, memory: dict[str, Any] | None = None) -> str:
    result = run_agent_state(query, memory)
    return str(result.get("final_output", ""))
