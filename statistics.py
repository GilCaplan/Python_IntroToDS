from math import sqrt


def calc_mean(values=[]):
    avr = 0
    for val in values:
        avr += val
    return avr/len(values)


def calc_stdv(values=[]):
    avr = calc_mean(values)
    s = 0
    for val in values:
        s += (val-avr)**2
    return sqrt(s/(len(values)-1))


def calc_covariance(values1=[], values2=[]):
    if len(values1) != len(values2):
        return 0
    cov = 0

    avr1 = calc_mean(values1)
    avr2 = calc_mean(values2)

    for x, y in zip(values1, values2):
        cov += (x-avr1)*(y-avr2)

    return cov/(len(values1)-1)


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    list = []
    if is_above:
        for key, value in data:
            if key == treatment and data > threshold:
                list.append(value)

    else:
        for key, value in data:
            if key == treatment and data <= threshold:
                list.append(value)
