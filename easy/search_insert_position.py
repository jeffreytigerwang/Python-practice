class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l



test1 = Solution()
nums = [1,3,5,6]

position = test1.searchInsert(nums,5)
print(position)