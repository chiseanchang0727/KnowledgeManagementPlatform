import pandas as pd
from utils.enums import ConfigType
from predictor.config.data_configs import DataConfig
from llm.config.llm_config import LLMConfig
from predictor.config.ml_configs import NNhyperparameters
import yaml


def normalize_keys(d):
    """Normalize the key to uppercase."""
    if isinstance(d, dict):
        return {k.upper(): v for k, v in d.items()}
    return d

class YamlLoader:
    def __init__(self, file_path):
        self.config_data = self.load_config_from_file(file_path)

    def load_config_from_file(self, file_path: str):
        with open(file_path, "r") as file:
            config_data = yaml.safe_load(file)
        return normalize_keys(config_data)
    
    def get_data_config(self):
        return DataConfig(**self.config_data.get(ConfigType.Data, {}))
    
    def get_llm_config(self):
        return LLMConfig(**self.config_data.get(ConfigType.LLM, {}))
    
    def get_model_nn_config(self):
        return NNhyperparameters(**self.config_data.get(ConfigType.Model_NN, {}))
    
    

def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        return None