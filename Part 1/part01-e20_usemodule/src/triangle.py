# Enter you module contents here
"Module-Docstring"
from math import sqrt

__author__ = "Fabian"
__version__ = "1.0"

def hypothenuse(x, y):
    "returns the hypothenuse"
    z = x**2 + y**2
    return sqrt(z)

def area(x , y):
    "returns the area"
    return 0.5*(x*y)


