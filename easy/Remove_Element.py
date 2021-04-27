class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = (value for value in nums if value != val)
        return len(nums)


numbers = [3,2,2,3]
value = 3

print(numbers)
test1 = Solution()
print(test1.removeElement(numbers, value))
