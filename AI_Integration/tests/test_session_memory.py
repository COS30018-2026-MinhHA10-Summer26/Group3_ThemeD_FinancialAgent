"""
Unit tests for ShortTermMemory and its integration with PlanningOrchestrator.
"""

from __future__ import annotations

import re
from typing import Any

import pytest

from ai_integration.memory.session_memory import ShortTermMemory


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

ISO_8601_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")

SAMPLE_DOCS: list[dict[str, Any]] = [
    {"text": "Tesla revenue was $81.5B in 2022.", "source": "10-K", "page": 1, "score": 0.92},
    {"text": "Operating margin improved to 16.8%.", "source": "10-K", "page": 5, "score": 0.88},
]

SEARCH_DOCS: list[dict[str, Any]] = [
    {"text": "Tesla announced Cybertruck deliveries.", "source": "reuters.com", "page": 1, "score": 0.0},
]


# ---------------------------------------------------------------------------
# 1. Initialisation
# ---------------------------------------------------------------------------

class TestInitialisation:
    def test_empty_memory(self) -> None:
        mem = ShortTermMemory()
        assert mem.get_context() == {}
        assert mem.get_retrieval_docs() == []
        assert mem.get_advisor_report() is None
        assert mem.get_advisor_report("v1") is None
        assert mem.get_critic_argument() == {"critique": None, "issues": []}


# ---------------------------------------------------------------------------
# 2. Context compartment
# ---------------------------------------------------------------------------

class TestContextCompartment:
    def test_set_and_get_context(self) -> None:
        mem = ShortTermMemory()
        mem.set_context(query="Analyze Tesla", route="deep_advice", metadata={"year": 2022}, plan={"workflow": []})
        ctx = mem.get_context()
        assert ctx["query"] == "Analyze Tesla"
        assert ctx["route"] == "deep_advice"
        assert ctx["metadata"] == {"year": 2022}
        assert ctx["plan"] == {"workflow": []}

    def test_context_defaults_to_empty_dicts(self) -> None:
        mem = ShortTermMemory()
        mem.set_context(query="q", route="qa")
        ctx = mem.get_context()
        assert ctx["metadata"] == {}
        assert ctx["plan"] == {}

    def test_context_returns_copy(self) -> None:
        mem = ShortTermMemory()
        mem.set_context(query="q", route="qa")
        ctx = mem.get_context()
        ctx["query"] = "MUTATED"
        assert mem.get_context()["query"] == "q"

    def test_context_has_timestamp(self) -> None:
        mem = ShortTermMemory()
        mem.set_context(query="q", route="qa")
        snap = mem.snapshot()
        assert snap["context"]["updated_at"] is not None
        assert ISO_8601_PATTERN.match(snap["context"]["updated_at"])


# ---------------------------------------------------------------------------
# 3. Retrieval docs compartment
# ---------------------------------------------------------------------------

class TestRetrievalDocsCompartment:
    def test_set_retrieval_docs(self) -> None:
        mem = ShortTermMemory()
        mem.set_retrieval_docs(SAMPLE_DOCS)
        assert len(mem.get_retrieval_docs()) == 2

    def test_append_retrieval_docs(self) -> None:
        mem = ShortTermMemory()
        mem.set_retrieval_docs(SAMPLE_DOCS)
        mem.append_retrieval_docs(SEARCH_DOCS)
        assert len(mem.get_retrieval_docs()) == 3

    def test_returns_copy(self) -> None:
        mem = ShortTermMemory()
        mem.set_retrieval_docs(SAMPLE_DOCS)
        docs = mem.get_retrieval_docs()
        docs.clear()
        assert len(mem.get_retrieval_docs()) == 2

    def test_timestamp_updated(self) -> None:
        mem = ShortTermMemory()
        mem.set_retrieval_docs(SAMPLE_DOCS)
        snap = mem.snapshot()
        assert snap["retrieval_docs"]["updated_at"] is not None
        assert snap["retrieval_docs"]["count"] == 2


# ---------------------------------------------------------------------------
# 4. Advisor report compartment (v1 + latest)
# ---------------------------------------------------------------------------

class TestAdvisorReportCompartment:
    def test_set_v1(self) -> None:
        mem = ShortTermMemory()
        mem.set_advisor_report("Report v1 content", version_label="v1")
        assert mem.get_advisor_report("v1") == "Report v1 content"
        assert mem.get_advisor_report() == "Report v1 content"  # latest == v1

    def test_set_v2_preserves_v1(self) -> None:
        mem = ShortTermMemory()
        mem.set_advisor_report("Report v1", version_label="v1")
        mem.set_advisor_report("Report v2", version_label="v2")
        assert mem.get_advisor_report("v1") == "Report v1"
        assert mem.get_advisor_report() == "Report v2"  # latest == v2

    def test_default_version_is_latest(self) -> None:
        mem = ShortTermMemory()
        mem.set_advisor_report("First", version_label="v1")
        mem.set_advisor_report("Second", version_label="v2")
        assert mem.get_advisor_report(None) == "Second"
        assert mem.get_advisor_report() == "Second"

    def test_timestamps(self) -> None:
        mem = ShortTermMemory()
        mem.set_advisor_report("R1", version_label="v1")
        snap = mem.snapshot()
        assert snap["advisor_report"]["v1_updated_at"] is not None
        assert snap["advisor_report"]["latest_updated_at"] is not None


# ---------------------------------------------------------------------------
# 5. Critic argument compartment
# ---------------------------------------------------------------------------

class TestCriticArgumentCompartment:
    def test_set_and_get(self) -> None:
        mem = ShortTermMemory()
        mem.set_critic_argument(critique="The report has gaps.", issues=["Missing risk analysis", "No citations"])
        arg = mem.get_critic_argument()
        assert arg["critique"] == "The report has gaps."
        assert arg["issues"] == ["Missing risk analysis", "No citations"]

    def test_default_empty_issues(self) -> None:
        mem = ShortTermMemory()
        mem.set_critic_argument(critique="OK")
        assert mem.get_critic_argument()["issues"] == []

    def test_timestamp(self) -> None:
        mem = ShortTermMemory()
        mem.set_critic_argument(critique="C", issues=["I1"])
        snap = mem.snapshot()
        assert snap["critic_argument"]["updated_at"] is not None


# ---------------------------------------------------------------------------
# 6. Snapshot
# ---------------------------------------------------------------------------

class TestSnapshot:
    def test_snapshot_complete_structure(self) -> None:
        mem = ShortTermMemory()
        mem.set_context(query="q", route="deep_advice")
        mem.set_retrieval_docs(SAMPLE_DOCS)
        mem.set_advisor_report("R1", "v1")
        mem.set_critic_argument(critique="C1", issues=["I1"])
        snap = mem.snapshot()

        assert "context" in snap
        assert "retrieval_docs" in snap
        assert "advisor_report" in snap
        assert "critic_argument" in snap

        assert snap["context"]["data"]["query"] == "q"
        assert snap["retrieval_docs"]["count"] == 2
        assert snap["advisor_report"]["v1"] == "R1"
        assert snap["advisor_report"]["latest"] == "R1"
        assert snap["critic_argument"]["critique"] == "C1"
        assert snap["critic_argument"]["issues"] == ["I1"]

    def test_snapshot_empty_memory(self) -> None:
        mem = ShortTermMemory()
        snap = mem.snapshot()
        assert snap["context"]["data"] == {}
        assert snap["context"]["updated_at"] is None
        assert snap["retrieval_docs"]["count"] == 0
        assert snap["advisor_report"]["v1"] is None
        assert snap["advisor_report"]["latest"] is None
        assert snap["critic_argument"]["critique"] is None


# ---------------------------------------------------------------------------
# 7. Orchestrator _extract_issues_from_critique
# ---------------------------------------------------------------------------

class TestExtractIssuesFromCritique:
    def test_extract_checklist(self) -> None:
        from ai_integration.agent1_planner.orchestrator import PlanningOrchestrator

        critique = (
            "## Issues to Resolve\n"
            "- [ ] Missing debt-to-equity ratio\n"
            "- [ ] No source citation for revenue figure\n"
            "- [x] Already resolved item\n"
            "- [ ] Weak competitive analysis\n"
            "Some trailing text.\n"
        )
        issues = PlanningOrchestrator._extract_issues_from_critique(critique)
        assert issues == [
            "Missing debt-to-equity ratio",
            "No source citation for revenue figure",
            "Weak competitive analysis",
        ]

    def test_no_issues(self) -> None:
        from ai_integration.agent1_planner.orchestrator import PlanningOrchestrator

        critique = "## Overall Verdict\nThe report is good."
        issues = PlanningOrchestrator._extract_issues_from_critique(critique)
        assert issues == []
