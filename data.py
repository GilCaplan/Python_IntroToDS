import pandas


def load_data(path, features):
    """
    Loads data from path with relevant feature columns

    :param path: path to the csv table file
    :param features: relevant columns from the table
    :return: dictionary with keys that are from features and values are lists for each row
    """

    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")

    for key in data.copy():
        if key not in features:
            data.pop(key)

    return data


def transfer_row(data1, data2, row_index):
    for key in data1.keys():
        data2[key].append(data1[key].pop(row_index))


def filter_by_feature(data, feature, values):
    data1 = dict(data)
    data2 = {}

    for key in data.keys():
        data2[key] = []

    for i, value in enumerate(data[feature]):
        if value in values:
            transfer_row(data1, data2, i)

    return data1, data2


def print_details(data, features, statistic_functions):
    for feature in features:
        feature_line = feature + ": "

        for stat_function in statistic_functions:
            feature_line += str(stat_function(data[feature])) + ", "

        print(feature_line.rstrip(", "))


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    for stat_name, stat_function in zip(statistic_functions_names, statistic_functions):
        print(stat_name + ": " + str(stat_function(data[features[0]], data[features[1]])))
