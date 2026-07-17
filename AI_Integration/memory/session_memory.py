"""
Short-term shared memory for the multi-agent pipeline.

This module provides a per-request memory store with four compartments that
agents in the ``deep_advice`` pipeline read and write during a single
request lifecycle.  The memory instance lives in RAM and is discarded after
the request completes.

Compartments
------------
- **context**:         Query, route, metadata, plan — set once by the orchestrator.
- **retrieval_docs**:  Documents gathered by RetrievalAgent / SearchAgent.
- **advisor_report**:  Advisor analysis output (keeps *v1* + *latest*).
- **critic_argument**: Critic feedback and issues checklist.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


class ShortTermMemory:
    """Per-request shared memory with four compartments.

    Design decisions
    ~~~~~~~~~~~~~~~~
    * **Not thread-safe** — the pipeline runs sequentially; no lock needed.
    * **Pure Python** — no Redis / DB dependency; lives in RAM for one request.
    * ``advisor_report`` stores the original *v1* and a *latest* pointer so
      downstream agents can compare versions when the advisor revises.
    * Every write records an ISO-8601 UTC timestamp for audit / debug.
    """

    # ------------------------------------------------------------------
    # Initialisation
    # ------------------------------------------------------------------

    def __init__(self) -> None:
        # Context compartment
        self._context: dict[str, Any] = {}
        self._context_updated_at: str | None = None

        # Retrieval docs compartment
        self._retrieval_docs: list[dict[str, Any]] = []
        self._retrieval_docs_updated_at: str | None = None

        # Advisor report compartment (v1 + latest)
        self._advisor_report_v1: str | None = None
        self._advisor_report_v1_updated_at: str | None = None
        self._advisor_report_latest: str | None = None
        self._advisor_report_latest_updated_at: str | None = None

        # Critic argument compartment
        self._critic_critique: str | None = None
        self._critic_issues: list[str] = []
        self._critic_argument_updated_at: str | None = None

        # Evaluator verdict compartment
        self._evaluator_verdict: dict[str, Any] = {}
        self._evaluator_verdict_updated_at: str | None = None

        # Revision loop tracking
        self._revision_count: int = 0

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _now() -> str:
        """Return the current UTC time as an ISO-8601 string."""
        return datetime.now(timezone.utc).isoformat()

    # ------------------------------------------------------------------
    # Context compartment
    # ------------------------------------------------------------------

    def set_context(
        self,
        query: str,
        route: str,
        metadata: dict[str, Any] | None = None,
        plan: dict[str, Any] | None = None,
    ) -> None:
        """Write the request context.  Called once by the orchestrator."""
        self._context = {
            "query": query,
            "route": route,
            "metadata": dict(metadata or {}),
            "plan": dict(plan or {}),
        }
        self._context_updated_at = self._now()

    def get_context(self) -> dict[str, Any]:
        """Return the full context dict (empty dict if never set)."""
        return dict(self._context)

    # ------------------------------------------------------------------
    # Retrieval docs compartment
    # ------------------------------------------------------------------

    def set_retrieval_docs(self, docs: list[dict[str, Any]]) -> None:
        """Replace the retrieval docs list (typically by RetrievalAgent)."""
        self._retrieval_docs = list(docs)
        self._retrieval_docs_updated_at = self._now()

    def append_retrieval_docs(self, docs: list[dict[str, Any]]) -> None:
        """Merge additional docs (typically by SearchAgent)."""
        self._retrieval_docs.extend(docs)
        self._retrieval_docs_updated_at = self._now()

    def get_retrieval_docs(self) -> list[dict[str, Any]]:
        """Return the current retrieval docs list."""
        return list(self._retrieval_docs)

    # ------------------------------------------------------------------
    # Advisor report compartment  (v1 + latest)
    # ------------------------------------------------------------------

    def set_advisor_report(self, report: str, version_label: str = "v1") -> None:
        """Store an advisor report.

        Parameters
        ----------
        report:
            The Markdown report text.
        version_label:
            ``"v1"`` for the first version.  Any other label (e.g. ``"v2"``)
            only updates *latest* without overwriting *v1*.
        """
        now = self._now()
        if version_label == "v1":
            self._advisor_report_v1 = report
            self._advisor_report_v1_updated_at = now
        self._advisor_report_latest = report
        self._advisor_report_latest_updated_at = now

    def get_advisor_report(self, version: str | None = None) -> str | None:
        """Return an advisor report.

        Parameters
        ----------
        version:
            ``"v1"`` to get the original version.  ``None`` (default) returns
            the latest version.
        """
        if version == "v1":
            return self._advisor_report_v1
        return self._advisor_report_latest

    # ------------------------------------------------------------------
    # Critic argument compartment
    # ------------------------------------------------------------------

    def set_critic_argument(self, critique: str, issues: list[str] | None = None) -> None:
        """Store the critic's feedback.

        Parameters
        ----------
        critique:
            Full Markdown critique text.
        issues:
            List of individual issue strings extracted from the
            ``## Issues to Resolve`` section.
        """
        self._critic_critique = critique
        self._critic_issues = list(issues or [])
        self._critic_argument_updated_at = self._now()

    def get_critic_argument(self) -> dict[str, Any]:
        """Return the critic feedback as a dict with *critique* and *issues*."""
        return {
            "critique": self._critic_critique,
            "issues": list(self._critic_issues),
        }

    # ------------------------------------------------------------------
    # Evaluator verdict compartment
    # ------------------------------------------------------------------

    def set_evaluator_verdict(self, verdict: dict[str, Any]) -> None:
        """Store the evaluator's structured verdict.

        Parameters
        ----------
        verdict:
            Dict with at least ``verdict`` ("PASS"/"FAIL"), plus optional
            detail keys like ``missing_topics``, ``unresolved_issues``, etc.
        """
        self._evaluator_verdict = dict(verdict)
        self._evaluator_verdict_updated_at = self._now()

    def get_evaluator_verdict(self) -> dict[str, Any]:
        """Return the latest evaluator verdict dict (empty if never set)."""
        return dict(self._evaluator_verdict)

    # ------------------------------------------------------------------
    # Revision loop tracking
    # ------------------------------------------------------------------

    def increment_revision_count(self) -> int:
        """Increment and return the revision loop counter."""
        self._revision_count += 1
        return self._revision_count

    def get_revision_count(self) -> int:
        """Return how many revision loops have been executed."""
        return self._revision_count

    # ------------------------------------------------------------------
    # Snapshot (debug / audit)
    # ------------------------------------------------------------------

    def snapshot(self) -> dict[str, Any]:
        """Serialise the entire memory state for logging or inspection."""
        return {
            "context": {
                "data": dict(self._context),
                "updated_at": self._context_updated_at,
            },
            "retrieval_docs": {
                "count": len(self._retrieval_docs),
                "updated_at": self._retrieval_docs_updated_at,
            },
            "advisor_report": {
                "v1": self._advisor_report_v1,
                "v1_updated_at": self._advisor_report_v1_updated_at,
                "latest": self._advisor_report_latest,
                "latest_updated_at": self._advisor_report_latest_updated_at,
            },
            "critic_argument": {
                "critique": self._critic_critique,
                "issues": list(self._critic_issues),
                "updated_at": self._critic_argument_updated_at,
            },
            "evaluator_verdict": {
                "data": dict(self._evaluator_verdict),
                "updated_at": self._evaluator_verdict_updated_at,
            },
            "revision_count": self._revision_count,
        }
