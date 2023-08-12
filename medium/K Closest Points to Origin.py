# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        res = []

        for p in points:
            dist.append([(p[0]**2 + p[1]**2)**0.5, p])

        heapq.heapify(dist)

        while k > 0 and dist:
            res.append(heapq.heappop(dist)[1])
            k -= 1

        return res
