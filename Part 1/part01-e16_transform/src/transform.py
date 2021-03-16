#!/usr/bin/env python3

def transform(s1, s2):
    s1 = list(map(int, s1.split()))
    s2 = list(map(int, s2.split()))
    result = []
    zipped = list(zip(s1, s2))
    result = []
    for i in zipped:
        result.append(i[0] * i[1])
    return result

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
