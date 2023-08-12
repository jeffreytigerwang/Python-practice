# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        path = set()
        tempMax = 0
        res = 0
        row = len(grid)
        column = len(grid[0])
        def dfs(r, c):
            nonlocal tempMax
            if r < 0 or c < 0 or r >= row or c >= column or (r, c) in path or grid[r][c] != 1:
                return
                # return 0

            path.add((r, c))
            tempMax += 1

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

            # return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) to eliminate nonlocal tempMax

        for r in range(row):
            for c in range(column):
                if grid[r][c] == 1 and (r, c) not in path:
                    dfs(r, c)
                    res = max(res, tempMax)
                    tempMax = 0

        return res
