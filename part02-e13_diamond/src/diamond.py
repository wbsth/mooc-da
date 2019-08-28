#!/usr/bin/env python3

import numpy as np

def diamond(n):
    q1 = np.fliplr(np.eye(n, dtype = int))
    q2 = np.eye(n, n-1, k = -1, dtype = int)
    q3 = np.eye(n-1, n, k = 1, dtype = int)
    q4 = np.fliplr(np.eye(n-1, k = 1, dtype = int))

    upper = np.concatenate((q1, q2), axis = 1)
    lower = np.concatenate((q3, q4), axis = 1)
    return (np.concatenate((upper, lower)))

def main():
    pass

if __name__ == "__main__":
    main()
