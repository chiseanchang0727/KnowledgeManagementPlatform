from base import LLMAgents
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts.chat import ChatPromptTemplate
from src.llm.prompts import SUMMARY_PROMPT


class SummaryBot(LLMAgents):
    def __init__(self) -> None:
        self.model = self.llm
    
    
    def summarize(self, input_string):
        
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system", SUMMARY_PROMPT
                ),
                (
                    "human","{input_string}"
                )
            ]
        )
        
        chain = (
            {"input_string": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        return chain.invoke(input_string)