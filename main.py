import sys
import data as d
import statistics as s


def solveq1(argv):
    data = d.load_data(argv[1], argv[2])

    summer = d.filter_by_feature(data, "season", data[1])
    features = ["hum", "t1", "cnt"]
    two_features = ["t1", "cnt"]
    stat_funcs = [s.calc_mean, s.calc_stdv]
    stat_funcs_name = ["calc_mean", "calc_stdv"]
    print("Summer \n")

    d.print_details(summer, features, stat_funcs)
    print("\n")
    d.print_joint_details(summer, two_features, [s.calc_covariance], stat_funcs_name)
    print("\n")

    holiday = d.filter_by_feature(data, "holiday", data[1])
    print("Holiday: \n")
    d.print_details(holiday, features, stat_funcs)
    print("\n")
    d.print_joint_details(holiday, two_features, [s.calc_covariance], stat_funcs_name)
    print("\n")

    print("All: \n")
    d.print_details(data, features, stat_funcs)
    print("\n")
    d.print_joint_details(data, two_features, [s.calc_covariance], stat_funcs_name)
    print("\n")


def solveq2(argv):
    data = d.load_data(argv[1], argv[2])

    features = ["t1", "cnt"]
    stat_funcs = [s.calc_mean, s.calc_stdv]

    winter = d.filter_by_feature(data, "season", 3)
    holiday, weekday = d.filter_by_feature(winter, "is_holiday", [1])

    print("If t1<=13.0, then:\n Winter holiday records: \n")
    print("cnt: ", d.print_details(holiday, features, stat_funcs))

    print("Winter weekly records: \n")
    print("cnt: ", d.print_details(weekday, features, stat_funcs))

    print("If t1>13.0, then:\n Winter holiday records:\n")
    print("cnt: ", d.print_details(holiday, features, stat_funcs))

    print("Winter weekly records: \n")
    print("cnt: ", d.print_details(weekday, features, stat_funcs))
    pass


def main(argv):
    solveq1(argv)
    solveq2(argv)


if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
