# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(0, len(nums)-1):
        #     # print(i)
        #     for j in range(i+1, len(nums)):
        #         # print(j)
        #         if nums[i] + nums[j] == target:
        #
        #             return [i,j]

        # Value : Index
        dict_p = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict_p:
                return [dict_p[diff], i]
            dict_p[n] = i

        return




nums = [3,4]
target = 7
answer = Solution()
print(answer.twoSum(nums, target))