import pandas as p


def load_data(path, features):
    df = p.read_cvs(path)
    data = df.to_dict(orient="list")

    # data is a dict: {"cnt":[list], "t1":[list],"is_holiday":[list]}
    data_with_features = {}
    for feature, lis in data:
        if feature in features:
            data_with_features[feature] = lis
    return data_with_features

#path - full path to data
#features - lists of relevant programs that we need


def filter_by_feature(data, feature, values):
    data1, data2 = []
    #set new lists for each feature in the list
    for key in data:
        data1[key] = []
        data2[key] = []
    #loop through each line of data, add to data1 if the value is in values
    #otherwise add to data2
    for i in range(len(data[feature])):#going through the data list line by line
        val = data[feature][i]
        if val in values:
            for key in data1:
                data1[key].add(data[key][i])
        else:
            for key in data2:
                data2[key].add(val)

    return data1, data2


def print_details(data, features, statistics_functions):
    for key in data:
        if key in features:
            for statistic in statistics_functions:
                print(statistic(data[key]), " ")


def print_joint_details(data, features, statistic_functions, statistic_functions_names):
    values1 = data[features[0]]
    values2 = data[features[1]]

    for name, func in zip(statistic_functions_names, statistic_functions):
        print(name, func(values1, values2))
