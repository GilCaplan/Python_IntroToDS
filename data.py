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


def copy_row(data1, data, row_index):
    for key in data1.keys():
        data1[key].append(data[key][row_index])


def filter_by_feature(data, feature, values):
    data1 = {}
    data2 = {}

    for key in data.keys():
        data1[key] = []
        data2[key] = []

    for i, value in enumerate(data[feature]):
        if value in values:
            copy_row(data1, data, i)
        else:
            copy_row(data2, data, i)

    return data1, data2


def print_details(data, features, statistics_functions):
    for key in data:
        if key in features:
            print(key, ": ")
            print(str(round(statistics_functions[0](data[key]), 2)), ", ")
            print(str(round(statistics_functions[1](data[key]), 2)), "\n")


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    values1 = data[features[0]]
    values2 = data[features[1]]

    for stat_name, func in zip(statistic_functions_names, statistic_functions):
        print(stat_name, ": ", str(round(func(values1, values2), 2)))
