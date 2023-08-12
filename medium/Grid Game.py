# https://leetcode.com/problems/grid-game/
from typing import List

# With prefix sum
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefixSum1 = grid[0].copy()
        prefixSum2 = grid[1].copy()
        res = float('inf')

        for i in range(1, n):
            prefixSum1[i] += prefixSum1[i - 1]
            prefixSum2[i] += prefixSum2[i - 1]

        for i in range(n):
            topSum = prefixSum1[-1] - prefixSum1[i]
            botSum = prefixSum2[i - 1] if i > 0 else 0

            # Second robot wants to maximize
            secondBot = max(topSum, botSum)

            # First robot wants to minimize
            res = min(res, secondBot)

        return res

# Without prefix sum - TLE
class Solution2:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = float('inf')

        for i in range(n):
            topSum = sum(grid[0][i + 1:])
            botSum = sum(grid[1][0: i])
            secondBot = max(topSum, botSum)

            # First robot wants to minimize
            res = min(res, secondBot)

        return res

sol = Solution()
grid = [[3,3,1],[8,5,2]]
print(sol.gridGame(grid))