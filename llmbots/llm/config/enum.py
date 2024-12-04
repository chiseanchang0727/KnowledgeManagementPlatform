from enum import Enum


class LLMType(str, Enum):
    """
    LLMType enum class definition.
    """

    # Raw Completion
    OpenAI = "openai"
    AzureOpenAI = "azure_openai"