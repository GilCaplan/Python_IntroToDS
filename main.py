import data as dt
import sys


def main(argv):
    london_data = dt.load_data(argv[1])
    df = dt.add_new_columns(london_data)
    dt.data_analysis(df)


if __name__ == '__main__':
    main(sys.argv)
