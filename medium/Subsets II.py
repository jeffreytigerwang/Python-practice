from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(nums, path):
            res.append(path[:])

            for i in range(len(nums)):
                if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                    path.append(nums[i])
                    backtracking(nums[i + 1:], path)
                    path.pop()

            return

        backtracking(nums, [])
        return res

def main():
    nums = [1, 2, 2]

    sol = Solution()
    print(sol.subsetsWithDup(nums))


if __name__ == "__main__":
    main()
