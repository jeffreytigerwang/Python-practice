class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element1 = set(nums)
        map2 = dict.fromkeys(element1, 0)
        for i in nums:
            map2[i] += 1
        return max(map2, key=lambda k: map2[k])


list1 = [1, 2, 2, 2, 3, 4, 5]

answer = Solution()
print(answer.majorityElement(list1))
