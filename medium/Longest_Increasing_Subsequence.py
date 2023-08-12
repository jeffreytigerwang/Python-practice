# https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation
class Solution:
    def lengthOfLIS(self, nums):
        # dp = LIS when index = i
        dp = [1] * len(nums)
        # dp[0] = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

def main():
    test = Solution()
    nums = [1,3,6,7,9,4,10,5,6]
    print(test.lengthOfLIS(nums))


if __name__ == "__main__":
    main()