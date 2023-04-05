import sys
import data as d
import statistics as s


def solveq1(argv):
    data = d.load_data(argv[1], argv[2])

    summer = d.filter_by_feature(data, "season", data[1])
    holiday = d.filter_by_feature(data, "holiday", data[1])

    features = ["hum", "t1", "cnt"]
    two_features = ["t1", "cnt"]
    stat_funcs = [s.calc_mean, s.calc_stdv]
    joint_stat_name = "Cov(t1, cnt)"

    print("Summer \n")

    d.print_details(summer, features, stat_funcs)
    print("\n")
    d.print_joint_details(summer, two_features, [s.calc_covariance], joint_stat_name)
    print("\n")

    print("Holiday: \n")
    d.print_details(holiday, features, stat_funcs)
    print("\n")
    d.print_joint_details(holiday, two_features, [s.calc_covariance], joint_stat_name)
    print("\n")

    print("All: \n")
    d.print_details(data, features, stat_funcs)
    print("\n")
    d.print_joint_details(data, two_features, [s.calc_covariance], joint_stat_name)
    print("\n")


def solveq2(argv):
    data = d.load_data(argv[1], argv[2])

    features = ["t1", "cnt"]
    stat_funcs = [s.calc_mean, s.calc_stdv]

    winter = d.filter_by_feature(data, "season", 3)
    holiday, weekday = d.filter_by_feature(winter, "is_holiday", [1])

    print("If t1<=13.0, then:\n")
    s.population_statistics("Winter holiday records:", winter, "t1", "cnt", 13, False, stat_funcs)
    s.population_statistics("Winter weekday records:", winter, "t1", "cnt",13, False, stat_funcs)
    print("If t1>13.0, then:\n")
    s.population_statistics("Winter holiday records:", winter, "t1", "cnt", 13, True, stat_funcs)
    s.population_statistics("Winter weekday records:", winter, "t1", "cnt", 13, True, stat_funcs)



def main(argv):
    # your_path = "C:\Users\USER\PycharmProjects\pythonProject"
    solveq1(argv)
    solveq2(argv)


if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
