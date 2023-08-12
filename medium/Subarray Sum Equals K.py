# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List

# TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if sum(nums) < k:
            return 0

        res = 0

        for i in range(len(nums)):
            temp = nums[i]

            if temp == k:
                res += 1

            for j in range(i + 1, len(nums)):
                temp += nums[j]

                if temp == k:
                    res += 1

        return res


# Prefix Sum
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumDict = {}
        prefixSumDict[0] = 1
        sum = 0
        res = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum - k in prefixSumDict:
                res += prefixSumDict[sum - k]

            prefixSumDict[sum] = 1 + prefixSumDict.get(sum, 0)

        return res


def main():
    sol = Solution2()
    nums = [1,2,3]
    print(sol.subarraySum(nums, 3))


if __name__ == '__main__':
    main()