# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Check if newInterval comes before intervals[i]
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]

            # Check if newInterval comes after intervals[i]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # newInterval does not come before or after intervals[i] --> must overlap somewhere
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)

        return res


