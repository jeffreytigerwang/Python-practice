# https://leetcode.com/problems/car-fleet/description/
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort()

        stack = []

        for p, s in reversed(pair):
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

