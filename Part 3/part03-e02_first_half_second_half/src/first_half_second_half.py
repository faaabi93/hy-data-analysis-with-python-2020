#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    # get the middle of the axis = 1
    x = int(a.shape[1] / 2)
    # summing the first half of the columns and comparing them to the second half of the columns
    b = np.sum(a[:, :x], axis = 1) > np.sum(a[:, x:], axis = 1)
    # returning the masked array.
    return a[b]

def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2]])
    print(first_half_second_half(a))

if __name__ == "__main__":
    main()
