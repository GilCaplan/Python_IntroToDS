import pandas as pd
from datetime import datetime

def load_data(path):
    """reads and returns panda dataframe"""
    df = pd.read_csv(path)
    return df

def add_new_columns(df):
    """adds columns to df and returns the new df"""
    df['season_name'] = df['season'].apply(lambda x: ['spring', 'summer', 'fall', 'winter'][x])

    df['Hour'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M:%S").hour)# 0-23
    df['Day'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M:%S").day)# 1-31
    df['Month'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M:%S").month)# 1-12
    df['Year'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M:%S").year)# 2015-17
    return df

