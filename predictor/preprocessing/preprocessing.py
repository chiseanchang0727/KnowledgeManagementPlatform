import re
import pandas as pd
from sklearn.preprocessing import StandardScaler

def clean_data(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    cols = ['Price', 'Open', 'High', 'Low', 'Vol.', 'Change %']

    for col in cols:
        if col == 'Vol.':
            df[col] = df[col].apply(lambda x: float(re.sub('K', '', x)) * 1000 if x != '-' else 0)
        elif col == 'Change %':
            df[col] = df[col].apply(lambda x: float(re.sub('%', '', x)) / 100)
        else:
            df[col] = df[col].apply(lambda x: float(re.sub(',', '', x)))
    
    return df



def feature_engineering(input_df: pd.DataFrame) -> pd.DataFrame:
    df = input_df.copy()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    # add lag feature
    
    return df

def scale_data(input_df: pd.DataFrame) -> pd.DataFrame:
    """Scale numeric features using StandardScaler."""
    df = input_df.copy()
    scaler = StandardScaler()

    # Select numeric columns for scaling
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df

def data_preprocessing(raw_data: pd.DataFrame) -> pd.DataFrame:
    data = feature_engineering(raw_data)
    
    data = clean_data(data)

    data = data.sort_values('Date').reset_index(drop=True)
    
    data = data.drop('Date', axis=1)

    data = scale_data(data)

    return data
