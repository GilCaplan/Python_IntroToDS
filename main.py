import data as dt
import sys
import clustering
import numpy as np
import time
def main(argv):
    print("Part A: ")
    london_data = dt.load_data(argv[1])
    df = dt.add_new_columns(london_data)
    dt.data_analysis(df)

    print("Part B: ")
    df = dt.load_data(argv[1])
    data = clustering.transform_data(df, ["cnt", "hum"])

    for k in [2, 3, 5]:
        print("k = " + str(k))
        labels, centroids = clustering.kmeans(data, k)

        clustering.visualize_results(data, labels, centroids, r"\home\student\hw2\plots")
        print(np.array_str(centroids, precision=3, suppress_small=True))
        print()


if __name__ == '__main__':
    main(sys.argv)
