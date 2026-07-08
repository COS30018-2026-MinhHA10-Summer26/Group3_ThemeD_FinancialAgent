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
from pathlib import Path
import re
from typing import Any

import yaml

from ai_integration.agent1_planner.answer_agent import AnswerAgent
from ai_integration.agent1_planner.retrieval_agent import RetrievalAgent
from ai_integration.memory.session_memory import ShortTermMemory


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
      "condition": "coverage_score < 0.9"
    }
  ]
}
"""


class PlanningOrchestrator:
    """Classifier + planner + executor for the financial agent stack."""

    def __init__(self) -> None:
        self.config = self._load_config()

    def run(self, query: str, memory: dict[str, Any] | None = None) -> dict[str, Any]:
        memory = dict(memory or {})
        workflow_steps: list[str] = ["input_processed"]
        errors: list[str] = []
        metadata = dict(memory.get("metadata", {}))

        cleaned_query = query.strip()
        decision = self.classify_query(cleaned_query)
        workflow_steps.append(f"classified:{decision['route']}")
        plan = self.plan_query(cleaned_query, decision)
        workflow_steps.append("planned_workflow")

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
        for step in workflow:
            agent_name = str(step.get("agent", "")).strip()
            if not agent_name:
                continue
            if not self._should_execute_step(step, state):
                state["workflow_steps"].append(f"skipped:{agent_name}")
                continue
            state["executed_agents"].append(agent_name)
            state["workflow_steps"].append(f"agent_started:{agent_name}")
            self._execute_agent_step(agent_name, state, memory)
            state["workflow_steps"].append(f"agent_completed:{agent_name}")
            if agent_name == "SkipAgent":
                break

    def _should_execute_step(self, step: dict[str, Any], state: dict[str, Any]) -> bool:
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

        # Sync to shared memory
        shared_memory: ShortTermMemory = state["shared_memory"]
        shared_memory.set_retrieval_docs(state["context_docs"])

    def _run_search_agent(self, state: dict[str, Any]) -> None:
        search_docs = self._search_for_context(state["cleaned_query"])
        merged_docs = self._deduplicate_documents(state.get("context_docs", []) + search_docs)
        state["context_docs"] = merged_docs
        top_k = int(self.config.get("top_k", 5))
        state["coverage_score"] = max(float(state.get("coverage_score", 0.0)), min(1.0, len(merged_docs) / max(top_k, 1)))
        state["tool_calls"].append({"tool": "SearchAgent"})
        state["tool_results"].append({"tool": "SearchAgent", "document_count": len(search_docs)})
        state["metadata"]["final_context_count"] = len(merged_docs)
        state["metadata"]["coverage_score"] = state["coverage_score"]
        state["workflow_steps"].append("searched_external_context")

        # Sync to shared memory
        shared_memory: ShortTermMemory = state["shared_memory"]
        shared_memory.append_retrieval_docs(search_docs)

    def _run_answer_agent(self, state: dict[str, Any]) -> None:
        agent = self._build_answer_agent()
        response = agent.run(state["cleaned_query"], state.get("context_docs", []), state.get("metadata", {}))
        state["response"] = response
        state["final_output"] = response
        state["messages"].append({"role": "assistant", "content": response})
        state["tool_calls"].append({"tool": "AnswerAgent"})
        state["tool_results"].append({"tool": "AnswerAgent", "status": "completed"})

    def _run_advisor_agent(self, state: dict[str, Any]) -> None:
        shared_memory: ShortTermMemory = state["shared_memory"]
        result = self._run_deep_advice(
            state["cleaned_query"],
            state.get("context_docs", []),
            state.get("metadata", {}),
            shared_memory,
        )
        state["tool_calls"].extend(result["tool_calls"])
        state["tool_results"].extend(result["tool_results"])
        state["workflow_steps"].extend(result["workflow_steps"])
        state["errors"].extend(result["errors"])
        state["artifacts"].update(result["artifacts"])
        state["report"] = result.get("advisor_report")
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
        if state["artifacts"].get("evaluator_report"):
            state["tool_calls"].append({"tool": "EvaluatorAgent"})
            state["tool_results"].append({"tool": "EvaluatorAgent", "status": "completed"})
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
    ) -> dict[str, Any]:
        workflow_steps: list[str] = []
        tool_calls: list[dict[str, Any]] = []
        tool_results: list[dict[str, Any]] = []
        errors: list[str] = []
        artifacts: dict[str, Any] = {}

        advisor_report = None
        critic_report = None
        evaluator_report = None

        advisor_cls = self._load_class("ai_integration.agent2_advisor.advisor", "AdvisorAgent")
        critic_cls = self._load_class("ai_integration.agent3_critic.critic", "CriticAgent")
        evaluator_cls = self._load_class("ai_integration.agent4_evaluator.evaluator", "EvaluatorAgent")

        if advisor_cls is None:
            final_output = self._deep_advice_fallback(query, context_docs)
            errors.append("advisor_agent_unavailable")
            return {
                "workflow_steps": workflow_steps,
                "tool_calls": tool_calls,
                "tool_results": tool_results,
                "errors": errors,
                "artifacts": artifacts,
                "advisor_report": None,
                "final_output": final_output,
            }

        # --- Advisor (v1) ---
        try:
            advisor = advisor_cls()
            advisor_report = advisor.run(query, context_docs)
            workflow_steps.append("advisor_completed")
            tool_calls.append({"tool": "AdvisorAgent"})
            tool_results.append({"tool": "AdvisorAgent", "status": "completed"})
            artifacts["advisor_report"] = advisor_report
            shared_memory.set_advisor_report(advisor_report, version_label="v1")
        except Exception as exc:
            errors.append(f"advisor_agent_error: {exc}")
            final_output = self._deep_advice_fallback(query, context_docs)
            return {
                "workflow_steps": workflow_steps,
                "tool_calls": tool_calls,
                "tool_results": tool_results,
                "errors": errors,
                "artifacts": artifacts,
                "advisor_report": advisor_report,
                "final_output": final_output,
            }

        # --- Critic ---
        if critic_cls is not None:
            try:
                critic = critic_cls()
                critic_report = critic.run(query, context_docs, advisor_report)
                workflow_steps.append("critic_completed")
                tool_calls.append({"tool": "CriticAgent"})
                tool_results.append({"tool": "CriticAgent", "status": "completed"})
                artifacts["critic_report"] = critic_report
                shared_memory.set_critic_argument(
                    critique=critic_report,
                    issues=self._extract_issues_from_critique(critic_report),
                )
            except Exception as exc:
                errors.append(f"critic_agent_error: {exc}")

        # --- Evaluator (reads from shared memory) ---
        if evaluator_cls is not None:
            try:
                evaluator = evaluator_cls()
                critic_arg = shared_memory.get_critic_argument()
                advisor_latest = shared_memory.get_advisor_report()  # latest version
                advisor_v1 = shared_memory.get_advisor_report("v1")
                evaluator_report = evaluator.run(
                    query,
                    context_docs,
                    response=advisor_v1 or advisor_report,
                    critic_issues=critic_arg.get("critique"),
                    advisor_report_v2=advisor_latest if advisor_latest != advisor_v1 else None,
                )
                workflow_steps.append("evaluator_completed")
                tool_calls.append({"tool": "EvaluatorAgent"})
                tool_results.append({"tool": "EvaluatorAgent", "status": "completed"})
                artifacts["evaluator_report"] = evaluator_report
            except Exception as exc:
                errors.append(f"evaluator_agent_error: {exc}")

        return {
            "workflow_steps": workflow_steps,
            "tool_calls": tool_calls,
            "tool_results": tool_results,
            "errors": errors,
            "artifacts": artifacts,
            "advisor_report": advisor_report,
            "final_output": advisor_report or self._deep_advice_fallback(query, context_docs),
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

        workflow = plan.get("workflow", [])
        normalized_workflow: list[dict[str, Any]] = []
        if isinstance(workflow, list):
            for index, step in enumerate(workflow, start=1):
                if not isinstance(step, dict):
                    continue
                agent = str(step.get("agent", "")).strip()
                if not agent:
                    continue
                normalized_step: dict[str, Any] = {
                    "step": int(step.get("step", index)),
                    "agent": agent,
                }
                if step.get("condition"):
                    normalized_step["condition"] = str(step["condition"])
                normalized_workflow.append(normalized_step)

        normalized_route = str(plan.get("route", route)).strip()
        if normalized_route not in {"skip", "qa", "deep_advice"}:
            normalized_route = route

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
                    {"step": 2, "agent": "SearchAgent", "condition": "coverage_score < 0.9"},
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
                {"step": 2, "agent": "SearchAgent", "condition": "coverage_score < 0.9"},
                {"step": 3, "agent": "AdvisorAgent"},
                {"step": 4, "agent": "CriticAgent"},
                {"step": 5, "agent": "EvaluatorAgent"},
            ],
        }

    def _load_class(self, module_name: str, class_name: str):
        try:
            module = importlib.import_module(module_name)
            return getattr(module, class_name)
        except Exception:
            return None

    def _load_config(self) -> dict[str, Any]:
        if not CONFIG_PATH.exists():
            return {"top_k": 5}
        with CONFIG_PATH.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file) or {"top_k": 5}

    def _search_for_context(self, query: str) -> list[dict[str, Any]]:
        try:
            module = importlib.import_module("ai_integration.tools.report_search_tool")
            report_search_tool = module.report_search_tool
            result = report_search_tool(query)
        except Exception:
            return []

        docs: list[dict[str, Any]] = []
        sources = result.get("sources", [])
        texts = result.get("synthetic_results", [])
        for index, text in enumerate(texts):
            source = sources[index]["url"] if index < len(sources) else f"search_result_{index + 1}"
            docs.append(
                {
                    "text": str(text)[:4000],
                    "content": str(text)[:4000],
                    "source": source,
                    "page": 1,
                    "score": 0.0,
                }
            )
        return docs

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


def run_agent_state(query: str, memory: dict[str, Any] | None = None) -> dict[str, Any]:
    orchestrator = PlanningOrchestrator()
    return orchestrator.run(query, memory)


def run_agent(query: str, memory: dict[str, Any] | None = None) -> str:
    result = run_agent_state(query, memory)
    return str(result.get("final_output", ""))
