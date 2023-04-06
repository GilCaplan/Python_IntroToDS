import sys
import data
import statistics


def qst1(london_data):
    print("Question 1:")
    features = ["hum", "t1", "cnt"]
    cov_features = ["t1", "cnt"]

    print("Summer: ")
    summer_data = data.filter_by_feature(london_data, "season", {1})[0]
    data.print_details(summer_data, features, [statistics.calc_mean, statistics.calc_stdv])
    data.print_joint_details(summer_data, cov_features, [statistics.calc_covariance], ["Cov(t1, cnt)"])

    print("Holiday: ")
    holiday_data = data.filter_by_feature(london_data, "is_holiday", {1})[0]
    data.print_details(holiday_data, features, [statistics.calc_mean, statistics.calc_stdv])
    data.print_joint_details(holiday_data, cov_features, [statistics.calc_covariance], ["Cov(t1, cnt)"])

    print("All: ")
    data.print_details(london_data, features, [statistics.calc_mean, statistics.calc_stdv])
    data.print_joint_details(london_data, cov_features, [statistics.calc_covariance], ["Cov(t1, cnt)"])

    print()


def qst2(winter_data):
    print("Question 2:")
    holiday, non_holiday = data.filter_by_feature(winter_data, "is_holiday", {1})
    stat_functions = [statistics.calc_mean, statistics.calc_stdv]

    print("If t1<=13.0, then:")
    statistics.population_statistics("Winter holiday records", holiday, "t1", "cnt", 13.0, False, stat_functions)
    statistics.population_statistics("Winter weekday records", non_holiday, "t1", "cnt", 13.0, False, stat_functions)
    print("If t1>13.0, then:")
    statistics.population_statistics("Winter holiday records", holiday, "t1", "cnt", 13.0, True, stat_functions)
    statistics.population_statistics("Winter weekday records", non_holiday, "t1", "cnt", 13.0, True, stat_functions)


def main(argv):
    # argv.append(r"london.csv")
    # argv.append("hum, t1, cnt, season, is_holiday")
    london_data = data.load_data(argv[1], argv[2].split(", "))
    qst1(london_data)
    qst2(data.filter_by_feature(london_data, "season", {3})[0])


if __name__ == '__main__':
    main(sys.argv)


