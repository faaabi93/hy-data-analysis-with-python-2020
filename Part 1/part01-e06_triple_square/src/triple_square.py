#!/usr/bin/env python3

def triple(x):
        return x*3

def square(x):
    return x**2

def main():
    for i in range(1, 10):
        x = triple(i)
        y = square(i)
        if x < y:
            break
        print("triple({})=={} square({})=={}".format(i, x, i, y))

if __name__ == "__main__":
    main()
