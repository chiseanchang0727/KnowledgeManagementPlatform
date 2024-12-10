import torch
import torch.nn as nn

from pytorch_lightning import LightningModule

class NN(LightningModule):
    def __init__(self, input_size, hidden_dims, lr, weight_decay, dropouts=None):
        super().__init__()
        layers = []
        input_dim = input_size

        for i, hidden_dim in enumerate(hidden_dims):
            layers.append(nn.BatchNorm1d(input_dim))

            if i > 0:
                layers.append(nn.ReLU())

            layers.append(nn.Linear(input_dim, hidden_dim))

            # if i < len(dropouts):
            #     layers.append(nn.Dropout(dropouts[i]))

            input_dim = hidden_dim
            
        # now the input_dim is the final round of hidden layer
        layers.append(nn.Linear(input_dim, 1))

        self.model = nn.Sequential(*layers)
        self.lr = lr
        self.weight_decay = weight_decay

        self.criterion = nn.MSELoss()


    def forward(self, x):
        # 1 means run one times
        return self.model(x).squeeze(-1) * 1
    
    def training_step(self, batch):
        x, y = batch
        y_pred = self(x)

        loss = self.criterion(y_pred, y)

        self.log('train_loss', loss, on_step=False, on_epoch=True, batch_size=x.size(0))

        return loss
    

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr, weight_decay=self.weight_decay)
        schedular = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer=optimizer, mode='min', factor=0.1, patience=5, verbose=True)

        return {
            'optimizer': optimizer,
            'lr_schedular': {
                'schedular': schedular,
                'monitor': 'val_loss'
            }
        }
    
    