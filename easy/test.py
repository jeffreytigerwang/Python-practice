from typing import List

matrix = [[1,2,3],[4,5,6]]

print(len(matrix[0]))
print(len(matrix))
print(matrix)

newMatrix = [[0]*len(matrix) for i in range(len(matrix[0]))]

print(newMatrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == j:
            newMatrix[i][j] = matrix[i][j]
        else:
            newMatrix[j][i] = matrix[i][j]

print(newMatrix)