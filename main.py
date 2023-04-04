import sys
import data as d
import statistics as s


def solveq1(argv):
    data = d.load_data(argv[1], argv[2])

    summer = d.filter_by_feature(data, "season", data[1])
    features = ["hum", "t1", "cnt"]
    two_features = ["t1", "cnt"]
    stat_funcs = [s.calc_mean, s.calc_stdv]
    print("Summer \n")

    d.print_details(summer, features, stat_funcs)
    print("\n")
    d.print_joint_details(summer, two_features, [s.calc_covariance])
    print("\n")

    holiday = d.filter_by_feature(data, "holiday", data[1])
    print("Holiday: \n")
    d.print_details(holiday, features, stat_funcs)
    print("\n")
    d.print_joint_details(holiday, two_features, [s.calc_covariance])
    print("\n")

    print("All: \n")
    d.print_details(data, features, stat_funcs)
    print("\n")
    d.print_joint_details(data, two_features, [s.calc_covariance])
    print("\n")




def main(argv):
    solveq1(argv)


if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
