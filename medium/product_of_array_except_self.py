class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # length = len(nums)
        # l, r, res = [1] * length, [1] * length, [1] * length
        #
        # for i in range(1, length):
        #     l[i] = l[i - 1] * nums[i - 1]
        #
        # for i in range(length - 2, -1, -1):
        #     r[i] = r[i + 1] * nums[i + 1]
        #
        # for i in range(length):
        #     res[i] = l[i] * r[i]
        #
        # return res

        length = len(nums)

        res = [1] * len(nums)

        # prefix = 1
        for i in range(1, length):
            res[i] = res[i - 1] * nums[i - 1]

        postfix = 1
        for i in range(length - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]


        return res

nums = [1,2,3,4]
answer = Solution()
print(answer.productExceptSelf(nums))
