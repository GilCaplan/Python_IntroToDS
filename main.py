import sys
import data as d
import statistics as s


def solveq1(argv):
    data = d.load_data(argv[1], argv[2])

    summer = d.filter_by_feature(data, "season", data[1])

    print("Summer \n")

    d.print_details(summer, ["hum", "t1", "cnt"], [s.calc_mean, s.calc_stdv])
    print("\n")
    d.print_joint_details(summer, ["t1", "cnt"], [s.calc_covariance])
    print("\n")

    holiday = d.filter_by_feature(data, "holiday", data[1])
    print("Holiday: \n")
    d.print_details(holiday, ["hum", "t1", "cnt"], [s.calc_mean, s.calc_stdv])
    print("\n")
    d.print_joint_details(holiday, ["t1", "cnt"], [s.calc_covariance])
    print("\n")




def main(argv):
    solveq1(argv)


if __name__ == '__main__':
    main(sys.argv)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
