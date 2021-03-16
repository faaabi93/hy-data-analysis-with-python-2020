#!/usr/bin/env python3
from functools import reduce

def sum_equation(L):
    if not L:
        return "0 = 0"

    y = [str(x) for x in L]
    z = " + ".join(y)
    x = str(reduce(lambda x,y:x+y, L, 0))

    y = str(y)

    return z + " = " + x

def main():
    sum_equation([1, 3, 6])

if __name__ == "__main__":
    main()
