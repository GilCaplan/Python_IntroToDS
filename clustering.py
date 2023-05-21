import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(2)


def add_noise(data):
    """
    :param data: dataset as numpy array of shape (n, 2)
    :return: data + noise, where noise~N(0,0.001^2)
    """
    noise = np.random.normal(loc=0, scale=0.001, size=data.shape)
    return data + noise


def choose_initial_centroids(data, k):
    """
    :param data: dataset as numpy array of shape (n, 2)
    :param k: number of clusters
    :return: numpy array of k random items from dataset
    """
    n = data.shape[0]
    initial_centroids = np.random.choice(range(n), k, replace=False)
    return data[initial_centroids]


def transform_data(df, features):
    """
    Performs the following transformations on df:
        - selecting relevant features
        - scaling
        - adding noise
    :param df: dataframe as was read from the original csv.
    :param features: list of 2 features from the dataframe
    :return: transformed data as numpy array of shape (n, 2)
    """
    new_df = df[features]
    #  make a new data frame with only the features given
    #  we need to read csv file again for new df

    x_min = [min(new_df[feature]) for feature in features]
    x_sum = [sum(new_df[feature]) for feature in features]
    # get min and sum for each column

    scale = lambda x, i: (x - x_min[i]) / x_sum[i]
    # scale numbers in columns using lambda expression, where I being the index

    new_df[features[0]].apply(lambda x: scale(x, 0))
    new_df[features[1]].apply(lambda x: scale(x, 1))

    # adding noise to data here?
    return np.array(new_df)


def distance_matrix(data, centroids):
    distances = np.empty((data.shape[0], centroids.shape[0]))
    # ill leave it like that or until ill find a way to abuse broadcasting of numpy

    # btw we don't need to go through the whole table because we know the table is symmetrical

    for i in range(data.shape[0]):
        for j in range(centroids.shape[0]):
            distances[i][j] = dist(data[i], centroids[j])

    return distances


def compute_centroid(cluster):
    return np.sum(cluster, axis=0) / cluster.shape[0]


def compute_centroids(clusters):
    return np.array([compute_centroid(cluster) for cluster in clusters])


def assign_labels(data, centroids):
    return np.argmin(distance_matrix(data, centroids), axis=1)


def get_clusters(data, labels, k):
    # clusters have different sizes therefore I made it a list of np arrays
    return [np.array(data[labels == i]) for i in range(k)]


def kmeans(data, k):
    """
    Running kmeans clustering algorithm.
    :param data: numpy array of shape (n, 2)
    :param k: desired number of cluster
    :return:
    * labels - numpy array of size n, where each entry is the predicted label (cluster number)
    * centroids - numpy array of shape (k, 2), centroid for each cluster.
    """

    prev_centroids = None
    current_centroids = choose_initial_centroids(data, k)

    while not np.array_equal(prev_centroids, current_centroids):
        labels = assign_labels(data, current_centroids)
        prev_centroids = current_centroids
        current_centroids = compute_centroids(get_clusters(data, labels, k))

    return labels, current_centroids


def visualize_results(data, labels, centroids, path):
    """
    Visualizing results of the kmeans model, and saving the figure.
    :param data: data as numpy array of shape (n, 2)
    :param labels: the final labels of kmeans, as numpy array of size n
    :param centroids: the final centroids of kmeans, as numpy array of shape (k, 2)
    :param path: path to save the figure to.
    """
    colors = ['red', 'blue', 'green', 'grey', 'yellow']
    x = np.linspace(min(data[1]), max(data[1]), 200)
    # can change afterward to what we need

    plt.plot(*x)
    plt.title("Results for kmeans with k = " f'{max(labels)}')
    # maybe -1 of we count from 0 and not 1 ? can check when we test the code
    plt.xlabel("cnt")
    plt.ylabel("hum")

    for i, label in enumerate(labels):
        plt.scatter(data[i][0], data[i][1], c=colors[label])

    for centroid in centroids:
        plt.scatter(centroid[0], centroid[1], c='black', s=20, marker='X')

    plt.show()
    plt.savefig(path)


def dist(x, y):
    """
    Euclidean distance between vectors x, y
    :param x: numpy array of size n
    :param y: numpy array of size n
    :return: the Euclidean distance
    """

    return np.sqrt(np.sum(np.power(x-y, 2)))


def assign_to_clusters(data, centroids):
    """
    Assign each data point to a cluster based on current centroids
    :param data: data as numpy array of shape (n, 2)
    :param centroids: current centroids as numpy array of shape (k, 2)
    :return: numpy array of size n
    """
    pass
    # return labels


def recompute_centroids(data, labels, k):
    """
    Recomputes new centroids based on the current assignment
    :param data: data as numpy array of shape (n, 2)
    :param labels: current assignments to clusters for each data point, as numpy array of size n
    :param k: number of clusters
    :return: numpy array of shape (k, 2)
    """
    
    pass
    # return centroids
