# https://leetcode.com/problems/find-the-difference-of-two-arrays/
from typing import List
from collections import Counter

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []]

        nums1Map = Counter(nums1)
        nums2Map = Counter(nums2)

        res[0] = [i for i in nums1Map if i not in nums2Map]
        res[1] = [i for i in nums2Map if i not in nums1Map]

        return res