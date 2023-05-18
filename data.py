import pandas as pd
from datetime import datetime


def load_data(path):
    """reads and returns panda dataframe"""
    df = pd.read_csv(path)
    return df


def add_new_columns(df):
    """adds columns to df and returns the new df"""
    # 2 Gil
    df['season_name'] = df['season'].apply(lambda x: ['spring', 'summer', 'fall', 'winter'][x])

    # 3 Gil
    df['Hour'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M").hour)# 0-23
    df['Day'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M").day)# 1-31
    df['Month'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M").month)# 1-12
    df['Year'] = df['timestamp'].apply(lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M").year)# 2015-17

    # 4 סייבה

    # 5 Gil
    df['t_diff'] = df.apply(lambda row: row['t1'] - row['t2'], axis=1)
    return df

def data_analysis(df):
    """prints statistics on transformed df"""

    dic = df.to_dict(orient="list")


    # 6 סייבה

    # 7
    # 1. Gil, 5 features (different from each other) that have the highest absolute correlation

    features = df.columns.values
    corr_df = df.drop(columns=['timestamp','season_name']).corr()
    dic = {f1+" "+f2:  corr_df.loc(f1, f2) for f1, f2 in zip(corr_df.columns.values, corr_df.rows.values) if f1!=f2}
    # make dictionary with all feature corr values, need to fix cause doesn't work
    # 2. uhhhh, 5 features (different from each other) that have the lowest absolute correlation
    return dic

