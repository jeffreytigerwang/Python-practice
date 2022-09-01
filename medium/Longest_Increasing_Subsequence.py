from typing import List

# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
class Solution:
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = i + (j - i) // 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size


def main():
    test = Solution()
    nums = [10,9,2,5,3,4]

    print(test.lengthOfLIS(nums))


if __name__ == "__main__":
    main()