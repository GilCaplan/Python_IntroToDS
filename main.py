import data as dt
import sys


def main(argv):
    london_data = dt.load_data(argv[1])
    dt.add_new_columns(london_data)


if __name__ == '__main__':
    main(sys.argv)
