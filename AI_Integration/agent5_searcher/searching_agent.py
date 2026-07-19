import json
import os
from pathlib import Path

import dotenv
from openai import OpenAI

from ai_integration.agent5_searcher.search_reranker import rerank_search_results
from ai_integration.entity_filter import filter_documents_for_query_entity
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

class SearchingAgent:
    def __init__(self,coverage_threshold=0.4,max_iterations=1,top_k=2):
        self.client = OpenAI(api_key = api_key)
        self.report_search_tool = report_search_tool
        self.coverage_threshold = coverage_threshold
        self.max_iterations = max_iterations
        self.top_k = top_k
        self.skill_context = SKILL_CONTEXT

    def identify_missing_information(self, user_query, documents):
        return self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.skill_context},
                {"role": "user", "content": f"User Query: {user_query}\n\nCurrent Documents: {documents}\n\nIdentify the missing information needed to fully answer the user query based on the current documents."}
            ]
        ).choices[0].message.content

    def generate_search_queries(self, user_query, documents, missing_info):
        return self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.skill_context},
                {"role": "user", "content": f"User Query: {user_query}\n\nCurrent Documents: {documents}\n\nMissing Information: {missing_info}\n\nGenerate specific search queries to retrieve the missing information."}
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
            if coverage >= self.coverage_threshold:
                break
            missing_info = self.identify_missing_information(
                user_query,
                documents
            )
            user_query = f"User Query: {user_query}\n\nThe identified missing information is: {missing_info}"
            
            queries = self._parse_search_queries(
                self.generate_search_queries(user_query,documents,missing_info)
            )
            print(f"Iteration {iteration + 1}: Generated Search Queries: {queries}")
            new_documents = self.retrieve_documents(queries, user_query)
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
