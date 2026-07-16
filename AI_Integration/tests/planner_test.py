from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ai_integration.agent1_planner.orchestrator import PlanningOrchestrator
from ai_integration.memory.session_memory import ShortTermMemory


class StubLLM:
    def generate_response(self, prompt: str) -> str:
        if "Classify the user's query" in prompt:
            lowered = prompt.lower()
            if "weather" in lowered or "joke" in lowered or "coffee" in lowered:
                return '{"route":"skip","reason":"Not finance.","confidence":0.98}'
            if "should i buy" in lowered:
                return '{"route":"deep_advice","reason":"Needs deeper advice.","confidence":0.92}'
            return '{"route":"qa","reason":"Finance Q&A.","confidence":0.88}'
        if "Create a JSON workflow plan" in prompt:
            if '"route": "skip"' in prompt or '"route":"skip"' in prompt:
                return '{"route":"skip","required_information":[],"workflow":[{"step":1,"agent":"SkipAgent"}]}'
            if '"route": "deep_advice"' in prompt or '"route":"deep_advice"' in prompt:
                return '{"route":"deep_advice","required_information":["recent financial performance","market risks"],"workflow":[{"step":1,"agent":"RetrievalAgent"},{"step":2,"agent":"SearchAgent","condition":"coverage_score < 0.9"},{"step":3,"agent":"AdvisorAgent"},{"step":4,"agent":"CriticAgent"},{"step":5,"agent":"EvaluatorAgent"}]}'
            return '{"route":"qa","required_information":["supporting evidence"],"workflow":[{"step":1,"agent":"RetrievalAgent"},{"step":2,"agent":"SearchAgent","condition":"coverage_score < 0.9"},{"step":3,"agent":"AnswerAgent"}]}'
        return "Unsupported prompt"


class StubPlanner(PlanningOrchestrator):
    def _build_external_llm(self):
        return StubLLM()

    def _build_retrieval_agent(self):
        class StubRetrievalAgent:
            def run(self_inner, query, memory):
                return {
                    "context_docs": [{"text": "stub context", "content": "stub context", "source": "stub"}],
                    "coverage_score": 0.4,
                    "workflow_steps": ["stub_retrieval"],
                    "tool_calls": [],
                    "tool_results": [],
                    "errors": [],
                    "metadata": {"retrieval_similarity": 0.4, "retrieval_threshold": 0.25, "final_context_count": 1, "coverage_score": 0.4},
                }
        return StubRetrievalAgent()

    def _search_for_context(self, query):
        return [{"text": "searched context", "content": "searched context", "source": "search"}]

    def _build_answer_agent(self):
        class StubAnswerAgent:
            def run(self_inner, query, context_docs, metadata=None):
                return "stub answer output"
        return StubAnswerAgent()

    def _run_deep_advice(self, query, context_docs, metadata, shared_memory):
        return {
            "workflow_steps": ["stub_deep_advice"],
            "tool_calls": [{"tool": "StubAdvisor"}],
            "tool_results": [{"tool": "StubAdvisor", "status": "completed"}],
            "errors": [],
            "artifacts": {"advisor_report": "stub advisor report", "critic_report": "stub critic", "evaluator_report": "stub evaluator"},
            "advisor_report": "stub advisor report",
            "final_output": "stub advisor report",
        }


def test_classifier_skip():
    planner = StubPlanner()
    decision = planner.classify_query("What is the weather in Sydney today?")
    assert decision["route"] == "skip"


def test_classifier_qa():
    planner = StubPlanner()
    decision = planner.classify_query("What was Tesla revenue in 2024?")
    assert decision["route"] == "qa"


def test_classifier_deep_advice():
    planner = StubPlanner()
    decision = planner.classify_query("Should I buy Tesla stock and what is the strategic outlook?")
    assert decision["route"] == "deep_advice"


def test_plan_generation():
    planner = StubPlanner()
    decision = planner.classify_query("Should I buy Tesla stock and what is the strategic outlook?")
    plan = planner.plan_query("Should I buy Tesla stock and what is the strategic outlook?", decision)
    assert plan["workflow"][0]["agent"] == "RetrievalAgent"
    assert plan["workflow"][-1]["agent"] == "EvaluatorAgent"


def test_run_skip_state():
    planner = StubPlanner()
    result = planner.run("Tell me a joke about coffee.")
    assert result["route"] == "skip"
    assert "outside the financial-analysis workflow" in result["final_output"]
    assert result["executed_agents"] == ["SkipAgent"]


def test_run_qa_state():
    planner = StubPlanner()
    result = planner.run("What was Tesla revenue in 2024?")
    assert result["route"] == "qa"
    assert result["final_output"] == "stub answer output"
    assert result["executed_agents"] == ["RetrievalAgent", "SearchAgent", "AnswerAgent"]


def test_run_deep_advice_state():
    planner = StubPlanner()
    result = planner.run("Should I buy Tesla stock and what is the strategic outlook?")
    assert result["route"] == "deep_advice"
    assert result["planned_workflow"][0]["agent"] == "RetrievalAgent"
    assert result["final_output"] == "stub advisor report"
    assert result["executed_agents"] == ["RetrievalAgent", "SearchAgent", "AdvisorAgent", "CriticAgent", "EvaluatorAgent"]


def test_advisor_context_delegate_retrieves_and_searches():
    class DelegatePlanner(PlanningOrchestrator):
        def __init__(self):
            super().__init__()
            self.config = {"top_k": 5, "advisor_context_threshold": 0.8}
            self.search_queries = []

        def _build_retrieval_agent(self):
            class StubRetrievalAgent:
                def run(self_inner, query, memory):
                    return {
                        "context_docs": [{"text": "local debt context", "content": "local debt context", "source": "local"}],
                        "coverage_score": 0.2,
                        "workflow_steps": [],
                        "tool_calls": [],
                        "tool_results": [],
                        "errors": [],
                        "metadata": {"coverage_score": 0.2},
                    }
            return StubRetrievalAgent()

        def _search_for_context(self, query):
            self.search_queries.append(query)
            return [{"text": "searched liquidity context", "content": "searched liquidity context", "source": "search"}]

    planner = DelegatePlanner()
    result = planner._delegate_context_request(
        "Should I buy Tesla?",
        [{"text": "existing context", "content": "existing context", "source": "existing"}],
        {
            "missing_information": ["short-term debt", "cash runway"],
            "search_queries": ["Tesla 2024 short-term debt 10-K"],
            "reason": "Risk analysis needs balance-sheet evidence.",
        },
    )

    assert result["coverage_score"] == 0.4
    assert result["metadata"]["searched_external_context"] is True
    assert planner.search_queries == ["Tesla 2024 short-term debt 10-K"]
    assert [doc["source"] for doc in result["context_docs"]] == ["local", "search"]


def test_deep_advice_uses_advisor_delegated_context():
    class DelegatingAdvisor:
        def __init__(self, context_provider=None):
            self.context_provider = context_provider
            self.current_context_docs = []
            self.delegated_context_events = []

        def run(self, query, context_docs):
            result = self.context_provider(
                query,
                context_docs,
                {
                    "missing_information": ["management outlook"],
                    "search_queries": ["Tesla management outlook annual report"],
                    "reason": "Need outlook evidence.",
                },
            )
            self.current_context_docs = context_docs + result["context_docs"]
            self.delegated_context_events.append({"added_document_count": len(result["context_docs"])})
            return "advisor report with delegated context"

    class DelegatePlanner(PlanningOrchestrator):
        def _load_class(self, module_name, class_name):
            if class_name == "AdvisorAgent":
                return DelegatingAdvisor
            return None

        def _build_retrieval_agent(self):
            class StubRetrievalAgent:
                def run(self_inner, query, memory):
                    return {
                        "context_docs": [{"text": "outlook context", "content": "outlook context", "source": "retrieved"}],
                        "coverage_score": 1.0,
                        "workflow_steps": [],
                        "tool_calls": [],
                        "tool_results": [],
                        "errors": [],
                        "metadata": {},
                    }
            return StubRetrievalAgent()

    planner = DelegatePlanner()
    result = planner._run_deep_advice(
        "Should I buy Tesla?",
        [{"text": "existing context", "content": "existing context", "source": "existing"}],
        {},
        shared_memory=ShortTermMemory(),
    )

    assert result["final_output"] == "advisor report with delegated context"
    assert result["artifacts"]["advisor_context_events"] == [{"added_document_count": 1}]
    assert [doc["source"] for doc in result["context_docs"]] == ["existing", "retrieved"]


if __name__ == "__main__":
    test_classifier_skip()
    test_classifier_qa()
    test_classifier_deep_advice()
    test_plan_generation()
    test_run_skip_state()
    test_run_qa_state()
    test_run_deep_advice_state()
    test_advisor_context_delegate_retrieves_and_searches()
    test_deep_advice_uses_advisor_delegated_context()
