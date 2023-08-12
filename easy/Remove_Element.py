# https://leetcode.com/problems/remove-element/
class Solution:
    def removeElement(self, nums, val):
        # # Short
        # nums[::] = [num for num in nums if num != val]
        # return len(nums)

        res = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1

        return res


numbers = [3,2,2,3]
value = 3

print(numbers)
test1 = Solution()
print(test1.removeElement(numbers, value))
