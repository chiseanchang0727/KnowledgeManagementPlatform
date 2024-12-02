import pandas as pd


def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        return None