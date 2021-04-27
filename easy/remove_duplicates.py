class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution1
        temp = []

        for num in nums:
            if num not in temp:
                temp.append(num)

        nums[:] = (temp[i] for i in range(0, len(temp)))

        return len(nums)

        # # Solution2
        #
        # curr = 0
        #
        # for i in range(1, len(nums)):
        #     if nums[curr] != nums[i]:
        #         curr += 1
        #         nums[curr] = nums[i]
        #     return curr+1


nums = [1, 1, 2]
answer = Solution()
print(answer.removeDuplicates(nums))
