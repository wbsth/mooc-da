#!/usr/bin/env python3

class Rational(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, numb):
        new_denom = int(self.denominator) * int(numb.denominator)
        mult1 = new_denom / self.denominator
        mult2 = new_denom / numb.denominator
        new_nume = int(mult1 * int(self.numerator) + mult2 * int(numb.numerator))
        return Rational(new_nume, new_denom)

    def __sub__(self, numb):
        new_denom = int(self.denominator) * int(numb.denominator)
        mult1 = new_denom / self.denominator
        mult2 = new_denom / numb.denominator
        new_nume = int(mult1 * int(self.numerator) - mult2 * int(numb.numerator))
        return Rational(new_nume, new_denom)

    def __mul__(self, numb):
        #multiplication
        new_denom = int(self.denominator * numb.denominator)
        new_nume = int(self.numerator * numb.numerator)
        return Rational(new_nume, new_denom)

    def __truediv__(self, numb):
        new_nume = int(self.numerator * numb.denominator)
        new_denom = int(self.denominator * numb.numerator)
        return Rational(new_nume, new_denom)

    def __eq__(self, numb):
        return self.numerator == numb.numerator and self.denominator == numb.denominator

    def __gt__(self, numb):
        new_denom = int(self.denominator) * int(numb.denominator)
        mult1 = new_denom / self.denominator
        mult2 = new_denom / numb.denominator
        return mult1 * self.numerator > mult2 * self.denominator

    def __lt__(self, numb):
        new_denom = int(self.denominator) * int(numb.denominator)
        mult1 = new_denom / self.denominator
        mult2 = new_denom / numb.denominator
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
