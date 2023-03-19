from bisect import bisect_left
from typing import List

# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
class Solution:
    def lengthOfLIS(self, nums):
        # # Appraoch 1: https://leetcode.com/problems/longest-increasing-subsequence/solutions/74824/java-python-binary-search-o-nlogn-time-with-explanation/
        # tails = [0] * len(nums)
        # size = 0
        # for x in nums:
        #     i, j = 0, size
        #     while i != j:
        #         m = i + (j - i) // 2
        #         if tails[m] < x:
        #             i = m + 1
        #         else:
        #             j = m
        #     tails[i] = x
        #     size = max(i + 1, size)
        # return size

        # Approach 2: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/

        tempList = []

        for i in range(len(nums)):
            if not tempList or tempList[-1] < nums[i]:
                tempList.append(nums[i])
            else:
                tempIndex = bisect_left(tempList, nums[i])
                tempList[tempIndex] = nums[i]

        return len(tempList)

def main():
    test = Solution()
    nums = [10,9,2,5,3,7,101,18]

    print(test.lengthOfLIS(nums))


if __name__ == "__main__":
    main()