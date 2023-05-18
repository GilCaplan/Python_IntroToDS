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

    corr_df = df.drop(columns=['timestamp', 'season_name']).corr()
    # gets correlations of columns and put's it in a new df
    features = corr_df.columns.values
    corr_dic = {}
    for i, feature in enumerate(features):
        for x in range(i):
            corr_dic[str(feature) + " " + str(features[x])] = abs(corr_df[feature][features[x]])

    # made dictionary with all correlation values without repeating features, now need to find top 5
    features_sorted = list(sorted(corr_dic.keys(), key=lambda x: corr_dic[x], reverse=True))
    print("max vals: ")
    for i in range(5):
        print(features_sorted[i] + " " + "%.2f" % corr_dic[features_sorted[i]])
    print("min vals")
    for i in range(5):
        j = len(corr_dic) - i - 1
        print(features_sorted[j] + " " + "%.2f" % corr_dic[features_sorted[j]])

    # make dictionary with all feature corr values, need to fix cause doesn't work
    # 2. uhhhh, 5 features (different from each other) that have the lowest absolute correlation
    return dic

