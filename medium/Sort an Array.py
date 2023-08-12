# https://leetcode.com/problems/sort-an-array/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            l = 0
            r = len(nums)
            mid = (l + r) // 2

            leftArray = mergeSort(nums[l: mid])
            rightArray = mergeSort(nums[mid: r])
            print(nums)
            print(leftArray)
            print(rightArray)
            print('')
            return merge(leftArray, rightArray, nums)

        def merge(left, right, nums):
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right[j]
                    j += 1
                    k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

            return nums

        return mergeSort(nums)

class Solution1:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        leftIndex = 0
        rightIndex = len(nums)
        midIndex = leftIndex + (rightIndex - leftIndex) // 2

        left = self.sortArray(nums[leftIndex: midIndex])
        right = self.sortArray(nums[midIndex: rightIndex])
        #
        # print(leftIndex)
        # print(rightIndex)

        return self.mergeTwoSortedArrays(left, right, nums)

    def mergeTwoSortedArrays(self, leftIndex, rightIndex, nums):
        i = 0
        j = 0
        k = 0

        while i < len(leftIndex) and j < len(rightIndex):
            if leftIndex[i] < rightIndex[j]:
                nums[k] = leftIndex[i]
                i = i + 1
            else:
                nums[k] = rightIndex[j]
                j = j + 1

            k = k + 1

        if i < len(leftIndex):
            nums[k:] = leftIndex[i:]

        if j < len(rightIndex):
            nums[k:] = rightIndex[j:]

        return nums


test = [1,4,6,2,843,0]
sol = Solution()
print(sol.sortArray(test))


