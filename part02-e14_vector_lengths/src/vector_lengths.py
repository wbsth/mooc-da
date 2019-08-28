#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt((a**2).sum(axis=1))

def main():
    test_array = np.array([[1,2,3], [4,5,6]])
    vector_lengths(test_array)

if __name__ == "__main__":
    main()
