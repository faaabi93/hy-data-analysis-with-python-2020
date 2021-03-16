#!/usr/bin/env python3

import math

def triangle(base, height):
    return base * height * 0.5

def rectangle(width, height):
    return width * height

def circle(radius):
    return math.pi * radius ** 2

def main():
    # enter you solution here
    while True:
        userinput = input("Coose a shape (triangle, rectangle, circle) ")
        if userinput == "":
            break
        if userinput == "triangle":
            base = int(input("Give base of the triangle "))
            height = int(input("Give height of the triangle "))
            print(f"The area is {triangle(base, height):.4f}")
        elif userinput == "rectangle":
            width = int(input("Give width of the rectangle "))
            height = int(input("Give height of the rectangle "))
            print(f"The area is {rectangle(width, height):.4f}")
        elif userinput == "circle":
            radius = int(input("Give radius of the circle "))
            print(f"The area is {circle(radius):.4f}")
        else:
            print("Unknown shape!")
if __name__ == "__main__":
    main()
