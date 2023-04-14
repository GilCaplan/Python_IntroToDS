import sys
import data
import statistics as s


def solveq1(london_data):
    print("Question 1:")

    features = ["hum", "t1", "cnt"]

    cov_features = ["t1", "cnt"]
    stat_funcs = [s.calc_mean, s.calc_stdv]
    joint_stat_name = ["Cov(t1, cnt)"]

    print("Summer")

    summer_data = data.filter_by_feature(london_data, "season", [1])[0]
    data.print_details(summer_data, features, stat_funcs)
    data.print_joint_details(summer_data, cov_features, [s.calc_covariance], joint_stat_name)
    print("Holiday: ")
    holiday = data.filter_by_feature(london_data, "is_holiday", [1])[0]
    data.print_details(holiday, features, stat_funcs)
    data.print_joint_details(holiday, cov_features, [s.calc_covariance], joint_stat_name)

    print("All: ")
    data.print_details(london_data, features, stat_funcs)
    data.print_joint_details(london_data, cov_features, [s.calc_covariance], joint_stat_name)
    print()


def solveq2(winter_data):
    print("Question 2: ")
    stat_funcs = [s.calc_mean, s.calc_stdv]

    holiday, non_holiday = data.filter_by_feature(winter_data, "is_holiday", [1])

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
    solveq1(london_data)
    solveq2(data.filter_by_feature(london_data, "season", [3])[0])


if __name__ == '__main__':
    main(sys.argv)

