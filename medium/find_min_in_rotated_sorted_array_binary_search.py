class Solution(object):
    def findMin(self, nums):
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while nums[left] > nums[right]:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


nums = [2,3,4,1]
answer = Solution()
print(answer.findMin(nums))