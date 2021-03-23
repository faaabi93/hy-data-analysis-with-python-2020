#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    # sepal length, sepal width, petal length, petal width
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    data = load()
    sepal_length = data[:, 0]
    petal_length = data[:, 2]
    r, p = scipy.stats.pearsonr(sepal_length, petal_length)
    return r

def correlations():
    data = load()
    r = np.corrcoef(data, rowvar = False)
    return r

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
