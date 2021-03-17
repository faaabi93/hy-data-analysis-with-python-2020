#!/usr/bin/env python3

import re
import os

def red_green_blue(filename="src/rgb.txt"):
    result = []
    reg = r"(\d+)\s+(\d+)\s+(\d+)\s+(.+)"
    with open(filename, 'r') as f:
        next(f)
        for line in f:
            result.append('\t'.join(re.search(reg, line).groups()))
    return result

def main():
    red_green_blue()

if __name__ == "__main__":
    main()
