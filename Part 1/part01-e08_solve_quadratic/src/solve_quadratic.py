#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    x = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
    y = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)

    return (x,y)


def main():
    pass

if __name__ == "__main__":
    main()
