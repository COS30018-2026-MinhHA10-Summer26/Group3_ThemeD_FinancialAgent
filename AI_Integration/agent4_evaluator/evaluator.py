import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
from openai import OpenAI

from ai_integration.agent4_evaluator.tools import (
    evaluation_quality_tool,
    issues_resolution_tool,
    query_relevance_tool,
    response_completeness_tool,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / "backend" / ".env"
load_dotenv(dotenv_path=str(PROJECT_ROOT / ".env"))
load_dotenv(dotenv_path=str(ENV_PATH))


class EvaluatorAgent:
    """
    Evaluator Agent — the final quality gate before a response reaches the user.

    Two operating modes:
      Mode A (RAG-only): evaluates a plain LLM response against the user query
                         and retrieved context documents.
      Mode B (Full pipeline): evaluates a revised advisor report (v2) against
                              the user query AND the Critic's issues checklist.
    """

    def __init__(
        self,
        model: str = "gpt-4o-mini",
        max_tool_loops: int = 5,
        max_self_review_loops: int = 2,
    ):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(f"OPENAI_API_KEY not found in env. Checked path: {ENV_PATH}")

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.max_tool_loops = max_tool_loops
        self.max_self_review_loops = max_self_review_loops

        self.tools_schema = [
            {
                "type": "function",
                "function": {
                    "name": "query_relevance_tool",
                    "description": (
                        "Checks whether a response or report addresses the key topics "
                        "implied by the user query. Returns topic-level coverage signals."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "The original user query."},
                            "response": {"type": "string", "description": "The LLM response or advisor report to evaluate."},
                        },
                        "required": ["query", "response"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "issues_resolution_tool",
                    "description": (
                        "Parses '- [ ]' checklist items from the Critic's report and checks "
                        "whether each issue has been addressed in the revised advisor report v2."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "critic_issues_markdown": {
                                "type": "string",
                                "description": "The Critic's full report containing '## Issues to Resolve' with '- [ ]' items.",
                            },
                            "advisor_report_v2": {
                                "type": "string",
                                "description": "The revised advisor report (second version) to check against.",
                            },
                        },
                        "required": ["critic_issues_markdown", "advisor_report_v2"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "response_completeness_tool",
                    "description": (
                        "Checks whether a response contains expected structural elements: "
                        "source citations, limitations/caveats, and actionable content."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "response": {"type": "string", "description": "The response text to check."},
                        },
                        "required": ["response"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "evaluation_quality_tool",
                    "description": (
                        "Self-checks whether the evaluator's own Markdown output is complete "
                        "enough (has verdict, query satisfaction, remaining gaps, recommendation)."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "evaluation_markdown": {"type": "string", "description": "The evaluator's output to self-check."},
                        },
                        "required": ["evaluation_markdown"],
                    },
                },
            },
        ]

    def _execute_tool(self, name: str, arguments: Dict[str, Any]) -> str:
        print(f"-> Evaluator is calling tool: '{name}' with args: {arguments}")

        try:
            if name == "query_relevance_tool":
                result = query_relevance_tool(**arguments)
            elif name == "issues_resolution_tool":
                result = issues_resolution_tool(**arguments)
            elif name == "response_completeness_tool":
                result = response_completeness_tool(**arguments)
            elif name == "evaluation_quality_tool":
                result = evaluation_quality_tool(**arguments)
            else:
                result = {"error": f"Tool '{name}' is not recognized."}
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as exc:
            return json.dumps({"error": f"Error executing tool '{name}': {exc}"}, ensure_ascii=False)

    def _build_context_string(self, context_docs: List[Dict[str, Any]]) -> str:
        context_str = ""
        for i, doc in enumerate(context_docs, 1):
            source = doc.get("source", f"Doc {i}")
            text = doc.get("text", doc.get("content", ""))
            context_str += f"\n--- DOCUMENT {i} (Source: {source}) ---\n{text}\n"
        return context_str

    def _run_tool_calling(self, messages: List[Dict[str, Any]], temperature: float = 0.1) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=self.tools_schema,
            tool_choice="auto",
            temperature=temperature,
        )

        loops = 0
        while loops < self.max_tool_loops:
            response_message = response.choices[0].message
            tool_calls = response_message.tool_calls

            if not tool_calls:
                return response_message.content or "Unable to generate an evaluation."

            messages.append(response_message)
            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                tool_output = self._execute_tool(function_name, function_args)
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": tool_output,
                    }
                )

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools_schema,
                tool_choice="auto",
                temperature=temperature,
            )
            loops += 1

        return response.choices[0].message.content or "Exceeded maximum evaluator tool loops."

    def _self_review_and_revise(
        self,
        query: str,
        context_docs: List[Dict[str, Any]],
        response_text: str,
        draft_evaluation: str,
        critic_issues: Optional[str],
        advisor_report_v2: Optional[str],
    ) -> str:
        final_evaluation = draft_evaluation

        for _ in range(self.max_self_review_loops):
            quality = evaluation_quality_tool(final_evaluation)
            if quality["passes"]:
                return final_evaluation

            context_str = self._build_context_string(context_docs)
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are reviewing your own Evaluator Agent output before it is sent. "
                        "Revise the evaluation so it fully satisfies the quality checklist. "
                        "Make sure to keep all required Markdown sections: Evaluation Verdict, "
                        "Query Satisfaction, Issues Resolution Status (if applicable), "
                        "Remaining Gaps, and Recommendation. "
                        "Keep the answer in English Markdown. Do not invent facts outside the provided context. "
                        "Be precise and objective."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"User Query:\n{query}\n\n"
                        f"Context Documents:\n{context_str}\n\n"
                        f"Response Being Evaluated:\n{response_text}\n\n"
                        + (f"Critic Issues Checklist:\n{critic_issues}\n\n" if critic_issues else "")
                        + (f"Revised Advisor Report (v2):\n{advisor_report_v2}\n\n" if advisor_report_v2 else "")
                        + f"Current Evaluation Draft:\n{final_evaluation}\n\n"
                        f"Failed Self-Check:\n{json.dumps(quality, indent=2)}\n\n"
                        "Return only the revised final Markdown evaluation."
                    ),
                },
            ]

            final_evaluation = self._run_tool_calling(messages, temperature=0.1)

        return final_evaluation

    def run(
        self,
        query: str,
        context_docs: List[Dict[str, Any]],
        response: str,
        critic_issues: Optional[str] = None,
        advisor_report_v2: Optional[str] = None,
    ) -> str:
        """
        Evaluate a response before it reaches the user.

        Mode A (RAG-only):
            Pass query, context_docs, and response.
            Leave critic_issues and advisor_report_v2 as None.

        Mode B (Full pipeline):
            Pass query, context_docs, response (original advisor report v1),
            critic_issues (Critic's full report with Issues to Resolve),
            and advisor_report_v2 (revised advisor report).
        """
        context_str = self._build_context_string(context_docs)
        is_pipeline_mode = critic_issues is not None and advisor_report_v2 is not None

        # ---------- Pre-run tools via Python (same pattern as Critic) ----------
        initial_audit: Dict[str, Any] = {
            "query_relevance": query_relevance_tool(
                query, advisor_report_v2 if is_pipeline_mode else response
            ),
            "response_completeness": response_completeness_tool(
                advisor_report_v2 if is_pipeline_mode else response
            ),
        }

        if is_pipeline_mode:
            initial_audit["issues_resolution"] = issues_resolution_tool(
                critic_issues, advisor_report_v2
            )

        # ---------- Build system message ----------
        if is_pipeline_mode:
            system_message = (
                "You are an Evaluator Agent — the final quality gate in a financial analysis pipeline.\n"
                "The pipeline flow is: User Query → Advisor (report v1) → Critic (critique + issues checklist) "
                "→ Advisor (revised report v2) → YOU.\n\n"
                "Your job is to evaluate the revised advisor report (v2) and determine:\n"
                "1. Whether it adequately answers the original user query.\n"
                "2. Whether ALL issues identified by the Critic in '## Issues to Resolve' have been resolved.\n"
                "3. If unresolved issues remain, list them clearly so the pipeline can iterate.\n\n"
                "OPERATING GUIDELINES:\n"
                "- Use tool audit results provided to ground your evaluation.\n"
                "- Be objective and precise. Do not invent facts.\n"
                "- Return the evaluation in English Markdown.\n\n"
                "Required Markdown sections:\n"
                "## Evaluation Verdict\n"
                "## Query Satisfaction\n"
                "## Issues Resolution Status\n"
                "## Remaining Gaps\n"
                "## Recommendation\n"
            )
        else:
            system_message = (
                "You are an Evaluator Agent — the final quality gate before a response reaches the user.\n"
                "You are evaluating a RAG-generated response against the user's original query and "
                "the retrieved context documents.\n\n"
                "Your job is to determine:\n"
                "1. Whether the response adequately answers the user query.\n"
                "2. Whether the response is grounded in the provided context documents.\n"
                "3. Whether there are gaps or missing information the user should be aware of.\n\n"
                "OPERATING GUIDELINES:\n"
                "- Use tool audit results provided to ground your evaluation.\n"
                "- Be objective and precise. Do not invent facts.\n"
                "- Return the evaluation in English Markdown.\n\n"
                "Required Markdown sections:\n"
                "## Evaluation Verdict\n"
                "## Query Satisfaction\n"
                "## Remaining Gaps\n"
                "## Recommendation\n"
            )

        # ---------- Build user message ----------
        user_content_parts = [
            f"User Query:\n{query}\n",
            f"Document Context:\n{context_str}\n",
        ]

        if is_pipeline_mode:
            user_content_parts.extend([
                f"Original Advisor Report (v1):\n{response}\n",
                f"Critic Report (with Issues to Resolve):\n{critic_issues}\n",
                f"Revised Advisor Report (v2):\n{advisor_report_v2}\n",
            ])
        else:
            user_content_parts.append(f"RAG Response:\n{response}\n")

        user_content_parts.append(
            f"Initial Tool Audit:\n{json.dumps(initial_audit, indent=2, ensure_ascii=False)}\n\n"
            "Evaluate the response and produce the evaluation report."
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": "\n".join(user_content_parts)},
        ]

        # ---------- Generate & self-review ----------
        draft_evaluation = self._run_tool_calling(messages, temperature=0.1)
        return self._self_review_and_revise(
            query, context_docs, response, draft_evaluation, critic_issues, advisor_report_v2
        )

    def evaluate_structured(
        self,
        query: str,
        context_docs: List[Dict[str, Any]],
        response: str,
        critic_issues: Optional[str] = None,
        advisor_report_v2: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Evaluate and return a structured verdict alongside the Markdown report.

        Returns a dict with:
        - ``verdict``: ``"PASS"`` or ``"STILL INCOMPLETE"``
        - ``evaluation_markdown``: the full Markdown evaluation text
        - ``all_topics_covered``: bool from query_relevance_tool
        - ``missing_topics``: list of topics not addressed
        - ``response_complete``: bool from response_completeness_tool
        - ``missing_elements``: list of missing structural elements
        - ``all_issues_resolved``: bool from issues_resolution_tool (pipeline mode)
        - ``unresolved_issues``: list of unresolved critic issues (pipeline mode)
        """
        # Generate the full Markdown evaluation via the existing run() method
        evaluation_md = self.run(
            query, context_docs, response, critic_issues, advisor_report_v2,
        )

        # Run pre-audit tools programmatically to get boolean signals
        is_pipeline = critic_issues is not None and advisor_report_v2 is not None
        target_text = advisor_report_v2 if is_pipeline else response

        relevance = query_relevance_tool(query, target_text)
        completeness = response_completeness_tool(target_text)

        issues_resolved = True
        unresolved_issues: list[str] = []
        if is_pipeline and critic_issues:
            resolution = issues_resolution_tool(critic_issues, advisor_report_v2)
            issues_resolved = resolution["all_resolved"]
            unresolved_issues = resolution.get("unresolved", [])

        verdict_pass = (
            relevance["all_covered"]
            and completeness["passes"]
            and issues_resolved
        )

        return {
            "verdict": "PASS" if verdict_pass else "FAIL",
            "evaluation_markdown": evaluation_md,
            "all_topics_covered": relevance["all_covered"],
            "missing_topics": relevance.get("missing_topics", []),
            "response_complete": completeness["passes"],
            "missing_elements": completeness.get("missing_elements", []),
            "all_issues_resolved": issues_resolved,
            "unresolved_issues": unresolved_issues,
        }
