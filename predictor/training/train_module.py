from predictor.models.nn import NN
from predictor.config.train_configs import TrainingConfig
from predictor.training.data_loader import DataModule

from pytorch_lightning import Trainer


def train(df, config: TrainingConfig):

    data_module = DataModule(df, config)


    for fold in range(config.n_fold):
        
        input_size = data_module.train_dataset.features.shape[1]

        model = NN(
            input_size=input_size,
            hidden_dims=config.n_hidden,
            lr=config.lr,
            weight_decay=config.weight_decay
        )

        test_trainer = Trainer(
            fast_dev_run=True,
        )

        test_trainer.fit(
            model,
            data_module.train_loader(fold),
            data_module.valid_loader(fold)
        )