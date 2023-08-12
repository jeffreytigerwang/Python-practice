# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        recDict = {}    # key = ratio
        res = 0

        for r in rectangles:
            key = r[0] / r[1]
            recDict[key] = 1 + recDict.get(key, 0)

        # sum = (n/2) * (first_term + last_term); n = 4, first term = 4
        # for val in recDict.values():
        #     res += ((val - 1) / 2) * val

        # OR - number of permutation where n = 4, k = 2

        for val in recDict.values():
            res += (val * (val - 1)) // 2

        return res
