# https://leetcode.com/problems/non-overlapping-intervals/
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[0])
        res = 0
        tempEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < tempEnd:
                # If overlapped, remove the interval that ends later ---> keep the one that ends first by min()
                tempEnd = min(tempEnd, intervals[i][1])
                res += 1
            else:
                tempEnd = intervals[i][1]

        return res

