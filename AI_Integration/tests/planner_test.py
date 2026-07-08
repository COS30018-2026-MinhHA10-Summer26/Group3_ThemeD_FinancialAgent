from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ai_integration.agent1_planner.orchestrator import PlanningOrchestrator


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


if __name__ == "__main__":
    test_classifier_skip()
    test_classifier_qa()
    test_classifier_deep_advice()
    test_plan_generation()
    test_run_skip_state()
    test_run_qa_state()
    test_run_deep_advice_state()
