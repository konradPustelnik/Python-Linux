#!/usr/bin/python3
import random

tmp = 4
max_value = 9

size = random.randint(0, tmp)

matrix = [[random.randint(0, max_value) for x in range(size)] for y in range(size)]
print(matrix)

def determinant(matrix, one):
    column = len(matrix)
    if column == 1:
        score = one * matrix[0][0]
        return score
    else:
        score = 0
        sign = -1
        for i in range(column):
            m = []
            for j in range(1, column):
                tmp = []
                for k in range(column):
                    if k != i:
                        tmp.append(matrix[j][k])
                m.append(tmp)
            sign *= -1
            score += one * determinant(m, sign * matrix[0][i])
        return score

print(determinant(matrix, 1))
