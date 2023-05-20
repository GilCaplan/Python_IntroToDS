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

    df['t_diff'] = df.apply(lambda row: row['t1'] - row['t2'], axis=1)
    return df


def get_time(x):
    return datetime.strptime(x, "%d/%m/%Y %H:%M")


def data_analysis(df):
    """prints statistics on transformed df"""

    dic = df.to_dict(orient="list")
    # 6 סייבה
    print("describe output:")
    print(df.describe().to_string())
    print()
    print("corr output:")
    corr = df.corr()
    print(corr.to_string())
    print()

    # 7
    # Gil, 5 features (different from each other) that have the highest/lowest absolute correlation
    corr_df = df.drop(columns=['timestamp', 'season_name']).corr()
    # gets correlations of columns and put's it in a new df
    features = corr_df.columns.values
    y = lambda feature, x: abs(corr_df[feature][features[x]])
    # I think in recommendation they meant to make (feature, features[x]) ?
    key = lambda feature, x: f'({feature}, {features[x]})'
    corr_dic = {key(feature, x): y(feature, x) for i, feature in enumerate(features) for x in range(i)}

    # made dictionary with all correlation values without repeating features, now need to find top 5
    features_sorted = list(sorted(corr_dic.keys(), key=lambda x: corr_dic[x], reverse=True))
    print("Highest correlated are:")
    for i in range(5):
        print(features_sorted[i] + " with " + "%.6f" % corr_dic[features_sorted[i]])
    print("Lowest correlated are:")
    for i in range(5):
        j = len(corr_dic) - i - 1
        print(features_sorted[j] + " with " + "%.6f" % corr_dic[features_sorted[j]])

    seasons = df.groupby('season_name')

    for season in seasons:
        print(season[0] + " average t_diff is " + "%.2f" % season[1]['t_diff'].mean())

    print("All average t_diff is " + "%.2f" % df['t_diff'].mean())
