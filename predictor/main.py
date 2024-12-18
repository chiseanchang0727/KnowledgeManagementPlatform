import os
import argparse
import pandas as pd

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Add the project root to PYTHONPATH
from utils.utils import YamlLoader

from predictor.preprocessing.preprocessing import data_preprocessing
from predictor.training.train_module import train

def get_argument():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--data_path', required=False, default='./predictor/data/')
    parser.add_argument('--config_path', required=False, default='configs.yaml', help="Pass the path of configs file.")

    # parser.add_argument('--check', required=False, help="Run 1 epoch to check the whole process is ok.")
    # parser.add_argument('--train', required=False)
    parser.add_argument('--mode', required=False, default=['check', 'train'])
    parser.add_argument('--predict', required=False)

    return parser.parse_args()




def main():

    args = get_argument()

    config_loader = YamlLoader(args.config_path)

    trainig_configs = config_loader.get_training_config()

    df_input = pd.read_csv(os.path.join(args.data_path, trainig_configs.data_config.input_data_name))

    df_preprocessed = data_preprocessing(df_input)
    
    # df_preprocessed.to_csv('./predictor/data/processed_data.csv')

    # train
    train(df_preprocessed, config=trainig_configs, mode=args.mode)
    
    print('end')

if __name__ == "__main__":
    main()