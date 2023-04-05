from math import sqrt


# returns the average of the list
def calc_mean(values):
    return sum(values)/len(values)


# returns the stdv
def calc_stdv(values):
    avr = calc_mean(values)
    s = 0
    for val in values:
        s += (val-avr)**2
    return sqrt(s/(len(values)-1))


# returns the Covariance of 2 lists
def calc_covariance(values1, values2):
    if len(values1) != len(values2):
        return 0

    cov = 0

    avr1 = calc_mean(values1)
    avr2 = calc_mean(values2)

    for x, y in zip(values1, values2):
        cov += (x-avr1)*(y-avr2)

    return cov/(len(values1)-1)


def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    print(feature_description, "\n")

    new_dict = {}
    for key in data:
        new_dict[key] = []

    if is_above:
        for i in range(len(data[treatment])):
            if data[treatment][i] > threshold:
                for key in new_dict:
                    new_dict[key].append(data[key][i])

    else:
        for i in range(len(data[treatment])):
            if data[treatment][i] <= threshold:
                for key in new_dict:
                    new_dict[key].append(data[key][i])

    print(statistic_functions[0](new_dict[target]), ", ")
    print(statistic_functions[1](new_dict[target]))
