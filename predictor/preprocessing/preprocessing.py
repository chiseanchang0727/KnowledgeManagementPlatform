import re
import pandas as pd


def change_data_type(input: pd.DataFrame):

    df = input.copy()
    cols = ['Price', 'Open', 'High', 'Low', 'Vol.', 'Change %']

    for col in cols:
        if col == 'Vol.':
            df[col] = df[col].apply(lambda x: float(re.sub('K', '', x))*1000 if x != '-' else 0)
        elif col == 'Change %':
            df[col] = df[col].apply(lambda x: float(re.sub('%', '', x)) /100)
        else:
            df[col] = df[col].apply(lambda x: float(re.sub(',', '', x)))
    return df




def data_preprocessing(raw_data):
    data = raw_data.copy()

    data['Date'] = pd.to_datetime(data['Date'])
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    data['Day'] = data['Date'].dt.day

    data = change_data_type(data)

    data = data.sort_values('Date').reset_index(drop=True)


    data = data.drop('Date', axis=1)

    return data