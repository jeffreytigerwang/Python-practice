# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        path = set()
        res = 0

        def dfs(r, c):

            if r < 0 or c < 0 or r >= row or c >= column or grid[r][c] == '0' or (r, c) in path:
                return

            path.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(row):
            for c in range(column):
                if grid[r][c] == '1' and (r, c) not in path:
                    res += 1
                    dfs(r, c)

        return res
