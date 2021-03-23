#!/usr/bin/env python3
import numpy as np
from functools import reduce
import math

def matrix_power(a, n):
    if n == 0:
        return np.eye(a.shape[0], dtype=int)
    else:
        x = (a for i in range(abs(n)))
        function = lambda x,y : x@y
        multiplicated = reduce(function, x)
        if n > 0:
            return multiplicated
        else:
            return np.linalg.inv(multiplicated)

def main():
    a = np.array([[0,1], [-1,0]])
    print(matrix_power(a, -3))

if __name__ == "__main__":
    main()