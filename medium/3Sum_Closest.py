from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = float('inf')
        res = float('inf')

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                diff = abs(target - sums)

                if diff == 0:
                    return sums

                if diff < minDiff:
                    minDiff = diff
                    res = sums

                if sums > target:
                    k = k - 1

                if sums < target:
                    j = j + 1

        return res


def main():
    tempList = [-1, 2, 1, -4]
    target = 1

    test = Solution()
    print(test.threeSumClosest(tempList, target))


if __name__ == "__main__":
    main()