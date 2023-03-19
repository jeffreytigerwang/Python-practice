# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m = len(matrix)
        # n = len(matrix[0]) - 1
        #
        # for row in range(m):
        #     if matrix[row][0] <= target <= matrix[row][-1]:
        #         l = 0
        #         r = n
        #
        #         while l <= r:
        #             mid = l + (r - l) // 2
        #
        #             if matrix[row][mid] == target:
        #                 return True
        #             elif matrix[row][mid] < target:
        #                 l = mid + 1
        #             else:
        #                 r = mid - 1
        #
        # return False


        m = len(matrix)
        n = len(matrix[0]) - 1

        begin = 0
        end = m - 1
        midRow = 0

        while begin <= end:
            midRow = begin + (end - begin) // 2

            if matrix[midRow][0] > target:
                end = midRow - 1
            elif matrix[midRow][-1] < target:
                begin = midRow + 1
            else:
                break

        if begin > end:
            return False

        l = 0
        r = n

        while l <= r:
            midColumn = l + (r - l) // 2

            if matrix[midRow][midColumn] == target:
                return True
            elif matrix[midRow][midColumn] < target:
                l = midColumn + 1
            else:
                r = midColumn - 1

        return False