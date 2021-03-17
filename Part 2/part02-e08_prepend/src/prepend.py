#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, param):
        self.a = param

    def write(self, s):
        print(self.a + s)


def main():
    p = Prepend("+++ ")
    p.write("Hello")

if __name__ == "__main__":
    main()
