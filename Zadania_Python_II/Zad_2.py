#!/usr/bin/python3
import math

class complex_number:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag
        self.z = complex(real, imag)

    def add(self, z1, z2):
        return complex(z1.real + z2.real, z1.imag + z2.imag)

    def remove(self, z1, z2):
        return complex(z1.real - z2.real, z1.imag - z2.imag)

    def abs(self):
        return math.sqrt(pow(self.real, 2) + pow(self.imag, 2))


z1 = complex_number(3, 5)
z2 = complex_number(2, -10)

print(z1.add(z1, z2))
print(z1.remove(z1, z2))
print(z2.add(z2, z1))
print(z2.remove(z2, z1))
print(z1.abs())
print(z2.abs())
