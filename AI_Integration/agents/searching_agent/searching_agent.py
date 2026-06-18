

SKILL_PATH = "ai_integration/agent/searching_agent/SKILL.md"
with open(SKILL_PATH, "r") as f:
    try:
        SKILL_CONTEXT = f.read()
    except UnicodeDecodeError:
        f.seek(0)
        f.encoding = "utf-8"
        SKILL_CONTEXT = f.read()

class SearchingAgent:
    def __init__(self,llm,report_search_tool,embedding_model,coverage_threshold=0.8,max_iterations=3):
        self.llm = llm
        self.report_search_tool = report_search_tool
        self.embedding_model = embedding_model
        self.coverage_threshold = coverage_threshold
        self.max_iterations = max_iterations
        self.skill_context = SKILL_CONTEXT

    def identify_missing_information(self, user_query, documents):
        return self.llm.generate_response(f"{self.skill_context}\n\nUser Query: {user_query}\n\nCurrent Documents: {documents}\n\nIdentify the missing information needed to fully answer the user query based on the current documents.")
    
    def generate_search_queries(self, user_query, documents, missing_info):
        return self.llm.generate_response(f"{self.skill_context}\n\nUser Query: {user_query}\n\nCurrent Documents: {documents}\n\nMissing Information: {missing_info}\n\nGenerate specific search queries to retrieve the missing information.")
    
    def retrieve_documents(self, queries):
        retrieved_docs = []
        for query in queries:
            search_results = self.report_search_tool(query)
            retrieved_docs.extend(search_results.get("synthetic_results", []))
        return retrieved_docs

    def run(self,user_query,initial_documents):
        documents = initial_documents
        iteration = 0
        while iteration < self.max_iterations:
            missing_info = self.identify_missing_information(
                user_query,
                documents
            )
            coverage = self.calculate_coverage(user_query,documents,missing_info)
            if coverage >= self.coverage_threshold:
                break
            queries = self.generate_search_queries(user_query,documents,missing_info)
            new_documents = self.retrieve_documents(queries)
            documents.extend(new_documents)
            iteration += 1
        return documents