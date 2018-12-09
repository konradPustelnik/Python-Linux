#!/usr/bin/python3

result = 0
a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

for i in range(len(a)):
    result = result + a[i] * b[i]

print(result)
