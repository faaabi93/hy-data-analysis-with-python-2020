#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, x):
        den = int(self.denominator) * int(x.denominator)
        mult1 = den / self.denominator
        mult2 = den / x.denominator
        num = int(mult1 * int(self.numerator) + mult2 * int(x.numerator))
        return Rational(num, den)

    def __sub__(self, x):
        den = int(self.denominator) * int(x.denominator)
        mult1 = den / self.denominator
        mult2 = den / x.denominator
        num = int(mult1 * int(self.numerator) - mult2 * int(x.numerator))
        return Rational(num, den)

    def __mul__(self, x):
        den = int(self.denominator * x.denominator)
        num = int(self.numerator * x.numerator)
        return Rational(num, den)

    def __truediv__(self, x):
        num = int(self.numerator * x.denominator)
        den = int(self.denominator * x.numerator)
        return Rational(num, den)

    def __eq__(self, x):
        return self.numerator == x.numerator and self.denominator == x.denominator

    def __gt__(self, x):
        den = int(self.denominator) * int(x.denominator)
        mult1 = den / self.denominator
        mult2 = den / x.denominator
        return mult1 * self.numerator > mult2 * self.denominator

    def __lt__(self, x):
        den = int(self.denominator) * int(x.denominator)
        mult1 = den / self.denominator
        mult2 = den / x.denominator
        return mult1 * self.numerator < mult2 * self.denominator

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
