from typing import List
from pydantic import BaseModel, Field


class NNhyperparameters(BaseModel):
    """Hyperparameters for NN training."""
    
    accelerator: str = Field(
        default='cpu', 
        description="Config for using GPU or CPU ."
    )
    
    seed: int = Field(
        default=42, 
        description="Random seed for consistent output."
    )
    
    batch_size: int = Field(
        default=100, 
        description="Size of the mini-batch for training."
    )
    
    lr: float = Field(
        default=1e-3, 
        description="Learning rate for the optimizer."
    )
    
    n_hidden: List[int] = Field(
        default=None, 
        description="Configuration for hidden layer sizes (e.g., [128, 64])."
    )
    
    epochs: int = Field(
        default=100, 
        description="Number of epochs to train the model."
    )
    
    n_fold: int = Field(
        default=5, 
        description="Number of folds for cross-validation."
    )
    
    weight_decay: float = Field(
        default=1e-4, 
        description="Weight decay (L2 regularization) for better convergence."
    )