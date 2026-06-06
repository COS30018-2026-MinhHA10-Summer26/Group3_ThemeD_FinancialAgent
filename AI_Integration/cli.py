"""
CLI entrypoint for running the financial agent orchestrator end to end.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
from typing import Any

from ai_integration.agent.orchestrator import run_agent_state
from ai_integration.ingestion.loader import load_documents


DEFAULT_RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the AI integration orchestrator workflow from the command line.",
    )
    parser.add_argument(
        "query_parts",
        nargs="*",
        help="Query text. You can also use --query for a single string.",
    )
    parser.add_argument(
        "--query",
        dest="query",
        help="Query text to send to the orchestrator.",
    )
    parser.add_argument(
        "--query-file",
        dest="query_file",
        help="Path to a text file containing the query.",
    )
    parser.add_argument(
        "--load-raw-docs",
        action="store_true",
        help="Load PDFs and other raw files from the raw data directory into memory.",
    )
    parser.add_argument(
        "--raw-dir",
        default=str(DEFAULT_RAW_DIR),
        help="Folder to load raw source documents from. Default: data/raw",
    )
    parser.add_argument(
        "--memory-file",
        help="Optional JSON file to merge into the orchestrator memory payload.",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        help="Override the number of final context documents to keep.",
    )
    parser.add_argument(
        "--retrieval-threshold",
        type=float,
        help="Override the threshold used to route into web search.",
    )
    parser.add_argument(
        "--company-name",
        help="Company name hint for official report searching.",
    )
    parser.add_argument(
        "--company-website",
        help="Official company or investor-relations website for report searching.",
    )
    parser.add_argument(
        "--year",
        dest="years",
        action="append",
        type=int,
        help="Target report year. Pass multiple times for multiple years.",
    )
    parser.add_argument(
        "--use-selenium",
        action="store_true",
        help="Allow Selenium fallback for official report discovery.",
    )
    parser.add_argument(
        "--dry-run-downloads",
        action="store_true",
        help="Do not download official reports; only simulate the plan.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the final workflow state as JSON.",
    )
    parser.add_argument(
        "--show-state",
        action="store_true",
        help="Print a compact execution summary after the final response.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    query = _resolve_query(args, parser)
    memory = _build_memory(args)

    result = run_agent_state(query, memory)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False, default=str))
        return 0

    final_output = result.get("report") if result.get("report_requested") and result.get("report") else result.get("response", "")
    print(final_output)

    if args.show_state:
        print("\n---")
        print("workflow_steps:", ", ".join(result.get("workflow_steps", [])))
        print("tool_calls:", json.dumps(result.get("tool_calls", []), ensure_ascii=False))
        print("errors:", json.dumps(result.get("errors", []), ensure_ascii=False))
        metadata = result.get("metadata", {})
        if metadata:
            print("metadata:", json.dumps(metadata, ensure_ascii=False, default=str))

    return 0


def _resolve_query(args: argparse.Namespace, parser: argparse.ArgumentParser) -> str:
    if args.query:
        return args.query.strip()

    if args.query_file:
        query_file = Path(args.query_file)
        if not query_file.exists():
            parser.error(f"query file does not exist: {query_file}")
        return query_file.read_text(encoding="utf-8").strip()

    if args.query_parts:
        return " ".join(args.query_parts).strip()

    stdin_text = sys.stdin.read().strip() if not sys.stdin.isatty() else ""
    if stdin_text:
        return stdin_text

    parser.error("provide a query via positional args, --query, --query-file, or stdin")
    return ""


def _build_memory(args: argparse.Namespace) -> dict[str, Any]:
    memory: dict[str, Any] = {}

    if args.memory_file:
        memory_path = Path(args.memory_file)
        memory = json.loads(memory_path.read_text(encoding="utf-8"))

    if args.top_k is not None:
        memory["top_k"] = args.top_k

    if args.retrieval_threshold is not None:
        memory["retrieval_threshold"] = args.retrieval_threshold

    if args.load_raw_docs:
        raw_dir = Path(args.raw_dir)
        memory["documents"] = load_documents(str(raw_dir)) if raw_dir.exists() else []

    metadata = dict(memory.get("metadata", {}))
    if args.company_name:
        metadata["company_name"] = args.company_name
    if args.company_website:
        metadata["company_website"] = args.company_website
    if args.years:
        metadata["target_years"] = args.years
    if args.use_selenium:
        metadata["use_selenium"] = True
    if args.dry_run_downloads:
        metadata["dry_run_downloads"] = True
    if metadata:
        memory["metadata"] = metadata

    return memory


if __name__ == "__main__":
    raise SystemExit(main())
