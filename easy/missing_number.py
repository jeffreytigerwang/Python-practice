from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(0, len(nums)):
            if i != nums[i]:
                return i

        return len(nums)


def main():
    nums = [0, 1]
    missingNumber = Solution()
    print(missingNumber.missingNumber(nums))


if __name__ == "__main__":
    main()