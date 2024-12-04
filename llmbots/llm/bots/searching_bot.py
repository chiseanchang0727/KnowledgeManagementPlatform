from .base import LLM




class WebSearchAI(LLM):
    def __init__(self):
        self.llm = self.get_llm()


