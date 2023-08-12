# https://leetcode.com/problems/next-greater-element-i/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Need hashmap to track the index of num in nums to avoid using index() function while going through nums2 with a for loop
        nums1Dict = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        # Use stack to achieve O(m +n )
        stack = []

        for i in range(len(nums2)):
            curr = nums2[i]

            while stack and curr > stack[-1]:
                val = stack.pop()
                res[nums1Dict[val]] = curr

            if curr in nums1Dict.keys():
                stack.append(curr)

        return res