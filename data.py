import pandas


def load_data(path, features):
    """
    Loads data from path with relevant feature columns
    :param path: path to the csv table file
    :param features: relevant columns from the table
    :return: dictionary with keys which are features and the values are lists for each feature (the column)
    """
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")

    for key in data.copy():
        if key not in features:
            data.pop(key)

    return data


def add_row(dictionary, data, row_index):
    for key in dictionary.keys():
        dictionary[key].append(data[key][row_index])
    return dictionary


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}

    for key in data.keys():
        data1[key] = []
        data2[key] = []

    for i, value in enumerate(data[feature]):
        if value in values:
            data1 = add_row(data1, data, i)
        else:
            data2 = add_row(data2, data, i)

    return data1, data2


def print_details(data, features, statistic_functions):
    for feature in features:
        feature_line = feature + ": "

        for stat_function in statistic_functions:
            feature_line += str(round(stat_function(data[feature]), 2)) + ", "

        print(feature_line.rstrip(", "))


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    values1 = data[features[0]]
    values2 = data[features[1]]

    for stat_name, func in zip(statistic_functions_names, statistic_functions):
        print(stat_name + ": " + "%.2f" % func(values1, values2))
