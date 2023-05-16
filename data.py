import pandas as pd
from datetime import datetime

def load_data(path):
    """reads and returns panda dataframe"""
    df = pd.read_csv(path)
    return df

def add_new_columns(df):
    """adds columns to df and returns the new df"""
    df['season_name'].apply(lambda x: ['spring', 'summer', 'fall', 'winter'][x])

    return df

