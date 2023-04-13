from math import sqrt
from data import filter_by_feature, print_details


def calc_mean(values):
    return sum(values) / len(values)


def calc_stdv(values):
    mean = calc_mean(values)
    return sqrt(sum(map(lambda x: (x - mean) ** 2, values)) / (len(values) - 1))


def calc_covariance(values1, values2):
    mean1 = calc_mean(values1)
    mean2 = calc_mean(values2)

    return sum(map(lambda x: (x[0] - mean1) * (x[1] - mean2), list(zip(values1, values2)))) / (len(values1) - 1)


def population_statistics(feature_desc, data, trt, trg, thr, is_abv, stats_funcs):
    """
       Prints statistical information on filtered data above/under threshold of treatment,
       according to the target feature
       :param feature_desc: string which describes the feature
       :param data: dictionary where keys are the features and values are lists of values of the features
       :param trt: name of a feature, treatment
       :param trg: name of a feature, target
       :param thr: critical value of the treatment feature, threshold
       :param is_abv: indicates if we need rows that are above or under the threshold with respect to treatment, above
       :param stats_funcs: list of statistical functions
       :return:
    """

    fd = dict((k, [x for i, x in enumerate(data[k]) if not (is_abv ^ (data[trt][i] > thr))]) for k in data.keys())
    print(feature_desc + "\n" + trg + ": " + "%.2f" % stats_funcs[0](fd[trg]) + ", %.2f" % stats_funcs[1](fd[trg]))
