import sys
import data
import statistics as s


def solve_q1(london_data):
    print("Question 1:")

    # lists that we use when calling data/statistic functions since we reuse the same values when calling the functions
    features = ["hum", "t1", "cnt"]
    cov_features = ["t1", "cnt"]
    stat_funcs = [s.calc_mean, s.calc_stdv]
    joint_stat_name = ["Cov(t1, cnt)"]

    print("Summer")

    # filters data into a new dictionary where season has the value 1 (represents summer)
    summer_data = data.filter_by_feature(london_data, "season", [1])[0]
    data.print_details(summer_data, features, stat_funcs)
    data.print_joint_details(summer_data, cov_features, [s.calc_covariance], joint_stat_name)

    print("Holiday: ")

    # filters data into a new dictionary where holiday has the value 1 (represents holiday)
    holiday = data.filter_by_feature(london_data, "is_holiday", [1])[0]
    data.print_details(holiday, features, stat_funcs)
    data.print_joint_details(holiday, cov_features, [s.calc_covariance], joint_stat_name)

    print("All: ")
    data.print_details(london_data, features, stat_funcs)
    data.print_joint_details(london_data, cov_features, [s.calc_covariance], joint_stat_name)
    print()


def solve_q2(winter_data):
    print("Question 2: ")

    # list of two statistic functions that are needed to be used
    stat_funcs = [s.calc_mean, s.calc_stdv]

    # filter winter_data by "is holiday" feature into two dictionaries such that holiday where the value in "is_holiday"
    # is 1, and in non_holiday is 0
    holiday, non_holiday = data.filter_by_feature(winter_data, "is_holiday", [1])

    # filter holiday and non_holiday into new dictionaries, so we only have the columns t1 and cnt (which are relevant)
    hol_cnt1 = {feature: holiday[feature] for feature in ["t1", "cnt"]}
    non_hol_cnt1 = {feature: non_holiday[feature] for feature in ["t1", "cnt"]}

    print("If t1<=13.0, then:")
    s.population_statistics("Winter holiday records", hol_cnt1, "t1", "cnt", 13, False, stat_funcs)
    s.population_statistics("Winter weekday records", non_hol_cnt1, "t1", "cnt", 13, False, stat_funcs)

    print("If t1>13.0, then:")
    s.population_statistics("Winter holiday records", hol_cnt1, "t1", "cnt", 13, True, stat_funcs)
    s.population_statistics("Winter weekday records", non_hol_cnt1, "t1", "cnt", 13, True, stat_funcs)


def main(argv):
    london_data = data.load_data(argv[1], argv[2].split(", "))

    # solves q1 according to given instructions
    solve_q1(london_data)

    # solves q2 according to given instructions
    solve_q2(data.filter_by_feature(london_data, "season", [3])[0])


if __name__ == '__main__':
    main(sys.argv)

