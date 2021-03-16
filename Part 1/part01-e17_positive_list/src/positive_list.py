#!/usr/bin/env python3

def is_positive(x):
    if x > 0:
        return True
    else:
        return False

def positive_list(L):
    return list(filter(is_positive, L))

def main():
    pass

if __name__ == "__main__":
    main()
