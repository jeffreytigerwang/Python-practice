# https://leetcode.com/problems/last-stone-weight/
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]

        while len(stones) >= 2:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, y - x)

        if not stones:
            return 0

        return -stones[0]