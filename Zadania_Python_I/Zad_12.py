#!/usr/bin/python3
import random

matrix1 = []
matrix2 = []
result = []

for i in range(0, 128):
    matrix1.append([])
    matrix2.append([])
    for j in range(0, 128):
        matrix1[i].append(int(round(random.random()*100)))
        matrix2[i].append(int(round(random.random()*100)))

for i in range(0, 128):
    result.append([])
    for j in range(0, 128):
        result[i].append(matrix1[i][j] + matrix2[i][j])

print(matrix1)
print(matrix2)
print(result)
