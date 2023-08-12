# https://leetcode.com/problems/largest-number/
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Merge sort approach
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            m = len(nums) // 2
            left = mergeSort(nums[: m])
            right = mergeSort(nums[m:])

            return merge(left, right, nums)

        def merge(left,right, nums):
            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):
                if int(left[i] + right[j]) > int(right[j] + left[i]):
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                nums[k] = left[i]
                k += 1
                i += 1

            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1

            return nums

        mergeSort(nums)

        return str(int(''.join(nums)))



sol = Solution()
nums = [3, 30, 34, 5, 9]

sol.largestNumber(nums)
