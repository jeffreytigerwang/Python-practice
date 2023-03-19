from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            if nums[mid] > target:
                if nums[mid] > nums[r] and nums[r] < target:
                    r = mid - 1
                elif nums[mid] > nums[r] and nums[r] > target:
                    l = mid + 1
                else:
                    r = mid - 1

            if nums[mid] < target:
                if nums[mid] < nums[l] and nums[l] > target:
                    l = mid + 1
                elif nums[mid] < nums[l] and nums[l] < target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1


nums = [4,5,6,7,0,1,2]
#nums = [1,2,3,4,5,6]

target = 3

answer = Solution()

print(answer.search(nums, target))
