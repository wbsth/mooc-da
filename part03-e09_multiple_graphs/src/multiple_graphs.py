#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    x1 = np.array([2,4,6,7])
    y1 = np.array([4,3,5,1])
    x2 = np.array([1,2,3,4])
    y2 = np.array([4,2,3,1])

    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.title('plot')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
if __name__ == "__main__":
    main()
