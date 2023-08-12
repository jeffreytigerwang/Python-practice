# https://leetcode.com/problems/brick-wall/
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        wallDict = {}

        for w in wall:
            temp = 0

            for i in range(len(w) - 1):
                temp += w[i]
                wallDict[temp] = 1 + wallDict.get(temp, 0)

        return len(wall) - max(wallDict.values()) if wallDict else len(wall)



sol = Solution()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
# wall = [[1],[1],[1]]
sol.leastBricks(wall)