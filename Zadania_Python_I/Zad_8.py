#!/usr/bin/python3
import random

var = 50

def random_fun(rang, length):
    return random.sample(range(rang), length)

def sort_fun(sort):
    for i in range(var):
        for l in range(var-1):
            if sort[l] < sort[l + 1]:
                tmp = sort[l+1]
                sort[l+1] = sort[l]
                sort[l] = tmp
    return (sort)


random_variables = random_fun(2*var, var)
print(sort_fun(random_variables))
