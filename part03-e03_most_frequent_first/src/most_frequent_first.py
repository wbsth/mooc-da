#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    # getting unique values from sorting column
    uniq = np.unique(a[:,c], axis = 0, return_counts=True)
    uniq_values,uniq_count = uniq
    count_sorted_ind = np.argsort(-uniq_count)
    # getting sorting column values sorted by their numb of occurencies
    val_sorted_by_count = uniq_values[count_sorted_ind].reshape((1,-1))
    # getting array of indexes of that sorted array
    indxs = np.concatenate([np.where((a[:,c] == x))[0] for x in np.nditer(val_sorted_by_count)])
    return a[indxs]

def main():
    pass

if __name__ == "__main__":
    main()
