class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        currMax = 1
        currMin = 1

        for i in nums:
            if i == 0:
                currMax = 1
                currMin = 1
                continue
            temp = currMax
            currMax = max(currMax*i, currMin*i,i)
            currMin = min(temp*i, currMin*i,i)
            res = max(res, currMax)
        return res


answer = Solution()
nums = [-2,3,-4]
print(answer.maxProduct(nums))

