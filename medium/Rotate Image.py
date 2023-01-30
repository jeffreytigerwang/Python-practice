# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def main():
    ans = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans.rotate(matrix)
    print(matrix)


if __name__ == "__main__":
    main()
