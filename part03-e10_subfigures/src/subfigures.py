#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    fig, ax = plt.subplots(1,2)
    ax[0].plot(a[:,0], a[:,1])
    ax[1].scatter(a[:,0], a[:,1], s=a[:,3],c=a[:,2])
    plt.show()

def main():
    a = np.array([[11,3,25,3], [33,14,15,3], [4,6,8,3], [50,50,50,50]])
    subfigures(a)

if __name__ == "__main__":
    main()
