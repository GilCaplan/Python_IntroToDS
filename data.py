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
    """
    adds the row in row_index from data to the dictionary
    :param dictionary: given dictionary with keys (strings), values (lists), we are adding values here
    :param data: dictionary with all the data
    :param row_index: the index of the row that we want to use
    :return: dictionary after changes were applied
    """
    for key in dictionary.keys():
        dictionary[key].append(data[key][row_index])
    return dictionary


def filter_by_feature(data, feature, values):
    """
    Function filters the rows from the table (which are located in data) into two new dictionaries, first one if
    the column values in the table (data[feature] which is the column) are located in the given values list, Otherwise
    to the second dictionary.
    :param data: given data with all the information
    :param feature: a column from the table (a key from data)
    :param values: list of values that we want to check against
    :return: data filtered into two dictionaries if data[feature] rows are in values or not
    """
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
    """
    The function prints statistic calculations based on the given features from the data dictionary
    :param data:  containing all data from the table, or a filtered version
    :param features: list of features from the table (key's from data)
    :param statistic_functions: statistic tools that we can use to do different calculations
    :return:
    """
    for feature in features:
        feature_line = feature + ": "

        for stat_function in statistic_functions:
            feature_line += str(round(stat_function(data[feature]), 2)) + ", "

        print(feature_line.rstrip(", "))


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    """
    Function prints calculations based of certain columns together from the table using the statistic tools
    :param data: dictionary containing data from the table or a filtered version.
    :param features: features from the table (key's from data)
    :param statistic_functions: statistic functions used for certain calculations
    :param statistic_functions_names: names of the statistical tools (methods)
    :return:
    """
    values1 = data[features[0]]
    values2 = data[features[1]]

    for stat_name, func in zip(statistic_functions_names, statistic_functions):
        print(stat_name + ": " + "%.2f" % func(values1, values2))
