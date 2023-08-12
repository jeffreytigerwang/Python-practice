# https://leetcode.com/problems/fruit-into-baskets/
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        l = 0
        fruitsMap = {}
        total = 0

        while l <= len(fruits) - res:
            r = l

            while r < len(fruits):
                if fruits[r] in fruitsMap or len(fruitsMap) < 2:
                    fruitsMap[fruits[r]] = 1 + fruitsMap.get(fruits[r], 0)
                    r += 1
                    total += 1
                    res = max(res, total)

                else:
                    fruitsMap[fruits[l]] -= 1
                    total -= 1
                    if fruitsMap[fruits[l]] <= 0:
                        del fruitsMap[fruits[l]]

                    l += 1

            l += 1

        return res


sol = Solution()
fruits = [1,2,3,2,2]
sol.totalFruit(fruits)
