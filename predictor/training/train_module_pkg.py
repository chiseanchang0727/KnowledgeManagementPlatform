import torch
from predictor.models.nn import NN
from predictor.config.train_configs import TrainingConfig
from predictor.training.data_loader import DataModule

from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import Timer

def train(df, config: TrainingConfig, type):

    data_module = DataModule(df, config)


    for fold in range(config.n_fold):
        data_module.train_loader(fold)
        data_module.valid_loader(fold)
        
        input_size = data_module.train_dataset.features.shape[1]

        model = NN(
            input_size=input_size,
            hidden_dims=config.model_nn.n_hidden,
            lr=config.model_nn.lr,
            weight_decay=config.model_nn.weight_decay
        )
        
        if type == 'check':
            test_trainer = Trainer(
                fast_dev_run=True,
            )

            test_trainer.fit(
                model,
                data_module.train_loader(fold),
                data_module.valid_loader(fold)
            )

        if type == 'train':
            print('Training start!')
            timer = Timer()

            trainer = Trainer(
                max_epochs=config.epochs,
                accelerator=config.accelerator if torch.cuda.is_available() else 'cpu',
                devices=1, # only one gpu
                enable_progress_bar=True,
                log_every_n_steps=10

            ) 

            trainer.fit( 
                model=model,
                train_dataloaders=data_module.train_loader(fold),
                val_dataloaders=data_module.valid_loader(fold)

            )

            print(f'Fold-{fold} Training completed in {timer.time_elapsed("train"):.2f}s')