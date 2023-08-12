# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0

        average = sum(arr[: k]) / k
        res = 1 if average >= threshold else 0
        l = 0

        for r in range(k, len(arr)):
            temp = (arr[r] - arr[l]) / k
            average += temp
            res += 1 if average >= threshold else 0
            l += 1

        return res

