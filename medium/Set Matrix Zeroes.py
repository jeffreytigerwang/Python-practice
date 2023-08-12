# https://leetcode.com/problems/set-matrix-zeroes/submissions/943473012/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        column = len(matrix[0])
        path = set()

        for r in range(row):
            for c in range(column):
                if matrix[r][c] == 0:
                    path.add((r, c))

        while path:
            r, c = path.pop()
            matrix[r] = [0 for i in range(column)]

            for i in range(row):
                matrix[i][c] = 0


def main():
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]

    sol.setZeroes(matrix)

if __name__ == "__main__":
    main()
