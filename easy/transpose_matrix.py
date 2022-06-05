from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix = [[0] * len(matrix) for i in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == j:
                    newMatrix[i][j] = matrix[i][j]
                else:
                    newMatrix[j][i] = matrix[i][j]

        return newMatrix


def main():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transposeMatrix = Solution()
    print(transposeMatrix.transpose(matrix))


if __name__ == "__main__":
    main()