import pandas as pd


def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        return None
    


def read_txt(file):
    try:
        # if file is a string
        if isinstance(file, str):
            with open(file, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        else:
            # if file is a file
            content = file.read().decode('utf-8', errors='replace')
        return content
    except FileNotFoundError:
        print(f"File not found: {file}")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""
