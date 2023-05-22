import data as dt
import sys
import clustering
import numpy as np


def main(argv):
    # just to run functions in order to test em :)

    # part 1
    london_data = dt.load_data(argv[1])
    df = dt.add_new_columns(london_data)
    dt.data_analysis(df)

    # part 2
    # idk why they said to read csv file again...
    df = dt.load_data(argv[1])
    data = clustering.transform_data(df, ["cnt", "hum"])

    for k in [2, 3, 5]:
        print("k = " + str(k))
        labels, centroids = clustering.kmeans(data, k)
        clustering.visualize_results(data, labels, centroids, None)
        print(np.array_str(centroids, precision=3, suppress_small=True))


if __name__ == '__main__':
    main(sys.argv)
