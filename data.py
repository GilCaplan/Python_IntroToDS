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
    df['Hour'] = df['timestamp'].apply(lambda x: get_time(x).hour)
    df['Day'] = df['timestamp'].apply(lambda x: get_time(x).day)
    df['Month'] = df['timestamp'].apply(lambda x: get_time(x).month)
    df['Year'] = df['timestamp'].apply(lambda x: get_time(x).year)

    # 4 סייבה

    # 5 Gil
    df['t_diff'] = df.apply(lambda row: row['t1'] - row['t2'], axis=1)
    return df


def get_time(x):
    return datetime.strptime(x, "%d/%m/%Y %H:%M")


def data_analysis(df):
    """prints statistics on transformed df"""

    dic = df.to_dict(orient="list")
    # 6 סייבה

    # 7
    # Gil, 5 features (different from each other) that have the highest/lowest absolute correlation
    corr_df = df.drop(columns=['timestamp', 'season_name']).corr()
    # gets correlations of columns and put's it in a new df
    features = corr_df.columns.values
    y = lambda feature, x: abs(corr_df[feature][features[x]])
    corr_dic = {f'({feature}, {features[x]})': y(feature, x) for i, feature in enumerate(features) for x in range(i)}

    # corr_dic = {} # erase this if you think the previous two liner is good uhhh
    # for i, feature in enumerate(features):# shortened to one line
    #     for x in range(i):
    #         corr_dic['('+str(feature) + ", " + str(features[x])+')'] = abs(corr_df[feature][features[x]])

    # made dictionary with all correlation values without repeating features, now need to find top 5
    features_sorted = list(sorted(corr_dic.keys(), key=lambda x: corr_dic[x], reverse=True))
    print("Highest correlated are:")
    for i in range(5):
        print(features_sorted[i] + " with " + "%.2f" % corr_dic[features_sorted[i]])
    print("Lowest correlated are:")
    for i in range(5):
        j = len(corr_dic) - i - 1
        print(features_sorted[j] + " with " + "%.2f" % corr_dic[features_sorted[j]])

    # 8. uhhhh
    return dic

