import pandas as p


def load_data(path, features):
    """
    Loads data from path with relevant feature columns
    :param path: path to the csv table file
    :param features: relevant columns from the table
    :return: dictionary with keys which are features and the values are lists for each feature (the column)
    """
    df = p.read_cvs(path)
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


def print_details(data, features, statistics_functions):
    for key in data:
        if key in features:
            print(key, ": ")
            print(str(round(statistics_functions[0](data[key]),2)), ", ")
            print(str(round(statistics_functions[1](data[key]), 2)), "\n")


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    values1 = data[features[0]]
    values2 = data[features[1]]

    for stat_name, func in zip(statistic_functions_names, statistic_functions):
        print(stat_name, ": ", str(round(func(values1, values2), 2)))
