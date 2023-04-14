from math import sqrt


def calc_mean(values):
    """
    Function calculates the mean (average)
    :param values: list of numbers
    :return: mean value
    """
    return sum(values) / len(values)


def calc_stdv(values):
    """
    Function returns the stdv calculation result from the given list (values)
    """
    return sqrt(sum(map(lambda x: (x-calc_mean(values))**2, values)) / (len(values)-1))


def calc_covariance(values1, values2):
    """
    Function returns the covariance calculation between the lists values1 and values2
    :param values1: first list of values, numbers
    :param values2: second list of values, numbers
    :return: Covariance calculation between values1 to values2
    """
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values2)

    return sum(map(lambda x: (x[0] - mean1) * (x[1] - mean2), list(zip(values1, values2)))) / (len(values1) - 1)


def population_statistics(feature_des, data, treatment, target, threshold, is_above, statistic_functions):
    """
       Prints statistical information on filtered data above/under threshold of treatment,
       according to the target feature
       :param feature_des: string which describes the feature
       :param data: dictionary where keys are the features and values are lists of values of the features
       :param treatment: name of a feature
       :param target: name of a feature
       :param threshold: critical value of the treatment feature
       :param is_above: indicates if we need rows that are above or under the threshold with respect to treatment
       :param statistic_functions: list of statistical functions
       :return:
       """
    f = dict((k, [x for i, x in enumerate(data[k]) if not (is_above ^ (data[treatment][i] > threshold))]) for k in data)
    print(feature_des + "\n" + target + ": %.2f, %.2f" % tuple(statistic_functions[i](f[target]) for i in [0, 1]))
