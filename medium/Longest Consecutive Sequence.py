# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        nums.sort()
        maxLength = 1
        tempLength = 1
        for i in range(len(nums) - 1):

            if nums[i] + 1 == nums[i + 1]:
                # print(nums[i])
                tempLength = tempLength + 1
                maxLength = max(maxLength, tempLength)
            elif nums[i] == nums[i + 1]:
                continue
            else:
                tempLength = 1

        # print(nums)
        # print(maxLength)

        return maxLength


def main():
    sol = Solution()
    nums = [0,3,7,2,5,8,4,6,0,1]
    sol.longestConsecutive(nums)

if __name__ == "__main__":
    main()
