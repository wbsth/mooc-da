#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    mid = int(a.shape[1] / 2)
    b = np.sum(a[:,:mid], 1) > np.sum(a[:,mid:], 1)
    return a[b]

def main():
    pass

if __name__ == "__main__":
    main()
