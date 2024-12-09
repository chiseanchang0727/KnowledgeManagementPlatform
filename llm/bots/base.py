import os
from llm.config.enum import LLMType
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

from llm.config.llm_config import LLMConfig

load_dotenv()


# class LLMBase:
#     def __init__(self, config):
#         self.config = config
    
#     def get_llm(self, llm_type=LLMType.AzureOpenAIChat):
#         if llm_type == LLMType.AzureOpenAIChat:
#             self.llm = self.get_aoai_llm()
#         else:
#             raise NotImplementedError(f"LLM Type {self.llm_type} is not supported yet.")
        

#     def get_aoai_llm(self):

#         # for AOAi
#         OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
#         OPEN_AI_VERSION = os.getenv('OPEN_AI_VERSION')
#         GPT_DEPLOYMENT_NAME = os.getenv('GPT_DEPLOYMENT_NAME')
#         OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
#         OPENAI_API_TYPE = os.getenv('OPENAI_API_TYPE')

#         return AzureChatOpenAI(
#             azure_endpoint=OPENAI_API_BASE,
#             openai_api_version=OPEN_AI_VERSION,
#             azure_deployment=GPT_DEPLOYMENT_NAME,
#             openai_api_key=OPENAI_API_KEY,
#             openai_api_type=OPENAI_API_TYPE,
#             temperature=0
#         )


def get_llm(config: LLMConfig):
    """Get LLM client."""
    
    if config.llm.type == LLMType.AzureOpenAIChat:
    
        return AzureChatOpenAI(
            azure_endpoint=config.llm.api_base,
            openai_api_version=config.llm.api_version,
            azure_deployment=config.llm.deployment_name,
            openai_api_key=config.llm.api_key,
            temperature=config.llm.temperature
        )

               
    
