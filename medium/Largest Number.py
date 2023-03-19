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

            mid = len(nums) // 2

            l = mergeSort(nums[:mid])
            r = mergeSort(nums[mid:])

            return merge(l, r)

        def merge(l, r):
            res = []
            i, j = 0, 0

            while i < len(l) and j < len(r):
                # if int(str(l[i]) + str(r[j])) > int(str(r[j]) + str(l[i])):
                if int(l[i] + r[j]) > int(r[j] + l[i]):
                    res.append(l[i])
                    i += 1
                else:
                    res.append(r[j])
                    j += 1

            while i < len(l):
                res.append(l[i])
                i += 1

            while j < len(r):
                res.append(r[j])
                j += 1

            return res

        res = mergeSort(nums)

        return str(int("".join(map(str, res))))


        # print(mergeSort(nums))


sol = Solution()
nums = [3,30,34,5,9]

sol.largestNumber(nums)

