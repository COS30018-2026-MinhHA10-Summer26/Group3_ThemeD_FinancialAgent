import json
import os
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
from dotenv import load_dotenv
from openai import OpenAI

# Import the tools from our local module
from ai_integration.agent2_advisor.tools import (
    comparison_tool,
    risk_assessment_tool,
    financial_calculator_tool,
    framework_template_library,
    figure_generation_tool
)

# Load environment variables
PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / "backend" / ".env"
load_dotenv(dotenv_path=str(PROJECT_ROOT / ".env"))
load_dotenv(dotenv_path=str(ENV_PATH))

ContextProvider = Callable[[str, List[Dict[str, Any]], Dict[str, Any]], Dict[str, Any]]


class AdvisorAgent:
    """
    Advisor Agent specialized in strategic business analysis and financial evaluation.
    Utilizes OpenAI's ChatCompletion API with native Tool calling.
    """
    
    def __init__(
        self,
        model: str = "gpt-4o-mini",
        max_tool_loops: int = 15,
        max_self_review_loops: int = 2,
        context_provider: ContextProvider | None = None,
    ):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(f"OPENAI_API_KEY not found in env. Checked path: {ENV_PATH}")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.max_tool_loops = max_tool_loops
        self.max_self_review_loops = max_self_review_loops
        self.context_provider = context_provider
        self.current_query = ""
        self.current_context_docs: List[Dict[str, Any]] = []
        self.delegated_context_events: List[Dict[str, Any]] = []
        
        # Define the tools schema for the OpenAI API
        self.tools_schema = [
            {
                "type": "function",
                "function": {
                    "name": "comparison_tool",
                    "description": (
                        "Compares key financial or operational metrics of two entities (companies, years, or industries) "
                        "and returns a formatted markdown table including changes. "
                        "IMPORTANT \u2014 ANTI-HALLUCINATION: Only pass numeric values that appear VERBATIM in the provided "
                        "documents or in prior tool outputs. Do NOT invent, estimate, round, or recall figures from "
                        "training knowledge to fill this tool. If an exact value is missing from the documents, omit "
                        "that metric and note its absence in the report instead of fabricating a plausible number."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "data_a": {
                                "type": "object",
                                "description": "Key-value pair metrics for Entity A. Values should be numeric for variance calculation."
                            },
                            "data_b": {
                                "type": "object",
                                "description": "Key-value pair metrics for Entity B. Values should be numeric for variance calculation."
                            },
                            "entity_a_name": {
                                "type": "string",
                                "description": "Name of Entity A (e.g. 'Tesla 2022')"
                            },
                            "entity_b_name": {
                                "type": "string",
                                "description": "Name of Entity B (e.g. 'Tesla 2021' or 'Industry Average')"
                            }
                        },
                        "required": ["data_a", "data_b", "entity_a_name", "entity_b_name"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "risk_assessment_tool",
                    "description": "Performs quantitative risk assessment calculations (Altman Z-Score for bankruptcy, debt/equity ratio, interest coverage) based on balance sheet and income statements.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "financial_metrics": {
                                "type": "object",
                                "description": "Required financial numbers. Keys: working_capital, total_assets, retained_earnings, ebit, market_cap, total_liabilities, sales. Optional: total_debt, equity, interest_expense."
                            }
                        },
                        "required": ["financial_metrics"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "financial_calculator_tool",
                    "description": "Calculates standard financial performance metrics: Break-even Point in units, ROI (Return on Investment), or CAGR (Compound Annual Growth Rate).",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "fixed_costs": {"type": "number", "description": "Fixed expenses for break-even calculation"},
                            "price_per_unit": {"type": "number", "description": "Selling price per unit"},
                            "variable_cost_per_unit": {"type": "number", "description": "Variable production cost per unit"},
                            "initial_investment": {"type": "number", "description": "Initial capital invested for ROI"},
                            "net_profit": {"type": "number", "description": "Net income generated for ROI"},
                            "beginning_value": {"type": "number", "description": "Starting value for CAGR"},
                            "ending_value": {"type": "number", "description": "Final value for CAGR"},
                            "years": {"type": "number", "description": "Number of periods for CAGR"}
                        }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "framework_template_library",
                    "description": "Retrieves the standard markdown template for business strategic frameworks: SWOT, Porter_5_Forces, PESTEL.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "framework_name": {
                                "type": "string",
                                "description": "The name of the framework. Allowed: SWOT, Porter, PESTEL."
                            }
                        },
                        "required": ["framework_name"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "figure_generation_tool",
                    "description": "Creates a report-ready figure. Bar and line charts are uploaded as PNG files to Supabase Storage under advisor_figure and return a public Markdown image link. Tables return Markdown only.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "figure_type": {
                                "type": "string",
                                "description": "Allowed values: bar_chart, line_chart, table."
                            },
                            "title": {
                                "type": "string",
                                "description": "Clear title for the figure."
                            },
                            "data": {
                                "type": "array",
                                "description": "Rows of figure data. Each row should be an object with the x_key and numeric y_keys.",
                                "items": {"type": "object"}
                            },
                            "x_key": {
                                "type": "string",
                                "description": "Column/key to use on the x-axis or first table column."
                            },
                            "y_keys": {
                                "type": "array",
                                "description": "Numeric columns/keys to plot on the y-axis.",
                                "items": {"type": "string"}
                            },
                            "x_label": {"type": "string"},
                            "y_label": {"type": "string"},
                            "caption": {
                                "type": "string",
                                "description": "Short factual caption explaining the figure."
                            },
                            "source_note": {
                                "type": "string",
                                "description": "Source note tying the figure to the provided documents or tool output."
                            }
                        },
                        "required": ["figure_type", "title", "data"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "request_additional_context",
                    "description": (
                        "Delegates to retrieval/search agents when the provided documents are missing "
                        "specific evidence needed for the analysis. Use this before drafting unsupported "
                        "claims or when the user asks for facts not present in the current context."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "missing_information": {
                                "type": "array",
                                "description": "Specific facts, metrics, filings, or disclosures missing from the current context.",
                                "items": {"type": "string"}
                            },
                            "search_queries": {
                                "type": "array",
                                "description": "Optional targeted document-oriented queries for the retrieval/search agents.",
                                "items": {"type": "string"}
                            },
                            "reason": {
                                "type": "string",
                                "description": "Why this extra context is required for the advisor report."
                            }
                        },
                        "required": ["missing_information", "reason"]
                    }
                }
            }
        ]

    def _execute_tool(self, name: str, arguments: Dict[str, Any]) -> str:
        """Executes the actual Python logic of the requested tool."""
        print(f"-> Agent is calling tool: '{name}' with args: {arguments}")
        
        try:
            if name == "comparison_tool":
                return comparison_tool(**arguments)
            
            elif name == "risk_assessment_tool":
                res = risk_assessment_tool(**arguments)
                return json.dumps(res, indent=2, ensure_ascii=False)
            
            elif name == "financial_calculator_tool":
                res = financial_calculator_tool(**arguments)
                return json.dumps(res, indent=2, ensure_ascii=False)
            
            elif name == "framework_template_library":
                return framework_template_library(**arguments)

            elif name == "figure_generation_tool":
                res = figure_generation_tool(**arguments)
                return json.dumps(res, indent=2, ensure_ascii=False)

            elif name == "request_additional_context":
                res = self._request_additional_context(arguments)
                return json.dumps(res, indent=2, ensure_ascii=False)
            
            else:
                return f"Error: Tool '{name}' is not recognized."
        except Exception as e:
            return f"Error executing tool '{name}': {str(e)}"

    def _request_additional_context(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if self.context_provider is None:
            return {
                "status": "unavailable",
                "message": "No retrieval/search delegate is configured for this AdvisorAgent.",
                "added_document_count": 0,
                "documents": [],
            }

        request_key = self._context_request_key(arguments)
        if any(self._context_request_key(event) == request_key for event in self.delegated_context_events):
            return {
                "status": "duplicate",
                "message": "This additional-context request was already attempted.",
                "added_document_count": 0,
                "documents": self._summarize_context_docs(self.current_context_docs),
            }

        result = self.context_provider(self.current_query, self.current_context_docs, arguments)
        new_docs = result.get("context_docs", [])
        if isinstance(new_docs, list):
            self.current_context_docs = self._deduplicate_documents(self.current_context_docs + new_docs)

        event = {
            "missing_information": arguments.get("missing_information", []),
            "search_queries": arguments.get("search_queries", []),
            "reason": arguments.get("reason", ""),
            "added_document_count": len(new_docs) if isinstance(new_docs, list) else 0,
            "coverage_score": result.get("coverage_score"),
            "metadata": result.get("metadata", {}),
        }
        self.delegated_context_events.append(event)

        return {
            "status": "completed",
            "added_document_count": event["added_document_count"],
            "coverage_score": event["coverage_score"],
            "documents": self._summarize_context_docs(new_docs if isinstance(new_docs, list) else []),
            "metadata": event["metadata"],
        }

    @staticmethod
    def _context_request_key(arguments: Dict[str, Any]) -> tuple[tuple[str, ...], tuple[str, ...], str]:
        missing_information = arguments.get("missing_information", [])
        search_queries = arguments.get("search_queries", [])
        reason = str(arguments.get("reason", "")).strip().lower()

        if not isinstance(missing_information, list):
            missing_information = [missing_information]
        if not isinstance(search_queries, list):
            search_queries = [search_queries]

        normalized_missing = tuple(sorted(str(item).strip().lower() for item in missing_information if str(item).strip()))
        normalized_queries = tuple(sorted(str(item).strip().lower() for item in search_queries if str(item).strip()))
        return normalized_missing, normalized_queries, reason

    def _summarize_context_docs(self, context_docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        summaries: List[Dict[str, Any]] = []
        for index, doc in enumerate(context_docs, start=1):
            text = str(doc.get("text", doc.get("content", ""))).replace("\n", " ").strip()
            summaries.append(
                {
                    "index": index,
                    "source": doc.get("source", f"Doc {index}"),
                    "page": doc.get("page", 1),
                    "score": doc.get("score"),
                    "preview": text[:700],
                }
            )
        return summaries

    def _deduplicate_documents(self, context_docs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        seen: set[tuple[str, str]] = set()
        unique: List[Dict[str, Any]] = []
        for doc in context_docs:
            text = str(doc.get("text", doc.get("content", ""))).strip()
            source = str(doc.get("source", "unknown"))
            key = (source, text)
            if key in seen:
                continue
            seen.add(key)
            normalized = dict(doc)
            normalized["text"] = text
            normalized["content"] = text
            normalized["source"] = source
            normalized["page"] = normalized.get("page", 1)
            unique.append(normalized)
        return unique

    def _build_context_string(self, context_docs: List[Dict[str, Any]]) -> str:
        context_str = ""
        for i, doc in enumerate(context_docs, 1):
            source = doc.get("source", f"Doc {i}")
            text = doc.get("text", doc.get("content", ""))
            context_str += f"\n--- DOCUMENT {i} (Source: {source}) ---\n{text}\n"
        return context_str

    def _run_tool_calling(self, messages: List[Dict[str, Any]], temperature: float = 0.2) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=self.tools_schema,
            tool_choice="auto",
            temperature=temperature
        )

        loops = 0
        while loops < self.max_tool_loops:
            response_message = response.choices[0].message
            tool_calls = response_message.tool_calls

            if not tool_calls:
                return response_message.content if response_message.content else "Unable to generate a response."

            messages.append(response_message)

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                tool_output = self._execute_tool(function_name, function_args)

                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": tool_output
                })

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=self.tools_schema,
                tool_choice="auto",
                temperature=temperature
            )

            loops += 1

        return response.choices[0].message.content or "Exceeded maximum tool processing loops."

    def _self_check_report(self, query: str, context_str: str, report: str) -> Dict[str, Any]:
        review_system_message = (
            "You are the Advisor Agent's internal quality reviewer. "
            "Check whether the draft report is ready to send to the user. "
            "Return only valid JSON with keys: passes (boolean), issues (array of strings), "
            "revision_instructions (string)."
        )

        review_user_message = (
            f"User Query:\n{query}\n\n"
            f"Document Context:\n{context_str}\n\n"
            f"Draft Advisor Report:\n{report}\n\n"
            "Quality checklist:\n"
            "1. Directly answers the user's actual request.\n"
            "2. Uses provided context and does not invent unsupported facts.\n"
            "3. Uses or references tool-derived calculations where financial math/risk analysis is needed.\n"
            "4. Includes financial health, future outlook, risks/limitations, and actionable advice when relevant.\n"
            "5. States additional information required if context is insufficient.\n"
            "6. Uses a chart/table figure when the report contains dense numeric comparisons that benefit from visualization.\n"
            "7. Any chart image is embedded as a Supabase Markdown image URL and has a factual caption/source note.\n"
            "8. Is clear English Markdown with source-aware claims.\n"
            "9. Every financial figure cited in the report (revenue, net income, EPS, assets, liabilities, ratios, etc.) "
            "appears VERBATIM in the provided Document Context or is derived directly from tool outputs — "
            "no rounded, estimated, or training-knowledge values are present.\n"
            "10. No metric was silently substituted from LLM training knowledge. "
            "If a figure was unavailable, the report explicitly states it is missing instead of providing an estimate.\n"
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": review_system_message},
                {"role": "user", "content": review_user_message}
            ],
            response_format={"type": "json_object"},
            temperature=0
        )

        content = response.choices[0].message.content or "{}"
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            parsed = {
                "passes": False,
                "issues": ["Self-check response was not valid JSON."],
                "revision_instructions": "Revise the report to satisfy the full quality checklist."
            }

        return {
            "passes": bool(parsed.get("passes", False)),
            "issues": parsed.get("issues", []),
            "revision_instructions": parsed.get("revision_instructions", "")
        }

    def _revise_report(
        self,
        query: str,
        context_str: str,
        current_report: str,
        self_check: Dict[str, Any]
    ) -> str:
        revision_messages = [
            {
                "role": "system",
                "content": (
                    "You are revising your own Advisor Agent report before sending it. "
                    "Fix the issues found in self-review while preserving correct analysis. "
                    "Use tools again if revised calculations, comparisons, or frameworks are needed. "
                    "Return only the final English Markdown report.\n\n"
                    "CRITICAL ANTI-HALLUCINATION RULE DURING REVISION: "
                    "Do NOT introduce any financial figure that does not appear verbatim in the Document Context or tool outputs. "
                    "If a figure needed to fix an issue is missing from the context, explicitly state it is unavailable "
                    "instead of substituting an estimate or a training-knowledge value."
                )
            },
            {
                "role": "user",
                "content": (
                    f"User Query:\n{query}\n\n"
                    f"Document Context:\n{context_str}\n\n"
                    f"Current Draft Report:\n{current_report}\n\n"
                    f"Self-Check Result:\n{json.dumps(self_check, indent=2, ensure_ascii=False)}\n\n"
                    "Revise the report so it is ready for the user."
                )
            }
        ]

        return self._run_tool_calling(revision_messages, temperature=0.15)

    def _self_review_and_revise(self, query: str, context_str: str, draft_report: str) -> str:
        final_report = draft_report

        for _ in range(self.max_self_review_loops):
            context_str = self._build_context_string(self.current_context_docs)
            self_check = self._self_check_report(query, context_str, final_report)
            if self_check["passes"]:
                return final_report

            final_report = self._revise_report(query, context_str, final_report, self_check)

        return final_report

    def revise_with_feedback(
        self,
        query: str,
        context_docs: List[Dict[str, Any]],
        current_report: str,
        critic_feedback: str,
        evaluator_feedback: Optional[str] = None,
    ) -> str:
        """Revise a report based on external Critic and/or Evaluator feedback.

        Unlike the internal ``_self_review_and_revise`` loop (which uses
        self-generated quality checks), this method accepts *external*
        feedback from the Critic Agent and optionally the Evaluator Agent
        to produce an improved version of the report.

        Parameters
        ----------
        query:
            The original user query.
        context_docs:
            The current retrieval context documents.
        current_report:
            The advisor report to revise (v1 or latest version).
        critic_feedback:
            Full Markdown critique from the Critic Agent, including the
            ``## Issues to Resolve`` checklist.
        evaluator_feedback:
            Optional Markdown evaluation from the Evaluator Agent.

        Returns
        -------
        str
            The revised advisor report (Markdown).
        """
        self.current_context_docs = self._deduplicate_documents(context_docs)
        context_str = self._build_context_string(self.current_context_docs)

        # Extract checklist items from critic feedback
        combined_issues: list[str] = []
        for line in critic_feedback.splitlines():
            stripped = line.strip()
            if stripped.startswith("- [ ]"):
                issue_text = stripped[len("- [ ]"):].strip()
                if issue_text:
                    combined_issues.append(issue_text)

        revision_instructions = (
            f"Critic Feedback:\n{critic_feedback}\n\n"
            + (f"Evaluator Feedback:\n{evaluator_feedback}\n\n"
               if evaluator_feedback else "")
            + "Address ALL the issues listed above. Keep verified data "
            + "and correct analysis intact."
        )

        feedback_as_self_check: Dict[str, Any] = {
            "passes": False,
            "issues": combined_issues,
            "revision_instructions": revision_instructions,
        }

        revised = self._revise_report(
            query, context_str, current_report, feedback_as_self_check,
        )
        # Rebuild context string (tools may have fetched new documents)
        context_str = self._build_context_string(self.current_context_docs)
        return self._self_review_and_revise(query, context_str, revised)

    def run(self, query: str, context_docs: List[Dict[str, Any]]) -> str:
        """
        Runs the Advisor Agent to analyze the user's query against the context documents.
        """
        
        self.current_query = query
        self.current_context_docs = self._deduplicate_documents(context_docs)
        self.delegated_context_events = []

        # Build the background context description for the model
        context_str = self._build_context_string(self.current_context_docs)

        system_message = (
            "You are a professional Advisor Agent specialized in strategic business and financial consulting.\n"
            "Your task is to provide high-quality advice and actionable suggestions based on the context documents provided.\n\n"
            "OPERATING GUIDELINES:\n"
            "1. ALWAYS USE THE PROVIDED TOOLS when financial calculations, comparisons, or analytical frameworks "
            "(SWOT, Porter's 5 Forces, PESTEL) are needed. Do not manually calculate complex financial or mathematical formulas.\n"
            "2. If the context documents lack necessary information for risk analysis or fulfilling the user's core request, "
            "call request_additional_context with the missing information and targeted search queries before drafting the final answer. "
            "Only state additional information is required if the retrieval/search delegate cannot provide it.\n"
            "3. The final report must be presented clearly in English using Markdown format, with clear sections, "
            "verified data from tools, and proper source citations.\n"
            "4. Do not invent revenue, income, debt, market cap, valuation, or risk inputs. If exact values are not present "
            "in the provided context or tool outputs, say they were not found and explain what evidence is needed.\n"
            "5. Ignore context documents that clearly belong to a different company than the user's requested company.\n"
            "6. When a chart would make key financial metrics easier to understand, use figure_generation_tool. "
            "Embed the returned Supabase Markdown image link directly in the report. Use Markdown tables when a table is clearer.\n\n"
            "GROUNDING RULES — MUST FOLLOW TO PREVENT HALLUCINATION:\n"
            "G1. Every financial figure you write (revenue, net income, EPS, debt, assets, ratios, percentages, etc.) MUST "
            "appear verbatim or be computed directly from numbers that appear verbatim in the provided documents or tool outputs. "
            "Never substitute a training-knowledge estimate.\n"
            "G2. Never round or simplify a source figure. If the document says '$97,690,000,000', do not write '$98B' or '$100B'. "
            "Use the exact value.\n"
            "G3. Before passing any value to comparison_tool, risk_assessment_tool, financial_calculator_tool, or "
            "figure_generation_tool, confirm that value is present word-for-word in the context. If it is not, call "
            "request_additional_context first.\n"
            "G4. If after calling request_additional_context the required data is still missing, write explicitly: "
            "'⚠️ [Metric name] was not found in the available documents. This figure cannot be confirmed without the source filing.'\n"
            "G5. It is always better to acknowledge missing data than to fabricate a plausible-looking number."
        )

        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": f"Document Context:\n{context_str}\n\nAnalysis Request: {query}"}
        ]

        draft_report = self._run_tool_calling(messages, temperature=0.2)
        context_str = self._build_context_string(self.current_context_docs)
        return self._self_review_and_revise(query, context_str, draft_report)
