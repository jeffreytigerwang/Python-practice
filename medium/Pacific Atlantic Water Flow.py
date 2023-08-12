# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        row = len(heights)
        column = len(heights[0])

        # Instead of going through all r,c in grid, Traverse BACKWARD from the borders of two ocean.
        def dfs(r, c, path, prevHeight):
            if r < 0 or c < 0 or r >= row or c >= column or (r, c) in path or heights[r][c] < prevHeight:
                return

            path.add((r, c))
            dfs(r - 1, c, path, heights[r][c])
            dfs(r + 1, c, path, heights[r][c])
            dfs(r, c - 1, path, heights[r][c])
            dfs(r, c + 1, path, heights[r][c])

        for c in range(column):
            dfs(0, c, pac, 0)   # default value for height
            dfs(row - 1, c, atl, 0)

        for r in range(row):
            dfs(r, 0, pac, 0)
            dfs(r, column - 1, atl, 0)

        res = pac.intersection(atl)

        return list(res)