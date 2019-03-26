import math

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return ComplexNumber(r, i)

    def __mul__(self, other):
        r = self.real*other.real - (self.imaginary*other.imaginary)
        i = self.imaginary*other.real + self.real*other.imaginary
        return ComplexNumber(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return ComplexNumber(r, i)

    def __truediv__(self, other):
        d = (other.real**2 + other.imaginary**2)
        r = (self.real*other.real + self.imaginary*other.imaginary)/d
        i = (self.imaginary*other.real - self.real*other.imaginary)/d
        return ComplexNumber(r, i)

    def __abs__(self):
        return (self.real**2 + self.imaginary**2)**0.5

    def __eq__(self, other):
        return (self.real == other.real) and (self.imaginary == other.imaginary)

    def __repr__(self):
        s = '+' if self.imaginary >= 0 else ''
        return f'<{self.real} {s} {self.imaginary}i>'

    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imaginary)

    def exp(self):
        e = math.e**self.real
        r = e*math.cos(self.imaginary)
        i = e*math.sin(self.imaginary)
        return ComplexNumber(r,i)
