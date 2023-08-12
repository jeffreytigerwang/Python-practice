# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            temp = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = temp

        return arr