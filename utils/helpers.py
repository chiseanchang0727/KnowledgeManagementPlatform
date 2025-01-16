import yaml
import pandas as pd
from utils.enums import ConfigType
from llm.config.llm_config import LLMConfig
# from predictor.config.train_configs import TrainingConfig
from app.config.upload_config import UploadConfig


class YamlLoader:
    def __init__(self, file_path):
        self.config_data = self.load_config_from_file(file_path)

    def load_config_from_file(self, file_path: str):
        with open(file_path, "r") as file:
            config_data = yaml.safe_load(file)
        return config_data # normalize_keys(config_data)
    
    def get_llm_config(self):
        return LLMConfig(**self.config_data[ConfigType.LLM.value])
    
    # def get_training_config(self):
    #     return TrainingConfig(**self.config_data[ConfigType.Training.value])
    
    def get_upload_config(self):
        return UploadConfig(**self.config_data[ConfigType.DataUpload.value])



def normalize_keys(d):
    """Normalize the key to uppercase."""
    if isinstance(d, dict):
        return {k.lower(): v for k, v in d.items()}
    return d


def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        return None