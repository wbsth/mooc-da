#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score


def nonconvex_clusters():
    df = pd.read_csv('src/data.tsv', sep='\t')
    features = df.loc[:, ['X1', 'X2']]
    labels = df.iloc[:, -1]
    lab_len = len(set(labels))
    reslist = []

    for i in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=i)
        model.fit(features)
        outliners = 0

        # number of clusters
        n_clusters = len(set(model.labels_))

        # correct number of clusters if outliers are present, count the outliers
        if -1 in model.labels_:
            n_clusters -= 1
            outliners = list(model.labels_).count(-1)

        permutation = find_permutation(n_clusters, labels, model.labels_)
        new_labels = pd.DataFrame([permutation[label] for label in model.labels_]).iloc[:, 0]
        non_outliers_mask = model.labels_ == -1

        if lab_len != n_clusters:
            score = None
        else:
            score = accuracy_score(labels[~non_outliers_mask], new_labels[~non_outliers_mask])

        reslist.append([i, score, n_clusters, outliners])

    df = pd.DataFrame(reslist, columns=['eps', 'Score', 'Clusters', 'Outliers'], dtype=float)
    return df


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
