import json
import os
from pathlib import Path
from typing import Any, Dict, List

from dotenv import load_dotenv
from openai import OpenAI

from ai_integration.agent3_critic.tools import (
    critique_quality_tool,
    evidence_consistency_tool,
    figure_audit_tool,
    report_coverage_tool,
    risk_gap_tool,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / "backend" / ".env"
load_dotenv(dotenv_path=str(PROJECT_ROOT / ".env"))
load_dotenv(dotenv_path=str(ENV_PATH))


class CriticAgent:
    """
    Critic Agent that reviews an Advisor Agent report from investor and
    competitor perspectives.

    The agent first uses review tools to gather audit signals, then writes a
    Markdown critique, then runs a self-review loop before returning the final
    answer.
    """

    def __init__(self, model: str = "gpt-4o-mini", max_tool_loops: int = 5, max_self_review_loops: int = 2):
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
                    "name": "report_coverage_tool",
                    "description": "Checks whether the advisor report covers the user's requested financial health, future outlook, advice, risks, and evidence dimensions.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string"},
                            "advisor_report": {"type": "string"},
                        },
                        "required": ["query", "advisor_report"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "evidence_consistency_tool",
                    "description": "Flags numbers in the advisor report that may not be supported by the provided context documents.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "advisor_report": {"type": "string"},
                            "context_docs": {
                                "type": "array",
                                "items": {"type": "object"},
                            },
                        },
                        "required": ["advisor_report", "context_docs"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "risk_gap_tool",
                    "description": "Finds risk themes visible in context documents that the advisor report may have missed.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "advisor_report": {"type": "string"},
                            "context_docs": {
                                "type": "array",
                                "items": {"type": "object"},
                            },
                        },
                        "required": ["advisor_report", "context_docs"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "critique_quality_tool",
                    "description": "Self-checks whether a critique has a verdict, logic gaps, investor lens, competitor lens, actionable revisions, and evidence discussion.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "critique_markdown": {"type": "string"},
                        },
                        "required": ["critique_markdown"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "figure_audit_tool",
                    "description": "Audits advisor report figures for Supabase image links, advisor_figure storage folder, captions/source notes, basic metadata consistency, and visualization quality issues.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "advisor_report": {"type": "string"},
                            "context_docs": {
                                "type": "array",
                                "items": {"type": "object"},
                            },
                            "figure_metadata": {
                                "type": "array",
                                "items": {"type": "object"},
                                "description": "Optional metadata returned by advisor figure_generation_tool.",
                            },
                        },
                        "required": ["advisor_report", "context_docs"],
                    },
                },
            },
        ]

    def _execute_tool(self, name: str, arguments: Dict[str, Any]) -> str:
        print(f"-> Critic is calling tool: '{name}' with args: {arguments}")

        try:
            if name == "report_coverage_tool":
                result = report_coverage_tool(**arguments)
            elif name == "evidence_consistency_tool":
                result = evidence_consistency_tool(**arguments)
            elif name == "risk_gap_tool":
                result = risk_gap_tool(**arguments)
            elif name == "critique_quality_tool":
                result = critique_quality_tool(**arguments)
            elif name == "figure_audit_tool":
                result = figure_audit_tool(**arguments)
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
                return response_message.content or "Unable to generate a critique."

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

        return response.choices[0].message.content or "Exceeded maximum critic tool loops."

    def _self_review_and_revise(
        self,
        query: str,
        context_docs: List[Dict[str, Any]],
        advisor_report: str,
        draft_critique: str,
    ) -> str:
        final_critique = draft_critique

        for _ in range(self.max_self_review_loops):
            quality = critique_quality_tool(final_critique)
            if quality["passes"]:
                return final_critique

            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are reviewing your own Critic Agent output before it is sent. "
                        "Revise the critique so it fully satisfies the quality checklist. "
                        "Keep the answer in English Markdown. Do not invent facts outside the provided context. "
                        "Be direct, investor-minded, and competitor-minded."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"User Query:\n{query}\n\n"
                        f"Context Documents:\n{self._build_context_string(context_docs)}\n\n"
                        f"Advisor Report Being Critiqued:\n{advisor_report}\n\n"
                        f"Current Critique Draft:\n{final_critique}\n\n"
                        f"Failed Self-Check:\n{json.dumps(quality, indent=2)}\n\n"
                        "Return only the revised final Markdown critique."
                    ),
                },
            ]

            final_critique = self._run_tool_calling(messages, temperature=0.1)

        return final_critique

    def run(self, query: str, context_docs: List[Dict[str, Any]], advisor_report: str) -> str:
        """
        Reviews the advisor report and returns a final English Markdown critique.
        """
        context_str = self._build_context_string(context_docs)
        initial_tool_audit = {
            "report_coverage": report_coverage_tool(query, advisor_report),
            "evidence_consistency": evidence_consistency_tool(advisor_report, context_docs),
            "risk_gaps": risk_gap_tool(advisor_report, context_docs),
            "figure_audit": figure_audit_tool(advisor_report, context_docs),
        }

        system_message = (
            "You are a Critic Agent for financial and strategic business reports.\n"
            "Your job is to challenge an Advisor Agent's report from two perspectives:\n"
            "1. A skeptical investor deciding whether the report is decision-grade.\n"
            "2. A serious competitor looking for weak assumptions and strategic blind spots.\n\n"
            "OPERATING GUIDELINES:\n"
            "- Always use the available tools before producing the first critique.\n"
            "- Focus on logic gaps, unsupported claims, missing risks, and weak recommendations.\n"
            "- Do not rewrite the advisor report. Give feedback that helps the advisor revise it.\n"
            "- Distinguish between 'not supported by context' and 'likely false'.\n"
            "- Return the critique in English Markdown.\n\n"
            "Required Markdown sections:\n"
            "## Overall Verdict\n"
            "## Major Logic Gaps\n"
            "## Unsupported or Weakly Supported Claims\n"
            "## Missing Investor Risks\n"
            "## Figure and Visualization Issues\n"
            "## Competitor Counterarguments\n"
            "## Revision Priorities\n"
        )

        messages = [
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": (
                    f"User Query:\n{query}\n\n"
                    f"Document Context:\n{context_str}\n\n"
                    f"Advisor Report:\n{advisor_report}\n\n"
                    f"Initial Tool Audit:\n{json.dumps(initial_tool_audit, indent=2, ensure_ascii=False)}\n\n"
                    "Audit the report and produce the critique."
                ),
            },
        ]

        draft_critique = self._run_tool_calling(messages, temperature=0.1)
        return self._self_review_and_revise(query, context_docs, advisor_report, draft_critique)
