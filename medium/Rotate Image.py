# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Approach 1
        # matrix.reverse()
        #
        # for i in range(len(matrix)):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Approach 2 - 1 line?
        # matrix1 = list(zip(*matrix[::-1]))
        #
        # for i in range(len(matrix)):
        #     matrix[i] = matrix1[i]

        # Approach 3 - Easy?
        left = 0
        right = len(matrix) - 1

        while left < right:
            top = left
            bottom = right

            # Can't use left, right - 1 because we will update left and right later, which means left + i does not make sense when rotating
            for i in range(right - left):

                topLeft = matrix[top][left + i]

                # bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # top left to top right
                matrix[top + i][right] = topLeft

            right -= 1
            left += 1

def main():
    ans = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans.rotate(matrix)
    print(matrix)


if __name__ == "__main__":
    main()
