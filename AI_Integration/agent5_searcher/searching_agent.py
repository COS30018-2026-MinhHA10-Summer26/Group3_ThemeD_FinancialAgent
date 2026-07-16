from ai_integration.tools.search_assess_tool import calculate_coverage
from openai import OpenAI
import dotenv
import os
from ai_integration.tools.report_search_tool import report_search_tool
from ai_integration.entity_filter import filter_documents_for_query_entity
import json

api_key = os.getenv("OPENAI_API_KEY") or dotenv.get_key(".env", "OPENAI_API_KEY")
SKILL_PATH = "ai_integration/agent5_searcher/SKILL.md"
with open(SKILL_PATH, "r") as f:
    try:
        SKILL_CONTEXT = f.read()
    except UnicodeDecodeError:
        f.seek(0)
        f.encoding = "utf-8"
        SKILL_CONTEXT = f.read()

class SearchingAgent:
    def __init__(self,coverage_threshold=0.4,max_iterations=1):
        self.client = OpenAI(api_key = api_key)
        self.report_search_tool = report_search_tool
        self.coverage_threshold = coverage_threshold
        self.max_iterations = max_iterations
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
        return filter_documents_for_query_entity(user_query, documents)
