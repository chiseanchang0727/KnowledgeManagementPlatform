import os
import argparse
import pandas as pd
from utils.utils import YamlLoader
from predictor.preprocessing.preprocessing import data_preprocessing

def get_argument():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--data_path', required=False, default='./predictor/data/')
    parser.add_argument('--config', required=True, default='configs.yaml', help="Pass the path of configs file.")

    parser.add_argument('--check', required=False, help="Run 1 epoch to check the whole process is ok.")
    parser.add_argument('--train', required=False)
    parser.add_argument('--inference', required=False)

    return parser.parse_args()




def main():

    args = get_argument()

    config_loader = YamlLoader(args.config)

    model_nn_config = config_loader.get_model_nn_config()

    df_input = pd.read_csv(args.data_path, config_loader.config_data['futuredataname'])

    df_preprocessed = data_preprocessing(df_input)


    
    
    
    # train






if __name__ == "__main__":
    main()