import torch
from pydantic import BaseModel, Field
from predictor.config.data_configs import DataConfig
from predictor.config.ml_configs import NNHyperparameters

class TrainingConfig(BaseModel):
    data_config: DataConfig = Field(
        default_factory=DataConfig, 
        description="Data configuration."
    )
    model_nn: NNHyperparameters = Field(
        default_factory=NNHyperparameters,
        description="Neural network hyperparameter configuration."
    )
    
    accelerator: str = Field(
        default='cpu',
        description="Config for using GPU or CPU."
    )
    seed: int = Field(
        default=42,
        description="Random seed for consistent output."
    )
    epochs: int = Field(
        default=None,
        description="Number of epochs to train the model."
    )
    n_fold: int = Field(
        default=None,
        description="Number of folds for cross-validation."
    )
    batch_size: int = Field(
        default=None, 
        description="Size of the mini-batch for training."
    )
