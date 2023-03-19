# https://leetcode.com/problems/koko-eating-bananas/
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        l = 1
        r = max(piles)

        res = max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            # print(mid)

            temp = 0

            for p in piles:
                temp += math.ceil(p / mid)

            if temp <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res


sol = Solution()
piles = [30,11,23,4,20]
h = 6
sol.minEatingSpeed(piles, h)