#!/usr/bin/env python3

def distinct_characters(L):
    dict = {}
    for i in L:
        dict[i] = len(set(i))

    return dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
