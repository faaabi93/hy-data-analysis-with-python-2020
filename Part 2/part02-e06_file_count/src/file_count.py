#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, "r") as file:
        lines = 0
        words = 0
        chara = 0
        for line in file:
            lines += 1
            words += len(line.split())
            chara += len(line)

    return (lines, words, chara)

def main():
    for file in sys.argv[1:]:
        l, w, c = file_count(file)
        print(f"{l}\t{w}\t{c}\t{file}")

if __name__ == "__main__":
    main()
