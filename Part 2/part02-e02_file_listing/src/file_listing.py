#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    reg = r'(\d+)\s+(\w+)\s+(\d+)\s+(\d+):(\d+)\s(.+)'
    with open(filename, 'r') as f:
        for i in f:
            size, month, day, hour, minute, filename = re.search(reg, i).groups()
            result.append((int(size), month, int(day), int(hour), int(minute), filename))
    return result    


def main():
    pass

if __name__ == "__main__":
    main()