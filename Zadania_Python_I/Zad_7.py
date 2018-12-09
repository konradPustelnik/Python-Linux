#!/usr/bin/python3
import math

def quadratic_fun(a,b,c):
    a = int(a)
    b = int(b)
    c = int(c)

    delta = b*b - 4*a*c

    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("The equation has 2 elements:", x1, x2)
    elif delta == 0:
        x0 = (-b)/(2*a)
        print("The equation has 1 element:", x0)
    else:
        print("The equation has not any element.")
    
a, b, c = input("Enter the factors of quadratic function: ").split()
quadratic_fun(a,b,c)
