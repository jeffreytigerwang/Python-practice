# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 1
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
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1

            nums[r], nums[pointer] = nums[pointer], nums[r]

            if pointer > k:
                return quickSelect(l, pointer - 1)
            elif pointer < k:
                return quickSelect(pointer + 1, r)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)



        # Heap
        # heapq.heapify(nums)
        #
        # while len(nums) > k:
        #     heapq.heappop(nums)

        # return nums[0]
