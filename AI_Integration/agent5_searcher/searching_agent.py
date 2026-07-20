import json
import os
from pathlib import Path
import time
from typing import Any

import dotenv
import openai
from openai import OpenAI

from ai_integration.agent5_searcher.search_reranker import rerank_search_results
from ai_integration.entity_filter import filter_documents_for_query_entity, missing_query_entities
from ai_integration.tools.report_search_tool import report_search_tool
from ai_integration.tools.search_assess_tool import calculate_coverage

api_key = os.getenv("OPENAI_API_KEY") or dotenv.get_key(".env", "OPENAI_API_KEY")
SKILL_PATH = Path(__file__).resolve().with_name("SKILL.md")
with SKILL_PATH.open("r", encoding="utf-8") as f:
    try:
        SKILL_CONTEXT = f.read()
    except UnicodeDecodeError:
        f.seek(0)
        SKILL_CONTEXT = f.read()


def _safe_chat_completion(client: OpenAI, **kwargs) -> Any:
    """Execute chat completion with retry and backoff on RateLimitError (429)."""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            return client.chat.completions.create(**kwargs)
        except openai.RateLimitError as exc:
            if attempt == max_retries - 1:
                raise
            sleep_time = (attempt + 1) * 4
            print(f"   [SearchingAgent] OpenAI RateLimitError (429). Retrying in {sleep_time}s (attempt {attempt + 1}/{max_retries})...")
            time.sleep(sleep_time)


class SearchingAgent:
    def __init__(self,coverage_threshold=0.4,max_iterations=1,top_k=2):
        self.client = OpenAI(api_key = api_key)
        self.report_search_tool = report_search_tool
        self.coverage_threshold = coverage_threshold
        self.max_iterations = max_iterations
        self.top_k = top_k
        self.skill_context = SKILL_CONTEXT

    def _truncate_docs_for_prompt(self, documents, max_chars_per_doc: int = 300) -> str:
        """Return a compact summary of documents to avoid TPM limits.
        Full text is not needed – a short preview is enough for the LLM to
        identify gaps and generate search queries."""
        lines = []
        for i, doc in enumerate(documents, 1):
            text = str(doc.get("text", doc.get("content", "")) if isinstance(doc, dict) else doc).strip()
            source = doc.get("source", f"doc-{i}") if isinstance(doc, dict) else f"doc-{i}"
            lines.append(f"[{i}] {source}: {text[:max_chars_per_doc]}{'...' if len(text) > max_chars_per_doc else ''}")
        return "\n".join(lines) if lines else "(no documents)"

    def identify_missing_information(self, user_query, documents):
        doc_summary = self._truncate_docs_for_prompt(documents)
        return _safe_chat_completion(
            self.client,
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.skill_context},
                {"role": "user", "content": f"User Query: {user_query}\n\nCurrent Documents (summaries):\n{doc_summary}\n\nIdentify the missing information needed to fully answer the user query based on the current documents."}
            ]
        ).choices[0].message.content

    def generate_search_queries(self, user_query, documents, missing_info):
        doc_summary = self._truncate_docs_for_prompt(documents)
        return _safe_chat_completion(
            self.client,
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.skill_context},
                {"role": "user", "content": f"User Query: {user_query}\n\nCurrent Documents (summaries):\n{doc_summary}\n\nMissing Information: {missing_info}\n\nGenerate specific search queries to retrieve the missing information."}
            ]
        ).choices[0].message.content

    def retrieve_documents(self, queries, user_query=""):
        retrieved_docs = []
        if not queries:
            return retrieved_docs

        for query in queries:
            if not query:
                continue
            try:
                search_results = self.report_search_tool(query)
            except Exception as exc:
                print(f"Search retrieval failed for {query!r}: {exc}")
                continue
            retrieved_docs.extend(search_results.get("synthetic_results", []))
        return filter_documents_for_query_entity(user_query, retrieved_docs)

    def _coverage(self, user_query, documents):
        filtered_documents = filter_documents_for_query_entity(user_query, documents)
        if not filtered_documents:
            return 0.0
        document_texts = [
            str(doc.get("text", doc.get("content", ""))) if isinstance(doc, dict) else str(doc)
            for doc in filtered_documents
        ]
        return calculate_coverage(user_query, document_texts)

    def _parse_search_queries(self, raw_query_response):
        try:
            parsed = json.loads(raw_query_response)
            queries = parsed.get("search_queries", [])
            if isinstance(queries, list):
                return [str(query) for query in queries if str(query).strip()]
        except json.JSONDecodeError:
            pass
        return [
            line.strip("-* 0123456789.").strip()
            for line in str(raw_query_response).splitlines()
            if line.strip()
        ]

    def run(self,user_query,initial_documents):
        documents = initial_documents if initial_documents else []
        iteration = 0
        original_query = user_query
        while iteration < self.max_iterations:
            coverage = self._coverage(user_query, documents)
            missing_entities = missing_query_entities(original_query, documents)
            if coverage >= self.coverage_threshold and not missing_entities:
                break
            missing_info = self.identify_missing_information(
                user_query,
                documents
            )
            search_context = (
                f"User Query: {original_query}\n\n"
                f"The identified missing information is: {missing_info}"
            )
            if missing_entities:
                search_context += (
                    "\n\nThe current context has no document for these named companies: "
                    f"{', '.join(sorted(missing_entities))}. Generate a targeted official-report query for each."
                )
            
            queries = self._parse_search_queries(
                self.generate_search_queries(search_context, documents, missing_info)
            )
            # Keep the entity-coverage guarantee deterministic even if the LLM
            # omits a company from its generated query list.
            queries.extend(
                f"{entity.title()} annual report 10-K investor relations PDF"
                for entity in sorted(missing_entities)
            )
            queries = list(dict.fromkeys(queries))
            print(f"Iteration {iteration + 1}: Generated Search Queries: {queries}")
            new_documents = self.retrieve_documents(queries, original_query)
            documents.extend(new_documents)
            iteration += 1

        # Apply entity filter first
        filtered = filter_documents_for_query_entity(original_query, documents)

        # Hybrid rerank: chunk → embed with OpenAI embeddings → top K
        top_k_chunks = rerank_search_results(
            query=original_query,
            raw_documents=filtered,
            top_k=self.top_k,
        )

        return top_k_chunks if top_k_chunks else filtered
