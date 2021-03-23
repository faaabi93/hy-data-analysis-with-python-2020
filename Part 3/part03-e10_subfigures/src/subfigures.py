#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def subfigures(a):
    x = a[:, 0]
    y = a[:, 1]
    c = a[:, 2]
    s = a[:, 3]

    fig, ax = plt.subplots(1, 2)
    ax[0].plot(x, y)
    ax[1].scatter(x, y, c=c, s=s)
    plt.show()

def main():
    a = np.array([[11,3,25,3], [33,14,15,3], [4,6,8,3], [50,50,50,50]])
    subfigures(a)

if __name__ == "__main__":
    main()
