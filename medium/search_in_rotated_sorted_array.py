from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            print(l, r, mid)

            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1


        return -1

nums = [3,1]
#nums = [1,2,3,4,5,6]

target = 1

answer = Solution()

print(answer.search(nums, target))
