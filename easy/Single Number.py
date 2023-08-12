# https://leetcode.com/problems/single-number/
from collections import defaultdict
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # # O(n)
        # dictionary = defaultdict(int)
        #
        # for num in nums:
        #     dictionary[num] += 1
        #
        # for key, value in dictionary.items():
        #     if value == 1:
        #         return key
        #
        # return 0

        # XOR everything --> same value will cancel out, leaving the only result as the res.

        res = 0 # n XOR 0 = n

        for n in nums:
            res ^= n

        return res


def main():
    nums = [2, 2, 1,1,1]
    sol = Solution()
    sol.singleNumber(nums)

if __name__ == "__main__":
    main()