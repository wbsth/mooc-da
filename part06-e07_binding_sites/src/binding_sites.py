#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
import scipy

from matplotlib import pyplot as plt

import seaborn as sns

sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc


def toint(x):
    """converts a nucleotide to an integer"""
    dictionary = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }
    return dictionary[x]

def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    label = df.loc[:, 'y':]
    feature = df.loc[:, 'X'].apply(lambda x: [toint(a) for a in x])
    feat_final = np.array(feature.tolist())
    return feat_final, label


def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()


def cluster_euclidean(filename):
    features, labels = get_features_and_labels(filename)
    clustering = AgglomerativeClustering(n_clusters=2, affinity='euclidean', linkage='average')
    y_pred = clustering.fit_predict(features, labels)
    permutation = find_permutation(2, labels, y_pred)
    new_labels = [permutation[label] for label in clustering.labels_]
    score = accuracy_score(labels, new_labels)

    return score


def cluster_hamming(filename):
    features, labels = get_features_and_labels(filename)
    distance = pairwise_distances(features, metric='hamming')
    print(distance)
    clustering = AgglomerativeClustering(n_clusters=2, affinity='precomputed', linkage='average')
    y_pred = clustering.fit_predict(distance, labels)
    permutation = find_permutation(2, labels, y_pred)
    new_labels = [permutation[label] for label in clustering.labels_]
    score = accuracy_score(labels, new_labels)

    return score


def main():
    print(cluster_hamming('src/data.seq'))



if __name__ == "__main__":
    main()
