# https://leetcode.com/problems/construct-quad-tree/
from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(row, column, n):
            allSame = True

            for i in range(n):
                for j in range(n):
                    if grid[row][column] != grid[row + i][column + j]:
                        allSame = False
                        break

            if allSame:
                return Node(grid[row][column], True, None, None, None, None)

            n = n // 2
            topLeft = dfs(row, column, n)
            topRight = dfs(row, column + n, n)
            bottomLeft = dfs(row + n, column, n)
            bottomRight = dfs(row + n, column + n, n)

            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(0, 0, len(grid))


