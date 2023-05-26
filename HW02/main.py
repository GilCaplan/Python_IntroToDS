import data as dt
import sys
import clustering
import numpy as np

def main(argv):
    print("Part A: ")
    london_data = dt.load_data(argv[1])
    df = dt.add_new_columns(london_data)
    dt.data_analysis(df)

    print("Part B: ")
    df = dt.load_data(argv[1])
    data = clustering.transform_data(df, ["cnt", "hum"])
    # scale data of columns cnt, hum to [0,1]

    for k in [2, 3, 5]:
        print("k = " + str(k))
        labels, centroids = clustering.kmeans(data, k)
        # calculate the labels of each data point & centroids with kmeans
        
        path = r"\home\student\hw2\plots\plot" + str(k) + ".png"
        clustering.visualize_results(data, labels, centroids, path)
        print(np.array_str(centroids, precision=3, suppress_small=True))
        print()


if __name__ == '__main__':
    main(sys.argv)
