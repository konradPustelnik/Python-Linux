#!/usr/bin/python3
import random
from multiprocessing import Pool

def creating_fun(size):
    array = []
    for i in range(0, size):
        array.append(random.randint(0, 100))

    histogram = [0] * (size + 1)
    for j in array:
        histogram[j] = histogram[j] + 1
    return histogram

result = Pool().map(creating_fun, (500000,) )

