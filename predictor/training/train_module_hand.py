import torch
from torch import nn, optim

from predictor.models.nn import NN
from predictor.config.train_configs import TrainingConfig
from predictor.training.data_loader import DataModule

def train(df, config: TrainingConfig, mode):

    data_module = DataModule(df, config)

    device = torch.device("cuda" if (torch.cuda.is_available() and config.accelerator == "gpu") else "cpu")

    total_train_loss = 0.0
    total_val_loss = 0.0

    for fold in range(config.n_fold):

        train_loader = data_module.train_loader(fold)
        valid_loader = data_module.valid_loader(fold)

        input_size = data_module.train_dataset.features.shape[1]

 
        model = NN(
            input_size=input_size,
            hidden_dims=config.model_nn.n_hidden,
            lr=config.model_nn.lr,
            weight_decay=config.model_nn.weight_decay
        ).to(device)

   
        optimizer = optim.Adam(model.parameters(), lr=config.model_nn.lr, weight_decay=config.model_nn.weight_decay)
        criterion = nn.MSELoss()  

        fold_train_loss = float('inf')
        fold_val_loss = float('inf')

        if mode == 'check':
            print("Running a quick check.")

            model.train()
            for batch_idx, (X, y) in enumerate(train_loader):
                X, y = X.to(device), y.to(device)

                optimizer.zero_grad()
                outputs = model(X)
                loss = criterion(outputs, y)
                loss.backward()
                optimizer.step()

                print(f"Check Batch {batch_idx}: Loss = {loss.item()}")
                
                # break after 1 run
                if batch_idx > 1:
                    break

        elif mode == 'train':
            print('Training start!')

            for epoch in range(config.epochs):
    
                model.train()
                train_loss = 0.0
                for batch_idx, (X, y) in enumerate(train_loader):
                    X, y = X.to(device), y.to(device)

                    optimizer.zero_grad()
                    outputs = model(X)
                    loss = criterion(outputs, y)
                    loss.backward()
                    optimizer.step()

                    train_loss += loss.item()


                avg_train_loss = train_loss / len(train_loader)
                if avg_train_loss < fold_train_loss:
                    fold_train_loss = avg_train_loss
 
                model.eval()
                val_loss = 0.0
                with torch.no_grad():
                    for X_val, y_val in valid_loader:
                        X_val, y_val = X_val.to(device), y_val.to(device)
                        val_outputs = model(X_val)
                        val_loss += criterion(val_outputs, y_val).item()

                avg_val_loss = val_loss / len(valid_loader)
                if avg_val_loss < fold_val_loss:
                    fold_val_loss = avg_val_loss

                print(f"Fold: {fold} | Epoch: {epoch+1}/{config.epochs} | "
                      f"Train Loss: {avg_train_loss:.4f} | Val Loss: {avg_val_loss:.4f}")

            total_train_loss += fold_train_loss
            total_val_loss += fold_val_loss

            print(f"Fold-{fold} Training completed!")
    
    avg_train_loss = total_train_loss / config.n_fold
    avg_val_loss = total_val_loss / config.n_fold

    print(f"Average Training Loss Across Folds: {avg_train_loss:.4f}")
    print(f"Average Validation Loss Across Folds: {avg_val_loss:.4f}")