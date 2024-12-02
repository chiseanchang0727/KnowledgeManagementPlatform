import os
from dotenv import load_dotenv

load_dotenv()

BASE_DATA_DIR = os.getenv('DATA_DIR')

HISTORICAL_DATA_DIR = os.getenv('HISTORICAL_DATA_DIR')


def check_path_config(base_dir=BASE_DATA_DIR, historical_data_dir=HISTORICAL_DATA_DIR):

    if not base_dir:
        raise ValueError("Base directory (base_dir) is not specified or found in environment variables.")
    if not historical_data_dir:
        raise ValueError("Historical data directory (historical_data_dir) is not specified or found in environment variables.")
    

def get_historical_files_path(data_name, base_dir=BASE_DATA_DIR, historcial_data_dir=HISTORICAL_DATA_DIR):
    check_path_config()
    return os.path.join(base_dir, historcial_data_dir, data_name)