from enum import Enum


class ConfigType(Enum):

    LLM = 'llm'
    Model_NN = 'Model_NN'
    Data = 'Data'
    Training = 'Training'

    # def __repr__(self) -> str:
    #     return f'"{self.value}"'