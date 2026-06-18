from langchain_core.prompts import ChatPromptTemplate
from langchain_core.openai import ChatOpenAI
from langchain_core.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = str(os.getenv("OPENAI_API_KEY"))

CONTEXT_PATH = "ai_integration/models/agent_context.md"
with open(CONTEXT_PATH, "r") as f:
    try:
        CONTEXT = f.read()
    except UnicodeDecodeError:
        f.seek(0)
        f.encoding = "utf-8"
        CONTEXT = f.read()
class ExternalLLM:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.llm = ChatOpenAI(model=self.model_name, temperature=self.temperature)

    def generate_response(self, prompt: str) -> str:
        chat_prompt = ChatPromptTemplate.from_messages([("system", CONTEXT), ("user", prompt)])
        chain = LLMChain(llm=self.llm, prompt=chat_prompt)
        response = chain.run({})
        return response