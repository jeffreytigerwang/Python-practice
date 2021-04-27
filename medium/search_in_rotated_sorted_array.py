class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            print(mid)

            if nums[mid] == target:
                return mid

            if nums[left] == target:
                return left

            if nums[right] == target:
                return right


            if nums[mid] > nums[right]: # e.g. nums = [4,5,6,7,8,1,2,3] target = 8
                if target < nums[mid] and target > nums[right]:
                    right = mid - 1
                    print("A")

                else:
                    left = mid + 1
                    print("B")

            else: # e.g., nums = [5,6,7,1,2,3,4] target = 2
                if target < nums[right] and target > nums[mid]:
                    left = mid + 1
                    print("C")

                else:
                    right = mid - 1
                    print("D")

        return -1


nums = [4,5,6,7,8,1,2,3]
#nums = [1,2,3,4,5,6]

target = 8

answer = Solution()

print(answer.search(nums, target))
