#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    print(image.shape)
    multiplicators = [0.2126, 0.7152, 0.0722]
    grayscaled = np.sum(multiplicators * image, axis = 2)
    return grayscaled

def to_red(image):
    multiplicators = [1, 0, 0]
    return image * multiplicators

def to_green(image):
    multiplicators = [0, 1, 0]
    return image * multiplicators

def to_blue(image):
    multiplicators = [0, 0, 1]
    return image * multiplicators

def main():
    painting=plt.imread('src/painting.png')
    fig, ax = plt.subplots(3,1)
    ax[0].imshow(to_red(painting))
    ax[1].imshow(to_green(painting)) 
    ax[2].imshow(to_blue(painting))
    plt.show()

    greyscaled = to_grayscale(painting)
    plt.imshow(greyscaled)
    plt.gray()
    plt.show()

if __name__ == "__main__":
    main()
