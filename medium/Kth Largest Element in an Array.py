# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        #
        # return nums[len(nums) - k]

        # Quick select approach

        k = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            pointer = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    # nums[i], nums[pointer] = nums[pointer], nums[i]
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1

            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer > k:
                return quickSelect(l, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, r)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)