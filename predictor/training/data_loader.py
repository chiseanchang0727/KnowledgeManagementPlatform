
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import TimeSeriesSplit
from predictor.config.ml_configs import NNhyperparameters

class CustomDataset(Dataset):
    def __init__(self, df_input: pd.DataFrame, features: list, label: str, accelerator='cpu'):
        """
        Args:
            df_input (pd.DataFrame): input DataFrame
            features (list): list of column names to use as features.
            label (str): column name to use as the target.
        """
        self.features = torch.FloatTensor(df_input[features].to_numpy()).to(accelerator)
        self.label = torch.FloatTensor(df_input[label].to_numpy()).to(accelerator)

    def __len__(self):
        """
        Returns the total number of data
        """
        return len(self.features)
    
    def __getitem__(self, index):
        """
        Retrieve one sample at the given index

        Args:
            idx(int): index of the sample to retrieve

        Returns:
            tuple(feature, target): as tensor
        """
        features = self.features[index]
        target = self.label[index]
        return features, target
    
class DataModule(nn.Module):
    def __init__(self, df_train, features, label, config: NNhyperparameters):
        super().__init__()
        self.df = df_train
        self.batch_size = config.batch_size
        self.accelerator = config.accelerator if torch.cuda.is_available() else 'cpu'
        
        # initial the datasets as None
        self.tain_dataset = None
        self.valid_dataset = None

        self.features = features
        self.label = label
        self.N_fold = config.n_fold

        self.setup()

    def setup(self, df, test_days=30):    
        self.index_dict = {}
        tss = TimeSeriesSplit(n_splits=self.N_fold, test_size=test_days)
        for i, (train_idx, val_idx) in enumerate(tss.split(df)):
            self.index_dict[i] = {
                "train_idx": train_idx,
                "val_idx": val_idx
            }


    def train_loader(self, fold, num_workers=0):
        self.train_dataset = CustomDataset(
            self.df[self.df.index.isin(self.index_dict[fold]['train_idx'])],
            features=self.features,
            label=self.label,
            accelerator=self.accelerator
        )
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=False, num_workers=num_workers)
    
    def valid_loader(self, fold, num_workers=0):
        self.valid_dataset = CustomDataset(
            self.df[self.df.index.isin(self.index_dict[fold]['val_idx'])],
            features=self.features,
            label=self.label,
            accelerator=self.accelerator
        )
        return DataLoader(self.valid_dataset, batch_size=self.batch_size, shuffle=False, num_workers=num_workers)
