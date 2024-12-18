
import math
import pandas as pd
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import TimeSeriesSplit
from predictor.config.train_configs import TrainingConfig

class CustomDataset(Dataset):
    def __init__(self, df_input: pd.DataFrame, features: list, target: str, accelerator: str):
        self.features = torch.FloatTensor(df_input[features].to_numpy()).to(accelerator)
        self.target = torch.FloatTensor(df_input[target].to_numpy()).to(accelerator)

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
        target = self.target[index]
        return features, target
    
class DataModule(nn.Module):
    def __init__(self, df, config: TrainingConfig, mode):
        super().__init__()
        if mode == 'train':
            split_idx = math.floor(len(df)*config.train_test_split)
            self.df_train = df[:split_idx]
            self.df_test = df[split_idx:]
            self.n_fold = config.n_fold
            self.setup()
            
        elif mode == 'eval':
            split_idx = math.floor(len(df)*config.train_test_split)
            self.df_train = df[:split_idx]
            self.df_test = df[split_idx:]
            
        elif mode == 'predict':
            self.df_all = df
            
        self.batch_size = config.batch_size
        self.accelerator = torch.device("cuda" if (torch.cuda.is_available() and config.accelerator == "gpu") else "cpu")
        
        # initial the datasets as None
        self.tain_dataset = None
        self.valid_dataset = None

        self.features = df.drop(config.data_config.target, axis=1).columns
        self.target = config.data_config.target
        

    def setup(self, test_days=30):    
        self.index_dict = {}
        # use TimeSeriesSplit to separate train and valid datasets
        tss = TimeSeriesSplit(n_splits=self.n_fold, test_size=test_days)
        for i, (train_idx, val_idx) in enumerate(tss.split(self.df_train)):
            self.index_dict[i] = {
                "train_idx": train_idx,
                "val_idx": val_idx
            }

    def train_loader(self, fold, num_workers=0):
        self.train_dataset = CustomDataset(
            self.df_train[self.df_train.index.isin(self.index_dict[fold]['train_idx'])],
            features=self.features,
            target=self.target,
            accelerator=self.accelerator
        )
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=False, num_workers=num_workers)
    
    def valid_loader(self, fold, num_workers=0):
        valid_dataset = CustomDataset(
            self.df_train[self.df_train.index.isin(self.index_dict[fold]['val_idx'])],
            features=self.features,
            target=self.target,
            accelerator=self.accelerator
        )
        return DataLoader(valid_dataset, batch_size=self.batch_size, shuffle=False, num_workers=num_workers)

    def test_loader(self, num_workers=0):
        test_dataset = CustomDataset(
            self.df_test,
            features=self.features,
            target=self.target,
            accelerator=self.accelerator
        )
        return DataLoader(test_dataset, batch_size=self.batch_size, shuffle=False, num_workers=num_workers)
        
    def full_train_data_loader(self, num_workers=0):
        self.full_train_dataset = CustomDataset(
            self.df_train,
            features=self.features,
            target=self.target,
            accelerator=self.accelerator
        )
        return DataLoader(self.full_train_dataset, batch_size=self.batch_size, shuffle=False, num_workers=num_workers)
    
    def full_data_loader(self, num_workers=0):
        full_dataset = CustomDataset(
            self.df_all,
            features=self.features,
            target=self.target,
            accelerator=self.accelerator
        )
        return DataLoader(full_dataset, batch_size=self.batch_size, shuffle=False, num_workers=num_workers)
        