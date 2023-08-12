# https://leetcode.com/problems/number-of-zero-filled-subarrays/
from typing import List



class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        zeroMap = {}    # key = length; val = frequency
        tempCount = 0
        sum = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                tempCount += 1
            else:
                if tempCount != 0:
                    zeroMap[tempCount] = 1 + zeroMap.get(tempCount, 0)
                    tempCount = 0

        if tempCount != 0:
            zeroMap[tempCount] = 1 + zeroMap.get(tempCount, 0)

        for n in zeroMap.keys():
            sum += (n * (n + 1) // 2) * zeroMap[n]

        return sum


def main():
    sol = Solution()
    nums = [1, 3, 0, 0, 2, 0, 0, 4]
    sol.zeroFilledSubarray(nums)


if __name__ == "__main__":
    main()