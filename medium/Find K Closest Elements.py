# https://leetcode.com/problems/find-k-closest-elements/description/

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        minDiff = float('inf')
        minIndex = 0

        while l <= r:
            mid = (r - l) // 2 + l

            if arr[mid] == x:
                minIndex = mid
                break
            elif arr[mid] < x:
                if abs(arr[mid] - x) <= minDiff:
                    minIndex = mid
                    minDiff = abs(arr[mid] - x)

                l += 1
            else:
                if abs(arr[mid] - x) < minDiff:
                    minIndex = mid
                    minDiff = abs(arr[mid] - x)
                r -= 1

        l, r = minIndex, minIndex

        # we use r + 1 and l - 1 to check for next value as the current value is already included
        # we use k - 1 because minIndex is already included
        for i in range(k - 1):
            if l == 0:
                r += 1
            elif r < len(arr) - 1 and abs(arr[r + 1] - x) < abs(arr[l - 1] - x):
                r += 1
            else:
                l -= 1

        return arr[l: r + 1]



sol = Solution()
array = [1,2,4,5]
k = 1
x = 3

sol.findClosestElements(array, k, x)