"""
    LLM Generator
    Implement an LLM to plan, generate and execute tool calls, and reason over results.
"""
from langgraph.graph import Workflow, END
from langgraph.prebuilt import LLMNode
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

def build_prompt(messages):
    return 
def get_llm():
    """Initialize and return the LLM node."""
    # For demonstration, we use a small model. In production, use a more powerful model.
    model_name = "Qwen/Qwen2-7B-Instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    def llm_invoke(messages):
        """Invoke the LLM with the given messages."""
        # Concatenate messages into a single prompt
        prompt = "\n".join(f"{role}: {content}" for role, content in messages)
        prompt = build_prompt(messages)
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=100)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    return LLMNode(llm_invoke)
