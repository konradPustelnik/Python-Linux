#!/usr/bin/python3
import random

size = 8
matrix1 = []
matrix2 = []
result = []

for i in range(0, size):
    matrix1.append([])
    matrix2.append([])
    for j in range(0, size):
        matrix1[i].append(int(round(random.random()*100)))
        matrix2[i].append(int(round(random.random()*100)))

result = [[0 for x in range(size)] for y in range(size)]
for i in range(len(matrix1)):
   for j in range(len(matrix2[0])):
       for k in range(len(matrix2)):
           result[i][j] += matrix1[i][k] * matrix2[k][j]

for i in matrix1:
   print(i)

for i in matrix2:
   print(i)

for i in result:
   print(i)
