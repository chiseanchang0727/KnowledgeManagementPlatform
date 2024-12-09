from devtools import pformat

from pydantic import BaseModel, Field

from llm.config.enum import LLMType
from llm.config.llm_parameters import LLMParameter

class LLMConfig(BaseModel):
    
    def __repr__(self) -> str:
        """Get a string representation."""
        return pformat(self, highlight=False)
    
    type: LLMType = Field(
        description='The type of LLM model to sue', default=LLMType.AzureOpenAIChat
    )
    
    llm: LLMParameter = Field(
        description="The LLM configuration to use.", default=LLMParameter()
    )