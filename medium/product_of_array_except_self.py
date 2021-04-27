class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L, R, res = [0]*len(nums), [0]*len(nums), [0]*len(nums)
        L[0] = 1
        R[len(nums)-1] = 1

        for i in range(1, len(nums)):
            L[i] = L[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            R[i] = R[i+1]*nums[i+1]

        for i in range(0, len(nums)):
            res[i] = L[i]*R[i]
        return res


nums = [1,2,3,4]
answer = Solution()
print(answer.productExceptSelf(nums))
