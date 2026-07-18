from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

from pathlib import Path

_current_dir = Path(__file__).resolve().parent
CONTEXT_PATH = _current_dir / "agent_context.md"
with open(CONTEXT_PATH, "r", encoding="utf-8") as f:
    CONTEXT = f.read()
class ExternalLLM:
    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.7):
        self.model_name = model_name
        self.temperature = temperature
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured for AnswerAgent.")
        self.llm = ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            api_key=api_key,
            timeout=60,
            max_retries=2,
        )

    def generate_response(self, prompt: str) -> str:
        # CONTEXT includes JSON examples. Passing it through ChatPromptTemplate
        # makes braces look like template variables (for example "prompts"),
        # which raises KeyError before the API is ever called.
        response = self.llm.invoke([
            SystemMessage(content=CONTEXT),
            HumanMessage(content=prompt),
        ])
        return str(response.content)
