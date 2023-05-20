import data as dt
import sys
import clustering


def main(argv):
    # just to run functions in order to test em :)
    london_data = dt.load_data(argv[1])
    df = dt.add_new_columns(london_data)
    dt.data_analysis(df)
    info = clustering.transform_data(df, ['t1', 't2'])


if __name__ == '__main__':
    main(sys.argv)
