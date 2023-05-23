import pandas as pd
from datetime import datetime


def load_data(path):
    """reads and returns panda dataframe"""
    df = pd.read_csv(path)
    return df


def add_new_columns(df):
    """adds columns to df and returns the new df"""

    df['season_name'] = df['season'].apply(lambda x: ['spring', 'summer', 'fall', 'winter'][x])

    df['Hour'] = df['timestamp'].apply(lambda x: get_time(x).hour)
    df['Day'] = df['timestamp'].apply(lambda x: get_time(x).day)
    df['Month'] = df['timestamp'].apply(lambda x: get_time(x).month)
    df['Year'] = df['timestamp'].apply(lambda x: get_time(x).year)

    df['is_weekend_holiday'] = df.apply(lambda row: 2 * row['is_holiday'] + row['is_weekend'], axis=1)

    df['t_diff'] = df.apply(lambda row: row['t2'] - row['t1'], axis=1)

    return df


def get_time(x):
    """ returns datatime object by dd/mm/yyyy H:M"""
    return datetime.strptime(x, "%d/%m/%Y %H:%M")


def data_analysis(df):
    """prints statistics on transformed df"""

    print("describe output:")
    print(df.describe().to_string())
    print()
    print("corr output:")
    corr = df.drop(columns=['timestamp', 'season_name']).corr()
    print(corr.to_string())
    print()

    # 5 features (different from each other) that have the highest/lowest absolute correlation
    # gets correlations of columns between feature to feature and places it in corr_dic
    features = corr.columns.values
    corr_dic = {(f1, f2): abs(corr[f1][f2]) for i, f2 in enumerate(features) for f1 in features[:i]}
    # made dictionary with all correlation values without repeating features.

    # sort the dictionary from biggest to smallest
    features_sorted = sorted(corr_dic.keys(), key=lambda x: corr_dic[x], reverse=True)

    print("Highest correlated are: ")
    for i in range(5):
        print(str(i+1) + ". " + str(features_sorted[i]) + " with " + "%.6f" % corr_dic[features_sorted[i]])
    print()

    print("Lowest correlated are: ")
    for i in range(5):
        print(str(i+1) + ". " + str(features_sorted[-1-i]) + " with " + "%.6f" % corr_dic[features_sorted[-1-i]])
    print()

    seasons = df.groupby('season_name')

    for season in seasons:
        print(season[0] + " average t_diff is " + "%.2f" % season[1]['t_diff'].mean())

    print("All average t_diff is " + "%.2f" % df['t_diff'].mean())
    print()
