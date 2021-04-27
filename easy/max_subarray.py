class Solution:
    def maxSubArray(self, nums):

        # Solution1:
        maxSub = nums[0]
        curM = 0

        for i in nums:
            curM = curM + i
            if curM < i:
                curM = i

            maxSub = max(maxSub, curM)
            print(maxSub)

        return maxSub

        # # Solution2:
        # maxSub, curSum = nums[0], 0
        #
        # for n in nums:
        #     if curSum < 0:
        #         curSum = 0
        #     curSum += n
        #     maxSub = max(maxSub, curSum)
        # return maxSub


list1 = [2,-99,100]

answer = Solution()
print(answer.maxSubArray(list1))