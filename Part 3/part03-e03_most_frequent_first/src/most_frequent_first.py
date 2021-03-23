#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    # unique values and their counts in two seperate arrays
    unique = np.unique(a[:,c], axis = 0, return_counts=True)
    # one-dimensional arrays
    unique_values,unique_count = unique
    # get sorted array of values in order of their occurences
    count_sorted_idx = np.argsort(-unique_count)
    # getting sorted column values sorted by their number of occurences
    values_sorted_by_count = unique_values[count_sorted_idx].reshape((1,-1))
    # getting an array of indexes of that sorted array
    idxs = np.concatenate([np.where((a[:,c] == x))[0] for x in np.nditer(values_sorted_by_count)])
    return a[idxs]


def main():
    a = np.array(
        [[5, 0, 1, 2, 3],
         [1, 2, 3, 4, 5],
         [2, 4, 6, 8, 9],
         [2, 5, 7, 3, 9],
         [9, 5, 6, 9, 5],
         [6, 3, 9, 4, 8]]
    )
    most_frequent_first(a, -1)

if __name__ == "__main__":
    main()
