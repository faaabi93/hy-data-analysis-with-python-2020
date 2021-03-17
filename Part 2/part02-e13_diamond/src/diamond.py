#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a = np.eye(n, dtype=int)
    b = np.fliplr(np.eye(n, n-1, -1, dtype=int))
    c = np.fliplr(np.eye(n-1, n, dtype=int))
    d = np.eye(n-1, n-1, -1, dtype=int)

    top = np.concatenate((b, a), axis=1)
    bottom = np.concatenate((c,d), axis=1)

    return np.concatenate((top, np.flip(bottom)))

def main():
    diamond(3)

if __name__ == "__main__":
    main()
