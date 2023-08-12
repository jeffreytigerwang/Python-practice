# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List

# Hashmap - Slow
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numMap = {}

        for index, num in enumerate(nums):
            if num not in numMap:
                numMap[num] = []

            numMap[num].append(index)


        for key in numMap.keys():
            indices = numMap[key]

            for i in range(len(indices) - 1):
                if abs(indices[i] - indices[i + 1]) <= k:
                    return True

        return False


# Sliding window - Fast
class Solution1:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True

            window.add(nums[r])

        return False