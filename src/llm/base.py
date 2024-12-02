import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.runnables import RunnablePassthrough

from prompts import SUMMARY_PROMPT

class LLMAgents:
    def __init__(self) -> None:
        load_dotenv()
        self.llm = self.get_llm()
    
    def get_llm(self):

        # for AOAi
        OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
        OPEN_AI_VERSION = os.getenv('OPEN_AI_VERSION')
        GPT_DEPLOYMENT_NAME = os.getenv('GPT_DEPLOYMENT_NAME')
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        OPENAI_API_TYPE = os.getenv('OPENAI_API_TYPE')

        llm = AzureChatOpenAI(
            azure_endpoint=OPENAI_API_BASE,
            openai_api_version=OPEN_AI_VERSION,
            azure_deployment=GPT_DEPLOYMENT_NAME,
            openai_api_key=OPENAI_API_KEY,
            openai_api_type=OPENAI_API_TYPE,
            temperature=0
        )

        return llm
    
    
    
    #TODO: user runnable to construct the summary bot
    def summary_bot(self):
        
        sys_prompt = SUMMARY_PROMPT
        
        return
    