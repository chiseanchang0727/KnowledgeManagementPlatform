import torch
from torch import nn, optim
from predictor.models.nn import NN
from predictor.config.train_configs import TrainingConfig
from predictor.training.data_loader import DataModule
from predictor.training.utils import set_seed, save_model


def evaluate(df, config: TrainingConfig, mode, save=False):
    set_seed(config.seed)
    
    # full train
    data_module = DataModule(df, config, mode)
    device = torch.device("cuda" if (torch.cuda.is_available() and config.accelerator == "gpu") else "cpu")

    full_train_data_loader = data_module.full_train_data_loader()
    test_loader = data_module.test_loader()
    
    input_size = data_module.full_train_dataset.features.shape[1]
    
    model = NN(
        input_size=input_size,
        hidden_dims=config.model_nn.n_hidden,
        dropouts=config.model_nn.dropout
    ).to(device)
    
    optimizer = optim.Adam(model.parameters(), lr=config.model_nn.lr, weight_decay=config.model_nn.weight_decay)
    
    if config.scheduler.type == 'ReduceLROnPlateau':
        scheular = optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, 
            mode=config.scheduler.mode, 
            factor=config.scheduler.factor, 
            patience=config.scheduler.patience, 
            min_lr=config.scheduler.min_lr
        )
        
    criterion = nn.MSELoss()
    
    print('Full-training start!')
    
    best_test_loss = float('inf')
    no_improvement_epochs = 0
    
    for epoch in range(config.epochs):
        model.train()
        train_loss = 0
        
        for _, (X, y) in enumerate(full_train_data_loader):
            X, y = X.to(device), y.to(device)
            
            optimizer.zero_grad()
            outputs = model(X)
            loss = criterion(outputs, y)        
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            
        avg_train_loss = train_loss / len(full_train_data_loader)
    
        model.eval()
        test_loss = 0
        with torch.no_grad():
            for X, y in test_loader:
                X, y = X.to(device), y.to(device)
                test_outputs = model(X)
                test_loss += criterion(test_outputs, y).item()

        avg_test_loss = test_loss / len(test_loader)
        
        if epoch % 1 == 0:
            print(f"Epoch {epoch+1}/{config.epochs} | Train Loss: {avg_train_loss:.4f} | Test Loss: {avg_test_loss:.4f}")
        
        scheular.step(avg_test_loss)
        
        if avg_test_loss < best_test_loss:
            best_test_loss = avg_test_loss
            no_improvement_epochs = 0
        else:
            no_improvement_epochs += 1
            
        if no_improvement_epochs > config.early_stopping:
            print(f'Early stopping triggered at epoch {epoch+1}')
            break
    
    if save:
        save_model(model, root_path=config.save_path)