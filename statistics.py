from math import sqrt
from data import filter_by_feature, print_details


def calc_mean(values):
    return sum(values) / len(values)


def calc_stdv(values):
    mean = calc_mean(values)
    return sqrt(sum(map(lambda x: (x-mean)**2), values) / (len(values)-1))


def calc_covariance(values1, values2):
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values2)

    return sum(map(lambda x: (x[0] - mean1) * (x[1] - mean2), list(zip(values1, values2)))) / (len(values1) - 1)


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    """
       Prints statistical information on filtered data above/under threshold of treatment, according to the target feature
       :param feature_description: string which describes the feature
       :param data: dictionary where keys are the features and values are lists of values of the features
       :param treatment: name of a feature
       :param target: name of a feature
       :param threshold: critical value of the treatment feature
       :param is_above: indicates if we need rows that are above or under the threshold with respect to treatment
       :param statistic_functions: list of statistical functions
       :return:
       """
    values = {x for x in data[treatment] if (is_above and x > threshold) or x <= threshold}
    data1, data2 = filter_by_feature(data, treatment, values)

    print(feature_description, end=":\n")
    print_details(data1, [target], statistic_functions)
