#!/usr/bin/env python3

import sys
import statistics

def summary(filename):
    with open(filename, "r") as f:
        numbers = []
        for line in f:
            try: 
                numbers.append(float(line))
            except:
                pass
    sm = sum(numbers)
    avg = statistics.mean(numbers)
    stdev = statistics.stdev(numbers)
    return (sm,avg,stdev)

def main():
    files = sys.argv[1:]
    for i in files:
        sm, av, std = summary(i)
        print(f"File: {i} Sum: {sm:.6f} Average: {av:.6f} Stddev: {std:.6f}")

if __name__ == "__main__":
    main()
