import numpy as np
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
    # choose k random initial centroids
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

    min_values = new_df.min()
    sum_values = new_df.sum()

    scale_df = (new_df - min_values) / sum_values
    # scale each entry in the df

    return add_noise(np.array(scale_df))


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
    labels = None
    current_centroids = choose_initial_centroids(data, k)

    # loop until prev centroids equal current because that's when we will finish the clustering
    while not np.array_equal(prev_centroids, current_centroids):
        labels = assign_to_clusters(data, current_centroids)

        # set current centroids to previous ones we can check if the algorithm converged.
        prev_centroids = current_centroids
        # find new centroids after calculated new labels for all the datapoints
        current_centroids = recompute_centroids(data, labels, k)

    return labels, current_centroids


def visualize_results(data, labels, centroids, path):
    """
    Visualizing results of the kmeans model, and saving the figure.
    :param data: data as numpy array of shape (n, 2)
    :param labels: the final labels of kmeans, as numpy array of size n
    :param centroids: the final centroids of kmeans, as numpy array of shape (k, 2)
    :param path: path to save the figure to.
    """

    if max(labels) > 5:
        colors = np.random.rand(max(labels)+1, 3)
    else:
        colors = np.array(['purple', 'yellow', 'red', 'blue', 'green', 'grey'])

    label_colors = colors[labels]

    plt.figure(figsize=(8, 8))
    plt.title("Results for kmeans with k = " f'{max(labels)+1}')
    plt.xlabel("cnt")
    plt.ylabel("hum")

    plt.scatter(data.T[0], data.T[1], color=label_colors, s=20)

    for centroid in centroids:
        plt.scatter(centroid[0], centroid[1], color='white', edgecolors='black', s=30, marker='*')

    plt.savefig(path)
    plt.show()


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
    return np.argmin(distance_matrix(data, centroids), axis=1)


def distance_matrix(data, centroids):
    distances = np.empty((data.shape[0], centroids.shape[0]))
    # set empty np array with the current size
    for i in range(data.shape[0]):
        for j in range(centroids.shape[0]):
            # calculate distances between each point to each centroid
            distances[i][j] = dist(data[i], centroids[j])

    return distances


def recompute_centroid(cluster):
    """find centroid for given cluster, sum of all the points divided by the amount of points"""
    return np.sum(cluster, axis=0) / cluster.shape[0]


def get_clusters(data, labels, k):
    """clusters have different sizes therefore a list of np arrays is returned"""
    return [np.array(data[labels == i]) for i in range(k)]


def recompute_centroids(data, labels, k):
    """
    Recomputes new centroids based on the current assignment
    :param data: data as numpy array of shape (n, 2)
    :param labels: current assignments to clusters for each data point, as numpy array of size n
    :param k: number of clusters
    :return: numpy array of shape (k, 2)
    """
    return np.array([recompute_centroid(cluster) for cluster in get_clusters(data, labels, k)])
